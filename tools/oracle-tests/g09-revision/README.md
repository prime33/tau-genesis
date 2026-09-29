# G09/G11 experiment — what pointwise revision drops, and who is told

Amendment 8 step 4. Three the example town seeds hold accepted clauses (`seeds_v0.tau`); a fourth party writes a contradicting update to `u` (`update_contradicting.tau`). Question for the oracle: after revision, which of the three clauses survive, and does anything in Tau's own output name the dropped one and its emitter?

Expected on the README's account of `u` (l.1757-1760, INFERENCE until run): local_resident's clause is dropped whenever `i_river_polluted` is true (it contradicts the update); civil_engineer's and example_admin's survive; Tau records nothing about the drop. That is G09 (revision ≠ reconciliation) shown, and the reason D22 puts Reconciling above `u`.

What the run does (`run.py`, once `TAU_ORACLE_HOST` or `TAU_BIN` answers):
1. `sat(seeds)` and `sat(update)` separately (both expected T), `sat(seeds ∧ update)` (expected F: they contradict when the river is polluted).
2. `spec_diff.py seeds_v0.tau revised.tau --oracle`, where `revised.tau` is what the interpreter reports as the current specification after the update step (`this` / `current_spec`). The diff's `dropped` list is the minority report's logical content (D22, F3).
3. Records the interpreter's own output verbatim beside the diff, so the claim "nothing dropped is recorded" is tested, not assumed.

Executing the update through `u` needs the interpreter path (binding `get_interpreter/step/current_spec`, or the REPL `run` with `u` as an input stream): that is F1 v1. Until then steps 1 and the textual diff run; step 2 is marked pending in `result.json`.

## What the run showed, and the two tools that read it (F3 v1)

Observed (FACT, `result.json`, Tau 0.7.0-alpha): the update `always o_priority_sewage[t] = 0` arrived at step 1 and the interpreter's `current_spec` became

    (always u = i_upd && (engineer)) && ((always P = 0 && E = 0 && i_river_polluted = 0) || (always P = 0))

Nothing was dropped outright. The v0 textual diff (still stored under `spec_diff_before_after`) reported the whole statement as `dropped` and the whole new statement as `added`, which is true and useless. The resident's clause `i_river_polluted = 0 || P != 0` and the admin's clause `E = 0 || P != 0` both survive, but only inside the first disjunct, whose own literal `always i_river_polluted[t] = 0` is violated by the input at step 2 (river polluted) — the input that made those clauses matter. The expectation above was wrong on one point: the admin's clause is conditioned too, not kept; `o_endorse` stayed `F` at every step, so that conditioning is visible in the spec, not (in this run) in the outputs. The engineer's clause and the `u = i_upd` route are kept at top level. Tau's stdout records the updated spec and nothing about what was conditioned or for whom (G09 shown; D22's reason).

- `tools/spec_diff.py` v1 parses both specs into `&&` / `||` / `always` / `sometimes` / `!` trees and classifies each conjunct of `before` as `kept`, `conditional` (with the disjunct's literals as `branch_condition` and its input-stream part as `lives_only_if`) or `dropped`, plus `added`; `--emitters emitters.json` attaches seed ids. Inputs: `spec_before.tau`, `spec_after.tau` (the interpreter's `initial_spec` and `steps[1].current_spec`, verbatim); output kept in `spec-diff.json`.
- `tools/minority_report.py` reads `result.json` directly and writes `minority-report.md`: for the step whose spec changed, the update that arrived, the classification per clause with emitter and branch condition, the outputs that flipped between that step and the next under the same inputs (`o_priority_sewage` T→F, steps 1→2), each later step's input checked against the branch literal, and the D22 "Standing" section (who may force a re-hearing).

Reproduce:

    python3 tools/spec_diff.py tools/oracle-tests/g09-revision/spec_before.tau tools/oracle-tests/g09-revision/spec_after.tau \
        --emitters tools/oracle-tests/g09-revision/emitters.json --inputs i_upd,i_river_polluted,i_sewage_contracted
    python3 tools/minority_report.py tools/oracle-tests/g09-revision/result.json \
        --emitters tools/oracle-tests/g09-revision/emitters.json --out tools/oracle-tests/g09-revision/minority-report.md
    python3 -m pytest -q tools/oracle-tests/test_spec_diff.py

Limits (INFERENCE where marked): "present in a branch" is syntactic entailment — a literal of the clause is a conjunct of the branch — so a clause that a branch entails only through algebra would show as `dropped`; `--oracle` replaces the check with `sat(branch && !clause)` but has not been run against the box for this record. `lives_only_if` reports the branch's `always` literal as written; whether the interpreter keeps that branch live after one violating step is the interpreter's semantics (README "starts running as if at time step 0"), not something the diff reads.
