#!/usr/bin/env python3
"""Minimal reproducer: IDNI's Python binding (tau-lang 3badb21, bindings/python/nanobind) segfaults in
tau.step() when a vector_input_stream remapped onto an sbf-typed input stream holds a value that the sbf
parser reads as a VARIABLE rather than a constant (e.g. "T", "x"). The same value through the REPL's
console prompt is accepted symbolically (`o1[0] := T`), and a value the parser rejects outright ("F.")
produces a clean `Failed to parse input value` message and step() returns; only the variable case crashes.

Observed (2026-09-29, image tau-oracle:latest on the D24 box, python3 driver inside the image):
    spec = "always o1[t]:sbf = i1[t]:sbf"   (same with `i1 : sbf := in console. o1 : sbf := out console.`)
    value "T"  -> returncode 139 (SIGSEGV) in tau.step(), no Python exception, no stderr
    value "x"  -> returncode 139
    value "F." -> returncode 0, "(Error) [sbf] Syntax Error: Unexpected '.' ... Failed to parse input value"
    value "0"  -> returncode 0, output "0"

Run (needs the image; the transport comes from tau_oracle's environment, e.g. TAU_ORACLE_HOST=tau@<ip>):
    python3 tools/oracle-tests/repro_binding_segfault.py [value]      # default value "T"
D10: this file is for a report to IDNI; it redistributes nothing of theirs.
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from tau_oracle import OracleV1  # noqa: E402

SPEC = "always o1[t]:sbf = i1[t]:sbf"
DRIVER = r'''
import sys
sys.path.insert(0, "/tau-lang/build/release/bindings/python/nanobind")
import tau
spec, value = %r, %r
opts = tau.interpreter_options()
i, o = tau.vector_input_stream(), tau.vector_output_stream()
opts.input_remaps["i1"] = i; opts.output_remaps["o1"] = o
it = tau.get_interpreter(spec, opts)
print("MARK get_interpreter ->", it is not None, flush=True)
i.put(value)
print("MARK step (value %%r)" %% value, flush=True)
r = tau.step(it)                      # <- SIGSEGV here for value "T" / "x"
print("MARK step returned", repr(r), "outputs", o.get_values(), flush=True)
'''


def main():
    value = sys.argv[1] if len(sys.argv) > 1 else "T"
    o = OracleV1(timeout=90)
    argv = o._python_argv()
    p = subprocess.run(argv, input=DRIVER % (SPEC, value), capture_output=True, text=True, timeout=o.timeout)
    print(p.stdout.rstrip()); print(p.stderr.rstrip(), file=sys.stderr)
    print(f"\nspec: {SPEC}\nvalue fed to i1 (sbf): {value!r}\nreturncode: {p.returncode}"
          + ("  (139 = SIGSEGV, the binding crashed without a Python exception)" if p.returncode == 139 else ""))
    return 0 if p.returncode == 139 else 1


if __name__ == "__main__":
    sys.exit(main())
