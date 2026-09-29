# dao/TEMPLATE.md — the DAO template, fixed

**Status:** draft v0.2, 2026-09-27, companion. Not instantiated. the author vetoes per item. v0.2 adds §12 (birth declaration, D17) and §13 (virtualization, A7).
**Source of authority:** the program's decisions (private record); the assessment is the fix list; gates become predicates; Negating gets a seat), the room rules (three forces, three homes; Negating never runs on human input), the room rules (weight, role-audit seat, natural seeds), §6 (Los Tres Soles).
**Fix list:** every defect in `docs/PROGRAM_ASSESSMENT.md` §3–§4 appears in §2 below with the fix that closes it. A defect not listed there is not fixed.

Labels: **RULE** = binding on any instance. **DEFAULT** = instance may override in its own `INSTANCE.md` with a logged reason. **SLOT** = deliberately left open; the template must not fill it.

---


> **v1.0-draft (2026-09-29): the template runs.** What binds stays here as text (§1, §3, §8, §10, §12, §13). What checks lives in [`template/`](template/README.md): one JSON Schema per record kind, the runtime `room.py` (init, affirm, object, propose, decide, disclose, anchor, verify), and the conformance suite. A directory is a room iff `room.py verify <dir>` passes; every DECIDE records the suite version it passed under. Section → what enforces it: §1 RULEs → `test_B_boundary` (declared wires only; a force never reads another's scratch; adversarial reads and truncation fail on a deployed room); §4 gates → `room.py propose` (the verifier disposes) and `test_F04`; §5 approval → `room.py decide` (refused without a satisfiable candidate and a keyed signatory) and `test_S5`; §6 ledger → `chain.py`, `test_S6`, `test_F06`; §7 weight → `dao/weight.md` (above the runtime, unchanged); §9 spend → `spend.jsonl` schema; F1–F17 → the tests named by their number where one exists (F4, F6, F7, F11, F14 today; the rest are the suite's backlog). The seventeen fixes stay in this file: they are the record of what went wrong once, stated as conditions, and the reason the suite exists.

## 1. Shape

An instance is a room with three forces and a record. It has:

| Part | What it is | Home |
|---|---|---|
| **Object** | what the instance is about (the instance: a paper; the instance: the example town as a room) | `INSTANCE.md` |
| **Ledger** | the Affirming record: everything that entered, raw, with provenance | `ledger/` |
| **Seeds** | the identities that have presence: people in their public roles, institutions, agents, and natural stakeholders | `agents/seed/*.tau` + `ledger/seeds/` |
| **Roster** | the agent members, one file each, with the force they serve | `roster.yml` |
| **Candidates** | what Reconciling proposes back to the room | `candidates/` |
| **Minority reports** | what Negating left unresolved on each candidate | `minority/` |
| **Decisions** | what the signer decided, authenticated | `decisions.jsonl` |
| **Spend** | every cost line, per provider, per run | `spend.jsonl` → `docs/RESOURCES.md` |

**RULE — three forces, three processes.** Affirming, Negating and Reconciling run as separate processes with separate contexts, separate logs, and a fixed order: Affirm → Negate → Reconcile. One process may not play two forces in one run. (Brief §6: "the three forces must not be one process pretending to be three.")

**RULE — what each force acts on.** Affirming acts on *information* (everything enters). Negating acts on *knowledge* (agent outputs only). Reconciling acts on *wisdom* (a judgment plus a minority report). (the room rules table.)

**RULE — Negating never runs on human input.** A person's words enter the ledger as-is and stay. Pruning applies to what the agents make of them. (the room rules.)

**RULE — agents propose, a person publishes.** No candidate returns to the room until the signer has signed it. (the room rules rail 6.)

---

## 2. The fix list

Each row: the defect as the assessment found it in the instance, the rule that closes it here, and the predicate it becomes (§4).

