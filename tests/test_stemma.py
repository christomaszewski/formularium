"""The kinship graph: one model, borrowed equations, shared people, structure, the hold-out."""

from __future__ import annotations

import dataclasses

from formularium import stemma
from formularium.catalogue import FORMULATIONS
from formularium.records import Added, Formulation

# Cooptera's models as its list gives them (cooptera@6d8d2d4), enough for these tests.
ENGINE = (
    "kennelly2007.trigger",
    "goidanich.incubation",
    "rule_3_10",
    "rossi2008.primary",
    "rossi2008pp.dormancy",
    "caffi2013.sporulation",
    "lalancette1988.sporulation_bounds",
    "brischetto2021.secondary",
    "magarey2005.generic",
    "magarey2010.rules",
    "madden1999.detection_bound",
    "sentelhas2008.wetness",
    "cooptera.rh90_wetness",
    "vitimeteo.oospores",
    "cannon2001.sensitivity",
    "noaa.solar_position",
    "alduchov1996.magnus",
    "hughes2017.scoring",
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
        structures=("dispersal-kernel",),
    )
    return dataclasses.replace(base, **over)


def test_a_formulation_and_the_pieces_of_one_model_are_the_same() -> None:
    assert stemma.link("rossi2008.primary", "rossi2008.primary") == stemma.SAME
    # The truth's oospores are a piece of Rossi 2008's model and of its dormancy rule.
    assert stemma.link("rossi2008.oospores", "rossi2008.primary") == stemma.SAME
    assert stemma.link("rossi2008.oospores", "rossi2008pp.dormancy") == stemma.SAME
    assert stemma.link("rossi2008.oospores", "rossi2008.incubation") == stemma.SAME


def test_a_shared_author_is_kinship() -> None:
    # Fedele 2025 is Rossi's and Caffi's too.
    assert "rossi2008.primary" in stemma.kin("fedele2025.dose", ENGINE)
    assert "caffi2013.sporulation" in stemma.kin("fedele2025.dose", ENGINE)
    # Kennelly 2007 and Magarey's fact sheet: Magarey, P. A. in both.
    assert "magarey2010.rules" in stemma.kin("kennelly2007.trigger", ENGINE)


def test_added_authors_count() -> None:
    cat = _with(rival=_candidate(authors=("Steinmetz, V.",), year=2005))
    # Steinmetz is one of VitiMeteo's project members added from a search summary.
    assert stemma.kin("rival", ENGINE, cat) == ["vitimeteo.oospores"]
    cat["rival"] = _candidate(
        authors=("Nobody, Z.",),
        added_authors=(Added(("Caffi, Tito",), "memory", "a test"),),
    )
    assert "caffi2013.sporulation" in stemma.kin("rival", ENGINE, cat)


def test_sentelhas_makes_florence_and_gillespie_kin() -> None:
    cat = _with(
        plasmo=_candidate(authors=("Orlandini, Simone", "Rosa, M.")),
        pedro1982=_candidate(authors=("Pedro, M. J.", "Gillespie, Terry J."), year=1982),
    )
    assert "sentelhas2008.wetness" in stemma.kin("plasmo", ENGINE, cat)
    assert "sentelhas2008.wetness" in stemma.kin("pedro1982", ENGINE, cat)


def test_a_borrowed_equation_is_kinship_without_a_shared_author() -> None:
    cat = _with(**{"uses-magarey": _candidate(borrows=("magarey2005.generic",))})
    found = {f.other: f.reason for f in stemma.links("uses-magarey", ENGINE, cat)}
    assert found["magarey2005.generic"] == "a borrowed equation"
    assert found["brischetto2021.secondary"] == "a borrowed equation"  # both compute it


def test_a_piece_counts_its_models_borrowings() -> None:
    # Rossi 2008's model borrows Goidanich's incubation; its incubation piece does too.
    found = {f.other: f.reason for f in stemma.links("rossi2008.incubation", ENGINE)}
    assert found["goidanich.incubation"] == "a borrowed equation"


