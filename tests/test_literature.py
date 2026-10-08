"""The literature notes' headers: required keys, known statuses, and ids that exist."""

from __future__ import annotations

import re
from pathlib import Path

from formularium.catalogue import FORMULATIONS
from formularium.datasets import DATASETS
from formularium.records import AUTHOR_SOURCES

LITERATURE = Path(__file__).resolve().parent.parent / "literature"
REQUIRED = ("id", "citation", "read", "status", "diseases", "crops", "regions", "processes")
LISTS = ("diseases", "crops", "regions", "processes", "records", "datasets")


def _header(path: Path) -> dict[str, str | list[str]]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert match, f"{path.name}: no header"
    header: dict[str, str | list[str]] = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if key in LISTS:
            assert value.startswith("[") and value.endswith("]"), (path.name, key)
            header[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        else:
            header[key] = value
    return header


def _notes() -> list[Path]:
    return sorted(p for p in LITERATURE.glob("*.md") if p.name not in ("README.md", "INGESTING.md"))


def test_every_note_has_a_valid_header() -> None:
    assert _notes()
    for path in _notes():
        header = _header(path)
        for key in REQUIRED:
            assert header.get(key) not in (None, ""), (path.name, key)
        assert header["id"] == path.stem, path.name
        assert header["status"] in AUTHOR_SOURCES, path.name


def test_a_notes_records_and_datasets_exist() -> None:
    for path in _notes():
        header = _header(path)
        for record in header.get("records", []):
            assert record in FORMULATIONS, (path.name, record)
        for data in header.get("datasets", []):
            assert data in DATASETS, (path.name, data)


def test_the_index_lists_every_note() -> None:
    index = (LITERATURE / "README.md").read_text(encoding="utf-8")
    linked = set(re.findall(r"\]\(([a-z0-9]+)\.md\)", index))
    assert linked == {p.stem for p in _notes()}


def test_a_scaffolded_note_has_every_key(tmp_path: Path) -> None:
    import importlib.util

    script = LITERATURE.parent / "scripts" / "new_note.py"
    spec = importlib.util.spec_from_file_location("new_note", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    path = module.scaffold("someone2020", tmp_path, "2026-10-08")
    header = _header(path)
    assert set(REQUIRED) | set(LISTS) <= set(header)
    assert header["id"] == "someone2020"
