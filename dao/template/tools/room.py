#!/usr/bin/env python3
"""room.py — the room runtime, eight verbs, form only (TEMPLATE v1). It writes schema-valid, hash-chained records and
refuses everything else; it never judges content. Judgment stays with the forces and the signer.

  room.py init <dir> <room-id>             scaffold a room (forces.json, variables.json, CHARTER.md, empty chains)
  room.py affirm <dir> '<json>'            append a ledger record (surface, author_class, text, provenance)
  room.py object <dir> '<json>'            append a minority record (an objection, verbatim; needs `target` record id)
  room.py propose <dir> <spec.tau> <name>  run the verifier (parse, sat) on a candidate; write candidates/<name>.{tau,json}; log a run
  room.py decide <dir> '<json>'            append a DECIDE (target clause@version list, signatory{role,key_id}; spec_hash must be a sat=T candidate)
  room.py disclose <dir> <variable> <class> <decision-id>   change a variable's class; only against an existing DECIDE
  room.py anchor <dir> [--dry-run]         anchor the heads (tools/anchor.py)
  room.py verify <dir>                     run the conformance suite on the room
"""
import hashlib, json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); TPL = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import chain
from validate import validate
CONFORMANCE_VERSION = "template-v1.0"


def now(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
def month(): return time.strftime("%Y-%m", time.gmtime())
def sha(s): return hashlib.sha256(s.encode() if isinstance(s, str) else s).hexdigest()


def append(kind, path, rec):
    """Validate against the schema (with prev/hash/id/ts filled as chain.append will) then append. F6: malformed → refused."""
    probe = dict(rec); rs = chain.records(path)
    probe["prev"] = rs[-1]["hash"] if rs else None; probe.setdefault("ts", now()); probe["hash"] = "0" * 64; probe["id"] = "0" * 12
    validate(kind, probe)
    return chain.append(path, rec)


def init(d, room_id):
    for sub in ("ledger", "candidates", "minority", "consent", "anchors", "forces", "runs"): os.makedirs(os.path.join(d, sub), exist_ok=True)
    forces = {"affirming": {"spec": "forces/affirming.tau", "may_read": ["i_record"], "scratch": []},
              "negating": {"spec": "forces/negating.tau", "may_read": ["i_ledger", "i_claim"], "scratch": []},
              "reconciling": {"spec": "forces/reconciling.tau", "may_read": ["i_ledger", "i_objection"], "scratch": ["o_scratch"]}}
    validate("forces", forces); json.dump(forces, open(os.path.join(d, "forces.json"), "w"), indent=1)
    open(os.path.join(d, "forces/affirming.tau"), "w").write("i_record : tau := in console. o_ledger : tau := out console. always o_ledger[t] = i_record[t]\n")
    open(os.path.join(d, "forces/negating.tau"), "w").write("i_ledger : tau := in console. i_claim : tau := in console. o_objection : tau := out console. always o_objection[t] = i_claim[t] & i_ledger[t]'\n")
    open(os.path.join(d, "forces/reconciling.tau"), "w").write("i_ledger : tau := in console. i_objection : tau := in console. o_scratch : tau := out console. o_candidate : tau := out console. always (o_scratch[t] = i_ledger[t] & i_objection[t]' && o_candidate[t] = o_scratch[t])\n")
    json.dump({"room": room_id, "variables": []}, open(os.path.join(d, "variables.json"), "w"), indent=1)
    if not os.path.exists(os.path.join(d, "CHARTER.md")):
        open(os.path.join(d, "CHARTER.md"), "w").write(f"# CHARTER — {room_id}\n\nRoom id: `{room_id}`. Signer: (role). Invariants: (list). Consent levels: (list). Address: (public key). Money: none. See dao/TEMPLATE.md.\n")
    for f in ("decisions.jsonl", "spend.jsonl", "runs/runs.jsonl", "anchors/anchors.jsonl", "minority/minority.jsonl", "consent/consent.jsonl"):
        open(os.path.join(d, f), "a").close()
    print(json.dumps({"room": room_id, "dir": d, "conformance_version": CONFORMANCE_VERSION}))


def affirm(d, rec):
    rec = json.loads(rec) if isinstance(rec, str) else rec
    surface = rec.get("surface", "channel")
    return append("record", os.path.join(d, "ledger", f"{surface}-{month()}.jsonl"), rec)


def object_(d, rec):
    rec = json.loads(rec) if isinstance(rec, str) else rec
    rec["surface"] = "minority"
    if "target" not in rec: sys.exit("an objection names the record id it objects to (`target`)")
    return append("record", os.path.join(d, "minority", "minority.jsonl"), rec)


def propose(d, spec_path, name):
    sys.path.insert(0, os.path.join(os.path.dirname(TPL), "..", "tools")); sys.path.insert(0, os.path.join(TPL, "..", "..", "tools"))
    from tau_oracle import OracleV1
    spec = open(spec_path).read().strip(); o = OracleV1(timeout=180)
    o.guard(spec); p = o.parse(spec); sat = o.sat(spec) if p["ok"] else "error"
    os.makedirs(os.path.join(d, "candidates"), exist_ok=True)
    open(os.path.join(d, "candidates", f"{name}.tau"), "w").write(spec + "\n")
    meta = {"name": name, "spec_hash": sha(spec), "parse_ok": bool(p["ok"]), "sat": sat if sat in ("T", "F") else "error", "pin": "3badb21", "ts": now()}
    json.dump(meta, open(os.path.join(d, "candidates", f"{name}.json"), "w"), indent=1)
    run = append("run", os.path.join(d, "runs", "runs.jsonl"), {"agent": "reconciling", "model": "verifier", "lane": "propose", "cost_usd": 0.0, "runner": "room.py",
                 "status": "complete" if p["ok"] else "error", "output_ref": f"candidates/{name}.json", "spec_hash": meta["spec_hash"], "parse_ok": meta["parse_ok"], "sat": meta["sat"]})
    print(json.dumps({**meta, "run": run["id"]}))
    return meta


def decide(d, rec):
    rec = json.loads(rec) if isinstance(rec, str) else rec
    rec.setdefault("kind", "DECIDE"); rec["conformance_version"] = CONFORMANCE_VERSION
    if rec["kind"] == "DECIDE":
        h = rec.get("spec_hash")
        cands = [json.load(open(os.path.join(d, "candidates", f))) for f in os.listdir(os.path.join(d, "candidates")) if f.endswith(".json")]
        ok = [c for c in cands if c["spec_hash"] == h and c["sat"] == "T"]
        if not ok: sys.exit("DECIDE refused: spec_hash is not a candidate the verifier found satisfiable (agents propose, the verifier disposes, a person publishes)")
        rec["verdict"] = "T"
    return append("decision", os.path.join(d, "decisions.jsonl"), rec)


def disclose(d, variable, cls, decision_id):
    ids = {r["id"] for r in chain.records(os.path.join(d, "decisions.jsonl"))}
    if decision_id not in ids: sys.exit("disclose refused: no such DECIDE")
    v = json.load(open(os.path.join(d, "variables.json")))
    entry = next((x for x in v["variables"] if x["name"] == variable), None)
    if entry is None: entry = {"name": variable, "source": "room"}; v["variables"].append(entry)
    entry["class"] = cls; entry["decision"] = decision_id; validate("variable", entry)
    json.dump(v, open(os.path.join(d, "variables.json"), "w"), indent=1)
    print(json.dumps(entry))


def anchor(d, dry):
    env = dict(os.environ, ROOM_DIR=d, ROOM_ID=json.load(open(os.path.join(d, "variables.json")))["room"])
    subprocess.run([sys.executable, os.path.join(HERE, "anchor.py")] + (["--dry-run"] if dry else []), env=env, check=True)


def verify(d):
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", os.path.join(TPL, "conformance"), "-p", "no:cacheprovider"], env=dict(os.environ, ROOM_DIR=os.path.abspath(d)))
    sys.exit(r.returncode)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    v = a[0]
    if v == "init": init(a[1], a[2])
    elif v == "affirm": print(json.dumps(affirm(a[1], a[2])))
    elif v == "object": print(json.dumps(object_(a[1], a[2])))
    elif v == "propose": propose(a[1], a[2], a[3])
    elif v == "decide": print(json.dumps(decide(a[1], a[2])))
    elif v == "disclose": disclose(a[1], a[2], a[3], a[4])
    elif v == "anchor": anchor(a[1], "--dry-run" in a)
    elif v == "verify": verify(a[1])
    else: sys.exit(__doc__)
