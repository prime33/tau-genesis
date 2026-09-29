#!/usr/bin/env python3
"""Learner v1 — the generate + verify loop (docs/learner-v1.md §2). The model proposes; the oracle disposes.

  python3 tools/learner/run.py --fragments valid_thought [--max-attempts 5] [--daily-cap 15] [--model anthropic-claude-opus-5]

Per fragment: prompt from tools/learner/retrieve.py (retrieval + grammar + LANGUEDOC + D19 list) → one generation
through the DigitalOcean gateway with the Anthropic SDK (base_url https://inference.do-ai.run, key DO_INFERENCE_KEY)
→ JSON answer {spec, streams, test, claims, unmapped} → Oracle.guard (D19) → parse → sat → OracleV1.interpret_auto with
the model's own test → comparison with its expected outputs on normalised Boolean forms (0/1 ≡ F/T). Any failing stage ends the attempt; the next
prompt appends the failed spec and the oracle's VERBATIM answer. Stops at verified, or gives up with a diagnosis
in {grammar, unsat, semantic, unmapped, refused}. Every attempt is one row in kb/attempts.db (the v2 dataset).
Spend: usage × list price per attempt, summed per UTC day; the run refuses to start an attempt past --daily-cap.
Verified specs go to tools/learner/out/<fragment>.tau + .test.json with the attempt id in the header.
"""
from __future__ import annotations

import argparse, hashlib, json, os, re, sqlite3, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.abspath(os.path.join(HERE, "..", ".."))
OPS = os.environ.get("TAU_OPS", os.path.join(os.path.dirname(PUB), "tau-genesis-ops"))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(PUB, "tools"))
import retrieve  # noqa: E402
from tau_oracle import OracleV1  # noqa: E402

DB = os.path.join(OPS, "kb", "attempts.db")
OUT = os.path.join(HERE, "out")
PRICE = {"anthropic-claude-opus-5": (5.0, 25.0, 0.50, 6.25), "anthropic-claude-5-sonnet": (2.0, 10.0, 0.20, 2.50),
         "anthropic-claude-haiku-4.5": (1.0, 5.0, 0.10, 1.25)}  # $/MTok: input, output, cache read, cache write
FRAGMENT_SETS = {
    "valid_thought": ["statement", "defined_concepts", "preserves_origin_trace", "does_not_contradict_prior_reasoning",
                      "logically_consistent_with_upstream_definitions", "authored_by_agent", "has_identity_stream",
                      "evaluates_lineage", "checks_coherence", "checks_amendment_status", "declares_all_terms_in_interface",
                      "does_not_leak_terms"],
    "step2": ["stream_version", "proposed_amendment", "consensus_threshold", "historical_integrity", "recursive_legitimacy",
              "semantic_consensus", "amendment_quorum", "contradiction_detection", "consensus_finality", "update_process", "consensus_logic"],
    # not sent: semantic_diff (M027, needs faculty F3), fork_resolution (M036, not expressible) — learner-v1.md §3
    "step3": ["semantic_expression", "freedom_of_expression", "non_retroactive_silencing", "semantic_integrity",
              "semantic_resonance", "integration", "coherence_preservation", "contradiction_as_invitation", "alignment_cycle",
              "contradiction_mediation", "shared_glossary_requirement", "semantic_alignment_duty", "prohibition_of_obfuscation",
              "coherence_audit_process"],
    # not sent: the whole-amendment keys and amendment 003's bare requires (M084) — tests/step3.json _about
    "step4": ["treatment_requirement", "water_protection", "health_priority", "allocation_priority", "river_town_priority",
              "stream_endorsement", "endorsement_from_town_admin", "endorsement_from_engineer", "endorsement_from_resident"],
    # step 4 = the ILLUSTRATIVE civic example (streams/*/example); its hidden tests are not written yet (CLEAN-PUBLIC-PLAN §4)
}
FRAGMENT_SETS["steps2-4"] = FRAGMENT_SETS["step2"] + FRAGMENT_SETS["step3"] + FRAGMENT_SETS["step4"]
JSON_SHAPE = ('Answer with ONE JSON object and nothing else: {"spec": "<Tau specification, one formula, statements joined with &&>", '
              '"streams": {"inputs": ["i_x", ...], "outputs": ["o_y", ...]}, "test": {"steps": [{"i_x": "T"|"F"|"<value>", ...}, ...3-5 steps], '
              '"expected": {"o_y": ["T"|"F"|..., one per step], ...}}, "claims": ["<one falsifiable sentence>", ...], "unmapped": ["<term>", ...]}. '
              'Stream values are the Tau printer\'s forms: "T"/"F" for tau/sbf truth values. Never use identifiers containing "being". '
              'If a term of the fragment has no Tau counterpart, put it in "unmapped" rather than inventing one.')


