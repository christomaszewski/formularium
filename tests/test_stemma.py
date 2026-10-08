"""The kinship graph: one model, borrowed equations, shared people, structure, the hold-out."""

from __future__ import annotations

import dataclasses

from formularium import stemma
from formularium.catalogue import FORMULATIONS
from formularium.records import Added, Formulation

# Cooptera's models as its list gives them (cooptera@7b102e0), enough for these tests.
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


def test_a_shared_author_alone_is_a_flag_not_a_dependency() -> None:
    """D27: Rossi and Caffi wrote Fedele 2025 and Caffi 2013, which share nothing else."""
    assert "caffi2013.sporulation" not in stemma.kin("fedele2025.dose", ENGINE)
    flagged = {f.other for f in stemma.flags("fedele2025.dose", ENGINE)}
    assert "caffi2013.sporulation" in flagged
    # Kennelly 2007 and Magarey's fact sheet: Magarey, P. A. in both, and nothing else.
    assert stemma.link("kennelly2007.trigger", "magarey2010.rules") is None
    assert "Magarey" in stemma.possible_dependence("kennelly2007.trigger", "magarey2010.rules")


def test_a_model_used_in_calibration_is_a_dependency() -> None:
    """Fedele 2025 fitted its dose curve to counts whose window Rossi 2008's model set."""
    found = {f.other: f.reason for f in stemma.links("fedele2025.dose", ENGINE)}
    assert found == {"rossi2008.primary": "calibrated with rossi2008.primary"}
    held = stemma.hold_out(["fedele2025.dose"], ENGINE)
    assert "rossi2008.primary" in held
    # Two formulations fitted with the same model's help depend on each other too.
    cat = _with(other=_candidate(calibrated_with=("rossi2008.primary",)))
    assert stemma.link("other", "fedele2025.dose", cat) == (
        "calibrated with a shared model, rossi2008.primary"
    )


def test_rossi_s_incubation_and_goidanich_share_calibration_data_inferred() -> None:
    """Rossi 2008's eqs 8-9 regress incubation on temperature at two humidity levels, after
    Goidanich et al. 1957 (inferred, trail). The dependency holds without the borrow."""
    # Since cooptera@7b102e0 Rossi 2008 no longer borrows the table: the data link alone holds.
    assert "goidanich.incubation" not in FORMULATIONS["rossi2008.primary"].borrows
    assert stemma.link("rossi2008.incubation", "goidanich.incubation") == (
        "shared calibration data, goidanich1957"
    )
    assert "inferred" in FORMULATIONS["rossi2008.primary"].calibration_note.lower()


def test_added_authors_count_toward_flags() -> None:
    cat = _with(rival=_candidate(authors=("Steinmetz, V.",), year=2005))
    # Steinmetz is one of VitiMeteo's project members, added from a search summary.
    assert [f.other for f in stemma.flags("rival", ENGINE, cat)] == ["vitimeteo.oospores"]
    cat["rival"] = _candidate(
        authors=("Nobody, Z.",),
        added_authors=(Added(("Caffi, Tito",), "memory", "a test"),),
    )
    assert "caffi2013.sporulation" in {f.other for f in stemma.flags("rival", ENGINE, cat)}


def test_sentelhas_flags_florence_and_gillespie() -> None:
    cat = _with(
        plasmo=_candidate(authors=("Orlandini, Simone", "Rosa, M.")),
        pedro1982=_candidate(authors=("Pedro, M. J.", "Gillespie, Terry J."), year=1982),
    )
    for name in ("plasmo", "pedro1982"):
        assert "sentelhas2008.wetness" not in stemma.kin(name, ENGINE, cat)
        assert "sentelhas2008.wetness" in {f.other for f in stemma.flags(name, ENGINE, cat)}


def test_a_borrowed_equation_is_kinship_without_a_shared_author() -> None:
    cat = _with(**{"uses-magarey": _candidate(borrows=("magarey2005.generic",))})
    found = {f.other: f.reason for f in stemma.links("uses-magarey", ENGINE, cat)}
    assert found["magarey2005.generic"] == "a borrowed equation"
    assert found["brischetto2021.secondary"] == "a borrowed equation"  # both compute it


def test_a_piece_counts_its_models_borrowings() -> None:
    # Rossi 2008's model computes Blaeser & Weltzien's survival equation (cooptera@7b102e0,
    # primary_infection.py); so does its incubation piece, as a piece of that model.
    assert stemma.link("rossi2008.incubation", "blaeser1979.survival") == "a borrowed equation"


