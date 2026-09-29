# dao/template — TEMPLATE v1: constitution, schemas, conformance

`../TEMPLATE.md` is the constitution: the forces, the RULEs, the seeds, the birth declaration. This directory is the part that runs.

- `schema/` — one JSON Schema per record kind (ledger record, decision, variable, consent, anchor, spend, run, forces). Validated on write (F6).
- `tools/room.py` — the runtime, eight verbs: `init`, `affirm`, `object`, `propose`, `decide`, `disclose`, `anchor`, `verify`. Form only; it never judges content.
- `tools/chain.py`, `anchor.py`, `anchor_verify.py`, `boundary_check.py`, `validate.py` — the primitives the verbs use.
- `conformance/` — the suite. A directory is a room iff `room.py verify <dir>` passes. Tests are named for the template line they enforce (S5, S6, F4, F6, F7, F11, F14, B1–B3). Deployment-level tests (append-only attribute, adversarial reads as other unix users) skip unless the room is deployed and say so.

Every DECIDE records the suite version it passed under (`conformance_version`). A room's private ops holds its instance; this directory holds what every instance shares.
