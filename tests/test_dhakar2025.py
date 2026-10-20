"""Dhakar et al. 2025's sensor-plate model, Eqs 1-11 as printed, each at a point."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import dhakar2025 as dh

DHA = FORMULATIONS["dhakar2025.leaf_wetness"]


def test_the_sensor_scale_and_the_wet_state() -> None:
    # Eq 1: 435 counts dry, 1100 wet; 701 counts is the 0.4 threshold (p. 3).
    scale = dh.sensor_wetness(
        np.array([435, 701, 1100]),
        DHA.published("sensor.dry_counts"),
        DHA.published("sensor.span_counts"),
    )
    assert scale == pytest.approx([0.0, DHA.published("sensor.wet_threshold"), 1.0])
    # Eq 2 and 2.3.1.5: wet above 0 mm; frozen hours excluded.
    lw = dh.leaf_wetness(
        np.array([0.1, 0.0, 0.2]), np.array([0.0, 0.0, 0.0]), 0.05, [5.0, 5.0, -1.0]
    )
    assert np.isnan(lw[2]) and dh.wet(lw).tolist() == [1.0, 0.0, 0.0]
    assert dh.interception(np.array([0.3, 2.0]), DHA.published("rain_cap")).tolist() == [0.3, 0.6]
    # Eq 11 (M2): no dew above the gate; the two printed gates differ.
    gated = dh.gated_dewfall(
        np.array([0.1, 0.1]), np.array([2.0, 2.0]), DHA.published("dpdc.table2")
    )
    assert gated.tolist() == [0.0, 0.0]
    assert dh.gated_dewfall(0.1, 2.0, DHA.published("dpdc.text")) == 0.1


def test_resistances_and_the_printed_bounds() -> None:
    d = DHA.published("plate_length")
    r_b = dh.boundary_resistance(
        1.0, d, DHA.published("nu"), DHA.published("kappa"),
        DHA.published("nusselt_a"), DHA.published("nusselt_b"),
    )  # fmt: skip
    assert r_b == pytest.approx(35.4, abs=0.2)  # s/m at 1 m/s (own calculation)
    r_s = dh.stomatal_resistance(
        DHA.published("stomata_n"),
        DHA.published("pore_diameter") * 1e-6,
        DHA.published("pore_length") * 1e-6,
        DHA.published("d_wv"),
    )
    assert r_s == pytest.approx(30.6, abs=0.2)
    # Table 2: Cd 4.23 below its own lower bound of 5.
    assert DHA.published("c_d") < 5.0
    assert dh.shape_scale(DHA.published("w_max"), DHA.published("c_f"), DHA.published("c_d")) == (
        pytest.approx(0.718 * 1.78 + 0.282 * 4.23)
    )


def test_eqs_3_and_6_as_printed() -> None:
    # Dew grows with the dew-point depression, and Eq 6 returns J m-2, not mm: at DPD 2 K,
    # 1 m/s, 10 °C, about 1.2e5 J m-2 in 15 min; divided by a latent heat of 2.45e6 J/kg
    # (not printed) that would be 0.05 mm (own calculation).
    d = DHA.published("plate_length")
    area = d * DHA.published("plate_width")
    r_b = dh.boundary_resistance(1.0, d, 15.1e-6, 2.15e-5, 0.72, 0.6)
    r_s = dh.stomatal_resistance(25e7, 6.23e-6, 2.5e-6, 2.12e-5)
    slope = 82.3  # Pa/K at 10 °C (FAO-56 Eq 13, the test's choice)

    def e_dew(dpd: float, gamma: float) -> float:
        return dh.dew_energy(
            283.15, dpd, r_b, r_s, slope, emissivity=1.0, sigma=DHA.published("sigma"),
            rho_a=DHA.published("rho_a"), cp=DHA.published("cp"), gamma=gamma, area=area,
        )  # fmt: skip

    assert e_dew(4.0, 66.0) == pytest.approx(2 * e_dew(2.0, 66.0))
    df = dh.dewfall(e_dew(2.0, 66.0), area, 60.0, 15.0)
    assert df == pytest.approx(1.18e5, rel=0.02)
    assert df / 2.45e6 == pytest.approx(0.048, abs=0.002)
    # With gamma as printed (0.246 Pa/K) the third term is about 270 times larger.
    assert e_dew(2.0, DHA.published("gamma_as_printed")) > 20 * e_dew(2.0, 66.0)


def test_eq_9_as_printed_cannot_be_evaluated_and_ep_is_finite() -> None:
    # ln(Zc - Zd/Z0) with SWEB's Zd = 2/3 Zc and Z0 = Zc/10 (not printed here) is ln(-6.52).
    z_c, z_ref = DHA.published("z_c"), DHA.published("z_ref")
    assert np.isnan(dh.canopy_wind(1.0, z_c, z_ref, 2 / 3 * z_c, z_c / 10, DHA.published("alpha")))
    factor = (1 + DHA.published("alpha") * (1 - z_c) / z_ref) ** -2
    assert factor == pytest.approx(0.0205, abs=1e-4)
    ep = dh.potential_evaporation(0.0823, 0.066, 2.45, 1.293, 1005, 3.0, 2700.0, 1.23, 1.0)
    assert np.isfinite(ep) and ep > 0
    assert dh.evaporation(1.0, DHA.published("w_f"), DHA.published("w_max")) == pytest.approx(
        0.368 * 0.718
    )
