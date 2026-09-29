"""Conformance suite (TEMPLATE v1): a directory is a room iff these pass. ROOM_DIR names the room. Each test is named for
the template line it enforces (S = section, F = fix-list item, B = boundary)."""
import os, sys, json, pytest
HERE = os.path.dirname(os.path.abspath(__file__)); TOOLS = os.path.join(os.path.dirname(HERE), "tools")
sys.path.insert(0, TOOLS)


@pytest.fixture(scope="session")
def room():
    d = os.environ.get("ROOM_DIR")
    if not d or not os.path.isdir(d): pytest.skip("ROOM_DIR not set")
    return os.path.abspath(d)


def chained_files(room):
    out = [os.path.join(room, "decisions.jsonl"), os.path.join(room, "runs", "runs.jsonl"), os.path.join(room, "anchors", "anchors.jsonl"),
           os.path.join(room, "minority", "minority.jsonl"), os.path.join(room, "consent", "consent.jsonl")]
    led = os.path.join(room, "ledger")
    if os.path.isdir(led): out += [os.path.join(led, f) for f in sorted(os.listdir(led)) if f.endswith(".jsonl")]
    return [p for p in out if os.path.exists(p)]
