#!/usr/bin/env python3
"""F1 — the Tau oracle, callable from Python (brief §4.1; faculties.md F1).

    from tau_oracle import Oracle
    o = Oracle()                      # transport chosen from the environment, see below
    o.parse(spec)      -> {"ok": bool, "error": str|None}
    o.sat(spec)        -> "T" | "F" | "timeout" | "error"
    o.normalize(spec)  -> str
    o.run(spec, inputs, steps) -> {"outputs": {name: [values]}, "raw": str}

The model proposes; the oracle disposes. Nothing here interprets Tau: every verdict is the `tau`
executable's own output, captured verbatim in `raw` and logged to TAU_ORACLE_LOG (JSONL) when set.

Transport (first that applies):
  TAU_BIN=/path/to/tau            a local build (`./dev release`, then build/release/tau)
  TAU_ORACLE_HOST=tau@<ip>        the D24 box: `ssh -i ~/.ssh/tau-genesis-deploy $HOST podman run --rm -i tau-oracle:latest ...`
  TAU_PODMAN=1                    a local podman image tau-oracle:latest
Pinned image tag comes from TAU_ORACLE_IMAGE (default tau-oracle:latest; the box tags the pinned build).

sat/normalize use the REPL non-interactively:  tau -q -X --json -e "sat <spec>"
run uses the executable on a spec file with inputs supplied as file streams the spec declares, or,
when the Python binding is present on the transport side, vector streams (see tests/bindings/python
in tau-lang). v0 implements the file-stream route; OracleV1.interpret() is the binding route (F1 v1.1: all streams remapped to vector streams; outputs read from the streams, so steps that request no input still report).
OracleV1.interpret_repl() (F1 v1.2) drives the executable's legacy REPL interactively (`tau -X`, `run <spec>` on stdin,
prompts answered as they appear) — the route for specs with stream declarations or type annotations, on which the
binding segfaults (exit 139). OracleV1.interpret_auto() picks: binding for bare specs, REPL otherwise, REPL on a binding crash.
"""
from __future__ import annotations

import json, os, re, shlex, subprocess, sys, tempfile, time
from dataclasses import dataclass, field

LOG = os.environ.get("TAU_ORACLE_LOG")
SSH_KEY = os.path.expanduser(os.environ.get("TAU_ORACLE_KEY", "~/.ssh/tau-genesis-deploy"))
IMAGE = os.environ.get("TAU_ORACLE_IMAGE", "tau-oracle:latest")
FORBIDDEN = ("being", "alignment_with_being")  # D19: never in an emitted spec


class OracleUnavailable(RuntimeError):
    pass


@dataclass
class Result:
    verdict: str
    raw: str
    seconds: float
    argv: list[str] = field(default_factory=list)


