"""Magarey's generic infection model, against the paper's numbers and Cooptera's copy."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations.magarey2005 import required_wet_hours, temperature_response

BRISCHETTO = FORMULATIONS["brischetto2021.secondary"]
CARDINAL = tuple(BRISCHETTO.published(n) for n in ("t_min_c", "t_opt_c", "t_max_c"))
W_MIN = BRISCHETTO.published("w_min_h")


def test_brischetto_2021s_numbers() -> None:
    # Figure 2's caption: "shortest wetness duration at optimal temperature = 2 h; minimal,
    # optimal, and maximal temperature for infection = 4.0, 21.0, and 30.2 °C".
    assert CARDINAL == (4.0, 21.0, 30.2) and W_MIN == 2.0
    assert required_wet_hours(np.array([21.0]), CARDINAL, W_MIN)[0] == pytest.approx(2.0)
    assert np.isinf(required_wet_hours(np.array([4.0, 30.2, -3.0, 35.0]), CARDINAL, W_MIN)).all()


def test_the_response_peaks_at_the_optimum_and_vanishes_at_the_limits() -> None:
    f = temperature_response(np.array([4.0, 10.0, 21.0, 27.0, 30.2]), CARDINAL)
    assert f[2] == pytest.approx(1.0)
    assert f[0] == 0.0 and f[4] == 0.0
    assert 0 < f[1] < 1 and 0 < f[3] < 1
    hours = required_wet_hours(np.array([10.0, 15.0, 21.0, 27.0]), CARDINAL, W_MIN)
    assert hours[0] > hours[1] > hours[2] < hours[3]


def test_cooptera_s_copy_agrees() -> None:
    # `minimum_wet_hours` in Cooptera's standalone/brischetto.py at cooptera@e8e3963, run from
    # its source on 2026-10-07: a second transcription of the same equation.
    cooptera = {
        5.0: 137.11118926842215,
        10.0: 6.240708380643788,
        15.0: 2.7059345026254125,
        21.0: 2.0,
        27.0: 3.289176975877565,
        30.0: 41.958386408980274,
    }
    t = np.array(list(cooptera))
    ours = required_wet_hours(t, CARDINAL, W_MIN)
    assert np.allclose(ours, list(cooptera.values()), rtol=1e-12, atol=0)


def test_magarey_2005s_own_numbers() -> None:
    # Table 2, read 2026-10-07: P. viticola on grape, fitted to Lalancette, Ellis & Madden 1988.
    paper = FORMULATIONS["magarey2005.generic"]
    cardinal = tuple(paper.published(f"p_viticola.{n}") for n in ("t_min_c", "t_opt_c", "t_max_c"))
    assert cardinal == (1.0, 20.0, 30.0)
    w_min, w_max = paper.published("p_viticola.w_min_h"), paper.published("p_viticola.w_max_h")
    assert (w_min, w_max) == (2.0, 14.0)
    # Eq. 1: Wmin at the optimum; the cap is the caller's.
    hours = required_wet_hours(np.array([20.0, 5.0, 29.5]), cardinal, w_min)
    assert hours[0] == pytest.approx(2.0)
    assert hours[1] > w_max and hours[2] > w_max  # near the limits only the cap binds
    capped = np.minimum(hours, w_max)
    assert capped[1] == capped[2] == 14.0
    # p. 93: an unknown Wmax is 3.8 + 3.0 Wmin; Table 2's grape Wmax was observed instead.
    rule = paper.published("w_max.intercept_h") + paper.published("w_max.slope") * w_min
    assert rule == pytest.approx(9.8)