def db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("""create table if not exists attempt(id integer primary key, ts text, fragment text, attempt_no int, model text,
        prompt_sha text, retrieved text, input_tokens int, cache_read int, cache_write int, output_tokens int, usd real,
        raw_answer text, spec text, test_json text, claims text, unmapped text, guard_error text,
        parse_ok int, parse_raw text, sat text, sat_raw text, run_ok int, run_raw text, verdict text, diagnosis text, seconds real)""")
    for col in ("ext_ok int", "ext_raw text", "reduced int", "interface text", "condition text"):
        try: c.execute(f"alter table attempt add column {col}")
        except sqlite3.OperationalError: pass
    return c


def spent_today(c) -> float:
    day = time.strftime("%Y-%m-%d", time.gmtime())
    return c.execute("select coalesce(sum(usd),0) from attempt where ts like ?", (day + "%",)).fetchone()[0]


def usd(model, u) -> float:
    pi, po, pcr, pcw = PRICE.get(model, PRICE["anthropic-claude-opus-5"])
    ci, cw = getattr(u, "cache_read_input_tokens", 0) or 0, getattr(u, "cache_creation_input_tokens", 0) or 0
    return round((u.input_tokens - ci - cw) / 1e6 * pi + ci / 1e6 * pcr + cw / 1e6 * pcw + u.output_tokens / 1e6 * po, 5)


def generate(client, model, system_stable, system_var, user, history):
    """One call. Stable prefix carries cache_control; history = list of (failed_spec, oracle_raw) appended verbatim."""
    msgs = [{"role": "user", "content": user}]
    for spec, raw in history:
        msgs.append({"role": "assistant", "content": json.dumps({"spec": spec})})
        msgs.append({"role": "user", "content": "The oracle said (verbatim):\n" + raw[-3000:] + "\n\nRevise. Same JSON shape."})
    system = [{"type": "text", "text": system_stable, "cache_control": {"type": "ephemeral"}}, {"type": "text", "text": system_var + "\n\n" + JSON_SHAPE}]
    kwargs = dict(model=model, max_tokens=8192, system=system, messages=msgs)  # 4096 was hit once (attempt 10): a truncated answer is a wasted attempt
    for extra in ({"thinking": {"type": "adaptive"}, "output_config": {"effort": "high"}}, {}):
        try:
            return client.messages.create(**kwargs, **extra)
        except Exception as e:  # noqa: BLE001
            last = e
            if "400" not in str(e) and "invalid" not in str(e).lower():
                raise
    raise last


def parse_answer(text: str) -> dict | None:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def series_match(got, expected) -> bool:
    """Compare on the oracle's normalised Boolean forms: sbf prints 0/1, tau prints T/F, the model may write either."""
    if got is None:
        return False
    return [OracleV1.norm_bool(x) for x in got] == [OracleV1.norm_bool(x) for x in expected]


