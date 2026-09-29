# tau-curriculum — the ordered set of Tau capabilities, each with the demo that proves it

Brief §4.5. Two columns matter: what the **oracle corpus** demonstrates at the pinned commit (FACT, from the corpus build of 2026-09-27: 414 items, 357 oracle calls, every verdict logged), and what the **learner** has demonstrated (none yet: Learner v1 has not run). This doubles as the author's study path: read the demo, run the item id through `tools/tau_oracle.py`, compare.

Source of counts: the private ops repo's `kb/tau-corpus/CURRICULUM-DATA.md` (item ids like `d1.5-L023` = demo 1.5, line 23). The corpus is small, as the brief said it would be: 251 specs and formulas, 49 with streams. Verdict columns are the oracle's, not ours.

| # | Capability | What it is (README, verbatim where quoted) | Proved by (demo / item) | Corpus items · parse ok · sat T/F | Learner status |
|---|---|---|---|---|---|
| 1 | **Streams** | "Streams represent the input and the output of Tau specifications" (README §Streams). `i1[t]`, `o1[t-2]`: a stream at a relative time. | demo 1.1 (`d1.1-L089`, `d1.1-L090`), demo 3.1, README copy example `o[t] = i[t]` (F1 test `test_readme_copy_example`, series T F T) | 51 · 38 · 38/5 | **11/12** valid_thought, **11/11** step 2, **14/14** step 3 (Family A amendments), **11/11** step 4 (a civic policy stream and its endorsements, private instance since D31) on hidden tests (2026-09-29) |
| 2 | **Temporal operators** | `always` quantifies the scoped `t` universally, `sometimes` existentially; a spec is a Boolean combination of such statements (README §Tau specifications). | demo 1.5 (`d1.5-*`), demo 1.1 (`d1.1-L097`–`L100`) | always 12 · 11 · 7/5; sometimes 5 · 5 · 2/3 | `always` **47/48** over four steps; `sometimes` not yet |
| 3 | **Sat semantics** | Satisfiable "if for all inputs, at each point in time, there exist outputs, that do not depend on future inputs while matching the specification" (README §Introduction). `sat`, `unsat`, `valid`; `normalize` decides validity. | demo 1.4, demo 1.5; the D20 toy (`tools/oracle-tests/d20-babel`: Family A **F**, v3 **T**) | sat verdicts over the corpus: T 158 · F 21 · error 9 | 54/54 of the learner's specs satisfiable (four steps) |
| 4 | **Recurrence relations** | Functions/predicates over stream history with an offset in the head (`f[n](x)`), fixpoints bounded by budgets. | demo 1.3 (`d1.3-L032`, `L041`), demo 4.3, demo 5.1 (`enumsteps`) | 65 · 31 · 23/4 | **3/4** lookbacks: `stream_version` (latch), `historical_integrity` (cumulative), `consensus_finality` (two-cycle window) verified first attempt after the idioms block; `evaluates_lineage` 0/5 before it. Output-on-output lookback (`consensus_logic`) 0/5 then 1/1 once the per-output `[0]` idiom was in the prefix (F1 test); step 3 `alignment_cycle` (ordered chain of three latches, four outputs) verified first attempt |
| 5 | **The `tau` type and `tau`-typed constants** | Specifications as values: `{spec}:tau` constants, nested; streams of type `tau` by default. | demo 1.1 (`d1.1-L117`), demo 2.1 (`d2.1-L026`), demo 3.2 | type 17 · 11 · 9/0; constants 7 · 7 · 4/0 | driver ready (F1 v1.3: `tau_form`/`tau_equal`, a `tau`-valued output is compared by normalised form; box test passes); first learner fragment for a spec-as-value not yet run. Open: a `tau`-valued INPUT at the REPL prompt times out at this pin |
| 6 | **Pointwise revision (`u`) and `this`** | "A Tau specification written into this stream, will be interpreted as a potential update. If the proposed update is not satisfiable as a stand-alone specification, no update is performed" (README §Pointwise revision). | demo 3.5 (`d3.5-L039`, `d3.5-L057`, both traced); F1 test `test_readme_update_example_revisions` (revision counter 1, 1, 2); the G09 experiment (`tools/oracle-tests/g09-revision`: the losing clauses survive only in a dead branch) | u 2 · 2 · 2/0; this 1 · 1 · 1/0 | not yet |
| 7 | **Abstract data types** | `type Point = {a: sbf, b: sbf}`, tuple-typed streams, member access, inheritance (`type Line of (Tagged) is …`). | demos 4.1–4.4 (`d4.1-L010`, `L014`); demo 4.1 lines 111–168 executed only in the trimmed rerun (nested Segment literals round-trip; partial copies default the non-copied member) | 70 · 61 · 55/2 (8 sat errors, type-inference examples shown on purpose) | not yet |
| 8 | **Bitvectors** | `bv[n]` terms, arithmetic with widening caps, case split of quantified variables (CVC5 underneath). | demos 2.3, 2.4, 3.4, 5.1 (`d2.3-L060`, `L065`) | 80 · 58 · 40/7 | not yet |
| 9 | Solver (`solve`, `lgrs`, min/max) | Compute a satisfying assignment for the free variables of a formula. | demos 2.1, 2.2, 2.3 (`d2.1-L008`, `L009`) | 40 · 39 · 39/1 | not yet |
| 10 | `sbf` / `fpbf` base algebras | Simple Boolean functions; `fpbf` is a sketch at this pin (demo 3.3), nothing executable. | demo 1.1 (`d1.1-L079`), demo 2.1 (`d2.1-L015`); fpbf: `d3.3-sketch` | sbf 77 · 59 · 53/2; fpbf 1 · 0 | not yet |

