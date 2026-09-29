# LANGUEDOC — the shared vocabulary (draft 1, 2026-09-27)

Brief §3 step 4: after the Phase 2 report, the author and the companion converge on one vocabulary that both the proposal and the Tau side use. Amendment 6: start it from the proposal's own conflicts, not from IDNI's glossary. Draft 1 folds Amendment 8 (D19–D23): the five rows below are decided; the rewrites in §2 are proposals awaiting the author's signature. Undecided rows keep their options.

| Term | Problem today | Options | Status |
|---|---|---|---|
| **Being** | Used as the thing everything aligns with; never defined (`docs/proposal/open-terms.md` §B). | **D19:** a constitutional primitive, not a Tau term. Stays in prose in `autopoietic_logos` as the orientation of the room. `being` and `alignment_with_being` are reserved-forbidden identifiers in any emitted spec (F5). Executing clauses that compare it are rewritten in measurable terms or retired (§2). | **decided D19** |
| **stream** | File / clause head / version sequence (`concepts.md`, M002). | Three words: *specification* (file), *predicate* (clause head), *history* (version sequence). | open |
| **identity** | Generic in constitution, self-referential in each seed (M003). | *identity* = the type; *seed* = an instance with presence (A5). | open |
| **seed** | A5 term: a stakeholder with presence, in time. | Adopt as the instance word for identities, including natural seeds. | proposed |
| **endorsement** | Five definitions (M004). | One predicate: endorses(seed, stream, rationale, t); no count, threshold or weight output (D21). Oracle-verified instance: learner step 4, `stream_endorsement` (three seeds, three record outputs). | proposed, with a verified instance |
| **amendment** | Family-A text vs v3 rewrite differ in logical direction (M008). | **D20:** Family A is canonical (rule form: if the antecedents are preserved then the obligation holds). v3 and `.tml` stay in history as a known-wrong translation; F1 toy runs both before the author signs the restoration. | **decided D20** |
| **weight / direction / next state** | A5 vocabulary; precursors in `amendment_quorum`, `value_distribution_criteria`. | **D21:** weight lives above Tau (F7); the opinion map's agree/disagree relation is the *direction* input; endorsement counts are records, never a magnitude. | **decided D21** |
| **room** | A3 term. | Keep; a room's civic streams are its constitution (the illustrative example under `streams/*/example/`; real instances live in their private ops, D31). | proposed |
| **Affirming / Negating / Reconciling** | §6 design terms. | Keep as force names; never as agent names. | proposed |
| **record / ledger / candidate / minority report** | Template terms (`dao/TEMPLATE.md`). | Keep. | proposed |
| **execute / emit / `::` / `=`** | Notation never defined (open-terms §C). | the author says what each means or they are dropped in the migration. | open — the author |
| **silencing (non-retroactive)** | `freedom_of_semantic_expression` / `contradiction_mediation`: what a revision may not do to prior speech (G11). | **D22:** split by object. *Records*: absolute, append-only; removal is a redaction record. *Clauses*: never silent, not undroppable; dropping another seed's accepted clause emits a minority-report entry and gives the emitter standing to force a re-hearing. Enforced above `u`; nothing reaches `u` unsigned. | **decided D22** |
| **TML / `.tml` / transcompiler** | The proposal's stated target; dormant since 2023 (G01). | **D23:** retired. Files move to history, never deleted; `kb/HISTORY.md` is the migration record; F2 targets Tau v0.7 at the pinned commit only. | **decided D23** |
| **consensus_finality (in clause_007)** | `constitution/consensus_logic.tau` defines it in clause_005 as a *state* ("no further contradiction … stable across verification cycles") and consumes it in clause_007 as a *permission* ("consensus_finality may be declared"). The learner's first reading of clause_007 was the clause_005 state (a two-cycle window over consensus); the pre-registered test read the permission (the same bit as the premises). Both defensible from the text; the test won for the measurement. | Decide which the rule means: (a) the permission bit, so clause_007's two outputs are one; or (b) the state, so clause_007's consequent is a lookback and clause_005 is its definition. Recommendation: (a) for clause_007 and keep clause_005 as the definition of the state a later clause may test. | proposed (from learner step 2) |
| **freedom_of_expression: per step or irrevocable** | Amendment 001 clause_002 says "the irrevocable right". The learner's first reading was cumulative (one rejection, lost for good); the pre-registered test read it per step (preserved at t unless an emission is rejected at t). The word "irrevocable" is about the right, not about its preservation record. | Decide: (a) per step, the right is preserved or breached at each t and the breach is a record (D22); or (b) cumulative, a single breach marks the stream. Recommendation: (a); (b) confuses the right with the room's standing. | proposed (from learner step 3) |

## 2. Rewrites under D19 — proposals for the author's signature