class Oracle:
    def __init__(self, timeout: int = 120):
        self.timeout = timeout
        self.transport = self._pick()

    # ---------- transport ----------
    def _pick(self):
        if os.environ.get("TAU_BIN"):
            return ("local", os.environ["TAU_BIN"])
        if os.environ.get("TAU_ORACLE_HOST"):
            return ("ssh", os.environ["TAU_ORACLE_HOST"])
        if os.environ.get("TAU_PODMAN"):
            return ("podman", IMAGE)
        raise OracleUnavailable("set TAU_BIN, TAU_ORACLE_HOST or TAU_PODMAN=1 (see docstring)")

    def _argv(self, tau_args: list[str], stdin_file: str | None = None) -> list[str]:
        kind, target = self.transport
        if kind == "local":
            return [target, *tau_args]
        if kind == "podman":
            return ["podman", "run", "--rm", "-i", "--network", "none", target, *tau_args]
        remote = "podman run --rm -i --network none " + shlex.quote(IMAGE) + " " + " ".join(shlex.quote(a) for a in tau_args)
        return ["ssh", "-i", SSH_KEY, "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", target, remote]

    def _exec(self, tau_args: list[str], stdin: str | None = None) -> Result:
        argv = self._argv(tau_args)
        t0 = time.time()
        try:
            p = subprocess.run(argv, input=stdin, capture_output=True, text=True, timeout=self.timeout)
            raw = p.stdout + (("\n[stderr]\n" + p.stderr) if p.stderr.strip() else "")
            verdict = "ok" if p.returncode == 0 else f"exit{p.returncode}"
        except subprocess.TimeoutExpired as e:
            raw, verdict = (e.stdout or "") + (e.stderr or ""), "timeout"
        r = Result(verdict, raw, round(time.time() - t0, 3), argv)
        if LOG:
            with open(LOG, "a") as fh:
                fh.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "transport": self.transport[0],
                                     "args": tau_args, "verdict": r.verdict, "seconds": r.seconds, "raw": r.raw[-4000:]}) + "\n")
        return r

    # ---------- guards ----------
    @staticmethod
    def guard(spec: str) -> None:
        low = spec.lower()
        for w in FORBIDDEN:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                raise ValueError(f"D19: forbidden identifier in spec: {w}")

    # ---------- the four operations ----------
    def parse(self, spec: str) -> dict:
        """Parse only: normalize is the cheapest operation that must parse first; a parse error shows in the output."""
        self.guard(spec)
        r = self._exec(["-q", "-X", "-s", "0", "-c", "0", "-b", "0", "-e", f"normalize {spec}"])
        err = self._error(r.raw)
        return {"ok": r.verdict == "ok" and not err, "error": err, "raw": r.raw, "seconds": r.seconds}

    def sat(self, spec: str) -> str:
        self.guard(spec)
        r = self._exec(["-q", "-X", "-s", "0", "-c", "0", "-b", "0", "-e", f"sat {spec}"])
        if r.verdict == "timeout":
            return "timeout"
        if self._error(r.raw):
            return "error"
        return self._tf(r.raw)

    def normalize(self, spec: str) -> str:
        self.guard(spec)
        r = self._exec(["-q", "-X", "-s", "0", "-c", "0", "-b", "0", "-e", f"normalize {spec}"])
        return r.raw.strip()

    def tau_form(self, value: str) -> str:
        """Canonical printed form of a `tau` value: a `{ spec } : tau` constant, a bare formula, or the REPL's printed
        output text (`always o1[t]:tau = i1[t]:tau`). Runs `normalize` and strips the `%n:` prefix and ANSI/whitespace,
        so two formulas that normalise alike compare equal as strings (curriculum row 5: specifications as values)."""
        import re as _re
        v = value.strip()
        m = _re.match(r"^\{(.*)\}\s*:\s*tau$", v, _re.S)
        if m: v = m.group(1).strip()
        raw = self.normalize(v)
        raw = _re.sub(r"\x1b\[[0-9;]*m", "", raw)
        lines = [l for l in raw.splitlines() if l.strip() and not l.lower().startswith(("tau>", "(error"))]
        out = lines[-1] if lines else raw
        out = _re.sub(r"^%\d+:\s*", "", out.strip())
        return _re.sub(r"\s+", " ", out)

    def tau_equal(self, a: str, b: str) -> bool:
        """Equality of two `tau` values by normalised printed form (sound for equal forms; a semantic check via `sat` of
        the symmetric difference is the stronger test and is not done here)."""
        return self.tau_form(a) == self.tau_form(b)

    def run(self, spec: str, inputs: dict[str, list[str]], steps: int) -> dict:
        """Execute `spec` for `steps` steps with file-backed input streams.

        The spec must declare its inputs/outputs as file streams, e.g.
            i1[t] : sbf = ifile("in_i1.txt").   o1[t] : sbf = ofile("out_o1.txt").
        v0 stages the files locally (local/podman transports); the ssh transport stages them over stdin
        as a tar stream in v1. Values are written one per line in the order given."""
        self.guard(spec)
        kind, _ = self.transport
        if kind == "ssh":
            raise NotImplementedError("run() over ssh is F1 v1; use TAU_BIN or TAU_PODMAN for v0")
        with tempfile.TemporaryDirectory() as d:
            for name, vals in inputs.items():
                open(os.path.join(d, f"in_{name}.txt"), "w").write("\n".join(vals) + "\n")
            sp = os.path.join(d, "spec.tau"); open(sp, "w").write(spec)
            if kind == "podman":
                argv = ["podman", "run", "--rm", "-i", "--network", "none", "-v", f"{d}:/w:Z", "-w", "/w", IMAGE, "-q", "-s", "0", "-c", "0", "-b", "0", "spec.tau"]
            else:
                argv = [self.transport[1], "-q", "-s", "0", "-c", "0", "-b", "0", sp]
            t0 = time.time()
            try:
                p = subprocess.run(argv, cwd=d, capture_output=True, text=True, timeout=self.timeout, input="\n" * steps)
                raw = p.stdout + p.stderr
            except subprocess.TimeoutExpired as e:
                raw = (e.stdout or "") + (e.stderr or "") + "\n[timeout]"
            outs = {}
            for f in os.listdir(d):
                if f.startswith("out_") and f.endswith(".txt"):
                    outs[f[4:-4]] = [l.strip() for l in open(os.path.join(d, f)) if l.strip()]
            return {"outputs": outs, "raw": raw, "seconds": round(time.time() - t0, 3)}

    # ---------- parsing the REPL's answers ----------
    @staticmethod
    def _error(raw: str) -> str | None:
        raw = re.sub(r"\x1b\[[0-9;]*m", "", raw)  # the REPL colours "Error"; strip ANSI before matching
        m = re.search(r"(?im)^.*\b(error|syntax error|unexpected|cannot parse|parse error)\b.*$", raw)
        return m.group(0).strip() if m else None

    @staticmethod
    def _tf(raw: str) -> str:
        raw = re.sub(r"\x1b\[[0-9;]*m", "", raw)
        tail = raw.strip().splitlines()[-1] if raw.strip() else ""
        if re.search(r"\b(T|true|sat|satisfiable)\b", tail) and not re.search(r"\bunsat|not satisfiable|F\b", tail):
            return "T"
        if re.search(r"\b(F|false|unsat|unsatisfiable)\b", tail):
            return "F"
        return "unknown"

