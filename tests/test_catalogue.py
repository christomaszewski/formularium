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


def test_the_calibration_data_recorded_so_far() -> None:
    """Each link read in its paper (2026-10-07 to 09); Rossi's Goidanich link since 2026-10-09."""
    recorded = {name: f.calibrated_on for name, f in FORMULATIONS.items() if f.calibrated_on}
    assert recorded == {
        "goidanich.incubation": ("goidanich1957",),
        "rossi2008.primary": ("goidanich1957", "laviola1986"),
        "rossi2002.onset": ("rossi2002.emilia",),
        "keil2007.sporulation": ("keil2007.freiburg",),
        "keil2007.sun_mortality": ("keil2007.freiburg",),
        "puelles2024.ur": ("puelles2024.rioja",),
        "rosa1995.incubation": ("goidanich1957", "zachos1959", "orlandini1993.emergences"),
        "orlandini2008.plasmo": (
            "orlandini2008.mondeggi",
            "blaeser1978.survival",
            "lalancette1988a",
            "goidanich1957",
        ),
        "rossi2008pp.dormancy": ("rossi2008pp.discs",),
        "brischetto2021.secondary": ("blaeser1979", "caffi2016"),
        "magarey2005.generic": ("blaeser1979", "caffi2016"),
        "madden1999.detection_bound": ("madden1995",),
        "cortazar2009.budburst": ("phenoclim",),
        "cortazar2009.brin": ("phenoclim",),
        "ramos2017.budburst": ("ramos2017.penedes",),
        "molitor2014.shoots": ("molitor2014.mt60",),
        "ferguson2014.cold_hardiness": ("ferguson2014.prosser",),
        "leoni2026.oospores": ("leoni2026.changins",),
        "zachos1959.incubation": ("zachos1959",),
        "zachos1959.sporangia_survival": ("zachos1959.conidia",),
        "kennelly2007.lesion_decline": ("kennelly2007.loxton",),
        "rafaila1968.incubation": ("rafaila1968",),
        "lalancette1988.infection": ("lalancette1988a",),
        "tranmanhsung1990.pom": ("tranmanhsung1990.bordeaux",),
        # Read 2026-10-09 in the papers; the 1978 and goidanich1957 links are inferred.
        "blaeser1979.survival": ("blaeser1978.survival", "blaeser1979"),
        "rosa1993.incubation": ("goidanich1957",),
        "orlandini1993.incubation": ("goidanich1957", "orlandini1993.emergences"),
        "orlandini1993.infection": ("blaeser1979", "orlandini1993.emergences"),
        "orlandini1993.survival": ("blaeser1978.survival",),
        "rouzet2003.cold_days": ("rouzet2003.balma",),
        "kennelly2007.trigger": ("kennelly2006.chancellor",),
    }