## Learner status, first measurement (2026-09-29)

Twelve `valid_thought` predicates, Claude Opus 5 through the DigitalOcean gateway, pre-registered external tests hidden from the model (`tools/learner/tests/valid_thought.json`), oracle at pin `3badb21`, REPL execution path. Numbers are the oracle's; every attempt is in the private `kb/attempts.db`.

| Measure | Baseline (model's own tests) | External (hidden tests) |
|---|---|---|
| parsed | 12 / 12 | 12 / 12 |
| satisfiable | 12 / 12 | 12 / 12 |
| asserted on the model's own test | 11 / 12 | 11 / 12 |
| asserted on the hidden external test | not applicable (own stream names) | **11 / 12** |
| attempts, spend | 45, $2.46 | 17, $0.64 |

The one miss, `evaluates_lineage`, is a Tau semantics lesson rather than a model failure: a spec with `o[t-1]` leaves step 0 to the solver, which chose F, after which the input could never change the output and the REPL stopped asking for it; the model's `[t = 0] ->` guard normalised away. The idiom Tau wants is the demos' explicit initial conjunct, `o[0] = i[0] && o[t] = i[t] & o[t-1]` (demo 3.4), which retrieval did not surface for this fragment. `statement` is verified and *reduced* by design (identity; the parser is the faculty). Verified specs: `tools/learner/out/`.

## Learner status, second measurement (2026-09-29, curriculum step 2)

Eleven fragments of `update_process` and `consensus_logic` (`semantic_diff` and `fork_resolution` not sent: M027 needs F3, M036 not expressible), hidden tests in `tools/learner/tests/step2.json` checked achievable with companion reference specs (11/11) before the run, same model and gateway, retriever now carrying an oracle-verified idioms block.

| Measure | External (hidden tests) |
|---|---|
| parsed · satisfiable | 15 / 15 · 15 / 15 (attempts) |
| fragments verified on the hidden test | **10 / 11**, all ten on the first attempt; `consensus_logic` **11 / 11** on a third measurement (attempt 2, see caveat) |
| lookback fragments verified | 3 / 3 (`stream_version`, `historical_integrity`, `consensus_finality`) |
| attempts, spend | 15, $0.63 (step 1: 62, $3.10) |

The miss, `consensus_logic`, is the first two-output fragment. The model submitted the same spec five times: per-step consensus plus a two-cycle finality window over it (`o_fd[t] = o_sc[t] & o_sc[t-1]`), and the oracle failed the model's own test every time because an output that feeds another output's lookback has its step 0 left to the solver, inputs unasked, unless it gets its own `[0]` conjunct (F1 test `test_output_lookback_needs_initial_conjunct_per_output`). Two lessons, both now in the runner: the idiom is in the prefix, and a spec identical to the previous attempt is named as such in the feedback. Six fragments first hit a DigitalOcean gateway outage (HTTP 500, "credential validation failed", about six minutes) and were rerun once the runner retried instead of abandoning; their attempts count above is complete. Third measurement (the author's go, 2 attempts, $0.13): `consensus_logic` verified-external on attempt 2. Caveat, recorded as a protocol finding: attempt 1 applied the idiom correctly and passed its own test with a two-cycle finality window; the hidden test disagreed (per-step), and the runner's feedback at that time included the oracle's trace against the hidden test, so attempt 2 had seen the expected series before matching it. Weaker evidence than a first-attempt pass; the runner now feeds back only the fact of disagreement. This is the only such case in 79 attempts. `amendment_quorum` was first flagged `reduced` because its output series coincided with one voter's on the test vector; the structural check now also requires a single-input spec, and the row was corrected.

## Learner status, third measurement (2026-09-29, curriculum step 3: the Family A amendments)

Fourteen fragments of the three amendments in their Family A text (D20), hidden tests in `tools/learner/tests/step3.json` checked achievable with companion reference specs (14/14) before the run; the retriever now shows the Family A file from git as canonical with the v3 block labelled the known-wrong translation (G03).

| Measure | External (hidden tests) |
|---|---|
| parsed · satisfiable | 16 / 16 sent to Tau (one answer was not a JSON object and never reached it) |
| fragments verified on the hidden test | **14 / 14**, twelve on the first attempt |
| attempts, spend | 17, $0.90 |

Three results matter beyond the count. `prohibition_of_obfuscation`: the learner re-derived the D20 toy's Family A form from the prose, `o_prohibited = i_obf | i_iso`, `o_complies` its negation, identical to `tools/oracle-tests/d20-babel/family_a.tau`. `semantic_integrity` (001 clause_004): the model wrote the rule in rule form, antecedents implying the two obligations and their absence implying their negation, the D20 direction stated explicitly rather than the v3 head conjunction. `alignment_cycle`: an ordered chain of three latches with four outputs and a per-output `[0]` conjunct, verified on the first attempt at $0.12, the most complex spec the learner has produced. The two retries: `freedom_of_expression` was first read as cumulative ("irrevocable": once violated, lost for good), failed its own test, then the hidden per-step test, and verified on attempt 3 after feedback that named the disagreement without showing the series (the protocol fix from the second measurement, working as intended). Twelve of fourteen first-attempt passes against two of eleven at step 1: the difference is the idioms block, not the model.

## Learner status, fourth measurement (2026-09-29, curriculum step 4: a civic policy stream and its endorsements)

*The fragment texts, tests and verified specs of this step belong to a community instance and moved to its private ops under D31. The measurement stands; the names below are the fragments' own.*

Eleven fragments: the six defined `sewage_priority` concepts, its clause_007 chain, and the endorsement rewrite (one predicate over three seeds, three record outputs, no count: LANGUEDOC 'endorsement', D21) with the three endorsement streams as its instances. Hidden tests in `tools/learner/tests/step4.json`, reference-checked 11/11 before the run.

| Measure | External (hidden tests) |
|---|---|
| parsed · satisfiable | 12 / 12 sent to Tau (one answer not a JSON object) |
| fragments verified on the hidden test | **11 / 11**, nine on the first attempt |
| attempts, spend | 13, $0.41 |

`stream_endorsement` came back as exactly the one-predicate form with no count, and its `unmapped` list names the things the five original definitions carried that the logic does not (the logical/professional distinction, budget status, the candidate as an object). `sewage_priority` clause_007 verified `reduced` by design and, better than the companion's reference, as a chain: the three collapses follow from neglect and the budget justification follows from the three collapses. The two retries were a self-test disagreement and a format failure. The policy's factual premise is not touched by any of this; that is the Reconciling check's territory.

**Correction to the first measurement (recorded).** With the `reduced` rule tightened on 2026-09-29 (series equality alone is not identity; the spec must read exactly one input), the flag was recomputed on all 57 verified rows: 20 changed, and of the eleven step 1 external passes only `statement` remains `reduced` (by design). The first-measurement text above said all were flagged; that flag was the coincidence bug, not a property of the specs. Across four steps, 47 of 48 fragments verified-external; 3 verified rows are `reduced`, all by design (`statement`, `sewage_priority`, and one baseline row).

## Learner status, fourth measurement bis (2026-09-29, the illustrative civic example)

After the community instance's text moved to its private ops (D31), the public tree's own step 4 is the synthetic example under `streams/*/example/`: nine fragments, hidden tests in `tools/learner/tests/step4.json` (reference-checked 9/9 before the run), concepts parsed straight from the stream files. **9 / 9 verified-external, all on the first attempt; 9 attempts, $0.21.** `river_town_priority` (the clause_005 chain) is `reduced` by design; `stream_endorsement` came back as the one-predicate form with three record outputs and no count (D21). The verified specs are in `tools/learner/out/`, so this tree now carries verified specifications of what it contains.

## Ablation: is v1 a learner or a prompt? (2026-09-29, learner-v1.md §4)

Same 36 fragments of steps 2-4, same hidden tests, one attempt each, with the retrieval sections (nearest chunks, corpus items by tag) and the oracle-verified idioms block removed from the prompt; grammar, LANGUEDOC rows, mapping rows and the fragment text kept. Rows carry `condition = bare` in `attempts.db` and never became verified outputs. Spend $1.00.

| First attempt, 36 fragments | bare (grammar + decisions + fragment) | full (+ retrieval + idioms) |
|---|---|---|
| parsed | 32 | 36 |
| satisfiable | 31 | 36 |
| asserted on the model's own test | 29 | 32 |
| **verified on the hidden test** | **28** | **31** |

**Reading (INFERENCE, counts are FACT).** Discordant fragments: six verified only under full, three only under bare; on 36 fragments that difference is inside the model's own sampling noise (a paired sign test on 9 discordant pairs does not reject equality). What is not noise is the failure mode: bare produced four parse failures and one unsatisfiable spec, full produced none, and in three of the four parse failures the first conjunct was the right logic followed by a second `always` block joined with `&&`, which this pin rejects ("Nesting of temporal quantifiers is not allowed"); the fourth, `alignment_cycle`, spent 7,953 output tokens on a `[t = 0] ->` guard and file streams. So: the model brings the logic; retrieval and the idioms bring the dialect, and their measurable contribution is syntactic reliability on the harder shapes (lookbacks, multi-output chains) rather than pass rate on the simple ones. By the design note's own criterion v1 is mostly a prompt in front of a verifier; the retrieval component earns its place on the fragments that need Tau's idioms, and nowhere else yet. Retrieval and idioms were removed together, so their separate contributions are still confounded; a second condition (idioms kept, retrieval removed) costs about $1 and would settle it.

## What "proved" means here

A row is proved for the **corpus** when the oracle parsed the item and, where a verdict applies, answered `sat`/`unsat` in agreement with the demo's own printed answer (18 of 19 printed answers agree; the exception is the bit-vector widening cap that demo 2.4 demonstrates). A row will be proved for the **learner** only when Learner v1, given a pseudocode fragment plus the LANGUEDOC mapping, produces a spec that the oracle parses, sat-checks and executes with asserted outputs (brief §4, "the model proposes; the oracle disposes"). Eyeballing does not count. The number that will go in the last column is the oracle pass rate on held-out demos.

## Known edges at this pin (3badb21), from the corpus build

- `normalize`/`sat` do not see session-level tuple-typed stream declarations that `run` sees (demo 4.1): a spec using ADT streams cannot be checked the way it is executed.
- `sat` of an unresolved definition application answers "unsat" with an error where the demo carries it symbolically (demos 4.2, 4.4).
- `sat` on a bare term answers `F` instead of rejecting.
- The README grammar makes `[index]` mandatory on function and predicate names; every example is index-free.
- Two file-stream definitions on one line mis-parse (demo 4.1 lines 107 and 115); one per line works.

## Study order for the author

Rows 1 → 2 → 3 → 6 first: streams, temporal operators, satisfiability, then pointwise revision, because those four are what the constitution's self-amendment maps onto (mapping.md M015, M024, M034, M046) and what G09 and D22 rest on. Rows 4, 5, 7 next: recurrence, `tau` constants and ADTs are where `valid_thought`'s predicates and the ledger record type will live (faculties F5, F9). Rows 8–10 last; bitvectors and the solver matter for weight arithmetic only after D21's layer exists.
