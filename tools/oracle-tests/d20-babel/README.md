# D20 toy — Family A vs v3, through the oracle

Amendment 8, D20: before the author signs the Family-A restoration, F1 runs both forms of the Babel amendment's clause 3 and the log records both outputs with the tau-lang commit hash.

- `family_a.tau` — the rule as the author wrote it: an obfuscating act is prohibited; compliance is its absence.
- `v3.tau` — the transcompiler's head-conjunction form: the predicate named for the norm is true exactly when the act obfuscates and isolates.
- `run.py` — conjoins each with the violation query `sometimes ( i_obf[t] & i_iso[t] & o_complies[t] )` and asks `sat`. Expected: Family A **F**, v3 **T**. Writes `result.json`.

Run once the oracle exists (`TAU_ORACLE_HOST=tau@<ip>` or `TAU_BIN=...`): `python3 tools/oracle-tests/d20-babel/run.py`. The specs' syntax is unverified until then; a parse error is itself a recorded result, not a reason to edit the claim.
