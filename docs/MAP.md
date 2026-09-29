# The whole, on one page (2026-09-29)

**What this is.** A 2025 constitutional proposal written as pseudocode, being turned clause by clause into specifications that a verifier accepts, and a template for communities to run rooms on that logic. Two repositories: this public one holds the formal layer; a private one holds the operational record, and each community holds its own private instance.

**What binds (prose, signed by the author).** The proposal itself, unchanged. The vocabulary decisions in `docs/LANGUEDOC.md`, with a glossary of every term in use. The room constitution in `dao/TEMPLATE.md`: three forces, four rules, seeds, what done looks like.

**What runs (code, tested).**

- The verifier wrapper, `tools/tau_oracle.py`: parse, satisfiability, normalisation, execution of Tau specifications at a pinned commit.
- The learner, `tools/learner/`: takes a proposal fragment, asks a model for a specification, lets the verifier decide, against tests registered before generation. 56 fragments verified so far; the numbers and their caveats are in `docs/tau-curriculum.md`.
- The template runtime, `dao/template/`: eight verbs that write hash-chained, schema-valid records for a room, and a conformance suite that says whether a directory is a room.

**What is measured, not believed.** Every number in this repository is the verifier's or the suite's. Pass rates are on hidden tests. The learner's prompt was ablated twice; the pass rate is the model's, the verifier is the product.

**What is decided, what waits.** Decided: primitives are oriented to and never computed; the amendments' first text is canonical; weight lives above the logic; records are absolute and clauses contestable; the old compiler target is retired; rooms are private by default and disclose by signed decision; tokens stay out; Zcash is a notary, never money. Waiting for the author's signature: six sentence rewrites, the restoration of the amendments' first text, two vocabulary questions the learner raised.

**What is not here.** Keys, hosts, the private record, any community's data, the language reference we work from (research use, not redistributed).

**How to read it.** `README.md` for the state; this page for the shape; `docs/LANGUEDOC.md` §3 for any word; `dao/template/PARTICIPANTE.md` if you are a person in a room, not a reader of code.
