"""Run the question generator for a given method + mode.

    # next-question, method C, against a held-out episode at a real turn
    python -m dwarkesh_qgen.generate --slug eric-jang --mode copilot --method c --turn 12

    # prep-stage, method B, N starter questions from research only
    python -m dwarkesh_qgen.generate --slug eric-jang --mode sparring --method b -n 8

Requires GENERATOR_BASE_URL / GENERATOR_MODEL (+ API key) in the env.
"""

from __future__ import annotations

import argparse

from . import dataset
from .llm import LLM
from .prompts import Method, Mode, build_messages, render_transcript


def generate(
    *,
    slug: str,
    mode: Mode,
    method: Method,
    turn: int | None = None,
    n: int = 5,
    k_shots: int = 2,
    temperature: float = 0.7,
    llm: LLM | None = None,
) -> dict:
    """Build the prompt for one query and call the generator. Returns prompt + output."""
    t = dataset.load_transcript(slug)
    research = dataset.default_research(t)

    transcript_so_far = ""
    reference = None
    if mode == Mode.COPILOT:
        if turn is None:
            raise ValueError("copilot mode needs --turn (index of the host question to predict)")
        ctx = t.turns[:turn]
        transcript_so_far = render_transcript(ctx)
        if turn < len(t.turns) and t.turns[turn].role == "host":
            reference = t.turns[turn].text  # the real Dwarkesh question at this point

    few_shots = None
    if method == Method.C:
        few_shots = dataset.sample_few_shots(mode=mode, exclude_slug=slug, k=k_shots, n_prep=n)

    messages = build_messages(
        method=method,
        mode=mode,
        guest=t.guest,
        research_prep=research,
        transcript_so_far=transcript_so_far,
        n=n,
        few_shots=few_shots,
    )

    llm = llm or LLM.for_role("GENERATOR")
    output = llm.chat(messages, temperature=temperature)
    return {
        "slug": slug,
        "guest": t.guest,
        "mode": mode.value,
        "method": method.value,
        "turn": turn,
        "messages": messages,
        "output": output,
        "reference": reference,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--mode", type=Mode, choices=list(Mode), default=Mode.COPILOT)
    ap.add_argument("--method", type=Method, choices=list(Method), default=Method.B)
    ap.add_argument("--turn", type=int, default=None)
    ap.add_argument("-n", type=int, default=5)
    ap.add_argument("--k-shots", type=int, default=2)
    ap.add_argument("--temperature", type=float, default=0.7)
    args = ap.parse_args()

    res = generate(
        slug=args.slug,
        mode=args.mode,
        method=args.method,
        turn=args.turn,
        n=args.n,
        k_shots=args.k_shots,
        temperature=args.temperature,
    )
    if res.get("reference"):
        print("=== REAL DWARKESH ===\n" + res["reference"] + "\n")
    print("=== GENERATED ===\n" + res["output"])


if __name__ == "__main__":
    main()
