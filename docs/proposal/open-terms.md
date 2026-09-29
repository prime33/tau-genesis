# Open terms — used but never defined, or not parseable (Phase 1a)

Rule of this file (brief §2a): where I do not understand, I say so here instead of guessing in `concepts.md`. Each entry: where the term is used (FACT, with path and line), what the surrounding text suggests (always **INFERENCE**), and the one question that would close it. Nothing here is a criticism of the proposal; a term left open is a finding about the text, not about the author.

Seeds from `docs/INVENTORY.md`: §4 "requires with no provider" (`agent_stream`, `amendment_protocol`, `universal_glossary`, `concept_definition`, `stream_comparison`, `civic_priority`, `local_agent_identity`, `tau_manifest.json`, `full_manifesto_experience`) and §6 declared-without-definition (`heritage_preservation`, `alignment_in_time`, `budget_amount`, `candidate_stream`, `endorsement_count`, `civic_participation`, `constitutional_execution`). One correction to the seed: `endorsement_count` **is** defined (`streams/civic/palomino/pending_priorities.tau:l.25-27`); it is declared and defined but not provided, so it moves out of this file.

Grouped: A. declared/required, never defined · B. prose terms never defined · C. notation I could not parse · D. structural questions about the text · E. amendment-sourced (brief) terms.

---

## A. Declared or required, never defined

### heritage_preservation
- **INFERENCE:** a fourth pillar alongside ecological/health/tourism, probably cultural or landscape heritage of the example town; the clause that would define it was never written.
- **Question:** What is being preserved — built heritage, cultural heritage (Kogi?), landscape — and by what act does the stream preserve it?

