"""Every line in the notes and records that mentions a paper: check them before and after.

    python scripts/cited_by.py SURNAME YEAR [--id NOTE_ID] [--root .]

Run it before writing a note. Other notes and records may already say what the paper
holds, which models use its data, or what it is credited with (2026-10-09: a note for
Gehmann 1987 was written without seeing that Gessler 2011 gives its oospore rule and
Hoppmann & Wittich 1997 its field data). Run it again after recording. Every claim credited
to the paper can now be checked at its source: confirm it, or correct the note that made it
(Leoni et al. 2026 credit Rossi et al. 2002 with a rule that paper does not print).

A surname matches however its umlauts and accents are written (Bläser, Blaeser, Blaser;
Giosuè, Giosue). The year must follow on the same line within a few words (et al.,
co-authors, '&'). With `--id`, lines naming the note or its records match too. The paper's
own note is skipped. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

GAP = 90  # characters allowed between a surname and its year: "et al.", co-authors


def fold(text: str) -> str:
    """Lower case, accents dropped, umlauts and their spelt-out forms made one."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"([aou])e", r"\1", text)


def matches(line: str, surname: str, year: str, note_id: str = "") -> bool:
    if note_id and re.search(rf"\b{re.escape(note_id)}\b", line):
        return True
    folded, name = fold(line), fold(surname)
    for m in re.finditer(rf"\b{re.escape(name)}\b", folded):
        if re.search(rf"\b{re.escape(year)}[a-z]?\b", folded[m.end() : m.end() + GAP]):
            return True
    return False


def search(root: Path, surname: str, year: str, note_id: str = "") -> list[tuple[Path, int, str]]:
    files = sorted((root / "literature").glob("*.md")) + sorted(
        (root / "src" / "formularium").glob("*.py")
    )
    found = []
    for path in files:
        if note_id and path.name == f"{note_id}.md":
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if matches(line, surname, year, note_id):
                found.append((path.relative_to(root), number, line.strip()))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("surname")
    parser.add_argument("year")
    parser.add_argument("--id", default="", help="the paper's note id, if it has one")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    found = search(args.root, args.surname, args.year, args.id)
    for path, number, line in found:
        print(f"{path}:{number}: {line[:200]}")
    print(f"{len(found)} lines", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
