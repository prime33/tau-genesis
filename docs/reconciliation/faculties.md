# faculties.md — the faculties deemed necessary (Phase 2)

**Status:** 2026-09-27, brief §3.2. Each faculty is something the mapping (`mapping.md`) found it could not do without. The four candidates the brief named (F1–F4) are here; the rest are what the rows actually revealed. Costs are order-of-magnitude in working days for one person with the corpus already in hand; no figure is a commitment. "Minimal test" is the smallest artefact whose existence proves the faculty exists — an empty results directory is not a result.

Kinds: **tool** (runs, produces an artefact) · **library** (called by tools) · **model** (learned or LLM-backed, must be audited) · **discipline** (a rule people follow, with a check).

Labels: FACT for what the cited sources say; INFERENCE for the need and the cost.

Ordering is by dependency: F1 first, everything else assumes it.

---

## F1 — Tau parse/sat oracle callable from Python

- **Must do.** Given a candidate specification as text: (a) parse it with the real grammar and return the parse tree or the error; (b) answer `sat` / `unsat` / `valid`; (c) `normalize`; (d) run it for *n* steps with given inputs and return the output-stream values; (e) report the free/undefined symbols of a parse tree. All against one pinned tau-lang commit, in a container, so the verifier is the same verifier every time .
- **Why the mapping needs it.** Every verdict in `mapping.md` is untested until this exists (header). Directly: M066 (`statement` = "parses"), M067 (free-symbol listing), M069/M070 (the two native gates are `sat` calls), M034, M098, M102, and every `direct` row.
- **FACT that shapes it.** The Python binding at HEAD exposes `get_interpreter`, `get_inputs_for_step`, `step`, `current_spec` and the stream classes only (`bindings/python/nanobind/tau_nanobind.cpp:l.147-180`); tau-testnet confirms: "tau-lang exposes `sat`/`unsat`/`valid`/`unrealizable` in its C++ API but not through its Python bindings, so a logical contradiction cannot be detected at all" (`tau-testnet/README.md:l.553`). So the oracle either wraps the `tau` REPL binary in line mode (`tau -X < script`, `demos/README.md`) and parses its text, or extends the nanobind module with the four logical procedures from `api<node>` (`src/api.h`, README l.2271-2280). The second is cleaner and is a contribution IDNI's licence assigns to IDNI AG (`LICENSE.md §3`); keep it as a local patch.
- **Kind.** tool + library.
- **Cost.** 3–5 days for the REPL wrapper; 5–8 days for the binding extension (C++ build, pinned commit, container). INFERENCE.
- **Minimal test.** From Python, on the pinned build: `sat("o1[t] = 0 && o1[t] = 1")` → unsat; `sat("always o1[t] = i1[t]")` → sat; running `u[0] = i1[0] && u[1] = i1[1] && u[2] = i1[2]` with the three inputs of `demo_3.5` reproduces its documented `o1` sequence (T, then F from step 3). Output committed as a text log with the commit hash.

## F2 — Pseudocode→Tau translation layer with a formal IR

- **Must do.** Turn a proposal clause into a Tau spec through an intermediate representation that (a) distinguishes the four things the author's notation conflates — *constant* (a value), *stream* (a time-indexed value), *predicate* (a definition), *type* (an ADT) — because Tau's constant/stream distinction decided several verdicts (M013, M088, M124); (b) carries the source `path:line` of every emitted token so `preserves_origin_trace` holds for the translation itself; (c) records which reading was chosen where the author's text allows two (M113 `and (…)` position, M121 formula vs term level, M008 Family A vs B); (d) refuses to emit anything that references an undefined name (F5).
- **Why the mapping needs it.** M110–M125 (the whole notation section), M008, M094 (toys), M085–M089 (the the example town specs). Without an IR, "expressible with work" never becomes expressed.
- **Kind.** tool (translator) + discipline (no emission without a source line; no silent choice).
- **Cost.** 10–20 days for Family C and the skeleton of Family A `if/then`; Family B and prose bodies depend on F8. INFERENCE.
- **Minimal test.** The three toys (M094) round-trip: `alpha := beta and not gamma` → `a = b & g'` → F1 says sat → the IR's provenance points at `streams/dev/example_logic.tau:l.8`. Then C093 (`sewage_priority` clause_007) emits an `always (… -> …)` over `sbf` atoms and F1 accepts it.

## F3 — Spec-diff tool for pointwise-revision reasoning

