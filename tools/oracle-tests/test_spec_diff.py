#!/usr/bin/env python3
"""Tests for tools/spec_diff.py v1 (F3). Run with
    python3 -m pytest -q tools/oracle-tests/test_spec_diff.py
or, without pytest,
    python3 tools/oracle-tests/test_spec_diff.py
No oracle is needed: the cases exercise the parser and the syntactic classification only."""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from spec_diff import canon, conjuncts, diff, parse, render  # noqa: E402

# the G09 record (tools/oracle-tests/g09-revision/result.json): initial_spec and steps[1].current_spec, verbatim
G09_BEFORE = ("always u[t]:tau = i_upd[t]:tau && (o_priority_sewage[t]:tau != 0 || i_river_polluted[t]:tau = 0) && "
              "(o_priority_sewage[t]:tau != 0 || o_endorse[t]:tau = 0) && (o_ask_accountability[t]:tau != 0 || i_sewage_contracted[t]:tau = 0)")
G09_AFTER = ("(always u[t]:tau = i_upd[t]:tau && (o_ask_accountability[t]:tau != 0 || i_sewage_contracted[t]:tau = 0)) && "
             "((always o_priority_sewage[t]:tau = 0 && o_endorse[t]:tau = 0 && i_river_polluted[t]:tau = 0) || (always o_priority_sewage[t]:tau = 0))")
RESIDENT = "always i_river_polluted[t] = 0 || o_priority_sewage[t] != 0"
ENGINEER = "always i_sewage_contracted[t] = 0 || o_ask_accountability[t] != 0"
ADMIN = "always o_endorse[t] = 0 || o_priority_sewage[t] != 0"


def by_clause(rep):
    return {c["clause"]: c for c in rep["clauses"]}


def test_kept_and_dropped_readme_minimal_example():
    # faculties.md F3 minimal test: README step 2, running spec requires o1[t] = 1, update o1[t] = 0
    rep = diff("always o1[t] = 1", "always o1[t] = 0")
    assert rep["dropped"] == ["always o1[t] = 1"]
    assert rep["added"] == ["always o1[t] = 0"]
    assert rep["kept"] == [] and rep["conditional"] == []
    assert rep["minority_report_lines"] == [{"clause": "always o1[t] = 1", "status": "dropped", "branch_condition": None,
                                             "lives_only_if": None, "emitter": None}]


def test_kept_is_insensitive_to_annotations_spacing_and_operand_order():
    # the seeds as written (seeds_v0.tau spelling) vs Tau's reprint with :tau annotations and swapped operands
    before = ("(always ((i_river_polluted[t] = 0) || (o_priority_sewage[t] != 0)))\n"
              "&& (always ((i_sewage_contracted[t]=0)||(o_ask_accountability[t]!=0)))")
    after = ("always (o_priority_sewage[t]:tau != 0 || i_river_polluted[t]:tau = 0) && "
             "(o_ask_accountability[t]:tau != 0 || i_sewage_contracted[t]:tau = 0)")
    rep = diff(before, after)
    assert sorted(rep["kept"]) == sorted([RESIDENT, ENGINEER])
    assert rep["dropped"] == rep["added"] == rep["conditional"] == []
    assert canon("x[t]:sbf != 0") == canon("x[t] != 0") == "x[t] != 0"
    # comments and a trailing period are ignored too
    rep = diff("# a comment\n(always a[t] = 0)  // trailing\n&& (always b[t] = 0).", "always a[t]:tau = 0 && b[t]:tau = 0")
    assert rep["dropped"] == rep["added"] == [] and sorted(rep["kept"]) == ["always a[t] = 0", "always b[t] = 0"]


