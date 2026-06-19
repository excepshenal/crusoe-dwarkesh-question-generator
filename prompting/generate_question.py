#!/usr/bin/env python3
"""Test the Dwarkesh question-generator prompt against the Crusoe inference endpoint.

No Python installs needed (stdlib + curl, which ships on macOS/Linux). Set your key, then:

  export CRUSOE_API_KEY=...                       # the key you were given
  # next-question mode — pass the conversation so far (a real interview subset):
  python generate_question.py --guest "Dario Amodei" \
      --research ../data/research/dario-amodei-2.md \
      --transcript ../data/transcript_subsets/dario-amodei-2-turn-40.json
  # prep mode — research only, get N starter questions:
  python generate_question.py --guest "Tyler Cowen" --research ../data/research/tyler-cowen-3.md

--research = the guest dossier. --transcript = the conversation so far, either a
data/transcript_subsets/*.json file (a real interview truncated to a turn) or a plain
.txt of speaker-labeled lines:
  Dwarkesh Patel: ...
  Dario Amodei: ...
(omit --transcript for prep mode). Prints the model's question(s).

--model picks the generator (default: qwen3-235b, the strongest model we can fine-tune).
In our eval, zai/GLM-5.1 is the strongest overall — try it with `--model zai/GLM-5.1`.
See MODELS below (or --help) for the full list available on the endpoint.
"""
import argparse, json, os, subprocess

ENDPOINT = "https://api.inference.crusoecloud.com/v1/chat/completions"
# Models available on the Crusoe inference endpoint (GET /v1/models). GLM-5.1 is the
# strongest overall; Qwen3-235B is the strongest we can fine-tune, so it's the default.
MODELS = [
    "Qwen/Qwen3-235B-A22B-Instruct-2507", "zai/GLM-5.1", "deepseek-ai/DeepSeek-V4-Pro",
    "deepseek-ai/Deepseek-V4-Flash", "deepseek-ai/DeepSeek-V3-0324",
    "nvidia/NVIDIA-Nemotron-3-Ultra-550B", "nvidia/NVIDIA-Nemotron-3-Super-120B-A12B",
    "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B", "nvidia/Nemotron-3-Nano-Omni-Reasoning-30B-A3B",
    "openai/gpt-oss-120b", "meta-llama/Llama-3.3-70B-Instruct", "google/gemma-4-31b-it",
    "yutori/n1.5",
]
DEFAULT_MODEL = "Qwen/Qwen3-235B-A22B-Instruct-2507"
SYSTEM = open(os.path.join(os.path.dirname(__file__), "system.md")).read()


def load_transcript(path):
    """Render the conversation-so-far to speaker-labeled text. A .json file (our
    transcript_subsets format, or any {turns:[{speaker,text}]}/[...]) is rendered;
    anything else is read as raw text."""
    raw = open(path).read()
    if not path.endswith(".json"):
        return raw
    data = json.loads(raw)
    turns = data["turns"] if isinstance(data, dict) else data
    return "\n\n".join(f"{t['speaker']}: {t['text']}" for t in turns)


def user_message(guest, research, transcript, n):
    if transcript.strip():
        task, tblock = "Next question.", transcript.strip()
    else:
        task, tblock = f"Generate {n} candidate questions for prep.", "(none — pre-interview)"
    return (f"GUEST: {guest}\n\nRESEARCH PREP:\n{research.strip()}\n\n"
            f"TRANSCRIPT SO FAR:\n{tblock}\n\nTASK: {task}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guest", required=True)
    ap.add_argument("--research", required=True, help="path to the guest dossier (markdown/text)")
    ap.add_argument("--transcript", default=None, help="path to conversation-so-far (omit for prep mode)")
    ap.add_argument("--n", type=int, default=6, help="number of starter questions in prep mode")
    ap.add_argument("--model", default=DEFAULT_MODEL, choices=MODELS,
                    help="generator model (default: qwen3-235b; zai/GLM-5.1 is strongest)")
    a = ap.parse_args()

    research = open(a.research).read()
    transcript = load_transcript(a.transcript) if a.transcript else ""
    system = SYSTEM.replace("{n}", str(a.n))
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": user_message(a.guest, research, transcript, a.n)}]
    # Generous cap: reasoning models (e.g. GLM-5.1) spend tokens on hidden reasoning first,
    # so a low cap leaves the answer empty.
    body = json.dumps({"model": a.model, "messages": messages, "temperature": 0.7, "max_tokens": 4096})
    # Shell out to curl: the endpoint blocks Python's default TLS fingerprint (curl's is accepted).
    proc = subprocess.run(
        ["curl", "-sS", "--fail", "--max-time", "240", "-X", "POST", ENDPOINT,
         "-H", f"Authorization: Bearer {os.environ['CRUSOE_API_KEY']}",
         "-H", "Content-Type: application/json", "--data-binary", "@-"],
        input=body, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"request failed: {proc.stderr.strip() or proc.returncode}")
    content = json.loads(proc.stdout)["choices"][0]["message"].get("content")
    if not content:
        raise SystemExit("model returned empty content — a reasoning model may need a higher token cap; retry or try a different --model")
    print(content.strip())


if __name__ == "__main__":
    main()
