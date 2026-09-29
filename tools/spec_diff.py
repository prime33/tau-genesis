#!/usr/bin/env python3
"""F3 v1 — spec-diff for pointwise-revision reasoning (faculties.md F3; D22: the diff IS the minority report's logic).

    python3 tools/spec_diff.py before.tau after.tau [--oracle] [--emitters emitters.json] [--inputs i_a,i_b]

v0 compared whole statements as strings. G09's oracle record showed why that is too coarse: revision produced
    (A) && ((B && C && river-never-polluted) || (update))
so a losing clause is not "dropped" — it survives inside a disjunctive branch that is dead under exactly the
inputs that made it matter. v1 therefore parses both specs into a tree (top-level `&&` conjuncts, `||`
disjuncts, `always`/`sometimes` blocks, `!`, atoms kept as strings) and classifies every conjunct of `before`:

  kept          a top-level conjunct of `after` (identical after normalisation, or entailed by one, or present
                in EVERY branch of a top-level disjunction)
  conditional   present in SOME branch of a top-level disjunction of `after`; `branch_condition` is that branch's
                literals (the condition under which the clause is still in force); `lives_only_if` is the
                input-stream part of it, e.g. "i_river_polluted[t] = 0"
  dropped       absent everywhere
plus `added`: top-level conjuncts of `after` not matched by any conjunct of `before`.

Precedence: `!` binds tightest, then `&&`, then `||`; `always`/`sometimes` (`[]`/`<>`) scope rightward as far as
possible, so `always A && B` is `always (A && B)` — the reading Tau's own printer uses (G09 initial_spec is one
unparenthesised `always` over four conjuncts; conjoined always-blocks are printed parenthesised).
Normalisation: whitespace, `:tau`/`:sbf` type annotations stripped, redundant parentheses removed, `&&`/`||`
children sorted (commutative), `always (A && B)` split into `always A && always B` (valid for always, not for
sometimes). "Present in a branch" is syntactic entailment: the clause (a literal or a disjunction of literals)
has a literal that is a conjunct of the branch. With --oracle and a reachable Tau (tools/tau_oracle.py) the
entailment check is `sat(branch && !clause) == F` instead, falling back to the syntactic check on error.

Emitter metadata (--emitters): JSON mapping clause text (any spelling; normalised here) -> seed id.
Unknown -> null. Output: JSON on stdout; exit 0 always (a diff is a finding, not a failure).
Not parsed as operators (kept inside atoms): `->`, `<-`, `<->`, `^^`, `?:`, quantifiers. Tau's normalised
output (`this[t]` / `current_spec()`) does not contain them; hand-written specs using them are compared as text.
"""
from __future__ import annotations

import json, os, re, sys

# ----------------------------------------------------------------------------- normalisation of atoms
_TYPE_ANN = re.compile(r"\s*:\s*(tau|sbf)\b")
_CMP = re.compile(r"\s*(!<=|!>=|!=|!<|!>|<=|>=|=|<|>)\s*")
_PUNCT = re.compile(r"\s*([\[\]\(\),&|+'])\s*")  # brackets and term-level operators carry no spaces


def norm_atom(s: str) -> str:
    s = _TYPE_ANN.sub("", s)
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").strip()
    s = _PUNCT.sub(r"\1", s)
    s = _CMP.sub(r" \1 ", s)
    return re.sub(r"\s+", " ", s).strip()


def strip_comments(text: str) -> str:
    return " ".join(l.split("#", 1)[0].split("//", 1)[0] for l in text.splitlines())


# ----------------------------------------------------------------------------- tree
# node = ("and", [..]) | ("or", [..]) | ("always", node) | ("sometimes", node) | ("not", node) | ("atom", str)

_TEMPORAL = {"always": "always", "[]": "always", "sometimes": "sometimes", "<>": "sometimes"}
_WORD = re.compile(r"(always|sometimes)\b")


class ParseError(ValueError):
    pass


class _P:
    def __init__(self, s: str):
        self.s, self.i, self.n = s, 0, len(s)

    def ws(self):
        while self.i < self.n and self.s[self.i].isspace():
            self.i += 1

    def peek(self, k=2):
        self.ws()
        return self.s[self.i:self.i + k]

    def formula(self):  # or-level
        left = [self.conj()]
        while self.peek() == "||":
            self.i += 2
            left.append(self.conj())
        return _flat("or", left)

    def conj(self):  # and-level
        left = [self.unary()]
        while self.peek() == "&&":
            self.i += 2
            left.append(self.unary())
        return _flat("and", left)

    def unary(self):
        self.ws()
        if self.i >= self.n:
            raise ParseError("unexpected end of formula")
        two = self.s[self.i:self.i + 2]
        m = _WORD.match(self.s, self.i)
        if m:
            self.i = m.end()
            return (_TEMPORAL[m.group(1)], self.formula())  # temporal operators scope to the right as far as possible
        if two in ("[]", "<>"):
            self.i += 2
            return (_TEMPORAL[two], self.formula())
        if self.s[self.i] == "!" and two not in ("!=", "!<", "!>"):
            self.i += 1
            return ("not", self.unary())
        if self.s[self.i] == "(":
            j = _match(self.s, self.i)
            after = self.s[j + 1:].lstrip()
            if after == "" or after[:2] in ("&&", "||") or after[0] in ").":
                # a formula group, not a term parenthesis
                inner = _P(self.s[self.i + 1:j]).parse()
                self.i = j + 1
                return inner
        return self.atom()

    def atom(self):
        start, depth = self.i, 0
        while self.i < self.n:
            c = self.s[self.i]
            two = self.s[self.i:self.i + 2]
            if depth == 0 and two in ("&&", "||"):
                break
            if c in "([":
                depth += 1
            elif c in ")]":
                if depth == 0:
                    break
                depth -= 1
            self.i += 1
        text = self.s[start:self.i].strip()
        if not text:
            raise ParseError(f"empty atom at {start}: {self.s[start:start + 30]!r}")
        return ("atom", norm_atom(text))

    def parse(self):
        node = self.formula()
        self.ws()
        if self.i < self.n and self.s[self.i] == ".":
            self.i += 1; self.ws()
        if self.i < self.n:
            raise ParseError(f"trailing input at {self.i}: {self.s[self.i:self.i + 30]!r}")
        return node


