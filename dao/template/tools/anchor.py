#!/usr/bin/env python3
"""Zcash anchor (D29, D30): notary only. Computes the ledger and decisions heads, builds the memo, and either
prints it (--dry-run) or hands it to a configurable wallet command that sends a dust shielded self-transfer
from the ROOM's address with that memo. The private key never touches this script or the repository.

Memo v0 (<= 512 bytes, ASCII): tg1|<room>|<kind>|<ledger-head>|<decisions-head>|<seq>|<YYYY-MM-DD>
  kind: epoch | decide | redact | disclose

Env:
  ROOM_DIR           the room directory (default: cwd)
  ROOM_ID            room slug (or --room)
  ZCASH_ANCHOR_CMD   shell command template with {memo} and {amount}; e.g. a zingo-cli / zcash-cli send to the
                     room's own address. Absent → dry-run only. Testnet first (README).
Output: appends one line to anchors/anchors.jsonl (also hash-chained) with heads, memo, txid (or "dry-run").
"""
import argparse, json, os, subprocess, sys, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOM_DIR") or os.getcwd()
sys.path.insert(0, HERE)
import chain

LEDGER_DIR = os.path.join(ROOT, "ledger")
DECISIONS = os.path.join(ROOT, "decisions.jsonl")
ANCHORS = os.path.join(ROOT, "anchors", "anchors.jsonl")


def ledger_head():
    """Head over all ledger files in name order: sha256 of the concatenated per-file heads."""
    files = sorted(f for f in (os.listdir(LEDGER_DIR) if os.path.isdir(LEDGER_DIR) else []) if f.endswith(".jsonl"))
    heads = [f"{f}:{chain.head(os.path.join(LEDGER_DIR, f))}" for f in files]
    return hashlib.sha256("\n".join(heads).encode()).hexdigest(), heads


def build_memo(room, kind, lh, dh, seq, date):
    memo = f"tg1|{room}|{kind}|{lh}|{dh}|{seq}|{date}"
    assert len(memo.encode()) <= 512, "memo over 512 bytes"
    return memo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--room", default=os.environ.get("ROOM_ID")); ap.add_argument("--kind", default="epoch", choices=["epoch", "decide", "redact", "disclose"])
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--amount", default="0.00001")
    a = ap.parse_args()
    if not a.room: sys.exit("room id required (--room or ROOM_ID)")
    lh, per_file = ledger_head(); dh = chain.head(DECISIONS)
    seq = len(chain.records(ANCHORS)) + 1; date = time.strftime("%Y-%m-%d", time.gmtime())
    memo = build_memo(a.room, a.kind, lh, dh, seq, date)
    cmd = os.environ.get("ZCASH_ANCHOR_CMD")
    if a.dry_run or not cmd:
        txid = "dry-run"
    else:
        r = subprocess.run(cmd.format(memo=memo, amount=a.amount), shell=True, capture_output=True, text=True)
        if r.returncode != 0: sys.exit(f"send failed: {r.stderr[-400:]}")
        txid = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "sent-no-txid"
    rec = chain.append(ANCHORS, {"seq": seq, "kind": a.kind, "room": a.room, "ledger_head": lh, "ledger_files": per_file, "decisions_head": dh, "memo": memo, "txid": txid})
    print(json.dumps({"seq": seq, "memo": memo, "txid": txid, "anchor_id": rec["id"]}))


if __name__ == "__main__":
    main()
