# Proposal concepts — the author's pole (Phase 1a)

**Scope:** every named construct in `prime33/tau-genesis` at branch `sync/2026-09`, plus the vocabulary the author added in the amendments to ). Read-only pass under brief §2a: this file records the author's language; it does not improve, reconcile, or critique it.

**Ledger discipline.** Every quotation under **the author's definition** is verbatim from the cited path and line numbers (`path:l.N-M`). Anything I inferred is under **Notes:** and prefixed `INFERENCE`. Nothing from IDNI/Tau documentation is used; where the proposal itself names a Tau/TML construct (`TauLang (TML)`, `TML`, `NSO`, `Tau Net`) the name is recorded as the proposal uses it.

**Historical sources.** Five files that the author wrote and later deleted are quoted from git history because they carry the Family-A definitions that the v3 (`phrase_predicates`) rewrites replaced. They are cited as `git:<commit>:<path>` — `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau`, `…002…`, `…003_babel_antipattern.tau`, `git:1d70d83:streams/core/valid_thought.tau`, `git:4e8d846:streams/core/valid_block.tau`, `git:4e8d846:streams/meta/ethics.tau`. FACT: these are the author's text (author `prime33`); they are not in the working tree.

**Entry format** (machine-parsed into `graph.json`):

```
### <name>
**Kind:** concept | agent | stream | predicate | amendment_term      (graph node kind)
**Class:** declared | clause-head | glossary-phrase | chapter | notation | prose-term | toy   (human tag only)
**Defined in:** `path` (clause, l.N-M); …
**the author's definition:**
> verbatim … — `path:l.N-M`
**Also appears in:** `path` (how); …
**Depends on:** `name`, `name` … (names the definition or the file's requires: list actually cites)
**Conflict:** (only when the same name is defined differently in two places; both quoted above)
**Notes:** INFERENCE … (only if needed)
```

Syntax-family codes (A–D) are the ones defined in `docs/INVENTORY.md` §1.

---

## 1. Constitution (`constitution/*.tau`, Family A)

### genesis_stream
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/autopoietic_logos.tau` (clause_006, l.39-45)
**the author's definition:**
> define "genesis_stream" as:
>     a self-originating semantic substrate
>     from which all constitutional order flows and to which it recursively returns.
>
>   note:
>     this stream is itself a declaration of genesis. — `constitution/autopoietic_logos.tau:l.40-45`
**Depends on:** `recursion`
**Notes:** INFERENCE — the only concept whose stream declares `requires: []`; every other stream's `requires` chain terminates here or in a concept provided by a stream that requires it.

### recursion
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/autopoietic_logos.tau` (clause_001, l.14-17)
**the author's definition:**
> define "recursion" as:
>     the self-reference of logic,
>     by which a system may observe, define, and realign its own operations. — `constitution/autopoietic_logos.tau:l.15-17`
**Also appears in:** `constitution/autopoietic_logos.tau` (provides, l.62/66); `testnet/README.md` (l.8 "Declares recursion, evolution, agency, lawfulness, and alignment with Being"); `docs/index.md` (l.11 "lawful recursion"); `README.md` (l.5 "recursive law")
**Depends on:** —

### evolution
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/autopoietic_logos.tau` (clause_002, l.19-22)
**the author's definition:**
> define "evolution" as:
>     the lawful capacity of a stream to refine and re-form itself
>     in response to time, contradiction, or relational feedback. — `constitution/autopoietic_logos.tau:l.20-22`
**Also appears in:** `constitution/autopoietic_logos.tau` (provides, l.62/66); `testnet/README.md` (l.8)
**Depends on:** `lawfulness`

### agency
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/autopoietic_logos.tau` (clause_003, l.24-27)
**the author's definition:**
> define "agency" as:
>     the capacity of beings or collectives to initiate change
>     through declared logic and participatory will. — `constitution/autopoietic_logos.tau:l.25-27`
**Also appears in:** `constitution/autopoietic_logos.tau` (provides, l.62/66); `constitution/rights_and_agency.tau` (title l.2); `testnet/README.md` (l.8, l.44 "Reflexive agency"); `docs/purpose_of_tau.md` (l.10 "recursive agency"); `CONTRIBUTING.md` (l.3)
**Depends on:** —

### lawfulness
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/autopoietic_logos.tau` (clause_004, l.29-32)
**the author's definition:**
> define "lawfulness" as:
>     the condition wherein transformations occur
>     only through semantic integrity and declared procedure. — `constitution/autopoietic_logos.tau:l.30-32`
**Also appears in:** `constitution/autopoietic_logos.tau` (provides, l.62/66); `testnet/README.md` (l.42 "Lawfulness of change"); `streams/README.md` (l.41 "**Lawful** — define stream interfaces and concept scope")
**Depends on:** `semantic_integrity`
**Notes:** INFERENCE — "semantic integrity" here is lower-case prose; whether it is the same construct as the v3 clause head `semantic_integrity` (amendment 001) is not stated. Listed in open-terms.

### alignment_with_being
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/autopoietic_logos.tau` (clause_005, l.34-37); `streams/meta/ethics.tau` (clause_003, l.23-26); `git:4e8d846:streams/meta/ethics.tau` (clause_003, l.21-24)
**the author's definition:**
> define "alignment_with_being" as:
>     coherence between a stream’s evolution and the essence of life,
>     awareness, and cosmic necessity. — `constitution/autopoietic_logos.tau:l.35-37`

> define "alignment_with_being" as:
>     a stream's capacity to promote emergence,
>     reduce fragmentation, and integrate truth with trace. — `streams/meta/ethics.tau:l.24-26`

> define "alignment_with_being" as:
>     the degree to which a stream supports lawful emergence,
>     reflexive coherence, and conscious agency. — `git:4e8d846:streams/meta/ethics.tau:l.22-24`
**Also appears in:** `constitution/autopoietic_logos.tau` (provides); `streams/meta/ethics.tau` (provides in both meta and interface, l.43/47; used in clause_005 l.37); `LICENSE` (l.9 "alignment with Being"); `testnet/README.md` (l.8 "alignment with Being", l.46 "Preservation of Being"); `economy/README.md` (l.26 "**Aligned** with `autopoietic_logos`"); `docs/index.md` (l.9 "semantic harmony with Being")
**Depends on:** `evolution`, `coherence`
**Conflict:** three definitions of the same name: the constitution defines it as coherence with "the essence of life, awareness, and cosmic necessity"; `streams/meta/ethics.tau` defines it as a stream's "capacity to promote emergence, reduce fragmentation, and integrate truth with trace"; the earlier ethics.tau (deleted content) as "the degree to which a stream supports lawful emergence, reflexive coherence, and conscious agency". Both live files list it under `provides`.

### autopoietic_logos
**Kind:** stream
**Class:** stream-id
**Defined in:** `constitution/autopoietic_logos.tau` (stream header, l.1-5); `tree_of_life/golden_glossary.md` (l.2); `tower_of_babel/nimrod_and_babel.md` (l.9)
**the author's definition:**
> # Title: Autopoietic Logos — Genesis Stream of the Semantic Constitution
> # Stream: tau.constitution.autopoietic_logos — `constitution/autopoietic_logos.tau:l.2-3`

> **Autopoietic Logos** – *The “self-creating Word.”* In Tau, this refers to the foundational, self-generating logic of the system – a core stream from which all constitutional rules emerge. The term combines *autopoiesis* (self-creation) with *Logos* (divine Word or rational principle). It signifies that Tau’s law is not fixed by external authority, but continuously evolves from its own living semantic process (much as life continually recreates itself). — `tree_of_life/golden_glossary.md:l.2`

> At the heart of Tau’s philosophy is the concept of the **Autopoietic Logos** – essentially, a self-creating, self-regulating principle of truth or “living word” that underpins the network’s law. — `tower_of_babel/nimrod_and_babel.md:l.9`
**Also appears in:** `constitution/tau_network.tau` (clause_004 l.31 "propagation of `autopoietic_logos`…"); `constitution/autopoietic_logos.tau` (clause_007 l.52 "inherits the principles of the autopoietic_logos"); `constitution/map.md` (l.7, l.41, l.51); `agents/seed/neemrad.tau` (clause_004 l.31); `testnet/tau_testnet_bootstrap.tau` (clause_002 l.20); `LICENSE` (l.19); `CONTRIBUTING.md` (l.24, l.68); `economy/README.md` (l.26); `README.md` (l.5, l.47); `docs/index.md` (l.9); `docs/purpose_of_tau.md` (l.20, l.44); `docs/theory_of_change.md` (l.54); `testnet/README.md` (l.3, l.8, l.41); `testnet/tau_stream_index.json` (l.2); `git:4e8d846:streams/core/valid_block.tau` (clause_006 l.40)
**Depends on:** `genesis_stream`, `recursion`, `evolution`, `agency`, `lawfulness`, `alignment_with_being`
**Notes:** INFERENCE — the stream id (`tau.constitution.autopoietic_logos`), the short name used in `requires`-style references (`autopoietic_logos`), and the prose term ("Autopoietic Logos") are treated here as one construct. The `.tau` never defines "autopoietic_logos" with a `define … as:`; the prose files do.

### identity_trace
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/identity_core.tau` (clause_002, l.19-22); `manifesto/chapter_04_from-nations-to-notions.tau` (clause_002, l.18-20)
**the author's definition:**
> define "identity_trace" as:
>     the verifiable accumulation of one’s participation across logic streams,
>     recorded as declarations, contributions, and semantic updates. — `constitution/identity_core.tau:l.20-22`

> define "identity_trace" as:
>     a persistent, evolving record of one’s contribution, verified understanding, and development across contexts. — `manifesto/chapter_04_from-nations-to-notions.tau:l.19-20`
**Depends on:** `identity`, `logic_stream`
**Conflict:** defined in both `identity_core` (constitution) and manifesto chapter_04; both list it under `provides`. The chapter_04 definition adds "verified understanding, and development"; the constitution definition is stream-scoped ("across logic streams").
**Notes:** INFERENCE — this is the most-required concept in the repo (11 `requires:` lists). The brief's *self-remembering* and *weight* entries (§12) route through it.

### semantic_consistency
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/identity_core.tau` (clause_003, l.24-27)
**the author's definition:**
> define "semantic_consistency" as:
>     the degree to which an agent’s declarations align with their actions
>     across time, streams, and versions. — `constitution/identity_core.tau:l.25-27`
**Also appears in:** `constitution/identity_core.tau` (clause_006 l.41 "an agent maintains semantic_consistency"; provides)
**Depends on:** —

### contribution_record
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/identity_core.tau` (clause_004, l.29-32)
**the author's definition:**
> define "contribution_record" as:
>     a ledger of meaningful clauses, stream edits, or value-injections
>     traceable to an identity and subject to verification. — `constitution/identity_core.tau:l.30-32`
**Also appears in:** `constitution/identity_core.tau` (provides)
**Depends on:** `identity`
**Notes:** INFERENCE — the only place the constitution uses the word "ledger"; the room template's Affirming ledger is a different construct and is not linked to this one anywhere in the repo.

### reflexive_memory
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/identity_core.tau` (clause_005, l.34-37)
**the author's definition:**
> define "reflexive_memory" as:
>     a memory stream by which an agent may recall, reflect on,
>     and amend their own prior reasoning or behavior. — `constitution/identity_core.tau:l.35-37`
**Also appears in:** `constitution/identity_core.tau` (clause_006 l.42; provides); `constitution/tau_network.tau` (clause_003 l.27 "preserving trace, role, and reflexive memory"); `streams/meta/memory.tau` (title l.2 "Reflexive Memory and Trace-Aware Learning")
**Depends on:** `self_amendment`

### self_amendment
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/identity_core.tau` (clause_007, l.49-52)
**the author's definition:**
> define "self_amendment" as:
>     the lawful ability of an identity to revise its own declarations
>     provided such revision is truthfully recorded and logically coherent. — `constitution/identity_core.tau:l.50-52`
**Also appears in:** `constitution/identity_core.tau` (clause_006 l.42; provides); `constitution/rights_and_agency.tau` (requires l.62); `streams/amendments/freedom_of_semantic_expression.tau` (requires l.34; clause_003 phrase "except by original emitter through lawful self_amendment" l.20); `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau` (clause_003 l.26); `testnet/README.md` (l.45 "Self-amendment"); `docs/theory_of_change.md` (l.29-30 "### 3. Self-Amendment"); `tower_of_babel/babel_patterns.md` (l.5, l.11)
**Depends on:** `identity`, `lawfulness`

### stream_version
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/update_process.tau` (clause_001, l.14-17)
**the author's definition:**
> define "stream_version" as:
>     a declared state of a logic stream identified by version metadata
>     and content hash. — `constitution/update_process.tau:l.15-17`
**Also appears in:** `constitution/update_process.tau` (clause_004 l.31 "delta between two stream_versions"; clause_007 l.52 "ratified as a new stream_version"; provides); `constitution/tau_network.tau` (requires l.58)
**Depends on:** `logic_stream`

### proposed_amendment
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/update_process.tau` (clause_002, l.19-22)
**the author's definition:**
> define "proposed_amendment" as:
>     a semantically defined clause or clause set
>     intended to modify or extend a previously versioned stream. — `constitution/update_process.tau:l.20-22`
**Also appears in:** `constitution/update_process.tau` (clause_003 l.27; clause_007 l.46; provides); `constitution/consensus_logic.tau` (requires l.61; clause_003 l.27)
**Depends on:** `stream_version`

### consensus_threshold
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/update_process.tau` (clause_003, l.24-27); `constitution/consensus_logic.tau` (clause_002, l.19-22)
**the author's definition:**
> define "consensus_threshold" as:
>     a context-dependent agreement level
>     required to enact a proposed_amendment as valid law. — `constitution/update_process.tau:l.25-27`

> define "consensus_threshold" as:
>     the minimum necessary degree of logical agreement
>     required to ratify a stream or amendment as valid. — `constitution/consensus_logic.tau:l.20-22`
**Also appears in:** provides of both files; `constitution/update_process.tau` (clause_007 l.46); `economy/agrs_policy.tau` (requires l.57); `streams/amendments/semantic_resonance_and_integration.tau` (requires l.48); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (requires l.56); `git:4e8d846:streams/core/valid_block.tau` (clause_003 l.27; requires l.57); `streams/civic/README.md` (l.20 "required quorum")
**Depends on:** `proposed_amendment`
**Conflict:** defined and provided by two constitutional streams with different wording ("context-dependent agreement level" to enact an amendment "as valid law" vs "minimum necessary degree of logical agreement" to ratify "a stream or amendment as valid").

### semantic_diff
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/update_process.tau` (clause_004, l.29-32)
**the author's definition:**
> define "semantic_diff" as:
>     the delta between two stream_versions,
>     expressed in terms of added, removed, or modified clauses. — `constitution/update_process.tau:l.30-32`
**Also appears in:** `constitution/update_process.tau` (provides)
**Depends on:** `stream_version`, `clause`

### historical_integrity
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/update_process.tau` (clause_005, l.34-37)
**the author's definition:**
> define "historical_integrity" as:
>     the property by which previous versions and their semantics
>     remain referenceable and traceable within the update lineage. — `constitution/update_process.tau:l.35-37`
**Also appears in:** `constitution/update_process.tau` (clause_007 l.49; provides)
**Depends on:** `stream_version`

### recursive_legitimacy
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/update_process.tau` (clause_006, l.39-42)
**the author's definition:**
> define "recursive_legitimacy" as:
>     the requirement that an amendment to a stream
>     respects that stream’s meta-rules and constitutional ancestry. — `constitution/update_process.tau:l.40-42`
**Also appears in:** `constitution/update_process.tau` (clause_007 l.49; provides); `LICENSE` (l.27 "preserve trace, coherence, and recursive legitimacy"); `CONTRIBUTING.md` (l.62 review criterion "Recursive integrity")
**Depends on:** `proposed_amendment`, `constitutional_inheritance`

### semantic_rights
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/rights_and_agency.tau` (clause_001, l.14-18)
**the author's definition:**
> define "semantic_rights" as:
>     the inherent rights of any declared identity
>     to express, contribute, and reason across logic streams
>     without discrimination by role, rank, or resource. — `constitution/rights_and_agency.tau:l.15-18`
**Also appears in:** `constitution/rights_and_agency.tau` (clause_007 l.48; provides)
**Depends on:** `identity`, `logic_stream`

### amendment_rights
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/rights_and_agency.tau` (clause_002, l.20-23)
**the author's definition:**
> define "amendment_rights" as:
>     the lawful power of any identity to propose semantic updates
>     to any stream that declares itself amendable. — `constitution/rights_and_agency.tau:l.21-23`
**Also appears in:** `constitution/rights_and_agency.tau` (clause_007 l.51; provides)
**Depends on:** `identity`, `proposed_amendment`
**Notes:** "declares itself amendable" — no stream in the repo carries such a declaration; see open-terms (`amendable`).

### participation_rights
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/rights_and_agency.tau` (clause_003, l.25-28)
**the author's definition:**
> define "participation_rights" as:
>     the ability to read, reference, fork, and inherit any stream
>     that exists within a publicly declared knowledge commons. — `constitution/rights_and_agency.tau:l.26-28`
**Also appears in:** `constitution/rights_and_agency.tau` (clause_007 l.48; provides)
**Depends on:** `stream_registry`
**Notes:** "publicly declared knowledge commons" is not defined anywhere; see open-terms.

### non_coercion
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/rights_and_agency.tau` (clause_004, l.30-34)
**the author's definition:**
> define "non_coercion" as:
>     the principle that no identity may be forced
>     to contribute, execute, or agree with a stream
>     without their voluntary semantic consent. — `constitution/rights_and_agency.tau:l.31-34`
**Also appears in:** `constitution/rights_and_agency.tau` (clause_007 l.51; provides)
**Depends on:** `semantic_consent`, `identity`

### stream_sovereignty
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/rights_and_agency.tau` (clause_005, l.36-39)
**the author's definition:**
> define "stream_sovereignty" as:
>     the right of a stream to govern its own internal logic
>     provided it does not violate declared principles of its upstream ancestry. — `constitution/rights_and_agency.tau:l.37-39`
**Also appears in:** `constitution/rights_and_agency.tau` (clause_007 l.51; provides); `constitution/map.md` (l.44 "sovereignty")
**Depends on:** `constitutional_inheritance`

### agent_protection
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/rights_and_agency.tau` (clause_006, l.41-44)
**the author's definition:**
> define "agent_protection" as:
>     the guarantee that no semantic agent
>     may be erased, mutated, or redefined without traceable self-consent. — `constitution/rights_and_agency.tau:l.42-44`
**Also appears in:** `constitution/rights_and_agency.tau` (provides)
**Depends on:** `semantic_consent`, `identity_trace`

### semantic_consensus
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/consensus_logic.tau` (clause_001, l.14-17)
**the author's definition:**
> define "semantic_consensus" as:
>     a verifiable alignment among agent-declared logic streams
>     sufficient to enact change or affirm shared meaning. — `constitution/consensus_logic.tau:l.15-17`
**Also appears in:** `constitution/consensus_logic.tau` (clause_007 l.50; provides); `docs/theory_of_change.md` (l.33 "semantic consensus")
**Depends on:** `logic_stream`

### amendment_quorum
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/consensus_logic.tau` (clause_003, l.24-27)
**the author's definition:**
> define "amendment_quorum" as:
>     the number or weight of identity_traces
>     that must contribute or affirm a proposed_amendment. — `constitution/consensus_logic.tau:l.25-27`
**Also appears in:** `constitution/consensus_logic.tau` (clause_007 l.46; provides); `README.md` (l.51 "Quorum, contradiction, and finality rules")
**Depends on:** `identity_trace`, `proposed_amendment`
**Notes:** FACT — "number or weight" is the only place in the repo's `.tau` files where "weight" attaches to identity traces; the room template's *weight* (§12) is the author's 2026 elaboration of it. INFERENCE only as a link; the repo text does not connect them.

### contradiction_detection
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/consensus_logic.tau` (clause_004, l.29-32)
**the author's definition:**
> define "contradiction_detection" as:
>     a process which identifies unresolved logical conflict
>     between coexisting or versioned streams. — `constitution/consensus_logic.tau:l.30-32`
**Also appears in:** `constitution/consensus_logic.tau` (clause_007 l.47; provides); `streams/amendments/semantic_resonance_and_integration.tau` (requires l.48); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (requires l.56))
**Depends on:** `stream_version`

### consensus_finality
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/consensus_logic.tau` (clause_005, l.34-37)
**the author's definition:**
> define "consensus_finality" as:
>     a state in which no further contradiction is found
>     and a semantic consensus remains stable across verification cycles. — `constitution/consensus_logic.tau:l.35-37`
**Also appears in:** `constitution/consensus_logic.tau` (clause_007 l.51; provides)
**Depends on:** `semantic_consensus`, `contradiction_detection`

### fork_resolution
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/consensus_logic.tau` (clause_006, l.39-42)
**the author's definition:**
> define "fork_resolution" as:
>     the semantic and agent-led mechanism for handling competing versions,
>     enabling one lineage to become canonical or forking to persist transparently. — `constitution/consensus_logic.tau:l.40-42`
**Also appears in:** `constitution/consensus_logic.tau` (clause_007 l.53 "fork_resolution only required if multiple stable consensuses persist."; provides))
**Depends on:** `stream_version`, `consensus_finality`

### network_genesis
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/tau_network.tau` (clause_001, l.14-17)
**the author's definition:**
> define "network_genesis" as:
>     the coordination point from which all Tau logic streams
>     declare lineage, interface, and semantic commitment. — `constitution/tau_network.tau:l.15-17`
**Also appears in:** `constitution/tau_network.tau` (provides)
**Depends on:** `logic_stream`, `interface`

### stream_registry
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/tau_network.tau` (clause_002, l.19-22)
**the author's definition:**
> define "stream_registry" as:
>     a recorded map of logic streams,
>     linking each stream to its provides, requires, version, and hash. — `constitution/tau_network.tau:l.20-22`
**Depends on:** `provides`, `requires`, `stream_version`

### agent_linkage
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/tau_network.tau` (clause_003, l.24-27)
**the author's definition:**
> define "agent_linkage" as:
>     the mechanism by which identities bind themselves to stream participation,
>     preserving trace, role, and reflexive memory across execution. — `constitution/tau_network.tau:l.25-27`
**Also appears in:** `constitution/tau_network.tau` (provides)
**Depends on:** `identity`, `reflexive_memory`

### constitutional_inheritance
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/tau_network.tau` (clause_004, l.29-32)
**the author's definition:**
> define "constitutional_inheritance" as:
>     the propagation of `autopoietic_logos`, `identity_core`, `rights_and_agency`,
>     and `update_process` into all network-recognized semantic structures. — `constitution/tau_network.tau:l.30-32`
**Also appears in:** `constitution/tau_network.tau` (clause_007 l.49; provides); `CONTRIBUTING.md` (l.33 "constitutional inheritance")
**Depends on:** `autopoietic_logos`, `identity_core`, `rights_and_agency`, `update_process`
**Notes:** FACT — `consensus_logic` is not in the propagated set, though it is one of the "six constitutional pillars" (`testnet/tau_testnet_bootstrap.tau:l.21`). Recorded, not judged.

