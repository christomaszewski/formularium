"""The paper library: one folder outside git holding every paper a literature note names.

    python scripts/library.py build DROP [DROP ...] [--library LIB] [--go]
    python scripts/library.py check [--library LIB]
    python scripts/library.py file ID PAPER [--text TXT] [--library LIB]

Papers stay out of every repository, so the library lives on the machines that hold the
papers; LIB defaults to `$FORMULARIUM_LIBRARY`. Its layout:

- `<id>.<ext>`: the paper a note names, renamed to the note's id; a note's second file is
  `<id>-2.<ext>`. Its text copy, where one exists, is `<id>.txt` beside it.
- `inbound/`: papers without a note yet, under the names they came with, one copy each
  (by checksum). `rejected/`: what a drop set aside as not papers.
- `manifest.tsv`: one row per file: note, path, the original file name (what the note's
  `files` holds), sha256, bytes, and where it was copied from.

`build` copies from the drops and never moves or overwrites; without `--go` it prints the
plan. `check` finds notes whose files are not in the library, files not in the manifest,
and copies whose checksum changed. `file` moves a paper from `inbound/` (or copies one from
elsewhere) to its note's id once the note names it. Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

NOTES = Path(__file__).resolve().parent.parent / "literature"
PAPER = {".pdf", ".docx", ".pptx", ".xlsx", ".tif", ".epub"}
COLUMNS = ("note", "path", "original_name", "sha256", "bytes", "copied_from")


@dataclass(frozen=True)
class Copy:
    note: str  # "" for inbound and rejected
    original: str
    source: Path
    dest: str  # relative to the library


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def note_files(directory: Path) -> dict[str, list[str]]:
    """Each note's `files`, by note id."""
    notes = {}
    for path in sorted(directory.glob("*.md")):
        match = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
        if not match:
            continue
        header = dict(line.partition(":")[::2] for line in match.group(1).splitlines())
        files = header.get("files", "").strip().strip("[]")
        notes[path.stem] = [f.strip() for f in files.split(",") if f.strip()]
    return notes


def plan(notes: dict[str, list[str]], drops: list[Path]) -> tuple[list[Copy], list[str]]:
    """What `build` would copy, and the problems found (a named file missing, or copies
    of one name that differ)."""
    by_name: dict[str, list[Path]] = {}
    for drop in drops:
        for path in sorted(drop.rglob("*")):
            if path.is_file():
                by_name.setdefault(path.name, []).append(path)
    copies, problems, noted = [], [], set()
    for note, files in sorted(notes.items()):
        papers = [f for f in files if Path(f).suffix.lower() != ".txt"]
        for i, name in enumerate(papers):
            found = by_name.get(name, [])
            if not found:
                problems.append(f"{note}: {name} is in no drop")
                continue
            sums = {sha256(p) for p in found}
            if len(sums) > 1:
                problems.append(f"{note}: copies of {name} differ")
            noted |= sums
            base = note if i == 0 else f"{note}-{i + 1}"
            copies.append(Copy(note, name, found[0], base + Path(name).suffix.lower()))
            text = Path(name).stem + ".txt"
            if text in by_name:
                copies.append(Copy(note, text, by_name[text][0], base + ".txt"))
    seen: set[str] = set()
    taken = {c.dest for c in copies}
    for _name, paths in sorted(by_name.items()):
        for path in paths:
            if path.suffix.lower() not in PAPER:
                continue
            digest = sha256(path)
            if digest in noted or digest in seen:
                continue
            seen.add(digest)
            folder = "rejected" if any(p.startswith("rejected") for p in path.parts) else "inbound"
            dest, n = f"{folder}/{path.name}", 1
            while dest in taken:
                dest, n = f"{folder}/{path.stem}.{n}{path.suffix}", n + 1
            taken.add(dest)
            copies.append(Copy("", path.name, path, dest))
    return copies, problems


