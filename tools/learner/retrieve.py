#!/usr/bin/env python3
"""Learner v1, step 0 (docs/learner-v1.md §8): retrieval and prompt sizing. NO generation.

  python3 tools/learner/retrieve.py --dry-run [--provider anthropic|do] [--fragment <concept>] [--k 5] [--out <json>]

Provider `do` = DigitalOcean Serverless Inference (OpenAI-format, base https://inference.do-ai.run/v1, key DO_INFERENCE_KEY).
It has no count_tokens, so sizing is a 1-output-token chat call on anthropic-claude-haiku-4.5 (usage.prompt_tokens),
plus 3 fragments repeated on anthropic-claude-opus-5 to calibrate the tokenizer ratio. Cost of a full dry-run ≈ $2.

For each v1 fragment (proposal constructs defined in the files listed in FRAGMENT_FILES, in curriculum
order): pull the author's definition verbatim from docs/proposal/concepts.md, its mapping.md rows, the LANGUEDOC
decided rows that mention its terms, the k nearest IDNI chunks from kb/tau.db (local embeddings), 3
corpus items by capability tag with sat=T, the grammar, the D19 forbidden list; assemble the exact
system + user messages Learner v1 would send; count tokens with the API (authenticated, no generation).
Writes a JSON report with per-fragment sizes and the stable-prefix size. The key is read by the SDK from
the environment (load it from .env in the calling shell); it is never printed or written.
"""
import argparse, json, os, re, sys, time
PUB = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OPS = os.environ.get("TAU_OPS", os.path.join(os.path.dirname(PUB), "tau-genesis-ops"))
sys.path.insert(0, os.path.join(OPS, "kb"))
MODEL = "claude-opus-5"
FRAGMENT_FILES = [  # curriculum order (learner-v1.md §3)
    "streams/core/valid_thought.tau", "constitution/update_process.tau", "constitution/consensus_logic.tau",
    "amendments/amendment_001_freedom_of_semantic_expression.tau", "amendments/amendment_002_semantic_resonance_and_integration.tau",
    "amendments/amendment_003_babel_antipattern.tau", "streams/amendments/freedom_of_semantic_expression.tau",
    "streams/amendments/semantic_resonance_and_integration.tau", "streams/amendments/babel_antipattern_principle.tau",
    "streams/policy/example/river_town_priority.tau", "streams/civic/example/endorsement_from_town_admin.tau",
    "streams/civic/example/endorsement_from_engineer.tau", "streams/civic/example/endorsement_from_resident.tau",
]
FORBIDDEN = ["being", "alignment_with_being"]
IDIOMS = (  # language facts measured on the oracle, not answers to any test; added after the step 1 miss (evaluates_lineage)
    "- A stream that refers to its own past (`o[t-1]`) leaves step 0 to the solver unless the spec fixes it. Fix it with an explicit "
    "initial conjunct INSIDE the temporal scope: `always (o[0] = i[0] && o[t] = <formula over o[t-1], i[t]>)`. A `[t = 0] ->` guard "
    "normalises away and does not do this.\n"
    "- A constant for a `tau`-typed stream in that position is written `0` / `1` (e.g. `o[0] = 0`), not `F` / `T`.\n"
    "- Demo forms: `o1[t] = o1[t-1] ^ o1[t-2] && o1[0] = 1 && o1[1] = 1` (demo 3.1, sbf, sat T); "
    "`o2[0] = i2[0] && o2[t] = o2[t-1] + i2[t]` (demo 3.4, bitvector counter).\n"
    "- Boolean truth of a term is `!= 0`; `&` `|` `'` are and/or/not on terms; several statements are joined with `&&` inside ONE `always (...)`. "
    "Two `always` blocks joined with `&&` are rejected at this pin ('Nesting of temporal quantifiers is not allowed'); use one scope. "
    "Do not add redundant 'sanity' conjuncts restating an equation as implications: they cannot help and one made a correct spec unsatisfiable.\n"
    "- Every output stream is reported by the interpreter, so a spec may declare and constrain several outputs in one formula.\n"
    "- If ANY output's past is referenced (`o1[t-1]`), then EVERY output needs its own `[0]` conjunct, including outputs without a lookback: "
    "otherwise step 0 of those outputs is left to the solver and NO inputs are requested at step 0 (measured: `o2[t] = o1[t] & o1[t-1]` with "
    "`o1[t] = i[t]` gave o1[0] = F, inputs unasked; adding `o1[0] = i[0]` fixed it). Input lookbacks (`i[t-1]`) do not have this problem."
)
TAG_RULES = [("always", "temporal_always"), ("sometimes", "temporal_sometimes"), ("stream", "streams"), ("`u`", "pointwise_revision_u"),
             ("pointwise", "pointwise_revision_u"), ("this", "this_stream"), ("recurrence", "recurrence"), ("`tau`", "tau_type"),
             ("constant", "tau_constant"), ("bv[", "bitvector"), ("bitvector", "bitvector"), ("ADT", "adt"), ("sat", "solver")]


