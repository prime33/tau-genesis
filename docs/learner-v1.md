# Learner v1 — retrieval + constrained generation + verify loop (design note)

**Status:** design, 2026-09-27. Brief §4.3. Nothing here runs until the author authorises spend under the D15 Anthropic ceiling and answers Q28 (a key of its own). The oracle (F1), the corpus (§4.2), the curriculum and the spec-diff (F3) exist; this is the loop that connects them.

**One sentence.** Given a pseudocode fragment from the proposal plus its LANGUEDOC row, retrieve the nearest verified Tau items, ask the model for a specification and its own test, run the specification through the oracle, feed the oracle's verbatim answer back until it passes or the budget ends, and log every attempt because the log is Learner v2's dataset.

**Rule that governs everything:** the model proposes; the oracle disposes. No specification leaves the loop as "verified" unless `tau` parsed it, `sat` returned `T`, and `interpret()` executed it against the test inputs with the asserted outputs (brief §4, "absolute integrity", operational definition).

## 1. Inputs and outputs

| In | Source |
|---|---|
| Fragment | one clause, stream or predicate of the proposal, Family A or B text verbatim (`docs/proposal/concepts.md` entry, with path and lines) |
| Mapping | its row(s) in `docs/reconciliation/mapping.md` (verdict and target constructs) and any `docs/LANGUEDOC.md` decision that touches its terms (D19 rewrites first) |
| Retrieved context | top-k corpus items by embedding similarity and by capability tag (`kb/tau-corpus/items.jsonl`, `kb/tau.db` chunks), the README grammar (`kb/tau-corpus/grammar.ebnf`), the three pinned README sections the item's tags point to |
| Oracle feedback | verbatim `raw` from `tools/tau_oracle.py` on the previous attempt |

| Out | Where |
|---|---|
| Attempt record | `kb/attempts.db` (SQLite, private ops repo), one row per model call: fragment id, prompt sha, retrieved ids, model id, effort, input/cached/output tokens, USD, the spec proposed, test inputs and expected outputs proposed, `parse`, `sat`, `run` results with the oracle's raw text, verdict ∈ {verified, failed, gave-up}, diagnosis |
| Verified spec | `tools/learner/out/<fragment-id>.tau` + `.test.json` (public repo), only when verified; header cites the attempt id and the tau-lang pin |
| Curriculum column | `docs/tau-curriculum.md` "Learner status" filled from `attempts.db` by script, never by hand: pass rate per capability on the held-out set |

## 2. The loop, per fragment

