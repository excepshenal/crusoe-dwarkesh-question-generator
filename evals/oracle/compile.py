#!/usr/bin/env python3
"""Compile the human (Max) oracle labels across batches into one dataset.

Joins each batch's blind items (`{set}_items.jsonl`) with Max's picks
(`{set}_answers_max.csv`) and writes, under evals/oracle/:
  - labeled.jsonl  machine-readable: every labeled card + human_winner, picked, matchup, spoiled.
  - labeled.md     human-readable: context + both candidates + revealed ground truth + Max's pick.

`spoiled` flags cards where a candidate came back blank/fragment (a generation token-cap bug,
now fixed) so the pick was forced — these are excluded from judge scoring downstream.

  python evals/oracle/compile.py            # default sets: v1 (first 10), v2 (20)
"""
import argparse, csv, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from evals import oracle

ORACLE = Path(__file__).resolve().parent


def load_items(p):
    return {it["display_id"]: it for it in (json.loads(l) for l in open(p) if l.strip())}


def load_picks(p):
    out = {}
    for row in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
        pick = (row.get("pick (a/b/tie)") or "").strip().lower()
        if pick in ("a", "b", "tie"):
            out[row["id"].zfill(3)] = (pick, (row.get("confidence (1-3)") or "").strip(),
                                       (row.get("notes") or "").strip())
    return out


def cat(src):  # human-friendly source category
    s = src.lower()
    if "dwarkesh" in s: return "Dwarkesh"
    if "qwen" in s: return "qwen3-235b"
    if "glm" in s: return "glm-5.1"
    if "gpt-oss" in s: return "gpt-oss-120b"
    return src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sets", default="v1,v2", help="comma-separated batch prefixes under evals/oracle/")
    a = ap.parse_args()

    records = []
    for setname in a.sets.split(","):
        items = load_items(ORACLE / f"{setname}_items.jsonl")
        picks = load_picks(ORACLE / f"{setname}_answers_max.csv")
        for did, (pick, conf, notes) in sorted(picks.items()):
            it = dict(items[did])
            qa, qb = it["question_a"], it["question_b"]
            spoiled = min(len(qa.strip()), len(qb.strip())) < 40   # a blank/fragment candidate
            picked_src = it["source_a"] if pick == "a" else (it["source_b"] if pick == "b" else "tie")
            it.update(set=setname, human_winner=pick, confidence=conf, notes=notes,
                      spoiled=spoiled, picked=cat(picked_src) if pick != "tie" else "tie",
                      matchup=" vs ".join(sorted({cat(it["source_a"]), cat(it["source_b"])})))
            records.append(it)

    (ORACLE / "labeled.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n")

    md = ["# Oracle — compiled human labels (Max)", "",
          f"{len(records)} labeled cards from batches: {a.sets}.",
          "Ground truth (which model wrote which) is revealed here — this file is NOT blind.",
          "⚠️ = a candidate came back blank/fragment (generation bug, now fixed); the pick was forced "
          "— excluded from judge calibration.", ""]
    for r in records:
        flag = " ⚠️ SPOILED" if r["spoiled"] else ""
        ctx = oracle.context_view(r.get("recap", ""), r["transcript_so_far"]).replace("\n", "\n> ")
        win = "tie" if r["human_winner"] == "tie" else f'{r["human_winner"].upper()} → **{r["picked"]}**'
        md += [f"## {r['set']}-{r['display_id']}  ·  {r['guest']}  ·  _{r['matchup']}_{flag}", "",
               "**Context:**", "", f"> {ctx}", "",
               f"**A** ({cat(r['source_a'])}): {r['question_a'] or '*(blank)*'}", "",
               f"**B** ({cat(r['source_b'])}): {r['question_b'] or '*(blank)*'}", "",
               f"**Max:** {win}  ·  confidence {r['confidence'] or '—'}", "",
               f"> _{r['notes']}_" if r["notes"] else "", "", "---", ""]
    (ORACLE / "labeled.md").write_text("\n".join(md))
    print(f"compiled {len(records)} cards ({sum(r['spoiled'] for r in records)} spoiled) -> evals/oracle/labeled.{{jsonl,md}}")


if __name__ == "__main__":
    main()
