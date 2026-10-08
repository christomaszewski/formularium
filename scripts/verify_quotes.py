"""Check a reading agent's quotes against the paper's text, line by line (step 5, verify).

    python -I scripts/verify_quotes.py PAPER.txt FACTS.json [--window 3]

FACTS.json is a list of objects with `line` (1-based, as the agent cited it) and `quote`
(the exact text it says is printed there), and optionally `claim` (what the quote is taken
to show). For each it prints:
- `ok`: the quote is on the cited line, or within `--window` lines of it (two-column
  layouts and wrapped lines shift text by a line or two);
- `moved N`: the quote is elsewhere in the text, at line N (the agent miscounted);
- `MISSING`: not found anywhere. Read the paragraph yourself: the agent may have
  paraphrased, mended a garbled number, or invented it.

Matching ignores runs of whitespace, case, and the usual extraction artefacts (ligatures,
Unicode minus and dashes, non-breaking spaces), so a quote that spans a line break still
matches. It checks that the words are printed, not that they mean what the claim says:
that judgement stays with the main session (INGESTING.md, step 5). Standard library only;
the paper's text is data, read and never executed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ARTEFACTS = {
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb00": "ff",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
    "\u2212": "-",  # minus sign
    "\u2013": "-",  # en dash
    "\u2014": "-",  # em dash
    "\u2010": "-",  # hyphen
    "\u2011": "-",  # non-breaking hyphen
    "\u00a0": " ",  # no-break space
    "\u2019": "'",
    "\u2018": "'",
    "\u201c": '"',
    "\u201d": '"',
}


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    for a, b in ARTEFACTS.items():
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip().lower()


def find(lines: list[str], quote: str, line: int, window: int) -> tuple[str, int | None]:
    """Where `quote` is printed: ("ok", line), ("moved", line) or ("MISSING", None)."""
    q = normalise(quote)
    if not q:
        return "MISSING", None

    def hit(start: int, stop: int) -> bool:
        start, stop = max(start, 0), min(stop, len(lines))
        return q in normalise(" ".join(lines[start:stop]))

    span = len(q) // 30 + 2  # a quote may wrap over several lines
    i = line - 1
    if hit(i - window, i + window + span):
        return "ok", line
    for j in range(len(lines)):
        here = q in normalise(" ".join(lines[j : j + span]))
        if here and q not in normalise(" ".join(lines[j + 1 : j + 1 + span])):
            return "moved", j + 1  # the line the quote starts on
    return "MISSING", None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("text", type=Path)
    ap.add_argument("facts", type=Path)
    ap.add_argument("--window", type=int, default=3)
    args = ap.parse_args()
    # split on newlines only: splitlines() also breaks at form feeds (pdftotext page breaks),
    # which would shift every line number after page 1 against grep -n and the Read tool
    lines = args.text.read_text(encoding="utf-8", errors="replace").split("\n")
    facts = json.loads(args.facts.read_text(encoding="utf-8"))
    bad = 0
    for f in facts:
        state, where = find(lines, str(f.get("quote", "")), int(f.get("line") or 0), args.window)
        bad += state != "ok"
        label = state if state != "moved" else f"moved {where}"
        print(f"{label:10s} l.{f.get('line')!s:6s} {str(f.get('quote', ''))[:90]}")
    print(f"{len(facts) - bad} of {len(facts)} at their cited lines; {bad} to check by hand")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
