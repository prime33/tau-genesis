#!/usr/bin/env python3
"""Hash chain over a JSONL file (ledger, decisions). Each record's `hash` = sha256 of canonical JSON of the
record without `hash`/`id`, with `prev` = previous record's hash. `id` = hash[:12].

  chain.py append <file> '<json>'   add a record (fills prev, hash, id, ts if missing)
  chain.py verify <file>            re-hash every record, check prev links; exit 1 on the first break
  chain.py head <file>              print the head hash (empty file: the string "genesis")
"""
import hashlib, json, sys, os, time


def canon(rec):
    r = {k: v for k, v in rec.items() if k not in ("hash", "id")}
    return json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def h(rec):
    return hashlib.sha256(canon(rec)).hexdigest()


def records(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def head(path):
    rs = records(path)
    return rs[-1]["hash"] if rs else "genesis"


def append(path, rec):
    rs = records(path)
    rec = dict(rec)
    rec["prev"] = rs[-1]["hash"] if rs else None
    rec.setdefault("ts", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    rec["hash"] = h(rec)
    rec["id"] = rec["hash"][:12]
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n")
    return rec


def verify(path):
    prev = None
    for n, rec in enumerate(records(path), 1):
        if rec.get("prev") != prev:
            return False, f"record {n} ({rec.get('id')}): prev {rec.get('prev')} != {prev}"
        if h(rec) != rec.get("hash"):
            return False, f"record {n} ({rec.get('id')}): hash mismatch"
        if rec.get("id") != rec["hash"][:12]:
            return False, f"record {n}: id mismatch"
        prev = rec["hash"]
    return True, f"ok: {n if 'n' in dir() else 0} records, head {prev or 'genesis'}"


if __name__ == "__main__":
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == "append":
        print(json.dumps(append(path, json.loads(sys.argv[3])), sort_keys=True))
    elif cmd == "verify":
        ok, msg = verify(path); print(msg); sys.exit(0 if ok else 1)
    elif cmd == "head":
        print(head(path))
