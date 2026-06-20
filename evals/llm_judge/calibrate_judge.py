#!/usr/bin/env python3
"""Score a system-prompt LLM judge against the human (Max) oracle labels.

Goal: a judge that REPRODUCES the human picks, so the eval can run at scale. For each labeled
card we ask the judge in BOTH A/B orders (de-bias: a flip => tie), give it the SAME context the
human saw (topic + recap + recent turns), and compare its pick to `human_winner`. Spoiled cards
(a candidate came back blank) are skipped.

  export CRUSOE_API_KEY=<crusoe key>
  python evals/llm_judge/calibrate_judge.py --prompt evals/llm_judge/system_prompt/judge_v2.md --model zai/GLM-5.1
"""
import argparse, json, os, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from core.llm import LLM, LLMConfig
from evals import oracle

BASE = "https://api.inference.crusoecloud.com/v1"


def judge_context(r):
    """Mirror what the human annotator saw: guest + blurb, topic, recap, recent turns."""
    blurb = oracle._guest_blurb(r["research"])
    head = f"GUEST: {r['guest']}" + (f" — {blurb}" if blurb else "")
    topic = f"\nTopic: {r['section']}" if r.get("section") else ""
    return f"{head}{topic}\n\n{oracle.context_view(r.get('recap', ''), r['transcript_so_far'])}"


def verdict(raw):
    """(winner in {A,B,TIE}, reason) from the judge's JSON; TIE if unparseable."""
    try:
        obj = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
        w = str(obj.get("winner", "tie")).strip().upper()
        return (w if w in ("A", "B") else "TIE"), str(obj.get("reason", ""))[:200]
    except Exception:
        return "TIE", ""


def judge_card(judge, system, r):
    ctx = judge_context(r)
    def ask(first, second):
        msg = f"CONTEXT:\n{ctx}\n\nCANDIDATE A:\n{first}\n\nCANDIDATE B:\n{second}"
        return verdict(judge.chat([{"role": "system", "content": system},
                                   {"role": "user", "content": msg}], temperature=0.0, max_tokens=3072))
    w1, r1 = ask(r["question_a"], r["question_b"])   # real a in slot A
    w2, r2 = ask(r["question_b"], r["question_a"])   # real a in slot B
    if w1 == "A" and w2 == "B":
        return "a", r1
    if w1 == "B" and w2 == "A":
        return "b", r1
    return "tie", (r1 or r2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", default="evals/llm_judge/system_prompt/judge_v2.md")
    ap.add_argument("--labeled", default="evals/oracle/labeled.jsonl")
    ap.add_argument("--model", default=os.environ.get("JUDGE_MODEL", "deepseek-ai/DeepSeek-V4-Pro"))
    ap.add_argument("--include-spoiled", action="store_true")
    a = ap.parse_args()

    system = Path(a.prompt).read_text()
    judge = LLM(LLMConfig(base_url=BASE, api_key=os.environ["CRUSOE_API_KEY"], model=a.model))
    recs = [json.loads(l) for l in open(a.labeled) if l.strip()]
    cards = [r for r in recs if r["human_winner"] != "tie" and (a.include_spoiled or not r["spoiled"])]

    with ThreadPoolExecutor(max_workers=8) as ex:
        picks = list(ex.map(lambda r: judge_card(judge, system, r), cards))

    from collections import Counter, defaultdict
    agree = 0; ties = 0; by = defaultdict(lambda: [0, 0]); disagreements = []
    for r, (jp, jr) in zip(cards, picks):
        hit = (jp == r["human_winner"])
        agree += hit; ties += (jp == "tie")
        by[r["matchup"]][0] += hit; by[r["matchup"]][1] += 1
        if not hit:
            disagreements.append((r, jp, jr))

    n = len(cards)
    print(f"\nJUDGE: {a.model}   PROMPT: {a.prompt}")
    print(f"AGREEMENT with Max: {agree}/{n} = {agree/n:.0%}   (judge said tie on {ties})")
    print("by matchup:")
    for m in sorted(by):
        h, t = by[m]; print(f"  {m:28} {h}/{t} = {h/t:.0%}")
    print(f"\nDISAGREEMENTS ({len(disagreements)}):")
    for r, jp, jr in disagreements:
        hp = r["human_winner"]
        print(f"  {r['set']}-{r['display_id']} {r['matchup']:24} Max={hp.upper()}->{r['picked']:12} judge={jp.upper()}")
        print(f"     Max:   {r['notes'][:110]}")
        print(f"     judge: {jr[:110]}")

    Path("evals/llm_judge/last_run.json").write_text(json.dumps(
        {"model": a.model, "prompt": a.prompt, "n": n, "agreement": agree / n, "judge_ties": ties,
         "by_matchup": {m: by[m] for m in by},
         "disagreements": [{"id": f"{r['set']}-{r['display_id']}", "matchup": r["matchup"],
                            "max": r["human_winner"], "judge": jp, "judge_reason": jr,
                            "max_note": r["notes"]} for r, jp, jr in disagreements]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
