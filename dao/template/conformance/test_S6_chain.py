"""§6 ledger format: every chained file re-verifies (prev links, hashes, ids)."""
import chain
from conftest import chained_files


def test_S6_every_chain_intact(room):
    bad = [(p, msg) for p in chained_files(room) for ok, msg in [chain.verify(p)] if not ok]
    assert not bad, bad