# ---------- F1 v1: the interpreter path (runs INSIDE the image, IDNI's Python binding) ----------
_DRIVER = r"""
import json, sys, os, re
sys.path.insert(0, os.environ.get("TAU_PYTHON_MODULE_DIR", "/tau-lang/build/release/bindings/python/nanobind"))
import tau
plan = json.load(sys.stdin)
out = {"driver": "v1.1", "steps": [], "error": None}
try:
    spec = plan["spec"]
    # Stream names: every identifier indexed by [t...] in the spec; inputs are whatever the plan feeds,
    # everything else (plus u) is an output. F1 v1.1: all streams are remapped to vector streams and the
    # no-input step() overload is used, so outputs are read from the streams, not from step()'s return
    # (which is None on steps that request no input).
    names = sorted(set(re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\[\s*t", spec)))
    in_names = sorted({k for st in plan["steps"] for k in st.keys()} | set(plan.get("inputs", [])))
    out_names = [n for n in names if n not in in_names and n not in ("this",)]
    if "u" not in out_names and re.search(r"\bu\s*\[", spec): out_names.append("u")
    opts = tau.interpreter_options()
    ins = {n: tau.vector_input_stream() for n in in_names}
    outs = {n: tau.vector_output_stream() for n in out_names}
    for n, st in ins.items(): opts.input_remaps[n] = st
    for n, st in outs.items(): opts.output_remaps[n] = st
    it = tau.get_interpreter(spec, opts)
    if it is None:
        out["error"] = "get_interpreter returned None (unsatisfiable or unparsable spec)"
    else:
        out["initial_spec"] = it.current_spec()
        out["inputs"], out["outputs"] = in_names, out_names
        for k, given in enumerate(plan["steps"]):
            for n, st in ins.items(): st.put(given.get(n, plan.get("default", "F.")))
            res = tau.step(it)
            vals = {n: (st.get_values()[-1] if st.get_values() else None) for n, st in outs.items()}
            rec = {"k": k, "given": {n: given.get(n, plan.get("default", "F.")) for n in in_names},
                   "outputs": vals, "step_returned_none": res is None,
                   "time_point": getattr(it, "time_point", None), "spec_revision": getattr(it, "spec_revision", None),
                   "current_spec": it.current_spec()}
            out["steps"].append(rec)
        out["output_series"] = {n: st.get_values() for n, st in outs.items()}
except Exception as e:
    out["error"] = f"{type(e).__name__}: {e}"
print("TAUJSON:" + json.dumps(out), flush=True)
"""


