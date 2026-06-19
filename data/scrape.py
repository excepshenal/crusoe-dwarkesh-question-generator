"""Scrape Dwarkesh podcast transcripts from the public Substack API.

Enumeration uses the paginated list endpoint; full bodies come from the per-slug
endpoint (the list endpoint occasionally truncates long posts). Only public
(`audience == "everyone"`) podcast posts are saved.

    python -m data.scrape            # scrape all public episodes
    python -m data.scrape --limit 5  # first 5 (smoke test)
    python -m data.scrape --slug eric-jang
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
import urllib.parse
from pathlib import Path

from .transcript import parse_post

BASE = "https://www.dwarkesh.com/api/v1"
# Substack sits behind Cloudflare, which blocks Python's TLS fingerprint (JA3) even
# with browser headers. curl's fingerprint is allowed, so we shell out to it.
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
DATA = Path(__file__).resolve().parent
RAW = DATA / "raw"
TRANSCRIPTS = DATA / "transcripts"


def _get_json(url: str, params: dict | None = None, retries: int = 3) -> object:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    last = ""
    for attempt in range(retries):
        proc = subprocess.run(
            ["curl", "-sS", "--fail", "-A", UA, "--max-time", "60", url],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            try:
                return json.loads(proc.stdout)
            except json.JSONDecodeError as e:
                last = f"bad JSON: {e}"
        else:
            last = proc.stderr.strip() or f"curl exit {proc.returncode}"
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed after {retries} tries: {last}")


def list_posts(page_size: int = 50, pause: float = 0.5) -> list[dict]:
    """Enumerate every post via the paginated list endpoint."""
    out: list[dict] = []
    offset = 0
    while True:
        batch = _get_json(f"{BASE}/posts", params={"limit": page_size, "offset": offset})
        if not batch:
            break
        out.extend(batch)
        offset += len(batch)
        time.sleep(pause)
        if len(batch) < page_size:
            break
    return out


def fetch_post(slug: str) -> dict:
    """Full post (with complete body_html) for a single slug."""
    return _get_json(f"{BASE}/posts/{slug}")


def _is_public_podcast(meta: dict) -> bool:
    return meta.get("type") == "podcast" and meta.get("audience") == "everyone"


def scrape(limit: int | None = None, only_slug: str | None = None, pause: float = 0.6) -> list[str]:
    RAW.mkdir(parents=True, exist_ok=True)
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)

    if only_slug:
        metas = [{"slug": only_slug, "type": "podcast", "audience": "everyone"}]
    else:
        print("Enumerating posts...")
        all_posts = list_posts()
        metas = [m for m in all_posts if _is_public_podcast(m)]
        print(f"  {len(all_posts)} posts total, {len(metas)} public podcast episodes")
        (DATA / "episodes_index.json").write_text(
            json.dumps(
                [
                    {k: m.get(k) for k in ("slug", "title", "post_date", "audience", "wordcount", "podcast_duration")}
                    for m in metas
                ],
                indent=2,
            )
        )
        if limit:
            metas = metas[:limit]

    saved: list[str] = []
    for i, meta in enumerate(metas, 1):
        slug = meta["slug"]
        try:
            post = fetch_post(slug)
            (RAW / f"{slug}.json").write_text(json.dumps(post))
            t = parse_post(post)
            if not t.turns:
                print(f"  [{i}/{len(metas)}] {slug}: WARNING no turns parsed — skipping")
                continue
            (TRANSCRIPTS / f"{slug}.json").write_text(json.dumps(t.to_dict(), indent=2, ensure_ascii=False))
            saved.append(slug)
            print(
                f"  [{i}/{len(metas)}] {slug}: guest={t.guest!r} "
                f"turns={len(t.turns)} (guest={len(t.guest_turns)}) sections={len(t.sections)}"
            )
        except Exception as e:  # noqa: BLE001
            print(f"  [{i}/{len(metas)}] {slug}: ERROR {e}")
        time.sleep(pause)

    print(f"\nSaved {len(saved)} transcripts to {TRANSCRIPTS}")
    return saved


def main() -> None:
    ap = argparse.ArgumentParser(description="Scrape Dwarkesh podcast transcripts.")
    ap.add_argument("--limit", type=int, default=None, help="only the first N episodes")
    ap.add_argument("--slug", type=str, default=None, help="scrape a single slug")
    ap.add_argument("--pause", type=float, default=0.6, help="seconds between requests")
    args = ap.parse_args()
    scrape(limit=args.limit, only_slug=args.slug, pause=args.pause)


if __name__ == "__main__":
    main()