def test_g09_conditional_with_branch_condition_and_emitters():
    em = {"always ((i_river_polluted[t] = 0) || (o_priority_sewage[t] != 0))": "agents.seed.local_resident",
          "always ((i_sewage_contracted[t] = 0) || (o_ask_accountability[t] != 0))": "agents.seed.civil_engineer",
          "always ((o_endorse[t] = 0) || (o_priority_sewage[t] != 0))": "agents.seed.example_admin"}
    rep = diff(G09_BEFORE, G09_AFTER, emitters=em, inputs=["i_upd", "i_river_polluted", "i_sewage_contracted"])
    c = by_clause(rep)
    assert rep["dropped"] == []
    assert sorted(rep["kept"]) == sorted(["always u[t] = i_upd[t]", ENGINEER])
    assert sorted(rep["conditional"]) == sorted([RESIDENT, ADMIN])
    r = c[RESIDENT]
    assert r["emitter"] == "agents.seed.local_resident"
    assert r["lives_only_if"] == "always i_river_polluted[t] = 0"
    assert r["branch_condition"] == "always o_priority_sewage[t] = 0 && always o_endorse[t] = 0 && always i_river_polluted[t] = 0"
    assert r["branch"] == {"disjunction": 0, "disjunct": 0, "of": 2}
    assert c[ADMIN]["emitter"] == "agents.seed.example_admin" and c[ADMIN]["status"] == "conditional"
    assert c[ENGINEER]["emitter"] == "agents.seed.civil_engineer" and c[ENGINEER]["status"] == "kept"
    assert c["always u[t] = i_upd[t]"]["emitter"] is None  # unknown -> null
    # the update is in every branch, hence unconditionally added
    assert "always o_priority_sewage[t] = 0" in rep["added"]
    assert [a for a in rep["added_detail"] if a["clause"] == "always o_priority_sewage[t] = 0"][0]["status"] == "added"
    assert {l["emitter"] for l in rep["minority_report_lines"]} == {"agents.seed.local_resident", "agents.seed.example_admin"}
    assert all(l["status"] == "conditional" for l in rep["minority_report_lines"])


def test_clause_in_every_branch_is_kept_not_conditional():
    before = "always a[t] = 0"
    after = "(always a[t] = 0 && b[t] = 0) || (always a[t] = 0 && c[t] != 0)"
    rep = diff(before, after)
    assert rep["kept"] == ["always a[t] = 0"] and rep["conditional"] == []
    assert by_clause(rep)["always a[t] = 0"]["via"].startswith("every branch")
    assert sorted(rep["added"]) == ["always b[t] = 0", "always c[t] != 0"]
    assert all(a["status"] == "added_conditional" for a in rep["added_detail"])


def test_added_only():
    # `always X && (sometimes Y)` would parse as always (X && sometimes Y): always scopes rightward as far as it can
    rep = diff("always a[t] = 0", "(always a[t] = 0) && (sometimes b[t] = 1)")
    assert rep["kept"] == ["always a[t] = 0"]
    assert rep["added"] == ["sometimes b[t] = 1"]
    assert rep["minority_report_lines"] == []


def test_nested_parentheses_and_operator_aliases_parse_to_the_same_tree():
    a = parse("(((always (((a[t] = 0) || (b[t] != 0))))) && ((sometimes ((c[t] = 1)))))")
    b = parse("([] (a[t] = 0 || b[t] != 0)) && (<> c[t] = 1)")
    assert render(a) == render(b) == "(always a[t] = 0 || b[t] != 0) && (sometimes c[t] = 1)"
    # term-level parentheses are not formula groups: `(x & y) = 0` stays one atom
    assert parse("always (x[t] & y[t]) = 0 && z[t] = 1") == ("always", ("and", [("atom", "(x[t]&y[t]) = 0"), ("atom", "z[t] = 1")]))
    # negation of a formula vs `!=` inside an atom
    assert parse("!(a[t] = 0) && b[t] != 0") == ("and", [("not", ("atom", "a[t] = 0")), ("atom", "b[t] != 0")])


def test_temporal_operator_scopes_rightward():
    # Tau prints `always A && B && C` for one always over the whole conjunction (G09 initial_spec), so that is how it is read
    assert render(parse("always a[t] = 0 && sometimes b[t] = 1")) == "always (sometimes b[t] = 1) && a[t] = 0"  # children sorted
    assert render(parse("(always a[t] = 0) && sometimes b[t] = 1")) == "(always a[t] = 0) && (sometimes b[t] = 1)"


def test_always_over_conjunction_is_split_but_sometimes_is_not():
    assert [render(c) for c in conjuncts(parse("always (p[t] = 0 && q[t] = 0)"))] == ["always p[t] = 0", "always q[t] = 0"]
    assert [render(c) for c in conjuncts(parse("sometimes (p[t] = 0 && q[t] = 0)"))] == ["sometimes p[t] = 0 && q[t] = 0"]
    # so `always (A && B)` vs `(always A) && (always B)` is a no-op diff
    rep = diff("always (p[t] = 0 && q[t] = 0)", "(always p[t] = 0) && (always q[t] = 0)")
    assert rep["dropped"] == rep["added"] == [] and len(rep["kept"]) == 2


if __name__ == "__main__":
    try:
        import pytest  # noqa: F401
        sys.exit(pytest.main(["-q", __file__]))
    except ImportError:
        failed = 0
        for name, fn in sorted(globals().items()):
            if name.startswith("test_") and callable(fn):
                try:
                    fn(); print(f"ok   {name}")
                except AssertionError as e:
                    failed += 1; print(f"FAIL {name}: {e}")
        print(f"{failed} failed"); sys.exit(1 if failed else 0)
