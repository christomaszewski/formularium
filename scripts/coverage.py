"""Which papers in a drop already have a literature note, and which still need one.

    python scripts/coverage.py DIR [DIR ...] [--notes literature]

For every PDF under the directories it prints the note that covers it, matched by the
note's `files` (the names the paper was dropped under) or its `doi`, against the DOIs on
the paper's first two pages and the DOI a publisher's file name often carries. It also
prints the page count, characters per page (under about 500 means a scan: OCR it first),
the first DOI found, and a copy that duplicates another byte for byte.

A match is a lead. A DOI on a first page can belong to a cited paper, and a paper whose
first pages print no DOI (most before about 2000) matches only by `files`. Before writing a
note for an unmatched paper, identify it: it may be a copy, under another name, of one
already noted. Standard library only; needs `pdftotext` and `pdfinfo` (poppler-utils).
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

DOI = re.compile(r"\b10\.\d{4,9}/[^\s\"<>,;]+", re.IGNORECASE)
SHORTEST = 8  # a DOI suffix shorter than this matches file names by accident


@dataclass(frozen=True)
class Note:
    id: str
    doi: str
    files: tuple[str, ...]


def normalise(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def read_notes(directory: Path) -> list[Note]:
    notes = []
    for path in sorted(directory.glob("*.md")):
        match = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
        if not match:
            continue
        header = dict(line.partition(":")[::2] for line in match.group(1).splitlines())
        files = header.get("files", "").strip().strip("[]")
        notes.append(
            Note(
                id=path.stem,
                doi=header.get("doi", "").strip(),
                files=tuple(f.strip() for f in files.split(",") if f.strip()),
            )
        )
    return notes


def match(name: str, dois: list[str], notes: list[Note]) -> list[str]:
    """The ids of the notes that cover a file called `name` whose first pages print `dois`."""
    found = {normalise(d) for d in dois}
    stem = normalise(Path(name).stem)
    covered = []
    for note in notes:
        doi = normalise(note.doi)
        suffix = normalise(note.doi.partition("/")[2])
        if (
            name in note.files
            or (doi and doi in found)
            or (len(suffix) >= SHORTEST and suffix in stem)
        ):
            covered.append(note.id)
    return covered


def _run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("dirs", nargs="+", type=Path)
    parser.add_argument(
        "--notes", type=Path, default=Path(__file__).resolve().parent.parent / "literature"
    )
    args = parser.parse_args()
    notes = read_notes(args.notes)
    seen: dict[str, Path] = {}
    rows = []
    for pdf in sorted(p for d in args.dirs for p in d.rglob("*") if p.suffix.lower() == ".pdf"):
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        duplicate = seen.setdefault(digest, pdf)
        try:
            pages = int(re.search(r"^Pages:\s+(\d+)", _run("pdfinfo", str(pdf)), re.M).group(1))
            text = _run("pdftotext", "-l", "2", "-layout", str(pdf), "-")
        except (subprocess.CalledProcessError, AttributeError):
            rows.append(("?", pdf, 0, 0, "(unreadable)", ""))
            continue
        dois = sorted({d.rstrip(".)") for d in DOI.findall(text)})
        per_page = len(text) / min(pages, 2) if pages else 0
        covered = ", ".join(match(pdf.name, dois, notes)) or "-"
        same = f"same as {duplicate.name}" if duplicate != pdf else ""
        rows.append((covered, pdf, pages, per_page, dois[0] if dois else "", same))
    rows.sort(key=lambda r: (r[0] != "-", str(r[1])))
    print(f"{'note':<18} {'pages':>5} {'ch/pg':>6}  file  [first DOI]  [duplicate]")
    for covered, pdf, pages, per_page, doi, same in rows:
        scan = "  scan?" if 0 < per_page < 500 else ""
        print(f"{covered:<18} {pages:>5} {per_page:>6.0f}  {pdf}  {doi}  {same}{scan}")
    uncovered = sum(1 for r in rows if r[0] == "-" and not r[5])
    print(f"\n{len(rows)} PDFs; {uncovered} distinct ones have no note. A match is a lead.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