def verify(o: OracleV1, ans: dict) -> dict:
    spec = (ans.get("spec") or "").strip()
    r = {"spec": spec, "guard_error": None, "parse_ok": 0, "parse_raw": "", "sat": None, "sat_raw": "", "run_ok": 0, "run_raw": ""}
    try:
        o.guard(spec)
    except ValueError as e:
        r["guard_error"] = str(e); r["verdict"], r["diagnosis"] = "failed", "grammar"; return r
    p = o.parse(spec); r["parse_ok"], r["parse_raw"] = int(p["ok"]), p["raw"]
    if not p["ok"]:
        r["verdict"], r["diagnosis"] = "failed", "grammar"; return r
    s = o.sat(spec); r["sat"] = s
    r["sat_raw"] = o._exec(["-q", "-X", "-s", "0", "-c", "0", "-b", "0", "-e", f"sat {spec}"]).raw if s not in ("T",) else ""
    if s != "T":
        r["verdict"], r["diagnosis"] = "failed", ("unsat" if s == "F" else "grammar"); return r
    test = ans.get("test") or {}
    steps, expected = test.get("steps") or [], test.get("expected") or {}
    if not steps or not expected:
        r["run_raw"] = "no test supplied"; r["verdict"], r["diagnosis"] = "failed", "semantic"; return r
    res = o.interpret_auto(spec, steps)   # binding for bare specs, REPL for declared/annotated streams or after a binding crash
    r["run_raw"] = json.dumps({k: v for k, v in res.items() if k != "tau_stdout"})[:6000]
    got = res.get("output_series") or {}
    ok = res.get("error") is None and all(series_match(got.get(k), v) for k, v in expected.items())
    r["run_ok"] = int(ok)
    if ok:
        r["verdict"], r["diagnosis"] = "verified", None
    else:
        r["verdict"], r["diagnosis"] = "failed", "semantic"
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragments", default="valid_thought"); ap.add_argument("--max-attempts", type=int, default=5)
    ap.add_argument("--daily-cap", type=float, default=15.0); ap.add_argument("--model", default="anthropic-claude-opus-5")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--ablate", choices=["bare"], help="learner-v1.md §4 baseline: no retrieval, no idioms; one attempt; rows tagged condition=bare; never writes out/")
    ap.add_argument("--tests", help="external pre-registered tests file name under tools/learner/tests/ (e.g. valid_thought); interface goes to the model, steps/expected stay hidden")
    a = ap.parse_args()
    tests = {}
    if a.tests:
        for tf in a.tests.split(","):
            tests.update(json.load(open(os.path.join(HERE, "tests", tf + ".json")))["tests"])
    from anthropic import Anthropic
    client = Anthropic(base_url="https://inference.do-ai.run", api_key=os.environ["DO_INFERENCE_KEY"])
    o = OracleV1(timeout=180)
    c = db(); concepts = retrieve.concepts()
    names = FRAGMENT_SETS.get(a.fragments) or a.fragments.split(",")
    os.makedirs(OUT, exist_ok=True)
    summary = {}
    for name in names:
        if name not in concepts:
            print(f"skip {name}: not in concepts.md"); continue
        system, user, meta = retrieve.build(name, concepts, a.k, ablate=a.ablate)
        stable, var = system.split("## Vocabulary decisions", 1)
        var = "## Vocabulary decisions" + var
        ext = tests.get(name)
        if ext:
            iface = ext["interface"]
            user += ("\n\n## Required stream interface (use exactly these names; the acceptance test is hidden)\n"
                     + "\n".join(f"- input `{k}`: {v}" for k, v in iface["inputs"].items())
                     + "\n" + "\n".join(f"- output `{k}`: {v}" for k, v in iface["outputs"].items())
                     + "\nDeclare each as a `tau` stream (e.g. `i_x : tau := in console.` / `o_y : tau := out console.`).")
        history, final = [], None
        for n in range(1, (1 if a.ablate else a.max_attempts) + 1):
            spent = spent_today(c)
            if spent >= a.daily_cap:
                print(f"DAILY CAP reached (${spent:.2f} ≥ ${a.daily_cap}); stopping before {name} attempt {n}"); summary[name] = "cap"; break
            t0 = time.time()
            m = None
            for tr in range(1, 4):  # the DO gateway answered 500 'credential validation failed' for ~6 min on 2026-09-29: retry, do not abandon
                try:
                    m = generate(client, a.model, stable, var, user, history); break
                except Exception as e:  # noqa: BLE001
                    print(f"{name} #{n}: API error (try {tr}/3) {str(e)[:120]}", flush=True)
                    if tr < 3: time.sleep(30 * tr)
            if m is None:
                summary[name] = "api-error"; break
            text = "".join(b.text for b in m.content if getattr(b, "type", "") == "text")
            cost = usd(a.model, m.usage)
            row = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "fragment": name, "attempt_no": n, "model": a.model,
                   "condition": a.ablate or "full",
                   "prompt_sha": hashlib.sha256((stable + var + user + json.dumps(history)).encode()).hexdigest()[:16],
                   "retrieved": json.dumps(meta), "input_tokens": m.usage.input_tokens,
                   "cache_read": getattr(m.usage, "cache_read_input_tokens", 0) or 0, "cache_write": getattr(m.usage, "cache_creation_input_tokens", 0) or 0,
                   "output_tokens": m.usage.output_tokens, "usd": cost, "raw_answer": text[:20000]}
            if m.stop_reason == "refusal":
                row.update(verdict="refused", diagnosis="refused", spec="", seconds=round(time.time() - t0, 2)); v = row
            else:
                ans = parse_answer(text)
                if ans is None:
                    v = {"spec": "", "verdict": "failed", "diagnosis": "format", "parse_raw": "answer was not one JSON object"}  # never reached Tau
                else:
                    v = verify(o, ans)
                    v["test_json"] = json.dumps(ans.get("test")); v["claims"] = json.dumps(ans.get("claims")); v["unmapped"] = json.dumps(ans.get("unmapped"))
                    # reduced (structural, v1.2): the spec ignores an offered input, or its output series equals one
                    # input series on the model's own test. The earlier word-match on `unmapped` fired on every answer
                    # (the model lists 6-17 unmapped prose terms each time) and said nothing.
                    offered = set((ext or {}).get("interface", {}).get("inputs", {})) if ext else set()
                    used = set(re.findall(r"\b(i_[a-z0-9_]+)\b", v.get("spec") or ""))
                    ignores_input = bool(offered) and bool(offered - used)
                    tst = ans.get("test") or {}
                    ins_series = {}
                    for st in tst.get("steps") or []:
                        for k_, val in st.items(): ins_series.setdefault(k_, []).append(str(val))
                    outs = (tst.get("expected") or {})
                    # identity needs BOTH: an output series equal to an input series AND a spec that reads exactly one input.
                    # Series equality alone fired on amendment_quorum (two-of-three; on the test vector the output happened
                    # to equal one voter's series). Coincidence on a 4-5 step vector is not structure.
                    identity = len(used) == 1 and any(list(map(str, ov)) == iv for ov in outs.values() for iv in ins_series.values())
                    v["reduced"] = int(ignores_input or identity)
                    if v["verdict"] == "verified":
                        if ext:
                            v["interface"] = json.dumps(ext["interface"])
                            res = o.interpret_auto(v["spec"], ext["steps"])
                            got = res.get("output_series") or {}
                            okx = res.get("error") is None and all(series_match(got.get(k), v_) for k, v_ in ext["expected"].items())
                            v["ext_ok"] = int(okx); v["ext_raw"] = json.dumps({"got": got, "expected": ext["expected"], "error": res.get("error")})[:4000]
                            v["verdict"] = "verified-external" if okx else "failed"
                            if not okx: v["diagnosis"] = "semantic-external"
                        else:
                            v["verdict"] = "verified-self"
                        if v["verdict"].startswith("verified") and v["reduced"]:
                            v["verdict"] += "-reduced"
                row.update(v); row["seconds"] = round(time.time() - t0, 2)
            cols = ["ts", "fragment", "attempt_no", "model", "prompt_sha", "retrieved", "input_tokens", "cache_read", "cache_write", "output_tokens", "usd",
                    "raw_answer", "spec", "test_json", "claims", "unmapped", "guard_error", "parse_ok", "parse_raw", "sat", "sat_raw", "run_ok", "run_raw",
                    "verdict", "diagnosis", "seconds", "ext_ok", "ext_raw", "reduced", "interface", "condition"]
            c.execute(f"insert into attempt({','.join(cols)}) values({','.join('?' * len(cols))})", [row.get(k) for k in cols]); c.commit()
            aid = c.execute("select max(id) from attempt").fetchone()[0]
            print(f"{name} #{n} [{aid}] {row['verdict']}/{row.get('diagnosis')} parse={row.get('parse_ok')} sat={row.get('sat')} run={row.get('run_ok')} ext={row.get('ext_ok')} "
                  f"${cost:.3f} in={row['input_tokens']} cached={row['cache_read']} out={row['output_tokens']} {row['seconds']}s", flush=True)
            if str(row["verdict"]).startswith("verified"):
                if a.ablate:
                    pass  # baseline rows never become verified outputs
                else:
                  with open(os.path.join(OUT, f"{name}.tau"), "w") as fh:
                      fh.write(f"# {name} — verified by the oracle (attempt {aid}, {row['ts']}, tau-lang 3badb21, model {a.model})\n# Source fragment: {', '.join(concepts[name]['defined_in'])}\n{row['spec']}\n")
                  with open(os.path.join(OUT, f"{name}.test.json"), "w") as fh:
                      fh.write(row["test_json"])
                final = row["verdict"]; break
            if row["verdict"] == "refused":
                final = "refused"; break
            fb = (row.get("guard_error") or "") + (row.get("parse_raw") or "") + (row.get("sat_raw") or "") + (row.get("run_raw") or "")
            if row.get("diagnosis") == "semantic-external":
                # The hidden test stays hidden: feed back the fact of disagreement only, never the trace or the expected
                # series (attempt 79, consensus_logic, saw the series and matched it on the next attempt; weaker evidence).
                fb += ("\nThe hidden acceptance test disagreed with your spec on the required interface. Your own test passed, so the "
                       "spec is consistent but reads the phrase differently from the acceptance test. Re-read the interface descriptions "
                       "(each output's description is the whole definition of that output) and change the reading; no trace is given.")
            if history and (row.get("spec") or "") == history[-1][0]:
                fb += "\nThis spec is IDENTICAL to your previous attempt and the oracle's answer is the same. Change the spec; do not resubmit it."
            history.append((row.get("spec") or text[:2000], fb))
            final = f"gave-up:{row.get('diagnosis')}"
        summary[name] = final or summary.get(name)
    print("\n=== summary ===")
    for k, v in summary.items():
        print(f"  {k:48s} {v}")
    n = len(summary); ver = sum(1 for v in summary.values() if str(v).startswith("verified"))
    tot = c.execute("select count(*), coalesce(sum(usd),0), sum(parse_ok), sum(case when sat='T' then 1 else 0 end), sum(run_ok), sum(coalesce(ext_ok,0)), sum(coalesce(reduced,0)) from attempt").fetchone()
    print(f"fragments verified: {ver}/{n} | attempts in db: {tot[0]} | parsed: {tot[2]} | sat T: {tot[3]} | run-asserted(self): {tot[4]} | external-asserted: {tot[5]} | reduced: {tot[6]} | spend total: ${tot[1]:.2f} | today: ${spent_today(c):.2f}")


if __name__ == "__main__":
    main()
