"""SWEB's Eqs 1-15 at a point each, and its sensitivity runs against the paper's Fig. 1."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import allen1998_psychrometrics as ps
from formularium.equations import magarey2006 as m

SWEB = FORMULATIONS["magarey2006.sweb"]
PSY = FORMULATIONS["allen1998.psychrometrics"]
ESAT = tuple(PSY.published(f"esat.{k}") for k in "abc")

# FAO-56's constants in SWEB's units (Table 2): mbar, J/g, g/cm³; SWEB prints none of them.
T_C, RH = 20.0, 75.0  # p. 378's sensitivity case
E_SAT = ps.saturation_kpa(T_C, *ESAT) * 10.0
E_AIR = E_SAT * RH / 100.0
SLOPE = ps.slope_kpa(T_C, *ESAT, PSY.published("slope.k")) * 10.0
P_KPA = 101.3
PSY_MBAR = (
    ps.psychrometric_kpa(
        P_KPA, PSY.published("cp"), PSY.published("epsilon"), PSY.published("lambda")
    )
    * 10.0
)
RHO = ps.air_density(P_KPA, T_C, PSY.published("density.r"), PSY.published("density.virtual")) / 1e3
CP = PSY.published("cp") * 1e3  # J/(g °C)
LAM = PSY.published("lambda") * 1e3  # J/g
U_Z = 1.5 * 6000.0  # 1.5 m/s in cm/min
W_PER_M2 = 60.0 / 1e4  # 1 W m-2 in J min-1 cm-2


def _wet_minutes(u_c: float, *, lai=1.0, w_max=None, c_l=None, dt=10.0) -> float:
    """Minutes of surface wetness after 2 mm of rain in the first 10 min (p. 378)."""
    w_max = SWEB.published("w_max") if w_max is None else w_max
    c_l = SWEB.published("canopy_storage_per_leaf_area") if c_l is None else c_l
    s, wet = np.array(0.0), 0
    for i in range(400):
        s, sw = m.step(
            s, np.array(0.2 if i == 0 else 0.0), np.array(0.0), np.array(lai), np.array(u_c),
            SLOPE, E_SAT, E_AIR, dt_min=dt, c_l=c_l, w_max=w_max,
            w_th=SWEB.published("w_th"), wind_exponent=SWEB.published("wind_exponent"),
            interception_k=SWEB.published("interception_k"),
            dew_share=SWEB.published("dew_radiation_share"), c_d=SWEB.published("c_d"),
            c_f=SWEB.published("c_f"), rho=RHO, cp=CP, lam=LAM, psy=PSY_MBAR,
        )  # fmt: skip
        if sw == 0:
            break
        wet += 1
    return wet * dt


def test_interception_and_storage_at_a_point() -> None:
    k = SWEB.published("interception_k")
    intercepted = m.interception(np.array([1.0, 2.0, 3.0]), 1.0, k)
    assert intercepted == pytest.approx([0.393, 0.632, 0.777], abs=1e-3)
    cap = m.storage_capacity(1.0, SWEB.published("canopy_storage_per_leaf_area"))
    assert cap == pytest.approx(0.02)  # cm, 0.2 mm per unit LAI
    # Eqs 1-3: wet while S/C > 0.1^(1/0.67) = 0.032, 0.0064 mm at LAI 1 (the record's flag).
    edge = SWEB.published("w_th") ** (1 / SWEB.published("wind_exponent"))
    assert edge == pytest.approx(0.0322, abs=1e-4)
    assert edge * cap * 10 == pytest.approx(0.0064, abs=1e-4)
    w_ind = m.wet_area_index(np.array([0.9, 1.0, 1.1]) * edge * cap, cap, 0.67)
    assert m.surface_wetness(w_ind, SWEB.published("w_th")).tolist() == [0.0, 0.0, 1.0]
    assert m.wet_fraction(1.0, SWEB.published("w_max")) == 0.5
    assert m.max_wet_area(0.5, 1.0, 0.0) == 0.5


def test_the_energy_balance_at_a_point() -> None:
    # Eq 9 with Rn = 0 is Eq 10; Eq 12 at -100 W m-2 is about 0.05 mm of dew an hour.
    h = m.transfer_coefficient(
        m.shape_scale(0.5, SWEB.published("c_f"), SWEB.published("c_d")), U_Z
    )
    assert m.shape_scale(np.array([0.0, 1.0]), 2.0, 8.7).tolist() == [8.7, 2.0]
    ep = m.potential_evaporation(RHO, CP, h, SLOPE, LAM, PSY_MBAR, E_SAT, E_AIR)
    full = m.potential_evaporation_full(0.0, RHO, CP, h, SLOPE, LAM, PSY_MBAR, E_SAT, E_AIR)
    assert ep == pytest.approx(full)
    assert m.evaporation(ep, 0.5) == pytest.approx(ep / 2)
    assert 0 < ep * 60 * 10 < 1.0  # mm per hour of potential evaporation: under 1 mm
    dp = m.potential_condensation(-100 * W_PER_M2, SLOPE, LAM, PSY_MBAR, 0.5)
    assert dp < 0  # Eq 12 keeps Rnc's sign
    assert -dp * 60 * 10 == pytest.approx(0.05, abs=0.005)


def test_eq_15_as_printed_does_not_close() -> None:
    # [1 + alpha (1 - Zc)/Z]^-2 with Zc, Z in cm: about 1000 at Zc 150, Z 200.
    alpha = SWEB.published("alpha")
    u = m.canopy_wind(U_Z, 150.0, 200.0, alpha, 2 / 3, 0.1)
    assert u / U_Z == pytest.approx(573.8, abs=0.1)
    assert m.canopy_wind(U_Z, 50.0, 200.0, alpha, 2 / 3, 0.1) < 0  # a negative log ratio
    # The sensitivity case then dries in one step, where Fig. 1A has about 150 min at LAI 1.
    assert _wet_minutes(float(u)) <= 10.0


def test_eqs_1_to_14_reproduce_fig_1a_and_1b_with_one_canopy_wind() -> None:
    # Fig. 1, read by eye (about +/- 10 min): A, LAI 1-4; B, Wmax 0.1-1.0. The canopy wind,
    # 0.3 U_Z, was found by trial (not printed); every other value is the paper's or FAO-56's.
    u_c = 0.3 * U_Z
    fig_a = {1.0: 150, 2.0: 310, 3.0: 480, 4.0: 640}
    for lai, minutes in fig_a.items():
        assert _wet_minutes(u_c, lai=lai) == pytest.approx(minutes, abs=20), lai
    fig_b = {0.1: 670, 0.2: 340, 0.4: 180, 0.8: 110, 1.0: 110}
    for w_max, minutes in fig_b.items():
        assert _wet_minutes(u_c, w_max=w_max) == pytest.approx(minutes, abs=20), w_max


def test_fig_1d_is_not_reproduced() -> None:
    # Eqs 3, 6 and 7 make the wet time proportional to Cl; Fig. 1D rises only from about 60
    # min at 0.005 cm to 190 min at 0.04 cm. Recorded as a flag on the record.
    u_c = 0.3 * U_Z
    low, high = _wet_minutes(u_c, c_l=0.005), _wet_minutes(u_c, c_l=0.04)
    assert high / low > 6
    assert abs(high - 190) > 100
