#!/usr/bin/env python3
"""F1 v1.1/v1.2 interpreter-path tests (binding, REPL pipe mode, interpret_auto). They need a live oracle (TAU_ORACLE_HOST or TAU_PODMAN=1) and are
skipped otherwise. Each case is an IDNI README example or the defect that v1.1 fixed."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
try:
    import pytest
    skip = pytest.mark.skipif(not (os.environ.get("TAU_ORACLE_HOST") or os.environ.get("TAU_PODMAN")), reason="no oracle transport")
except ImportError:  # plain python3 runner
    pytest = None
    def skip(f): return f


def _o():
    from tau_oracle import OracleV1
    return OracleV1()


@skip
def test_no_input_steps_report_outputs():
    r = _o().interpret("o1[t] = 1.", [{}, {}, {}])
    assert r["error"] is None
    assert r["output_series"] == {"o1": ["T", "T", "T"]}
    assert all(s["step_returned_none"] for s in r["steps"])  # the v1 defect, now harmless


@skip
def test_readme_copy_example():
    r = _o().interpret("o[t] = i[t].", [{"i": "T"}, {"i": "F"}, {"i": "T"}])
    assert r["output_series"] == {"o": ["T", "F", "T"]}


@skip
def test_readme_update_example_revisions():
    r = _o().interpret("u[t] = i1[t].", [{"i1": "o1[t] = 1"}, {"i1": "o2[t] = 0 && o2[t] = 1"}, {"i1": "o1[t] = 0"}])
    revs = [s["spec_revision"] for s in r["steps"]]
    assert revs == [1, 1, 2]              # accepted, rejected (unsat), accepted-and-revised
    assert r["steps"][1]["outputs"]["u"] == "F"


# ---------- F1 v1.2: interpret_auto (binding for bare specs, REPL for declared/annotated streams) ----------

@skip
def test_auto_readme_copy_example_uses_binding():
    r = _o().interpret_auto("o[t] = i[t].", [{"i": "T"}, {"i": "F"}, {"i": "T"}])
    assert r["error"] is None and r["path"] == "binding"
    assert r["output_series"] == {"o": ["T", "F", "T"]}
    assert r["output_series_raw"] == {"o": ["T", "F", "T"]}


@skip
def test_auto_accumulator_with_sbf_declarations():
    spec = "i1 : sbf := in console. o1 : sbf := out console. always o1[t] = i1[t] | o1[t-1]"
    r = _o().interpret_auto(spec, [{"i1": "0"}, {"i1": "1"}, {"i1": "0"}, {"i1": "0"}])
    assert r["error"] is None and r["path"] == "repl"
    # lookback: step 0 is unconstrained (no input requested, solver's free choice); from step 1 the
    # input is consumed; once o1[t-1] = 1 the REPL stops asking for i1 (it no longer matters)
    assert r["steps"][0]["given"] == {}
    assert r["steps"][1]["given"] == {"i1": "1"}
    assert r["output_series"]["o1"][1:] == ["T", "T", "T"]
    assert r["output_series_raw"]["o1"][1:] == ["1", "1", "1"]      # sbf prints 0/1, normalised to F/T
    assert "Execution step: 3" in r["tau_stdout"]


@skip
def test_auto_two_input_sbf_conjunction():
    spec = "i1 : sbf := in console. i2 : sbf := in console. o1 : sbf := out console. always o1[t] = i1[t] & i2[t]"
    steps = [{"i1": "1", "i2": "1"}, {"i1": "T", "i2": "F"}, {"i1": "0", "i2": "0"}]   # T/F on an sbf stream is converted to 1/0
    r = _o().interpret_auto(spec, steps)
    assert r["error"] is None and r["path"] == "repl"
    assert r["output_series"] == {"o1": ["T", "F", "F"]}
    assert r["output_series_raw"] == {"o1": ["1", "0", "0"]}
    assert [s["given"] for s in r["steps"]] == [{"i1": "1", "i2": "1"}, {"i1": "1", "i2": "0"}, {"i1": "0", "i2": "0"}]


@skip
def test_auto_equivalence_with_sbf_annotations():
    # `<->` joins formulas, not terms: `o1[t]:sbf <-> i1[t]:sbf` is a syntax error in 3badb21
    r = _o().interpret_auto("always (o1[t]:sbf = 1 <-> i1[t]:sbf = 1)", [{"i1": "1"}, {"i1": "0"}, {"i1": "1"}])
    assert r["error"] is None and r["path"] == "repl"
    assert r["output_series"] == {"o1": ["T", "F", "T"]}


@skip
def test_auto_falls_back_when_the_binding_crashes():
    # forced onto the binding, an sbf stream fed "T" segfaults (exit 139): interpret_auto must notice and rerun via the REPL
    r = _o().interpret_auto("always o1[t]:sbf = i1[t]:sbf", [{"i1": "T"}, {"i1": "F"}], prefer="binding")
    assert r["path"] == "repl-after-binding-crash"
    assert r["fallback"]["from"] == "binding" and r["fallback"]["returncode"] == 139
    assert r["error"] is None and r["output_series"] == {"o1": ["T", "F"]}


@skip
def test_repl_reports_unsat_and_syntax_errors():
    o = _o()
    r = o.interpret_repl("always (o1[t] = 0 && o1[t] = 1)", [{}, {}])
    assert r["error"] and "unsat" in r["error"] and r["output_series"] == {}
    r = o.interpret_repl("always o1[t]:sbf <-> i1[t]:sbf", [{"i1": "1"}])
    assert r["error"] and "Syntax Error" in r["error"]


def test_norm_bool_and_stream_types_offline():
    from tau_oracle import OracleV1
    assert [OracleV1.norm_bool(x) for x in ("1", "0", "T", "F", "T.", "x")] == ["T", "F", "T", "F", "T", "x"]
    t = OracleV1.stream_types("i1 : sbf := in console. i2 := in console. o_pot : tau := out console. s : bv[8] := in file(\"a\"). always o1[t]:sbf = i1[t]")
    assert t == {"i1": "sbf", "i2": "tau", "o_pot": "tau", "s": "bv[8]", "o1": "sbf"}
    assert OracleV1.needs_repl("i1 : sbf := in console. always o1[t] = i1[t]")
    assert OracleV1.needs_repl("always o1[t]:sbf = i1[t]:sbf")
    assert not OracleV1.needs_repl("o[t] = i[t].")


if __name__ == "__main__":
    if not (os.environ.get("TAU_ORACLE_HOST") or os.environ.get("TAU_PODMAN")):
        print("skipped: no oracle transport"); sys.exit(0)
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok", name)


def test_repl_output_regex_accepts_padded_names():
    """The REPL aligns the ':=' column, so a shorter output name is followed by several spaces (found 2026-09-29
    on the step 2 reference check: only the longest-named output was collected)."""
    from tau_oracle import OracleV1
    m1 = OracleV1._RE_OUT.match("o_consensus[0]           := T")
    m2 = OracleV1._RE_OUT.match("o_finality_declarable[0] := T")
    assert m1 and m1.groups() == ("o_consensus", "0", "T")
    assert m2 and m2.groups() == ("o_finality_declarable", "0", "T")


@skip
def test_output_lookback_needs_initial_conjunct_per_output():
    """Measured 2026-09-29 (step 2 run, consensus_logic): when o2[t] refers to o1[t-1], step 0 of o1 is left to the solver
    and the REPL asks no inputs at step 0, even though o1[t] itself has no lookback. Giving o1 its own [0] conjunct fixes it."""
    d = "i_q : tau := in console. i_b : tau := in console. o1 : tau := out console. o2 : tau := out console. "
    steps = [{"i_q": "T", "i_b": "F"}, {"i_q": "T", "i_b": "F"}, {"i_q": "T", "i_b": "T"}]
    bare = d + "always (o1[t] = i_q[t] & i_b[t]' && o2[0] = 0 && o2[t] = o1[t] & o1[t-1])"
    fixed = d + "always (o1[0] = i_q[0] & i_b[0]' && o1[t] = i_q[t] & i_b[t]' && o2[0] = 0 && o2[t] = o1[t] & o1[t-1])"
    o = _o()
    rb, rf = o.interpret_repl(bare, steps), o.interpret_repl(fixed, steps)
    assert rb["steps"][0]["given"] == {} and rb["output_series"]["o1"][0] == "F"
    assert rf["steps"][0]["given"] and rf["output_series"]["o1"] == ["T", "T", "F"] and rf["output_series"]["o2"] == ["F", "T", "F"]


@skip
def test_tau_valued_output_compares_by_normal_form():
    """Curriculum row 5: a tau-typed output holding a specification prints as its normalised formula; the driver compares
    it with an expected `{ spec } : tau` constant through `normalize` (measured 2026-09-29 on the box)."""
    o = _o()
    spec = ("i : tau := in console. o : tau := out console. always ((i[t] != 0 -> o[t] = { always o1[t] = i1[t] } : tau) "
            "&& (i[t] = 0 -> o[t] = { always o1[t] = i1[t]' } : tau))")
    r = o.interpret_repl(spec, [{"i": "T"}, {"i": "F"}])
    got = r["output_series_raw"]["o"]
    assert o.tau_equal(got[0], "{ always o1[t] = i1[t] } : tau")
    assert o.tau_equal(got[1], "{ always o1[t] = i1[t]' } : tau")
    assert not o.tau_equal(got[0], got[1])
