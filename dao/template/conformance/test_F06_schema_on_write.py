"""F6: every record validates against its schema (malformed records are refused on write; this re-checks the files)."""
import os, json
import chain
from validate import validate
from conftest import chained_files

KIND = {"decisions.jsonl": "decision", "runs.jsonl": "run", "anchors.jsonl": "anchor", "consent.jsonl": "consent"}


def test_F06_all_records_schema_valid(room):
    bad = []
    for p in chained_files(room):
        kind = KIND.get(os.path.basename(p), "record")
        for r in chain.records(p):
            try: validate(kind, r)
            except Exception as e: bad.append((os.path.relpath(p, room), r.get("id"), str(e).splitlines()[0][:100]))
    assert not bad, bad


def test_F06_forces_and_variables_valid(room):
    validate("forces", json.load(open(os.path.join(room, "forces.json"))))
    for v in json.load(open(os.path.join(room, "variables.json")))["variables"]: validate("variable", v)
