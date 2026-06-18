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

   TASK: Next question.               # copilot mode (transcript present)
   ```
   For **prep mode** (no transcript), the TASK line is `Generate N candidate questions for prep.`

So: same fixed system prompt every time; you slot `(guest research, conversation so far)` into the
user message. That's the whole method.

## Two modes
- **Copilot / next-question:** pass the conversation so far → one sharp next question.
- **Prep / sparring:** no transcript → N starter questions for interview prep.

## Run it
**Option A — ready-made examples (curl).** `examples/*.json` are complete request bodies (3 guests:
Dario Amodei + Sarah Paine in copilot mode, Tyler Cowen in prep mode). `examples/*.md` show the
exact assembled prompt for each.
```bash
export CRUSOE_API_KEY=<your key>
curl -s https://api.inference.crusoecloud.com/v1/chat/completions \
  -H "Authorization: Bearer $CRUSOE_API_KEY" -H "Content-Type: application/json" \
  -d @examples/dario-amodei-2_copilot.json \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['choices'][0]['message']['content'])"
```

**Option B — your own inputs (script; needs only Python 3 + curl, both preinstalled on macOS/Linux).**
```bash
export CRUSOE_API_KEY=<your key>
python3 try_prompt.py --guest "Dario Amodei" --research research.md --transcript convo.txt   # next question
python3 try_prompt.py --guest "Tyler Cowen"  --research research.md                            # prep questions
```
where `research.md` is the guest dossier and `convo.txt` is the conversation so far (speaker-labeled
lines). Bring your own `(research, conversation)` pairs to probe it on whatever guests you like.

## What to look for
Is the question sharp, specific, non-obvious, and genuinely reactive to the last thing the guest
said — or generic/softball/off-thread? This is the v0 baseline; we'll iterate (and eventually
fine-tune) to beat it, measured against the human-labeled oracle.
