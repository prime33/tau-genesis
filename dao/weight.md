# dao/weight.md — weight, direction, and the contest procedure

**Status:** draft v0.1, 2026-09-26, companion, from the program's decisions (private record). The four numbered points under "For the record (the author)" are the author's and binding. Everything under "Function" is the strategic instance's design consequence, drafted here as v0 for the author's veto.

## the author's record (binding)

1. Every stakeholder has presence in the platform, in time, with identity and agency — residents, institutions, businesses, press, the river and the Sierra.
2. Not one seed, one vote. Decisions are assessed by weight — talent, information, knowledge, wisdom — with direction, so each next state of the self-amending chain is timestamped as the best-assessed step, not the most-voted one.
3. Roles are themselves evaluated. Agents are judged on their record.
4. Greater than the sum of its parts. The reconciled state is not the aggregate of votes.

## RULEs

- **Computed, never assigned.** No person and no collective assigns weight. It is a function of the seed's ledger record in a domain.
- **Per domain, no global weight.** The civil engineer is high on feasibility, ordinary on lived priority; the resident the reverse.
- **Floor, not zero.** A seed with no record has the floor weight. Affirming records it in full regardless. Weight governs Reconciling, never Affirming.
- **Timestamped, revisable, visible.** Every weight value carries the ledger records it was computed from and the time. Old values are kept.
- **Contestable with grounds.** Any agent may object to a weight, citing records. The objection is logged in `minority/` whether or not it prevails.
- **The function is Negating's first target.** Before any candidate is weighed, the objector attacks `weight()` itself: what it rewards, what it cannot see.
- **Separate seat.** Role evaluation runs in the role-audit seat, never in the listener and never in a reconciler.

## Domains (v0, DEFAULT — instance may extend with a logged reason)

`feasibility` · `lived_priority` · `public_health` · `hydrology` · `heritage` · `budget` · `procedure` (what the administration can lawfully do) · `record` (accuracy of what the seed has stated before).

A domain is a label on a ledger record's claims. Records get domain labels from the collectors (mechanical, by surface) and from Reconciling (by reading). Labels are themselves records and contestable.

## Function (v0 — strategic instance's proposal, the author may veto)

For a seed `s`, domain `d`, time `t`:

```
weight(s, d, t) = floor + g( held(s,d,t), corrected(s,d,t), provenance(s,d,t) )
```

where, over the seed's records in `d` up to `t`:

- `held` — claims the seed made that later records did not contradict and that a signed candidate relied on;
- `corrected` — claims the seed made that it later corrected itself (counts *for* the seed: self-correction is record quality) versus claims corrected by others (counts against);
- `provenance` — the fraction of the seed's claims that carry a resolvable source.

`g` is monotone in `held` and `provenance`, decreasing in others-corrected, and bounded so that no single seed can outweigh the floor-weight sum of the seeds in the room (the Socrates objection cuts both ways: no oligarchy of the record either). The concrete shape of `g` is **SLOT**: it is the first thing the objector attacks and the first thing Phase 2 must ask of Tau (does IDNI's opinion map carry weight and direction, or only logical agreement? — `docs/reconciliation/mapping.md`, own row).

**Direction.** A weight value carries a sign per candidate: the seed's record in `d` supports or opposes the candidate's claims in `d`. Reconciling computes the next state from weighted, directed positions, then writes the candidate *and* the minority report; the report carries every opposing position that the weight did not carry.

**Natural seeds.** The river and the Sierra accrue weight in `hydrology` and `heritage` from records *about* them (hydrology, incidents, closures, what Kogi and residents say). Who speaks for them is **SLOT** (`TEMPLATE.md` §8).

## Contest procedure

1. An agent files an objection to a weight: `{seed, domain, value, records_cited, grounds}` to `minority/weights/`.
2. The role-audit seat re-computes with the objection's records included and publishes both values with the diff.
3. If the values differ, the objection is `upheld` and the new value stands; if not, it is `overruled` and stays logged. Either way the objection is part of the record.
4. A signer may not set a weight. A signer may order a re-computation with stated grounds; that order is a decision (`TEMPLATE.md` §5).

## What this file does not do

It does not compute anything yet. `gates/weight.py` in an instance implements v0 once the ledger has enough records for `held` to mean something; until then every seed sits at the floor and Reconciling says so in each candidate.