def _match(s: str, i: int) -> int:
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "(":
            depth += 1
        elif s[j] == ")":
            depth -= 1
            if depth == 0:
                return j
    raise ParseError(f"unbalanced parenthesis at {i}")


def _flat(kind, items):
    out = []
    for it in items:
        out.extend(it[1] if it[0] == kind else [it])
    return out[0] if len(out) == 1 else (kind, out)


def parse(text: str):
    """Parse a Tau formula (comments allowed) into a tree."""
    return _P(strip_comments(text)).parse()


def render(node) -> str:
    """Canonical text: sorted commutative children, minimal parentheses, no type annotations."""
    k = node[0]
    if k == "atom":
        return node[1]
    if k in ("always", "sometimes"):
        return f"{k} {render(node[1])}"
    if k == "not":
        c = render(node[1])
        return "!" + (c if node[1][0] == "atom" else f"({c})")
    op = " && " if k == "and" else " || "
    parts = []
    for c in node[1]:
        r = render(c)
        if c[0] in ("and", "or", "always", "sometimes") and not (k == "and" and c[0] == "and"):
            r = f"({r})"
        parts.append(r)
    return op.join(sorted(parts))


def canon(text: str) -> str:
    return render(parse(text))


# ----------------------------------------------------------------------------- conjuncts and branches
def conjuncts(node) -> list:
    """Top-level conjuncts, with `always (A && B)` distributed to `always A`, `always B` (sound for always only)."""
    out = []
    items = node[1] if node[0] == "and" else [node]
    for it in items:
        if it[0] == "always" and it[1][0] == "and":
            out.extend(("always", c) for c in it[1][1])
        else:
            out.append(it)
    return out


def literals(node):
    """(temporal, [literal canonical strings]) for a clause of the form [always] (l1 || l2 ...) or [always] l.
    A spec with no `always` is implicitly always (README grammar section), so a bare formula is treated as always."""
    temporal = "always"
    if node[0] in ("always", "sometimes"):
        temporal, node = node[0], node[1]
    if node[0] == "or":
        return temporal, [render(c) for c in node[1]]
    return temporal, [render(node)]


def _syntactic_entails(branch: list, clause) -> str | None:
    """Return the branch conjunct that entails `clause`, or None. branch: list of conjunct nodes."""
    ct, cl = literals(clause)
    for b in branch:
        if render(b) == render(clause):
            return render(b)
        bt, bl = literals(b)
        if bt == ct == "always" and len(bl) == 1 and bl[0] in cl:
            return render(b)
    return None


def entails(branch: list, clause, oracle=None) -> str | None:
    """Which conjunct (or the whole branch) forces `clause`. Syntactic by default; `sat(branch && !clause) == F` with an oracle."""
    hit = _syntactic_entails(branch, clause)
    if hit or oracle is None:
        return hit
    try:
        b = " && ".join(f"({render(x)})" for x in branch)
        if oracle.sat(f"({b}) && !({render(clause)})") == "F":
            return b
    except Exception:  # noqa: BLE001 — the oracle is optional; the syntactic answer stands
        pass
    return None


_STREAM = re.compile(r"\b([A-Za-z_]\w*)\s*\[")


def streams_of(text: str) -> set:
    return set(_STREAM.findall(text))


def input_part(lits: list, inputs) -> list:
    """Literals that mention only input streams (`inputs` is a set of names, or None for the i-prefix convention)."""
    out = []
    for l in lits:
        names = streams_of(l)
        if names and all((n in inputs) if inputs is not None else n.startswith("i") for n in names):
            out.append(l)
    return out


# ----------------------------------------------------------------------------- emitters
def load_emitters(path_or_map) -> dict:
    raw = json.load(open(path_or_map)) if isinstance(path_or_map, str) else dict(path_or_map or {})
    out = {}
    for k, v in raw.items():
        try:
            c = canon(k)
        except ParseError:
            c = norm_atom(k)
        out[c] = v
        out[_bare(c)] = v
    return out


