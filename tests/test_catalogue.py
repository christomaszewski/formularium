"""The catalogue's own bookkeeping: known tags, settled sources, and equations that exist."""

from __future__ import annotations

import importlib
import re

from formularium.catalogue import FORMULATIONS
from formularium.datasets import DATASETS
from formularium.records import AUTHOR_SOURCES, MAKERS, ROLES, STRUCTURES

# Published by an agency or a standard, with no personal authors.
INSTITUTIONAL = {"noaa.solar_position", "fao56.eq47"}


def test_every_record_uses_known_tags_and_sources() -> None:
    for name, f in FORMULATIONS.items():
        assert f.structures and set(f.structures) <= set(STRUCTURES), name
        assert (f.authors_from in AUTHOR_SOURCES) == bool(f.authors), name
        assert f.made_by in MAKERS, name
        assert f.role in ROLES, name
        for other in f.borrows + f.part_of + f.calibrated_with:
            assert other in FORMULATIONS and other != name, (name, other)
        for data in f.calibrated_on:
            assert data in DATASETS, (name, data)
        for added in f.added_authors:
            assert added.names and added.found in AUTHOR_SOURCES and added.why, name
        for p in f.parameters:
            assert p.checked in AUTHOR_SOURCES and p.unit and p.where, (name, p.name)


def test_every_published_record_has_authors_or_says_why_not() -> None:
    for name, f in FORMULATIONS.items():
        if not f.made_by and not f.authors:
            assert name in INSTITUTIONAL, name


def test_the_roles_judged_so_far() -> None:
    """Agrarium decision D26: every record not listed here is a process."""
    judged = {name: f.role for name, f in FORMULATIONS.items() if f.role != "process"}
    assert judged == {
        "madden1999.detection_bound": "observation",
        "cannon2001.sensitivity": "observation",
        "noaa.solar_position": "reference",
        "alduchov1996.magnus": "reference",
        "fao56.eq47": "reference",
        "amerine1944.winkler_index": "reference",
        "hughes2017.scoring": "reference",
    }


def test_ids_are_lower_case_ascii() -> None:
    for name in FORMULATIONS:
        assert re.fullmatch(r"[a-z0-9][a-z0-9._\-]*", name), name


def test_every_equations_module_exists_and_names_its_formulation() -> None:
    for name, f in FORMULATIONS.items():
        if f.equations:
            module = importlib.import_module(f"formularium.equations.{f.equations}")
            assert name == module.FORMULATION, name


def test_a_dois_shape() -> None:
    for name, f in FORMULATIONS.items():
        assert not f.doi or f.doi.startswith("10."), name


def test_every_dataset_says_where_its_use_was_read() -> None:
    for name, d in DATASETS.items():
        assert d.citation and d.where and d.checked in AUTHOR_SOURCES, name
