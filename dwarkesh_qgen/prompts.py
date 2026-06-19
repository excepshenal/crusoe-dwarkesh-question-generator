"""Prompt assembly for the Dwarkesh question generator.

One system + user template drives two modes and three prompting methods:

  Modes:
    - NEXT_QUESTION: transcript present -> generate ONE next question.
    - PREP:          transcript empty   -> generate N starter questions.

  Methods (increasing complexity; mirrors the project's Method-1 a/b/c):
    - A: user prompt only (research + instruction), no system prompt, no shots.
    - B: A + the "what makes a great Dwarkesh question" system prompt.
    - C: B + few-shot examples (real (prep+transcript -> his next turn) pairs).

Method 2 (SFT) trains on the Method-B prompt shape (system + user, no shots).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

_SYSTEM_PATH = Path(__file__).resolve().parent.parent / "prompts" / "system.md"


class Mode(str, Enum):
    NEXT_QUESTION = "next-question"  # transcript present
    PREP = "prep"  # transcript empty


class Method(str, Enum):
    A = "a"  # user-only
    B = "b"  # + system
    C = "c"  # + few-shot


@dataclass
class FewShot:
    """A worked example: the prompt context and Dwarkesh's actual next question(s)."""

    guest: str
    research_prep: str
    transcript_so_far: str  # rendered, possibly empty
    mode: Mode
    answer: str  # his real next turn (next-question) or real starter questions (prep)


def load_system_prompt(n: int = 5) -> str:
    text = _SYSTEM_PATH.read_text()
    return text.replace("{n}", str(n))


def render_transcript(turns) -> str:
    """Speaker-attributed plain text from a list of Turn objects (or dicts)."""
    lines = []
    for t in turns:
        speaker = t["speaker"] if isinstance(t, dict) else t.speaker
        text = t["text"] if isinstance(t, dict) else t.text
        lines.append(f"{speaker}: {text}")
    return "\n\n".join(lines)


def build_user_message(
    guest: str,
    research_prep: str,
    transcript_so_far: str,
    mode: Mode,
    n: int = 5,
) -> str:
    if mode == Mode.PREP:
        task = f'Generate {n} candidate questions for prep.'
        transcript_block = "(none — pre-interview)"
    else:
        task = "Next question."
        transcript_block = transcript_so_far.strip() or "(none yet)"
    return (
        f"GUEST: {guest}\n\n"
        f"RESEARCH PREP:\n{research_prep.strip()}\n\n"
        f"TRANSCRIPT SO FAR:\n{transcript_block}\n\n"
        f"TASK: {task}"
    )


def build_messages(
    *,
    method: Method,
    mode: Mode,
    guest: str,
    research_prep: str,
    transcript_so_far: str = "",
    n: int = 5,
    few_shots: list[FewShot] | None = None,
) -> list[dict]:
    """Assemble OpenAI-style chat messages for the given method and mode."""
    messages: list[dict] = []

    if method in (Method.B, Method.C):
        messages.append({"role": "system", "content": load_system_prompt(n=n)})

    if method == Method.C:
        for shot in few_shots or []:
            messages.append(
                {
                    "role": "user",
                    "content": build_user_message(
                        shot.guest, shot.research_prep, shot.transcript_so_far, shot.mode, n=n
                    ),
                }
            )
            messages.append({"role": "assistant", "content": shot.answer})

    # Method A has no system prompt, so fold a one-line instruction into the user turn.
    user = build_user_message(guest, research_prep, transcript_so_far, mode, n=n)
    if method == Method.A:
        instr = (
            f"Generate {n} sharp, non-obvious interview questions for prepping this guest, "
            "grounded in the research below.\n\n"
            if mode == Mode.PREP
            else "Generate the single best next interview question, grounded in the materials below.\n\n"
        )
        user = instr + user
    messages.append({"role": "user", "content": user})
    return messages
