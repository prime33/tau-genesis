#!/usr/bin/env python3
"""Verify anchors against the repository. Input: the anchor stream as seen through the room's viewing key
(a JSON list of {"txid":..., "memo":...} exported from the wallet), or, without a wallet, anchors/anchors.jsonl
itself (then only the chain and the heads are checked, not the on-chain presence).

  anchor_verify.py [--memos memos.json]

Checks: (1) anchors.jsonl chain intact; (2) every memo parses and its heads match the recorded heads;
(3) the LATEST anchor's heads equal the heads recomputed from ledger/ and decisions.jsonl now (earlier anchors
are checked against their own recorded heads; recomputing history needs the ledger prefix at that time, which
the chain gives: a head is a commitment to everything before it); (4) with --memos, every recorded txid/memo
appears on chain and no on-chain memo for this room is missing from the file.
"""
import argparse, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import chain, anchor


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--memos"); a = ap.parse_args()
    ok, msg = chain.verify(anchor.ANCHORS); print("anchors chain:", msg)
    bad = 0 if ok else 1
    # a head is only a commitment if the file behind it re-verifies: check every chained file first
    files = [anchor.DECISIONS] + sorted(os.path.join(anchor.LEDGER_DIR, f) for f in (os.listdir(anchor.LEDGER_DIR) if os.path.isdir(anchor.LEDGER_DIR) else []) if f.endswith(".jsonl"))
    for f in files:
        okf, msgf = chain.verify(f); print(f"{os.path.relpath(f, anchor.ROOT)}: {msgf}")
        if not okf: bad += 1
    recs = chain.records(anchor.ANCHORS)
    for r in recs:
        parts = r["memo"].split("|")
        if len(parts) != 7 or parts[0] != "tg1" or parts[3] != r["ledger_head"] or parts[4] != r["decisions_head"]:
            print(f"anchor {r['seq']}: memo does not match recorded heads"); bad += 1
    if recs:
        lh, _ = anchor.ledger_head(); dh = chain.head(anchor.DECISIONS); last = recs[-1]
        if (lh, dh) != (last["ledger_head"], last["decisions_head"]):
            print(f"latest anchor {last['seq']}: heads differ from the repository now (ledger {lh[:12]} vs {last['ledger_head'][:12]}; decisions {dh[:12]} vs {last['decisions_head'][:12]}) — records were added since, or history was altered")
        else:
            print(f"latest anchor {last['seq']}: heads match the repository now")
    if a.memos:
        onchain = {m["memo"]: m["txid"] for m in json.load(open(a.memos))}
        for r in recs:
            if r["memo"] not in onchain: print(f"anchor {r['seq']}: memo not found on chain"); bad += 1
            elif r["txid"] not in ("dry-run", onchain[r["memo"]]): print(f"anchor {r['seq']}: txid differs"); bad += 1
        room = recs[0]["room"] if recs else None
        mine = {m for m in onchain if m.startswith(f"tg1|{room}|")}
        for m in mine - {r["memo"] for r in recs}: print(f"on chain but not in file: {m[:60]}…"); bad += 1
    print("result:", "OK" if bad == 0 else f"{bad} problem(s)"); sys.exit(0 if bad == 0 else 1)


if __name__ == "__main__":
    main()
