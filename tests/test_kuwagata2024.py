"""Kuwagata et al. 2024's one-layer dew model: each equation at a point, and the printed rates."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import allen1998_psychrometrics as ps
from formularium.equations import kuwagata2024 as k

KUW = FORMULATIONS["kuwagata2024.canopy_dew"]
PSY = FORMULATIONS["allen1998.psychrometrics"]
ESAT = tuple(PSY.published(f"esat.{x}") for x in "abc")

# The paper prints sigma, epsilon, beta, rho_w and p_s; q_SAT, cp, rho and l it does not.
# The test's choices: FAO-56's e° with q = 0.622 e / (p - 0.378 e), cp 1005, rho 1.2, l 2.45e6.
S_STAR = k.sigma_star(KUW.published("emissivity"), KUW.published("stefan_boltzmann"))
RHO_W = KUW.published("water_density")
P_KPA = KUW.published("surface_pressure") / 10.0
CP, RHO, LAT = 1005.0, 1.2, 2.45e6
PER_DAY = 1000.0 * 86400.0  # m/s of water to mm per day


def q_sat(t_k: np.ndarray) -> np.ndarray:
    e = ps.saturation_kpa(np.asarray(t_k) - 273.15, *ESAT)
    return 0.622 * e / (P_KPA - 0.378 * e)


def dq_sat(t_k: np.ndarray) -> np.ndarray:
    return (q_sat(np.asarray(t_k) + 1e-3) - q_sat(np.asarray(t_k) - 1e-3)) / 2e-3


T, R_EFF = 293.15, -100.0  # 20 °C and -100 W m-2, the case of l. 508-511
Q, D = q_sat(T), dq_sat(T)


def exact_rate(k_l: np.ndarray, rh: float) -> np.ndarray:
    """Eqs 4-7 solved for T_L by bisection of Eq 6 (beta 1): dW/dt in mm per day."""
    lo, hi = np.full_like(k_l, T - 60.0), np.full_like(k_l, T + 10.0)
    for _ in range(80):
        mid = (lo + hi) / 2
        h = k.sensible_heat(CP, RHO, k_l, mid, T)
        le = k.latent_heat(LAT, RHO, KUW.published("beta"), k_l, q_sat(mid), rh, Q)
        res = k.effective_radiation_residual(R_EFF, T, mid, h, le, S_STAR)
        hi, lo = np.where(res < 0, mid, hi), np.where(res >= 0, mid, lo)
    t_l = (lo + hi) / 2
    e_l = RHO * k_l * (q_sat(t_l) - rh * Q)
    return k.dew_rate(e_l, RHO_W) * PER_DAY


def test_the_heat_budget_terms_at_a_point() -> None:
    r_d = k.downward_radiative_flux(0.0, 300.0, 0.3, 0.2, 1.0)
    assert r_d == 300.0
    assert k.downward_radiative_flux(100.0, 0.0, 0.3, 0.2, 1.0) == pytest.approx(50.0)
    h = k.sensible_heat(CP, RHO, 0.01, T - 2.0, T)
    le = k.latent_heat(LAT, RHO, 1.0, 0.01, q_sat(T - 2.0), 0.9, Q)
    # Eq 1 with T_S = T_L is Eq 6: the two residuals agree.
    t_l = T - 2.0
    eq1 = k.heat_budget_residual(r_d, t_l, t_l, h, le, S_STAR)
    eq6 = k.effective_radiation_residual(r_d - S_STAR * T**4, T, t_l, h, le, S_STAR)
    assert eq1 == pytest.approx(eq6)
    assert k.dew_rate(-1e-5, RHO_W) * PER_DAY == pytest.approx(0.864)


def test_the_printed_rates_from_the_exact_solution() -> None:
    # l. 508-511: at -100 W m-2 and 20 °C the maximum rate is 1.42 mm/day at rh 0.9, 0.37 at
    # 0.6 (26 %) and 0.058 at 0.4 (4 %).
    k_l = np.logspace(-5, 1, 2001)
    for rh, printed in ((0.9, 1.42), (0.6, 0.37), (0.4, 0.058)):
        assert exact_rate(k_l, rh).max() == pytest.approx(printed, rel=0.05), rh


def test_the_approximate_solution_is_consistent_and_eq_19_is_not() -> None:
    k_l = np.logspace(-5, 1, 200001)
    for rh in (0.9, 0.6):
        g_1 = k.g1(T, D, S_STAR, RHO, CP, LAT)
        k_l0 = k.critical_exchange_velocity(R_EFF, rh, T, Q, D, S_STAR, RHO, CP)
        k_lm = k.exchange_velocity_at_max(g_1, k_l0)
        g_2 = k.g2(R_EFF, rh, T, Q, D, S_STAR, RHO)
        best = k.max_rate(g_1, g_2, k_lm, k_l0, RHO_W)
        t_l = k.approximate_canopy_temperature(R_EFF, T, rh, Q, D, k_l, S_STAR, RHO, CP, LAT)
        rate = k.approximate_dew_rate(RHO, k_l, rh, Q, D, t_l, T, RHO_W)
        # Eqs 15-16 are the maximum of Eq 14 over k_L, and Eq 17 is where it crosses zero.
        assert best == pytest.approx(rate.max(), rel=1e-6)
        assert k_lm == pytest.approx(k_l[rate.argmax()], rel=1e-3)
        t_l0 = k.approximate_canopy_temperature(R_EFF, T, rh, Q, D, k_l0, S_STAR, RHO, CP, LAT)
        assert k.approximate_dew_rate(RHO, k_l0, rh, Q, D, t_l0, T, RHO_W) == pytest.approx(
            0.0, abs=1e-15
        )
        assert t_l0 == pytest.approx(k.canopy_temperature_at_kl0(T, rh, Q, D))  # Eq 22
        # Eq 19's second form is minus its first.
        assert k.g2_second_form(k_l0, rh, T, Q, S_STAR, RHO, CP) == pytest.approx(-g_2)
        # Eq 21 as printed is not Eq 12 at k_Lm.
        printed = k.canopy_temperature_at_klm(R_EFF, T, rh, Q, D, k_lm, S_STAR, RHO, CP, LAT)
        eq12 = k.approximate_canopy_temperature(R_EFF, T, rh, Q, D, k_lm, S_STAR, RHO, CP, LAT)
        assert abs(printed - eq12) > 50.0
    # At rh 0.9 the approximation is near the exact rate; it drifts where |T_L - T| > 5 K.
    assert best == pytest.approx(0.674 / PER_DAY, rel=0.01)  # the last loop's rh, 0.6


def test_limits_and_critical_humidity() -> None:
    # Eq 10 is the rh = 1 limit; Eqs 20 and 23 the k_L = 0 and infinite limits of Eq 12.
    sat = k.max_rate_saturated(R_EFF, D, CP, LAT, RHO_W)
    assert exact_rate(np.array([10.0]), 1.0)[0] == pytest.approx(sat * PER_DAY, rel=1e-3)
    still = k.approximate_canopy_temperature(R_EFF, T, 0.8, Q, D, 0.0, S_STAR, RHO, CP, LAT)
    assert still == pytest.approx(k.approximate_still_temperature(R_EFF, T, S_STAR))
    windy = k.approximate_canopy_temperature(R_EFF, T, 0.8, Q, D, 1e9, S_STAR, RHO, CP, LAT)
    assert windy == pytest.approx(k.canopy_temperature_ventilated(T, 0.8, Q, D, CP, LAT), abs=1e-4)
    # Eqs 8-9: below about 0.27 no dew at -100 W m-2 and 20 °C; the paper says rh_cr < 0.4.
    t_l00 = k.canopy_temperature_still(R_EFF, T, S_STAR)
    rh_cr = k.critical_rh(q_sat(t_l00), Q)
    assert 0.2 < rh_cr < 0.4
    # Eq 28's residual vanishes at the fully ventilated canopy temperature.
    lo, hi = T - 30.0, T
    for _ in range(80):
        mid = (lo + hi) / 2
        if k.ventilated_residual(mid, q_sat(mid), T, 0.8, Q, CP, LAT) > 0:
            hi = mid
        else:
            lo = mid
    assert mid == pytest.approx(k.canopy_temperature_ventilated(T, 0.8, Q, D, CP, LAT), abs=0.3)


def test_dew_amounts_and_the_exchange_velocity() -> None:
    assert k.reference_dew(0.01, -1e-8, 1800.0) == pytest.approx(0.01 - 1.8e-5)
    assert k.potential_dew(0.0, -1e-6, 1800.0) == 0.0
    chosen = k.potential_rate(np.array([2.0, 2.0]), np.array([-1.0, -1.0]), [0.9, 0.2], 0.3)
    assert chosen.tolist() == [2.0, -1.0]
    # Kuwagata's wind correction from 2 m to the top of a 1 m canopy.
    u = k.canopy_top_wind(
        1.0,
        KUW.published("wind.z_obs"),
        KUW.published("wind.canopy_height"),
        KUW.published("wind.displacement_share"),
        KUW.published("wind.z0"),
    )
    assert u == pytest.approx(np.log(3.3) / np.log(13.3))
    # Maruyama's g_a as printed at 1 m/s, D_L 0.1 m, lambda 0.025, nu 1.5e-5 (the test's
    # constants): about 25 "m/s", far outside the 1e-3 to 1e-1 m/s of l. 521; divided by
    # rho cp, inside it.
    g_a = k.maruyama_conductance(
        1.0,
        0.0,
        KUW.published("canopy_length_scale"),
        0.025,
        1.5e-5,
        9.81,
        293.15,
        (KUW.published("kl.nusselt_a"), KUW.published("kl.nusselt_b")),
        KUW.published("kl.sides"),
    )
    assert g_a == pytest.approx(24.9, abs=0.1)
    assert 1e-3 < g_a / (RHO * CP) < 1e-1
