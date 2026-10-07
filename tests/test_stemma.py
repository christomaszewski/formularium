"""The kinship graph: borrowed equations, shared people, shared structure, and the hold-out."""

from __future__ import annotations

import dataclasses

from formularium import stemma
from formularium.catalogue import FORMULATIONS
from formularium.records import Formulation

# The engine's models as Agrarium last listed them (cooptera@4818d26), enough for these tests.
ENGINE = (
    "goidanich.incubation",
    "kennelly2007.trigger",
    "rule-3-10",
    "magarey2010.rules",
    "magarey2005.generic",
    "brischetto2021.secondary",
    "rossi2008.primary",
    "caffi2013.sporulation",
    "sentelhas2008.wetness",
    "rh90.wetness",
    "vitimeteo.oospores",
)


def _with(**entries: Formulation) -> dict[str, Formulation]:
    return {**FORMULATIONS, **entries}


def _candidate(**over) -> Formulation:
    base = Formulation(
        "secondary infection",
        "a candidate",
        year=1993,
        authors=("Somebody, A.",),
        authors_complete=True,
        authors_from="read",
    )
    return dataclasses.replace(base, **over)


def test_a_formulation_is_its_own_kin() -> None:
    assert stemma.link("rossi2008.primary", "rossi2008.primary") == "the same formulation"


def test_a_shared_author_is_kinship() -> None:
    # Fedele 2025 is Rossi's and Caffi's too.
    assert "rossi2008.primary" in stemma.kin("fedele2025.dose", ENGINE)
    assert "caffi2013.sporulation" in stemma.kin("fedele2025.dose", ENGINE)
    # Kennelly 2007 and Magarey's fact sheet share a surname: kin, the safe way round.
    assert "magarey2010.rules" in stemma.kin("kennelly2007.trigger", ENGINE)


def test_sentelhas_makes_florence_and_gillespie_kin() -> None:
    cat = _with(
        plasmo=_candidate(authors=("Orlandini, S.", "Rosa, M.")),
        pedro1982=_candidate(authors=("Pedro, M. J.", "Gillespie, T. J."), year=1982),
    )
    assert "sentelhas2008.wetness" in stemma.kin("plasmo", ENGINE, cat)
    assert "sentelhas2008.wetness" in stemma.kin("pedro1982", ENGINE, cat)


def test_a_borrowed_equation_is_kinship_without_a_shared_author() -> None:
    cat = _with(**{"uses-magarey": _candidate(borrows=("magarey2005.generic",))})
    found = {f.other: f.reason for f in stemma.links("uses-magarey", ENGINE, cat)}
    assert found["magarey2005.generic"] == "a borrowed equation"
    assert found["brischetto2021.secondary"] == "a borrowed equation"  # both compute it


def test_an_unrelated_group_is_not_kin() -> None:
    cat = _with(ohio=_candidate(authors=("Lalancette, N.", "Madden, L. V.", "Ellis, M. A.")))
    assert stemma.kin("ohio", ENGINE, cat) == []
    # A formulation nobody published, with no authors, has no kin through people.
    assert stemma.kin("kernel.mixture", ENGINE) == []


def test_the_hold_out_takes_kin_and_shared_structure() -> None:
    held = stemma.hold_out(["rossi2008.primary", "fedele2025.dose"], ENGINE)
    assert "rossi2008.primary" in held  # the truth's own model
    assert "caffi2013.sporulation" in held  # Rossi's group, through Fedele and Rossi
    assert "brischetto2021.secondary" in held  # Rossi again
    assert "rh90.wetness" not in held  # Cooptera's own, unrelated
    # A rain-and-temperature trigger as the truth holds out every engine trigger.
    cat = _with(trigger=_candidate(structure="rain-temperature-trigger"))
    held = stemma.hold_out(["trigger"], ENGINE, cat)
    assert {"kennelly2007.trigger", "rule-3-10", "magarey2010.rules"} <= set(held)
    assert all("the same structure" in r for r in held["rule-3-10"])


def test_an_unrelated_truth_holds_out_nothing() -> None:
    cat = _with(ohio=_candidate(authors=("Lalancette, N.", "Madden, L. V.", "Ellis, M. A.")))
    assert stemma.hold_out(["ohio", "kernel.mixture"], ENGINE, cat) == {}
