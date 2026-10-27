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
plan. A first build makes the library; `build --add` adds to one that exists: papers whose
notes are not yet filed, a note's paper found in `inbound/` (moved to its id), and new
papers without notes (to `inbound/`); anything already held, by checksum, is left alone.
`check` finds notes whose files are not in the library, files not in the manifest,
and copies whose checksum changed. `file` moves a paper from `inbound/` (or copies one from
elsewhere) to its note's id once the note names it. Standard library only.

A note's `files` may annotate a name, as `paper.pdf (the 2026-10-18 drop, supplied by
Chris)`: the annotation is dropped, commas inside it do not split the list.
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
        notes[path.stem] = file_names(header.get("files", ""))
    return notes


def file_names(field: str) -> list[str]:
    """The file names a note's `files` lists, without their annotations.

    `[a.pdf (the 10-18 drop, supplied by Chris), b.pdf]` gives `a.pdf` and `b.pdf`: commas
    inside parentheses do not split, and a parenthesis after a name's extension is dropped."""
    field = field.strip()
    if field.startswith("[") and field.endswith("]"):
        field = field[1:-1]
    pieces, depth, current = [], 0, ""
    for char in field:
        depth += {"(": 1, ")": -1}.get(char, 0)
        if char == "," and depth <= 0:
            pieces.append(current)
            current, depth = "", 0
        else:
            current += char
    pieces.append(current)
    names = []
    for piece in pieces:
        piece = piece.strip()
        if piece.endswith(")"):  # a closing annotation, as in `a.pdf (the 10-18 drop)`
            depth = 0
            for i in range(len(piece) - 1, -1, -1):
                depth += {")": 1, "(": -1}.get(piece[i], 0)
                if depth == 0:
                    head = piece[:i].rstrip()
                    if re.search(r"\.[A-Za-z0-9]{2,5}$", head):
                        piece = head
                    break
        if piece:
            names.append(piece)
    return names


def _is_pdf(path: Path) -> bool:
    with open(path, "rb") as f:
        return f.read(5) == b"%PDF-"


def _alias(path: Path) -> str:
    """`text/altieri_2023/paper.pdf` is `altieri_2023.pdf`, the name its note gives."""
    return path.parent.name + path.suffix


def plan(notes: dict[str, list[str]], drops: list[Path]) -> tuple[list[Copy], list[str]]:
    """What `build` would copy, and the problems found (a named file missing, or copies
    of one name that differ)."""
    by_name: dict[str, list[Path]] = {}
    for drop in drops:
        for path in sorted(drop.rglob("*")):
            if path.is_file():
                by_name.setdefault(path.name, []).append(path)
                if path.stem == "paper":  # extract_paper.py's text/<key>/paper.pdf
                    by_name.setdefault(_alias(path), []).append(path)
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
            rejected = any(p.startswith("rejected") for p in path.parts)
            if path.suffix.lower() == ".pdf" and not _is_pdf(path):
                rejected = True  # a failed download saved as .pdf: an HTML page, say
            folder = "rejected" if rejected else "inbound"
            name = _alias(path) if path.stem == "paper" else path.name
            dest, n = f"{folder}/{name}", 1
            while dest in taken:
                dest, n = f"{folder}/{Path(name).stem}.{n}{path.suffix}", n + 1
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


def add_plan(
    copies: list[Copy], problems: list[str], notes: dict[str, list[str]], library: Path
) -> tuple[list[tuple[Copy, bool]], list[str]]:
    """What `build --add` would place, each with whether it moves out of `inbound/`, and the
    problems that remain: a note's file already filed is no problem, wherever it was found."""
    rows = read_manifest(library)
    filed = {(r["note"], r["original_name"]) for r in rows}
    by_sum: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        by_sum.setdefault(r["sha256"], []).append(r)
    taken = {r["path"] for r in rows}
    owner = {r["path"]: r["note"] for r in rows}
    left = [
        p
        for p in problems
        if not any(
            p.startswith(f"{note}: {name} ") and (note, name) in filed
            for note, names in notes.items()
            for name in names
        )
    ]
    placed: list[tuple[Copy, bool]] = []
    for c in copies:
        if c.note and (c.note, c.original) in filed:
            continue
        held = by_sum.get(sha256(c.source), [])
        if not c.note and held:
            continue  # a paper without a note, already held somewhere
        if any(r["note"] == c.note for r in held):
            continue  # this note already holds these bytes under another name
        inbound = [r for r in held if r["note"] == "" and r["path"].startswith("inbound/")]
        dest = c.dest
        if dest in taken and dest.endswith(".txt") and owner.get(dest) == c.note:
            continue  # the note already has its text copy (an excerpt, say): keep it
        if dest in taken:
            if c.note:
                left.append(f"{c.note}: {dest} is taken by another file; not filed")
                continue
            stem, suffix, n = Path(dest).stem, Path(dest).suffix, 1
            while dest in taken:
                dest, n = f"inbound/{stem}.{n}{suffix}", n + 1
        taken.add(dest)
        move = bool(inbound)  # a note's paper waiting in inbound/: move it to the note's id
        source = library / inbound[0]["path"] if inbound else c.source
        placed.append((Copy(c.note, c.original, source, dest), move))
    return placed, left


def add(copies, problems, notes, library: Path, go: bool) -> int:
    """`build --add`: print the plan, and with `go` place the files and extend the manifest."""
    placed, left = add_plan(copies, problems, notes, library)
    to_notes = [c for c, _ in placed if c.note]
    print(
        f"to add: {sum(1 for c in to_notes if not c.dest.endswith('.txt'))} papers and "
        f"{sum(1 for c in to_notes if c.dest.endswith('.txt'))} text copies under note ids"
        f" ({sum(1 for c, m in placed if m)} moved from inbound/);"
        f" {sum(1 for c, _ in placed if c.dest.startswith('inbound/'))} to inbound/,"
        f" {sum(1 for c, _ in placed if c.dest.startswith('rejected/'))} to rejected/"
    )
    for problem in left:
        print("problem:", problem)
    for c, move in placed:
        print("plan:", c.dest, "<-", c.source.name, "(move)" if move else "")
    if not go:
        return 0
    rows = read_manifest(library)
    for c, move in placed:
        new = _place(c.source, library, c.dest, c.note, c.original, move=move)
        if move:
            moved_from = c.source.relative_to(library).as_posix()
            rows = [r for r in rows if r["path"] != moved_from]
        rows.append(new)
        write_manifest(library, rows)
    print(f"added {len(placed)} files; checksums verified")
    return 0


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
    b.add_argument("--add", action="store_true", help="add to a library that exists")
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
        if args.add:  # prints its own plan and only the problems that remain
            return add(copies, problems, notes, args.library, args.go)
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
            sys.exit("the library already has a manifest: use build --add, check and file")
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
