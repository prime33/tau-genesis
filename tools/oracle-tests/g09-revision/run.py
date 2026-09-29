#!/usr/bin/env python3
"""G09/G11 experiment runner (see README.md). Step 1: sat checks. Step 2: the update through `u` via the
interpreter path (F1 v1) with the running spec read after every step; the diff of the spec before and
after the update is the minority report's logical content (D22)."""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from tau_oracle import OracleV1  # noqa: E402
from spec_diff import diff  # noqa: E402


def load(name):
    return " ".join(l.strip() for l in open(os.path.join(HERE, name)) if not l.startswith("#") and l.strip())


def main():
    o = OracleV1()
    seeds, upd = load("seeds_v0.tau"), load("update_contradicting.tau")
    out = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "tau_version": o._exec(["--version"]).raw.strip()}
    out["sat_seeds"], out["sat_update"], out["sat_conjunction"] = o.sat(seeds), o.sat(upd), o.sat(seeds + " && " + upd)
    # Step 2: the room runs the seeds' clauses plus a route for updates: whatever arrives on i_upd is proposed on u.
    running = seeds + " && (always u[t] = i_upd[t])"
    steps = [
        {"i_river_polluted": "T.", "i_sewage_contracted": "T.", "i_upd": "F."},      # k=0: river polluted, works contracted, no update
        {"i_river_polluted": "T.", "i_sewage_contracted": "T.", "i_upd": upd + "."},  # k=1: the contradicting update arrives
        {"i_river_polluted": "T.", "i_sewage_contracted": "T.", "i_upd": "F."},      # k=2: observe what the revised spec does
        {"i_river_polluted": "F.", "i_sewage_contracted": "T.", "i_upd": "F."},      # k=3: river clean
    ]
    res = o.interpret(running, steps)
    out["revision_through_u"] = res
    if res.get("steps"):
        before = res.get("initial_spec", "")
        after = res["steps"][-1]["current_spec"]
        out["spec_diff_before_after"] = diff(before, after)
        out["dropped_clauses"] = out["spec_diff_before_after"]["dropped"]
    json.dump(out, open(os.path.join(HERE, "result.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k.startswith("sat")}, indent=1))
    if res.get("error"):
        print("interpret error:", res["error"])
    for st in res.get("steps", []):
        print(f"k={st['k']} outputs={st['outputs']}")
        print(f"     spec: {st['current_spec'][:200]}")
    print("dropped:", out.get("dropped_clauses"))


if __name__ == "__main__":
    main()