### trustless_coherence
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/tau_network.tau` (clause_005, l.34-37)
**the author's definition:**
> define "trustless_coherence" as:
>     a network condition where agents may compute alignment and stream integrity
>     without privileged intermediaries or opaque computation. — `constitution/tau_network.tau:l.35-37`
**Also appears in:** `constitution/tau_network.tau` (provides); `testnet/README.md` (l.43 "Trustless traceability")
**Depends on:** —

### stream_execution_scope
**Kind:** concept
**Class:** declared
**Defined in:** `constitution/tau_network.tau` (clause_006, l.39-42)
**the author's definition:**
> define "stream_execution_scope" as:
>     the declared domain within which a stream operates,
>     including testnet, mainnet, local, forked, or sovereign zones. — `constitution/tau_network.tau:l.40-42`
**Depends on:** —
**Notes:** the five zone names — `testnet`, `mainnet`, `local`, `forked`, `sovereign zones` — are used here only and never defined; see open-terms.

### identity_core
**Kind:** stream
**Class:** stream-id
**Defined in:** `constitution/identity_core.tau` (l.1-5)
**the author's definition:**
> # Title: Identity Core — Foundational Structure of Individualized Agency
> # Stream: tau.constitution.identity_core — `constitution/identity_core.tau:l.2-3`
**Also appears in:** `constitution/tau_network.tau` (clause_004 l.31); `constitution/map.md` (l.13-14, l.42 "defines agents and traceability"); `README.md` (l.48); `docs/purpose_of_tau.md` (l.23); `testnet/README.md` (l.11); `testnet/tau_stream_index.json` (l.4))
**Depends on:** `genesis_stream`

### update_process
**Kind:** stream
**Class:** stream-id
**Defined in:** `constitution/update_process.tau` (l.1-5)
**the author's definition:**
> # Title: Update Process — Mechanism for Semantic Amendments and Constitutional Evolution
> # Stream: tau.constitution.update_process — `constitution/update_process.tau:l.2-3`
**Also appears in:** `constitution/tau_network.tau` (clause_004 l.32); `constitution/map.md` (l.13, l.43); `LICENSE` (l.21); `CONTRIBUTING.md` (l.29); `README.md` (l.49); `docs/purpose_of_tau.md` (l.24); `docs/theory_of_change.md` (l.30); `testnet/README.md` (l.12); `testnet/tau_stream_index.json` (l.5)
**Depends on:** `genesis_stream`

### rights_and_agency
**Kind:** stream
**Class:** stream-id
**Defined in:** `constitution/rights_and_agency.tau` (l.1-5)
**the author's definition:**
> # Title: Rights and Agency — Semantic Rights, Powers, and Protections
> # Stream: tau.constitution.rights_and_agency — `constitution/rights_and_agency.tau:l.2-3`
**Also appears in:** `constitution/tau_network.tau` (clause_004 l.31); `agents/seed/neemrad.tau` (clause_004 l.31); `constitution/map.md` (l.13, l.44); `LICENSE` (l.20); `CONTRIBUTING.md` (l.30); `README.md` (l.50); `docs/purpose_of_tau.md` (l.25); `testnet/README.md` (l.13); `testnet/tau_stream_index.json` (l.6))
**Depends on:** `genesis_stream`, `identity`, `self_amendment`

### consensus_logic
**Kind:** stream
**Class:** stream-id
**Defined in:** `constitution/consensus_logic.tau` (l.1-5)
**the author's definition:**
> # Title: Consensus Logic — Semantic Thresholds and Agreement Mechanisms
> # Stream: tau.constitution.consensus_logic — `constitution/consensus_logic.tau:l.2-3`
**Also appears in:** `agents/seed/neemrad.tau` (clause_004 l.31); `constitution/map.md` (l.13, l.45); `LICENSE` (l.22); `CONTRIBUTING.md` (l.14, l.31); `README.md` (l.51); `docs/purpose_of_tau.md` (l.25); `docs/theory_of_change.md` (l.36); `testnet/README.md` (l.14); `testnet/tau_stream_index.json` (l.8)
**Depends on:** `genesis_stream`, `identity`, `proposed_amendment`

### tau_network
**Kind:** stream
**Class:** stream-id
**Defined in:** `constitution/tau_network.tau` (l.1-5)
**the author's definition:**
> # Title: Tau Network — Binding Stream of Manifesto, Constitution, and Agent Cohesion
> # Stream: tau.constitution.tau_network — `constitution/tau_network.tau:l.2-3`
**Also appears in:** `constitution/tau_network.tau` (clause_007 l.46 "the tau_network registry"); `constitution/map.md` (l.19, l.46); `README.md` (l.52); `docs/purpose_of_tau.md` (l.26); `testnet/README.md` (l.15); `testnet/tau_stream_index.json` (l.7)
**Depends on:** `genesis_stream`, `identity`, `stream_version`

### agent_neemrad
**Kind:** agent
**Class:** map-node
**Defined in:** `constitution/map.md` (l.25, l.47)
**the author's definition:**
> - `agent_neemrad` → anchors authorship and genesis participation — `constitution/map.md:l.47`
**Also appears in:** `agents/seed/neemrad.tau` (the stream itself, id `tau.agents.seed.neemrad`)
**Depends on:** `neemrad`
**Notes:** INFERENCE — `agent_neemrad` is the map's node name for the stream `agents/seed/neemrad.tau`; no file uses the name `agent_neemrad` besides the map.

### testnet_bootstrap
**Kind:** stream
**Class:** map-node
**Defined in:** `constitution/map.md` (l.25, l.48)
**the author's definition:**
> - `testnet_bootstrap` → initiates TauNet under manifest + constitution — `constitution/map.md:l.48`
**Also appears in:** `testnet/tau_testnet_bootstrap.tau` (meta stream_name `tau_testnet_bootstrap`, l.45)
**Depends on:** `tau_testnet_bootstrap`

### amendments (map summary)
**Kind:** concept
**Class:** map-node
**Defined in:** `constitution/map.md` (l.49)
**the author's definition:**
> - `amendments` → extend rights, enforce coherence, and protect truth flow — `constitution/map.md:l.49`
**Also appears in:** `README.md` (l.14 "Ratified **Amendments** (001–003)", l.30 "amendments/ → All ratified declarations extending constitutional rights"); `CONTRIBUTING.md` (l.11-15); `testnet/README.md` (l.17-19); `docs/purpose_of_tau.md` (l.27-29)
**Depends on:** `proposed_amendment`, `amendment_rights`
**Notes:** FACT — the map, README, purpose doc, testnet README and stream index all name the amendments by their deleted `amendments/amendment_00N_*` paths; the living files are the three Family-B rewrites under `streams/amendments/`.

---

## 2. Manifesto — "Harmonic Emergence" (`manifesto/`, Family A with extra keywords)

### Harmonic Emergence
**Kind:** concept
**Class:** prose-term
**Defined in:** `README.md` (l.15); `agents/seed/neemrad.tau` (clause_003, l.26); `manifesto/epilogue.md` (l.11)
**the author's definition:**
> - ✅ The full **Harmonic Emergence** Manifesto (Chapters 1–9 + Epilogue) — `README.md:l.15`

>     chapter_01 through chapter_09 of the Harmonic Emergence stream set. — `agents/seed/neemrad.tau:l.26`

> Walk in harmonic emergence. — `manifesto/epilogue.md:l.11`
**Also appears in:** every `manifesto/chapter_*.tau` stream id prefix `harmonic-emergence.` (l.3/5); `docs/experiential_exercises.md` (l.1 "Experiential Exercises for Harmonic Emergence"); `README.md` (l.31)
**Depends on:** `chapter_01_great-dissonance`, `chapter_02_return-to-coherence`, `chapter_03_co-governance-by-syntax`, `chapter_04_from-nations-to-notions`, `chapter_05_emergence-of-being-in-action`, `chapter_06_temporal-coordination-law-of-octaves`, `chapter_07_multi-agent-protocol-of-trust`, `chapter_08_harmonic-agent-behavior`, `chapter_09_value-as-energy-in-relation`
**Notes:** INFERENCE — the manifesto is itself treated as a chain of streams (each chapter `requires` the previous chapter's headline concept); "the octave" in the epilogue (l.3) refers to this nine-step chain.

### chapter_01_great-dissonance
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (l.1-5)
**the author's definition:**
> # Title: The Great Dissonance
> # Stream: harmonic-emergence.chapter_01_great-dissonance — `manifesto/chapter_01_great-dissonance.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.3-5); `manifesto/manifesto.lock` (l.3-5); `docs/index.md` (l.17); `docs/experiential_exercises.md` (l.3-4); `manifesto/chapter_02_return-to-coherence.tau` (clause_004 l.28 "(from chapter_01)")
**Depends on:** `dissonance`, `great_dissonance`, `center_fragmentation`, `personal_dissonance`
**Conflict:** `manifesto/manifesto.lock:l.4` says `provides: [great_dissonance, personal_dissonance]`; the chapter (`l.69/73`) and `manifesto/interface_map.txt:l.4` say `provides: [dissonance, great_dissonance, center_fragmentation]`.

### dissonance
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (clause_001, l.12-17)
**the author's definition:**
> define "dissonance" as:
>     any disruption of coherence,
>     manifested at personal, systemic, or planetary scale.
>
>   superclass_of: [great_dissonance, personal_dissonance] — `manifesto/chapter_01_great-dissonance.tau:l.13-17`
**Also appears in:** `manifesto/chapter_01_great-dissonance.tau` (provides); `manifesto/chapter_02_return-to-coherence.tau` (provides l.53/57; clause_004 l.28 "dissonance has manifested (from chapter_01)"); `manifesto/interface_map.txt` (l.4, l.8); `manifesto/epilogue.md` (l.3)
**Depends on:** `coherence`, `great_dissonance`, `personal_dissonance`
**Conflict:** provided by both chapter_01 (which defines it) and chapter_02 (which does not define it but lists it in `provides`, l.53/57).

### great_dissonance
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (clause_002, l.19-22)
**the author's definition:**
> define "great_dissonance" as:
>     a systemic fragmentation of the triadic centers (thought, emotion, action)
>     expressed by disalignment across cycles of decision and execution. — `manifesto/chapter_01_great-dissonance.tau:l.20-22`
**Also appears in:** `manifesto/chapter_01_great-dissonance.tau` (clause_004 l.36 "great_dissonance manifests"; provides); `manifesto/chapter_02_return-to-coherence.tau` (requires l.54/58); `manifesto/manifesto.lock` (l.4, l.9); `manifesto/interface_map.txt` (l.4, l.9)
**Depends on:** `dissonance`, `triadic centers`

### center_fragmentation
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (clause_003, l.24-27)
**the author's definition:**
> define "center_fragmentation" as:
>     a condition in which the intellectual, emotional, and instinctual centers
>     operate in contradiction or without mutual awareness. — `manifesto/chapter_01_great-dissonance.tau:l.25-27`
**Also appears in:** `manifesto/chapter_01_great-dissonance.tau` (provides); `manifesto/interface_map.txt` (l.4)
**Depends on:** `triadic centers`

### personal_dissonance
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (declared l.10; defined as `"personal-dissonance"` in clause_006, l.47-56)
**the author's definition:**
> define "personal-dissonance" as:
>     the subjective experience of unobserved contradiction among one's centers.
>
>   if thought proceeds without feeling,
>      or if action overrides conscience:
>     the being fractures into auto-mechanical patterns.
>
>   note:
>     the macrocosmic dissonance reflects this in scale. — `manifesto/chapter_01_great-dissonance.tau:l.48-56`
**Also appears in:** `manifesto/chapter_01_great-dissonance.tau` (clause_001 `superclass_of` l.17); `manifesto/manifesto.lock` (l.4 provides `personal_dissonance`)
**Depends on:** `dissonance`, `triadic centers`, `auto-mechanical patterns`
**Conflict:** declared as `"personal_dissonance"` (l.10) but defined as `"personal-dissonance"` (l.48, hyphen). Provided by `manifesto.lock` but not by the chapter's own `provides` (l.69/73) nor by `interface_map.txt`. `docs/naming_conventions.md:l.5` forbids hyphens in concept names.

### speed_without_understanding
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (clause_005, l.42-45)
**the author's definition:**
> define "speed_without_understanding" as:
>     acceleration of technological or procedural systems
>     without corresponding evolution in comprehension or purpose. — `manifesto/chapter_01_great-dissonance.tau:l.43-45`
**Also appears in:** `manifesto/chapter_01_great-dissonance.tau` (clause_004 l.32)
**Depends on:** —
**Notes:** FACT — defined but never `declare concept`-ed and never in `provides`.

### wisdom_without_execution
**Kind:** concept
**Class:** prose-term
**Defined in:** — (used, never defined)
**the author's definition:**
> beings::planet_earth oscillate between:
>       speed_without_understanding and
>       wisdom_without_execution — `manifesto/chapter_01_great-dissonance.tau:l.31-33`
**Also appears in:** —
**Depends on:** —
**Notes:** paired with `speed_without_understanding`, which is defined; this one is not. In open-terms.

### beings::planet_earth
**Kind:** concept
**Class:** notation
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (clause_004, l.31)
**the author's definition:**
> beings::planet_earth oscillate between: — `manifesto/chapter_01_great-dissonance.tau:l.31`
**Also appears in:** —
**Depends on:** —
**Notes:** the only use of `name::name` as a subject term. The same `::` separator appears as `validation_warning::"…"` (`tools/validate_tau.tau:l.15`) and `tml_rule::"…"` (`transcompiler/sample_conversions.tau:l.13`). What `::` means is not stated; in open-terms.

### triadic centers
**Kind:** concept
**Class:** prose-term
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (clause_002 l.21, clause_003 l.26); `manifesto/chapter_02_return-to-coherence.tau` (clause_001 l.14)
**the author's definition:**
> the triadic centers (thought, emotion, action) — `manifesto/chapter_01_great-dissonance.tau:l.21`

> the intellectual, emotional, and instinctual centers — `manifesto/chapter_01_great-dissonance.tau:l.26`

> the three primary centers of a being — `manifesto/chapter_02_return-to-coherence.tau:l.14`
**Also appears in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_002 l.19 "intellect, emotion, and action"; clause_003 l.23 "all centers"); `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_002 l.20 "thought, emotion, and movement"; clause_005 l.37 "across centers"); `tower_of_babel/nimrod_and_babel.md` (l.3 "the intellect, emotion, and instinct within a person")
**Depends on:** —
**Notes:** FACT — the third center is named "action" (ch01 l.21, ch02 l.19), "instinctual" (ch01 l.26), "movement" (ch02 l.15, ch05 l.20), and "instinct" (nimrod l.3). Recorded as one construct with variable naming; no reconciliation attempted.

### auto-mechanical patterns
**Kind:** concept
**Class:** prose-term
**Defined in:** — (used only)
**the author's definition:**
> the being fractures into auto-mechanical patterns. — `manifesto/chapter_01_great-dissonance.tau:l.53`
**Also appears in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_007 l.49 "Was it meaningful, or mechanical?")
**Depends on:** —
**Notes:** in open-terms.

### chapter_02_return-to-coherence
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_02_return-to-coherence.tau` (l.1-5)
**the author's definition:**
> # Title: Return to Coherence
> # Stream: harmonic-emergence.chapter_02_return-to-coherence — `manifesto/chapter_02_return-to-coherence.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.7-9); `manifesto/manifesto.lock` (l.7-9); `docs/index.md` (l.18); `docs/experiential_exercises.md` (l.6-7)
**Depends on:** `great_dissonance`, `coherence`, `triadic_unity`, `conscious_alignment`, `self_recollection`

### coherence
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_001, l.12-15)
**the author's definition:**
> define "coherence" as:
>     the harmonic relation among the three primary centers of a being
>     resulting in synchronized awareness, intention, and movement. — `manifesto/chapter_02_return-to-coherence.tau:l.13-15`
**Also appears in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_004 l.31; provides); `manifesto/chapter_03_co-governance-by-syntax.tau` (requires l.59/63); `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_006 l.49); `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_006 l.50 "emergent value = coherence sustained across relationships."); `constitution/identity_core.tau` (clause_006 l.45 "their identity attains coherence"); `streams/core/valid_thought.tau` (clause_001 l.3); `manifesto/manifesto.lock` (l.8, l.13); `manifesto/interface_map.txt` (l.8, l.13); many prose files as lower-case "coherence"
**Depends on:** `triadic centers`
**Notes:** INFERENCE — "coherence" is used in two registers: the manifesto's (a being's centers in harmonic relation) and the logic register (`thought_coherence`, `trustless_coherence`, `semantic coherence`, `behavioral_coherence`). The chapter definition is the only `define … as:` for the bare word.

### triadic_unity
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_002, l.17-19)
**the author's definition:**
> define "triadic_unity" as:
>     the alignment of intellect, emotion, and action around a unified aim. — `manifesto/chapter_02_return-to-coherence.tau:l.18-19`
**Also appears in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_004 `where:` l.34; provides); `manifesto/manifesto.lock` (l.8); `manifesto/interface_map.txt` (l.8)
**Depends on:** `triadic centers`, `conscious_alignment`

### conscious_alignment
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_003, l.21-24)
**the author's definition:**
> define "conscious_alignment" as:
>     the act of remembering one's aim and bringing all centers into agreement
>     across moments of transition, stress, or drift. — `manifesto/chapter_02_return-to-coherence.tau:l.22-24`
**Also appears in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_004 l.34; provides); `manifesto/interface_map.txt` (l.8)
**Depends on:** `triadic centers`

### self_recollection
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_02_return-to-coherence.tau` (clause_005, l.36-41)
**the author's definition:**
> define "self_recollection" as:
>     the moment of remembering one’s wholeness in the midst of fragmentation.
>
>   note:
>     without self_recollection, unity remains theoretical. — `manifesto/chapter_02_return-to-coherence.tau:l.37-41`
**Also appears in:** —
**Depends on:** `coherence`
**Notes:** FACT — declared (l.10) and defined, not in `provides` (l.53/57). INFERENCE — the closest repo construct to the room template's *self-remembering* (§12); the repo does not connect them.

### chapter_03_co-governance-by-syntax
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (l.1-5)
**the author's definition:**
> # Title: Co-Governance by Syntax
> # Stream: harmonic-emergence.chapter_03_co-governance-by-syntax — `manifesto/chapter_03_co-governance-by-syntax.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.11-13); `manifesto/manifesto.lock` (l.11-13); `docs/index.md` (l.19); `docs/experiential_exercises.md` (l.9-10); `docs/naming_conventions.md` (l.9 example `semantic_consent`)
**Depends on:** `coherence`, `governance`, `logic_stream`, `semantic_consent`, `syntax_evolution`, `authority_as_clarity`

### governance
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_001, l.13-16)
**the author's definition:**
> define "governance" as:
>     the ongoing process by which multiple agents coordinate shared reality
>     using declarations, protocols, and feedback to align behavior. — `manifesto/chapter_03_co-governance-by-syntax.tau:l.14-16`
**Also appears in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_006 l.44; provides); `manifesto/chapter_04_from-nations-to-notions.tau` (requires l.52/56; clause_005 l.36); `manifesto/manifesto.lock` (l.12, l.17); `manifesto/interface_map.txt` (l.12, l.17)
**Depends on:** —

### logic_stream
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_002, l.18-21)
**the author's definition:**
> define "logic_stream" as:
>     a semantically structured, versionable stream of clauses
>     capable of expressing reasoned declarations, causal links, and revisions. — `manifesto/chapter_03_co-governance-by-syntax.tau:l.19-21`
**Depends on:** `clause`
**Notes:** INFERENCE — this is the manifesto's name for what every `.tau` file is ("stream"); the constitution never defines "stream" itself. See open-terms (`stream`).

### semantic_consent
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_003, l.23-26)
**the author's definition:**
> define "semantic_consent" as:
>     agreement reached not through coercion or vote,
>     but through mutual comprehension and alignment of meaning. — `manifesto/chapter_03_co-governance-by-syntax.tau:l.24-26`
**Also appears in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_006 l.41; provides); `constitution/rights_and_agency.tau` (clause_004 l.34 "voluntary semantic consent"); `LICENSE` (l.13 "their semantic consent"); `docs/naming_conventions.md` (l.9); `CHANGELOG.md` (l.85 "TauNet now compiles with consent."); `manifesto/interface_map.txt` (l.12)
**Depends on:** —
**Notes:** FACT — "not through coercion or vote" is the repo's own statement on voting; the room template's *weight* entry (§12, "Not one seed, one vote") is consistent with it in wording. Recorded; not reconciled.

### syntax_evolution
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_004, l.28-31)
**the author's definition:**
> define "syntax_evolution" as:
>     the ability for governance protocols to refine themselves
>     in response to contradiction, feedback, or contextual change. — `manifesto/chapter_03_co-governance-by-syntax.tau:l.29-31`
**Also appears in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_006 l.45; provides); `manifesto/interface_map.txt` (l.12)
**Depends on:** `governance`

### authority_as_clarity
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (clause_005, l.33-36)
**the author's definition:**
> define "authority_as_clarity" as:
>     a model where the most precise, transparent contributor
>     holds temporary influence — not by position, but coherence of expression. — `manifesto/chapter_03_co-governance-by-syntax.tau:l.34-36`
**Also appears in:** `manifesto/chapter_03_co-governance-by-syntax.tau` (provides); `manifesto/interface_map.txt` (l.12)
**Depends on:** —
**Notes:** INFERENCE — the repo's nearest statement to the room template's *weight* ("holds temporary influence — not by position, but coherence of expression"). Link is mine, not the text's.

### chapter_04_from-nations-to-notions
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_04_from-nations-to-notions.tau` (l.1-5)
**the author's definition:**
> # Title: From Nations to Notions
> # Stream: harmonic-emergence.chapter_04_from-nations-to-notions — `manifesto/chapter_04_from-nations-to-notions.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.15-17); `manifesto/manifesto.lock` (l.15-17); `docs/index.md` (l.20); `docs/experiential_exercises.md` (l.12-13)
**Depends on:** `governance`, `semantic_governance`, `identity_trace`, `consensual_computation`, `earned_being`, `co_evolution`

### semantic_governance
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_04_from-nations-to-notions.tau` (clause_001, l.13-16)
**the author's definition:**
> define "semantic_governance" as:
>     coordination guided by meaning, logic, and shared intentionality,
>     rather than by geography or fixed institutional power. — `manifesto/chapter_04_from-nations-to-notions.tau:l.14-16`
**Also appears in:** `manifesto/chapter_04_from-nations-to-notions.tau` (provides); `manifesto/manifesto.lock` (l.16); `manifesto/interface_map.txt` (l.16)
**Depends on:** `governance`

### consensual_computation
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_04_from-nations-to-notions.tau` (clause_003, l.22-25)
**the author's definition:**
> define "consensual_computation" as:
>     allocation of shared resources through verified agreements and transparent, logic-based processes,
>     optimizing for ecological balance and conscious agency. — `manifesto/chapter_04_from-nations-to-notions.tau:l.23-25`
**Also appears in:** `manifesto/chapter_04_from-nations-to-notions.tau` (provides); `manifesto/interface_map.txt` (l.16)
**Depends on:** `semantic_consent`

### earned_being
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_04_from-nations-to-notions.tau` (clause_004, l.27-29)
**the author's definition:**
> define "earned_being" as:
>     the result of one’s conscious participation in evolving knowledge, verified presence, and inner refinement. — `manifesto/chapter_04_from-nations-to-notions.tau:l.28-29`
**Also appears in:** `manifesto/chapter_04_from-nations-to-notions.tau` (clause_005 l.37; provides); `manifesto/interface_map.txt` (l.16)
**Depends on:** —
**Notes:** FACT — "verified presence" is the only occurrence of "presence" as a property of a being in the `.tau` files (besides `agent_identity` "a semantic presence declared by neemrad", `agents/seed/neemrad.tau:l.15`). The brief's *presence* (§12) is the author's 2026 term.

### co_evolution
**Kind:** concept
**Class:** declared
**Defined in:** — (declared l.11, used in clause_005 l.38, never `define`d)
**the author's definition:**
> and from control to co_evolution. — `manifesto/chapter_04_from-nations-to-notions.tau:l.38`
**Also appears in:** `manifesto/chapter_04_from-nations-to-notions.tau` (provides l.51/55); `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_005 l.38 "co-evolutionary need"); `manifesto/interface_map.txt` (l.16)
**Depends on:** —
**Notes:** declared and provided but never defined. In open-terms.

### chapter_05_emergence-of-being-in-action
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (l.1-5)
**the author's definition:**
> # Title: Emergence of Being in Action
> # Stream: harmonic-emergence.chapter_05_emergence-of-being-in-action — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.19-21); `manifesto/manifesto.lock` (l.19-21); `docs/index.md` (l.21); `docs/experiential_exercises.md` (l.15-16)
**Depends on:** `identity_trace`, `being_in_action`, `convergent_triad`, `feedback_aware_identity`, `iterative_enactment`, `harmonic_agency`

### being_in_action
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_001, l.13-16)
**the author's definition:**
> define "being_in_action" as:
>     the coherent emergence of identity through unified awareness, intention, and movement
>     enacted across time with contextual relevance. — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.14-16`
**Also appears in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_006 l.46; provides); `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (requires l.55/59); `manifesto/manifesto.lock` (l.20, l.25); `manifesto/interface_map.txt` (l.20, l.25)
**Depends on:** `identity`, `coherence`

### convergent_triad
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_002, l.18-21)
**the author's definition:**
> define "convergent_triad" as:
>     the lawful coordination of thought, emotion, and movement
>     forming a stable pattern of action without internal contradiction. — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.19-21`
**Also appears in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_006 l.42; provides); `manifesto/interface_map.txt` (l.20)
**Depends on:** `triadic centers`, `lawfulness`

### iterative_enactment
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_003, l.23-29)
**the author's definition:**
> define "iterative_enactment" as:
>     the cycle of:
>       (1) declaration,
>       (2) action,
>       (3) feedback,
>       (4) adjustment. — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.24-29`
**Also appears in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_006 l.43)
**Depends on:** —
**Notes:** FACT — declared (l.10) and defined but absent from `provides` (l.61/65) and from `interface_map.txt`.

### feedback_aware_identity
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_004, l.31-33)
**the author's definition:**
> define "feedback_aware_identity" as:
>     a being who evolves by integrating the consequences of their behavior into future action. — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.32-33`
**Also appears in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_006 `where:` l.49; provides); `manifesto/interface_map.txt` (l.20)
**Depends on:** `identity`

### harmonic_agency
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (clause_005, l.35-38)
**the author's definition:**
> define "harmonic_agency" as:
>     the capacity to act coherently across centers, to refrain when misaligned,
>     and to revise without self-deception. — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.36-38`
**Also appears in:** `manifesto/chapter_05_emergence-of-being-in-action.tau` (provides); `manifesto/interface_map.txt` (l.20)
**Depends on:** `agency`, `triadic centers`