- **Must do.** Given a running spec before and after a revision (or any two specs A, B): compute and normalize `A & B'` (programs A admits that B drops) and `B & A'` (programs B adds), and the shared part `A & B`; report which `always`/`sometimes` parts were kept, dropped or replaced by the algorithm's three steps (README l.1814-1848); present the result as the *minority report's logical content* — what the revision silenced.
- **Why the mapping needs it.** M027 (`semantic_diff`), M128, M132 (minority report), M133 (disagreement surface), M081 (the alignment-cycle gap), M028. Revision records nothing about what it dropped (FACT, README l.1757-1760); this tool is the only way to make Negating's overruled objections "visibly preserved" (brief §6).
- **Kind.** tool over F1.
- **Cost.** 5–10 days. INFERENCE. The algebra is native (`normalize`, `&`, `'`); the work is reading `this[t]` before and after and presenting the difference.
- **Minimal test.** On the README's minimal example (step 2: running spec requires `o1[t] = 1`, update `o1[t] = 0`): the tool reports "dropped: `always o1[t] = 1`; added: `always o1[t] = 0`; kept: nothing" and the dropped part equals `pre & post'` normalized.

## F4 — `demos/`-style test harness asserting on output streams

- **Must do.** Run a spec for *n* steps with scripted inputs (vector streams are in the binding: `tau.vector_input_stream`, README l.2290-2305) and assert the output-stream values, step by step; keep the scripts as text next to the spec; run in the pinned container; fail loudly on a native crash (tau-testnet reports "a sustained Tau run can hit a native segfault", `tau-testnet/README.md:l.729`).
- **Why the mapping needs it.** M050 (the execution loop), M052 (time constraints), M087 (counts and thresholds), M131 (ADT ledger stream), M023 (does `this[t-k]` resolve? — first open question), and every `expressible with work` row that claims a behaviour over time.
- **Kind.** tool.
- **Cost.** 2–4 days once F1 exists. INFERENCE.
- **Minimal test.** A harness file for `always o[t] = i[t]` with inputs T, F, T asserts outputs T, F, T (the README's own binding example, l.2296-2305), and a second file asserts the `demo_3.5` sequence including the rejected update at step 1 (`u[1] := F`).

## F5 — Definition oracle for `Being` (and every undefined load-bearing name)

- **Must do.** Hold the list of names the proposal uses without defining (open-terms §A–B: `Being`, `heritage_preservation`, `real_world_estimate`, `co_evolution`, …) and refuse, at translation time (F2), to emit any Tau that references one of them until a definition exists and is signed; for `Being` specifically, hold the author's decision among the three LANGUEDOC options (define / declare primitive / replace).
- **Why the mapping needs it.** M001 (not expressible), M005, M074, M082, M084. FACT: Tau's only device for an undefined name is an uninterpreted constant "assigned a default value in a suitable way" (README l.1434-1437), which would make every ethics clause vacuous rather than false.
- **Kind.** discipline (the author decides) + a check in F2.
- **Cost.** 1 day of tooling; the decision is the author's and has no day count. INFERENCE.
- **Minimal test.** F2 rejects `alignment_with_being(x)` with the message "Being: undefined (open-terms §B)"; after a signed definition lands in `docs/LANGUEDOC.md`, the same input is accepted.

## F6 — Stream / predicate / history splitter for `stream`

- **Must do.** Classify every occurrence of "stream" in the proposal (and every `stream_name`, `provides` entry, and `requires` entry) as *specification* (file), *predicate* (clause head) or *history* (version sequence), per LANGUEDOC; flag occurrences that resist classification for the author; never let the author's "stream" be translated as Tau's `stream_variable`.
- **Why the mapping needs it.** M002, M045, M119; the kb's `stream_registry → stream_definition` embedding bridge (0.67) is exactly the homonym this prevents (METRICS bridge list).
- **Kind.** tool (over `docs/proposal/concepts.md` and the `.tau` files) + discipline.
- **Cost.** 2–3 days. INFERENCE.
- **Minimal test.** A table with one row per occurrence (path:line, sense, reviewer) covering 100% of occurrences in `concepts.md`; zero rows left "unclassified" after the author's pass.

## F7 — Weight layer above Tau

- **Must do.** Implement `weight(s, d, t)` from `dao/weight.md` — computed from the ledger per domain, floor not zero, timestamped, contestable, with the contest procedure — and expose it to Reconciling as one input beside the opinion-map direction (M129). Keep it *outside* Tau: the mapping found no weight construct in the language, the testnet or TABA (M010, FACT), and A5 wants it contestable, which Tau's `u` cannot represent.
- **Why the mapping needs it.** M010, M033, M048, M056, M063, M092, M130, M135 — the whole A5 cluster; also M007 (the count that A5 rejects is the only magnitude Tau has).
- **Kind.** library + discipline (the function is Negating's first target, `dao/weight.md`).
- **Cost.** 10–15 days after the ledger holds enough records for `held` to mean anything; before that every seed sits at the floor and the library returns the floor. INFERENCE.
- **Minimal test.** On a synthetic ledger of ~50 records across the three the example town seeds and two domains, the contest procedure runs end to end: an objection file in, two weight values and their diff out, `upheld`/`overruled` recorded — with the civil engineer high on `feasibility` and ordinary on `lived_priority` as A5 states.

## F8 — Natural-language phrase → predicate binder (Family B and ledger content)

- **Must do.** Bind a phrase ("preserves origin trace", "a neighbour says the road flooded") to a predicate name or to an atom of a spec, with three properties the current files lack: the binding is a *function* (one phrase, one predicate — today "defined concepts" and "aligns with defined concepts" go to two predicates, concepts.md `defined_concepts` note); every binding cites the ledger record or proposal line it rests on; and the binder never invents an atom that F5 would reject. For ledger content the binder is a model and must be audited by Negating; for the glossary files it can be an exact table.
- **Why the mapping needs it.** M006, M011 (interaction *content*), M059, M080, M082, M093, M111, M120 — every row where a `sbf`/`tau` atom must stand for something a person said.
- **Kind.** model (for free text) + library (exact table for `core_phrases.tau` / `predicate_phrases.tau`) + discipline (cite or drop).
- **Cost.** v0 exact table: 3–5 days. Free-text binding: open-ended; budget a first 10 days for a the example town-only vocabulary and measure recall against a hand-labelled sample. INFERENCE.
- **Minimal test.** v0: every phrase in `streams/glossary/core_phrases.tau` and `streams/dev/predicate_phrases.tau` binds to exactly one predicate, the two files agree, and the four disagreements concepts.md records are resolved in a signed table. v1: on 100 hand-labelled synthetic ledger records, the binder's atoms are accepted by a reviewer at a stated precision, and every rejected binding cites its record.

## F9 — Spec composer / linker (`requires` / `provides` → one satisfiable spec)

- **Must do.** Take the author's per-file specs and their `requires`/`provides` lists and produce one Tau spec: conjoin definitions, rename clashing predicates, and — the part that matters — detect the composition hazard IDNI measured: "Two total-form rules on the same stream do not compose: conjoined the spec is unsatisfiable and the interpreter fails to build; fed sequentially through `i0` the later one silently supersedes the earlier" (`tau-testnet/README.md:l.521`). Report, per shared output stream, which files write it and whether the composite is satisfiable (F1).
- **Why the mapping needs it.** M014, M019, M038, M042, M070, M089, M102, M119. Tau has no module system (FACT: `spec => [ definitions ] local_spec`, README l.349-352); the constitution is six files.
- **Kind.** tool over F1/F2.
- **Cost.** 5 days. INFERENCE.
- **Minimal test.** Composing the F2 outputs of `autopoietic_logos` and `identity_core` yields a spec F1 calls sat; adding a deliberately conflicting `always` on a shared stream is reported with the two file names, not swallowed.

## F10 — Ledger record ADT and provenance checker

- **Must do.** Define the Tau-side ledger record (`type Record = {author: bv[384], t: bv[64], sha: bv[256], …}` on a tuple-typed file stream, README l.1657-1690) and the host-side checker that makes `preserves_origin_trace` executable: the record id resolves, the quoted span occurs in the stored text, the chain hash verifies, zero tolerance (`dao/TEMPLATE.md §4`, F1–F4 of the fix list). Text, URLs and rationales stay in the private ledger; only hashes and keys enter Tau.
- **Why the mapping needs it.** M020, M022, M068, M131, M132, M134 — every "trace", "record", "ledger" and "origin" row; also M006 (rationale stored as hash).
- **Kind.** library (ADT + hash binding) + tool (checker).
- **Cost.** 3–5 days. INFERENCE.
- **Minimal test.** A synthetic record round-trips through a tuple-typed Tau stream (write, read back, hash equal); the checker rejects a candidate whose quoted span is not in the cited record and accepts one whose span is, with the record id in its report.

## F11 — Seed key registry, including natural seeds

- **Must do.** Give every seed (the three the example town agents, neemrad, the river, the Sierra, later institutions) a `bv[384]` key constant and a signed identity spec; generate the acceptor-guarded composite rule pattern (`tau-testnet/README.md:l.527-529`) so each seed's writes are key-scoped; keep the proxy interface for natural seeds as a marked SLOT with no rule, per A5. The registry is what makes M003, M039, M058, M059, M061 real.
- **Why the mapping needs it.** M003, M039, M058–M064; and gap G05 — Tau's identity model is "whoever holds the key" (`l.391`), so a natural seed without a keyholder is not a seed to Tau.
- **Kind.** tool + discipline (who holds a natural seed's key is a the author decision, not a default).
- **Cost.** 2–3 days for keys and composite-rule generation; the proxy question has no day count. INFERENCE.
- **Minimal test.** Each of the six `agents/seed/*.tau` has a key; a generated composite rule for `endorses` compiles under F1; a write from an unregistered key is refused by the composite's else-branch; the natural seeds' entries carry `proxy_interface: OPEN` and no key-holder.

---

## Dependency order and a first budget

F1 → F4 → F2 (needs F5's list and F6's split as inputs) → F9 → F3 → F10 → F11 → F8 (v0 table first) → F7 (last: needs a ledger with records).

Order-of-magnitude total for v0 of everything: 45–75 days. INFERENCE. The two items with no day count — the definition of Being (F5) and who speaks for the river (F11) — are the author's, and both block rows in `mapping.md` regardless of tooling.