Rule: every clause that must *execute* and today compares `alignment_with_being` is rewritten in defined, measurable terms (`coherence`, `origin_trace`, `record`) or retired. The original stays quoted beside the rewrite. Prose uses of "Being" (manifesto ch05, LICENSE, `docs/index.md`, `testnet/README.md`) are untouched: they orient, they do not execute.

| # | Where | Original (verbatim) | Proposed rewrite | Kind | Grounds |
|---|---|---|---|---|---|
| R1 | `constitution/autopoietic_logos.tau` clause_005 | `define "alignment_with_being" as: coherence between a stream's evolution and the essence of life, awareness, and cosmic necessity.` | **Keep as prose, mark non-executing.** Add `note: constitutional primitive (D19); not referenced by any emitted specification.` Remove `alignment_with_being` from the `provides:` lists (l.62, l.66) so no stream can `require` it. | retire from interface | D19: a primitive is oriented to, never computed. |
| R2 | `streams/meta/ethics.tau` clause_003 | `define "alignment_with_being" as: a stream's capacity to promote emergence, reduce fragmentation, and integrate truth with trace.` | Rename the *executing* content: `define "trace_integrity" as: the degree to which a stream's clauses preserve origin_trace (every claim cites its records) and coherence (no contradiction with accepted clauses unless amended), measured per revision.` | rewrite | The definition's measurable half is exactly `preserves_origin_trace` + `does_not_contradict_prior_reasoning` (`valid_thought`); "promote emergence, reduce fragmentation" is orientation and returns to prose. |
| R3 | `streams/meta/ethics.tau` clause_005 | `define "ethical_comparison" as: a semantic operation yielding relative value_score based on impact_scope and alignment_with_being.` | `define "ethical_comparison" as: a semantic operation yielding relative value_score based on impact_scope and trace_integrity, with the comparing seed's weight per domain (dao/weight.md) as the only magnitude.` | rewrite | D19 removes the primitive from the computation; D21 supplies the magnitude. |
| R4 | `streams/meta/ethics.tau` clause_001 | `define "value_score" as: a computed scalar representing semantic alignment with collective well-being, lawfulness, and coherence.` | `define "value_score" as: a computed scalar over a candidate stream: coherence (sat-checked), trace_integrity, and impact_scope, each labelled with the records it rests on; never a vote count.` | rewrite | "collective well-being" is undefined; the three retained terms are gate predicates or ledger-derived. |
| R5 | `streams/meta/ethics.tau` meta/interface `provides` | `provides: [stream_preference, value_score, impact_scope, alignment_with_being]` | `provides: [stream_preference, value_score, impact_scope, trace_integrity]` | rename | Follows R2. |
| R6 | `streams/amendments/freedom_of_semantic_expression.tau` (v3) clause_001 | `"seeks to inform, request, align, or reflect Being" : intentional_semantic_action` | Under D20 the Family-A text is canonical; in the restored Family-A file the phrase stays as prose in the definition of `intentional_semantic_action`, and the executing predicate binds to `authored_by_agent ∧ has_identity_stream` (an emission from a declared identity). | rebind | "reflect Being" is orientation; what executes is that a declared identity emitted it. |

Each rewrite becomes a candidate stream `…_v0.2.tau` only after the author signs this table; until then the originals stand and `alignment_with_being` remains a forbidden identifier for any spec the oracle sees.


## 3. Glossary — every term in use, one line each (the shared-glossary requirement, applied to ourselves)

**RULE (2026-09-29).** No term enters a document of this project without a line here. A term that is not here is not used. Identifier families are frozen at three for the record (D decisions, Q questions, M mappings) plus test names; G, R, A, F, L and S identifiers already in the documents keep their meaning and gain no new members.