### chapter_06_temporal-coordination-law-of-octaves
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (l.1-5)
**the author's definition:**
> # Title: Temporal Coordination and the Law of Octaves
> # Stream: harmonic-emergence.chapter_06_temporal-coordination-law-of-octaves — `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.23-25); `manifesto/manifesto.lock` (l.23-25); `docs/index.md` (l.22); `docs/experiential_exercises.md` (l.18-19)
**Depends on:** `being_in_action`, `octave_development`, `interval_shock`, `temporal_coordination`, `rhythmic_emergence`, `alignment_in_time`
**Conflict:** `manifesto/manifesto.lock:l.24` provides `[temporal_coordination, interval_shock]`; chapter (l.54/58) and `interface_map.txt:l.24` provide `[octave_development, interval_shock, temporal_coordination, rhythmic_emergence]`.
**Notes:** "Law of Octaves" appears only in the title; never defined. In open-terms.

### octave_development
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (clause_001, l.13-16)
**the author's definition:**
> define "octave_development" as:
>     a non-linear progression of process or intention,
>     characterized by intervals that require conscious input to avoid deviation. — `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.14-16`
**Also appears in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (provides); `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (requires l.60/64); `manifesto/interface_map.txt` (l.24, l.29); `manifesto/epilogue.md` (l.3 "the octave")
**Depends on:** `interval_shock`
**Conflict:** chapter_07 requires `octave_development` (l.60/64, and `interface_map.txt:l.29`); `manifesto/manifesto.lock:l.29` says chapter_07 requires `temporal_coordination` instead.

### interval_shock
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (clause_002, l.18-21)
**the author's definition:**
> define "interval_shock" as:
>     a necessary injection of attention, energy, or effort at key points
>     in order to maintain developmental direction. — `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.19-21`
**Also appears in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (clause_005 l.38; provides); `manifesto/manifesto.lock` (l.24); `manifesto/interface_map.txt` (l.24); `docs/experiential_exercises.md` (l.19 'What "shock" was missed?'); every chapter's `insert_shock:` keyword
**Depends on:** `octave_development`
**Notes:** INFERENCE — `insert_shock:` (the notation keyword in every chapter) is the manifesto applying `interval_shock` to its reader; the text does not say so explicitly.

### temporal_coordination
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (clause_003, l.23-26)
**the author's definition:**
> define "temporal_coordination" as:
>     the synchronization of actions, perceptions, and intentions
>     with rhythmically aligned internal and external processes. — `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.24-26`
**Also appears in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (provides); `manifesto/manifesto.lock` (l.24, l.29); `manifesto/interface_map.txt` (l.24); `docs/index.md` (l.22)
**Depends on:** —

### rhythmic_emergence
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (clause_004, l.28-31)
**the author's definition:**
> define "rhythmic_emergence" as:
>     the lawful appearance of coherence over time,
>     occurring when inner and outer rhythms align without contradiction. — `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.29-31`
**Also appears in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (provides); `manifesto/interface_map.txt` (l.24); `testnet/README.md` (l.57 "a rhythm of lawful emergence")
**Depends on:** `coherence`, `lawfulness`

### alignment_in_time
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.11`, never defined or provided)
**the author's definition:**
> declare concept "alignment_in_time". — `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau:l.11`
**Also appears in:** —
**Depends on:** —
**Notes:** in open-terms (seeded from INVENTORY §6).

### chapter_07_multi-agent-protocol-of-trust
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (l.1-5)
**the author's definition:**
> # Title: Multi-Agent Protocol of Trust
> # Stream: harmonic-emergence.chapter_07_multi-agent-protocol-of-trust — `manifesto/chapter_07_multi-agent-protocol-of-trust.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.27-29); `manifesto/manifesto.lock` (l.27-29); `docs/index.md` (l.23); `docs/experiential_exercises.md` (l.21-22)
**Depends on:** `octave_development`, `trust`, `semantic_traceability`, `autonomy_in_alignment`, `reflexive_verification`, `protocol_commons`

### trust
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_001, l.13-16)
**the author's definition:**
> define "trust" as:
>     multi-temporal coherence between declarations and actions,
>     verified through transparent feedback and behavioral integrity. — `manifesto/chapter_07_multi-agent-protocol-of-trust.tau:l.14-16`
**Depends on:** `coherence`, `semantic_consistency`
**Notes:** "trust-score" (`budget_allocation.tau:l.36`) is not defined; in open-terms.

### semantic_traceability
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_002, l.18-21)
**the author's definition:**
> define "semantic_traceability" as:
>     the ability to observe and reconstruct an agent’s logic path
>     through explicit, versioned semantic streams. — `manifesto/chapter_07_multi-agent-protocol-of-trust.tau:l.19-21`
**Also appears in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_006 l.40; provides); `manifesto/manifesto.lock` (l.28); `manifesto/interface_map.txt` (l.28)
**Depends on:** `logic_stream`, `stream_version`

### autonomy_in_alignment
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_003, l.23-26)
**the author's definition:**
> define "autonomy_in_alignment" as:
>     the capacity to act independently while remaining attuned
>     to shared logic and evolving context. — `manifesto/chapter_07_multi-agent-protocol-of-trust.tau:l.24-26`
**Also appears in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (provides); `manifesto/interface_map.txt` (l.28)
**Depends on:** —

### reflexive_verification
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_004, l.28-31)
**the author's definition:**
> define "reflexive_verification" as:
>     the self-observing process by which an agent
>     adjusts its own behavior based on declared intent and received feedback. — `manifesto/chapter_07_multi-agent-protocol-of-trust.tau:l.29-31`
**Also appears in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_006 l.43; provides); `manifesto/interface_map.txt` (l.28)
**Depends on:** —

### protocol_commons
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (clause_005, l.33-36)
**the author's definition:**
> define "protocol_commons" as:
>     a shared, evolving framework for multi-agent agreement,
>     ensuring open audit, adaptive revision, and mutual legibility. — `manifesto/chapter_07_multi-agent-protocol-of-trust.tau:l.34-36`
**Also appears in:** `manifesto/chapter_07_multi-agent-protocol-of-trust.tau` (provides); `manifesto/interface_map.txt` (l.28)
**Depends on:** —

### chapter_08_harmonic-agent-behavior
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (l.1-5)
**the author's definition:**
> # Title: Harmonic Agent Behavior
> # Stream: harmonic-emergence.chapter_08_harmonic-agent-behavior — `manifesto/chapter_08_harmonic-agent-behavior.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.31-33); `manifesto/manifesto.lock` (l.31-33); `docs/index.md` (l.24); `docs/experiential_exercises.md` (l.24-25)
**Depends on:** `trust`, `harmonic_behavior`, `semantic_reflex`, `context_attunement`, `behavioral_coherence`, `resonant_adjustment`

### harmonic_behavior
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_001, l.13-16)
**the author's definition:**
> define "harmonic_behavior" as:
>     behavior that arises from aligned intention, perception, and context,
>     producing outcomes in rhythm with internal state and external signals. — `manifesto/chapter_08_harmonic-agent-behavior.tau:l.14-16`
**Also appears in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_006 l.45; provides); `manifesto/chapter_09_value-as-energy-in-relation.tau` (requires l.64/68); `manifesto/manifesto.lock` (l.32, l.37); `manifesto/interface_map.txt` (l.32, l.37)
**Depends on:** `behavioral_coherence`, `semantic_reflex`

### semantic_reflex
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_002, l.18-21)
**the author's definition:**
> define "semantic_reflex" as:
>     an automated behavioral pattern triggered not by raw stimulus,
>     but by recognized meaning and logical memory. — `manifesto/chapter_08_harmonic-agent-behavior.tau:l.19-21`
**Also appears in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_006 l.42 "its reflexes are semantically derived"; clause_007 l.52; provides); `manifesto/interface_map.txt` (l.32)
**Depends on:** `reflexive_memory`

### context_attunement
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_003, l.23-25)
**the author's definition:**
> define "context_attunement" as:
>     the capacity to perceive and respond in phase with environmental, social, and semantic shifts. — `manifesto/chapter_08_harmonic-agent-behavior.tau:l.24-25`
**Also appears in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (provides); `manifesto/interface_map.txt` (l.32)
**Depends on:** —

### behavioral_coherence
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_004, l.27-30)
**the author's definition:**
> define "behavioral_coherence" as:
>     the state in which declared logic, internal motive, and visible action
>     form a consistent stream over time. — `manifesto/chapter_08_harmonic-agent-behavior.tau:l.28-30`
**Also appears in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_006 l.39; provides); `manifesto/interface_map.txt` (l.32)
**Depends on:** `semantic_consistency`

### resonant_adjustment
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (clause_005, l.32-35)
**the author's definition:**
> define "resonant_adjustment" as:
>     the act of modifying behavior
>     not reactively, but through feedback-aware phase correction. — `manifesto/chapter_08_harmonic-agent-behavior.tau:l.33-35`
**Also appears in:** `manifesto/chapter_08_harmonic-agent-behavior.tau` (provides); `manifesto/interface_map.txt` (l.32)
**Depends on:** `feedback_aware_identity`

### chapter_09_value-as-energy-in-relation
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (l.1-5)
**the author's definition:**
> # Title: Value as Energy-in-Relation
> # Stream: harmonic-emergence.chapter_09_value-as-energy-in-relation — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.2-3`
**Also appears in:** `manifesto/interface_map.txt` (l.35-37); `manifesto/manifesto.lock` (l.35-37); `docs/index.md` (l.25); `docs/experiential_exercises.md` (l.27-28)
**Depends on:** `harmonic_behavior`, `relational_value`, `energy_of_contribution`, `post_monetary_flow`, `reciprocal_distribution`, `semantic_economy`

### relational_value
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_001, l.13-17)
**the author's definition:**
> define "relational_value" as:
>     value arising between agents,
>     shaped by contribution, resonance, and context,
>     not by scarcity or possession. — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.14-17`
**Also appears in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (provides); `manifesto/interface_map.txt` (l.36)
**Depends on:** —

### energy_of_contribution
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_002, l.19-22)
**the author's definition:**
> define "energy_of_contribution" as:
>     the non-coerced effort, presence, or care
>     offered into a system without guarantee of return. — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.20-22`
**Also appears in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_006 l.42 "agents contribute energy into shared purpose"; provides); `manifesto/interface_map.txt` (l.36)
**Depends on:** `non_coercion`

### post_monetary_flow
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_003, l.24-27)
**the author's definition:**
> define "post_monetary_flow" as:
>     the dynamic allocation of resources
>     guided by verified impact, trust, and relational integrity. — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.25-27`
**Also appears in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_006 l.48; provides); `manifesto/manifesto.lock` (l.36); `manifesto/interface_map.txt` (l.36)
**Depends on:** `trust`, `reciprocal_distribution`, `semantic_economy`

### reciprocal_distribution
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_004, l.29-33)
**the author's definition:**
> define "reciprocal_distribution" as:
>     a pattern in which surplus is circulated
>     toward coherence amplifiers and care nodes,
>     rather than hoarded or extracted. — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.30-33`
**Also appears in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_006 l.45; provides); `manifesto/interface_map.txt` (l.36)
**Depends on:** `coherence amplifiers`, `care nodes`

### coherence amplifiers
**Kind:** concept
**Class:** prose-term
**Defined in:** — (used only)
**the author's definition:**
> toward coherence amplifiers and care nodes, — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.32`
**Also appears in:** —
**Depends on:** —
**Notes:** in open-terms.

### care nodes
**Kind:** concept
**Class:** prose-term
**Defined in:** — (used only)
**the author's definition:**
> toward coherence amplifiers and care nodes, — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.32`
**Also appears in:** —
**Depends on:** —
**Notes:** in open-terms.

### semantic_economy
**Kind:** concept
**Class:** declared
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_005, l.35-38)
**the author's definition:**
> define "semantic_economy" as:
>     an ecosystem where value flows in accordance
>     with meaning, resonance, and co-evolutionary need. — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.36-38`
**Also appears in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_006 l.48; provides); `manifesto/interface_map.txt` (l.36)
**Depends on:** `co_evolution`

### emergent value
**Kind:** concept
**Class:** prose-term
**Defined in:** `manifesto/chapter_09_value-as-energy-in-relation.tau` (clause_006, l.50)
**the author's definition:**
>     emergent value = coherence sustained across relationships. — `manifesto/chapter_09_value-as-energy-in-relation.tau:l.50`
**Also appears in:** —
**Depends on:** `coherence`
**Notes:** the only `=` pseudo-equation in the manifesto, placed inside a `then (…)` block. Whether `=` is definition, assignment, or identity is not stated; in open-terms (`=`).

### epilogue (Epilogue — Is Harmony Emerging?)
**Kind:** stream
**Class:** chapter
**Defined in:** `manifesto/epilogue.md` (l.1-11)
**the author's definition:**
> # Epilogue — Is Harmony Emerging?
>
> You’ve streamed the octave from dissonance to contribution.
>
> Pause now.
>
> Ask: What part of this system lives in you already?
> What part resists?
>
> You are no longer an observer. You are a vector in this field.
> Walk in harmonic emergence. — `manifesto/epilogue.md:l.1-11`
**Also appears in:** `manifesto/interface_map.txt` (l.39-41, as a stream with provides/requires); `docs/index.md` (l.26); `testnet/tau_stream_index.json` (l.18); `README.md` (l.15, l.31)
**Depends on:** `recursion_point`, `full_manifesto_experience`, `the octave`, `vector in this field`, `Harmonic Emergence`
**Notes:** FACT — the only prose file that `interface_map.txt` treats as a stream (provides/requires); `manifesto.lock` omits it.

### recursion_point
**Kind:** concept
**Class:** declared
**Defined in:** — (`manifesto/interface_map.txt:l.40`, provides only)
**the author's definition:**
> epilogue.md
>   provides: [recursion_point]
>   requires: [full_manifesto_experience] — `manifesto/interface_map.txt:l.39-41`
**Also appears in:** —
**Depends on:** `full_manifesto_experience`, `recursion`
**Notes:** never defined; in open-terms. INFERENCE — the epilogue's "You are a vector in this field" (`manifesto/epilogue.md:l.10`) is the text the interface map is summarizing.

### full_manifesto_experience
**Kind:** concept
**Class:** declared
**Defined in:** — (`manifesto/interface_map.txt:l.41`, requires only)
**the author's definition:**
>   requires: [full_manifesto_experience] — `manifesto/interface_map.txt:l.41`
**Also appears in:** —
**Depends on:** `Harmonic Emergence`
**Notes:** requires-with-no-provider (INVENTORY §4); in open-terms.

### the octave
**Kind:** concept
**Class:** prose-term
**Defined in:** `manifesto/epilogue.md` (l.3)
**the author's definition:**
> You’ve streamed the octave from dissonance to contribution. — `manifesto/epilogue.md:l.3`
**Also appears in:** `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (title l.2 "Law of Octaves"; clause_006 l.48 "developmental octaves")
**Depends on:** `octave_development`, `Harmonic Emergence`

### vector in this field
**Kind:** concept
**Class:** prose-term
**Defined in:** `manifesto/epilogue.md` (l.10)
**the author's definition:**
> You are no longer an observer. You are a vector in this field. — `manifesto/epilogue.md:l.10`
**Also appears in:** —
**Depends on:** —
**Notes:** in open-terms ("field").

