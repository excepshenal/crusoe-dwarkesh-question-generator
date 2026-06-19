#!/usr/bin/env python3
"""Test the Dwarkesh question-generator prompt against the Crusoe inference endpoint.

No Python installs needed (stdlib + curl, which ships on macOS/Linux). Set your key, then:

  export CRUSOE_API_KEY=...                       # the key you were given
  # next-question mode — pass the conversation so far:
  python generate_question.py --guest "Dario Amodei" --research research.md --transcript convo.txt
  # prep mode — research only, get N starter questions:
  python generate_question.py --guest "Tyler Cowen" --research research.md

research.md = the guest dossier; convo.txt = the conversation so far, e.g.
  Dwarkesh Patel: ...
  Dario Amodei: ...
(omit --transcript for prep mode). Prints the model's question(s).
"""
import argparse, json, os, subprocess

ENDPOINT = "https://api.inference.crusoecloud.com/v1/chat/completions"
MODEL = "openai/gpt-oss-120b"
SYSTEM = open(os.path.join(os.path.dirname(__file__), "system_prompt.txt")).read()


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
    a = ap.parse_args()

    research = open(a.research).read()
    transcript = open(a.transcript).read() if a.transcript else ""
    system = SYSTEM.replace("{n}", str(a.n))
    messages = [{"role": "system", "content": system},
                {"role": "user", "content": user_message(a.guest, research, transcript, a.n)}]
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": 0.7, "max_tokens": 1024})
    # Shell out to curl: the endpoint blocks Python's default TLS fingerprint (curl's is accepted).
    proc = subprocess.run(
        ["curl", "-sS", "--fail", "--max-time", "120", "-X", "POST", ENDPOINT,
         "-H", f"Authorization: Bearer {os.environ['CRUSOE_API_KEY']}",
         "-H", "Content-Type: application/json", "--data-binary", "@-"],
        input=body, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"request failed: {proc.stderr.strip() or proc.returncode}")
    print(json.loads(proc.stdout)["choices"][0]["message"]["content"].strip())


if __name__ == "__main__":
    main()
