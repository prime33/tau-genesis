# tau-genesis

A constitutional proposal for the Tau Network, written in 2025 as pseudocode, being reconciled clause by clause with the Tau Language as it actually exists. A verifier decides what holds. Nothing in this repository counts as a Tau specification until the `tau` executable has parsed it, found it satisfiable, and executed it with the asserted outputs.

## Where things stand (29 September 2026)

**Two branches.** `main` is the last signed state of the 2025 genesis and does not move without the author's signature. `genesis-2026`, the default branch, is the reviewed working state: the 2025 proposal untouched, plus the reconciliation work beside it. It will be merged into `main` once the amendment restoration and the vocabulary decisions below carry the author's signature.

**The proposal and the foundation.** The 2025 text targets Tau Meta-Language (TML), which IDNI has since retired. The foundation now is the Tau Language, v0.7, pinned at commit `3badb21` of IDNI's `tau-lang`. The proposal's 370 concepts and 207 claims are quoted in `docs/proposal/`; 134 of its constructs are mapped to Tau constructs with a verdict each in `docs/reconciliation/mapping.md`; 11 faculties the language does not provide are listed in `faculties.md`; and 13 places where proposal and foundation genuinely disagree are argued in `gaps.md`. The vocabulary decisions that resolve the first of those disagreements are in `docs/LANGUEDOC.md`.

**What the verifier has accepted.** Four measurements on 29 September 2026, each against tests written and registered before any generation and never shown to the model:

| Step | Fragments | Verified against the hidden test | On the first attempt |
|---|---|---|---|
| gate predicates of a valid thought (`streams/core/valid_thought.tau`) | 12 | 11 | 2 |
| amendment mechanics (`constitution/update_process.tau`, `consensus_logic.tau`) | 11 | 11 | 10 |
| the three amendments, Family A text | 14 | 14 | 12 |
| a civic policy stream and its three endorsements (moved to a private instance under D31; numbers stand) | 11 | 11 | 9 |

The 47 accepted specifications are in `tools/learner/out/`, each with the attempt that produced it and the `tau-lang` pin in its header; the tests are in `tools/learner/tests/`; the numbers, the misses and every caveat are in `docs/tau-curriculum.md`. An ablation on the same 36 fragments of the last three steps (retrieval and measured idioms removed from the prompt, one attempt each) verified 28 against 31 with them: inside sampling noise, except that the bare prompt produced four parse failures and the full one none. The model brings the logic; the retrieved examples bring Tau's dialect.

**Decided, awaiting signature.** D19: `being` and `alignment_with_being` are constitutional primitives, oriented to and never computed; no emitted specification may name them. D20: the Family A text of the three amendments is canonical; the v3 rewrite in `streams/amendments/` is a known-wrong translation kept for history, and the verifier has now reproduced the Family A side of every clause. D21: weight lives above Tau; endorsement counts are records, never a magnitude. D22: non-retroactive silencing splits by object, records absolute and clauses contestable. D23: the TML target is retired. The six rewrites in LANGUEDOC §2 and the Family A restoration wait for the author's signature.

## How to read this repository

The whole on one page: `docs/MAP.md`. Every term in use, one line each: `docs/LANGUEDOC.md` §3. For a person in a room rather than a reader of code: `dao/template/PARTICIPANTE.md`.

**The 2025 proposal**, unchanged, is everything the original README described: `constitution/`, `streams/`, `amendments/` (now under `streams/amendments/`, v3 form; the Family A text is in git history at `c55ce7c~1`), `manifesto/`, `economy/`, `testnet/`, `agents/seed/`, `tree_of_life/`, `tower_of_babel/`, `transcompiler/`. That README is preserved verbatim as `docs/proposal/README-2025.md`. Its checkmarks describe what the proposal intended; the table above describes what has been verified.

**The 2026 reconciliation** sits beside it:

- `docs/proposal/` — every concept and claim of the proposal, quoted with file and line; open terms.
- `docs/reconciliation/` — the mapping, the faculties, the gaps.
- `docs/LANGUEDOC.md` — the vocabulary both sides use, decided rows and pending rewrites.
- `docs/tau-curriculum.md` — the ordered set of Tau capabilities, what the corpus proves and what the learner has demonstrated.
- `docs/learner-v1.md` — the design of the retrieval-generation-verification loop.
- `dao/` — the template for the three-force room (Affirming, Negating, Reconciling), the weight note. Community instances live in their own private ops (D31).
- `tools/tau_oracle.py` — the verifier wrapper: parse, satisfiability, normalisation, execution through the REPL.
- `tools/spec_diff.py`, `tools/minority_report.py` — what a revision keeps, drops or makes conditional; the record a dropped clause leaves.
- `tools/oracle-tests/` — the D20 toy (both forms of the Babel clause through the verifier), the G09 revision experiment, and the driver's tests.
- `tools/learner/` — the loop, the pre-registered tests, the accepted specifications.

## The rule

The model proposes; the oracle disposes. A specification is accepted only when `tau` at the pinned commit parsed it, `sat` answered `T`, and execution against a test written before generation produced exactly the asserted output series. Every attempt, accepted or not, is logged with the verifier's verbatim answer; the failures are the curriculum. Where the proposal and the foundation disagree, the disagreement is written down with both sides quoted, and the decision is the author's, recorded in LANGUEDOC.

## Running the verifier

The wrapper needs a `tau` binary or a host that has one; it is pinned to `tau-lang` commit `3badb21`, built from IDNI's source under their license. Set one of `TAU_BIN`, `TAU_ORACLE_HOST` or `TAU_PODMAN=1` (see the module docstring), then:

```bash
python3 -m pytest tools/oracle-tests/            # driver tests, run on the host with the binary
python3 tools/oracle-tests/d20-babel/run.py     # Family A vs v3 through the verifier
python3 tools/learner/run.py --fragments valid_thought --tests valid_thought   # needs a model key in the environment
```

No key, token or host address is stored in this repository.

## What is not here

The operational record of this work (decisions, questions, logs, the IDNI corpus index, every learner attempt) is a private repository, and so are the keys. IDNI's language reference and demos are used for research under their license and are not redistributed here; the accepted specifications are this repository's own.

## License

The 2025 proposal is published under the Tau Genesis License (`LICENSE`). Its clause on "alignment with Being" is, under D19, an orientation and not a computable requirement; that reading is the author's to sign.
