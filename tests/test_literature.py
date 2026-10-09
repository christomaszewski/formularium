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


def test_cited_by_finds_a_paper_however_its_name_is_written(tmp_path: Path) -> None:
    cited_by = _script("cited_by")
    (tmp_path / "literature").mkdir()
    (tmp_path / "src" / "formularium").mkdir(parents=True)
    (tmp_path / "literature" / "a.md").write_text(
        "- Blaeser & Weltzien 1978 measured survival.\n"
        "- Bläser (1978) is the dissertation.\n"
        "- Blaser et al. found it in 1999, much later.\n"
        "- Giosue, Girometta, Rossi & Bugiani 2002b mapped it.\n",
        encoding="utf-8",
    )
    (tmp_path / "literature" / "giosue2002.md").write_text("Giosuè 2002 itself\n")
    (tmp_path / "src" / "formularium" / "catalogue.py").write_text('"giosue2002.maps": 1\n')
    found = cited_by.search(tmp_path, "Bläser", "1978")
    assert [n for _, n, _ in found] == [1, 2]  # 1999 is not 1978
    found = cited_by.search(tmp_path, "Giosuè", "2002", "giosue2002")
    assert [(p.name, n) for p, n, _ in found] == [("a.md", 4), ("catalogue.py", 1)]


def test_kin_report_reads_an_engine_list_and_gives_reasons(tmp_path: Path) -> None:
    kin_report = _script("kin_report")
    listed = tmp_path / "engine_models.json"
    listed.write_text('{"formulations": [{"id": "goidanich.incubation"}, "rule_3_10"]}')
    assert kin_report.load_engine(listed) == ["goidanich.incubation", "rule_3_10"]
    lines = kin_report.report(["rosa1993.incubation"], ["goidanich.incubation", "rule_3_10"])
    assert lines[0] == "rosa1993.incubation"
    assert "  linked: goidanich.incubation: shared calibration data, goidanich1957" in lines
    assert "  same form: goidanich.incubation: daily-incubation-table" in lines
    assert kin_report.report(["rule_3_10"], ["goidanich.incubation"])[1].startswith("  nothing")


def test_every_note_names_its_files_without_a_path() -> None:
    for path in _notes():
        for name in _header(path).get("files", []):
            assert "/" not in name, (path.name, name)


def test_a_scaffolded_note_has_every_key(tmp_path: Path) -> None:
    path = _script("new_note").scaffold("someone2020", tmp_path, "2026-10-08")
    header = _header(path)
    assert set(REQUIRED) | set(LISTS) <= set(header)
    assert header["id"] == "someone2020"


def test_a_note_filled_from_a_triage_record_puts_surnames_first(tmp_path: Path) -> None:
    new_note = _script("new_note")
    record = {
        "title": "A model",
        "authors": [
            "L. V. Madden",
            "Mélanie Rouxel",
            "Maddalena G.",
            "Carolina Pañitrur-De la Fuente",
        ],
        "year": "2020",
        "journal": "Plant Disease",
        "volume": "84",
        "pages": "1-9",
        "doi": "https://doi.org/10.1/abcdefgh",
        "region": "Ohio (Wooster)",
    }
    fill = new_note.header_from(record, ["a b.pdf"], "2026-10-08, abstract")
    path = new_note.scaffold("madden2020", tmp_path, "2026-10-08", fill)
    header = _header(path)
    assert header["citation"] == (
        "Madden, L. V., Rouxel, Mélanie, Maddalena, G. & Pañitrur-De la Fuente, Carolina."
        " 2020. A model. Plant Disease 84:1-9"
    )
    assert header["doi"] == "10.1/abcdefgh"
    assert header["files"] == ["a b.pdf"]
    assert header["regions"] == ["Ohio"]


def test_quotes_are_found_at_their_line_or_reported(tmp_path: Path) -> None:
    verify = _script("verify_quotes")
    lines = ["Results", "the optimum was 17.5", "°C after 15", "hr of wetness", "", "end"]
    assert verify.find(lines, "17.5 °C after 15 hr", 2, 1) == ("ok", 2)  # across a line break
    assert verify.find(lines, "optimum was 17.5", 6, 1) == ("moved", 2)
    assert verify.find(lines, "optimum was 18", 2, 3) == ("MISSING", None)
    assert verify.find([f"x {chr(0x2212)} 0.24 W"], "x - 0.24 w", 1, 0) == (
        "ok",
        1,
    )  # a Unicode minus


def test_the_library_renames_papers_to_their_notes_and_checks_them(tmp_path: Path) -> None:
    library = _script("library")
    drop, lib = tmp_path / "drop", tmp_path / "lib"
    (drop / "a" / "rejected-documents").mkdir(parents=True)
    (drop / "a" / "Phyto78.pdf").write_bytes(b"paper one")
    (drop / "a" / "Phyto78.txt").write_text("text one")
    (drop / "a" / "supp.PDF").write_bytes(b"supplement")
    (drop / "a" / "copy-of-phyto78.pdf").write_bytes(b"paper one")  # same bytes, other name
    (drop / "a" / "unread.pdf").write_bytes(b"paper two")
    (drop / "a" / "rejected-documents" / "page.pdf").write_bytes(b"not a paper")
    notes = {"lalancette1988": ["Phyto78.pdf", "supp.PDF"], "biggs2016": []}

    copies, problems = library.plan(notes, [drop])
    assert problems == []
    assert sorted(c.dest for c in copies) == [
        "inbound/unread.pdf",
        "lalancette1988-2.pdf",
        "lalancette1988.pdf",
        "lalancette1988.txt",
        "rejected/page.pdf",
    ]
    rows = [library._place(c.source, lib, c.dest, c.note, c.original, move=False) for c in copies]
    library.write_manifest(lib, rows)
    assert (drop / "a" / "Phyto78.pdf").exists()  # copied, never moved
    assert library.check(notes, lib) == []

    notes["newpaper2020"] = ["unread.pdf"]
    library.file_paper("newpaper2020", lib / "inbound" / "unread.pdf", None, notes, lib)
    assert (lib / "newpaper2020.pdf").read_bytes() == b"paper two"
    assert not (lib / "inbound" / "unread.pdf").exists()
    assert library.check(notes, lib) == []

    (lib / "lalancette1988.pdf").chmod(0o644)
    (lib / "lalancette1988.pdf").write_bytes(b"changed")
    notes["missing2001"] = ["gone.pdf"]
    assert library.check(notes, lib) == [
        "missing2001: gone.pdf is not in the library",
        "lalancette1988.pdf: its checksum changed",
    ]
