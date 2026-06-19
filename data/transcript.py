"""Parse Dwarkesh Substack post HTML into structured, speaker-attributed transcripts.

The Substack `body_html` for a podcast post is regular:
  - `<h3>HH:MM:SS – Section title</h3>` mark chapter boundaries.
  - `<p><strong>Speaker Name</strong></p>` marks a speaker label.
  - Following `<p>...</p>` blocks (until the next label/section) are that speaker's turn.
  - Paragraphs before the first speaker label are Dwarkesh's written intro/framing.

We treat "Dwarkesh Patel" as the host; every other speaker is a guest.
"""

from __future__ import annotations

import html as _html
import re
from dataclasses import asdict, dataclass, field

HOST_NAME = "Dwarkesh Patel"

# Ordered block-level elements we care about.
_BLOCK_RE = re.compile(r"<(h2|h3|p)\b[^>]*>(.*?)</\1>", re.DOTALL | re.IGNORECASE)
# Leading <strong>NAME</strong> in a <p>, with whatever follows. Tolerates a leading
# [timestamp] and emphasis wrappers (<em>/<i>/<b>) seen across transcript eras.
# Covers: block ("<p><strong>Name</strong></p>"), inline ("<strong>Name</strong> text"),
# bracketed ("[00:01] <strong>Name:</strong> text"), and emphasized ("<em><strong>Name</strong></em>").
_STRONG_PREFIX_RE = re.compile(
    r"^\s*(?:\[[^\]]*\]\s*)?(?:<(?:em|i|b)\b[^>]*>\s*)*<strong>(.*?)</strong>(.*)$",
    re.DOTALL | re.IGNORECASE,
)
# Some transcripts use <br>-separated lines inside one <p> rather than one <p> per turn.
_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
# Footnote reference markers — drop them, they aren't spoken words.
_SUP_RE = re.compile(r"<sup\b.*?</sup>", re.DOTALL | re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")
_SECTION_HDR_RE = re.compile(r"^\s*(\d{1,2}:\d{2}(?::\d{2})?)\s*[–—-]\s*(.*)$")
# Inline timestamp that some older transcripts place after the speaker label, e.g.
# "(00:24): ..." or "00:24): ..." — strip it from the start of a turn's text.
_LEADING_TS_RE = re.compile(r"^\s*\(?\s*\d{1,2}:\d{2}(?::\d{2})?\s*\)?\s*:?\s*")


def _clean_text(fragment: str) -> str:
    """Strip footnote markers and all tags, unescape entities, collapse whitespace."""
    fragment = _SUP_RE.sub("", fragment)
    fragment = _TAG_RE.sub("", fragment)
    fragment = _html.unescape(fragment)
    return " ".join(fragment.split()).strip()


@dataclass
class Turn:
    speaker: str
    role: str  # "host" | "guest"
    text: str
    section_idx: int  # index into Transcript.sections, or -1 if pre-section


@dataclass
class Section:
    timestamp: str
    title: str


@dataclass
class Transcript:
    slug: str
    title: str
    url: str
    guest: str
    host: str = HOST_NAME
    post_date: str = ""
    audience: str = ""
    wordcount: int = 0
    description: str = ""
    intro: str = ""  # Dwarkesh's written framing before the spoken transcript
    sections: list[Section] = field(default_factory=list)
    turns: list[Turn] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def guest_turns(self) -> list[Turn]:
        return [t for t in self.turns if t.role == "guest"]

    @property
    def host_turns(self) -> list[Turn]:
        return [t for t in self.turns if t.role == "host"]


def _norm_name(raw: str) -> str:
    """Normalize a candidate speaker label: drop trailing timestamps/parens/colons."""
    name = _clean_text(raw)
    name = re.split(r"[(\d]", name, maxsplit=1)[0]  # cut at "(" or a digit (timestamp)
    return name.strip(" :–—-").strip()


def _strong_prefix(inner: str) -> tuple[str | None, str]:
    """If the <p> begins with <strong>..</strong>, return (raw_name, remainder_html)."""
    m = _STRONG_PREFIX_RE.match(inner)
    if not m:
        return None, inner
    return m.group(1), m.group(2)


def _detect_speakers(body: str) -> set[str]:
    """Pre-pass: speaker names are short leading-<strong> labels that recur (>=3x).

    Handles both transcript formats and avoids treating incidental bold as a speaker.
    """
    counts: dict[str, int] = {}
    for m in _BLOCK_RE.finditer(body):
        if m.group(1).lower() != "p":
            continue
        raw, _ = _strong_prefix(m.group(2))
        if raw is None:
            continue
        name = _norm_name(raw)
        if name and len(name) <= 40 and any(c.isalpha() for c in name):
            counts[name] = counts.get(name, 0) + 1
    speakers = {n for n, c in counts.items() if c >= 3}
    speakers |= {n for n in counts if HOST_NAME.lower() in n.lower()}
    return speakers


def _detect_guest(speakers: list[str]) -> str:
    """The most frequent non-host speaker label is the guest."""
    counts: dict[str, int] = {}
    for s in speakers:
        if s != HOST_NAME:
            counts[s] = counts.get(s, 0) + 1
    return max(counts, key=counts.get) if counts else "Unknown"


def parse_post(post: dict) -> Transcript:
    """Build a Transcript from a Substack post dict (from the posts API)."""
    body = _BR_RE.sub("</p><p>", post.get("body_html") or "")  # treat <br> lines as paragraphs
    speakers = _detect_speakers(body)
    sections: list[Section] = []
    turns: list[Turn] = []
    intro_parts: list[str] = []
    cur_speaker: str | None = None
    cur_role: str | None = None
    cur_section = -1
    seen_speaker = False
    speaker_labels: list[str] = []

    def add_text(text: str) -> None:
        if not (turns and turns[-1].speaker == cur_speaker):
            text = _LEADING_TS_RE.sub("", text)  # only at the start of a turn
        if turns and turns[-1].speaker == cur_speaker and turns[-1].section_idx == cur_section:
            turns[-1].text += "\n\n" + text
        else:
            turns.append(Turn(speaker=cur_speaker, role=cur_role, text=text, section_idx=cur_section))

    for m in _BLOCK_RE.finditer(body):
        tag, inner = m.group(1).lower(), m.group(2)

        if tag in ("h2", "h3"):
            text = _clean_text(inner)
            hdr = _SECTION_HDR_RE.match(text)
            if hdr:
                sections.append(Section(timestamp=hdr.group(1), title=hdr.group(2).strip()))
                cur_section = len(sections) - 1
            cur_speaker = None  # a header ends the current speaker's turn
            continue

        # tag == "p": may start with a speaker label (block or inline format).
        raw, remainder = _strong_prefix(inner)
        if raw is not None and _norm_name(raw) in speakers:
            name = _norm_name(raw)
            cur_speaker = name
            cur_role = "host" if HOST_NAME.lower() in name.lower() else "guest"
            speaker_labels.append(name)
            seen_speaker = True
            rest = _clean_text(remainder)
            if rest:  # inline format: dialogue follows the label in the same <p>
                add_text(rest)
            continue

        text = _clean_text(inner)
        if not text:
            continue
        if not seen_speaker:
            intro_parts.append(text)  # pre-transcript framing
            continue
        if cur_speaker is None:
            continue  # stray paragraph between header and next label
        add_text(text)

    for t in turns:
        t.text = t.text.strip()
    turns = [t for t in turns if t.text]
    guest = _detect_guest(speaker_labels)
    return Transcript(
        slug=post.get("slug", ""),
        title=post.get("title", ""),
        url=post.get("canonical_url", ""),
        guest=guest,
        post_date=post.get("post_date", ""),
        audience=post.get("audience", ""),
        wordcount=post.get("wordcount", 0) or 0,
        description=_clean_text(post.get("description") or ""),
        intro="\n\n".join(intro_parts),
        sections=sections,
        turns=turns,
    )
