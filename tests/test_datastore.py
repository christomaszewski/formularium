"""The dataset store: what it refuses, and what `check` finds."""

import json
import stat
import subprocess
import sys
from pathlib import Path

import pytest

TOOL = Path(__file__).parent.parent / "scripts" / "datastore.py"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True)


def record(tmp: Path, **changes: object) -> Path:
    (tmp / "src").mkdir(exist_ok=True)
    (tmp / "src" / "a.csv").write_text("x\n1\n")
    (tmp / "build.py").write_text("print(1)\n")
    fields: dict[str, object] = {
        "id": "demo.table",
        "title": "A table",
        "kind": "raw",
        "source": "https://example.org/a",
        "licence": "CC BY 4.0",
        "licence_where": "the page",
        "rights": "shareable",
        "retrieved": "2026-11-05",
        "from": [],
        "made_by": "a test",
        "how": "download it",
        "record": "",
        "used_by": [],
        "notes": "",
        "data": [str(tmp / "src")],
        "scripts": [],
    }
    fields.update(changes)
    path = tmp / f"{fields['id']}.json"
    path.write_text(json.dumps(fields))
    return path


def add(tmp: Path, **changes: object) -> subprocess.CompletedProcess[str]:
    return run("add", str(record(tmp, **changes)), "--store", str(tmp / "store"), "--go")


def test_a_plan_writes_nothing(tmp_path: Path) -> None:
    result = run("add", str(record(tmp_path)), "--store", str(tmp_path / "store"))
    assert result.returncode == 0 and "plan" in result.stdout
    assert not (tmp_path / "store" / "demo.table").exists()


def test_add_copies_records_and_passes_check(tmp_path: Path) -> None:
    assert add(tmp_path).returncode == 0
    home = tmp_path / "store" / "demo.table"
    assert (home / "data" / "src" / "a.csv").read_text() == "x\n1\n"
    assert (tmp_path / "src" / "a.csv").exists(), "a source is copied, never moved"
    assert json.loads((home / "dataset.json").read_text())["licence"] == "CC BY 4.0"
    assert not (home / "data" / "src" / "a.csv").stat().st_mode & stat.S_IWUSR
    check = run("check", "--store", str(tmp_path / "store"))
    assert check.returncode == 0 and "0 problems" in check.stdout


def test_an_id_is_never_overwritten(tmp_path: Path) -> None:
    assert add(tmp_path).returncode == 0
    again = add(tmp_path)
    assert again.returncode != 0 and "already" in again.stderr


@pytest.mark.parametrize(
    ("changes", "why"),
    [
        ({"licence": "unknown"}, "shareable"),
        ({"rights": "public"}, "rights"),
        ({"kind": "other"}, "kind"),
        ({"source": ""}, "source"),
        ({"id": "Bad Id"}, "id"),
        ({"kind": "derived", "scripts": [], "how": ""}, "script"),
        ({"from": ["not.there"]}, "not.there"),
        ({"source": "https://example.org/meteocat/x"}, "Meteocat"),
        ({"title": "XEMA readings"}, "Meteocat"),
    ],
)
def test_refused(tmp_path: Path, changes: dict[str, object], why: str) -> None:
    result = add(tmp_path, **changes)
    assert result.returncode != 0 and why in result.stderr
    assert not (tmp_path / "store" / "demo.table").exists()


def test_a_meteocat_path_is_refused(tmp_path: Path) -> None:
    bad = tmp_path / "xema"
    bad.mkdir()
    (bad / "W4.json").write_text("{}")
    result = add(tmp_path, data=[str(bad)])
    assert result.returncode != 0 and "Meteocat" in result.stderr


def test_derived_takes_the_tightest_rights(tmp_path: Path) -> None:
    assert add(tmp_path, id="demo.closed", rights="local-only").returncode == 0
    result = add(tmp_path, id="demo.open", kind="derived", **{"from": ["demo.closed"]})
    assert result.returncode != 0 and "local-only" in result.stderr


def test_caches_are_not_copied(tmp_path: Path) -> None:
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "__pycache__").mkdir()
    (tmp_path / "src" / "__pycache__" / "a.pyc").write_bytes(b"0")
    assert add(tmp_path).returncode == 0
    assert not list((tmp_path / "store").rglob("*.pyc"))


def test_check_finds_a_changed_a_missing_and_a_stray_file(tmp_path: Path) -> None:
    assert add(tmp_path).returncode == 0
    held = tmp_path / "store" / "demo.table" / "data" / "src" / "a.csv"
    held.chmod(0o644)
    held.write_text("changed\n")
    (held.parent / "stray.csv").write_text("x\n")
    check = run("check", "--store", str(tmp_path / "store"))
    assert check.returncode != 0
    assert "checksum changed" in check.stdout and "not in the manifest" in check.stdout
    held.unlink()
    assert "missing" in run("check", "--store", str(tmp_path / "store")).stdout
