"""F7: every agent output carries model, lane, cost, runner. F11: an incomplete or errored run is not gate-eligible (no
DECIDE may rest on it). F14: runs are records in the room, not gitignored."""
import os
import chain


def test_F07_runs_carry_provenance(room):
    for r in chain.records(os.path.join(room, "runs", "runs.jsonl")):
        assert all(k in r for k in ("model", "lane", "cost_usd", "runner", "status")), r["id"]


def test_F11_no_decision_on_incomplete_run(room):
    runs = chain.records(os.path.join(room, "runs", "runs.jsonl"))
    bad_hashes = {r.get("spec_hash") for r in runs if r["status"] != "complete"}
    good_hashes = {r.get("spec_hash") for r in runs if r["status"] == "complete"}
    for d in chain.records(os.path.join(room, "decisions.jsonl")):
        if d["kind"] == "DECIDE":
            assert d.get("spec_hash") not in (bad_hashes - good_hashes), f"{d['id']} rests on an incomplete run"


def test_F14_runs_are_committed(room):
    gi = os.path.join(room, ".gitignore")
    if os.path.exists(gi):
        assert not any(l.strip().startswith("runs") for l in open(gi)), "runs/ is gitignored"
    assert os.path.exists(os.path.join(room, "runs", "runs.jsonl"))
