#!/usr/bin/env python3
"""Re-verify every attempt in kb/attempts.db through the current oracle path (no API calls, no spend).
Writes kb/learner/reverify-<date>.json and prints the corrected verdict per attempt and per fragment."""
import json, os, sqlite3, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import run as R  # noqa: E402
from tau_oracle import OracleV1  # noqa: E402
OPS = R.OPS
o = OracleV1(timeout=240)
tests = json.load(open(os.path.join(HERE, "tests", "valid_thought.json")))["tests"]
c = sqlite3.connect(R.DB)
rows = c.execute("select id, fragment, attempt_no, spec, test_json, unmapped, verdict, diagnosis from attempt where spec is not null and spec != '' order by id").fetchall()
out = []
for aid, frag, n, spec, tj, um, v0, d0 in rows:
    ans = {"spec": spec, "test": json.loads(tj) if tj else {}, "unmapped": json.loads(um) if um else []}
    t0 = time.time()
    v = R.verify(o, ans)
    ext = tests.get(frag); ext_ok = None
    if v["verdict"] == "verified" and ext:
        res = o.interpret_auto(spec, ext["steps"])
        got = res.get("output_series") or {}
        ext_ok = int(res.get("error") is None and all(R.series_match(got.get(k), vv) for k, vv in ext["expected"].items()))
    words = [w for w in frag.split("_") if len(w) > 3] + ["faculty", "parser"]
    reduced = int(bool(ans["unmapped"]) and any(w in " ".join(ans["unmapped"]).lower() for w in words))
    rec = {"id": aid, "fragment": frag, "attempt": n, "old": f"{v0}/{d0}", "new": v["verdict"], "diagnosis": v.get("diagnosis"),
           "parse_ok": v["parse_ok"], "sat": v["sat"], "run_ok": v["run_ok"], "ext_ok": ext_ok, "reduced": reduced, "path": None, "seconds": round(time.time() - t0, 1)}
    out.append(rec)
    print(f"[{aid:3d}] {frag:46s} #{n} old={rec['old']:22s} new={v['verdict']}/{v.get('diagnosis')} parse={v['parse_ok']} sat={v['sat']} self={v['run_ok']} ext={ext_ok} reduced={reduced}", flush=True)
path = os.path.join(OPS, "kb", "learner", f"reverify-{time.strftime('%Y-%m-%d')}.json"); json.dump(out, open(path, "w"), indent=1)
best = {}
for r in out:
    b = best.setdefault(r["fragment"], {"self": 0, "ext": 0, "reduced": 0, "parsed": 0, "sat": 0})
    b["parsed"] |= r["parse_ok"]; b["sat"] |= int(r["sat"] == "T"); b["self"] |= r["run_ok"]; b["ext"] |= int(r["ext_ok"] or 0); b["reduced"] |= r["reduced"] if r["run_ok"] else 0
print("\n=== per fragment (any attempt) ===")
for f, b in best.items(): print(f"  {f:46s} parsed={b['parsed']} sat={b['sat']} self={b['self']} external={b['ext']} reduced={b['reduced']}")
n = len(best); print(f"fragments: {n} | parsed {sum(b['parsed'] for b in best.values())} | sat {sum(b['sat'] for b in best.values())} | self-asserted {sum(b['self'] for b in best.values())} | external-asserted {sum(b['ext'] for b in best.values())} | reduced {sum(b['reduced'] for b in best.values())}")
print("report:", path)