| # | Defect (the instance, `PROGRAM_ASSESSMENT.md`) | RULE in the template | Predicate |
|---|---|---|---|
| F1 | Quotation gate passes a file with zero quotations (§4: "0 defects in 1 quotations → PASS"). | A deliverable with no ledger citations is **not gate-eligible**. Minimum evidence is a hard floor, DEFAULT 1 cited record per claim. | `preserves_origin_trace` |
| F2 | Gate tolerates `max(5, 8%)` wrong citations (§3 limit 3). | Tolerance is **zero** for wrong-page/wrong-record. Tool false-positives are fixed in the tool, not absorbed in a tolerance. | `preserves_origin_trace` |
| F3 | Fenced blocks are blanked; invented quotations sat there (§3 limit 4). | The gate reads **all** text. Nothing is exempt by markup. | `preserves_origin_trace` |
| F4 | Only essay quotations checked; FACT sources checked by no tool (§3 limit 5). | Every FACT cites a **ledger record id**; the gate resolves the id and matches the quoted span against the record's stored text. A FACT whose source is not in the ledger is an INFERENCE until it is. | `preserves_origin_trace`, `statement` |
| F5 | Adversarial verifier disabled on day one by a chat line (§4). | Negating's standing is **structural**: it cannot be disabled by editing policy. Disabling requires a signed decision with grounds in `decisions.jsonl`, and the decision is itself a Negating target. Its objections are logged even when overruled; it may force a re-hearing; it has veto on admissibility, not on outcome. (§6.) | `does_not_contradict_prior_reasoning` |
| F6 | Reviewer emitted 0–50 cards for two days; merged and counted (§2.2). | Every card is **schema-validated on write**; a malformed card is rejected, logged as a fault, and never counted. | (mechanical) |
| F7 | Ledger has no model, lane, cost or runner field; Opus 4.5 verdicts under the `fable` alias count as Fable's (§3). | Every agent output record carries `model_id` (the resolved id, never an alias), `lane`, `runner`, `cost_usd`, `turns`, `head_sha`. Alias resolution is logged. | `authored_by_agent` |
| F8 | "Best practice, fine tuned practices." recorded as human approval (§3, D-0015). | **Approval protocol** (§5): a decision exists only when the authenticated signer emits the exact form. Anything else is *no decision* and the item waits. | `authored_by_agent` (signer identity) |
| F9 | Two reviewer configurations disagreed on 40 of 76 merged PRs; not decidable from the record (§2.2). | Review is **comparable or doubled**: the same resolved model reviews a whole tier, or two reviewers on different model families review everything and the disagreement surface is logged as a research object (§6). | (mechanical) |
| F10 | No gate measures whether a reader learns anything; a correct restatement of the issue scores 10 (§4). | Each deliverable must carry a **`claims:` block**: ≥1 claim that is falsifiable against the ledger, and one sentence on what a reader would do differently. Negating's first task on every deliverable is to try to refute the claims block. No claims block → not gate-eligible. | `statement`, `defined_concepts` |
| F11 | Runs that hit the turn cap are submitted "as they stand" (§4). | A capped or errored run is marked **`incomplete`** and is not gate-eligible. It may be resumed, never reviewed. | (mechanical) |
| F12 | Automation idles indefinitely: 40 "ready" issues invisible to the ready set (§4). | The ready set counts **everything**. A round that plans zero items while any item is ready emits a `stall` event. DEFAULT 3 consecutive stalls → the round refuses to run again without a signed decision (dead-man's switch). | `checks_amendment_status` |
| F13 | Metrics stopped on day two; heartbeats reported OK while reading nothing (§4). | Metrics are computed **every round** from the ledger, not by a separate job that can stop. A heartbeat carries what was read (record ids), or it is a stall. | `evaluates_lineage` |
| F14 | Run logs gitignored; verifier texts survive only in PR comments (§3). | Runs are **records**: `runs/` is committed (text only, secrets scrubbed by the writer, not by review). | `preserves_origin_trace` |
| F15 | Principal is not authenticated; queue rows self-declare their author (§3). | No `by: human` row without **authenticated** identity (§5). Until authentication exists, the instance has no signer and publishes nothing. | `has_identity_stream` |
| F16 | Deliverables narrate their own revision history; a third is bookkeeping (§2.3). | Revision history lives in the ledger (`runs/`), **not in the deliverable**. The deliverable states the current position only. | `semantic_containment` |
| F17 | Two purposes pulled apart: the study, and the institution-building (§1). | An instance has **one object**. Roster, studio, persona work that does not cite the object's ledger is out of scope and is logged as spend without output. | `does_not_leak_terms` |

---

## 3. Roster — roles, by force

Roles, not head-count. Instance 2's head-count and which of the instance's roles carry over is **Q7**, open.

### Affirming (information)

- **Listener** — writes raw records to the ledger from a channel. Never summarizes, interprets, replies for the room, or grades anyone. Full spec: `palomino/roles/listener.md`. (Seven, if its traits fit; the constraint matters, not the name.)
- **Collectors** — mechanical intake from public surfaces (`intake/`). One per surface. They classify `author_class` and nothing else.

RULE: Affirming's measure is **recall**. It is audited by sampling the channel against the ledger; a missed record is a finding.

### Negating (knowledge)

- **Objector** — objects, with stated grounds, to agent outputs: candidates, weights, role evaluations, the weighting function itself (the room rules). Every objection cites the ledger records it rests on. Objections are logged in `minority/` whether or not they prevail.
- **Second objector** — an independent pass on a different model family (brief §9: "so the disagreement surface isn't one model arguing with itself"). Experiment 1 (§7) makes the two passes adversarial by side.

RULE: Negating's measure is **precision and stated grounds**. An objection without a ledger citation is itself inadmissible. Negating cannot be removed or disabled by the members it objects to (F5).

### Reconciling (wisdom)

- **Reconciler** — produces a candidate (a `.tau` stream a person could read and sign) plus a minority report carrying every unresolved objection verbatim. Its measure is whether the candidate can be **acted on** and whether the objections are **visibly preserved**, not absorbed.

### Seats outside the forces

- **Role-audit** — evaluates agents on their record, per domain (`weight.md`). It is not the listener and not a reconciler: whoever records everyone's words must not grade everyone's standing (the room rules). Whether this is "Route 7" or a distinct member is **Q12**.
- **Signer** — a person. the author. Authenticated (§5). The only one who publishes.

DEFAULT: one model family per force at minimum; Negating's second pass on a different family.

---

## 4. Gates as predicates

Brief the room rules step 3: the template's gates are the predicates the proposal already names. Source: `streams/core/valid_thought.tau` (v0.1.0, family B). Each predicate below has (a) the author's phrase, verbatim, (b) the executable check v0 (Python, in the instance's `gates/`), (c) the Tau form it will take in Phase 3 (**SLOT** until the oracle exists — do not write Tau here).

| Predicate (stream) | the author's phrase | Executable check v0 |
|---|---|---|
| `statement` (`valid_thought`) | "a statement" | The deliverable has a `claims:` block with ≥1 claim (F10). |
| `defined_concepts` (`valid_thought`) | "defined concepts" | Every term in the candidate's `interface: provides/requires` resolves to an entry in `docs/proposal/concepts.md` or is declared in the candidate. |
| `preserves_origin_trace` (`valid_thought`) | "preserves origin trace" | Every quoted span and every FACT cites a ledger record id; the id exists; the span occurs in the record's stored text; zero tolerance (F1–F4, F14). |
| `does_not_contradict_prior_reasoning` (`valid_thought`) | "does not contradict prior reasoning unless explicitly amended" | Negating has run on the candidate and its objections are in `minority/`; any contradiction with a signed candidate is either resolved or declared as an amendment (F5). |
| `logically_consistent_with_upstream_definitions` (`thought_coherence`) | "logical consistency with declared upstream dependencies and definitions" | Every `requires` term has a provider among signed candidates or the constitution; dangling `requires` fail (the inventory §4 list is the current failure set). |
| `authored_by_agent` (`thought_origin_trace`) | "authored by agent" | The record carries a resolved `model_id`, `lane`, `runner`, `cost_usd` (F7) or an authenticated human id (F8). |
| `has_identity_stream` (`thought_origin_trace`) | "has identity stream" | The author id maps to an `agents/seed/*.tau` (agents, natural seeds) or to an authenticated signer (F15). |
| `evaluates_lineage` (`reflexive_integrity`) | "evaluates lineage" | Metrics for the round are computed from the ledger and attached (F13). |
| `checks_coherence` (`reflexive_integrity`) | "checks coherence" | The candidate's `claims:` were tested by Negating (F10). |
| `checks_amendment_status` (`reflexive_integrity`) | "checks amendment status" | The round's ready set is complete and stalls are emitted (F12). |
| `declares_all_terms_in_interface` (`semantic_containment`) | "declares all terms in interface" | Terms used in the body ⊆ declared ∪ glossary ∪ `requires` (F16, F17). |
| `does_not_leak_terms` (`semantic_containment`) | "does not leak terms" | Nothing from another instance's object appears (the wall: the instance's paper never enters the instance; F17). |

RULE: a candidate passes the gate only if **all** predicates hold. A gate report lists each predicate with PASS/FAIL and the record ids it checked. A failing predicate names which underspecification caused it; that is the input to Phase 2 ("an agent failure shows which predicate is underspecified").

---

## 5. Approval protocol

RULE: a decision by the signer exists if and only if all of:

1. The message comes from the **authenticated** signer identity (an instance names its mechanism in `INSTANCE.md`; DEFAULT: a signed git commit by the signer's key, or a message bound to a verified channel id **and** confirmed by a signed commit within 24 h).
2. The message contains the exact form `DECIDE <item-id>: <ACCEPT|REJECT|REVISE|WAIT>` followed by grounds. Free text is not a decision (F8).
3. The decision is appended to `decisions.jsonl` with the message verbatim and its provenance, and mirrored as one line in `docs/DECISIONS.md`.

Anything else — including "approved", "fine", "go ahead", "best practice" — is **no decision**; the item stays `wait` and the summons is re-raised once, then lapses with a logged `no-decision` event. A lapse is never read as approval.

---

## 6. Ledger format

The Affirming record. Full schema with field types: `palomino/ledger/SCHEMA.md` (the instance's copy; the template's canonical fields are the same).

RULE: **append-only, hash-chained** (`prev` = previous record's `id` in the same file), one JSONL file per surface per month. A record is never edited; corrections are new records with `supersedes`. Removal on request (the room rules rail 3) is a `redaction` record that blanks `text` and keeps the id, the chain, and the event.

RULE: **provenance on every record**: `surface`, `url`, `fetched_at`, `sha` (of `text`), `collector`, `collector_version`. A record without provenance is not a record.

RULE: **private persons are never profiled** (the room rules rails): `author_class = private_person` stores only `author_hash` (salted, salt not committed); no cross-surface linking; location no finer than the room.

---

## 7. Weight and role evaluation

See `dao/weight.md`. Summary of the RULEs: weight is computed from the ledger per domain, never assigned; floor weight is not zero; weight governs Reconciling, never Affirming; every weight is timestamped, revisable, visible, and contestable with grounds; the weighting function is Negating's first target; role evaluation is a separate seat.

---

## 8. Natural seeds

RULE (the room rules): the river and the Sierra are seeds now. Each has an identity stream (`agents/seed/rio_example.tau`, `agents/seed/sierra.tau`) and a ledger partition (`ledger/seeds/rio_example/`, `ledger/seeds/sierra/`) holding everything observed or said about them. That record is their memory and, in time, the basis of their weight.

**SLOT — proxy interface.** Who speaks for a natural seed and how its agency executes is open. The template does not invent a proxy rule. The identity streams carry a marked `proxy_interface: OPEN` clause.

---

## 9. Spend

RULE: every run appends to `spend.jsonl` (`ts, provider, model_id, lane, usd, run_id, purpose`); every provider has a cap set before first spend; the instance's line in `docs/RESOURCES.md` is regenerated from `spend.jsonl`, not written by hand. Unmeasured spend is a finding (assessment §5.2), not a footnote.

---

## 10. What the template does not decide

- Q7 head-count and carry-over roles.
- Q12 whether the role-audit seat is Seven or distinct.
- The proxy interface for natural seeds (SLOT).
- The Tau form of any predicate (Phase 3).
- Whether IDNI's opinion maps carry weight and direction or only logical agreement (Phase 2 `mapping.md` row; the room rules).

## 11. Back-port to the instance

Per the room rules step 2 the fixes back-port to another program. Not started: the instance's fate is Q6 and its repo is untouched until the author decides. The back-port list is §2 above, F1–F17, in that order.

---

## 12. Birth declaration: what done looks like, and when spending stops (D17)

RULE: an instance declares, at birth, in `INSTANCE.md`, two things it cannot later edit without a signed decision:

- **`STOP-CONDITION`** — the pre-registered condition under which the instance stops spending, written before the first run. No "one more round". Pattern: electric-coin-company `STOP-CONDITION.md`. Minimum content: the metric, its threshold, who reads it, and the date after which idle equals stopped. Every round evaluates it and logs the result; three consecutive `stalled` evaluations trip the dead-man's switch (§2 F12).
- **`MISSION-COMPLETE`** — what done looks like, as an acceptance test a person can run: the artifacts that must exist, the checks they must pass (gate predicates, §4), and the reopen list (what would reopen the mission). Pattern: electric-coin-company `MISSION-COMPLETE.md`, status DRAFT → IN FORCE by signed decision.
- Every host, pod or bucket the instance creates carries a **TTL** in `spend.jsonl` and `docs/RESOURCES.md`; past its TTL it is a line item to the signer, not a running cost.

Instance 1 (another program) has neither; its only stop condition is "rounds repeat until the ready set is empty" (sweep, `docs/plan.md:23-34`). Its fate is Q6; the pattern applies regardless.

## 13. Virtualization as the physical form of the design (A7, strategic instance's read; the author to veto)

Not infrastructure: the form four existing requirements take.

1. **Isolation of the three forces.** Affirming, Negating and Reconciling each run in their own container or VM with their own filesystem and network policy. Separate contexts stop being a discipline (§1) and become a boundary: Negating cannot read Reconciling's scratch; Affirming cannot be pruned by anyone.
2. **Snapshot = state of the self-amending chain.** Every accepted revision of the running specification is a snapshot, hash-linked to the ledger records and objections that produced it. Rollback is pointwise revision reversed. A5's "timestamp the best next state" becomes a snapshot id.
3. **Firmware = constitution.** Each instance boots from a signed base image carrying the constitution and this template. The image is read-only to every member and writable only through `update_process` with the signer's signature. An agent that could rewrite its own firmware is Nimrod (`tower_of_babel/`). Mnemosyne note for `kb/HISTORY.md`: adopt the modern boot, never lose the origin — TML is the BIOS we migrate from without forgetting.
4. **Reproducibility of the oracle.** tau-lang is built once, in a container, from the pinned commit (`docs/RESOURCES.md`), snapshotted; every verification runs in a fresh clone of that image. The verifier is the same verifier every time.
5. **Nested virtualization as the Tau mirror.** `tau`-typed constants let a specification reason over specifications; a VM that runs VMs is the machine-level image of that. Hypothesis for Phase 2 mapping (M013), not a requirement.

Cost: Stage A-sim fits on the laptop with Podman/Docker and a snapshot-capable filesystem (btrfs or ZFS). Stage B and the oracle need a host with nested virtualization (Q4). Firecracker or plain KVM for members; containers suffice for collectors.

