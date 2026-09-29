"""§5 approval protocol, F8, F15: a decision exists only with an authenticated signatory, a verifier-approved candidate,
and the suite version; DISCLOSE changes a variable only through a DECIDE."""
import os, json
import chain


def test_S5_decision_has_signatory_and_candidate(room):
    cands = {}
    cd = os.path.join(room, "candidates")
    for f in (os.listdir(cd) if os.path.isdir(cd) else []):
        if f.endswith(".json"): c = json.load(open(os.path.join(cd, f))); cands[c["spec_hash"]] = c
    for d in chain.records(os.path.join(room, "decisions.jsonl")):
        assert d["signatory"]["role"] and len(d["signatory"]["key_id"]) >= 8, d["id"]
        assert d["conformance_version"], d["id"]
        if d["kind"] == "DECIDE":
            assert d.get("spec_hash") in cands and cands[d["spec_hash"]]["sat"] == "T", f"{d['id']}: DECIDE without a satisfiable candidate"


def test_S5_variable_classes_rest_on_decisions(room):
    ids = {d["id"] for d in chain.records(os.path.join(room, "decisions.jsonl"))}
    for v in json.load(open(os.path.join(room, "variables.json")))["variables"]:
        if v["class"] in ("public-by-decision", "shielded"):
            assert v.get("decision") in ids, f"{v['name']}: {v['class']} without a DECIDE"