### alignment_in_time
- **Used in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.11` (declare only). Not in provides, not in `interface_map.txt`.
- **INFERENCE:** the chapter's headline property, of which `temporal_coordination` and `rhythmic_emergence` are components; or an earlier name for `temporal_coordination`.
- **Question:** Is `alignment_in_time` a distinct concept (and what is its definition), or a leftover name?

### budget_amount
- **INFERENCE:** the numeric field of a `budget_proposal` ("requested amount", l.25); the registry carries the value.

### candidate_stream
- **Question:** Are `candidate_stream` and `civic_priority_candidate` the same thing? And is the room template's "candidate stream" this construct or a new one?

### civic_participation / constitutional_execution
- **Used in:** `economy/agrs_policy.tau:l.10-11` (declare), `l.45` (clause_006: "it serves civic_participation or constitutional_execution"); `economy/README.md:l.8-9`.
- **INFERENCE:** two reward categories: acting in a civic stream (endorsing, proposing) vs executing constitutional procedure (amending, verifying). Never defined.
- **Question:** What acts count as each, and who verifies "serves"?

### civic_priority
- **INFERENCE:** the author intended `sewage_priority.tau` (or some policy stream) to *be* the civic_priority, i.e. a policy stream provides it by being one; or budget_allocation's requires/provides were swapped.
- **Question:** Which stream provides `civic_priority` — the policy stream that instantiates it, or `budget_allocation.tau` that defines it?

### local_agent_identity
- **INFERENCE:** the three `agents/seed/*.tau` the example town agents are its instances ("Local Agent Identities", `README.md:l.126`); each provides `identity`, not `local_agent_identity`.
- **Question:** Is `local_agent_identity` a role that an `identity` acquires (how?), or a separate concept an agent stream must provide?

### agent_stream / amendment_protocol / universal_glossary
- **Used in:** `streams/amendments/babel_antipattern_principle.tau:l.40` (requires). `universal_glossary` also in prose (`tree_of_life/golden_glossary.md:l.4`, `tower_of_babel/nimrod_and_babel.md:l.5,11`, `tower_of_babel/babel_patterns.md:l.3`, `CHANGELOG.md:l.112`).
- **INFERENCE:** `agent_stream` = any `agents/seed/*.tau`; `amendment_protocol` = `update_process`; `universal_glossary` = `tree_of_life/golden_glossary.md` per CHANGELOG l.112 — but the transcompiler's "glossary" is `streams/glossary/core_phrases.tau`/`transcompiler/index/glossary.json`. Two glossaries, one name.
- **Question:** Which artifact is the "universal semantic glossary" that `shared_glossary_requirement` obliges terms to be defined in — the six-term prose file, the phrase→predicate file, or something not yet written?

### concept_definition
- **Used in:** `streams/core/valid_thought.tau:l.41` (requires), also `git:1d70d83:…:l.45`.
- **INFERENCE:** names the `declare concept` + `define … as:` mechanism as a dependency; or an intended core stream (`identity.tau`, `truth_reference.tau` were also announced and never written).
- **Question:** Is `concept_definition` a stream the author meant to write, or the notation itself?

### stream_comparison
- **Used in:** `streams/meta/ethics.tau:l.44/48` (requires), title l.2. Defined only in the deleted version (`git:4e8d846:streams/meta/ethics.tau:l.26-29`) where it was *provided*.
- **INFERENCE:** the 2025-05-27 rewrite moved the definition out (renaming it `ethical_comparison`) but left the `requires`.
- **Question:** Is `stream_comparison` still a concept, and if so is `ethical_comparison` its replacement?

### tau_manifest.json (as a `requires` entry)
- **Used in:** `testnet/tau_testnet_bootstrap.tau:l.48/52`.
- **INFERENCE:** the filename stands for the concept `bootstrap_manifest` defines ("the pointer to the canonical tau_manifest.json"), i.e. a stream requiring a file.
- **Question:** Can a `requires` entry be a file, and what does it mean for a stream to require a file (existence? hash match?).

### full_manifesto_experience / recursion_point
- **Used in:** `manifesto/interface_map.txt:l.39-41` (epilogue entry only).
- **INFERENCE:** the epilogue "requires" that the reader has streamed all nine chapters and "provides" the moment the reader turns back into the field ("You are a vector in this field", `epilogue.md:l.10`).
- **Question:** Are these two names concepts of the system or a description of the reader's experience? If concepts, what would provide `full_manifesto_experience`?

### co_evolution
- **Used in:** `manifesto/chapter_04-…:l.11` (declare), `l.38`, provides l.51/55; "co-evolutionary need" in ch09 l.38.
- **INFERENCE:** mutual evolution of agents and governance; the author wrote the `if/then` that uses it but not the `define`.
- **Question:** Definition?

### real_world_estimate
- **INFERENCE:** a cost/feasibility figure attached to a proposal, confirmed by a professional (the civil engineer) — the one point where the stream touches something outside the logic.
- **Question:** What is an estimate *of* (cost, feasibility, time), in what form, and what does "confirmed" consist of?

### jurisdictional_fund / queue_status / network_activation / stream_integrity_commitment / genesis_reference (not provided)
- **Used in:** declared and used in `budget_allocation.tau:l.13,58`; `pending_priorities.tau:l.11,44`; `tau_testnet_bootstrap.tau:l.8-11,35-39`. Only `queue_status`, `network_activation`, `bootstrap_manifest` are provided.
- **INFERENCE:** state variables rather than concepts: a fund balance, a queue flag, an activation flag.
- **Question:** Does the author's language distinguish a *concept* (defined once) from a *state* (that changes)? The `=` notation (C below) suggests yes but nothing says so.

### truth_reference / identity (core) / valid_block
- **Used in:** `streams/core/README.md:l.13-16`; `valid_block` existed 2025-05-24→27 (`git:4e8d846`).
- **INFERENCE:** planned core streams; `truth_reference` ("semantic link between declarations and observable states") would be the only construct connecting the logic to the world.
- **Question:** Are these still intended, and is `valid_block` (blocks, hashes, signatures) still part of the proposal or was its deletion a decision?

---

## B. Prose terms never defined

### Being (capitalised)
- **Used in:** `constitution/autopoietic_logos.tau:l.11,35` (`alignment_with_being`); `streams/amendments/freedom_of_semantic_expression.tau:l.3,6` ("reflect Being"); `LICENSE:l.9` ("alignment with Being"); `testnet/README.md:l.8,46` ("Preservation of Being"); `docs/purpose_of_tau.md:l.47` ("Rooted in Being"); `docs/index.md:l.9`; `manifesto/chapter_05` title "Emergence of Being in Action"; `earned_being` (ch04).
- **INFERENCE:** the term everything is "aligned with", never defined; the closest gloss is `alignment_with_being` itself ("the essence of life, awareness, and cosmic necessity", autopoietic_logos l.36-37). It carries the manifesto's Gurdjieff-flavoured sense (centers, octaves, shocks, self-remembering).
- **Question:** Is "Being" a primitive of the proposal (undefined by design), or should it get a definition before anything is formalised against it?

### semantic integrity (lower case) vs `semantic_integrity` (v3 head)
- **Used in:** `constitution/autopoietic_logos.tau:l.32`; `git:c55ce7c~1:amendment_001:l.33`; `streams/amendments/freedom_of_semantic_expression.tau:l.23` (head); `CHANGELOG.md:l.58`.
- **INFERENCE:** the same property; the v3 rewrite promoted the phrase to a head.
- **Question:** Same construct?

### stream (bare)
- **Used in:** everywhere; defined only indirectly as `logic_stream` (`manifesto/chapter_03-…:l.19-21`).
- **INFERENCE:** a `.tau` file = a stream; but `provides` in v3 is "list of logical streams this file outputs" (`transcompiler/stream_format.md:l.10`), so in v3 a clause head is also a stream; and `stream_name` names a file in Family A and a clause head in Family B.
- **Question:** What is the unit called "stream": a file, a clause head, a versioned sequence, or all three?

### thought vs clause vs statement
- **Used in:** `streams/core/valid_thought.tau` ("a thought", "a statement"); `git:1d70d83:…:l.15` ("a statement or clause"); `streams/core/README.md:l.5` ("how a thought is coherent").
- **INFERENCE:** thought = the semantic content of a clause; the v3 predicate `statement` is its carrier.
- **Question:** Is a thought a clause, a stream, or something an agent does with them?

### execute / executable / execution
- **Used in:** `constitution/tau_network.tau:l.50` ("becomes executable under stream_execution_scope"); `constitution/rights_and_agency.tau:l.33` ("forced to contribute, execute, or agree with a stream"); `LICENSE:l.5,15` ("execute… any stream"; "Execution of streams in contradiction to their declared interface"); `docs/purpose_of_tau.md:l.3` ("executable medium"); `transcompiler/README.md:l.33` ("makes meaning *executable*"); `README.md:l.22` ("executable TML logic").
- **INFERENCE:** to run a stream through TML (the transcompiler's claim), but also, for an agent, to act on a stream (rights_and_agency).
- **Question:** What does executing a stream do, and who or what executes it?

### emergence / harmonic emergence
- **Used in:** stream-id prefix of the manifesto; `docs/purpose_of_tau.md:l.51` ("Everything else emerges in resonance"); `docs/theory_of_change.md:l.70`; `testnet/README.md:l.57`; `rhythmic_emergence`, `being_in_action` definitions.
- **INFERENCE:** the appearance of coherence over time (ch06 l.30); used as the proposal's name for its own success condition.
- **Question:** Is emergence an observable (something a system can detect) or the name of the whole program?

### "publicly declared knowledge commons"
- **Used in:** `constitution/rights_and_agency.tau:l.28`.
- **INFERENCE:** the set of streams in the `stream_registry`.
- **Question:** What declares a stream public, and is the registry the commons?

### "declares itself amendable"
- **Used in:** `constitution/rights_and_agency.tau:l.23`.
- **INFERENCE:** a flag a stream would carry; no stream in the tree carries one, so either all are amendable by default or none.
- **Question:** How does a stream declare itself amendable, and what is the default?

### zones: testnet / mainnet / local / forked / sovereign zones
- **Used in:** `constitution/tau_network.tau:l.42`.
- **INFERENCE:** deployment scopes; "sovereign zones" links to `stream_sovereignty`.
- **Question:** Are these five values of `stream_execution_scope`, and what differs between them?

### wisdom_without_execution / auto-mechanical patterns / triadic centers (third center name)
- **Used in:** `manifesto/chapter_01-…:l.33,53`; centers named action/instinctual/movement/instinct across ch01, ch02, ch05, nimrod l.3.
- **INFERENCE:** Gurdjieff's three centers; the third center's name varies with the sentence.
- **Question:** Is the triad fixed as (thought, emotion, action), and is `wisdom_without_execution` meant to be defined symmetrically with `speed_without_understanding`?

### coherence amplifiers / care nodes
- **Used in:** `manifesto/chapter_09-…:l.32`.
- **INFERENCE:** agents or streams that increase coherence / that care for others, to whom surplus flows.
- **Question:** How would either be identified in the system?

### "vector in this field" / "the octave"
- **Used in:** `manifesto/epilogue.md:l.3,10`.
- **INFERENCE:** field = the manifesto's space of coherence; octave = the nine chapters as a musical progression (Law of Octaves).
- **Question:** Is "field" a system construct or a metaphor?

### Law of Octaves
- **Used in:** title of ch06 only (`l.2`); `octave_development` is defined but the "law" is not stated.
- **Question:** What is the law — the statement that intervals require shocks (clause_005)?

### trust-score / trace weight / "number or weight of identity_traces"
- **INFERENCE:** three names for a weighting of identities; the room template's *weight* is the first definition.
- **Question:** Are these three the same quantity, and does the room template's *weight* replace them?

### public logic field / semantic escape / semantic silos
- **Used in:** `streams/amendments/freedom_of_semantic_expression.tau:l.10`; `semantic_resonance_and_integration.tau:l.43`; `git:c55ce7c~1:amendment_003:l.10`.
- **INFERENCE:** public logic field = the commons; semantic escape = leaving a contradiction by forking rather than by alignment_cycle; silos = incompatible sub-languages.
- **Question:** Is "semantic escape" the same act as `fork_resolution`'s "forking to persist transparently"? If so the two amendments/constitution assign it different valences.

### jurisdictional coordination stream / "tagged under" / review criteria / minimum threshold
- **Used in:** `sewage_priority.tau:l.54`; `example_admin.tau:l.18`; `pending_priorities.tau:l.36,41`.
- **Question:** For each: which construct is meant?

### semantic validation / the network manifest / semantic validators
- **Used in:** `economy/agrs_policy.tau:l.29-30`; `economy/README.md:l.32`.
- **INFERENCE:** validation = `validate_tau` + `valid_thought`; manifest = `tau_manifest.json`; validators = the agents with `stream_validation_authority` / `technical_validation`.
- **Question:** Which?

### blocking conflict / verification cycles / stable consensuses
- **Used in:** `constitution/consensus_logic.tau:l.37,47,53`.
- **INFERENCE:** a contradiction that prevents ratification vs one that does not; repeated runs of contradiction_detection; multiple lineages each with finality.
- **Question:** What distinguishes a blocking conflict from a non-blocking one?

### hash / content hash / signed
- **Used in:** `constitution/update_process.tau:l.17`; `constitution/tau_network.tau:l.22`; `testnet/tau_testnet_bootstrap.tau:l.16,30`; `testnet/README.md:l.34` ("Signed SHA-256"); `git:4e8d846:valid_block.tau` ("cryptographic hash", "digital signatures").
- **INFERENCE:** SHA-256 of file bytes (what `tools/tau_publish.py` computes); "signed" has no mechanism.
- **Question:** Hash of what (file bytes, normalised clauses), and what signs?

### Tau testnet charter / The Tau Genesis Assembly / "six constitutional pillars" vs "five founding concepts"
- **Used in:** `tau_testnet_bootstrap.tau:l.40`; `LICENSE:l.32`; `tau_testnet_bootstrap.tau:l.21` vs `constitution/autopoietic_logos.tau:l.55`.
- **INFERENCE:** charter = the constitution + amendments; Assembly = the author/neemrad; "five founding concepts" excludes `genesis_stream` from the six declared (or is a miscount).
- **Question:** Which five?

### post-representational democracy / semantic nervous system / stream cognition principle / Coherence scoring (trace, structure, ethics)
- **Used in:** `docs/index.md:l.11`; `docs/purpose_of_tau.md:l.43`; `CHANGELOG.md:l.14`; `transcompiler/spec.md:l.43`.
- **INFERENCE:** slogans naming intended properties; "coherence scoring" would combine `preserves_origin_trace`, clause structure, and `value_score`.
- **Question:** Are these targets the author wants formalised or framing to leave as prose?

### NSO / TauLang (TML) / Tau Net (as used by the proposal)
- **Used in:** `transcompiler/spec.md:l.12,24,41`; `docs/index.md:l.44`; `README.md:l.37,143`; amendments' titles "of the Tau Net".
- **INFERENCE:** the proposal's names for the foundation it expected to compile into; "NSO" is never expanded. Per brief §2a no IDNI source is consulted here; Phase 1b/2 resolve what these denote on IDNI's side.
- **Question (for Phase 2, not this pass):** what did the author take TML, TauLang, NSO and "Tau Net" to be when writing, and does the 2025 meaning survive the TML→Tau Language migration?

---

## C. Notation I could not parse

### `::`
- **Used in:** `beings::planet_earth` (`ch01:l.31`), `validation_warning::"…"` (`validate_tau.tau:l.15,20,25,29`), `tml_rule::"…"` (`sample_conversions.tau:l.13`).
- **INFERENCE:** namespace qualifier; typed literal; embedded foreign-language literal — three roles.
- **Question:** One operator or three?

### `=`
- **Used in:** `queue_status = active` (`pending_priorities.tau:l.44`), `emergent value = coherence sustained across relationships.` (`ch09:l.50`), `semantic_coherence = true` / `valid_block = true` (`git:4e8d846:valid_block.tau:l.46,49`).
- **INFERENCE:** assignment in the civic/block cases, definition or identity in the manifesto case.
- **Question:** Is `=` assignment, equality test, or definition — and can a `then (…)` block contain assignments?

### `and (…)` block position
- **Used in:** before `then` (update_process, rights_and_agency, ch07–09) and after `then` (autopoietic_logos l.54-56).
- **Question:** Is the `and (…)` after `then` a second consequent, or a separate obligation?

### `because (…)`, `therefore (…)`, `where:`
- **Used in:** ch01 l.38; ch06 l.40, sewage_priority l.52; ch02 l.33, ch05 l.48.
- **INFERENCE:** `because` = justification (not a premise); `therefore` = derived obligation; `where` = side condition on the consequent.
- **Question:** Are these logical connectives with a truth-functional reading, or annotations?

### `insert_shock:` / `function:`
- **Used in:** last numbered clause of every chapter.
- **INFERENCE:** addressed to a human reader; possibly the stream's `interval_shock` applied reflexively; possibly outside the logic.
- **Question:** Are these clauses part of what a stream *provides*, or commentary?

### `superclass_of:`
- **Used in:** ch01 l.17 only.
- **Question:** Is there a class hierarchy among concepts, and does `dissonance ⊃ great_dissonance` mean anything to `requires`/`provides`?

### `if … :` without parentheses
- **Used in:** ch01 l.51-53; `validate_tau.tau:l.14,19,24,28`.
- **Question:** Same construct as `if (…) then (…)`?

### `emit`
- **Used in:** `validate_tau.tau` (warnings), `pending_priorities.tau:l.45` ("is emitted to <stream id>"), amendment 001 ("emit semantic expression"), endorsements ("emitted by").
- **INFERENCE:** the act by which an identity or stream produces a declaration into another stream or the public field — the proposal's word for output/publication.
- **Question:** Is `emit` an operation with a target (stream id) and a payload, and what happens on the receiving stream?

### `requires` referent type
- **Used in:** entries are concept names (`identity_trace`), stream names (`valid_thought`, `agrs`), or a filename (`tau_manifest.json`); `provides` in v3 is "logical streams".
- **Question:** What kind of thing is a `requires` entry, and is `provides`/`requires` matching by exact name intended to be the dependency mechanism (as `naming_conventions.md:l.6` and `transcompiler/spec.md:l.32-33` imply)?

### version scopes
- **Used in:** clause tags (`v0.1.0`, one `v0.1.1`), `meta: version:` (`v0.1.0`/`v0.1.1`), `VERSION` (`v0.2.3-…`), `interface_map.txt` (v0.1.1), `constitution/map.md` (v0.1.0).
- **Question:** How do clause, stream and repo versions relate, and which one is `stream_version`'s "version metadata"?

### `phrase_predicates` where a phrase maps to another clause's head
- **Used in:** `freedom_of_semantic_expression.tau:l.26-27`.
- **Question:** Intended (heads usable as body predicates) or an artifact of the v3 rewrite?

---

## D. Structural questions about the text (recorded here because they block a faithful graph)

### Which amendment text is canonical — Family-A originals (deleted 2025-06-03) or Family-B rewrites?
- FACT: README, purpose doc, testnet README, stream index and CHANGELOG all name the deleted `amendments/amendment_00N_*.tau`; the tree holds only `streams/amendments/*.tau` (v3). Definitions differ in form and, for clause_004/006 heads, in logical direction (see `Conflict` under `semantic_integrity`, `contradiction_mediation`, `prohibition_of_obfuscation`).
- **Question:** Which does the author regard as the amendment: the prose/Family-A text, or the v3 predicate form generated from it?

### `meta:` vs `interface:` — which block is authoritative when they differ?
- FACT: `streams/meta/ethics.tau` (4 vs 2), `streams/meta/memory.tau` (5 vs 3), deleted `valid_thought`/`valid_block` (all heads vs one).
- **INFERENCE:** `meta:` = everything the file defines; `interface:` = what it exports.
- **Question:** Is that the intended distinction?

### Same name, different definitions
- FACT (all recorded as `Conflict` in concepts.md): `alignment_with_being` ×3, `identity` ×4, `identity_trace` ×2, `consensus_threshold` ×2, `stream_endorsement` ×5, `endorsement_rationale` ×3, `agrs_reward` ×2, `value_score` ×2, `semantic_coherence` ×2, `dissonance` (provided twice), plus phrase→predicate divergences (`authored_by_agent`, `has_identity_stream`, `does_not_leak_terms`, `logically_consistent_with_upstream_definitions`, `does_not_contradict_prior_reasoning`, `defined_concepts`/`aligns_with_defined_concepts`).
- **Question:** Does the author's language allow a name to be *instantiated* per stream (the the example town pattern: each agent defines `identity` as itself) — in which case it needs a construct distinguishing definition from instance — or are these to be reconciled?

### `manifesto.lock` vs `interface_map.txt` vs chapter files
- FACT: ch01 and ch06 provides differ; ch07 requires differ; lock omits the epilogue.
- **Question:** Which is the intended dependency map?

### Declared but not provided / defined but not declared
- FACT: `personal_dissonance` (declared with underscore, defined with hyphen, provided only by the lock), `speed_without_understanding` (defined, never declared), `iterative_enactment`, `self_recollection`, `ethical_comparison`, `endorsement_signal`, `endorsement_count` (declared and defined, not provided); `condition_a/b`, `conclusion_c` (used, never declared).
- **Question:** Is `provides` meant to equal the set of declared concepts (`naming_conventions.md:l.6`), or a chosen subset?

### `.tml` files — part of the proposal or build output?
- FACT: byte-reproducible from the `.tau` by `parser_v3.py`; drop descriptions, phrases and `requires`.
- **Question:** Does the author consider the Horn-clause form to *be* the meaning of a Family-B clause?

---

## E. Amendment-sourced (brief) terms left open by the brief itself

### direction
- **INFERENCE:** the sign or orientation of an assessment (for/against, or toward which next state); may be the author's word for what an opinion "points at".
- **Question:** What carries a direction — a weight, a decision, a seed's record — and what are its values?

### next state / "self-amending chain"
- **Used in:** l.209, l.211.
- **INFERENCE:** the sequence of `stream_version`s; "best-assessed step" replaces `consensus_threshold` in `update_process` clause_007.
- **Question:** Is this an amendment to `update_process`/`consensus_logic` (thresholds → weighted assessment) or a layer above them?

### presence (two senses)
- **Used in:** l.208 (stakeholder standing "in the platform, in time"), l.101 (Seven as "the presence" in a channel).
- **Question:** One construct or two?

### floor weight
- **Used in:** l.218. Value not given.
- **Question:** What is the floor, and is it per domain?

### "the July Babel argument"
- **Used in:** l.215 ("Nobody assigns it — not a person, not the collective (the July Babel argument applies to both)").
- FACT: not in the repo, not elsewhere in the brief.
- **Question:** What is it? (It is cited as the reason weight cannot be assigned; the graph needs it.)

### "Route 7"
- **Used in:** l.221, Q12 l.235.
- **Question:** A distinct auditing member, or Seven? (the author's Q12.)

### the Sierra
- **Used in:** l.208, l.223.
- **INFERENCE:** Sierra Nevada de Santa Marta (the example town, "Kogi").
- **Question:** Confirm; and is the seed the mountain, the park, or the Kogi's territory?

### room ↔ the example town streams (the mapping the brief asks for)
- Recorded under `room` in concepts.md as INFERENCE. The brief's l.122 hypothesis (room = Tau specification, interaction = input stream event, Affirming = always-accept `sometimes`, Reconciling = pointwise revision) is Phase 2 material and untested.
- **Question (Phase 2):** as stated in the brief.

### Law of Three vs the manifesto's triad
- FACT: the repo's triad is thought/emotion/action (centers); the room template's is information/knowledge/wisdom (forces). Neither text relates them.
- **Question:** Are they meant to correspond (e.g. Affirming↔?, Negating↔?, Reconciling↔?), or are they independent?
