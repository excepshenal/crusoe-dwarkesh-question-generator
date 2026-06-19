#!/usr/bin/env python3
"""Sweep multiple Crusoe models as the GENERATOR on the same oracle contexts (Method B).

Produces one next-question per (model, context) so we can compare generator models head-to-head
on identical inputs. Used for the model-selection finding in INVESTIGATION.md (GLM-5.1 / DeepSeek
beat the v0 gpt-oss baseline; not pure scale). Shells out to curl (no SDK dependency).

  export TOKEN=<crusoe key>
  python evals/model_sweep.py --items evals/oracle/v1_items.jsonl --ids 1-10 --out evals/model_sweep_results.json
"""
import argparse, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ENDPOINT = os.environ.get("GENERATOR_BASE_URL", "https://api.inference.crusoecloud.com/v1").rstrip("/") + "/chat/completions"
SYSTEM = (REPO / "prompting" / "system.md").read_text().replace("{n}", "5")

DEFAULT_MODELS = [
    "openai/gpt-oss-120b",                  # v0 baseline
    "deepseek-ai/DeepSeek-V4-Pro",          # flagship
    "zai/GLM-5.1",
    "nvidia/NVIDIA-Nemotron-3-Ultra-550B",  # largest
    "Qwen/Qwen3-235B-A22B-Instruct-2507",
    "meta-llama/Llama-3.3-70B-Instruct",    # smaller anchor
]


def user_msg(it):
    tb = it["transcript_so_far"].strip() or "(none yet)"
    return (f"GUEST: {it['guest']}\n\nRESEARCH PREP:\n{it['research'].strip()}\n\n"
            f"TRANSCRIPT SO FAR:\n{tb}\n\nTASK: Next question.")


def call(items, model, did, token):
    body = json.dumps({"model": model, "temperature": 0.7, "max_tokens": 2048,
                       "messages": [{"role": "system", "content": SYSTEM},
                                    {"role": "user", "content": user_msg(items[did])}]})
    p = subprocess.run(["curl", "-sS", "--fail", "--max-time", "240", "-X", "POST", ENDPOINT,
                        "-H", f"Authorization: Bearer {token}", "-H", "Content-Type: application/json",
                        "--data-binary", "@-"], input=body, capture_output=True, text=True)
    if p.returncode != 0:
        return model, did, f"[ERROR {p.returncode}: {p.stderr.strip()[:120]}]"
    try:
        return model, did, (json.loads(p.stdout)["choices"][0]["message"].get("content") or "").strip()
    except Exception as e:
        return model, did, f"[PARSE-ERR {e}: {p.stdout[:120]}]"


def parse_ids(spec):
    if "-" in spec:
        lo, hi = (int(x) for x in spec.split("-")); return [f"{k:03d}" for k in range(lo, hi + 1)]
    return [s.strip().zfill(3) for s in spec.split(",")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", default="evals/oracle/v1_items.jsonl")
    ap.add_argument("--ids", default="1-10", help="display_ids: range '1-10' or list '1,3,5'")
    ap.add_argument("--models", default=",".join(DEFAULT_MODELS))
    ap.add_argument("--out", default="evals/model_sweep_results.json")
    a = ap.parse_args()

    token = os.environ.get("GENERATOR_API_KEY") or os.environ["TOKEN"]
    items = {json.loads(l)["display_id"]: json.loads(l) for l in open(a.items) if l.strip()}
    ids, models = parse_ids(a.ids), a.models.split(",")
    results = {m: {} for m in models}
    tasks = [(m, d) for m in models for d in ids]
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = [ex.submit(call, items, m, d, token) for m, d in tasks]
        for i, f in enumerate(as_completed(futs), 1):
            m, d, o = f.result(); results[m][d] = o
            print(f"  [{i}/{len(tasks)}] {m} {d}: {len(o)} chars", file=sys.stderr)
    Path(a.out).write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"DONE -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
