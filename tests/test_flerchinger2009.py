"""Dilley & O'Brien's clear sky and Unsworth's cloud, as Flerchinger et al. 2009 print them."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import flerchinger2009 as fl

REC = FORMULATIONS["flerchinger2009.dilley_unsworth"]
SIGMA = 5.67e-8  # the Stefan-Boltzmann constant; the test's, not the paper's (none printed)
DILLEY = tuple(REC.published(f"dilley.{k}") for k in ("a", "b", "c", "t_ref", "w_ref"))


def _clear(t_k: np.ndarray, e_kpa: np.ndarray) -> np.ndarray:
    w = fl.precipitable_water(e_kpa, t_k, REC.published("prata.w_coefficient"))
    return fl.dilley_clear_sky(t_k, w, *DILLEY)


def test_the_corrected_clear_sky_at_a_point() -> None:
    # 15 °C and 1.2 kPa: w = 1.94 cm, L_clr 301.4 W m-2, eps_clr 0.771 (own calculation).
    t, e = 288.15, 1.2
    w = fl.precipitable_water(e, t, REC.published("prata.w_coefficient"))
    assert w == pytest.approx(1.937, abs=1e-3)
    l_clr = _clear(t, e)
    assert l_clr == pytest.approx(301.4, abs=0.05)
    eps = fl.clear_sky_emissivity(l_clr, t, SIGMA)
    assert eps == pytest.approx(0.771, abs=1e-3)
    # The uncorrected Table 1 (sqrt(w/25), w = 4650 e/T) would give the same w/25 term
    # by accident of the two typos only when both are kept: 4650/25 = 465/2.5.
    typo = DILLEY[0] + DILLEY[1] * (t / 273.16) ** 6 + DILLEY[2] * np.sqrt(4650 * e / t / 25)
    assert typo == pytest.approx(l_clr)


def test_unsworth_goes_to_the_cloud_base_emissivity() -> None:
    eps_clr = np.array([0.70, 0.80])
    k = REC.published("unsworth.k")
    assert fl.unsworth_emissivity(eps_clr, 0.0, k) == pytest.approx(eps_clr)
    full = fl.unsworth_emissivity(eps_clr, 1.0, k)
    assert full == pytest.approx(0.84 + 0.16 * eps_clr)
    assert (full > eps_clr).all() and (full < 1.0).all()


def test_downward_longwave_rises_with_cloud_and_humidity() -> None:
    t = np.full(3, 283.15)
    eps = fl.clear_sky_emissivity(_clear(t, np.array([0.6, 0.9, 1.2])), t, SIGMA)
    assert np.all(np.diff(eps) > 0)
    k = REC.published("unsworth.k")
    l_d = fl.downward_longwave(fl.unsworth_emissivity(eps[1], np.array([0, 0.5, 1]), k), t, SIGMA)
    assert np.all(np.diff(l_d) > 0)
    # At 10 °C and 0.9 kPa the isothermal net longwave L_d - sigma T^4 is -89.5 W m-2 clear
    # and -14.3 W m-2 overcast (own calculation): the range a canopy's night radiation spans.
    assert l_d[0] - SIGMA * 283.15**4 == pytest.approx(-89.5, abs=0.1)
    assert l_d[2] - SIGMA * 283.15**4 == pytest.approx(-14.3, abs=0.1)


def test_cloud_from_the_clearness_index() -> None:
    c = fl.cloud_from_clearness(
        np.array([0.1, 0.15, 0.475, 0.8, 0.9]), REC.published("k_cld"), REC.published("k_clr")
    )
    assert c.tolist() == pytest.approx([1.0, 1.0, 0.5, 0.0, 0.0])


def test_the_validation_is_recorded_as_printed() -> None:
    # Table 10 (14 sites) and Table 12 (7 independent sites), Dilley-Unsworth.
    assert REC.published("rmsd.hourly") == 24.5
    assert REC.published("rmsd.daily") == 14.9
    assert REC.published("rmsd.independent") == 26.9
