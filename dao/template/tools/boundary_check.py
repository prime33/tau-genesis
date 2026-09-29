#!/usr/bin/env python3
"""The boundary as a test (TEMPLATE §1, §13): each force's specification may declare only the input streams its
`forces.json` entry allows, and no force may declare another force's scratch as input. A wire that is not declared
cannot be read; this checks the declarations. Usage: boundary_check.py <room-dir>; exit 1 on a violation."""
import json, os, re, sys


def stream_types(spec):
    return {m.group(1): (m.group(2) or "tau") for m in re.finditer(r"([A-Za-z_][A-Za-z0-9_.]*)\s*(?::\s*([a-z]+(?:\[[0-9]+\])?))?\s*:=\s*(?:in|out)\s+(?:console|file\([^)]*\))", spec)}


def inputs_of(spec):
    return {m.group(1) for m in re.finditer(r"([A-Za-z_][A-Za-z0-9_.]*)\s*(?::\s*[a-z]+(?:\[[0-9]+\])?)?\s*:=\s*in\s+", spec)}


def check(room):
    forces = json.load(open(os.path.join(room, "forces.json")))
    scratch_owner = {s: f for f, cfg in forces.items() for s in cfg.get("scratch", [])}
    problems = []
    for name, cfg in forces.items():
        p = os.path.join(room, cfg["spec"])
        if not os.path.exists(p): problems.append(f"{name}: spec {cfg['spec']} missing"); continue
        ins = inputs_of(open(p).read())
        extra = ins - set(cfg["may_read"])
        if extra: problems.append(f"{name}: reads undeclared wires {sorted(extra)} (may_read: {cfg['may_read']})")
        for s in ins:
            if s in scratch_owner and scratch_owner[s] != name: problems.append(f"{name}: reads {scratch_owner[s]}'s scratch `{s}`")
    return problems


if __name__ == "__main__":
    pr = check(sys.argv[1]); print("\n".join(pr) if pr else "boundary: ok"); sys.exit(1 if pr else 0)
