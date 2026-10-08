"""The literature notes' headers: required keys, known statuses, and ids that exist."""

from __future__ import annotations

import re
from pathlib import Path

from formularium.catalogue import FORMULATIONS
from formularium.datasets import DATASETS
from formularium.records import AUTHOR_SOURCES

LITERATURE = Path(__file__).resolve().parent.parent / "literature"
REQUIRED = ("id", "citation", "read", "status", "diseases", "crops", "regions", "processes")
LISTS = ("diseases", "crops", "regions", "processes", "records", "datasets", "files")


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


def _script(name: str):
    import importlib.util
    import sys

    script = LITERATURE.parent / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # a dataclass looks its module up there
    spec.loader.exec_module(module)
    return module


def test_coverage_matches_a_paper_by_its_file_name_or_doi() -> None:
    coverage = _script("coverage")
    notes = [
        coverage.Note("zachos1959", "", ("hellenic_1959_2_4.pdf",)),
        coverage.Note("rossi2013", "10.1007/s10658-012-0114-2", ()),
        coverage.Note("short2000", "10.1/ab12", ()),
    ]
    assert coverage.match("hellenic_1959_2_4.pdf", [], notes) == ["zachos1959"]
    assert coverage.match("s10658-012-0114-2.pdf", [], notes) == ["rossi2013"]
    assert coverage.match("x.pdf", ["10.1007/S10658-012-0114-2"], notes) == ["rossi2013"]
    assert coverage.match("ab12.pdf", [], notes) == []  # too short a suffix to trust
    assert coverage.match("x.pdf", ["10.1/AB12"], notes) == ["short2000"]


def test_every_note_names_its_files_without_a_path() -> None:
    for path in _notes():
        for name in _header(path).get("files", []):
            assert "/" not in name, (path.name, name)


def test_a_scaffolded_note_has_every_key(tmp_path: Path) -> None:
    path = _script("new_note").scaffold("someone2020", tmp_path, "2026-10-08")
    header = _header(path)
    assert set(REQUIRED) | set(LISTS) <= set(header)
    assert header["id"] == "someone2020"