def _bare(c: str) -> str:
    return c[7:] if c.startswith("always ") else c


def emitter_of(clause_text: str, emitters: dict | None):
    if not emitters:
        return None
    return emitters.get(clause_text) or emitters.get(_bare(clause_text))


# ----------------------------------------------------------------------------- the diff
def diff(before: str, after: str, oracle=None, emitters=None, inputs=None) -> dict:
    """Classify each conjunct of `before` against `after`. `inputs`: iterable of input stream names (None -> i-prefix)."""
    inputs = set(inputs) if inputs is not None else None
    em = load_emitters(emitters) if emitters else {}  # path or dict; idempotent on already-canonical keys
    bt, at = parse(before), parse(after)
    bc, ac = conjuncts(bt), conjuncts(at)
    top = [c for c in ac if c[0] != "or"]
    ors = [c for c in ac if c[0] == "or"]
    branches = [[(i, j, conjuncts(d)) for j, d in enumerate(o[1])] for i, o in enumerate(ors)]

    clauses, matched_after = [], set()
    for c in bc:
        text = render(c)
        rec = {"clause": text, "emitter": emitter_of(text, em), "status": None, "via": None,
               "branch_condition": None, "lives_only_if": None, "branch": None}
        hit = entails(top, c, oracle)
        if hit:
            rec.update(status="kept", via=hit); matched_after.add(hit)
        else:
            for i, o in enumerate(ors):
                hits = [(j, d, entails(d, c, oracle)) for _, j, d in branches[i]]
                if all(h for _, _, h in hits):
                    rec.update(status="kept", via=f"every branch of disjunction {i}",
                               branch_condition=[" && ".join(render(x) for x in d) for _, d, _ in hits], branch=i)
                    break
                live = [(j, d, h) for j, d, h in hits if h]
                if live:
                    j, d, h = live[0]
                    lits = [render(x) for x in d]
                    inp = input_part(lits, inputs)
                    rec.update(status="conditional", via=h, branch_condition=" && ".join(lits),
                               lives_only_if=" && ".join(inp) if inp else None,
                               branch={"disjunction": i, "disjunct": j, "of": len(hits)})
                    break
            if rec["status"] is None:
                rec["status"] = "dropped"
        clauses.append(rec)

    before_texts = {render(c) for c in bc}
    added = []
    for c in ac:
        text = render(c)
        if c[0] == "or":
            bl = [[render(x) for x in conjuncts(d)] for d in c[1]]
            common = [l for l in bl[0] if all(l in b for b in bl[1:])]
            for l in common:
                if l not in before_texts:
                    added.append({"clause": l, "status": "added", "via": f"every branch of disjunction", "branch_condition": None})
            for j, lits in enumerate(bl):
                for l in lits:
                    if l not in common and l not in before_texts:
                        inp = input_part(lits, inputs)
                        added.append({"clause": l, "status": "added_conditional", "branch_condition": " && ".join(lits),
                                      "lives_only_if": " && ".join(inp) if inp else None, "branch": {"disjunct": j, "of": len(bl)}})
        elif text not in before_texts and text not in matched_after:
            added.append({"clause": text, "status": "added", "via": None, "branch_condition": None})

    rep = {
        "kept": [r["clause"] for r in clauses if r["status"] == "kept"],
        "conditional": [r["clause"] for r in clauses if r["status"] == "conditional"],
        "dropped": [r["clause"] for r in clauses if r["status"] == "dropped"],
        "added": [r["clause"] for r in added],
        "clauses": clauses,
        "added_detail": added,
        "disjunctions": [{"index": i, "branches": [" && ".join(render(x) for x in d) for _, _, d in branches[i]]} for i in range(len(ors))],
        "inputs_inferred": inputs is None,
        "normalised_by_oracle": bool(oracle),
    }
    if oracle:
        try:
            rep["sat_before"] = oracle.sat(before)
            rep["sat_after"] = oracle.sat(after)
            rep["sat_conjunction"] = oracle.sat(f"({before}) && ({after})")
        except Exception as e:  # noqa: BLE001
            rep["oracle_error"] = f"{type(e).__name__}: {e}"
    rep["minority_report_lines"] = [
        {"clause": r["clause"], "status": r["status"], "branch_condition": r["branch_condition"],
         "lives_only_if": r["lives_only_if"], "emitter": r["emitter"]}
        for r in clauses if r["status"] in ("dropped", "conditional")
    ]
    return rep


def main():
    argv = sys.argv[1:]
    if len(argv) < 2 or argv[0].startswith("-"):
        print(__doc__); sys.exit(0)
    before, after = open(argv[0]).read(), open(argv[1]).read()
    oracle, emitters, inputs = None, None, None
    if "--oracle" in argv:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from tau_oracle import Oracle
        oracle = Oracle()
    if "--emitters" in argv:
        emitters = load_emitters(argv[argv.index("--emitters") + 1])
    if "--inputs" in argv:
        inputs = [s.strip() for s in argv[argv.index("--inputs") + 1].split(",") if s.strip()]
    print(json.dumps(diff(before, after, oracle, emitters, inputs), indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
