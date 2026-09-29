#!/usr/bin/env python3
"""D20 toy: does an obfuscating, isolating act satisfy the norm? Ask the oracle, record both answers.

For each form we conjoin the spec with the VIOLATION query
    && (sometimes (i_obf[t] & i_iso[t] & o_complies[t]) != 0)
and call sat. Expected (A8, D20): Family A -> F (an obfuscator cannot comply); v3 -> T (it can).
Whatever the oracle says is what the log records, with the tau-lang pin and the spec hashes.
"""
import hashlib, json, os, subprocess, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tau_oracle import Oracle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
QUERY = "&& (sometimes (i_obf[t] & i_iso[t] & o_complies[t]) != 0)"


def load(name):
    return " ".join(l.strip() for l in open(os.path.join(HERE, name)) if not l.startswith("#") and l.strip())


def main():
    o = Oracle()
    version = o._exec(["--version"]).raw.strip()
    out = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "tau_version": version, "query": QUERY, "results": {}}
    for name in ("family_a.tau", "v3.tau"):
        spec = load(name)
        full = spec + " " + QUERY
        parsed = o.parse(spec)
        verdict = o.sat(full) if parsed["ok"] else "parse-error"
        out["results"][name] = {"spec_sha256": hashlib.sha256(spec.encode()).hexdigest(), "parse": parsed["ok"],
                                "parse_error": parsed["error"], "sat_with_violation": verdict}
        print(f"{name:14s} parse={parsed['ok']} sat(spec ∧ violation)={verdict}")
    expected = {"family_a.tau": "F", "v3.tau": "T"}
    out["matches_D20_expectation"] = all(out["results"][k]["sat_with_violation"] == v for k, v in expected.items())
    path = os.path.join(HERE, "result.json"); json.dump(out, open(path, "w"), indent=1)
    print("recorded", path, "| matches D20 expectation:", out["matches_D20_expectation"])


if __name__ == "__main__":
    main()
