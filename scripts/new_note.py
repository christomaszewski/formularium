"""Start a literature note with the header and sections literature/README.md asks for.

    python scripts/new_note.py zachos1959 [--dir literature]
    python -I scripts/new_note.py chen2019onset --triage TRIAGE.json --key KEY \
        --files "a.pdf,b.pdf" --read "2026-10-08, first pages, by a triage agent (MODEL)"

Writes literature/<id>.md, refusing to overwrite. Fill in every field, then add a line
for the note to the index in literature/README.md; tests/test_literature.py fails until
both are done properly (an empty `status` is not one of the allowed values).

With `--triage`, the header is filled from a triage agent's record (the JSON the triage
brief in INGESTING.md asks for): the citation with the authors as printed, the DOI, the
region, and the files given. The record is a lead, not a reading: check the citation
against the paper before committing, since the header claims it was read.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TEMPLATE = """---
id: {id}
citation:
doi:
read:
status:
diseases: []
crops: []
regions: []
processes: []
records: []
datasets: []
files: []
---

# {id}:

## What it holds

- **Data:** sites, years, cultivars, conditions, counts.
- **Formulations:** equations and values, with the table or page.

## Dependence

- Which models it computes, which data it was fitted to, which models shaped its data, and
  whose authors it shares.

## Bearing ({date})

- What was concluded, and for whom.
"""


PARTICLES = {"de", "da", "del", "della", "dalla", "di", "van", "der", "von", "la", "le", "du"}


def surname_first(name: str) -> str:
    """'L. V. Madden' or 'Mélanie Rouxel' as 'Madden, L. V.' or 'Rouxel, Mélanie'.

    A name already written 'Surname, Given' is kept; 'Maddalena G.' (surname, then
    initials) becomes 'Maddalena, G.'. Particles stay with the surname: 'Van der Heyden'."""
    name = " ".join(name.split())
    if "," in name or not name or re.search(r"\(|Authority|Agency|Institute|Service", name):
        return name  # already inverted, or an organisation
    parts = name.split(" ")
    initial = re.compile(r"^(?:[A-ZÀ-Ý]\.?-?)+$|^[A-ZÀ-Ý]\.[A-ZÀ-Ý]\.?$")
    if len(parts) > 1 and all(initial.match(p) for p in parts[1:]) and not initial.match(parts[0]):
        return f"{parts[0]}, {' '.join(parts[1:])}"
    i = len(parts) - 1
    while i > 1 and (
        parts[i - 1].lower() in PARTICLES or parts[i - 1].lower().endswith(("-de", "-da"))
    ):
        i -= 1
    if len(parts) == 1:
        return name
    return f"{' '.join(parts[i:])}, {' '.join(parts[:i])}"


def citation(record: dict) -> str:
    """A citation line from a triage record: authors as printed, year, title, journal."""
    authors = [surname_first(a) for a in record.get("authors", [])]
    who = ", ".join(authors[:-1]) + " & " + authors[-1] if len(authors) > 1 else "".join(authors)
    if not record.get("authors_complete", True):
        who += " et al. (byline not seen in full)"
    where = record.get("journal", "")
    if record.get("volume"):
        where += f" {record['volume']}"
    if record.get("pages"):
        where += f":{record['pages']}" if record.get("volume") else f", {record['pages']}"
    parts = [who or "No author printed", str(record.get("year") or "n.d."), record["title"]]
    return ". ".join(p.strip().rstrip(".") for p in [*parts, where] if p.strip())


def header_from(record: dict, files: list[str], read: str) -> dict[str, str]:
    doi = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", record.get("doi", "").replace(" ", ""))
    return {
        "citation": citation(record),
        "doi": doi,
        "read": read,
        "status": "read",
        "regions": f"[{record.get('region', '').split('(')[0].split(';')[0].strip()}]",
        "files": f"[{', '.join(files)}]",
    }


def scaffold(note_id: str, directory: Path, date: str, fill: dict[str, str] | None = None) -> Path:
    if not re.fullmatch(r"[a-z]+[0-9]{4}[a-z0-9]*", note_id):
        raise ValueError("an id is <surname><year>, lower case, optionally a word: zachos1959")
    path = directory / f"{note_id}.md"
    if path.exists():
        raise FileExistsError(path)
    text = TEMPLATE.format(id=note_id, date=date)
    for key, value in (fill or {}).items():
        if any(c in value for c in "\n"):
            raise ValueError(f"{key} must be one line")
        text = re.sub(rf"^{key}:.*$", f"{key}: {value}".rstrip(), text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> int:
    import datetime

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("id")
    parser.add_argument(
        "--dir", type=Path, default=Path(__file__).resolve().parent.parent / "literature"
    )
    parser.add_argument("--triage", type=Path, help="a triage agent's JSON: a list of records")
    parser.add_argument("--key", help="the record's key in --triage")
    parser.add_argument("--files", default="", help="dropped file names, comma-separated")
    parser.add_argument("--read", default="", help="the note's `read` field")
    args = parser.parse_args()
    fill = None
    if args.triage:
        records = {r["key"]: r for r in json.loads(args.triage.read_text(encoding="utf-8"))}
        files = [f.strip() for f in args.files.split(",") if f.strip()]
        fill = header_from(records[args.key], files, args.read)
    path = scaffold(args.id, args.dir, datetime.date.today().isoformat(), fill)
    print(f"wrote {path}; fill it in and add it to {args.dir / 'README.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
