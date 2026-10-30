"""The library tool's `text` subcommand: a text copy added beside a paper already filed."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "library", Path(__file__).resolve().parents[1] / "scripts" / "library.py"
)
library = importlib.util.module_from_spec(_SPEC)
sys.modules["library"] = library  # its dataclass looks itself up there
_SPEC.loader.exec_module(library)


def _library_with_paper(tmp_path: Path) -> Path:
    lib = tmp_path / "lib"
    lib.mkdir()
    (lib / "smith2020.pdf").write_bytes(b"%PDF-1.4 a paper")
    row = {
        "note": "smith2020",
        "path": "smith2020.pdf",
        "original_name": "paper.pdf",
        "sha256": library.sha256(lib / "smith2020.pdf"),
        "bytes": "16",
        "copied_from": "drop",
    }
    library.write_manifest(lib, [row])
    return lib


def test_text_is_added_beside_its_paper(tmp_path: Path) -> None:
    lib = _library_with_paper(tmp_path)
    txt = tmp_path / "paper.txt"
    txt.write_text("the text", encoding="utf-8")
    row = library.file_text("smith2020", txt, lib)
    assert row["path"] == "smith2020.txt" and (lib / "smith2020.txt").read_text() == "the text"
    rows = library.read_manifest(lib)
    assert [r["path"] for r in rows] == ["smith2020.pdf", "smith2020.txt"]
    assert txt.exists()  # copied, not moved


def test_text_needs_a_filed_paper_and_never_overwrites(tmp_path: Path) -> None:
    lib = _library_with_paper(tmp_path)
    txt = tmp_path / "paper.txt"
    txt.write_text("the text", encoding="utf-8")
    with pytest.raises(SystemExit):
        library.file_text("jones2021", txt, lib)
    library.file_text("smith2020", txt, lib)
    with pytest.raises(SystemExit):
        library.file_text("smith2020", txt, lib)