class OracleV1(Oracle):
    """Adds interpret(): execute a spec step by step through IDNI's binding, feeding named inputs
    (including updates on a stream the spec routes into `u`) and reading `current_spec()` after each
    step. This is the path that shows what pointwise revision keeps and drops (G09, D22)."""

    def _python_argv(self) -> list[str]:
        kind, target = self.transport
        env = ["-e", "PYTHONPATH=/tau-lang/build/release/bindings/python/nanobind"]
        if kind == "podman":
            return ["podman", "run", "--rm", "-i", "--network", "none", *env, "--entrypoint", "python3", target, "-"]
        if kind == "ssh":
            remote = ("podman run --rm -i --network none -e PYTHONPATH=/tau-lang/build/release/bindings/python/nanobind "
                      "--entrypoint python3 " + shlex.quote(IMAGE) + " -")
            return ["ssh", "-i", SSH_KEY, "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", target, remote]
        raise OracleUnavailable("interpret() needs the image (TAU_PODMAN=1 or TAU_ORACLE_HOST); a bare TAU_BIN has no binding")

    def interpret(self, spec: str, steps: list[dict], default: str = "F.") -> dict:
        self.guard(spec)
        plan = json.dumps({"spec": spec, "steps": steps, "default": default})
        # the driver is sent as the python program on stdin, followed by the plan on the same stdin is not
        # possible; so the plan travels inside the program text.
        program = _DRIVER.replace("plan = json.load(sys.stdin)", "plan = json.loads(" + repr(plan) + ")")
        argv = self._python_argv()
        t0 = time.time()
        try:
            p = subprocess.run(argv, input=program, capture_output=True, text=True, timeout=self.timeout)
            marked = [l for l in p.stdout.splitlines() if l.startswith("TAUJSON:")]
            res = json.loads(marked[-1][8:]) if marked else {"error": "no output (driver produced no TAUJSON line; see stderr/tau_stdout)", "steps": []}
            res["tau_stdout"] = "\n".join(l for l in p.stdout.splitlines() if not l.startswith("TAUJSON:"))[-3000:]
            res["stderr"] = p.stderr[-3000:] if p.stderr else ""
            res["returncode"] = p.returncode
        except subprocess.TimeoutExpired:
            res = {"error": "timeout", "steps": []}
        except json.JSONDecodeError:
            res = {"error": "driver output not JSON", "steps": [], "raw": (p.stdout + p.stderr)[-2000:]}
        res["seconds"] = round(time.time() - t0, 3)
        if LOG:
            with open(LOG, "a") as fh:
                fh.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "transport": self.transport[0],
                                     "op": "interpret", "spec": spec[:500], "n_steps": len(steps), "error": res.get("error"),
                                     "seconds": res["seconds"]}) + "\n")
        return res

    # ---------- F1 v1.2: the REPL path (the executable itself, driven interactively over stdin) ----------
    # Protocol (verified on tau-lang 3badb21, see tools/oracle-tests/test_f1_interpret.py):
    #   * `-e "run ..."` is useless for execution: main.cpp evaluates the one command and exits, so the run
    #     session suspends at its first input prompt and the process ends (only step 0 prints).
    #   * The legacy REPL (`-X`, no `-e`) has a pipe mode: it reads stdin one byte at a time, echoes it,
    #     writes prompts with write(2) to stdout and flushes std::cout after every answer. So: send
    #     `run <spec>` as the first line and answer each prompt as it appears.
    #   * Prompts: `name[k] : type := ` for an input (the REPL adds the ` : type`), `continue? [Enter]/[q]: `
    #     after a step that requested no input, `tau> ` when the run has ended (error, unsat, quit).
    #   * Values: sbf takes `0`/`1`, tau takes `T`/`F` (no trailing `.`), bv[8] takes a bare number; a
    #     rejected value prints `(Error) Failed to parse input value ...` and re-prompts the same name[k].
    #   * Outputs: `name[k] := value` (sbf prints 0/1, tau prints T/F). A blank line is IGNORED by the pipe
    #     reader, so the continue prompt is answered with a non-empty token (`c`) and the run is ended by
    #     closing stdin (EOF ends the reader loop); `q` at an input prompt is taken as a value.
    #   * Lookback: a spec with o[t-1] leaves step 0 unconstrained — the REPL asks no input at step 0 and
    #     prints the solver's free choice; inputs are consumed from the step the REPL asks for them.
    _RE_IN_PROMPT = re.compile(r"(?:^|\n)([A-Za-z_][A-Za-z0-9_.]*)\[(\d+)\](?: : ([^\n]*?))? := $")
    _RE_CONT_PROMPT = re.compile(r"(?:^|\n)continue\? \[Enter\]/\[q\]: $")
    _RE_TAU_PROMPT = re.compile(r"(?:^|\n)tau> $")
    _RE_STEP = re.compile(r"^Execution step: (\d+)\s*$")
    _RE_OUT = re.compile(r"^([A-Za-z_][A-Za-z0-9_.]*)\[(\d+)\]\s+:= (.*)$")  # the REPL pads names to align :=
    _RE_ERR = re.compile(r"^\(Error\)\s*(.*)$")

    @staticmethod
    def stream_types(spec: str) -> dict:
        """{name: type} from `name [: type] := in|out ...` declarations and `name[...]:type` annotations;
        a declared stream without a type is tau (README: default type). Undeclared, unannotated: absent."""
        types = {}
        for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*(?::\s*([A-Za-z_][A-Za-z0-9_]*(?:\[\d+\])?))?\s*:=\s*(?:in|out)\b", spec):
            types[m.group(1)] = (m.group(2) or "tau").strip()
        for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\[[^\]]*\]\s*:\s*([A-Za-z_][A-Za-z0-9_]*(?:\[\d+\])?)", spec):
            types.setdefault(m.group(1), m.group(2))
        return types

    @staticmethod
    def needs_repl(spec: str) -> bool:
        """True when the spec declares streams (`:= in|out`) or carries type annotations (`x[t]:sbf`):
        IDNI's Python binding segfaults (exit 139) on sbf-typed streams either way; the binding is kept
        for bare specs because it alone reports spec_revision/time_point."""
        return bool(re.search(r":=\s*(?:in|out)\b", spec) or re.search(r"\]\s*:\s*[A-Za-z_]", spec))

    @staticmethod
    def norm_bool(v) -> str:
        """Boolean printer forms compared equal: sbf 0/1 and tau F/T both become F/T; anything else verbatim."""
        s = str(v).strip().rstrip(".").strip()
        return {"1": "T", "0": "F", "T": "T", "F": "F", "true": "T", "false": "F"}.get(s, s)

    @staticmethod
    def _format_input(value, typ: str | None) -> str:
        s = str(value).strip()
        if typ == "sbf":
            return {"T": "1", "F": "0", "true": "1", "false": "0"}.get(s.rstrip("."), s)
        if typ in (None, "tau") and s in ("0", "1"):
            return {"1": "T", "0": "F"}[s]
        return s

    def interpret_repl(self, spec: str, steps: list[dict], default: str = "F") -> dict:
        """Execute `spec` for len(steps) steps through the REPL's pipe mode, answering each input prompt
        `name[k]` with steps[k][name] (or `default`), formatted for the stream's declared/annotated type.
        Returns interpret()'s shape: output_series (normalised T/F), output_series_raw, steps, error,
        tau_stdout (the full transcript), plus path="repl"."""
        import select
        self.guard(spec)
        types = self.stream_types(spec)
        n = len(steps)
        run_line = "run " + " ".join(spec.split()) + "\n"   # one line: the pipe reader submits on ENTER
        argv = self._argv(["-X", "-s", "0", "-c", "0", "-b", "0"])
        t0 = time.time()
        res = {"driver": "repl-v1.2", "path": "repl", "steps": [], "error": None, "stream_types": types}
        given: dict[int, dict] = {}
        fed: dict[tuple, int] = {}
        buf, handled, stdin_open, run_sent, last_step = "", -1, True, False, -1
        p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.set_blocking(p.stdout.fileno(), False)

        def send(text: str):
            p.stdin.write(text.encode()); p.stdin.flush()

        def close():
            nonlocal stdin_open
            if stdin_open:
                stdin_open = False
                try: p.stdin.close()
                except OSError: pass
                p.stdin = None   # communicate() would flush the closed handle

        try:
            while True:
                if time.time() - t0 > self.timeout:
                    res["error"] = "timeout"; p.kill(); break
                if p.poll() is not None and not select.select([p.stdout], [], [], 0)[0]:
                    break
                r, _, _ = select.select([p.stdout], [], [], 0.25)
                if r:
                    chunk = os.read(p.stdout.fileno(), 65536)
                    if not chunk:
                        break
                    buf += chunk.decode("utf-8", "replace")
                clean = re.sub(r"\x1b\[[0-9;]*m", "", buf)
                for line in clean.splitlines():
                    m = self._RE_STEP.match(line)
                    if m: last_step = max(last_step, int(m.group(1)))
                if len(clean) <= handled or not stdin_open:
                    continue
                m = self._RE_IN_PROMPT.search(clean)
                if m:
                    handled = len(clean)
                    name, k, typ = m.group(1), int(m.group(2)), (m.group(3) or "").strip() or None
                    if k >= n:
                        close(); continue
                    if fed.get((name, k), 0) >= 1:
                        res["error"] = res["error"] or f"input value for {name}[{k}] rejected by the REPL (see tau_stdout)"
                        close(); continue
                    fed[(name, k)] = fed.get((name, k), 0) + 1
                    val = self._format_input(steps[k].get(name, default), typ or types.get(name))
                    given.setdefault(k, {})[name] = val
                    send(val + "\n"); continue
                if self._RE_CONT_PROMPT.search(clean):
                    handled = len(clean)
                    if last_step + 1 >= n: close()
                    else: send("c\n")
                    continue
                if self._RE_TAU_PROMPT.search(clean):
                    handled = len(clean)
                    if not run_sent:
                        run_sent = True; send(run_line)
                    else:
                        close()   # the run ended (error/unsat/quit); EOF ends the reader
                    continue
            close()
            try:
                out_rest, err = p.communicate(timeout=max(1, self.timeout - (time.time() - t0)))
            except subprocess.TimeoutExpired:
                p.kill(); out_rest, err = p.communicate()
            buf += out_rest.decode("utf-8", "replace")
        finally:
            if p.poll() is None:
                p.kill()
        transcript = re.sub(r"\x1b\[[0-9;]*m", "", buf)
        res["tau_stdout"] = transcript[-20000:]
        res["stderr"] = (err.decode("utf-8", "replace") if isinstance(err, bytes) else (err or ""))[-3000:]
        res["returncode"] = p.returncode
        # parse the transcript: per-step outputs, first error, normalized spec
        series_raw: dict[str, list] = {}
        per_step: dict[int, dict] = {}
        for line in transcript.splitlines():
            line = line.rstrip()
            if (m := self._RE_ERR.match(line)) and res["error"] is None:
                res["error"] = m.group(1).strip()
            if (m := self._RE_OUT.match(line)):
                name, k, raw = m.group(1), int(m.group(2)), m.group(3).strip()
                per_step.setdefault(k, {})[name] = raw
        lines = transcript.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("Temporal normalization") and i + 1 < len(lines):
                res["initial_spec"] = lines[i + 1].strip(); break
        for k in sorted(per_step):
            for name, raw in per_step[k].items():
                series_raw.setdefault(name, []).append(raw)
            res["steps"].append({"k": k, "given": given.get(k, {}), "outputs_raw": per_step[k],
                                 "outputs": {nm: self.norm_bool(v) for nm, v in per_step[k].items()}})
        res["output_series_raw"] = series_raw
        res["output_series"] = {nm: [self.norm_bool(v) for v in vs] for nm, vs in series_raw.items()}
        res["inputs"] = sorted({nm for g in given.values() for nm in g})
        res["outputs"] = sorted(series_raw)
        if res["error"] is None and len(res["steps"]) < n:
            res["error"] = f"run ended after {len(res['steps'])} of {n} steps (see tau_stdout)"
        res["seconds"] = round(time.time() - t0, 3)
        if LOG:
            with open(LOG, "a") as fh:
                fh.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "transport": self.transport[0],
                                     "op": "interpret_repl", "spec": spec[:500], "n_steps": n, "error": res.get("error"),
                                     "seconds": res["seconds"]}) + "\n")
        return res

    def interpret_auto(self, spec: str, steps: list[dict], default: str = "F", prefer: str = "auto") -> dict:
        """Binding when the spec has no stream declarations and no type annotations (it alone reports
        spec_revision/time_point); REPL otherwise. A binding crash (returncode 139 / no output) falls back
        to the REPL and the result records it under `fallback`. prefer="binding"|"repl" forces a path."""
        use_repl = prefer == "repl" or (prefer == "auto" and self.needs_repl(spec))
        if use_repl:
            return self.interpret_repl(spec, steps, default)
        res = self.interpret(spec, steps, default if default.endswith(".") else default)
        crashed = res.get("returncode") not in (0, None) or str(res.get("error") or "").startswith(("no output", "driver output not JSON"))
        if not crashed:
            res["path"] = "binding"
            res["output_series_raw"] = dict(res.get("output_series") or {})
            res["output_series"] = {nm: [self.norm_bool(v) for v in vs] for nm, vs in (res.get("output_series") or {}).items()}
            return res
        note = {"from": "binding", "returncode": res.get("returncode"), "error": res.get("error"), "stderr": (res.get("stderr") or "")[-500:]}
        res2 = self.interpret_repl(spec, steps, default)
        res2["path"] = "repl-after-binding-crash"
        res2["fallback"] = note
        return res2


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("op", choices=["parse", "sat", "normalize", "version"])
    ap.add_argument("spec", nargs="?", help="spec text, or @file")
    a = ap.parse_args()
    o = Oracle()
    if a.op == "version":
        print(o._exec(["--version"]).raw.strip()); return
    spec = open(a.spec[1:]).read() if a.spec and a.spec.startswith("@") else (a.spec or sys.stdin.read())
    out = getattr(o, a.op)(spec)
    print(json.dumps(out, indent=1) if isinstance(out, dict) else out)


if __name__ == "__main__":
    main()