def read_manifest(library: Path) -> list[dict[str, str]]:
    path = library / "manifest.tsv"
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_manifest(library: Path, rows: list[dict[str, str]]) -> None:
    with open(library / "manifest.tsv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _place(source: Path, library: Path, dest: str, note: str, original: str, move: bool) -> dict:
    target = library / dest
    if target.exists():
        sys.exit(f"refusing to overwrite {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    digest = sha256(source)
    (shutil.move if move else shutil.copy2)(source, target)
    if sha256(target) != digest:
        sys.exit(f"checksum changed copying {source} to {target}")
    home = str(Path.home())
    return {
        "note": note,
        "path": dest,
        "original_name": original,
        "sha256": digest,
        "bytes": str(target.stat().st_size),
        "copied_from": str(source).replace(home, "~", 1),
    }


def check(notes: dict[str, list[str]], library: Path) -> list[str]:
    rows = read_manifest(library)
    problems = []
    filed = {(r["note"], r["original_name"]) for r in rows}
    for note, files in sorted(notes.items()):
        for name in files:
            if (note, name) not in filed and Path(name).suffix.lower() != ".txt":
                problems.append(f"{note}: {name} is not in the library")
    listed = {r["path"] for r in rows}
    for path in sorted(library.rglob("*")):
        rel = path.relative_to(library).as_posix()
        if path.is_file() and rel != "manifest.tsv" and rel not in listed:
            problems.append(f"{rel}: not in the manifest")
    for row in rows:
        path = library / row["path"]
        if row["note"] and row["note"] not in notes:
            problems.append(f"{row['path']}: its note {row['note']} does not exist")
        if not path.exists():
            problems.append(f"{row['path']}: listed but missing")
        elif sha256(path) != row["sha256"]:
            problems.append(f"{row['path']}: its checksum changed")
    return problems


def file_paper(note: str, paper: Path, text: Path | None, notes: dict, library: Path) -> list:
    if paper.name not in notes.get(note, []):
        sys.exit(f"{note}'s files do not name {paper.name}: add it to the note first")
    rows = read_manifest(library)
    taken = {r["path"] for r in rows}
    base, n = note, 2
    while base + paper.suffix.lower() in taken:
        base, n = f"{note}-{n}", n + 1
    inbound = (library / "inbound").resolve()
    new = [
        _place(
            paper,
            library,
            base + paper.suffix.lower(),
            note,
            paper.name,
            move=paper.resolve().parent == inbound,
        )
    ]
    rows = [r for r in rows if r["path"] != f"inbound/{paper.name}"]
    if text:
        new.append(_place(text, library, base + ".txt", note, text.name, move=False))
    write_manifest(library, rows + new)
    return new


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--library", type=Path, default=os.environ.get("FORMULARIUM_LIBRARY"))
    parser.add_argument("--notes", type=Path, default=NOTES)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("drops", type=Path, nargs="+")
    b.add_argument("--go", action="store_true")
    sub.add_parser("check")
    f = sub.add_parser("file")
    f.add_argument("note")
    f.add_argument("paper", type=Path)
    f.add_argument("--text", type=Path)
    args = parser.parse_args()
    if args.library is None:
        parser.error("give --library or set FORMULARIUM_LIBRARY")
    notes = note_files(args.notes)

    if args.command == "build":
        copies, problems = plan(notes, args.drops)
        filed = [c for c in copies if c.note]
        print(
            f"{len(notes)} notes; {sum(1 for c in filed if not c.dest.endswith('.txt'))} "
            f"papers and {sum(1 for c in filed if c.dest.endswith('.txt'))} text copies "
            f"to the library; {sum(1 for c in copies if c.dest.startswith('inbound/'))} "
            f"to inbound/, {sum(1 for c in copies if c.dest.startswith('rejected/'))} "
            "to rejected/"
        )
        for problem in problems:
            print("problem:", problem)
        if not args.go or problems:
            return 1 if problems else 0
        if read_manifest(args.library):
            sys.exit("the library already has a manifest: use check and file")
        args.library.mkdir(parents=True, exist_ok=True)
        rows = [
            _place(c.source, args.library, c.dest, c.note, c.original, move=False) for c in copies
        ]
        write_manifest(args.library, rows)
        print(f"copied {len(rows)} files; checksums verified")
        return 0
    if args.command == "check":
        problems = check(notes, args.library)
        for problem in problems:
            print(problem)
        print(f"{len(problems)} problems")
        return 1 if problems else 0
    for row in file_paper(args.note, args.paper, args.text, notes, args.library):
        print("filed", row["path"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