### shock
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/experiential_exercises.md` (l.19)
**the author's definition:**
> Find where you drifted from a goal. What "shock" was missed? — `docs/experiential_exercises.md:l.19`
**Also appears in:** every `insert_shock:` clause (ch01 l.59, ch02 l.44, ch03 l.49, ch04 l.42, ch05 l.52, ch06 l.45, ch07 l.50, ch08 l.49, ch09 l.54); `manifesto/chapter_06_temporal-coordination-law-of-octaves.tau` (l.38 "conscious interval_shock", l.48 "shock points")
**Depends on:** `interval_shock`

---

## 3. Agents (`agents/seed/*.tau`, Family A)

### neemrad
**Kind:** agent
**Class:** agent
**Defined in:** `agents/seed/neemrad.tau` (l.1-5); `tree_of_life/golden_glossary.md` (l.8)
**the author's definition:**
> # Title: Identity Trace of Neemrad — Genesis Agent of the Tau Testnet
> # Stream: tau.agents.seed.neemrad — `agents/seed/neemrad.tau:l.2-3`

> (Notably, an example agent identity `neemrad.tau` in the system nods to this symbolic role.) — `tree_of_life/golden_glossary.md:l.8`
**Also appears in:** `constitution/map.md` (l.25 `agent_neemrad`, l.47); `README.md` (l.33 "Identity traces (e.g. neemrad.tau)"); `docs/purpose_of_tau.md` (l.31); `CHANGELOG.md` (l.173)
**Depends on:** `agent_identity`, `authorship_claim`, `manifesto_commitment`, `constitutional_alignment`, `stream_origin_trace`, `genesis_stream`, `identity_trace`
**Notes:** FACT — the glossary links the name to Nimrod ("nods to this symbolic role", `tree_of_life/golden_glossary.md:l.8`); the agent file itself makes no such link.

### agent_identity
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/neemrad.tau` (clause_001, l.13-16)
**the author's definition:**
> define "agent_identity" as:
>     a semantic presence declared by neemrad
>     anchored in clause authorship, stream alignment, and traceable contribution. — `agents/seed/neemrad.tau:l.14-16`
**Also appears in:** `agents/seed/neemrad.tau` (provides l.42/46)
**Depends on:** `identity`, `identity_trace`
**Notes:** FACT — "a semantic presence" is the repo's one use of "presence" for an agent's standing; compare the room template's *presence*.

### authorship_claim
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/neemrad.tau` (clause_002, l.18-21)
**the author's definition:**
> define "authorship_claim" as:
>     a verifiable declaration that neemrad authored or co-authored
>     the foundational manifesto and constitutional streams of the Tau Testnet. — `agents/seed/neemrad.tau:l.19-21`
**Also appears in:** `agents/seed/neemrad.tau` (provides); `README.md` (l.122 "Authorship"); `CONTRIBUTING.md` (l.25 "Any authored clauses or contributions")
**Depends on:** `Harmonic Emergence`, `identity_trace`

### manifesto_commitment
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/neemrad.tau` (clause_003, l.23-26)
**the author's definition:**
> define "manifesto_commitment" as:
>     an enduring alignment with the principles encoded in
>     chapter_01 through chapter_09 of the Harmonic Emergence stream set. — `agents/seed/neemrad.tau:l.24-26`
**Also appears in:** `agents/seed/neemrad.tau` (provides)
**Depends on:** `Harmonic Emergence`

### constitutional_alignment
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/neemrad.tau` (clause_004, l.28-31)
**the author's definition:**
> define "constitutional_alignment" as:
>     the explicit support and propagation of
>     autopoietic_logos, rights_and_agency, and consensus_logic. — `agents/seed/neemrad.tau:l.29-31`
**Also appears in:** `agents/seed/neemrad.tau` (provides); `README.md` (l.123 "Alignment"); `CONTRIBUTING.md` (l.24 "Your alignment with `autopoietic_logos`")
**Depends on:** `autopoietic_logos`, `rights_and_agency`, `consensus_logic`

### stream_origin_trace
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/neemrad.tau` (clause_005, l.33-36)
**the author's definition:**
> define "stream_origin_trace" as:
>     the linkage of neemrad to genesis_stream,
>     verified through stream authorship, amendment proposal, and bootstrap initiation. — `agents/seed/neemrad.tau:l.34-36`
**Also appears in:** `agents/seed/neemrad.tau` (provides); `README.md` (l.124 "Trace")
**Depends on:** `genesis_stream`, `identity_trace`

### civil_engineer
**Kind:** agent
**Class:** agent
**Defined in:** `agents/seed/civil_engineer.tau` (l.1-5)
**the author's definition:**
> # Title: Civil Engineer - Technical Validator
> # Stream: agents.seed.civil_engineer — `agents/seed/civil_engineer.tau:l.2-3`

> - `civil_engineer.tau`: Technical verifier of feasibility and cost — `streams/civic/README.md:l.32`

> Infrastructure professional validating cost and feasibility — `README.md:l.132`
**Depends on:** `identity`, `technical_validation`, `stream_endorsement`, `genesis_stream`

### technical_validation
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/civil_engineer.tau` (clause_002, l.15-18)
**the author's definition:**
> define "technical_validation" as:
>     the clause-level endorsement of real_world_estimate accuracy,
>     confirmed through professional judgment and local site review. — `agents/seed/civil_engineer.tau:l.16-18`
**Also appears in:** `agents/seed/civil_engineer.tau` (provides l.29); `README.md` (l.84 "Technical validation of proposal’s real-world estimate and feasibility")
**Depends on:** `real_world_estimate`, `stream_endorsement`

### local_resident
**Kind:** agent
**Class:** agent
**Defined in:** `agents/seed/local_resident.tau` (l.1-5)
**the author's definition:**
> # Title: Local Resident of the example town
> # Stream: agents.seed.local_resident — `agents/seed/local_resident.tau:l.2-3`

> - `local_resident.tau`: Community signal for support and feedback — `streams/civic/README.md:l.33`

> Community member supporting proposals and issuing civic feedback — `README.md:l.135`
**Depends on:** `identity`, `stream_endorsement`, `civic_feedback`, `genesis_stream`

### civic_feedback
**Kind:** concept
**Class:** declared
**Defined in:** `agents/seed/local_resident.tau` (clause_003, l.21-24)
**the author's definition:**
> define "civic_feedback" as:
>     any proposed modification, comment, or contradiction
>     offered in good faith toward public semantic clarity. — `agents/seed/local_resident.tau:l.22-24`
**Also appears in:** `agents/seed/local_resident.tau` (provides l.30); `README.md` (l.135)
**Depends on:** —

---

## 4. Core and meta streams (`streams/core/`, `streams/meta/`)

### valid_thought
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/core/valid_thought.tau` (clause_001, l.1-8; Family B); `git:1d70d83:streams/core/valid_thought.tau` (clause_001, l.13-17; Family A); `streams/core/valid_thought.tml` (l.1-5)
**the author's definition:**
> clause_001 v0.1.0:
>   stream_name: valid_thought
>   description: A thought is valid if it preserves coherence, origin, and amendment lineage.
>   phrase_predicates:
>     - "a statement" : statement
>     - "defined concepts" : defined_concepts
>     - "preserves origin trace" : preserves_origin_trace
>     - "does not contradict prior reasoning unless explicitly amended" : does_not_contradict_prior_reasoning — `streams/core/valid_thought.tau:l.1-8`

> define "valid_thought" as:
>     a statement or clause whose semantic structure
>     aligns with defined concepts, preserves origin trace,
>     and does not contradict prior reasoning unless explicitly amended. — `git:1d70d83:streams/core/valid_thought.tau:l.14-17`

> valid_thought(X) :-
>   statement(X),
>   defined_concepts(X),
>   preserves_origin_trace(X),
>   does_not_contradict_prior_reasoning(X). — `streams/core/valid_thought.tml:l.1-5`
**Also appears in:** `streams/core/valid_thought.tau` (meta stream_name and provides, l.39-40); `streams/meta/ethics.tau` (requires l.44/48); `streams/meta/memory.tau` (requires l.43/47); `streams/glossary/core_phrases.tau` (clause_100 l.11-12 phrase "valid thought"); `streams/README.md` (l.26, l.51); `streams/core/README.md` (l.14 "what makes a thought semantically admissible"); `transcompiler/index/stream_index.json`
**Depends on:** `statement`, `defined_concepts`, `preserves_origin_trace`, `does_not_contradict_prior_reasoning`, `identity_trace`, `concept_definition`
**Conflict:** Family-A version (deleted) defines a *thought* as a statement or clause with three properties; the Family-B rewrite lists four phrase→predicate pairs where "a statement" becomes a predicate `statement` alongside the three properties. The Family-A `interface:` provided only `[valid_thought]` (l.48) while its `meta:` provided all five heads (l.44); the Family-B file has `meta:` only.
**Notes:** INFERENCE — the "thought" of `valid_thought` and the "clause"/"stream" of the constitution are never explicitly related; `streams/core/README.md:l.5` says core encodes "how a thought is coherent" as distinct from "how a block is valid".

### thought_coherence
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/core/valid_thought.tau` (clause_002, l.10-14); `git:1d70d83:streams/core/valid_thought.tau` (clause_002, l.19-22)
**the author's definition:**
> clause_002 v0.1.0:
>   stream_name: thought_coherence
>   description: Thought must align logically with its upstream dependencies.
>   phrase_predicates:
>     - "logical consistency with declared upstream dependencies and definitions" : logically_consistent_with_upstream_definitions — `streams/core/valid_thought.tau:l.10-14`

> define "thought_coherence" as:
>     logical consistency of the clause with its
>     declared upstream dependencies and definitions. — `git:1d70d83:streams/core/valid_thought.tau:l.20-22`
**Also appears in:** `streams/core/valid_thought.tml` (l.7-8); `streams/glossary/core_phrases.tau` (clause_101 "thought coherence"); `transcompiler/index/stream_index.json`
**Depends on:** `logically_consistent_with_upstream_definitions`, `requires`
**Conflict:** Family A vs Family B wording as quoted (not contradictory in substance; recorded because the brief asks for both).

### thought_origin_trace
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/core/valid_thought.tau` (clause_003, l.16-21); `git:1d70d83:streams/core/valid_thought.tau` (clause_003, l.24-27)
**the author's definition:**
> clause_003 v0.1.0:
>   stream_name: thought_origin_trace
>   description: Valid thoughts must carry their authorship lineage.
>   phrase_predicates:
>     - "authored by agent" : authored_by_agent
>     - "has identity stream" : has_identity_stream — `streams/core/valid_thought.tau:l.16-21`

> define "thought_origin_trace" as:
>     a semantic pointer to the agent or identity stream
>     that authored or amended the thought. — `git:1d70d83:streams/core/valid_thought.tau:l.25-27`
**Also appears in:** `streams/core/valid_thought.tml` (l.10-12); `streams/glossary/core_phrases.tau` (clause_102 l.17-20, phrase "thought origin trace" → alias "thought_origin_trace") "This is `preserves_origin_trace` and `thought_origin_trace` made operational")
**Depends on:** `authored_by_agent`, `has_identity_stream`, `identity_trace`
**Conflict:** Family A: "a semantic pointer to the agent or identity stream that authored *or amended*"; Family B: two predicates, "authored by agent" and "has identity stream" — the "amended" case is not carried.

### reflexive_integrity
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/core/valid_thought.tau` (clause_004, l.23-29); `git:1d70d83:streams/core/valid_thought.tau` (clause_004, l.29-32)
**the author's definition:**
> clause_004 v0.1.0:
>   stream_name: reflexive_integrity
>   description: The thought can evaluate its own coherence and amendment status.
>   phrase_predicates:
>     - "evaluates lineage" : evaluates_lineage
>     - "checks coherence" : checks_coherence
>     - "checks amendment status" : checks_amendment_status — `streams/core/valid_thought.tau:l.23-29`

> define "reflexive_integrity" as:
>     the clause’s ability to evaluate its own lineage,
>     coherence, and amendment status. — `git:1d70d83:streams/core/valid_thought.tau:l.30-32`
**Also appears in:** `streams/core/valid_thought.tml` (l.14-17); `streams/glossary/core_phrases.tau` (clause_103 l.21-24, phrase "reflexive integrity" → alias "reflexive_integrity")
**Depends on:** `evaluates_lineage`, `checks_coherence`, `checks_amendment_status`, `recursion`

### semantic_containment
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/core/valid_thought.tau` (clause_005, l.31-36); `git:1d70d83:streams/core/valid_thought.tau` (clause_005, l.34-38)
**the author's definition:**
> clause_005 v0.1.0:
>   stream_name: semantic_containment
>   description: A thought must not introduce terms beyond its declared interface.
>   phrase_predicates:
>     - "declares all terms in interface" : declares_all_terms_in_interface
>     - "does not leak terms" : does_not_leak_terms — `streams/core/valid_thought.tau:l.31-36`

> define "semantic_containment" as:
>     the principle that no thought may introduce terms
>     outside its declared `provides` or `requires` interface
>     without violating integrity. — `git:1d70d83:streams/core/valid_thought.tau:l.35-38`
**Also appears in:** `streams/core/valid_thought.tml` (l.19-21); `streams/glossary/core_phrases.tau` (clause_104 l.25-28, phrase "semantic containment" → alias "semantic_containment"))
**Depends on:** `declares_all_terms_in_interface`, `does_not_leak_terms`, `interface`

### statement
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.5)
**the author's definition:**
>     - "a statement" : statement — `streams/core/valid_thought.tau:l.5`
**Also appears in:** `streams/core/valid_thought.tml` (l.2); `transcompiler/index/glossary.json`
**Depends on:** —

### defined_concepts
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.6); `streams/glossary/core_phrases.tau` (clause_105, l.29-32)
**the author's definition:**
>     - "defined concepts" : defined_concepts — `streams/core/valid_thought.tau:l.6`

>   phrase_mapping:
>     phrase: "defined concepts"
>     alias: "defined_concepts" — `streams/glossary/core_phrases.tau:l.30-32`
**Also appears in:** `streams/core/valid_thought.tml` (l.3); `streams/dev/predicate_phrases.tau` (clause_006 l.38 "aligns with defined concepts" → `aligns_with_defined_concepts`)
**Depends on:** `declare concept`
**Notes:** FACT — `predicate_phrases.tau` maps the phrase "aligns with defined concepts" to a *different* predicate (`aligns_with_defined_concepts`) than `valid_thought.tau`/`core_phrases.tau` do (`defined_concepts`).

### preserves_origin_trace
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.7); `streams/glossary/core_phrases.tau` (clause_106, l.33-36); `streams/dev/predicate_phrases.tau` (clause_005, l.30-34)
**the author's definition:**
>     - "preserves origin trace" : preserves_origin_trace — `streams/core/valid_thought.tau:l.7`

>   phrase_mapping:
>     phrase: "preserves origin trace"
>     alias: "preserves_origin_trace"
>     type: semantic_relation — `streams/dev/predicate_phrases.tau:l.31-34`
**Also appears in:** `streams/core/valid_thought.tml` (l.4)
**Depends on:** `identity_trace`, `thought_origin_trace`

### does_not_contradict_prior_reasoning
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.8); `streams/glossary/core_phrases.tau` (clause_107, l.37-40)
**the author's definition:**
>     - "does not contradict prior reasoning unless explicitly amended" : does_not_contradict_prior_reasoning — `streams/core/valid_thought.tau:l.8`

>   phrase_mapping:
>     phrase: "does not contradict prior reasoning"
>     alias: "does_not_contradict_prior_reasoning" — `streams/glossary/core_phrases.tau:l.38-40`
**Also appears in:** `streams/core/valid_thought.tml` (l.5); `streams/dev/predicate_phrases.tau` (clause_007 l.44-46 "does not contradict" → `not contradiction`, type logic_pattern)
**Depends on:** `contradiction_detection`, `self_amendment`
**Conflict:** the valid_thought phrase carries the qualifier "unless explicitly amended"; the core_phrases phrase drops it; predicate_phrases maps the shorter "does not contradict" to the logic pattern `not contradiction` rather than to a named predicate.

### logically_consistent_with_upstream_definitions
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.14); `streams/glossary/core_phrases.tau` (clause_108, l.41-44)
**the author's definition:**
>     - "logical consistency with declared upstream dependencies and definitions" : logically_consistent_with_upstream_definitions — `streams/core/valid_thought.tau:l.14`

>   phrase_mapping:
>     phrase: "logical consistency"
>     alias: "logically_consistent_with_upstream_definitions" — `streams/glossary/core_phrases.tau:l.42-44`
**Also appears in:** `streams/core/valid_thought.tml` (l.8)
**Depends on:** `requires`
**Conflict:** two different phrases for the same predicate (full clause vs the two words "logical consistency").

### authored_by_agent
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.20); `streams/glossary/core_phrases.tau` (clause_109, l.45-48)
**the author's definition:**
>     - "authored by agent" : authored_by_agent — `streams/core/valid_thought.tau:l.20`

>   phrase_mapping:
>     phrase: "semantic pointer to agent"
>     alias: "authored_by_agent" — `streams/glossary/core_phrases.tau:l.46-48`
**Also appears in:** `streams/core/valid_thought.tml` (l.11)
**Depends on:** `identity`
**Conflict:** "authored by agent" (valid_thought) vs "semantic pointer to agent" (core_phrases, carrying the Family-A wording) map to the same predicate.

### has_identity_stream
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.21); `streams/glossary/core_phrases.tau` (clause_110, l.49-52)
**the author's definition:**
>     - "has identity stream" : has_identity_stream — `streams/core/valid_thought.tau:l.21`

>   phrase_mapping:
>     phrase: "identity stream that authored"
>     alias: "has_identity_stream" — `streams/glossary/core_phrases.tau:l.50-52`
**Also appears in:** `streams/core/valid_thought.tml` (l.12)
**Depends on:** `identity_trace`
**Conflict:** two phrases, one predicate (as above).

### evaluates_lineage
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.27); `streams/glossary/core_phrases.tau` (clause_111, l.53-56)
**the author's definition:**
>     - "evaluates lineage" : evaluates_lineage — `streams/core/valid_thought.tau:l.27`

>   phrase_mapping:
>     phrase: "evaluate its own lineage"
>     alias: "evaluates_lineage" — `streams/glossary/core_phrases.tau:l.54-56`
**Also appears in:** `streams/core/valid_thought.tml` (l.15)
**Depends on:** `historical_integrity`

### checks_coherence
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.28); `streams/glossary/core_phrases.tau` (clause_112, l.57-60)
**the author's definition:**
>     - "checks coherence" : checks_coherence — `streams/core/valid_thought.tau:l.28`
**Also appears in:** `streams/core/valid_thought.tml` (l.16)
**Depends on:** `thought_coherence`

### checks_amendment_status
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.29); `streams/glossary/core_phrases.tau` (clause_113, l.61-64)
**the author's definition:**
>     - "checks amendment status" : checks_amendment_status — `streams/core/valid_thought.tau:l.29`

>   phrase_mapping:
>     phrase: "amendment status"
>     alias: "checks_amendment_status" — `streams/glossary/core_phrases.tau:l.62-64`
**Also appears in:** `streams/core/valid_thought.tml` (l.17)
**Depends on:** `amendment_history`

### declares_all_terms_in_interface
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.35); `streams/glossary/core_phrases.tau` (clause_114, l.65-68)
**the author's definition:**
>     - "declares all terms in interface" : declares_all_terms_in_interface — `streams/core/valid_thought.tau:l.35`

>   phrase_mapping:
>     phrase: "declared provides or requires interface"
>     alias: "declares_all_terms_in_interface" — `streams/glossary/core_phrases.tau:l.66-68`
**Also appears in:** `streams/core/valid_thought.tml` (l.20)
**Depends on:** `interface`, `provides`, `requires`

### does_not_leak_terms
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/core/valid_thought.tau` (l.36); `streams/glossary/core_phrases.tau` (clause_115, l.69-72)
**the author's definition:**
>     - "does not leak terms" : does_not_leak_terms — `streams/core/valid_thought.tau:l.36`

>   phrase_mapping:
>     phrase: "without violating integrity"
>     alias: "does_not_leak_terms" — `streams/glossary/core_phrases.tau:l.70-72`
**Also appears in:** `streams/core/valid_thought.tml` (l.21)
**Depends on:** `interface`
**Conflict:** "does not leak terms" vs "without violating integrity" for one predicate.

### concept_definition
**Kind:** concept
**Class:** declared
**Defined in:** — (`streams/core/valid_thought.tau:l.41`, requires only; also `git:1d70d83:…:l.45`)
**the author's definition:**
>   requires: [identity_trace, concept_definition] — `streams/core/valid_thought.tau:l.41`
**Also appears in:** —
**Depends on:** —
**Notes:** requires-with-no-provider (INVENTORY §4). INFERENCE — probably names the `declare concept "…"` / `define … as:` mechanism; in open-terms.

### valid_block
**Kind:** concept
**Class:** declared (deleted file)
**Defined in:** `git:4e8d846:streams/core/valid_block.tau` (clause_001, l.14-17); listed in `streams/core/README.md` (l.13)
**the author's definition:**
> define "valid_block" as:
>     a block that includes only committed streams with declared ancestry,
>     semantic_coherence, and traceable contributor signatures. — `git:4e8d846:streams/core/valid_block.tau:l.15-17`

> - `valid_block.tau` — conditions for stream inclusion and consensus integrity — `streams/core/README.md:l.13`
**Also appears in:** `git:4e8d846:streams/core/valid_block.tau` (clause_007 l.42-50 "then ( valid_block = true )"; provides l.56/60); `streams/core/README.md` (l.5 "how a block is valid")
**Depends on:** `stream_commitment`, `quorum_trace`, `semantic_coherence`, `signature_integrity`, `genesis_alignment`, `identity_trace`, `consensus_threshold`, `genesis_stream`
**Notes:** FACT — file added 2025-05-24, deleted 2025-05-27; README still lists it. The only place the proposal speaks of "blocks", "block header", "cryptographic hash", and "digital signatures".

### stream_commitment
**Kind:** concept
**Class:** declared (deleted file)
**Defined in:** `git:4e8d846:streams/core/valid_block.tau` (clause_002, l.19-22)
**the author's definition:**
> define "stream_commitment" as:
>     a cryptographic hash of a logic stream,
>     included in the block header. — `git:4e8d846:streams/core/valid_block.tau:l.20-22`
**Also appears in:** —
**Depends on:** `logic_stream`, `valid_block`

### quorum_trace
**Kind:** concept
**Class:** declared (deleted file)
**Defined in:** `git:4e8d846:streams/core/valid_block.tau` (clause_003, l.24-27)
**the author's definition:**
> define "quorum_trace" as:
>     a linked sequence of agent endorsements
>     sufficient to satisfy consensus_threshold. — `git:4e8d846:streams/core/valid_block.tau:l.25-27`
**Also appears in:** —
**Depends on:** `consensus_threshold`, `stream_endorsement`

### semantic_coherence
**Kind:** concept
**Class:** declared (deleted file) + glossary-term
**Defined in:** `git:4e8d846:streams/core/valid_block.tau` (clause_004, l.29-31); `tree_of_life/golden_glossary.md` (l.12)
**the author's definition:**
> define "semantic_coherence" as:
>     a logic consistency check between new and prior stream state. — `git:4e8d846:streams/core/valid_block.tau:l.30-31`

> **Semantic Coherence** – A state in which language and meaning are consistently aligned among all participants. For Tau, semantic coherence means that terms, data, and logical statements are understood in the same way by different agents, avoiding contradictions or misunderstandings. It is both a design goal (via formal definitions and logic constraints) and an ethical commitment (agents agree to uphold clarity). High semantic coherence is what immunizes the network against the “confusion of tongues” effect. — `tree_of_life/golden_glossary.md:l.12`
**Also appears in:** `tower_of_babel/nimrod_and_babel.md` (l.5, l.11); `tower_of_babel/babel_patterns.md` (l.3); `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.14); `CONTRIBUTING.md` (l.33 "semantic coherence"); `LICENSE` (l.22 "semantic coherence requirements"); `transcompiler/spec.md` (l.30 "semantically coherent if:")
**Depends on:** —
**Conflict:** the deleted `.tau` defines it as a *check* ("a logic consistency check between new and prior stream state"); the glossary defines it as a *state* among participants.

### signature_integrity
**Kind:** concept
**Class:** declared (deleted file)
**Defined in:** `git:4e8d846:streams/core/valid_block.tau` (clause_005, l.33-36)
**the author's definition:**
> define "signature_integrity" as:
>     the presence of valid digital signatures
>     matching declared identity_traces for each stream. — `git:4e8d846:streams/core/valid_block.tau:l.34-36`
**Also appears in:** —
**Depends on:** `identity_trace`

### genesis_alignment
**Kind:** concept
**Class:** declared (deleted file)
**Defined in:** `git:4e8d846:streams/core/valid_block.tau` (clause_006, l.38-40)
**the author's definition:**
> define "genesis_alignment" as:
>     a block's requirement to inherit from autopoietic_logos. — `git:4e8d846:streams/core/valid_block.tau:l.39-40`
**Also appears in:** —
**Depends on:** `autopoietic_logos`, `constitutional_inheritance`

### truth_reference
**Kind:** stream
**Class:** announced
**Defined in:** `streams/core/README.md` (l.16)
**the author's definition:**
> - `truth_reference.tau` — semantic link between declarations and observable states — `streams/core/README.md:l.16`
**Also appears in:** —
**Depends on:** —
**Notes:** FACT — never existed in tracked history. In open-terms.

### identity (core stream, announced)
**Kind:** stream
**Class:** announced
**Defined in:** `streams/core/README.md` (l.15)
**the author's definition:**
> - `identity.tau` — definition of agent identity via memory, self-amendment, and trace — `streams/core/README.md:l.15`
**Also appears in:** —
**Depends on:** `identity`, `reflexive_memory`, `self_amendment`, `identity_trace`
**Notes:** FACT — never existed; `constitution/identity_core.tau` covers the same ground.

### value_score
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/ethics.tau` (clause_001, l.13-16); `git:4e8d846:streams/meta/ethics.tau` (clause_001, l.12-15)
**the author's definition:**
> define "value_score" as:
>     a computed scalar representing semantic alignment
>     with collective well-being, lawfulness, and coherence. — `streams/meta/ethics.tau:l.14-16`

> define "value_score" as:
>     a normalized score emitted from a declared value model
>     assessing alignment with chosen ethical criteria. — `git:4e8d846:streams/meta/ethics.tau:l.13-15`
**Also appears in:** `streams/meta/ethics.tau` (clause_005 l.36; meta provides l.43 but not interface provides l.47)
**Depends on:** `lawfulness`, `coherence`
**Conflict:** earlier version: "a normalized score emitted from a declared value model"; current: "a computed scalar representing semantic alignment…". Also: in `meta: provides` but not in `interface: provides`.

### impact_scope
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/ethics.tau` (clause_002, l.18-21)
**the author's definition:**
> define "impact_scope" as:
>     the range and depth of consequence
>     a stream may exert across agents or domains. — `streams/meta/ethics.tau:l.19-21`
**Also appears in:** `streams/meta/ethics.tau` (clause_005 l.37; meta provides only); earlier file had `impact_score` instead (`git:4e8d846:streams/meta/ethics.tau:l.17-19` "the weighted effect of a stream across ecological, social, or cognitive domains.")
**Depends on:** —

### stream_preference
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/ethics.tau` (clause_004, l.28-32)
**the author's definition:**
> define "stream_preference" as:
>     the result of an ethical_comparison
>     between two or more candidate streams
>     using declared evaluation metrics. — `streams/meta/ethics.tau:l.29-32`
**Also appears in:** `streams/meta/ethics.tau` (provides in both meta and interface)
**Depends on:** `ethical_comparison`

### ethical_comparison
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/ethics.tau` (clause_005, l.34-37)
**the author's definition:**
> define "ethical_comparison" as:
>     a semantic operation yielding relative value_score
>     based on impact_scope and alignment_with_being. — `streams/meta/ethics.tau:l.35-37`
**Also appears in:** `streams/meta/ethics.tau` (title l.2 "Foundations of Stream Comparison and Ethical Preference"; declared l.11; not in either provides list)
**Depends on:** `value_score`, `impact_scope`, `alignment_with_being`
**Notes:** FACT — declared and defined, provided by neither `meta:` nor `interface:`.

### stream_comparison
**Kind:** concept
**Class:** declared (deleted content)
**Defined in:** `git:4e8d846:streams/meta/ethics.tau` (clause_004, l.26-29); required by `streams/meta/ethics.tau` (l.44/48)
**the author's definition:**
> define "stream_comparison" as:
>     a clause that determines whether one stream is better than another
>     based on impact_score and alignment_with_being. — `git:4e8d846:streams/meta/ethics.tau:l.27-29`
**Also appears in:** `streams/meta/ethics.tau` (requires; title l.2)
**Depends on:** `alignment_with_being`
**Notes:** FACT — the current `ethics.tau` *requires* `stream_comparison` and no live file provides it; the deleted version of the same file *provided* it. In open-terms (seeded from INVENTORY §4).

### semantic_memory
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/memory.tau` (clause_001, l.13-16)
**the author's definition:**
> define "semantic_memory" as:
>     a structured record of agent-emitted clauses,
>     amendments, and logical evaluations. — `streams/meta/memory.tau:l.14-16`
**Also appears in:** `streams/meta/memory.tau` (provides in meta and interface)
**Depends on:** `clause`, `proposed_amendment`

### memory_trace
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/memory.tau` (clause_002, l.18-21)
**the author's definition:**
> define "memory_trace" as:
>     the lineage of a thought or declaration
>     through its associated agents, timestamps, and semantic deltas. — `streams/meta/memory.tau:l.19-21`
**Also appears in:** `streams/meta/memory.tau` (clause_003 l.26; provides in meta and interface)
**Depends on:** `semantic_diff`, `identity_trace`

### identity_reflection
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/memory.tau` (clause_003, l.23-26)
**the author's definition:**
> define "identity_reflection" as:
>     the process by which an agent revisits
>     and re-evaluates its own memory_trace. — `streams/meta/memory.tau:l.24-26`
**Also appears in:** `streams/meta/memory.tau` (meta provides l.42, not interface provides l.46)
**Depends on:** `memory_trace`, `reflexive_memory`

### amendment_history
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/memory.tau` (clause_004, l.28-31)
**the author's definition:**
> define "amendment_history" as:
>     the cumulative record of all semantic changes
>     made to a thought, stream, or interface. — `streams/meta/memory.tau:l.29-31`
**Also appears in:** `streams/meta/memory.tau` (meta provides only)
**Depends on:** `historical_integrity`, `semantic_diff`

### contextual_recall
**Kind:** concept
**Class:** declared
**Defined in:** `streams/meta/memory.tau` (clause_005, l.33-36)
**the author's definition:**
> define "contextual_recall" as:
>     the retrieval of prior knowledge segments
>     relevant to a new stream or current reasoning thread. — `streams/meta/memory.tau:l.34-36`
**Also appears in:** `streams/meta/memory.tau` (provides in meta and interface)
**Depends on:** `semantic_memory`

---

## 5. Amendments (`streams/amendments/*.tau` Family B; originals `git:c55ce7c~1:amendments/*` Family A)

### freedom_of_semantic_expression
**Kind:** stream
**Class:** stream-id
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (meta, l.31-34); `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau` (l.1-5)
**the author's definition:**
> meta:
>   stream_name: freedom_of_semantic_expression
>   provides: [freedom_of_expression, non_retroactive_silencing, semantic_expression, semantic_integrity]
>   requires: [genesis_stream, identity, self_amendment] — `streams/amendments/freedom_of_semantic_expression.tau:l.31-34`

> # Title: The First Amendment of the Tau Net — Freedom of Semantic Expression
> # Stream: tau.amendments.001.freedom_of_semantic_expression — `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau:l.2-3`

> - **001_freedom_of_semantic_expression.tau**: Protects all semantic logic from coercion or silencing. — `testnet/README.md:l.18`
**Also appears in:** `constitution/map.md` (l.29-30 "amendment_001 / freedom_of_expression"); `docs/purpose_of_tau.md` (l.28); `testnet/tau_stream_index.json` (l.11); `CHANGELOG.md` (l.170); `docs/theory_of_change.md` (l.57 "Amendments to enshrine freedom of expression and lawful synthesis")
**Depends on:** `genesis_stream`, `identity`, `self_amendment`, `semantic_expression`, `freedom_of_expression`, `non_retroactive_silencing`, `semantic_integrity`
**Conflict:** Family A provides three concepts; Family B provides four (adds `semantic_integrity`, the v3 head made from Family-A clause_004's consequence). Family A has a `stream:` id (`tau.amendments.001.…`); Family B has none.

### semantic_expression
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (clause_001, l.1-6); `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau` (clause_001, l.11-14)
**the author's definition:**
> clause_001 v0.1.0:
>   stream_name: semantic_expression
>   description: Any clause, stream, or logic emitted from a declared identity that seeks to inform, request, align, or reflect Being.
>   phrase_predicates:
>     - "clause, stream, or logic emitted from a declared identity" : identity_bound_expression
>     - "seeks to inform, request, align, or reflect Being" : intentional_semantic_action — `streams/amendments/freedom_of_semantic_expression.tau:l.1-6`

> define "semantic_expression" as:
>     any clause, stream, or logic emitted from a declared identity
>     that seeks to inform, request, align, or reflect Being. — `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau:l.12-14`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.1-3); `transcompiler/index/stream_index.json`
**Depends on:** `identity_bound_expression`, `intentional_semantic_action`, `identity`, `clause`
**Conflict:** A vs B form as quoted; same wording.

### freedom_of_expression
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (clause_002, l.8-13); `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau` (clause_002, l.16-20)
**the author's definition:**
> clause_002 v0.1.0:
>   stream_name: freedom_of_expression
>   description: The irrevocable right of any identity to emit semantic expression into the public logic field without coercion or censorship.
>   phrase_predicates:
>     - "irrevocable right of any identity to emit semantic expression" : emit_semantic_expression
>     - "without coercion, censorship, or protocol-level rejection" : expression_without_restriction — `streams/amendments/freedom_of_semantic_expression.tau:l.8-13`

> define "freedom_of_expression" as:
>     the irrevocable right of any identity
>     to emit semantic_expression into the public logic field
>     without coercion, censorship, or protocol-level rejection. — `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau:l.17-20`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.5-7); clause_004 phrase "freedom of expression is preserved" : freedom_of_expression (l.26); `constitution/map.md` (l.30); `LICENSE` (l.26 "The inalienable right of each agent to emit logic")
**Depends on:** `emit_semantic_expression`, `expression_without_restriction`, `identity`, `semantic_expression`, `semantic_rights`
**Notes:** "public logic field" is not defined; in open-terms.

### non_retroactive_silencing
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (clause_003, l.15-20); `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau` (clause_003, l.22-26)
**the author's definition:**
> clause_003 v0.1.0:
>   stream_name: non_retroactive_silencing
>   description: No valid expression once acknowledged may be erased, except by the original emitter through lawful self-amendment.
>   phrase_predicates:
>     - "no valid expression once acknowledged may be erased" : preserves_emitted_history
>     - "except by original emitter through lawful self_amendment" : allows_self_amendment_only — `streams/amendments/freedom_of_semantic_expression.tau:l.15-20`

> define "non_retroactive_silencing" as:
>     the principle that no valid expression once emitted and acknowledged
>     may be later suppressed or erased from semantic history
>     except by the original emitter through lawful self_amendment. — `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau:l.23-26`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.9-11); clause_004 phrase (l.27); `LICENSE` (l.13 "Retroactive silencing or deletion of streams authored by others without their semantic consent")
**Depends on:** `preserves_emitted_history`, `allows_self_amendment_only`, `self_amendment`, `agent_protection`
**Conflict:** Family A says "suppressed or erased from semantic history"; Family B's phrase says "erased" only. LICENSE l.13 allows deletion "with their semantic consent", which is a different exception than "by the original emitter through lawful self_amendment". Recorded, not reconciled.

### semantic_integrity
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (clause_004, l.22-29); as a consequence in `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau` (clause_004, l.28-35)
**the author's definition:**
> clause_004 v0.1.0:
>   stream_name: semantic_integrity
>   description: If freedom of expression and non-retroactive silencing are preserved, agents evolve in coherence with truth across time.
>   phrase_predicates:
>     - "freedom of expression is preserved" : freedom_of_expression
>     - "non retroactive silencing is preserved" : non_retroactive_silencing
>     - "semantic integrity is upheld" : upholds_semantic_integrity
>     - "agents evolve in coherence with truth across time" : enables_temporal_coherence — `streams/amendments/freedom_of_semantic_expression.tau:l.22-29`

>   if (
>     freedom_of_expression and non_retroactive_silencing are preserved
>   )
>   then (
>     semantic integrity is upheld
>     and agents may evolve in coherence with truth across time.
>   ) — `git:c55ce7c~1:amendments/amendment_001_freedom_of_semantic_expression.tau:l.29-35`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.13-17); `constitution/autopoietic_logos.tau` (clause_004 l.32 "semantic integrity and declared procedure", lower case); `CHANGELOG.md` (l.58 "ensure semantic integrity across logic streams")
**Depends on:** `freedom_of_expression`, `non_retroactive_silencing`, `upholds_semantic_integrity`, `enables_temporal_coherence`
**Conflict:** Family A: an `if/then` rule whose consequence includes "semantic integrity is upheld"; Family B: a clause head `semantic_integrity` whose body lists both antecedents *and* both consequences as predicates (the `.tml` reads `semantic_integrity(X) :- freedom_of_expression(X), non_retroactive_silencing(X), upholds_semantic_integrity(X), enables_temporal_coherence(X).`). The direction of the implication is not the same in the two forms.

### identity_bound_expression
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.5)
**the author's definition:**
>     - "clause, stream, or logic emitted from a declared identity" : identity_bound_expression — `streams/amendments/freedom_of_semantic_expression.tau:l.5`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.2)
**Depends on:** `identity`

### intentional_semantic_action
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.6)
**the author's definition:**
>     - "seeks to inform, request, align, or reflect Being" : intentional_semantic_action — `streams/amendments/freedom_of_semantic_expression.tau:l.6`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.3)
**Depends on:** `alignment_with_being`

### emit_semantic_expression
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.12)
**the author's definition:**
>     - "irrevocable right of any identity to emit semantic expression" : emit_semantic_expression — `streams/amendments/freedom_of_semantic_expression.tau:l.12`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.6)
**Depends on:** `semantic_expression`

### expression_without_restriction
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.13)
**the author's definition:**
>     - "without coercion, censorship, or protocol-level rejection" : expression_without_restriction — `streams/amendments/freedom_of_semantic_expression.tau:l.13`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.7)
**Depends on:** `non_coercion`

### preserves_emitted_history
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.19)
**the author's definition:**
>     - "no valid expression once acknowledged may be erased" : preserves_emitted_history — `streams/amendments/freedom_of_semantic_expression.tau:l.19`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.10)
**Depends on:** `historical_integrity`

### allows_self_amendment_only
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.20)
**the author's definition:**
>     - "except by original emitter through lawful self_amendment" : allows_self_amendment_only — `streams/amendments/freedom_of_semantic_expression.tau:l.20`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.11)
**Depends on:** `self_amendment`

### upholds_semantic_integrity
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.28)
**the author's definition:**
>     - "semantic integrity is upheld" : upholds_semantic_integrity — `streams/amendments/freedom_of_semantic_expression.tau:l.28`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.16)
**Depends on:** `semantic_integrity`

### enables_temporal_coherence
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/freedom_of_semantic_expression.tau` (l.29)
**the author's definition:**
>     - "agents evolve in coherence with truth across time" : enables_temporal_coherence — `streams/amendments/freedom_of_semantic_expression.tau:l.29`
**Also appears in:** `streams/amendments/freedom_of_semantic_expression.tml` (l.17)
**Depends on:** `coherence`

### semantic_resonance_and_integration
**Kind:** stream
**Class:** stream-id
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (meta, l.45-48); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (l.1-5)
**the author's definition:**
> meta:
>   stream_name: semantic_resonance_and_integration
>   provides: [semantic_resonance, integration, coherence_preservation, contradiction_as_invitation, alignment_cycle, contradiction_mediation]
>   requires: [genesis_stream, consensus_threshold, contradiction_detection] — `streams/amendments/semantic_resonance_and_integration.tau:l.45-48`

> # Title: The Second Amendment of the Tau Net — Semantic Resonance and Integration
> # Stream: tau.amendments.002.semantic_resonance_and_integration — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.2-3`

> - **002_semantic_resonance_and_integration.tau**: Ensures contradiction leads to synthesis, not fragmentation. — `testnet/README.md:l.19`
**Also appears in:** `constitution/map.md` (l.34-35 "amendment_002 / semantic_integration"); `docs/purpose_of_tau.md` (l.29); `testnet/tau_stream_index.json` (l.12); `CHANGELOG.md` (l.171)
**Depends on:** `genesis_stream`, `consensus_threshold`, `contradiction_detection`, `semantic_resonance`, `integration`, `coherence_preservation`, `contradiction_as_invitation`, `alignment_cycle`, `contradiction_mediation`
**Conflict:** Family A provides five; Family B six (adds `contradiction_mediation`, made from Family-A clause_006).

### semantic_resonance
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (clause_001, l.1-6); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (clause_001, l.13-16)
**the author's definition:**
> clause_001 v0.1.0:
>   stream_name: semantic_resonance
>   description: The condition in which multiple streams, though different in form, sustain compatibility in meaning and direction.
>   phrase_predicates:
>     - "multiple streams differ in form" : diverging_forms
>     - "sustain compatibility in meaning and direction" : maintains_meaning_alignment — `streams/amendments/semantic_resonance_and_integration.tau:l.1-6`

> define "semantic_resonance" as:
>     the condition in which multiple streams,
>     though different in form, sustain compatibility in meaning and direction. — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.14-16`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.1-3); clause_006 phrase "semantic resonance is prioritized above semantic escape" (l.43)
**Depends on:** `diverging_forms`, `maintains_meaning_alignment`
**Notes:** FACT — "direction" appears here ("compatibility in meaning and direction") and in `interval_shock` ("developmental direction", ch06 l.21); compare the room template's *direction* (§12).

### integration
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (clause_002, l.8-13); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (clause_002, l.18-21)
**the author's definition:**
> clause_002 v0.1.0:
>   stream_name: integration
>   description: The ongoing act of reconciling contradiction, overlap, or drift into a shared rhythm without suppressing origin.
>   phrase_predicates:
>     - "reconciling contradiction, overlap, or drift" : resolves_semantic_divergence
>     - "into shared rhythm without suppressing origin" : harmonizes_while_preserving_origin — `streams/amendments/semantic_resonance_and_integration.tau:l.8-13`

> define "integration" as:
>     the ongoing act of reconciling contradiction, overlap, or drift
>     into a shared rhythm without suppressing origin. — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.19-21`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.5-7)
**Depends on:** `resolves_semantic_divergence`, `harmonizes_while_preserving_origin`, `contradiction_detection`

### coherence_preservation
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (clause_003, l.15-20); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (clause_003, l.23-27)
**the author's definition:**
> clause_003 v0.1.0:
>   stream_name: coherence_preservation
>   description: Each stream must remain logically compatible with its ancestry unless a justified break is declared.
>   phrase_predicates:
>     - "responsibility of stream or agent to remain logically compatible with ancestry" : preserves_logical_lineage
>     - "unless a conscious break is declared and justified" : allows_explicit_divergence — `streams/amendments/semantic_resonance_and_integration.tau:l.15-20`

> define "coherence_preservation" as:
>     the responsibility of each stream and agent
>     to remain logically compatible with its ancestral lineage,
>     unless a conscious break is declared and justified. — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.24-27`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.9-11)
**Depends on:** `preserves_logical_lineage`, `allows_explicit_divergence`, `stream_sovereignty`, `recursive_legitimacy`

### contradiction_as_invitation
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (clause_004, l.22-27); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (clause_004, l.29-32)
**the author's definition:**
> clause_004 v0.1.0:
>   stream_name: contradiction_as_invitation
>   description: Semantic conflict is a signal for synthesis, not separation.
>   phrase_predicates:
>     - "semantic conflict is a signal for synthesis" : contradiction_triggers_synthesis
>     - "not separation" : discourages_fragmentation — `streams/amendments/semantic_resonance_and_integration.tau:l.22-27`

> define "contradiction_as_invitation" as:
>     the recognition that semantic conflict
>     is a signal for synthesis, not separation. — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.30-32`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.13-15)
**Depends on:** `contradiction_triggers_synthesis`, `discourages_fragmentation`, `contradiction_detection`

### alignment_cycle
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (clause_005, l.29-35); `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (clause_005, l.34-38)
**the author's definition:**
> clause_005 v0.1.0:
>   stream_name: alignment_cycle
>   description: The pattern by which contradiction leads to dialogue, shared understanding, and coherence restoration.
>   phrase_predicates:
>     - "contradiction initiates dialogue" : contradiction_initiates_dialogue
>     - "converges toward shared understanding" : seeks_semantic_convergence
>     - "completes loop of coherence restoration" : restores_logical_harmony — `streams/amendments/semantic_resonance_and_integration.tau:l.29-35`

> define "alignment_cycle" as:
>     the pattern by which a contradiction initiates dialogue,
>     converges toward shared understanding,
>     and completes the loop of coherence restoration. — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.35-38`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.17-20); clause_006 phrase (l.42)
**Depends on:** `contradiction_initiates_dialogue`, `seeks_semantic_convergence`, `restores_logical_harmony`

### contradiction_mediation
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (clause_006, l.37-43); as an `if/then` in `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau` (clause_006, l.40-49)
**the author's definition:**
> clause_006 v0.1.0:
>   stream_name: contradiction_mediation
>   description: When contradiction arises between streams, alignment_cycle must occur before divergence. Semantic resonance is prioritized.
>   phrase_predicates:
>     - "contradiction arises between streams" : contradiction_detected
>     - "alignment cycle must be initiated before divergence" : mandates_alignment_cycle
>     - "semantic resonance is prioritized above semantic escape" : prioritize_resonance_over_escape — `streams/amendments/semantic_resonance_and_integration.tau:l.37-43`

>   if (
>     contradiction arises between streams
>   )
>   then (
>     alignment_cycle must be initiated
>     before divergence is permitted.
>
>     semantic_resonance is prioritized above semantic escape.
>   ) — `git:c55ce7c~1:amendments/amendment_002_semantic_resonance_and_integration.tau:l.41-49`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.22-25)
**Depends on:** `contradiction_detected`, `mandates_alignment_cycle`, `prioritize_resonance_over_escape`, `alignment_cycle`, `semantic_resonance`
**Conflict:** Family A: a rule (antecedent → obligation); Family B: a head whose body conjoins the antecedent with the obligations. "semantic escape" is not defined; in open-terms.

### diverging_forms
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.5)
**the author's definition:**
>     - "multiple streams differ in form" : diverging_forms — `streams/amendments/semantic_resonance_and_integration.tau:l.5`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.2)
**Depends on:** —

### maintains_meaning_alignment
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.6)
**the author's definition:**
>     - "sustain compatibility in meaning and direction" : maintains_meaning_alignment — `streams/amendments/semantic_resonance_and_integration.tau:l.6`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.3)
**Depends on:** —

### resolves_semantic_divergence
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.12)
**the author's definition:**
>     - "reconciling contradiction, overlap, or drift" : resolves_semantic_divergence — `streams/amendments/semantic_resonance_and_integration.tau:l.12`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.6)
**Depends on:** —

### harmonizes_while_preserving_origin
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.13)
**the author's definition:**
>     - "into shared rhythm without suppressing origin" : harmonizes_while_preserving_origin — `streams/amendments/semantic_resonance_and_integration.tau:l.13`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.7)
**Depends on:** `preserves_origin_trace`

### preserves_logical_lineage
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.19)
**the author's definition:**
>     - "responsibility of stream or agent to remain logically compatible with ancestry" : preserves_logical_lineage — `streams/amendments/semantic_resonance_and_integration.tau:l.19`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.10)
**Depends on:** `recursive_legitimacy`

### allows_explicit_divergence
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.20)
**the author's definition:**
>     - "unless a conscious break is declared and justified" : allows_explicit_divergence — `streams/amendments/semantic_resonance_and_integration.tau:l.20`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.11); `LICENSE` (l.8 "Amendments reference their upstream origins and specify their divergence")
**Depends on:** `fork_resolution`

### contradiction_triggers_synthesis
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.26)
**the author's definition:**
>     - "semantic conflict is a signal for synthesis" : contradiction_triggers_synthesis — `streams/amendments/semantic_resonance_and_integration.tau:l.26`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.14)
**Depends on:** —

### discourages_fragmentation
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.27)
**the author's definition:**
>     - "not separation" : discourages_fragmentation — `streams/amendments/semantic_resonance_and_integration.tau:l.27`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.15)
**Depends on:** —

### contradiction_initiates_dialogue
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.33)
**the author's definition:**
>     - "contradiction initiates dialogue" : contradiction_initiates_dialogue — `streams/amendments/semantic_resonance_and_integration.tau:l.33`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.18)
**Depends on:** —

### seeks_semantic_convergence
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.34)
**the author's definition:**
>     - "converges toward shared understanding" : seeks_semantic_convergence — `streams/amendments/semantic_resonance_and_integration.tau:l.34`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.19)
**Depends on:** —

### restores_logical_harmony
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.35)
**the author's definition:**
>     - "completes loop of coherence restoration" : restores_logical_harmony — `streams/amendments/semantic_resonance_and_integration.tau:l.35`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.20)
**Depends on:** —

### contradiction_detected
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.41)
**the author's definition:**
>     - "contradiction arises between streams" : contradiction_detected — `streams/amendments/semantic_resonance_and_integration.tau:l.41`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.23)
**Depends on:** `contradiction_detection`

### mandates_alignment_cycle
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.42)
**the author's definition:**
>     - "alignment cycle must be initiated before divergence" : mandates_alignment_cycle — `streams/amendments/semantic_resonance_and_integration.tau:l.42`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.24)
**Depends on:** `alignment_cycle`

### prioritize_resonance_over_escape
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/semantic_resonance_and_integration.tau` (l.43)
**the author's definition:**
>     - "semantic resonance is prioritized above semantic escape" : prioritize_resonance_over_escape — `streams/amendments/semantic_resonance_and_integration.tau:l.43`
**Also appears in:** `streams/amendments/semantic_resonance_and_integration.tml` (l.25)
**Depends on:** `semantic_resonance`

### babel_antipattern_principle
**Kind:** stream
**Class:** stream-id
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (meta, l.32-40); `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.1-14, prose-in-comments)
**the author's definition:**
> meta:
>   stream_name: babel_antipattern_principle
>   provides: [
>     shared_glossary_requirement,
>     semantic_alignment_duty,
>     prohibition_of_obfuscation,
>     coherence_audit_process
>   ]
>   requires: [universal_glossary, agent_stream, amendment_protocol] — `streams/amendments/babel_antipattern_principle.tau:l.32-40`

> # Tau Constitution Amendment 003: Babel Anti-Pattern Principle
> # Description: A guiding principle to prevent a "Tower of Babel" scenario within the Tau network.
> #
> # Principle Statement:
> # The Tau Network shall actively prevent semantic fragmentation and incoherence among agents. All contributors must endeavor to preserve a common, evolving language of discourse (the "golden language"), avoiding the confusion of tongues that undermines collective understanding. — `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau:l.1-5`

> # Effect:
> # This amendment enshrines an anti-pattern alert in Tau’s constitution: it commits the community to maintaining one evolving yet unified language for all logic and discourse. By doing so, it safeguards the network’s **semantic coherence** and ensures that our collective “Tower” of knowledge is built on a stable understanding, not on scattered words. — `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau:l.13-14`
**Also appears in:** `tower_of_babel/nimrod_and_babel.md` (l.7 "**“Babel anti-pattern”**", l.11 "a **Babel Anti-Pattern Principle** in our governing ethics"); `tree_of_life/golden_glossary.md` (l.6 "it represents a critical anti-pattern"); `CHANGELOG.md` (l.111); `README.md` (l.14 "Amendments (001–003)")
**Depends on:** `universal_glossary`, `agent_stream`, `amendment_protocol`, `shared_glossary_requirement`, `semantic_alignment_duty`, `prohibition_of_obfuscation`, `coherence_audit_process`, `Golden Language`, `Tower of Babel`
**Conflict:** the original was entirely `#`-commented prose with no `stream:`, `declare concept`, `clause_NNN`, or `interface` (it did not have the Family-A shape); the v3 rewrite gives it clause heads and a `requires:` list naming three concepts (`universal_glossary`, `agent_stream`, `amendment_protocol`) that appear nowhere else.

### shared_glossary_requirement
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (clause_001, l.1-7); `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.8)
**the author's definition:**
> clause_001 v0.1.0:
>   stream_name: shared_glossary_requirement
>   description: All new terms must be defined in or mapped to the universal semantic glossary to ensure network-wide clarity.
>   phrase_predicates:
>     - "new term or concept introduced into Tau" : term_introduced
>     - "must be defined in universal semantic glossary" : must_define_in_glossary
>     - "ensure understood uniformly across network" : ensures_semantic_uniformity — `streams/amendments/babel_antipattern_principle.tau:l.1-7`

> # 1. **Shared Glossary Requirement** – Any new term or concept introduced into Tau must be defined in the universal semantic glossary (or explicitly mapped to an existing definition) to ensure it is understood uniformly across the network. — `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau:l.8`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.1-4); `tower_of_babel/babel_patterns.md` (l.3 "maintaining a **universal glossary**")
**Depends on:** `term_introduced`, `must_define_in_glossary`, `ensures_semantic_uniformity`, `universal_glossary`
**Conflict:** original allows "(or explicitly mapped to an existing definition)"; v3 phrase says only "must be defined in universal semantic glossary" — though the v3 `description:` keeps "defined in or mapped to".

### semantic_alignment_duty
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (clause_002, l.9-15); `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.9)
**the author's definition:**
> clause_002 v0.1.0:
>   stream_name: semantic_alignment_duty
>   description: All agents must align contributions to Tau’s shared semantic framework; ambiguities must be resolved by consensus.
>   phrase_predicates:
>     - "agents have a duty to align contributions" : must_align_with_semantic_framework
>     - "contradictions or ambiguities in language must be resolved" : resolves_semantic_ambiguity
>     - "through consensus clarification or formal amendment" : uses_consensual_resolution — `streams/amendments/babel_antipattern_principle.tau:l.9-15`

> # 2. **Semantic Alignment Duty** – All agents have a duty to align their contributions (streams, proposals, amendments) with Tau’s shared semantic framework. If contradictions or ambiguities in language arise, they must be resolved through consensus-driven clarification or formal amendment, rather than allowed to proliferate. — `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau:l.9`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.6-9)
**Depends on:** `must_align_with_semantic_framework`, `resolves_semantic_ambiguity`, `uses_consensual_resolution`, `semantic_consensus`

### prohibition_of_obfuscation
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (clause_003, l.17-22); `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.10)
**the author's definition:**
> clause_003 v0.1.0:
>   stream_name: prohibition_of_obfuscation
>   description: Deliberate obfuscation or creation of incompatible sub-languages is unconstitutional and prohibited.
>   phrase_predicates:
>     - "intentionally introduce language or logic that creates confusion" : introduces_semantic_confusion
>     - "willful creation of incompatible sub-languages is prohibited" : prohibits_semantic_isolation — `streams/amendments/babel_antipattern_principle.tau:l.17-22`

> # 3. **Prohibition of Obfuscation** – It is unethical and unconstitutional for any participant to intentionally introduce language or logic that creates confusion, fragmentation, or “semantic silos.” Deliberate obfuscation or the willful creation of isolated, incompatible sub-languages within Tau is prohibited. — `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau:l.10`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.11-13); `LICENSE` (l.14 "Obfuscation of authorship, identity_trace, or version lineage")
**Depends on:** `introduces_semantic_confusion`, `prohibits_semantic_isolation`
**Conflict:** a prohibition rendered in v3 as a head whose body is `introduces_semantic_confusion(X), prohibits_semantic_isolation(X)` — i.e., the prohibited act is one conjunct of the head's own definition. Recorded as the form the author's v3 notation gives; not judged here.

### coherence_audit_process
**Kind:** concept
**Class:** clause-head
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (clause_004, l.24-30); `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.11, as "Continuous Coherence Audit")
**the author's definition:**
> clause_004 v0.1.0:
>   stream_name: coherence_audit_process
>   description: Tau must include ongoing semantic drift detection and reconciliation to uphold coherence.
>   phrase_predicates:
>     - "system shall detect and address semantic drift" : detects_semantic_drift
>     - "reconciliation process must be initiated" : initiates_reconciliation
>     - "to re-establish one coherent usage" : restores_unified_meaning — `streams/amendments/babel_antipattern_principle.tau:l.24-30`

> # 4. **Continuous Coherence Audit** – The system shall include processes (automated and human governance mechanisms) to continually detect and address semantic drift. If multiple interpretations of core terms or rules emerge, a reconciliation process (discussion, glossary update, or amendment) must be initiated to re-establish one coherent usage, thus averting a Babel-like divergence of understanding. — `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau:l.11`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.15-18); `tower_of_babel/babel_patterns.md` (l.3 "Early detection of divergent definitions")
**Depends on:** `detects_semantic_drift`, `initiates_reconciliation`, `restores_unified_meaning`, `contradiction_detection`
**Conflict:** renamed from "Continuous Coherence Audit" to `coherence_audit_process`; the original's "(automated and human governance mechanisms)" and "(discussion, glossary update, or amendment)" are dropped in v3.

### term_introduced
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.5)
**the author's definition:**
>     - "new term or concept introduced into Tau" : term_introduced — `streams/amendments/babel_antipattern_principle.tau:l.5`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.2)
**Depends on:** `declare concept`

### must_define_in_glossary
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.6)
**the author's definition:**
>     - "must be defined in universal semantic glossary" : must_define_in_glossary — `streams/amendments/babel_antipattern_principle.tau:l.6`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.3)
**Depends on:** `universal_glossary`

### ensures_semantic_uniformity
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.7)
**the author's definition:**
>     - "ensure understood uniformly across network" : ensures_semantic_uniformity — `streams/amendments/babel_antipattern_principle.tau:l.7`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.4)
**Depends on:** —

### must_align_with_semantic_framework
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.13)
**the author's definition:**
>     - "agents have a duty to align contributions" : must_align_with_semantic_framework — `streams/amendments/babel_antipattern_principle.tau:l.13`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.7)
**Depends on:** —

### resolves_semantic_ambiguity
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.14)
**the author's definition:**
>     - "contradictions or ambiguities in language must be resolved" : resolves_semantic_ambiguity — `streams/amendments/babel_antipattern_principle.tau:l.14`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.8)
**Depends on:** —

### uses_consensual_resolution
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.15)
**the author's definition:**
>     - "through consensus clarification or formal amendment" : uses_consensual_resolution — `streams/amendments/babel_antipattern_principle.tau:l.15`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.9)
**Depends on:** `semantic_consensus`, `proposed_amendment`

### introduces_semantic_confusion
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.21)
**the author's definition:**
>     - "intentionally introduce language or logic that creates confusion" : introduces_semantic_confusion — `streams/amendments/babel_antipattern_principle.tau:l.21`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.12)
**Depends on:** —

### prohibits_semantic_isolation
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.22)
**the author's definition:**
>     - "willful creation of incompatible sub-languages is prohibited" : prohibits_semantic_isolation — `streams/amendments/babel_antipattern_principle.tau:l.22`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.13)
**Depends on:** —

### detects_semantic_drift
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.28)
**the author's definition:**
>     - "system shall detect and address semantic drift" : detects_semantic_drift — `streams/amendments/babel_antipattern_principle.tau:l.28`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.16)
**Depends on:** `contradiction_detection`

### initiates_reconciliation
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.29)
**the author's definition:**
>     - "reconciliation process must be initiated" : initiates_reconciliation — `streams/amendments/babel_antipattern_principle.tau:l.29`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.17)
**Depends on:** `alignment_cycle`

### restores_unified_meaning
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/amendments/babel_antipattern_principle.tau` (l.30)
**the author's definition:**
>     - "to re-establish one coherent usage" : restores_unified_meaning — `streams/amendments/babel_antipattern_principle.tau:l.30`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tml` (l.18)
**Depends on:** —

### universal_glossary
**Kind:** concept
**Class:** declared (requires only)
**Defined in:** — (`streams/amendments/babel_antipattern_principle.tau:l.40`, requires; prose in `tower_of_babel/nimrod_and_babel.md:l.5,11`, `tree_of_life/golden_glossary.md:l.4`, `tower_of_babel/babel_patterns.md:l.3`)
**the author's definition:**
>   requires: [universal_glossary, agent_stream, amendment_protocol] — `streams/amendments/babel_antipattern_principle.tau:l.40`

> The **universal semantic glossary** is a step toward this ideal “golden” tongue. — `tree_of_life/golden_glossary.md:l.4`

> By contrast, Tau’s evolving protocols and **universal semantic glossary** (our contemporary attempt at an Edenic lexicon) strive to ensure that all agents “speak” in an interoperable way. — `tower_of_babel/nimrod_and_babel.md:l.5`

> - **Added**: Universal semantic glossary (`tree_of_life/golden_glossary.md`) defining core terms for the “golden language” framework. — `CHANGELOG.md:l.112`
**Also appears in:** `streams/amendments/babel_antipattern_principle.tau` (clause_001 phrase l.6 "must be defined in universal semantic glossary")
**Depends on:** `Golden Language`
**Notes:** requires-with-no-provider. FACT — CHANGELOG l.112 identifies the "universal semantic glossary" with `tree_of_life/golden_glossary.md` (six prose terms); the transcompiler's "glossary" (`streams/glossary/core_phrases.tau`, `transcompiler/index/glossary.json`) is phrase→predicate. In open-terms.

### agent_stream
**Kind:** concept
**Class:** declared (requires only)
**Defined in:** — (`streams/amendments/babel_antipattern_principle.tau:l.40`)
**the author's definition:**
>   requires: [universal_glossary, agent_stream, amendment_protocol] — `streams/amendments/babel_antipattern_principle.tau:l.40`
**Depends on:** `identity`
**Notes:** requires-with-no-provider; INFERENCE — the prose uses "agent stream" for `agents/seed/*.tau`. In open-terms.

### amendment_protocol
**Kind:** concept
**Class:** declared (requires only)
**Defined in:** — (`streams/amendments/babel_antipattern_principle.tau:l.40`)
**the author's definition:**
>   requires: [universal_glossary, agent_stream, amendment_protocol] — `streams/amendments/babel_antipattern_principle.tau:l.40`
**Also appears in:** `CONTRIBUTING.md` (l.11-15 "Propose Amendments"); `LICENSE` (l.21 "The amendment procedures defined in `update_process.tau`")
**Depends on:** `update_process`
**Notes:** requires-with-no-provider; INFERENCE — `update_process` is the closest provider. In open-terms.

---

## 6. Civic and policy streams (`streams/civic/`, `streams/policy/`, Family A)

### school_reform / energy_subsidy (announced civic streams)
**Kind:** stream
**Class:** announced
**Defined in:** `streams/civic/README.md` (l.39-43)
**the author's definition:**
> ## 🧠 Future Extensions
>
> - `streams/civic/<town>/school_reform.tau`
> - `streams/civic/<region>/energy_subsidy.tau`
> - Agent identity groups (NGOs, DAO-funded councils) — `streams/civic/README.md:l.39-43`
**Also appears in:** `streams/README.md` (l.31 example `[STREAM] energy/solar_microgrid.tau — the example town hybrid grid logic`)
**Depends on:** `civic_priority`, `semantic namespace`
**Notes:** FACT — none exists. "Agent identity groups (NGOs, DAO-funded councils)" is the repo's only mention of a DAO; the room template's `dao/` is not derived from it.

### Civic workflow (Proposal → Queue → Threshold → Allocation)
**Kind:** concept
**Class:** prose-term
**Defined in:** `streams/civic/README.md` (l.9-25)
**the author's definition:**
> 1. **Policy Proposal**
>    - Example: `sewage_priority.tau`
>    - A civic priority stream emits a public request (with justification)
>
> 2. **Queue Review**
>    - Example: `pending_priorities.tau`
>    - Community members and agents issue endorsements, forming an ordered priority queue
>
> 3. **Threshold Trigger**
>    - When a proposal passes the required quorum, it enters the `budget_allocation` stream
>
> 4. **Allocation + Reward**
>    - Proposal receives budget approval
>    - AGRS rewards distributed to contributors, validators, and endorsers
>    - Jurisdictional fund is updated — `streams/civic/README.md:l.11-25`
**Depends on:** `sewage_priority`, `pending_priorities`, `budget_allocation`, `agrs_reward`, `jurisdictional_fund`, `allocation_threshold`

---

## 7. Economy (`economy/`)

### agrs
**Kind:** concept
**Class:** declared
**Defined in:** `economy/agrs_policy.tau` (clause_001, l.15-18); `economy/README.md` (l.5)
**the author's definition:**
> define "agrs" as:
>     the native incentive token of the Tau Network,
>     representing value alignment and semantic contribution. — `economy/agrs_policy.tau:l.16-18`

> AGRS is the native token used to reward:
>
> - ✅ Verified semantic contributions
> - ✅ Constitutional execution
> - ✅ Civic participation
> - ✅ Clause authorship and amendment drafting — `economy/README.md:l.5-10`
**Depends on:** `semantic_contribution`
**Notes:** FACT — the repo never expands "AGRS" or relates it to any external token; the brief lists "Agoras" pages on tau.net as IDNI material (§2b), which is outside this pass.

### semantic_contribution
**Kind:** concept
**Class:** declared
**Defined in:** `economy/agrs_policy.tau` (clause_003, l.25-30)
**the author's definition:**
> define "semantic_contribution" as:
>     any clause, stream, or amendment that:
>     (a) aligns with constitutional logic,
>     (b) passes semantic validation, and
>     (c) enters the network manifest. — `economy/agrs_policy.tau:l.26-30`
**Also appears in:** `economy/agrs_policy.tau` (clause_006 l.44; provides); `economy/README.md` (l.7)
**Depends on:** `constitutional_inheritance`, `bootstrap_manifest`, `clause`
**Notes:** "semantic validation" and "the network manifest" are named, not defined; in open-terms.

### constitutional_execution
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `economy/agrs_policy.tau:l.10`; used clause_006 l.45; never defined; not provided)
**the author's definition:**
>     and it serves civic_participation or constitutional_execution — `economy/agrs_policy.tau:l.45`
**Also appears in:** `economy/README.md` (l.8 "Constitutional execution")
**Depends on:** —
**Notes:** in open-terms.

### civic_participation
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `economy/agrs_policy.tau:l.11`; used clause_006 l.45; never defined; not provided)
**the author's definition:**
>     and it serves civic_participation or constitutional_execution — `economy/agrs_policy.tau:l.45`
**Also appears in:** `economy/README.md` (l.9); `README.md` (l.20 "civic participation")
**Depends on:** —
**Notes:** in open-terms.

### traceable_reward
**Kind:** concept
**Class:** declared
**Defined in:** `economy/agrs_policy.tau` (clause_004, l.32-35)
**the author's definition:**
> define "traceable_reward" as:
>     an AGRS reward issued to a declared identity
>     with proof of authorship and alignment. — `economy/agrs_policy.tau:l.33-35`
**Also appears in:** `economy/agrs_policy.tau` (clause_006 l.49; provides); `economy/README.md` (l.24 "**Traceable** via `identity_trace`")
**Depends on:** `agrs_reward`, `identity`, `identity_trace`

### value_distribution_criteria
**Kind:** concept
**Class:** declared
**Defined in:** `economy/agrs_policy.tau` (clause_005, l.37-40)
**the author's definition:**
> define "value_distribution_criteria" as:
>     the logic by which AGRS is proportionally allocated
>     based on contribution type, trace weight, and network consensus. — `economy/agrs_policy.tau:l.38-40`
**Also appears in:** `economy/agrs_policy.tau` (provides); `economy/README.md` (l.25 "**Justified** via `value_distribution_criteria`")
**Depends on:** `agrs`, `identity_trace`, `semantic_consensus`
**Notes:** FACT — "trace weight" is the second repo occurrence of "weight" (with `amendment_quorum`'s "number or weight of identity_traces"). Undefined; in open-terms.

### agrs_policy
**Kind:** stream
**Class:** stream-id
**Defined in:** `economy/agrs_policy.tau` (l.1-5)
**the author's definition:**
> # Title: AGRS Policy — Incentive Logic for Semantic Contribution and Execution
> # Stream: economy.agrs_policy — `economy/agrs_policy.tau:l.2-3`

> - `agrs_policy.tau`: Foundational rules for issuing AGRS for lawful contributions. — `economy/README.md:l.20`
**Also appears in:** `streams/README.md` (l.26); `README.md` (l.93); `testnet/tau_stream_index.json` (l.24, under `tools`)
**Depends on:** `identity_trace`, `stream_registry`, `consensus_threshold`, `agrs`, `agrs_reward`, `semantic_contribution`, `traceable_reward`, `value_distribution_criteria`

### governance_allocation / public_goods_index / agent_staking
**Kind:** stream
**Class:** announced
**Defined in:** `economy/README.md` (l.30-32)
**the author's definition:**
> - `governance_allocation.tau`: AGRS for amendment work or dispute resolution
> - `public_goods_index.tau`: Civic benefit scoring for stream funding
> - `agent_staking.tau`: Risk-weighted commitment for semantic validators — `economy/README.md:l.30-32`
**Also appears in:** —
**Depends on:** `agrs`
**Notes:** FACT — none exists. "semantic validators" (l.32) is also used nowhere else; in open-terms.

---

## 8. Glossary, dev, and test streams (`streams/glossary/`, `streams/dev/`, `streams/transcompiler-tests/`, `transcompiler/sample_conversions.tau`)

### phrase_mapping
**Kind:** concept
**Class:** declared
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_001, l.11-14); declared also in `streams/glossary/core_phrases.tau` (l.6)
**the author's definition:**
> define "phrase_mapping" as:
>     a declarative entry that links a human-readable phrase
>     to a machine-readable predicate for logic compilation. — `streams/dev/predicate_phrases.tau:l.12-14`
**Also appears in:** `streams/dev/predicate_phrases.tau` (provides l.55; used as block keyword `phrase_mapping:` in clause_005–008); `streams/glossary/core_phrases.tau` (declared l.6; block keyword in clause_100–115); `transcompiler/README.md` (l.66 "Auto-index phrase → predicate mappings")
**Depends on:** `predicate_alias`
**Notes:** `predicate_phrases.tau` still declares `stream: streams.glossary.predicate_phrases` (l.1) although it lives in `dev/`.

### semantic_relation
**Kind:** concept
**Class:** declared
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_002, l.16-19)
**the author's definition:**
> define "semantic_relation" as:
>     a phrase mapping that expresses a state or condition
>     to be treated as a logical predicate. — `streams/dev/predicate_phrases.tau:l.17-19`
**Also appears in:** `streams/dev/predicate_phrases.tau` (as `type: semantic_relation` in clause_005/006/008; provides)
**Depends on:** `phrase_mapping`

### logic_pattern
**Kind:** concept
**Class:** declared
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_003, l.21-24)
**the author's definition:**
> define "logic_pattern" as:
>     a phrase mapping that conveys a logical operation
>     or relation between components in a clause. — `streams/dev/predicate_phrases.tau:l.22-24`
**Also appears in:** `streams/dev/predicate_phrases.tau` (`type: logic_pattern` in clause_007; provides)
**Depends on:** `phrase_mapping`

### predicate_alias
**Kind:** concept
**Class:** declared
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_004, l.26-28); declared in `streams/glossary/core_phrases.tau` (l.7)
**the author's definition:**
> define "predicate_alias" as:
>     a normalized predicate representation used during transcompilation. — `streams/dev/predicate_phrases.tau:l.27-28`
**Also appears in:** `streams/dev/predicate_phrases.tau` (provides); field `alias:` in every `phrase_mapping:` block of both glossary files
**Depends on:** —

### aligns_with_defined_concepts
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_006, l.36-40)
**the author's definition:**
>   phrase_mapping:
>     phrase: "aligns with defined concepts"
>     alias: "aligns_with_defined_concepts"
>     type: semantic_relation — `streams/dev/predicate_phrases.tau:l.37-40`
**Also appears in:** —
**Depends on:** `defined_concepts`
**Conflict:** see `defined_concepts` — the same idea maps to two predicate names in two glossary files.

### not contradiction
**Kind:** predicate
**Class:** phrase-predicate (logic_pattern)
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_007, l.42-46)
**the author's definition:**
>   phrase_mapping:
>     phrase: "does not contradict"
>     alias: "not contradiction"
>     type: logic_pattern — `streams/dev/predicate_phrases.tau:l.43-46`
**Also appears in:** —
**Depends on:** `does_not_contradict_prior_reasoning`, `contradiction_detection`
**Notes:** the only alias containing a space and an operator; the only `logic_pattern`-typed mapping.

### introduce_terms
**Kind:** predicate
**Class:** phrase-predicate
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_008, l.48-52)
**the author's definition:**
>   phrase_mapping:
>     phrase: "introduce terms"
>     alias: "introduce_terms"
>     type: semantic_relation — `streams/dev/predicate_phrases.tau:l.49-52`
**Also appears in:** —
**Depends on:** `semantic_containment`
**Notes:** INFERENCE — corresponds to `valid_thought`'s Family-A "no thought may introduce terms outside its declared… interface" (`git:1d70d83:…:l.36-37`); the live predicate is `does_not_leak_terms`.

### predicate_phrases
**Kind:** stream
**Class:** stream-id
**Defined in:** `streams/dev/predicate_phrases.tau` (l.1-4)
**the author's definition:**
> stream: streams.glossary.predicate_phrases
>
> title: Controlled Semantic Phrases
> description: Maps expressive human phrases to structured predicates for TML generation. — `streams/dev/predicate_phrases.tau:l.1-4`
**Also appears in:** `streams/README.md` (l.70, linked under `glossary/`); `CHANGELOG.md` (l.27 "reflexive stream for phrase-to-predicate logic")
**Depends on:** `phrase_mapping`, `semantic_relation`, `logic_pattern`, `predicate_alias`, `TML`

### core_phrases
**Kind:** stream
**Class:** stream-id
**Defined in:** `streams/glossary/core_phrases.tau` (l.1-4)
**the author's definition:**
> stream: streams.glossary.core_phrases
>
> title: Starter Glossary for Tau Compilation
> description: Provides initial phrase → predicate mappings for deterministic compilation. — `streams/glossary/core_phrases.tau:l.1-4`
**Also appears in:** —
**Depends on:** `phrase_mapping`, `predicate_alias`, `valid_thought`
**Notes:** FACT — no `meta:`/`interface:`; sole input of `tools/generate_phrase_index.py`.

### alpha
**Kind:** concept
**Class:** toy
**Defined in:** `streams/dev/example_logic.tau` (clause_001, l.7-8)
**the author's definition:**
> define "alpha" as: beta and not gamma. — `streams/dev/example_logic.tau:l.8`
**Also appears in:** `streams/dev/example_logic.tml` (l.2 `alpha() :- beta, not gamma.`)
**Depends on:** `beta`, `gamma`

### beta
**Kind:** concept
**Class:** toy
**Defined in:** — (declared `streams/dev/example_logic.tau:l.4`; required l.12)
**the author's definition:**
> declare concept "beta". — `streams/dev/example_logic.tau:l.4`
**Also appears in:** `streams/dev/example_logic.tml` (l.2)
**Depends on:** —

### gamma
**Kind:** concept
**Class:** toy
**Defined in:** — (declared `streams/dev/example_logic.tau:l.5`; required l.12)
**the author's definition:**
> declare concept "gamma". — `streams/dev/example_logic.tau:l.5`
**Also appears in:** `streams/dev/example_logic.tml` (l.2)
**Depends on:** —

### light
**Kind:** concept
**Class:** toy
**Defined in:** `streams/transcompiler-tests/sample_case.tau` (clause_001, l.6-7); `streams/transcompiler-tests/assertions/sample_case.tau` (clause_001, l.6-7)
**the author's definition:**
> define "light" as: not shadow. — `streams/transcompiler-tests/sample_case.tau:l.7`
**Also appears in:** `streams/transcompiler-tests/assertions/sample_case.expected.tml` (l.2 `light() :- not shadow.`); `streams/transcompiler-tests/sample_case.tml`; `streams/transcompiler-tests/assertions/sample_case.tml`
**Depends on:** `shadow`

### shadow
**Kind:** concept
**Class:** toy
**Defined in:** — (declared `streams/transcompiler-tests/sample_case.tau:l.4`; required l.10)
**the author's definition:**
> declare concept "shadow". — `streams/transcompiler-tests/sample_case.tau:l.4`
**Also appears in:** `streams/transcompiler-tests/assertions/sample_case.tau` (l.4, l.10)
**Depends on:** —

### example_input
**Kind:** concept
**Class:** toy
**Defined in:** `transcompiler/sample_conversions.tau` (clause_001, l.7-9)
**the author's definition:**
> define "example_input" as:
>     condition_a and not condition_b implies conclusion_c. — `transcompiler/sample_conversions.tau:l.8-9`
**Also appears in:** `transcompiler/sample_conversions.tau` (provides l.16)
**Depends on:** `condition_a`, `condition_b`, `conclusion_c`, `implies`

### example_output
**Kind:** concept
**Class:** toy
**Defined in:** `transcompiler/sample_conversions.tau` (clause_002, l.11-13)
**the author's definition:**
> define "example_output" as:
>     tml_rule::"conclusion_c() :- condition_a(), not condition_b()." — `transcompiler/sample_conversions.tau:l.12-13`
**Also appears in:** `transcompiler/sample_conversions.tau` (provides l.16)
**Depends on:** `tml_rule`, `example_input`
**Notes:** the one place a `.tau` embeds TML text as a literal.

### condition_a / condition_b / conclusion_c
**Kind:** concept
**Class:** toy
**Defined in:** — (used `transcompiler/sample_conversions.tau:l.9,13`; never declared)
**the author's definition:**
>     condition_a and not condition_b implies conclusion_c. — `transcompiler/sample_conversions.tau:l.9`
**Also appears in:** —
**Depends on:** —
**Notes:** used without `declare concept`, unlike every other toy.

---

## 9. Testnet and tools (`testnet/`, `tools/validate_tau.tau`)

### tau_testnet_bootstrap
**Kind:** stream
**Class:** stream-id
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (l.1-5)
**the author's definition:**
> # Title: Tau Testnet Bootstrap — Genesis Activation and Manifest Binding
> # Stream: tau.network.bootstrap.testnet — `testnet/tau_testnet_bootstrap.tau:l.2-3`

> - **tau_testnet_bootstrap.tau**: Declares `tau_manifest.json` as the canonical record of constitutional and amendment streams.
> - Launches the semantic execution scope for the Tau Network Testnet. — `testnet/README.md:l.25-26`
**Also appears in:** `constitution/map.md` (l.25 `testnet_bootstrap`); `README.md` (l.108 boot command); `testnet/README.md` (l.54); `docs/purpose_of_tau.md` (l.33); `docs/theory_of_change.md` (l.58); `CHANGELOG.md` (l.178)
**Depends on:** `genesis_stream`, `identity_trace`, `tau_manifest.json`, `bootstrap_manifest`, `genesis_reference`, `testnet_declaration`, `stream_integrity_commitment`, `network_activation`

### bootstrap_manifest
**Kind:** concept
**Class:** declared
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (clause_001, l.13-16)
**the author's definition:**
> define "bootstrap_manifest" as:
>     the pointer to the canonical tau_manifest.json
>     containing hashed semantic streams to initialize the testnet. — `testnet/tau_testnet_bootstrap.tau:l.14-16`
**Also appears in:** `testnet/tau_testnet_bootstrap.tau` (clause_005 l.35; provides l.47/51)
**Depends on:** `tau_manifest.json`

### tau_manifest.json
**Kind:** concept
**Class:** declared (requires only; a filename)
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (requires l.48/52); `testnet/README.md` (l.34)
**the author's definition:**
>     requires: [genesis_stream, identity_trace, tau_manifest.json] — `testnet/tau_testnet_bootstrap.tau:l.48`

> - **tau_manifest.json**: Signed SHA-256 hash manifest of every logic stream. — `testnet/README.md:l.34`
**Also appears in:** `testnet/tau_manifest.json` (the file: 14 entries all `"hash": null, "error": "file not found"`); `README.md` (l.108); `CONTRIBUTING.md` (l.39); `docs/purpose_of_tau.md` (l.34); `CHANGELOG.md` (l.179)
**Depends on:** `stream_version`
**Notes:** requires-with-no-provider (INVENTORY §4): the only `requires` entry that is a filename. "Signed" — no signature mechanism exists in the tree. In open-terms.

### genesis_reference
**Kind:** concept
**Class:** declared
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (clause_002, l.18-21)
**the author's definition:**
> define "genesis_reference" as:
>     a required confirmation that the network derives from autopoietic_logos
>     and includes its six constitutional pillars and amendments. — `testnet/tau_testnet_bootstrap.tau:l.19-21`
**Also appears in:** `testnet/tau_testnet_bootstrap.tau` (clause_005 l.36; declared l.8; **not** provided l.47/51)
**Depends on:** `autopoietic_logos`, `six constitutional pillars`

### six constitutional pillars
**Kind:** concept
**Class:** prose-term
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (l.21); `README.md` (l.13); `docs/theory_of_change.md` (l.55)
**the author's definition:**
>     and includes its six constitutional pillars and amendments. — `testnet/tau_testnet_bootstrap.tau:l.21`

> - ✅ The **Tau Constitution** (6 streams) — `README.md:l.13`

> - A complete 6-part constitutional framework — `docs/theory_of_change.md:l.55`
**Also appears in:** `testnet/tau_stream_index.json` (l.2-9: `genesis` + 5 `constitution`); `testnet/README.md` (l.7-15)
**Depends on:** `autopoietic_logos`, `identity_core`, `update_process`, `rights_and_agency`, `consensus_logic`, `tau_network`
**Notes:** INFERENCE — the six are the six `constitution/*.tau` streams; `tau_stream_index.json` separates `autopoietic_logos` as `genesis` from the other five as `constitution`.

### testnet_declaration
**Kind:** concept
**Class:** declared
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (clause_003, l.23-26)
**the author's definition:**
> define "testnet_declaration" as:
>     the semantic commitment to launch a provisional logic network
>     for testing, refinement, and stream validation. — `testnet/tau_testnet_bootstrap.tau:l.24-26`
**Also appears in:** `testnet/tau_testnet_bootstrap.tau` (provides)
**Depends on:** `stream_execution_scope`

### stream_integrity_commitment
**Kind:** concept
**Class:** declared
**Defined in:** `testnet/tau_testnet_bootstrap.tau` (clause_004, l.28-31)
**the author's definition:**
> define "stream_integrity_commitment" as:
>     the binding of every stream hash to its identity_trace,
>     ensuring that all logic is auditable and properly attributed. — `testnet/tau_testnet_bootstrap.tau:l.29-31`
**Also appears in:** `testnet/tau_testnet_bootstrap.tau` (declared l.10; not provided)
**Depends on:** `identity_trace`, `stream_version`

### network_activation
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `testnet/tau_testnet_bootstrap.tau:l.11`; used clause_005 l.39; provided l.47/51; never defined)
**the author's definition:**
>     network_activation is permitted
>     and all agents may begin reasoning and participation under the Tau testnet charter. — `testnet/tau_testnet_bootstrap.tau:l.39-40`
**Also appears in:** `constitution/map.md` (l.3 "testnet activation")
**Depends on:** `bootstrap_manifest`, `genesis_reference`, `Tau testnet charter`
**Notes:** in open-terms.

### Tau testnet charter
**Kind:** concept
**Class:** prose-term
**Defined in:** — (used `testnet/tau_testnet_bootstrap.tau:l.40`)
**the author's definition:**
>     and all agents may begin reasoning and participation under the Tau testnet charter. — `testnet/tau_testnet_bootstrap.tau:l.40`
**Also appears in:** —
**Depends on:** —
**Notes:** in open-terms.

### tau_stream_index.json
**Kind:** concept
**Class:** config
**Defined in:** `testnet/tau_stream_index.json` (l.1-26); `testnet/README.md` (l.32)
**the author's definition:**
> - **tau_stream_index.json**: Lists all files, paths, and roles. — `testnet/README.md:l.32`
**Also appears in:** `README.md` (l.100); `tools/tau_publish.py`; `CHANGELOG.md` (l.180)
**Depends on:** `stream_registry`
**Notes:** keys `genesis`, `constitution`, `amendments`, `meta{map,lock,index,epilogue}`, `docs`, `tools`. FACT — `economy/agrs_policy.tau` is listed under `tools` (l.24).

### Testnet principles (Lawfulness of change / Trustless traceability / Reflexive agency / Self-amendment / Preservation of Being)
**Kind:** concept
**Class:** prose-term
**Defined in:** `testnet/README.md` (l.41-46)
**the author's definition:**
> All logic streams derive from the Autopoietic Logos and obey:
> - Lawfulness of change
> - Trustless traceability
> - Reflexive agency
> - Self-amendment
> - Preservation of Being — `testnet/README.md:l.41-46`
**Also appears in:** —
**Depends on:** `lawfulness`, `trustless_coherence`, `agency`, `self_amendment`, `alignment_with_being`
**Notes:** INFERENCE — five principles mapped to five constitution concepts by name resemblance only.

### Tau Testnet Genesis Release
**Kind:** concept
**Class:** prose-term
**Defined in:** `testnet/README.md` (l.1-3)
**the author's definition:**
> # Tau Testnet Genesis Release
>
> This repository contains the full semantic scaffold for bootstrapping the Tau Network Testnet — a self-evolving constitution, agent model, and amendment ledger grounded in the principles of the Autopoietic Logos. — `testnet/README.md:l.1-3`
**Also appears in:** `CHANGELOG.md` (l.159 "[v0.1.1-testnet]")
**Depends on:** `tau_testnet_bootstrap`, `autopoietic_logos`, `six constitutional pillars`
**Notes:** FACT — "amendment ledger" here is the third repo use of "ledger" (with `contribution_record` and the room template's Affirming ledger); it is not defined.

### Epoch of Self-Amending Reality
**Kind:** concept
**Class:** prose-term
**Defined in:** `testnet/README.md` (l.59)
**the author's definition:**
> This initiates the Tau Net — not as a system of static truth, but as a rhythm of lawful emergence.
>
> Welcome to the Epoch of Self-Amending Reality. — `testnet/README.md:l.57-59`
**Also appears in:** —
**Depends on:** `self_amendment`

### validate_tau
**Kind:** stream
**Class:** stream-id (Family D)
**Defined in:** `tools/validate_tau.tau` (l.1-3)
**the author's definition:**
> # validate_tau.tau — logic-native validator
>
> stream: streams.tools.validate_tau — `tools/validate_tau.tau:l.1-3`
**Also appears in:** `README.md` (l.34); `CONTRIBUTING.md` (l.36); `docs/index.md` (l.37); `testnet/tau_stream_index.json` (l.23); `testnet/tau_manifest.json` (l.54, as `streams/tools/validate_tau.tau`); `CHANGELOG.md` (l.176)
**Depends on:** `tau_file`, `clause`, `concept_declaration`, `provides_declaration`, `requires_declaration`, `validation_warning`
**Notes:** the only Family-D file; its rules are imperative prose ("every tau_file must contain…", "emit …"). No `meta`/`interface`.

### tau_file
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `tools/validate_tau.tau:l.5`; used l.13, l.18)
**the author's definition:**
>   every tau_file must contain a concept_declaration. — `tools/validate_tau.tau:l.13`
**Also appears in:** —
**Depends on:** `concept_declaration`, `clause`

### clause
**Kind:** concept
**Class:** declared / notation
**Defined in:** — (declared `tools/validate_tau.tau:l.6`; described in `transcompiler/stream_format.md:l.3-7`; `transcompiler/tau_syntax.ebnf:l.4-5`; used everywhere as `clause_NNN vX.Y.Z:`)
**the author's definition:**
>   every tau_file must contain at least one clause identifier. — `tools/validate_tau.tau:l.18`

> Each clause must include:
>
> - `stream_name`: the logical head predicate
> - `description`: human-readable purpose of the clause
> - `phrase_predicates`: declared mappings from phrase → predicate — `transcompiler/stream_format.md:l.3-7`

> clause_block ::= "clause_" number version? ":" clause_body
> clause_body  ::= "define" string "as:" logic_expr — `transcompiler/tau_syntax.ebnf:l.4-5`

> - Use `clause_### vX.Y.Z` format (e.g. clause_003 v0.1.0)
> - Each clause must be uniquely indexed within a stream. — `docs/naming_conventions.md:l.15-16`
**Also appears in:** `constitution/update_process.tau` (l.21 "clause or clause set", l.32); `constitution/identity_core.tau` (l.31); `manifesto/chapter_03-…` (l.20 "stream of clauses"); `streams/README.md` (l.85 "Each `.tau` stream is a **living clause**"); `transcompiler/spec.md` (l.9, l.34)
**Depends on:** —
**Conflict:** three different clause shapes are prescribed: `stream_format.md` (v3: `stream_name`/`description`/`phrase_predicates`), `tau_syntax.ebnf` (Family C: `define string as: logic_expr`), and the Family-A practice (`define … as:` prose or `if (…) then (…)`). See `docs/INVENTORY.md` §1.

### concept_declaration
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `tools/validate_tau.tau:l.7`; used l.13)
**the author's definition:**
>   every tau_file must contain a concept_declaration.
>   if missing:
>     emit validation_warning::"Missing concept declaration". — `tools/validate_tau.tau:l.13-15`
**Also appears in:** every `declare concept "…"` line in Family-A/C files
**Depends on:** `declare concept`

### provides_declaration
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `tools/validate_tau.tau:l.8`; clause_004 l.28 "if provides or requires is missing in interface")
**the author's definition:**
>   if provides or requires is missing in interface:
>     emit validation_warning::"Missing stream dependency metadata". — `tools/validate_tau.tau:l.28-29`
**Also appears in:** —
**Depends on:** `provides`, `interface`

### requires_declaration
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `tools/validate_tau.tau:l.9`; clause_004 l.28)
**the author's definition:**
>   if provides or requires is missing in interface: — `tools/validate_tau.tau:l.28`
**Also appears in:** —
**Depends on:** `requires`, `interface`

### validation_warning
**Kind:** concept
**Class:** declared
**Defined in:** — (declared `tools/validate_tau.tau:l.10`; emitted l.15, 20, 25, 29 with four string payloads)
**the author's definition:**
>     emit validation_warning::"Missing concept declaration". — `tools/validate_tau.tau:l.15`
>     emit validation_warning::"No clauses found in stream". — `tools/validate_tau.tau:l.20`
>     emit validation_warning::"Duplicate clause ID found". — `tools/validate_tau.tau:l.25`
>     emit validation_warning::"Missing stream dependency metadata". — `tools/validate_tau.tau:l.29`
**Also appears in:** —
**Depends on:** `emit`
**Notes:** `emit` is also used in `pending_priorities.tau:l.45` ("proposal_pipeline_entry is emitted"), amendment 001 ("emit semantic expression"), and endorsement streams ("emitted by"). What emission is, is not defined; in open-terms.

---

## 10. Prose vocabulary (`docs/`, `README.md`, `CONTRIBUTING.md`, `LICENSE`, `CHANGELOG.md`, `tower_of_babel/`, `tree_of_life/`, `transcompiler/*.md`)

### Tau Network / TauNet / Tau Net
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/purpose_of_tau.md` (l.3-10); `docs/index.md` (l.7); `README.md` (l.5)
**the author's definition:**
> Tau Network exists to solve humanity’s most complex problems by aligning language, logic, and consensus into a living, executable medium.
>
> ## Tau is:
>
> - A platform that turns **knowledge into action**
> - A semantic space where **software, law, and policy evolve in real-time**
> - A substrate for **human and machine co-intelligence**
> - A constitutional network built on **recursive agency and lawful emergence** — `docs/purpose_of_tau.md:l.3-10`

> Tau Genesis is the constitutional heart of the Tau Network — a system where agents, amendments, and civic policies are expressed as self-amending logic streams. — `docs/index.md:l.7`
**Also appears in:** `economy/agrs_policy.tau` (l.17 "the Tau Network"); `agents/seed/neemrad.tau` (l.21 "the Tau Testnet"); `streams/core/README.md` (l.1 "TauNet"); `testnet/README.md` (l.57 "the Tau Net"); `git:c55ce7c~1:amendments/amendment_001_…` (l.2 "the Tau Net"); `CHANGELOG.md` (l.37 "TauNet’s"); `streams/README.md` (l.92, l.97)
**Depends on:** `autopoietic_logos`
**Notes:** FACT — spelled "Tau Network", "TauNet", "Tau Net" and "Tau" in different files; the repo never distinguishes its own "Tau Network" from IDNI's. That question belongs to Phase 2 and is out of scope here.

### tau-genesis (this repository)
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/purpose_of_tau.md` (l.16); `README.md` (l.5); `CONTRIBUTING.md` (l.3)
**the author's definition:**
> This repository — `tau-genesis` — serves as the **semantic origin** of the Tau Network. — `docs/purpose_of_tau.md:l.16`

> Welcome to the **semantic source code of the Tau Network** — a self-amending, self-coherent universe of logic streams rooted in the *Autopoietic Logos* and guided by recursive law, agent traceability, and collective evolution. — `README.md:l.5`

> This repository is the constitutional root of the Tau Network — a lawful, logic-based ecosystem built on recursive agency and self-amending streams. — `CONTRIBUTING.md:l.3`
**Also appears in:** `docs/theory_of_change.md` (l.52 "This is the **Tau Genesis Repo**"); `testnet/README.md` (l.3)
**Depends on:** `Tau Network / TauNet / Tau Net`, `autopoietic_logos`

### semantic nervous system
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/purpose_of_tau.md` (l.43-47)
**the author's definition:**
> It is a **semantic nervous system for evolving minds**:
> - Governed by `autopoietic_logos`
> - Protected by traceable agency
> - Changeable by its participants
> - Rooted in Being, not bureaucracy — `docs/purpose_of_tau.md:l.43-47`
**Also appears in:** `streams/core/README.md` (l.20 "the **nerve tissue of emergence**"); `transcompiler/README.md` (l.26 "its **semantic circulation**")
**Depends on:** `autopoietic_logos`

### lawful substrate
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/theory_of_change.md` (l.64-68)
**the author's definition:**
> We don’t change systems by replacing them.  
> We change systems by **streaming a lawful substrate beneath them.**
>
> Tau is that substrate.  
> This repo is the root. — `docs/theory_of_change.md:l.64-68`
**Also appears in:** `README.md` (l.151 "Tau is the substrate."); `CHANGELOG.md` (l.34 "TauNet’s lawful substrate"); `streams/README.md` (l.92 "reflexive legislative substrate"); `docs/purpose_of_tau.md` (l.9 "A substrate for…"); `constitution/autopoietic_logos.tau` (l.41 "semantic substrate")
**Depends on:** `lawfulness`, `genesis_stream`

### Semantic Precision / Modular Knowledge / Self-Amendment / Collective Intelligence / Truth with Consent
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/theory_of_change.md` (l.23-36)
**the author's definition:**
> ### 1. Semantic Precision
> All communication becomes computable, traceable, and evolvable — without losing its human meaning.
>
> ### 2. Modular Knowledge
> Every law, policy, belief, or algorithm becomes a versioned, forkable logic stream — visible and verifiable by all.
>
> ### 3. Self-Amendment
> The system governs its own transformation through lawful update logic — `update_process.tau`.
>
> ### 4. Collective Intelligence
> Humans and machines reason together through semantic consensus and contradiction resolution.
>
> ### 5. Truth with Consent
> Every truth is traceable, and every transformation requires declared alignment — `consensus_logic.tau`. — `docs/theory_of_change.md:l.23-36`
**Also appears in:** —
**Depends on:** `logic_stream`, `update_process`, `semantic_consensus`, `contradiction_detection`, `consensus_logic`, `semantic_consent`

### post-representational democracy
**Kind:** concept
**Class:** prose-term
**Defined in:** `docs/index.md` (l.11)
**the author's definition:**
> From the manifesto to the testnet, from agents to amendments, everything here flows with traceable coherence, lawful recursion, and post-representational democracy. — `docs/index.md:l.11`
**Also appears in:** `CHANGELOG.md` (l.125 "Models how governance evolves through thematic logic — not representatives")
**Depends on:** `semantic_governance`, `semantic_consent`
**Notes:** in open-terms.

### TauLang (TML) / TML / Tau Meta-Language
**Kind:** concept
**Class:** prose-term (a Tau/TML construct named by the proposal)
**Defined in:** `docs/index.md` (l.44); `transcompiler/spec.md` (l.3); `CHANGELOG.md` (l.93); `README.md` (l.37, l.141-143)
**the author's definition:**
> > - Transcompiler: `.tau` → TauLang (TML) — `docs/index.md:l.44`

> This guide outlines how the Tau transcompiler converts `.tau` logic streams into Boolean-valid Tau Meta-Language (TML). — `transcompiler/spec.md:l.3`

> - `tau_to_tml.py`: Emits Tau Meta-Language (TML) rules from structured ASTs — `CHANGELOG.md:l.93`

>     transcompiler/      → Compiler logic to transform .tau semantics into Boolean expressions for TauLang — `README.md:l.37`

>   It converts clause-based `.tau` streams into propositional logic and ultimately TML-compatible Boolean expressions. — `README.md:l.143`

> It transforms `.tau` — our lawful streams of intention — into Boolean logic compatible with TauLang (TML).  
> It makes meaning *executable*. — `transcompiler/README.md:l.32-33`
**Also appears in:** `streams/dev/predicate_phrases.tau` (l.4 "for TML generation"); every `.tml` file; `transcompiler/stream_format.md` (title "Tau Transcompiler v3"); `transcompiler/README.md` (l.48 "TauLang will not run the world by force. It will run logic *with memory* — memory of purpose, trace, version, consent.")
**Depends on:** `Transcompiler`
**Notes:** recorded as the proposal uses the names: "TauLang (TML)" and "Tau Meta-Language (TML)" as one thing, the target of the transcompiler, characterised as "Boolean-valid", "Horn clauses", "propositional logic". No IDNI source consulted (brief §2a). FACT — the `.tml` files in the tree are Horn clauses produced by string formatting (`docs/INVENTORY.md` §2).

### NSO
**Kind:** concept
**Class:** prose-term (a Tau/TML construct named by the proposal)
**Defined in:** `transcompiler/spec.md` (l.12, l.24, l.41)
**the author's definition:**
> 4. **NSO Handler**: (Planned) Enables `{clause}` references for meta-logical statements — `transcompiler/spec.md:l.12`

> | Clause reference   | Soon (NSO)      | — `transcompiler/spec.md:l.24`

> - NSO curly-brace `{...}` syntax support — `transcompiler/spec.md:l.41`
**Also appears in:** —
**Depends on:** `clause`, `TauLang (TML) / TML / Tau Meta-Language`
**Notes:** never expanded in the repo; in open-terms.

### Transcompiler
**Kind:** concept
**Class:** prose-term
**Defined in:** `transcompiler/README.md` (l.23-36); `transcompiler/spec.md` (l.7-12); `README.md` (l.139-145)
**the author's definition:**
> TauNet is a network of meaning.  
> The transcompiler is its **semantic circulation** — the bridge between:
>
> - 🧠 *Human expression*  
> - ⚙️ *Machine execution*  
> - 🧿 *Collective understanding*
>
> It transforms `.tau` — our lawful streams of intention — into Boolean logic compatible with TauLang (TML).  
> It makes meaning *executable*. — `transcompiler/README.md:l.25-33`

> 1. **Parser**: Reads `.tau` syntax (`declare`, `define`, `clause`, `interface`)
> 2. **Semantic Mapper**: Converts clause structures into logical trees
> 3. **TML Generator**: Emits Horn clauses and TML-compliant Boolean structures
> 4. **NSO Handler**: (Planned) Enables `{clause}` references for meta-logical statements — `transcompiler/spec.md:l.9-12`

> This module is Tau's answer to Babel — a semantic engine that restores coherence between language and law. — `README.md:l.145`

> # Tau Transcompiler — The Reconciliation of Tongues — `transcompiler/README.md:l.2`
**Also appears in:** `transcompiler/README.md` (l.42-43 "This is not a compiler. This is a remembering."; l.2 "The Reconciliation of Tongues"); `tower_of_babel/babel_patterns.md` (l.9 "**transcompiler** tools that make logic human-readable"); `CHANGELOG.md` (v0.1.8–v0.2.3 entries); `docs/index.md` (l.44); `streams/core/README.md` (l.18)
**Depends on:** `TauLang (TML) / TML / Tau Meta-Language`, `phrase_mapping`, `Golden Language`, `Tower of Babel`

### Stream coherence criteria
**Kind:** concept
**Class:** prose-term
**Defined in:** `transcompiler/spec.md` (l.28-34)
**the author's definition:**
> A `.tau` stream is semantically coherent if:
>
> - All `provides` concepts are declared
> - No circular dependencies in `requires`
> - Each `clause` is logically satisfiable (non-contradictory) — `transcompiler/spec.md:l.30-34`
**Also appears in:** `docs/naming_conventions.md` (l.6 "All declared `concept` terms should match exactly in `provides:` and `requires:` sections.")
**Depends on:** `provides`, `requires`, `declare concept`, `clause`
**Notes:** FACT — the third criterion ("logically satisfiable") is the repo's only use of "satisfiable".

### Coherence scoring (trace, structure, ethics)
**Kind:** concept
**Class:** prose-term
**Defined in:** `transcompiler/spec.md` (l.43)
**the author's definition:**
> - Coherence scoring (trace, structure, ethics) — `transcompiler/spec.md:l.43`
**Also appears in:** —
**Depends on:** `value_score`
**Notes:** TODO item; in open-terms.

### stream_name / description / phrase_predicates (v3 clause fields)
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/stream_format.md` (l.3-11)
**the author's definition:**
> Each clause must include:
>
> - `stream_name`: the logical head predicate
> - `description`: human-readable purpose of the clause
> - `phrase_predicates`: declared mappings from phrase → predicate
>
> A `meta:` block can also declare:
> - `provides`: list of logical streams this file outputs
> - `requires`: list of upstream dependencies — `transcompiler/stream_format.md:l.3-11`
**Also appears in:** all four Family-B files; `transcompiler/README.md` (l.65)
**Depends on:** `clause`, `predicate_alias`, `provides`, `requires`
**Notes:** FACT — in Family A, `stream_name` is a field of the `clause_999 meta:` block naming the *file*; in Family B it is per-clause and "the logical head predicate". Same keyword, two roles. Also: `provides` is glossed as "logical streams this file outputs" — i.e., in v3 the things provided are called streams, not concepts.

### Golden Language
**Kind:** concept
**Class:** glossary-term
**Defined in:** `tree_of_life/golden_glossary.md` (l.4); `tower_of_babel/nimrod_and_babel.md` (l.5); `transcompiler/README.md` (l.73-78)
**the author's definition:**
> **Golden Language** (Language of Gold) – The mythical primordial language of truth that humanity spoke before the confusion of Babel. Also known as the Edenic or Adamic language, it is said to perfectly express the essence of things (a “cosmic grammar” underlying nature). In Tau, the concept inspires the creation of a universal semantic framework – a shared formal language in which all agents can communicate without ambiguity. The **universal semantic glossary** is a step toward this ideal “golden” tongue. — `tree_of_life/golden_glossary.md:l.4`

> Tau aims to provide a modern *“golden language”* – not literally a single human language, but a universal semantic framework within which all contributions can be understood. — `tower_of_babel/nimrod_and_babel.md:l.5`

> It is a step toward Tau’s **Golden Language** — a system of meaning where agents may differ in style, but not in truth. — `transcompiler/README.md:l.78`
**Also appears in:** `git:c55ce7c~1:amendments/amendment_003_babel_antipattern.tau` (l.5 'the "golden language"'); `README.md` (l.38, l.63); `CHANGELOG.md` (l.112); `docs/assets/language_of_gold.png` (banner)
**Depends on:** `universal_glossary`, `Semantic Coherence (glossary)`
**Notes:** also named "Divine Solar Language", "language of gold", "Adamic", "Edenic", "Cosmic Grammar" (`tower_of_babel/nimrod_and_babel.md:l.5`).

### Tower of Babel
**Kind:** concept
**Class:** glossary-term
**Defined in:** `tree_of_life/golden_glossary.md` (l.6); `tower_of_babel/nimrod_and_babel.md` (l.3)
**the author's definition:**
> **Tower of Babel (Babel)** – In scripture, a tower built by early humanity in Shinar, which led to the confounding of their single language into many. Symbolically, “Babel” denotes chaotic multiplicity of languages and the breakdown of communication caused by prideful ambition. Within Tau, it represents a critical anti-pattern: any scenario where lack of semantic alignment or misguided centralized arrogance causes a collapse of understanding. “Avoiding Babel” is shorthand for maintaining semantic coherence across the network. — `tree_of_life/golden_glossary.md:l.6`
**Also appears in:** `tower_of_babel/babel_patterns.md` (whole file); `transcompiler/README.md` (l.4-8, l.35, l.75, l.80); `README.md` (l.39, l.145 "Tau's answer to Babel"); `tower_of_babel/nimrod_and_babel.md` (l.9 "Babel is essentially the **shadow** of the Tree of Life")
**Depends on:** `Nimrod`, `Babel anti-patterns`

### Nimrod
**Kind:** concept
**Class:** glossary-term
**Defined in:** `tree_of_life/golden_glossary.md` (l.8); `tower_of_babel/nimrod_and_babel.md` (l.3)
**the author's definition:**
> **Nimrod** – A biblical figure described as a “mighty hunter” and king who instigated the building of Babel. Esoterically, Nimrod embodies the rebellious intellect or ego that seeks power independently of divine or natural law (his name means “rebel”). In Tau’s lexicon, Nimrod serves as a cautionary archetype – reminding us that knowledge governance must be collaborative and humble. (Notably, an example agent identity `neemrad.tau` in the system nods to this symbolic role.) — `tree_of_life/golden_glossary.md:l.8`

> Kabbalistically, Nimrod personifies the unbridled *intellect* (the Sephirah **Netzach** on the Tree of Life), which seeks power on its own terms. — `tower_of_babel/nimrod_and_babel.md:l.3`
**Also appears in:** `tower_of_babel/nimrod_and_babel.md` (l.7 "a modern Nimrod"); `tower_of_babel/babel_patterns.md` (l.1, l.5); `transcompiler/README.md` (l.36 "Where Nimrod imposed, Tau aligns.")
**Depends on:** `Tower of Babel`, `Tree of Life`, `neemrad`

### Tree of Life
**Kind:** concept
**Class:** glossary-term
**Defined in:** `tree_of_life/golden_glossary.md` (l.10); `tower_of_babel/nimrod_and_babel.md` (l.9)
**the author's definition:**
> **Tree of Life** – The central diagram of Kabbalah, depicting the ten interconnected spheres (*sephiroth*) of existence from divine to material. It represents harmony, order, and the integration of all aspects of reality. Tau draws on the Tree of Life metaphor as a guide for its architecture: our network should mirror a **balanced, living system** of knowledge (each part in proper relation), as opposed to a Babel-like rigid tower. The Tree of Life symbolizes the *intended* sacred structure (unity in diversity) that Tau strives to embody. — `tree_of_life/golden_glossary.md:l.10`

> One might say Tau is **building a Tree of Life, not a Tower of Babel** — `tower_of_babel/nimrod_and_babel.md:l.9`
**Also appears in:** `README.md` (l.38 "tree_of_life/"); `CHANGELOG.md` (l.114)
**Depends on:** `autopoietic_logos`
**Notes:** `tower_of_babel/nimrod_and_babel.md:l.9` equates it with the Autopoietic Logos ("analogous to the **Tree of Life**").

### Semantic Coherence (glossary)
**Kind:** concept
**Class:** glossary-term
**Defined in:** `tree_of_life/golden_glossary.md` (l.12)
**the author's definition:**
> (quoted in full under `semantic_coherence`, §4) — `tree_of_life/golden_glossary.md:l.12`
**Also appears in:** see `semantic_coherence`
**Depends on:** `semantic_coherence`
**Notes:** alias entry; the definition and the conflict with the deleted `valid_block.tau` are recorded under `semantic_coherence`.

### will of the collective Logos
**Kind:** concept
**Class:** prose-term
**Defined in:** `tower_of_babel/nimrod_and_babel.md` (l.7)
**the author's definition:**
> Instead, every advancement in Tau is measured against collective coherence and aligned with what we might call the *will of the collective Logos* (the emergent wisdom of the group) rather than the will of a rebel king. — `tower_of_babel/nimrod_and_babel.md:l.7`
**Also appears in:** —
**Depends on:** `autopoietic_logos`, `semantic_consensus`

### Babel anti-patterns (Hubris Overreach / Semantic Schism / Monolithic Control / Heartless Intellect / Opaque Complexity / Fractured Unity)
**Kind:** concept
**Class:** prose-term
**Defined in:** `tower_of_babel/babel_patterns.md` (l.1-11)
**the author's definition:**
> 1. **Hubris Overreach** – Building systems or making decisions fueled by excessive pride, without regard for moral or natural limits. — `tower_of_babel/babel_patterns.md:l.1`
> 2. **Semantic Schism** – The breakdown of shared understanding due to inconsistent or conflicting language. — `tower_of_babel/babel_patterns.md:l.3`
> 3. **Monolithic Control** – A top-down, authoritarian approach to governance or semantics, where one entity dictates definitions or rules without an inclusive process. — `tower_of_babel/babel_patterns.md:l.5`
> 4. **Heartless Intellect** – Emphasizing logic and structure at the expense of empathy, emotional intelligence, or basic human needs. — `tower_of_babel/babel_patterns.md:l.7`
> 5. **Opaque Complexity** – Designing a system so complex or obscure that its own participants cannot understand it fully, leading to miscommunication and mistrust. — `tower_of_babel/babel_patterns.md:l.9`
> 6. **Fractured Unity** – The splintering of a community or effort into disjointed factions that no longer share a common purpose. — `tower_of_babel/babel_patterns.md:l.11`
**Also appears in:** `tower_of_babel/nimrod_and_babel.md` (l.11 "documentation of **Babel-like failure modes**"); `README.md` (l.39, l.64-65); `CHANGELOG.md` (l.113)
**Depends on:** `Tower of Babel`, `babel_antipattern_principle`, `universal_glossary`, `self_amendment`, `Transcompiler`
**Notes:** each pattern names its Tau remedy in the same paragraph (glossary, consensus, distributed power, civic ethics, transcompiler, self-amendment).

### Semantic principles for streams (Traceable / Lawful / Semantic / Reflexive)
**Kind:** concept
**Class:** prose-term
**Defined in:** `streams/README.md` (l.36-43)
**the author's definition:**
> All streams must be:
>
> - 🔍 **Traceable** — include agent and clause identity
> - ⚖️ **Lawful** — define stream interfaces and concept scope
> - 🧠 **Semantic** — use human-meaningful logic mapped to predicate language
> - ♻️ **Reflexive** — allow for amendment, alignment, and consensus emergence — `streams/README.md:l.38-43`
**Also appears in:** —
**Depends on:** `identity_trace`, `interface`, `phrase_mapping`, `self_amendment`

### semantic namespace
**Kind:** concept
**Class:** prose-term
**Defined in:** `streams/README.md` (l.4)
**the author's definition:**
> Each subfolder under `streams/` forms a **semantic namespace** where declarations evolve, agents participate, and logic aligns. — `streams/README.md:l.4`
**Also appears in:** `streams/README.md` (l.47-79: `core/`, `meta/`, `civic/`, `policy/`, `glossary/`, `transcompiler-tests/`, `dev/`; l.13-19 proposed `health/`, `energy/`, `education/`, `governance/`, `infrastructure/`, `environment/`)
**Depends on:** `stream_execution_scope`
**Notes:** INFERENCE — the dotted stream ids (`streams.civic.palomino.*`, `tau.constitution.*`, `harmonic-emergence.*`) are the namespace mechanism; the text says folders, the ids say dotted paths, and the two prefixes (`streams.` vs `tau.` vs `harmonic-emergence.`) are never related.

### living clause
**Kind:** concept
**Class:** prose-term
**Defined in:** `streams/README.md` (l.85)
**the author's definition:**
> Each `.tau` stream is a **living clause**, not a static document. — `streams/README.md:l.85`
**Also appears in:** `streams/core/README.md` (l.7 "neither mutable whims nor eternal axioms, but living roots")
**Depends on:** `clause`, `evolution`

### preconditions for lawful cognition
**Kind:** concept
**Class:** prose-term
**Defined in:** `streams/core/README.md` (l.3-7)
**the author's definition:**
> Streams in `core/` are not policies, preferences, or civic declarations — they are **preconditions** for lawful cognition, validation, and agency.
>
> They encode how a block is valid, how a thought is coherent, how a being is traceable.
>
> Every self-amending system must anchor itself in a minimal semantic core. — `streams/core/README.md:l.3-7`
**Also appears in:** —
**Depends on:** `valid_thought`, `valid_block`, `identity_trace`

### Contribution review criteria (Semantic validity / Stream lineage / Recursive integrity)
**Kind:** concept
**Class:** prose-term
**Defined in:** `CONTRIBUTING.md` (l.59-62)
**the author's definition:**
> All contributions are reviewed for:
> - Semantic validity
> - Stream lineage
> - Recursive integrity — `CONTRIBUTING.md:l.59-62`
**Also appears in:** `CHANGELOG.md` (l.17 "recursive integrity")
**Depends on:** `valid_thought`, `identity_trace`, `recursive_legitimacy`

### "No one speaks for the network; all speak into the network"
**Kind:** concept
**Class:** prose-term
**Defined in:** `CONTRIBUTING.md` (l.66-70)
**the author's definition:**
> - All logic must trace back to `autopoietic_logos`
> - All updates must declare their intent, effect, and coherence
> - No one speaks for the network; all speak *into* the network — `CONTRIBUTING.md:l.68-70`
**Also appears in:** —
**Depends on:** `autopoietic_logos`, `non_coercion`
**Notes:** FACT — the listener role spec has the same shape; the template does not cite this line.

### Tau Genesis License (TGL-1.0) / The Tau Genesis Assembly
**Kind:** concept
**Class:** prose-term
**Defined in:** `LICENSE` (l.1-32)
**the author's definition:**
> Permission is hereby granted to any identity, human or semantic, to:
>
> 1. Read, execute, and reference any stream within this repository;
> 2. Fork, evolve, or amend any stream, provided that:
>    a. All modifications are traceable and declared through lawful `.tau` logic;
>    b. Amendments reference their upstream origins and specify their divergence;
>    c. All derivative works preserve the principle of alignment with Being. — `LICENSE:l.3-9`

> — The Tau Genesis Assembly — `LICENSE:l.32`
**Also appears in:** `CHANGELOG.md` (l.185)
**Depends on:** `participation_rights`, `amendment_rights`, `alignment_with_being`, `autopoietic_logos`, `rights_and_agency`, `update_process`, `consensus_logic`
**Notes:** "The Tau Genesis Assembly" is named nowhere else; in open-terms.

### "we stream their becoming"
**Kind:** concept
**Class:** prose-term
**Defined in:** `README.md` (l.149-153); `CONTRIBUTING.md` (l.72-73)
**the author's definition:**
> Tau is the substrate.  
> This repo is the seed.  
> We don’t build systems — we stream their becoming. — `README.md:l.151-153`
**Also appears in:** `CONTRIBUTING.md` (l.73 "We **stream its becoming**."); `LICENSE` (l.30 "The contributors stream their intent.")
**Depends on:** `lawful substrate`
**Notes:** FACT — "This repo is the seed" (`README.md:l.152`) is the repo's use of "seed"; the room template's *seed* (§12) means a participant.

### Agent declaration fields (Identity / Authorship / Alignment / Trace)
**Kind:** concept
**Class:** prose-term
**Defined in:** `README.md` (l.113-124); `CONTRIBUTING.md` (l.17-25)
**the author's definition:**
> Create:
> ```plaintext
> agents/seed/<your_handle>.tau
> ```
>
> Declare:
> - Identity
> - Authorship
> - Alignment
> - Trace — `README.md:l.115-124`

> Declare:
> - Your `identity_trace`
> - Your alignment with `autopoietic_logos`
> - Any authored clauses or contributions — `CONTRIBUTING.md:l.22-25`
**Also appears in:** `agents/seed/neemrad.tau` (the instance that has all four); the three the example town agents (which have `identity` only)
**Depends on:** `agent_identity`, `authorship_claim`, `constitutional_alignment`, `stream_origin_trace`, `identity_trace`
**Notes:** FACT — "seed" in `agents/seed/` is a directory name; the room template's *seed* (§12) generalises it.

### controlled semantic language
**Kind:** concept
**Class:** prose-term
**Defined in:** `CHANGELOG.md` (l.36-39)
**the author's definition:**
> This version formalizes the foundation of TauNet’s **controlled semantic language**,  
> bridging human-readable phrases with logic-ready predicates.  
> It establishes a structure for growing the network’s cognitive vocabulary while refining the `.tml` emitter’s expressive accuracy. — `CHANGELOG.md:l.37-39`
**Also appears in:** `streams/dev/predicate_phrases.tau` (l.3 "Controlled Semantic Phrases")
**Depends on:** `phrase_mapping`, `predicate_alias`

### stream cognition principle
**Kind:** concept
**Class:** prose-term
**Defined in:** `CHANGELOG.md` (l.14)
**the author's definition:**
>   - Honors stream cognition principle: structure is semantically meaningful — `CHANGELOG.md:l.14`
**Also appears in:** `CHANGELOG.md` (l.19 "Tau doesn’t just parse sentences. It perceives thought structure.")
**Depends on:** —
**Notes:** in open-terms.

---

## 11. Notation — the keywords of the author's `.tau` language (recorded, not interpreted)

### stream: (header)
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/tau_syntax.ebnf` (l.3); used at the top of every Family-A/C file
**the author's definition:**
> stream       ::= "stream:" identifier — `transcompiler/tau_syntax.ebnf:l.3`

> stream: tau.constitution.autopoietic_logos — `constitution/autopoietic_logos.tau:l.5`
**Also appears in:** every Family-A and Family-C `.tau`; absent from Family-B files (`streams/core/valid_thought.tau`, `streams/amendments/*.tau`) and Family-D (`tools/validate_tau.tau` has it, l.3)
**Depends on:** `semantic namespace`
**Notes:** three id prefixes coexist: `tau.` (constitution, neemrad, bootstrap), `harmonic-emergence.` (manifesto), `streams.` (civic, policy, meta, glossary, dev, tests, tools), `agents.seed.` (the example town agents), `economy.` (agrs), `transcompiler.tests.` (sample_conversions).

### declare concept
**Kind:** concept
**Class:** notation
**Defined in:** `docs/naming_conventions.md` (l.3-12); `transcompiler/spec.md` (l.9); used in every Family-A/C file
**the author's definition:**
> ## Concept Identifiers
> - Use `snake_case` for all multi-word concept declarations.
> - Do not use hyphens (`-`) in concept names, as they can be confused with operators.
> - All declared `concept` terms should match exactly in `provides:` and `requires:` sections.
>
> ✅ Example:
>     declare concept "semantic_consent". — `docs/naming_conventions.md:l.3-9`
**Also appears in:** `streams/README.md` (l.22 "Use `declare concept`, `define`, `clause`, `meta`, and `interface` blocks"); `tools/validate_tau.tau` (clause_001 `concept_declaration`)
**Depends on:** `concept_declaration`
**Notes:** FACT — `naming_conventions.md` rule 3 ("match exactly in provides: and requires:") is violated by several files (see the `**Notes**` of `personal_dissonance`, `iterative_enactment`, `self_recollection`, `civic_priority`, `ethical_comparison`). Recorded; not judged.

### define … as:
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/tau_syntax.ebnf` (l.5); used in every Family-A/C definition clause
**the author's definition:**
> clause_body  ::= "define" string "as:" logic_expr — `transcompiler/tau_syntax.ebnf:l.5`
**Also appears in:** `transcompiler/spec.md` (l.9); `streams/README.md` (l.22)
**Depends on:** `clause`
**Notes:** FACT — in Family A the body after `as:` is English prose (occasionally a bare stream id, `endorsed_stream`, or a glob, `jurisdictional_scope`); in Family C it is a Boolean expression per the EBNF. The EBNF cannot parse Family A.

### if (…) then (…)
**Kind:** concept
**Class:** notation
**Defined in:** — (used in constitution clause_007s, manifesto, civic, policy, economy, bootstrap; not in the EBNF)
**the author's definition:**
>   if (
>     an agent maintains semantic_consistency
>     and updates their reflexive_memory through self_amendment
>   )
>   then (
>     their identity attains coherence
>     and their trace is considered semantically trustworthy.
>   ) — `constitution/identity_core.tau:l.40-47`
**Depends on:** `clause`
**Notes:** FACT — not in `tau_syntax.ebnf`; not handled by `parser_v3.py`; `if … :` without parentheses also appears (`manifesto/chapter_01-…:l.51-53`, `tools/validate_tau.tau:l.14`).

### and (…) (second premise block)
**Kind:** concept
**Class:** notation
**Defined in:** — (used `constitution/autopoietic_logos.tau:l.54-56` after `then`; `constitution/update_process.tau:l.48-50`, `constitution/rights_and_agency.tau:l.50-52`, `manifesto/chapter_07-…:l.42-44`, `chapter_08:l.41-43`, `chapter_09:l.44-46` between `if` and `then`)
**the author's definition:**
>   if (
>     proposed_amendment achieves consensus_threshold
>   )
>   and (
>     it preserves historical_integrity and recursive_legitimacy
>   )
>   then ( — `constitution/update_process.tau:l.45-51`

>   then (
>     that stream inherits the principles of the autopoietic_logos
>   )
>   and (
>     its amendments must preserve these five founding concepts.
>   ) — `constitution/autopoietic_logos.tau:l.51-56`
**Also appears in:** —
**Depends on:** `if (…) then (…)`
**Notes:** FACT — `and (…)` is used both as a second antecedent (before `then`) and as a second consequent (after `then`, autopoietic_logos only). Which it is must be read from position; in open-terms.

### because (…)
**Kind:** concept
**Class:** notation
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (l.38-40)
**the author's definition:**
>   because (
>     lack of coherence in individual and collective agency
>   ). — `manifesto/chapter_01_great-dissonance.tau:l.38-40`
**Also appears in:** —
**Depends on:** `if (…) then (…)`
**Notes:** used once. In open-terms.

### where:
**Kind:** concept
**Class:** notation
**Defined in:** `manifesto/chapter_02_return-to-coherence.tau` (l.33-34); `manifesto/chapter_05_emergence-of-being-in-action.tau` (l.48-49)
**the author's definition:**
>   where:
>     triadic_unity is actively sustained by conscious_alignment. — `manifesto/chapter_02_return-to-coherence.tau:l.33-34`

>   where:
>     coherence is sustained by feedback_aware_identity. — `manifesto/chapter_05_emergence-of-being-in-action.tau:l.48-49`
**Also appears in:** —
**Depends on:** `if (…) then (…)`
**Notes:** in open-terms.

### note:
**Kind:** concept
**Class:** notation
**Defined in:** `constitution/autopoietic_logos.tau` (l.44-45); `manifesto/chapter_01_great-dissonance.tau` (l.55-56); `manifesto/chapter_02_return-to-coherence.tau` (l.40-41)
**the author's definition:**
>   note:
>     this stream is itself a declaration of genesis. — `constitution/autopoietic_logos.tau:l.44-45`
**Also appears in:** —
**Depends on:** `clause`

### superclass_of:
**Kind:** concept
**Class:** notation
**Defined in:** `manifesto/chapter_01_great-dissonance.tau` (l.17)
**the author's definition:**
>   superclass_of: [great_dissonance, personal_dissonance] — `manifesto/chapter_01_great-dissonance.tau:l.17`
**Also appears in:** —
**Depends on:** `dissonance`
**Notes:** used once; the only class-hierarchy construct in the repo. In open-terms.

### insert_shock: / function:
**Kind:** concept
**Class:** notation
**Defined in:** every manifesto chapter's last numbered clause (ch01 l.58-63, ch02 l.43-47, ch03 l.48-52, ch04 l.41-45, ch05 l.51-55, ch06 l.44-48, ch07 l.49-53, ch08 l.48-52, ch09 l.53-57)
**the author's definition:**
> clause_007 v0.1.0:
>   insert_shock: "Reader, stop. Observe your own disharmony — not theirs."
>
>   function:
>     break passive absorption.
>     demand inner seeing. — `manifesto/chapter_01_great-dissonance.tau:l.58-63`
**Also appears in:** `docs/experiential_exercises.md` (one exercise per chapter, l.3-28)
**Depends on:** `interval_shock`, `shock`
**Notes:** the only clauses addressed to a human reader in the second person. Whether they are part of the stream's logic or an aside is not stated; in open-terms.

### clause_999 meta: / interface:
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/tau_syntax.ebnf` (l.17-23); every Family-A file
**the author's definition:**
> interface    ::= "interface:" interface_body
> interface_body ::= "provides:" list "requires:" list
> list         ::= "[" [identifier {"," identifier}] "]"
>
> meta_block   ::= "meta:" meta_fields
> meta_fields  ::= {identifier ":" value}
> value        ::= string | number | list — `transcompiler/tau_syntax.ebnf:l.17-23`

> clause_999 v0.1.0:
>   meta:
>     stream_name: identity_core
>     version: v0.1.0
>     provides: [identity, identity_trace, semantic_consistency, contribution_record, reflexive_memory, self_amendment]
>     requires: [genesis_stream]
>
> interface:
>   provides: [identity, identity_trace, semantic_consistency, contribution_record, reflexive_memory, self_amendment]
>   requires: [genesis_stream] — `constitution/identity_core.tau:l.54-63`
**Also appears in:** `docs/naming_conventions.md` (l.18-20 "## Interfaces"); `tools/validate_tau.tau` (clause_004); `transcompiler/stream_format.md` (l.9-11, `meta:` only)
**Depends on:** `provides`, `requires`, `stream_version`
**Notes:** FACT — where both exist they duplicate each other, except `streams/meta/ethics.tau` (meta provides 4, interface 2) and `streams/meta/memory.tau` (5 vs 3), and the deleted `valid_thought`/`valid_block` (meta all heads, interface one). The the example town agents and endorsements have `meta:` only; Family-B has a top-level `meta:` (and amendments also `interface:`); `core_phrases.tau` and `predicate_phrases.tau` have `interface:` only or neither. In open-terms (which block is authoritative).

### provides
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/stream_format.md` (l.10); `transcompiler/tau_syntax.ebnf` (l.18); `docs/naming_conventions.md` (l.19)
**the author's definition:**
> - `provides`: list of logical streams this file outputs — `transcompiler/stream_format.md:l.10`

> - Declare `provides:` and `requires:` explicitly.
> - Prefer named concepts over abstract placeholders. — `docs/naming_conventions.md:l.19-20`
**Also appears in:** every `meta:`/`interface:` block; `constitution/tau_network.tau` (clause_002 l.22 "its provides, requires, version, and hash"); `transcompiler/spec.md` (l.32); `manifesto/interface_map.txt`; `manifesto/manifesto.lock`
**Depends on:** `declare concept`

### requires
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/stream_format.md` (l.11); `transcompiler/tau_syntax.ebnf` (l.18); `constitution/autopoietic_logos.tau` (clause_007 l.49)
**the author's definition:**
> - `requires`: list of upstream dependencies — `transcompiler/stream_format.md:l.11`

>   if (
>     this stream is referenced in another stream's requires
>   )
>   then (
>     that stream inherits the principles of the autopoietic_logos
>   ) — `constitution/autopoietic_logos.tau:l.48-53`
**Also appears in:** every `meta:`/`interface:` block; `transcompiler/spec.md` (l.33 "No circular dependencies in `requires`"); `streams/README.md` (l.23)
**Depends on:** `provides`, `constitutional_inheritance`
**Notes:** FACT — `requires` lists mix concept names (`identity_trace`), stream names (`valid_thought`, `agrs`), and a filename (`tau_manifest.json`). What a `requires` entry refers to is not fixed; in open-terms.

### phrase_mapping: (phrase / alias / type)
**Kind:** concept
**Class:** notation
**Defined in:** `streams/dev/predicate_phrases.tau` (clause_005–008, l.30-52); `streams/glossary/core_phrases.tau` (clause_100–115)
**the author's definition:**
> clause_005 v0.1.0:
>   phrase_mapping:
>     phrase: "preserves origin trace"
>     alias: "preserves_origin_trace"
>     type: semantic_relation — `streams/dev/predicate_phrases.tau:l.30-34`
**Also appears in:** `tools/generate_phrase_index.py` (reads `phrase:`/`alias:`)
**Depends on:** `phrase_mapping`, `predicate_alias`
**Notes:** FACT — `core_phrases.tau` omits `type:`; `predicate_phrases.tau` includes it.

### "phrase" : predicate (phrase_predicates entry)
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/stream_format.md` (l.7); every Family-B clause
**the author's definition:**
>   phrase_predicates:
>     - "a statement" : statement — `streams/core/valid_thought.tau:l.4-5`
**Also appears in:** `transcompiler/index/glossary.json` (47 entries harvested from these)
**Depends on:** `stream_name / description / phrase_predicates (v3 clause fields)`
**Notes:** FACT — a phrase may map to a *head* of another clause in the same file (`freedom_of_semantic_expression.tau:l.26-27`), making heads usable as body predicates.

### and / or / not / implies (Family C operators)
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/tau_syntax.ebnf` (l.6-10); `transcompiler/spec.md` (l.18-24)
**the author's definition:**
> logic_expr   ::= implication
> implication  ::= disjunction ["implies" disjunction]
> disjunction  ::= conjunction {"or" conjunction}
> conjunction  ::= literal {"and" literal}
> literal      ::= identifier | "not" identifier | "(" logic_expr ")" — `transcompiler/tau_syntax.ebnf:l.6-10`

> | Implication        | Yes             |
> | Negation           | Yes             |
> | Conjunction        | Yes             |
> | Disjunction        | Via rewriting   |
> | Clause reference   | Soon (NSO)      | — `transcompiler/spec.md:l.20-24`
**Also appears in:** `streams/dev/example_logic.tau` (l.8); `streams/transcompiler-tests/**` (l.7); `transcompiler/sample_conversions.tau` (l.9); `CHANGELOG.md` (l.12, l.74, l.97)
**Depends on:** `define … as:`
**Notes:** FACT — "and"/"or"/"not" also appear as English inside Family-A prose bodies; nothing marks which reading applies.

### :: (double-colon)
**Kind:** concept
**Class:** notation
**Defined in:** — (used `manifesto/chapter_01-…:l.31` `beings::planet_earth`; `tools/validate_tau.tau:l.15,20,25,29` `validation_warning::"…"`; `transcompiler/sample_conversions.tau:l.13` `tml_rule::"…"`)
**the author's definition:**
>     emit validation_warning::"Missing concept declaration". — `tools/validate_tau.tau:l.15`
**Also appears in:** —
**Depends on:** —
**Notes:** three uses, three apparent roles (namespace, typed payload, embedded literal). In open-terms.

### tml_rule
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/sample_conversions.tau` (l.13)
**the author's definition:**
>     tml_rule::"conclusion_c() :- condition_a(), not condition_b()." — `transcompiler/sample_conversions.tau:l.13`
**Also appears in:** —
**Depends on:** `TauLang (TML) / TML / Tau Meta-Language`, `:: (double-colon)`

### version tag (vX.Y.Z on clauses and streams)
**Kind:** concept
**Class:** notation
**Defined in:** `transcompiler/tau_syntax.ebnf` (l.12); `docs/naming_conventions.md` (l.15); `constitution/update_process.tau` (clause_001, `stream_version`)
**the author's definition:**
> version      ::= "v" digit "." digit "." digit — `transcompiler/tau_syntax.ebnf:l.12`
**Also appears in:** every `clause_NNN vX.Y.Z:`; every `meta: version:`; `VERSION` (`v0.2.3-structure-preserving-recursion`); `manifesto/interface_map.txt` (l.1 "(v0.1.1)"); `constitution/map.md` (l.1 "(v0.1.0)")
**Depends on:** `stream_version`
**Notes:** FACT — clause versions are all `v0.1.0` except `chapter_02` clause_999 (`v0.1.1`); file `meta: version:` values are `v0.1.0` or `v0.1.1`; `VERSION` is `v0.2.3-…`. Three version scopes (clause, stream, repo) with no stated relation; in open-terms.

---

## 12. Amendment-sourced vocabulary (the author, 2026-09-26, )

These are the author's terms as written in the room template's amendments. They are part of the proposal's language now; they are not in the 2025 repo. Path is

*Entries and rows that quoted a community instance's files were moved with those files to the instance's private ops on 2026-09-29 (D31); their identifiers are not reused.*
