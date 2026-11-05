"""The dataset store: one folder outside git holding the data our passes download or assemble.

    python scripts/datastore.py add RECORD.json [--store DIR] [--go]
    python scripts/datastore.py check [--store DIR] [--quick]
    python scripts/datastore.py list [--store DIR]

Data stay out of every repository, as papers do, so the store lives beside the paper library:
DIR defaults to `$FORMULARIUM_DATASETS`, else `datasets` beside `$FORMULARIUM_LIBRARY`. Its layout:

- `<id>/data/`: the files, as downloaded or as assembled, read-only.
- `<id>/scripts/`: the scripts that built them, so a derived table can be built again.
- `<id>/dataset.json`: where it came from, its licence and where that is stated, its rights
  (`shareable`, `local-only`), which store datasets it was built from, and how to rebuild it.
- `manifest.tsv`: one row per file: dataset, path, sha256, bytes, where it was copied from.

`add` copies and never moves or overwrites; without `--go` it prints the plan. It refuses:
- a record with a field missing, or `shareable` without a stated licence: an unknown licence is
  `local-only`;
- a derived dataset with neither a script nor a `how`;
- a dataset built from one not in the store, or looser in rights than what it was built from;
- anything from Meteocat, whose readings, and scores resting on them, stay in Cooptera.
`check` finds files missing, changed or not in the manifest (`--quick`: sizes, not checksums).
Standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path

FIELDS = [
    "id",
    "title",
    "kind",
    "source",
    "licence",
    "licence_where",
    "rights",
    "retrieved",
    "from",
    "made_by",
    "how",
    "record",
    "used_by",
    "notes",
    "data",
    "scripts",
]
KINDS = ("raw", "derived")
RIGHTS = ("shareable", "local-only")
SKIP = {"__pycache__", ".git", "venv", ".venv"}
NOT_HERE = re.compile(r"meteocat|\bxema\b|/xema(/|$)", re.IGNORECASE)
MANIFEST = "manifest.tsv"
HEADER = "dataset\tpath\tsha256\tbytes\tsource\n"


def default_store() -> Path | None:
    if os.environ.get("FORMULARIUM_DATASETS"):
        return Path(os.environ["FORMULARIUM_DATASETS"])
    library = os.environ.get("FORMULARIUM_LIBRARY")
    return Path(library).parent / "datasets" if library else None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1 << 20):
            digest.update(chunk)
    return digest.hexdigest()


def files_under(path: Path) -> list[Path]:
    """A file, or a folder's files, without caches and virtual environments."""
    if path.is_file():
        return [path]
    return sorted(
        p
        for p in path.rglob("*")
        if p.is_file() and not SKIP & set(p.relative_to(path).parts) and p.suffix != ".pyc"
    )


