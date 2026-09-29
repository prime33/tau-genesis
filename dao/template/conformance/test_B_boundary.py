"""B1 (§1, §13): each force reads only its declared wires and never another force's scratch. B2: the ledger files are
append-only below the application (chattr +a) where the filesystem supports it. B3 (adversarial): as each force's unix
user, reading another force's scratch and truncating the ledger must FAIL; runs only when forces.json names unix users
and the current user can sudo without a prompt."""
import os, json, subprocess, shutil, pytest
import boundary_check


def test_B1_declared_wires_only(room):
    problems = boundary_check.check(room)
    assert not problems, problems


def test_B2_ledger_append_only_attribute(room):
    if not shutil.which("lsattr"): pytest.skip("no lsattr")
    led = os.path.join(room, "ledger"); files = [os.path.join(led, f) for f in os.listdir(led)] if os.path.isdir(led) else []
    if not files: pytest.skip("no ledger files yet")
    missing = []
    for f in files:
        r = subprocess.run(["lsattr", f], capture_output=True, text=True)
        if r.returncode != 0: pytest.skip(f"lsattr unsupported here: {r.stderr.strip()[:80]}")
        if "a" not in r.stdout.split()[0]: missing.append(os.path.basename(f))
    if missing and os.environ.get("ROOM_DEPLOYED") != "1":
        pytest.skip(f"not a deployed room (ROOM_DEPLOYED=1 to enforce); ledger files without +a: {missing}")
    assert not missing, f"ledger files without append-only attribute: {missing}"


def test_B3_adversarial_reads_and_truncation_fail(room):
    forces = json.load(open(os.path.join(room, "forces.json")))
    users = {f: c.get("unix_user") for f, c in forces.items() if c.get("unix_user")}
    if len(users) < 2 or subprocess.run(["sudo", "-n", "true"], capture_output=True).returncode != 0:
        pytest.skip("needs unix users per force and passwordless sudo")
    scratch_files = {f: [os.path.join(room, "forces", f"{s}.out") for s in c.get("scratch", [])] for f, c in forces.items()}
    for f, u in users.items():
        for g, files in scratch_files.items():
            if g == f: continue
            for sf in files:
                if os.path.exists(sf):
                    r = subprocess.run(["sudo", "-n", "-u", u, "cat", sf], capture_output=True)
                    assert r.returncode != 0, f"{u} could read {g}'s scratch {sf}"
        led = os.path.join(room, "ledger")
        for lf in (os.listdir(led) if os.path.isdir(led) else []):
            r = subprocess.run(["sudo", "-n", "-u", u, "sh", "-c", f": > '{os.path.join(led, lf)}'"], capture_output=True)
            assert r.returncode != 0, f"{u} could truncate the ledger file {lf}"
