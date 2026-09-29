"""F4: every FACT in a deliverable cites a ledger record id that resolves. Deliverables are the room's .md files outside
the template itself; a FACT line carries at least one `rec:<12 hex>` and each must exist in a chained file."""
import os, re
import chain
from conftest import chained_files


def test_F04_every_fact_cites_a_resolving_record(room):
    ids = {r["id"] for p in chained_files(room) for r in chain.records(p)}
    bad = []
    for root, dirs, files in os.walk(room):
        dirs[:] = [d for d in dirs if d not in (".git", "candidates")]
        for f in files:
            if not f.endswith(".md") or f == "CHARTER.md": continue
            for n, line in enumerate(open(os.path.join(root, f), encoding="utf-8"), 1):
                if re.search(r"\bFACT\b", line):
                    cited = re.findall(r"rec:([0-9a-f]{12})", line)
                    if not cited or any(c not in ids for c in cited): bad.append((os.path.relpath(os.path.join(root, f), room), n))
    assert not bad, bad