1. **Retrieve.** k = 8 items: 5 by cosine over the fragment + mapping text (MiniLM, local, as in `kb/build.py`), 3 by the mapping's capability tags with `sat = T` and a trace. Always include the grammar and the D19 forbidden-identifier list.
2. **Generate.** One request, structured output (`output_config.format`) with fields: `spec` (Tau text), `streams` (declared inputs/outputs with types), `test` (3–5 steps of named inputs and the expected outputs), `claims` (what the spec asserts, in one sentence each, for F10's claims block), `unmapped` (any term of the fragment the model could not place; must be honest, not filled). Model: `claude-opus-5`, adaptive thinking, `effort: high` for the first attempt, `xhigh` on the third; `max_tokens` 16k non-streaming. Server-side refusal fallback on (`fallbacks: "default"`); a refusal is logged as an attempt with verdict `refused`.
3. **Guard.** `Oracle.guard(spec)`: `being` and `alignment_with_being` anywhere → the attempt fails before the oracle (D19). Any construct outside the pinned grammar is left to the oracle to reject; the loop does not pre-filter syntax.
4. **Verify.** `parse` → `sat` → `OracleV1.interpret(spec, test.steps)`; compare the oracle's `output_series` with `test.expected` exactly. Each stage's raw text is stored. First failing stage ends the attempt.
5. **Retry.** Up to 5 attempts per fragment. The next prompt appends the failed spec and the oracle's verbatim answer under "the oracle said"; nothing paraphrased. On attempt 4 the retrieval set is refreshed with the 3 nearest items to the *failed spec* instead of the fragment (the model's error is closer to the corpus than the author's prose is).
6. **Stop.** Verified, or gave-up with a diagnosis in one of four classes: `grammar` (never parsed), `unsat` (parsed, never satisfiable: the fragment asserts a contradiction or an undecidable pattern; that is a Phase 2 finding, filed to `gaps.md` as a candidate), `semantic` (ran, wrong outputs: the model's test disagrees with its spec), `unmapped` (the model declared terms it could not place; those go to `open-terms.md`).

## 3. Order of work

Curriculum rows 1, 2, 3, 6 first (streams, temporal operators, satisfiability, pointwise revision), because the constitution's self-amendment maps onto them (M015, M024, M034, M046). Fragments in that order:

1. `streams/core/valid_thought.tau` predicates (Family B; the gate predicates of `dao/TEMPLATE.md` §4) — 12 predicates.
2. `constitution/update_process.tau`, `consensus_logic.tau` (the amendment mechanics).
3. The three amendments in Family A (D20).
4. `streams/policy/palomino/sewage_priority.tau` and its three endorsements, with `endorsement` rewritten per LANGUEDOC (one predicate, M004).
5. Rows 4, 5, 7 of the curriculum (recurrence, `tau` constants, ADTs) for `identity_core`, `rights_and_agency` and the ledger record type (F9).

Rows that the mapping marks **not expressible** or **needs a faculty** are not sent; the learner is not asked to invent what Phase 2 says Tau lacks.

## 4. Evaluation, and what counts

- **Held-out set:** 15 demo specifications from `kb/tau-corpus/items.jsonl` re-expressed as pseudocode in the proposal's own style by hand (the author or the companion, before any run), plus the 27 core proposal files. The demo round-trips have a known-good answer; the proposal files have only the oracle.
- **Metric:** oracle pass rate, three numbers reported separately: parsed, satisfiable, run-asserted. Never eyeballed. Per capability tag for the curriculum column.
- **Baseline to beat:** attempt 1 with no retrieval (grammar only). If retrieval does not raise the pass rate on the demo round-trips, v1 is a prompt, not a learner, and the note says so.
  - **Measured 2026-09-29** (`docs/tau-curriculum.md`, Ablation): on 36 proposal fragments with hidden tests, bare 28/36 vs full 31/36 on the first attempt, inside sampling noise; the robust difference is parse reliability (4 parse failures + 1 unsat under bare, 0 under full). So the note says so: v1 is mostly a prompt in front of a verifier, and retrieval plus idioms pay for themselves on the lookback and multi-output shapes. The demo round-trip set of this bullet was never built; the proposal fragments with pre-registered tests replaced it. Split condition (idioms only) on 25 fragments: 19 verified against 22 full and 20 bare; the prompt components are within noise of each other on first-attempt pass rate.
- **Disagreement surface:** every `unsat` and `semantic` give-up is a row for Phase 2 (`gaps.md`), tagged with the fragment and the oracle's text.

## 5. Spend, caching, batching

- **Ceiling:** D15 Anthropic placeholder for tau-genesis, $382/month; a daily cap of $15 in the runner, hard stop; every attempt's USD from `usage` written to `attempts.db` and summed into the log's `SPEND:` line.
- **Estimate (INFERENCE):** stable prefix (grammar + LANGUEDOC + D19 list + instructions) ≈ 25k tokens, cached after the first call; per attempt ≈ 6k fresh input + 3k output at Opus 5 rates ($5 / $25 per MTok) ≈ $0.11 plus the cached-prefix read. 60 fragments × ≤ 5 attempts ≈ 300 calls ≈ $35–60 for the first full pass. Batches API (50% off, results in any order, keyed by `custom_id`) for the first attempt of every fragment; interactive calls for retries, because each retry depends on the oracle's answer to the previous one.
- **Caching:** tools → system → messages order; the prefix is frozen per run (no timestamps, sorted retrieval ids); `usage.cache_read_input_tokens` checked on every call and logged; zero on the second call means a silent invalidator and the run pauses.

## 5a. Channel (added 2026-09-28)

While the Anthropic organisation is on hold (Q29), generation goes through DigitalOcean Serverless Inference, which serves the Anthropic Messages API at `https://inference.do-ai.run` with a model access key: same request shapes, same list prices, cache counters in `usage`. Differences that bind v1: no `count_tokens` (sizing is a 1-output-token call), no Anthropic Batches API (DigitalOcean's batch product is a later saving; v1's first attempts run interactive), model ids carry the `anthropic-` prefix (`anthropic-claude-opus-5`). Measured on the dry-run of 2026-09-28: median prompt 9,152 tokens, prefix ≈ 4,900, first pass ≈ $11.4 uncached / $8.7 cached, 95 fragments.

## 6. Where it runs, with what key

- On the oracle box, next to the image (`TAU_PODMAN=1`, no ssh hop per call). The runner is a systemd oneshot started by hand, never a timer, until the author says otherwise.
- **Q28:** the only Anthropic key on the desk lives in another project's `.env` (`docs/RESOURCES.md`). Using it here crosses a wall the sweep's standing rules forbid. Learner v1 needs a key of its own, created for tau-genesis, injected into the box at launch as an environment variable (D24: the box never holds `.env` files), and rotated when the run ends.
- Retrieval reads IDNI's corpus at inference time: research use under D10. No fine-tuning, no weights, no redistribution of the items; the verified specs the learner emits are ours, and each carries the attempt id that produced it.

## 7. What v1 does not do

- It does not touch the ledger, the room, or any the example town record: fragments are the public proposal's text.
- It does not decide canonical text: D19/D20 rewrites are inputs, and a verified spec for an amendment is a candidate for the author's signature, not a restoration.
- It does not train anything. Learner v2 (brief §4.4) starts only when `attempts.db` holds hundreds of verified pairs and D10's licence question is answered.

## 8. First step, no spend

`tools/learner/retrieve.py --fragment <concept-id> --dry-run`: retrieval only, prints the k items, the grammar sections and the assembled prompt with its token count (`count_tokens`, no generation). Running it over the 60 fragments above yields the prompt-size distribution and the cache-prefix size, and that number decides the daily cap before the first paid call.