def concepts():
    """Parse docs/proposal/concepts.md into {name: {defined_in:[paths], definition:str, block:str}}."""
    txt = open(os.path.join(PUB, "docs/proposal/concepts.md")).read()
    out = {}
    for m in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", txt, re.S | re.M):
        name, block = m.group(1).strip(), m.group(2)
        d = re.search(r"\*\*Defined in:\*\*(.*)", block)
        paths = re.findall(r"`([^`]+)`", d.group(1)) if d else []
        q = re.search(r"\*\*the author's definition:\*\*\n(.*?)(?=\n\*\*|\Z)", block, re.S)
        out[name] = {"defined_in": paths, "definition": (q.group(1).strip() if q else ""), "block": block}
    for name, entry in stream_concepts().items():   # streams not in the harvest (e.g. the ILLUSTRATIVE example): parsed from the files
        out.setdefault(name, entry)
    return out


def stream_concepts():
    """Concept entries parsed straight from `.tau` stream files in FRAGMENT_FILES: every `define "x" as:` block, plus the
    stream's own name carrying its if/then rule. Lets the learner run on a stream the 2025 harvest never saw."""
    out = {}
    for rel in FRAGMENT_FILES:
        path = os.path.join(PUB, rel)
        if not os.path.exists(path): continue
        txt = open(path, encoding="utf-8").read()
        for m in re.finditer(r'define "([A-Za-z_][A-Za-z0-9_]*)" as:\n((?:[ \t]+.*\n?)+)', txt):
            body = " ".join(l.strip() for l in m.group(2).splitlines())
            out[m.group(1)] = {"defined_in": [rel], "definition": f"> {body}", "block": m.group(0)}
        rule = re.search(r"(?ms)^\s*if \(.*?\)\s*\n?\s*then \(.*?\)(?:\s*therefore \(.*?\))?", txt)
        stem = os.path.splitext(os.path.basename(rel))[0]
        if stem not in out:
            body = rule.group(0) if rule else "\n".join(l for l in txt.splitlines() if l.strip() and not l.startswith("#"))
            out[stem] = {"defined_in": [rel], "definition": "> " + " ".join(l.strip() for l in body.splitlines()), "block": body}
    return out


def mapping_rows(name):
    txt = open(os.path.join(PUB, "docs/reconciliation/mapping.md")).read()
    return [l for l in txt.splitlines() if l.startswith("| M") and re.search(r"\b" + re.escape(name) + r"\b", l)]


def languedoc_rows(terms):
    txt = open(os.path.join(PUB, "docs/LANGUEDOC.md")).read()
    rows = [l for l in txt.splitlines() if l.startswith("| **") and "decided" in l]
    return [l for l in rows if any(t.lower() in l.lower() for t in terms)]


def kb_search(query, k):
    """Nearest chunks from the private knowledge base (kb/tau.db in the ops repository). Without it, retrieval is empty
    and the learner runs as the ablation's bare condition (docs/tau-curriculum.md, Ablation)."""
    if not os.path.exists(os.path.join(OPS, "kb", "tau.db")):
        return []
    import sqlite3, numpy as np
    from build import Embedder
    c = sqlite3.connect(os.path.join(OPS, "kb/tau.db")); c.row_factory = sqlite3.Row
    q = Embedder().encode([query])[0]
    rows = c.execute("select ch.id, ch.text, ch.embedding, d.title, d.type, ch.start_line, ch.end_line from chunk ch join document d on d.id=ch.doc_id where ch.embedding is not null and d.pole='idni'").fetchall()
    E = np.frombuffer(b"".join(r["embedding"] for r in rows), dtype=np.float32).reshape(len(rows), -1)
    sims = E @ q
    return [{"chunk": rows[i]["id"], "sim": float(sims[i]), "title": rows[i]["title"], "type": rows[i]["type"], "text": rows[i]["text"]} for i in np.argsort(-sims)[:k]]


def items_by_tag(tags, n=3):
    p = os.path.join(OPS, "kb/tau-corpus/items.jsonl")
    if not os.path.exists(p):
        return []
    items = [json.loads(l) for l in open(p)]
    hits = [it for it in items if it.get("sat") == "T" and it.get("parse_ok") and set(it.get("capability_tags", [])) & set(tags)]
    hits.sort(key=lambda it: -len(set(it.get("capability_tags", [])) & set(tags)))
    return hits[:n]


