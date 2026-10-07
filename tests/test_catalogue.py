"""The catalogue's own bookkeeping: known tags, settled sources, and equations that exist."""

from __future__ import annotations

import importlib
import re

from formularium.catalogue import FORMULATIONS
from formularium.records import AUTHOR_SOURCES, MAKERS, STRUCTURES


def test_every_record_uses_known_tags_and_sources() -> None:
    for name, f in FORMULATIONS.items():
        assert not f.structure or f.structure in STRUCTURES, name
        assert (f.authors_from in AUTHOR_SOURCES) == bool(f.authors), name
        assert f.made_by in MAKERS, name
        for b in f.borrows:
            assert b in FORMULATIONS, (name, b)
        for p in f.parameters:
            assert p.checked in AUTHOR_SOURCES and p.unit and p.where, (name, p.name)


def test_every_published_record_has_authors_or_says_why_not() -> None:
    # A published formulation names its authors; NOAA's solar position names an agency.
    for name, f in FORMULATIONS.items():
        if not f.made_by and not f.authors:
            assert name == "noaa.solar-position", name


def test_ids_are_lower_case_ascii() -> None:
    for name in FORMULATIONS:
        assert re.fullmatch(r"[a-z0-9][a-z0-9.\-]*", name), name


def test_every_equations_module_exists_and_names_its_formulation() -> None:
    for name, f in FORMULATIONS.items():
        if f.equations:
            module = importlib.import_module(f"formularium.equations.{f.equations}")
            assert name == module.FORMULATION, name


def test_a_dois_shape() -> None:
    for name, f in FORMULATIONS.items():
        assert not f.doi or f.doi.startswith("10."), name
