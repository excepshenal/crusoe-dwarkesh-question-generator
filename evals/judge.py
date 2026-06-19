"""The frozen production LLM judge used to grade generators at scale.

Best config from calibration (see llm_judge/): zai/GLM-5.1 + judge.md (the promoted judge_v2),
~85% agreement with the human oracle. Keep this FROZEN while iterating generators — calibrating
the judge and tuning a generator must not share a loop (else you optimize the judge's quirks).
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from core.llm import LLM, LLMConfig

_JUDGE_MD = Path(__file__).resolve().parent / "judge.md"
_CRUSOE = "https://api.inference.crusoecloud.com/v1"
DEFAULT_JUDGE_MODEL = "zai/GLM-5.1"


class Judge:
    def __init__(self, model: str = DEFAULT_JUDGE_MODEL, prompt_path: Path = _JUDGE_MD, llm: LLM | None = None):
        self.model = model
        self.system = Path(prompt_path).read_text()
        self.llm = llm or LLM(LLMConfig(base_url=_CRUSOE, api_key=os.environ["CRUSOE_API_KEY"], model=model))
        self.name = f"judge:{model.split('/')[-1]}"


def default_judge() -> Judge:
    return Judge()


def _verdict(raw: str) -> str:
    """Winner ('A'|'B'|'TIE') from the judge's JSON; 'TIE' if unparseable."""
    try:
        obj = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
        w = str(obj.get("winner", "tie")).strip().upper()
        return w if w in ("A", "B") else "TIE"
    except Exception:
        return "TIE"


def judge_pairwise(judge: Judge, context: str, a: str, b: str) -> str:
    """Compare candidate `a` vs `b` for this context, de-biased by running BOTH orders
    (a flip => tie). Returns 'a' | 'b' | 'tie' (referring to the args, not slot labels)."""
    def ask(first: str, second: str) -> str:
        msg = f"CONTEXT:\n{context}\n\nCANDIDATE A:\n{first}\n\nCANDIDATE B:\n{second}"
        return _verdict(judge.llm.chat(
            [{"role": "system", "content": judge.system}, {"role": "user", "content": msg}],
            temperature=0.0, max_tokens=3072))

    w1 = ask(a, b)   # a in slot A
    w2 = ask(b, a)   # a in slot B
    if w1 == "A" and w2 == "B":
        return "a"
    if w1 == "B" and w2 == "A":
        return "b"
    return "tie"