def test_the_ohio_lineage_depends_only_where_it_computes_the_engines_bound() -> None:
    ohio = ("Lalancette, N.", "Ellis, M. A.", "Madden, L. V.")
    cat = _with(
        infection=_candidate(authors=ohio, year=1988),
        sporulation=_candidate(
            authors=ohio, year=1988, borrows=("lalancette1988.sporulation_bounds",)
        ),
    )
    # Ohio's infection model shares only authors with the engine: flagged, not held out.
    assert stemma.kin("infection", ENGINE, cat) == []
    flagged = {f.other for f in stemma.flags("infection", ENGINE, cat)}
    assert {"lalancette1988.sporulation_bounds", "madden1999.detection_bound"} <= flagged
    # Its sporulation model computes the bound the engine's Brischetto port computes.
    found = {f.other: f.reason for f in stemma.links("sporulation", ENGINE, cat)}
    assert found["lalancette1988.sporulation_bounds"] == "a borrowed equation"
    assert found["brischetto2021.secondary"] == "a borrowed equation"  # both compute it


def test_shared_calibration_data_is_a_dependency() -> None:
    # Brischetto 2021's Magarey parameters were fitted to Blaeser & Weltzien and Caffi 2016.
    cat = _with(fitted=_candidate(calibrated_on=("caffi2016",)))
    found = {f.other: f.reason for f in stemma.links("fitted", ENGINE, cat)}
    assert found["brischetto2021.secondary"] == "shared calibration data, caffi2016"
    assert found["magarey2005.generic"] == "shared calibration data, caffi2016"


def test_a_shared_implementation_is_a_dependency() -> None:
    cat = _with(
        a=_candidate(authors=("One, A.",), equations="magarey2005"),
        b=_candidate(authors=("Two, B.",), equations="magarey2005"),
    )
    assert (
        stemma.link("a", "b", cat) == "a shared implementation, formularium.equations.magarey2005"
    )


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
    # Madden's sampling bound stays for an Ohio truth; the bound its sporulation computes goes.
    cat = _with(
        ohio=_candidate(
            authors=("Lalancette, N.", "Madden, L. V.", "Ellis, M. A."),
            year=1988,
            borrows=("lalancette1988.sporulation_bounds",),
        )
    )
    held = stemma.hold_out(["ohio"], ENGINE, cat)
    assert "lalancette1988.sporulation_bounds" in held
    assert "madden1999.detection_bound" not in held
    assert "madden1999.detection_bound" not in stemma.hold_out(
        ["ohio"], ENGINE, cat, by_authors=True
    )


def test_an_unrelated_group_is_not_kin() -> None:
    cat = _with(elsewhere=_candidate(authors=("Somebody, A.", "Else, B.")))
    assert stemma.kin("elsewhere", ENGINE, cat) == []
    assert stemma.flags("elsewhere", ENGINE, cat) == []
    assert stemma.kin("kernel.mixture", ENGINE) == []  # made up, no authors


def test_the_hold_out_takes_dependencies_and_shared_structure() -> None:
    held = stemma.hold_out(["rossi2008.primary", "fedele2025.dose"], ENGINE)
    assert "rossi2008.primary" in held  # the truth's own model
    assert "goidanich.incubation" in held  # Rossi 2008 borrows it
    assert "cooptera.rh90_wetness" not in held  # Cooptera's own, unrelated
    cat = _with(trigger=_candidate(structures=("rain-temperature-trigger",)))
    held = stemma.hold_out(["trigger"], ENGINE, cat)
    assert {"kennelly2007.trigger", "rule_3_10", "magarey2010.rules"} <= set(held)
    assert all("the same structure" in r for r in held["rule_3_10"])


def test_authorship_alone_is_held_out_only_in_the_sensitivity_arm() -> None:
    """D27's example: Rossi 2008 against Caffi 2013, distinct structures, Rossi in both."""
    truth = ["rossi2008.primary"]
    assert "caffi2013.sporulation" not in stemma.hold_out(truth, ENGINE)
    sensitivity = stemma.hold_out(truth, ENGINE, by_authors=True)
    assert any("possible dependence" in r for r in sensitivity["caffi2013.sporulation"])
    # Reference pieces stay even there, and the main arm's reasons are kept.
    assert "hughes2017.scoring" not in sensitivity
    assert "goidanich.incubation" in sensitivity


def test_an_unrelated_truth_holds_out_nothing() -> None:
    cat = _with(elsewhere=_candidate(authors=("Somebody, A.", "Else, B.")))
    assert stemma.hold_out(["elsewhere", "kernel.mixture"], ENGINE, cat) == {}


def test_shared_calibration_data_links_an_observation_piece() -> None:
    """D29: a truth matched to Madden, Hughes & Ellis 1995's Ohio data holds out the engine's
    sampling bound, which was fitted to the same data. Authors alone still do not."""
    cat = _with(spread=_candidate(calibrated_on=("madden1995",)))
    assert stemma.link("spread", "madden1999.detection_bound", cat) == (
        "shared calibration data, madden1995"
    )
    assert "madden1999.detection_bound" in stemma.hold_out(["spread"], ENGINE, cat)
    cat = _with(madden=_candidate(authors=("Madden, L. V.",), year=1995))
    assert stemma.link("madden", "madden1999.detection_bound", cat) is None
    assert "madden1999.detection_bound" not in stemma.hold_out(["madden"], ENGINE, cat)
