"""Start a literature note with the header and sections literature/README.md asks for.

    python scripts/new_note.py zachos1959 [--dir literature]

Writes literature/<id>.md, refusing to overwrite. Fill in every field, then add a line
for the note to the index in literature/README.md; tests/test_literature.py fails until
both are done properly (an empty `status` is not one of the allowed values).
"""

from __future__ import annotations

import argparse
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


def scaffold(note_id: str, directory: Path, date: str) -> Path:
    if not re.fullmatch(r"[a-z]+[0-9]{4}[a-z0-9]*", note_id):
        raise ValueError("an id is <surname><year>, lower case, optionally a word: zachos1959")
    path = directory / f"{note_id}.md"
    if path.exists():
        raise FileExistsError(path)
    path.write_text(TEMPLATE.format(id=note_id, date=date), encoding="utf-8")
    return path


def main() -> int:
    import datetime

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("id")
    parser.add_argument(
        "--dir", type=Path, default=Path(__file__).resolve().parent.parent / "literature"
    )
    args = parser.parse_args()
    path = scaffold(args.id, args.dir, datetime.date.today().isoformat())
    print(f"wrote {path}; fill it in and add it to {args.dir / 'README.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
