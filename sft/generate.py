"""SFT generator — the Phase-2 sibling of `prompting.generate.PromptingGenerator`.

`SFTGenerator` implements the same `core.generator.Generator` protocol, so it drops straight
into the eval harness: `python -m evals.run_eval --generator sft ...` scores it against real
Dwarkesh with the frozen judge, identical to the prompting versions.

It reproduces the **training input shape** so eval matches what the model saw: the Method-B chat
(system = prompting/system.md + the GUEST/RESEARCH/TRANSCRIPT/TASK user message), with the
transcript truncated to 10k chars exactly as `sft.build_dataset` did. No few-shots (SFT replaces
them — the disposition is in the weights).

Two serving backends, switchable with one flag (or SFT_BASE_URL/SFT_MODEL env):
    --serving vllm    local vLLM (http://localhost:8000/v1); --model is the LoRA ADAPTER name
    --serving crusoe  the Crusoe inference API; --model is the served model id, key = CRUSOE_API_KEY

    # local LoRA adapter on vLLM:
    python -m sft.generate --serving vllm --model dwarkesh-run1-ckpt32 --slug eric-jang --turn 12
    # or set it once: export SFT_BASE_URL=http://localhost:8000/v1 SFT_MODEL=dwarkesh-run1-ckpt32
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core.generator import EvalCard
from core.llm import LLM, LLMConfig
from data import dataset
from prompting.prompts import Method, Mode, build_messages, render_transcript
from sft.build_dataset import truncate_transcript


# Endpoint presets — pick with serving=; SFT_BASE_URL (env) or base_url= override either.
SERVING = {
    "vllm": "http://localhost:8000/v1",                  # local vLLM; model = the LoRA adapter name
    "crusoe": "https://api.inference.crusoecloud.com/v1",  # Crusoe inference API
}


class SFTGenerator:
    """A Generator backed by the fine-tuned model. Same Method-B prompt + 10k truncation as training.

    Backend is configurable and deferred: `serving` ('vllm'|'crusoe') picks the base_url, or set
    SFT_BASE_URL/SFT_MODEL (api key falls back to CRUSOE_API_KEY), or pass base_url=/model=. The LLM
    is built lazily so messages_for() and `name` work offline; only generate() needs a live endpoint.
    """

    def __init__(self, *, model: str | None = None, serving: str | None = None, base_url: str | None = None,
                 temperature: float = 0.0, max_tokens: int = 1024, llm: LLM | None = None):
        self.temperature, self.max_tokens, self._llm, self.serving = temperature, max_tokens, llm, serving
        env = LLMConfig.from_env("SFT")
        self.model = model or env.model
        base_url = base_url or env.base_url or (SERVING.get(serving) if serving else None)
        self._cfg = LLMConfig(base_url=base_url, api_key=env.api_key, model=self.model)
        self.name = f"sft:{(self.model or 'TBD').split('/')[-1]}"

    @property
    def llm(self) -> LLM:
        if self._llm is None:
            if not self._cfg.base_url or not self._cfg.model:
                raise ValueError(
                    "SFT serving socket not configured — pass --serving vllm|crusoe with --model "
                    "(the vLLM adapter name or served model id), or set SFT_BASE_URL/SFT_MODEL. "
                    "See sft/README.md.")
            self._llm = LLM(self._cfg)
        return self._llm

    def messages_for(self, card: EvalCard, n: int = 5) -> list[dict]:
        """The exact chat the model trained on: Method-B, transcript truncated to 10k chars."""
        ts = truncate_transcript(card.transcript_so_far) if card.transcript_so_far.strip() else ""
        return build_messages(method=Method.B, mode=card.mode, guest=card.guest,
                              research_prep=card.research, transcript_so_far=ts, n=n)

    def generate(self, card: EvalCard, *, n: int = 5) -> str:
        msgs = self.messages_for(card, n=n)
        return (self.llm.chat(msgs, temperature=self.temperature, max_tokens=self.max_tokens) or "").strip()


def _card_for(slug: str, mode: Mode, turn: int | None) -> EvalCard:
    """Build one EvalCard from the corpus (mirrors prompting.generate)."""
    t = dataset.load_transcript(slug)
    research = dataset.default_research(t)
    transcript_so_far, reference = "", None
    if mode == Mode.NEXT_QUESTION:
        if turn is None:
            raise SystemExit("next-question mode needs --turn (index of the host question to predict)")
        transcript_so_far = render_transcript(t.turns[:turn])
        if turn < len(t.turns) and t.turns[turn].role == "host":
            reference = t.turns[turn].text
    return EvalCard(slug=slug, guest=t.guest, research=research, transcript_so_far=transcript_so_far,
                    mode=mode, reference=reference, turn_idx=turn)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--mode", type=Mode, choices=list(Mode), default=Mode.NEXT_QUESTION)
    ap.add_argument("--turn", type=int, default=None)
    ap.add_argument("-n", type=int, default=6)
    ap.add_argument("--serving", choices=list(SERVING), default=None,
                    help="endpoint preset: vllm=localhost:8000, crusoe=inference API (or set SFT_BASE_URL)")
    ap.add_argument("--model", default=None, help="served model / vLLM adapter name (or set SFT_MODEL)")
    ap.add_argument("--temperature", type=float, default=0.0)
    a = ap.parse_args()

    card = _card_for(a.slug, a.mode, a.turn)
    gen = SFTGenerator(model=a.model, serving=a.serving, temperature=a.temperature)
    if card.reference:
        print("=== REAL DWARKESH ===\n" + card.reference + "\n")
    print("=== GENERATED (" + gen.name + ") ===\n" + gen.generate(card, n=a.n))


if __name__ == "__main__":
    main()
