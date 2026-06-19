#!/usr/bin/env python3
"""Build a blind oracle batch pitting two models against each other and against real Dwarkesh.

Picks fresh held-out contexts (clean next-question cuts, mid-interview, spread across guests),
EXCLUDING any context/answer used in prior batches (so a human re-labeling can't recognize a
repeated card). Generates each model's next-question, then lays out three strata:
  - model_a vs model_b      (tool_vs_tool — clean preference, no Dwarkesh to recognize)
  - model_a vs Dwarkesh     (vs_tool)
  - model_b vs Dwarkesh     (vs_tool)
Writes {out}_items.jsonl (hidden truth) + {out}_sheet.md (blind) + {out}_answers.csv (blank).

  export TOKEN=<crusoe key>
  python evals/oracle/build_batch.py --out evals/oracle/v3 --exclude v1,v2

This reproduces the v2 recipe (defaults: qwen vs glm, 10/5/5). One generation per cell, temp 0.7
(deploy setting), no cherry-picking — an honest sample of each generator.
"""
import argparse, json, os, random, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from data import dataset
from evals import oracle
from core.llm import LLM, LLMConfig

ORACLE = Path(__file__).resolve().parent


def short(model):  # model id -> friendly ground-truth label
    s = model.lower()
    return "qwen3-235b" if "qwen" in s else "glm-5.1" if "glm" in s else "gpt-oss-120b" if "gpt-oss" in s else model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="prefix, e.g. evals/oracle/v3")
    ap.add_argument("--model-a", default="Qwen/Qwen3-235B-A22B-Instruct-2507")
    ap.add_argument("--model-b", default="zai/GLM-5.1")
    ap.add_argument("--n-ab", type=int, default=10, help="model_a vs model_b cards")
    ap.add_argument("--n-a-dw", type=int, default=5, help="model_a vs Dwarkesh cards")
    ap.add_argument("--n-b-dw", type=int, default=5, help="model_b vs Dwarkesh cards")
    ap.add_argument("--exclude", default="v1,v2", help="prior batch prefixes whose contexts to avoid")
    ap.add_argument("--min-turns", type=int, default=6, help="min prior turns (mid-interview, not an opener)")
    ap.add_argument("--seed", type=int, default=20260619)
    a = ap.parse_args()

    rng = random.Random(a.seed)
    base = os.environ.get("GENERATOR_BASE_URL", "https://api.inference.crusoecloud.com/v1")
    token = os.environ.get("JUDGE_API_KEY") or os.environ.get("GENERATOR_API_KEY") or os.environ["TOKEN"]
    A = LLM(LLMConfig(base_url=base, api_key=token, model=a.model_a))
    B = LLM(LLMConfig(base_url=base, api_key=token, model=a.model_b))
    SA, SB, DW = short(a.model_a), short(a.model_b), "dwarkesh"
    n_total = a.n_ab + a.n_a_dw + a.n_b_dw

    # exclude contexts + Dwarkesh answers a human could have already seen
    seen_ctx, seen_q = set(), set()
    for pfx in [p for p in a.exclude.split(",") if p]:
        for it in (json.loads(l) for l in open(ORACLE / f"{pfx}_items.jsonl") if l.strip()):
            seen_ctx.add(it["transcript_so_far"]); seen_q |= {it["question_a"], it["question_b"]}

    _, heldout = dataset.split_slugs()
    pool = []
    for slug in heldout:
        t = dataset.load_transcript(slug)
        for ex in dataset.next_question_examples(t):
            if (dataset.is_clean_question(ex.target) and ex.transcript_so_far not in seen_ctx
                    and ex.target not in seen_q and len(oracle._split_turns(ex.transcript_so_far)) >= a.min_turns):
                pool.append(ex)
    rng.shuffle(pool)

    picked, per_guest, used = [], {}, set()
    for cap in (1, 2, 3, 4):
        for ex in pool:
            if len(picked) == n_total: break
            if ex.transcript_so_far in used or per_guest.get(ex.guest, 0) >= cap:
                continue
            picked.append(ex); used.add(ex.transcript_so_far); per_guest[ex.guest] = per_guest.get(ex.guest, 0) + 1
        if len(picked) == n_total: break
    assert len(picked) == n_total, f"only {len(picked)}/{n_total} fresh contexts available"

    def gen(ex):
        return (ex, oracle._tool_question(A, ex.guest, ex.research, ex.transcript_so_far),
                oracle._tool_question(B, ex.guest, ex.research, ex.transcript_so_far),
                oracle.summarize_context(ex.transcript_so_far, A))
    with ThreadPoolExecutor(max_workers=12) as exr:
        gens = list(exr.map(gen, picked))

    order = list(range(n_total)); rng.shuffle(order)
    kind = {i: ("ab" if r < a.n_ab else "adw" if r < a.n_ab + a.n_a_dw else "bdw") for r, i in enumerate(order)}

    items = []
    for i, (ex, qa, qb, recap) in enumerate(gens):
        ctx = dict(slug=ex.slug, guest=ex.guest, mode="next-question", research=ex.research,
                   transcript_so_far=ex.transcript_so_far, section=ex.section, recap=recap)
        if kind[i] == "ab":
            q1, q2, s1, s2, exp = oracle._place(rng, qa, qb, SA, SB, False); strat = "tool_vs_tool"
        elif kind[i] == "adw":
            q1, q2, s1, s2, exp = oracle._place(rng, ex.target, qa, DW, SA, False); strat = "vs_tool"
        else:
            q1, q2, s1, s2, exp = oracle._place(rng, ex.target, qb, DW, SB, False); strat = "vs_tool"
        items.append(oracle.OracleItem(f"{ex.slug}-{strat}-{kind[i]}-{i}", strat, **ctx,
                                       question_a=q1, question_b=q2, source_a=s1, source_b=s2, expected=exp))

    jl, md, ans = oracle.write(items, a.out)
    print(f"wrote {len(items)} cards across {len(per_guest)} guests:\n  {jl}\n  {md}\n  {ans}")


if __name__ == "__main__":
    main()