def test_the_ohio_lineage_is_kin_through_the_bound_the_engine_computes() -> None:
    cat = _with(
        ohio=_candidate(authors=("Lalancette, N.", "Ellis, M. A.", "Madden, L. V."), year=1988)
    )
    found = {f.other: f.reason for f in stemma.links("ohio", ENGINE, cat)}
    assert "Lalancette" in found["lalancette1988.sporulation_bounds"]
    assert "brischetto2021.secondary" not in found  # borrowing it is the engine model's own
    # Madden & Hughes's sampling bound is an observation piece: Madden alone links nothing.
    assert "madden1999.detection_bound" not in found


# -- Roles (D26) -----------------------------------------------------------------------------


def test_lineage_counts_only_between_process_models() -> None:
    cat = _with(
        statistician=_candidate(authors=("Hughes, Gareth",), year=2015),
        modeller=_candidate(authors=("Hughes, Gareth",), year=2015, role="observation"),
    )
    assert (
        stemma.kin("statistician", ["hughes2017.scoring", "madden1999.detection_bound"], cat) == []
    )
    assert stemma.link("modeller", "hughes2017.scoring", cat) is None
    assert stemma.link("hughes2017.scoring", "hughes2017.scoring", cat) == stemma.SAME


def test_borrowing_a_reference_piece_makes_nobody_kin() -> None:
    # Magarey's fact sheet borrows the sun's position; Sentelhas 2008 borrows Magnus.
    cat = _with(
        dew=_candidate(authors=("Nobody, Z.",), borrows=("alduchov1996.magnus",)),
        sunny=_candidate(authors=("Nobody, Z.",), borrows=("noaa.solar_position",)),
    )
    assert "sentelhas2008.wetness" not in stemma.kin("dew", ENGINE, cat)
    assert "magarey2010.rules" not in stemma.kin("sunny", ENGINE, cat)


def test_the_hold_out_by_role() -> None:
    # A truth whose own scouts compute the engine's detection sensitivity, and whose
    # microclimate uses the sun and Magnus: the matched observation piece goes; the
    # reference pieces stay, though the truth uses them.
    truth = ["cannon2001.sensitivity", "noaa.solar_position", "alduchov1996.magnus"]
    held = stemma.hold_out(truth, ENGINE)
    assert set(held) == {"cannon2001.sensitivity"}
    # An observation of the same structure, the truth's own, holds it out too.
    cat = _with(scout=_candidate(role="observation", structures=("detection-sensitivity",)))
    assert set(stemma.hold_out(["scout"], ENGINE, cat)) == {"cannon2001.sensitivity"}
    # Madden's sampling bound stays for an Ohio truth; Lalancette's bound goes.
    cat = _with(
        ohio=_candidate(authors=("Lalancette, N.", "Ellis, M. A.", "Madden, L. V."), year=1988)
    )
    held = stemma.hold_out(["ohio"], ENGINE, cat)
    assert "lalancette1988.sporulation_bounds" in held
    assert "madden1999.detection_bound" not in held


def test_an_unrelated_group_is_not_kin() -> None:
    cat = _with(elsewhere=_candidate(authors=("Somebody, A.", "Else, B.")))
    assert stemma.kin("elsewhere", ENGINE, cat) == []
    assert stemma.kin("kernel.mixture", ENGINE) == []  # made up, no authors


def test_the_hold_out_takes_kin_and_shared_structure() -> None:
    held = stemma.hold_out(["rossi2008.primary", "fedele2025.dose"], ENGINE)
    assert "rossi2008.primary" in held  # the truth's own model
    assert "caffi2013.sporulation" in held  # Rossi's group
    assert "brischetto2021.secondary" in held  # Rossi again
    assert "cooptera.rh90_wetness" not in held  # Cooptera's own, unrelated
    cat = _with(trigger=_candidate(structures=("rain-temperature-trigger",)))
    held = stemma.hold_out(["trigger"], ENGINE, cat)
    assert {"kennelly2007.trigger", "rule_3_10", "magarey2010.rules"} <= set(held)
    assert all("the same structure" in r for r in held["rule_3_10"])


def test_an_unrelated_truth_holds_out_nothing() -> None:
    cat = _with(elsewhere=_candidate(authors=("Somebody, A.", "Else, B.")))
    assert stemma.hold_out(["elsewhere", "kernel.mixture"], ENGINE, cat) == {}
