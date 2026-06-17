"""Thin OpenAI-compatible chat client, configured by env var prefix.

Everything (the generator under test, the LLM judge, the research bootstrapper)
speaks the OpenAI chat API. The platform's inference endpoint is OpenAI-compatible,
and Claude is reachable via its OpenAI-compatible endpoint, so one client covers all.

Configure per role with env vars (prefix in {GENERATOR, JUDGE, RESEARCH}):
    {PREFIX}_BASE_URL   e.g. https://api.anthropic.com/v1/   (generator: your endpoint)
    {PREFIX}_API_KEY
    {PREFIX}_MODEL      e.g. claude-opus-4-8

Defaults point the JUDGE/RESEARCH roles at Claude; the GENERATOR has no default
endpoint until you provide one (the inference API is supplied later).
"""

from __future__ import annotations

import os
from dataclasses import dataclass

# Sensible Claude defaults for roles we run ourselves. All overridable by env.
_DEFAULTS = {
    "JUDGE": {"base_url": "https://api.anthropic.com/v1/", "model": "claude-opus-4-8"},
    "RESEARCH": {"base_url": "https://api.anthropic.com/v1/", "model": "claude-opus-4-8"},
    "GENERATOR": {"base_url": None, "model": None},
}


@dataclass
class LLMConfig:
    base_url: str | None
    api_key: str | None
    model: str | None

    @classmethod
    def from_env(cls, prefix: str) -> "LLMConfig":
        d = _DEFAULTS.get(prefix, {})
        return cls(
            base_url=os.getenv(f"{prefix}_BASE_URL", d.get("base_url")),
            api_key=os.getenv(f"{prefix}_API_KEY") or os.getenv("ANTHROPIC_API_KEY"),
            model=os.getenv(f"{prefix}_MODEL", d.get("model")),
        )


class LLM:
    def __init__(self, cfg: LLMConfig):
        if not cfg.base_url or not cfg.model:
            raise ValueError("LLM needs base_url and model (set the role's *_BASE_URL/*_MODEL env vars).")
        from openai import OpenAI  # lazy: data tooling shouldn't require the SDK

        self.cfg = cfg
        self.client = OpenAI(base_url=cfg.base_url, api_key=cfg.api_key or "EMPTY")

    @classmethod
    def for_role(cls, prefix: str) -> "LLM":
        return cls(LLMConfig.from_env(prefix))

    def chat(self, messages: list[dict], temperature: float = 0.7, max_tokens: int = 1024, **kw) -> str:
        resp = self.client.chat.completions.create(
            model=self.cfg.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kw,
        )
        return (resp.choices[0].message.content or "").strip()