FAMILY_A_COMMIT = "c55ce7c~1"  # D20: the deleted Family A amendment files are canonical; the tree holds only the v3 form
_family_a_cache = {}


def family_a_text(entry):
    """The Family A file(s) a concept was defined in, verbatim from git (short files), or None."""
    paths = [p.split(":", 2)[2] for p in entry.get("defined_in", []) if p.startswith(f"git:{FAMILY_A_COMMIT}:")]
    out = []
    for path in paths:
        if path not in _family_a_cache:
            local = os.path.join(PUB, "docs", "proposal", "family-a", os.path.basename(path))  # preserved in the tree
            if os.path.exists(local):
                _family_a_cache[path] = open(local, encoding="utf-8").read()
            else:
                import subprocess
                r = subprocess.run(["git", "-C", PUB, "show", f"{FAMILY_A_COMMIT}:{path}"], capture_output=True, text=True)
                _family_a_cache[path] = r.stdout if r.returncode == 0 else None
        if _family_a_cache[path]:
            out.append(f"### {path} (Family A, canonical under D20)\n" + _family_a_cache[path].strip())
    return "\n\n".join(out) or None


def build(name, c, k, ablate=None):
    """ablate="bare": no retrieval sections and no idioms block (learner-v1.md §4 baseline: grammar + decisions + fragment only).
    ablate="noretrieval": idioms kept, retrieval sections removed (the split condition)."""
    entry = c[name]
    fa = family_a_text(entry)
    definition = entry["definition"]
    if fa:
        definition = ("LANGUEDOC D20: the Family A text is canonical; the v3 block quoted after it (streams/amendments/*.tau, the "
                      "head-conjunction rewrite) is a known-wrong translation kept for history (G03). Translate the Family A clause.\n\n"
                      + fa + "\n\n### v3 block (not canonical)\n" + definition)
    rows = mapping_rows(name)
    tags = sorted({t for kw, t in TAG_RULES for r in rows if kw in r}) or ["streams", "temporal_always"]
    terms = [name] + re.findall(r"`([a-z_]+)`", entry["block"])[:6]
    ld = languedoc_rows(terms)
    query = f"{name}: {entry['definition']} {' '.join(rows)[:600]}"
    chunks = kb_search(query, k)
    items = items_by_tag(tags)
    gp = os.path.join(OPS, "kb/tau-corpus/grammar.ebnf")  # transcription of the README grammar: research use, kept private (D10)
    grammar = open(gp).read() if os.path.exists(gp) else ("(grammar not shipped: transcribe the Syntax section of the tau-lang README "
                                                          "at commit 3badb21 into kb/tau-corpus/grammar.ebnf of a sibling ops directory, or set TAU_OPS)")
    system = (
        "You translate one clause of a constitutional proposal (pseudocode) into a Tau Language v0.7 specification. "
        "The oracle decides; you propose. Rules: use only the grammar below; never use the identifiers "
        f"{', '.join(FORBIDDEN)} (D19); declare every input/output stream with its type; give a test of 3-5 steps with named "
        "inputs and the exact expected outputs; list every term of the clause you could not place under `unmapped` instead "
        "of inventing a construct. Answer as JSON: {spec, streams, test:{steps:[{...}], expected:{...}}, claims:[...], unmapped:[...]}.\n\n"
        "## Tau grammar (README, transcribed)\n" + grammar +
        ("" if ablate == "bare" else "\n\n## Idioms verified by the oracle at pin 3badb21 (2026-09-29)\n" + IDIOMS) +  # noretrieval keeps the idioms
        "\n\n## Vocabulary decisions in force (LANGUEDOC)\n" + "\n".join(ld or ["(none for these terms)"])
    )
    user = (
        f"## Fragment: `{name}` — defined in {', '.join(entry['defined_in'])}\n{definition}\n\n"
        "## Mapping (Phase 2)\n" + ("\n".join(rows) or "(no row)") + "\n\n" +
        ("" if ablate in ("bare", "noretrieval") else
         "## Nearest verified Tau material\n" + "\n\n".join(f"[{h['chunk']} {h['type']} {h['title']} sim={h['sim']:.2f}]\n{h['text'][:1500]}" for h in chunks) +
         "\n\n## Corpus items by capability " + ",".join(tags) + "\n" + "\n".join(f"- {it['id']} ({it['source']}): {it['text'][:300]}" for it in items) + "\n\n") +
        "Produce the specification, its streams, the test, the claims, and `unmapped`."
    )
    return system, user, {"tags": tags, "chunks": [] if ablate else [h["chunk"] for h in chunks], "items": [] if ablate else [it["id"] for it in items],
                          "languedoc_rows": len(ld), "mapping_rows": len(rows), "ablate": ablate}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--provider", default="anthropic", choices=["anthropic", "do", "offline"]); ap.add_argument("--fragment"); ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--out", default=os.path.join(OPS, "kb/learner/dryrun-%s.json" % time.strftime("%Y-%m-%d")))
    a = ap.parse_args()
    if not a.dry_run: sys.exit("only --dry-run exists in step 0 (no generation)")
    c = concepts()
    names = [a.fragment] if a.fragment else [n for n, e in c.items() if any(p.replace("git:c55ce7c~1:", "") in FRAGMENT_FILES or p in FRAGMENT_FILES for p in e["defined_in"])]
    report = {"provider": a.provider, "model": MODEL, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "k": a.k, "fragments": []}
    if a.provider == "anthropic":
        from anthropic import Anthropic
        ws = os.environ.get("ANTHROPIC_WORKSPACE_ID")
        client = Anthropic(default_headers={"anthropic-workspace-id": ws}) if ws else Anthropic()
        def count(system, user, model=MODEL):
            return client.messages.count_tokens(model=model, system=system, messages=[{"role": "user", "content": user}]).input_tokens, 0.0
    elif a.provider == "offline":
        # No API: characters / 3.6 (INFERENCE: a rough English+code ratio; Opus 5's tokenizer runs ~1-1.35x denser
        # than older ones, so treat these as a lower bound). Gives the distribution before any tier or key exists.
        def count(system, user, model="offline"):
            return int((len(system) + len(user)) / 3.6), 0.0
    else:
        from openai import OpenAI
        client = OpenAI(base_url="https://inference.do-ai.run/v1", api_key=os.environ["DO_INFERENCE_KEY"])
        PRICE_IN = {"anthropic-claude-haiku-4.5": 1.0, "anthropic-claude-opus-5": 5.0}
        def count(system, user, model="anthropic-claude-haiku-4.5"):
            r = client.chat.completions.create(model=model, max_tokens=1, messages=[{"role": "system", "content": system}, {"role": "user", "content": user}])
            n = r.usage.prompt_tokens
            return n, round(n / 1e6 * PRICE_IN[model] + 1 / 1e6 * PRICE_IN[model] * 5, 5)
    spent = 0.0; prefix_counted = None; calib = []
    for i, n in enumerate(names):
        system, user, meta = build(n, c, a.k)
        if prefix_counted is None:
            prefix_counted, usd = count(system.split("## Vocabulary decisions")[0], "x"); spent += usd
            report["stable_prefix_tokens"] = prefix_counted
        tot, usd = count(system, user); spent += usd
        rec = {"fragment": n, "defined_in": c[n]["defined_in"], "input_tokens": tot, **meta}
        if a.provider == "do" and i < 3:
            tot5, usd5 = count(system, user, "anthropic-claude-opus-5"); spent += usd5
            rec["input_tokens_opus5"] = tot5; calib.append(tot5 / tot if tot else 1.0)
        report["fragments"].append(rec)
        print(f"{i+1:3d}/{len(names)} {tot:6d} tok  {n}  tags={','.join(meta['tags'])}", flush=True)
    if calib:
        ratio = sum(calib) / len(calib); report["opus5_over_haiku_ratio"] = round(ratio, 3)
        for f in report["fragments"]: f["input_tokens_opus5_est"] = int(f.get("input_tokens_opus5") or f["input_tokens"] * ratio)
        prefix_counted = int(prefix_counted * ratio)
    report["dry_run_usd"] = round(spent, 4)
    toks = [f.get("input_tokens_opus5_est", f["input_tokens"]) for f in report["fragments"]]
    report["summary"] = {"fragments": len(toks), "min": min(toks), "median": sorted(toks)[len(toks)//2], "max": max(toks), "sum": sum(toks),
                         "fresh_per_call_median": sorted(toks)[len(toks)//2] - prefix_counted,
                         "est_usd_first_attempt_uncached": round(sum(toks) / 1e6 * 5 + len(toks) * 3000 / 1e6 * 25, 2),
                         "est_usd_first_attempt_prefix_cached": round((sum(toks) - len(toks) * prefix_counted) / 1e6 * 5 + len(toks) * 3000 / 1e6 * 25 + len(toks) * prefix_counted / 1e6 * 0.5, 2)}
    os.makedirs(os.path.dirname(a.out), exist_ok=True); json.dump(report, open(a.out, "w"), indent=1)
    print(json.dumps(report["summary"], indent=1)); print("report:", a.out)


if __name__ == "__main__":
    main()