| Term | Meaning, one sentence | Where it lives |
|---|---|---|
| proposal | The 2025 text of this repository: constitution, streams, amendments, manifesto, written as pseudocode. | `constitution/`, `streams/`, `docs/proposal/README-2025.md` |
| foundation | The Tau Language as IDNI ships it, pinned at commit `3badb21`. | IDNI's `tau-lang`; `docs/tau-curriculum.md` |
| specification | A Tau formula over streams that the executable parses; "spec" for short. | everywhere |
| stream | A named sequence of values in time, input or output, declared in a specification. | Tau; `tools/tau_oracle.py` |
| verifier, oracle | The `tau` executable driven by `tools/tau_oracle.py`: parse, satisfiability, normalisation, execution. | `tools/tau_oracle.py` |
| verified | Parsed, found satisfiable, and executed with the asserted outputs against a test written before generation. | `README.md`, the rule |
| hidden test | A pre-registered acceptance test the model never sees; only its stream interface is shown. | `tools/learner/tests/` |
| learner | The loop retrieval → generation → verification that produces specifications from proposal fragments. | `tools/learner/`, `docs/learner-v1.md` |
| fragment | One clause, definition or rule of the proposal sent to the learner. | `tools/learner/run.py` |
| curriculum | The ordered list of Tau capabilities with what the corpus and the learner have demonstrated. | `docs/tau-curriculum.md` |
| ablation | The learner run with parts of the prompt removed, to see what they contribute. | `docs/tau-curriculum.md` |
| reduced | A verified specification that reads exactly one input and copies it; correct by design, flagged. | `docs/tau-curriculum.md` |
| mapping (M) | One row per proposal construct: the Tau construct it maps to and a verdict. | `docs/reconciliation/mapping.md` |
| faculty | A capability the language does not provide and the room needs above it (F1–F11). | `docs/reconciliation/faculties.md` |
| gap (G) | A place where proposal and foundation genuinely disagree, both sides quoted. | `docs/reconciliation/gaps.md` |
| decision (D) | A signed choice by the author, numbered, never rewritten. | private record; cited by number |
| question (Q) | An open item the author must answer, numbered. | private record; cited by number |
| rewrite (R) | A proposed change to a proposal sentence awaiting the author's signature. | `docs/LANGUEDOC.md` §2 |
| Family A / v3 | The amendments as first written / their later head-conjunction rewrite; A is canonical (D20). | `docs/proposal/family-a/`, `streams/amendments/` |
| primitive | A constitutional term oriented to and never computed: `being`, `alignment_with_being` (D19). | `docs/LANGUEDOC.md` |
| room | A community as an environment that invites participation, run on the template. | `dao/TEMPLATE.md` |
| instance | One room's private ops that passes the conformance suite. | `dao/template/` |
| seed | An identity with presence in a room: a person in a public role, an institution, an agent, a river. | `dao/TEMPLATE.md`, `agents/seed/` |
| natural seed | A seed that is not a person or institution (a river, a mountain range), spoken for by records. | `dao/TEMPLATE.md` §8 |
| force | One of the three separate processes of a room: Affirming, Negating, Reconciling. | `dao/TEMPLATE.md` §1 |
| Affirming | The force that records everything that enters, raw, with provenance; never prunes. | `dao/TEMPLATE.md` |
| Negating | The force that objects, on agent outputs only, citing records; never on human input. | `dao/TEMPLATE.md` |
| Reconciling | The force that proposes candidate specifications and minority reports. | `dao/TEMPLATE.md` |
| signer | The role that publishes: no candidate returns to the room unsigned. | `dao/TEMPLATE.md` §5 |
| ledger | The Affirming record: append-only, hash-chained lines, one file per surface per month. | `dao/template/schema/record.schema.json` |
| record | One ledger line with id, previous hash, time, surface, author class, text, provenance. | same |
| redaction | A record that blanks a text on the emitter's request and keeps the event. | `dao/TEMPLATE.md` §6 |
| candidate | A specification Reconciling proposes, run through the verifier, awaiting a DECIDE. | `room.py propose` |
| DECIDE | The signed record that enacts a candidate or a disclosure; the room's only act of publication. | `room.py decide` |
| minority report | The record of what a revision dropped and who objected, kept verbatim. | `tools/minority_report.py` |
| spec-diff | What a revision keeps, drops or makes conditional, clause by clause. | `tools/spec_diff.py` |
| weight | A computed, per-domain, revisable measure of a seed's record; never assigned, never a vote count. | `dao/weight.md` |
| direction | A seed's agree/disagree relation to a position; the opinion map's input. | `dao/weight.md` |
| variable | A named fact of a room with a class: public by source, public by decision, private, shielded. | `dao/template/schema/variable.schema.json` |
| disclosure | A DECIDE that changes a variable's class; private by default, public by decision. | `room.py disclose` |
| consent level | How a person appears: public name, role only, anonymous, keyed pseudonym. | `dao/template/schema/consent.schema.json` |
| anchor | A dust shielded Zcash transaction whose memo carries the ledger and decision heads; notary only, never money. | `dao/template/tools/anchor.py` |
| viewing key | The key that lets someone read a room's anchor stream; giving it is a logged consent. | `dao/template/tools/anchor_verify.py` |
| boundary | A force may read only the streams it declares; no wire, no read. | `dao/template/tools/boundary_check.py` |
| conformance | The test suite a directory must pass to be a room; its version is in every DECIDE. | `dao/template/conformance/` |
| template | The constitution (`TEMPLATE.md`) plus the schemas, runtime and suite (`template/`). | `dao/` |
| runtime | `room.py`: eight verbs that write schema-valid records and judge nothing. | `dao/template/tools/room.py` |
| companion | The model instance that does this work under the author's direction; every claim it makes is checkable. | private record |
| author | The person who wrote the proposal and signs decisions. | everywhere |
| FACT / INFERENCE / SPECULATION | Confirmed against primary data / a reading of it / a guess; every claim carries one. | house rule |
| in-sample / hidden | A number measured on what the model saw / on tests it never saw; always stated. | house rule |