def held(store: Path) -> dict[str, dict[str, object]]:
    records = {}
    for path in sorted(store.glob("*/dataset.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        records[record["id"]] = record
    return records


def faults(record: dict[str, object], store: Path) -> list[str]:
    """Why this record may not enter the store: every reason, not the first."""
    missing = [f for f in FIELDS if f not in record]
    if missing:
        return [f"missing fields: {', '.join(missing)}"]
    found = []
    if not re.fullmatch(r"[a-z0-9]+([._-][a-z0-9]+)*", str(record["id"])):
        found.append(f"bad id: {record['id']!r}")
    if record["kind"] not in KINDS:
        found.append(f"kind must be one of {KINDS}")
    if record["rights"] not in RIGHTS:
        found.append(f"rights must be one of {RIGHTS}")
    if not record["source"]:
        found.append("no source")
    if not record["data"]:
        found.append("no data")
    if record["rights"] == "shareable" and (
        record["licence"] in ("", "unknown") or not record["licence_where"]
    ):
        found.append("shareable needs a licence, and where it is stated")
    if record["kind"] == "derived" and not (record["scripts"] or record["how"]):
        found.append("a derived dataset needs a script, or a `how`")
    text = [record[k] for k in ("id", "title", "source", "made_by")]
    text += [*record["data"], *record["scripts"]]  # type: ignore[misc]
    if any(NOT_HERE.search(str(t)) for t in text):
        found.append("Meteocat's readings stay in Cooptera")
    others = held(store) if store.is_dir() else {}
    for parent in record["from"]:  # type: ignore[attr-defined]
        if parent not in others:
            found.append(f"built from {parent}, which is not in the store")
        elif others[parent]["rights"] == "local-only" and record["rights"] == "shareable":
            found.append(f"built from {parent}, which is local-only, so this is too")
    for path in [*record["data"], *record["scripts"]]:  # type: ignore[misc]
        if not Path(path).exists():
            found.append(f"no such path: {path}")
    return found


def plan(record: dict[str, object]) -> list[tuple[Path, str]]:
    """(source file, path inside the dataset) for every file; names must not collide."""
    pairs = []
    for folder in ("data", "scripts"):
        for item in record[folder]:  # type: ignore[attr-defined]
            root = Path(item)
            for path in files_under(root):
                inner = path.name if root.is_file() else f"{root.name}/{path.relative_to(root)}"
                pairs.append((path, f"{folder}/{inner}"))
    names = [dest for _, dest in pairs]
    clashes = sorted({n for n in names if names.count(n) > 1})
    if clashes:
        raise SystemExit(f"two sources share a name: {clashes[:3]}")
    return pairs


def add(record_path: Path, store: Path, go: bool) -> int:
    record = json.loads(record_path.read_text(encoding="utf-8"))
    home = store / str(record.get("id"))
    if home.exists():
        print(f"{record['id']}: already in the store; nothing is overwritten", file=sys.stderr)
        return 1
    found = faults(record, store)
    if found:
        print(f"{record.get('id')}: refused:", *found, sep="\n  ", file=sys.stderr)
        return 1
    pairs = plan(record)
    size = sum(p.stat().st_size for p, _ in pairs)
    print(f"plan: {record['id']}: {len(pairs)} files, {size / 1e6:.1f} MB, {record['rights']}")
    if not go:
        return 0
    store.mkdir(parents=True, exist_ok=True)
    rows = []
    for source, inner in pairs:
        dest = home / inner
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
        digest = sha256(dest)
        if digest != sha256(source):
            raise SystemExit(f"copy differs from its source: {source}")
        dest.chmod(0o444)
        rows.append(f"{record['id']}\t{inner}\t{digest}\t{dest.stat().st_size}\t{source}\n")
    (home / "dataset.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    manifest = store / MANIFEST
    with manifest.open("a", encoding="utf-8") as f:
        if manifest.stat().st_size == 0:
            f.write(HEADER)
        f.writelines(rows)
    print(f"added {record['id']}: {len(rows)} files, checksums verified")
    return 0


def check(store: Path, quick: bool) -> int:
    problems = []
    listed = set()
    manifest = store / MANIFEST
    lines = manifest.read_text(encoding="utf-8").splitlines()[1:] if manifest.exists() else []
    for line in lines:
        dataset, inner, digest, size, _ = line.split("\t")
        path = store / dataset / inner
        listed.add(path)
        if not path.is_file():
            problems.append(f"{dataset}/{inner}: missing")
        elif path.stat().st_size != int(size) or (not quick and sha256(path) != digest):
            problems.append(f"{dataset}/{inner}: checksum changed")
    for home in sorted(p for p in store.iterdir() if p.is_dir()) if store.is_dir() else []:
        if not (home / "dataset.json").is_file():
            problems.append(f"{home.name}: no dataset.json")
        for path in sorted(p for p in home.rglob("*") if p.is_file()):
            if path.name != "dataset.json" and path not in listed:
                problems.append(f"{home.name}/{path.relative_to(home)}: not in the manifest")
    print(*problems, sep="\n") if problems else None
    print(
        f"{len(listed)} files in {len(held(store)) if store.is_dir() else 0} datasets; "
        f"{len(problems)} problems"
    )
    return 1 if problems else 0


def listing(store: Path) -> int:
    sizes: dict[str, int] = {}
    manifest = store / MANIFEST
    for line in manifest.read_text(encoding="utf-8").splitlines()[1:]:
        dataset, _, _, size, _ = line.split("\t")
        sizes[dataset] = sizes.get(dataset, 0) + int(size)
    for key, record in held(store).items():
        mb = sizes.get(key, 0) / 1e6
        print(f"{key}\t{record['kind']}\t{record['rights']}\t{record['licence']}\t{mb:.1f} MB")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("add", "check", "list"):
        p = sub.add_parser(name)
        p.add_argument("--store", type=Path, default=default_store())
        if name == "add":
            p.add_argument("record", type=Path)
            p.add_argument("--go", action="store_true")
        if name == "check":
            p.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    if args.store is None:
        parser.error("no store: set FORMULARIUM_DATASETS or FORMULARIUM_LIBRARY, or use --store")
    if args.command == "add":
        return add(args.record, args.store, args.go)
    if args.command == "check":
        return check(args.store, args.quick)
    return listing(args.store)


if __name__ == "__main__":
    sys.exit(main())
