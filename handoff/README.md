# Dwarkesh question-generator — prompting method (test pack)

This is the **prompting** side of the project: a base model turned into a Dwarkesh-style
question generator purely by prompt (no fine-tuning yet). You can test it against the inference
endpoint with the materials here.

## Endpoint
- **URL:** `https://api.inference.crusoecloud.com/v1` (OpenAI-compatible)
- **Model:** `openai/gpt-oss-120b`
- **Auth:** `Authorization: Bearer <YOUR_API_KEY>` — you'll be given a key separately.

## The prompt (two messages)
1. **System** = `system_prompt.txt` (fixed): what makes a great Dwarkesh question + style rules.
2. **User** = the guest's research + the conversation so far, in this shape:
   ```
   GUEST: <name>

   RESEARCH PREP:
   <the guest dossier>

   TRANSCRIPT SO FAR:
   <the conversation so far>          # or "(none — pre-interview)"

   TASK: Next question.               # next-question mode (transcript present)
   ```
   For **prep mode** (no transcript), the TASK line is `Generate N candidate questions for prep.`

So: same fixed system prompt every time; you slot `(guest research, conversation so far)` into the
user message. That's the whole method.

## Two modes
- **Next-question:** pass the conversation so far → one sharp next question.
- **Prep:** no transcript → N starter questions for interview prep.

## Run it
Use `generate_question.py` (Python 3 + curl, both preinstalled on macOS/Linux):
```bash
export CRUSOE_API_KEY=<your key>
cd handoff
# next-question mode — pass the conversation so far (ready-made example):
python3 generate_question.py --guest "Dario Amodei" --research ../research/dario-amodei-2.md \
  --transcript examples/dario-amodei-2_convo.txt
# prep mode — research only, get starter questions:
python3 generate_question.py --guest "Tyler Cowen" --research ../research/tyler-cowen-3.md
```
`--research` is the guest dossier; `--transcript` is the conversation so far (speaker-labeled lines;
omit it for prep mode). Bring your own `(research, conversation)` pairs to probe any guest.
`examples/*.md` show the exact assembled prompt for reference; `system_prompt.txt` is the fixed
system prompt.

## What to look for
Is the question sharp, specific, non-obvious, and genuinely reactive to the last thing the guest
said — or generic/softball/off-thread? This is the v0 baseline; we'll iterate (and eventually
fine-tune) to beat it, measured against the human-labeled oracle.
