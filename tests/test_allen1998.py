"""FAO-56's net longwave (Eq 39, hourly) and psychrometrics, against its own Example 19."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import allen1998 as lw
from formularium.equations import allen1998_psychrometrics as ps

RNL = FORMULATIONS["allen1998.net_longwave"]
PSY = FORMULATIONS["allen1998.psychrometrics"]
ESAT = tuple(PSY.published(f"esat.{k}") for k in "abc")


def test_example_19s_night_hour() -> None:
    # Ch. 4, Example 19, 02:00-03:00 at N'Diaye: 28 °C, RH 90 %, Rs/Rso 0.8 assumed.
    e_sat = ps.saturation_kpa(28.0, *ESAT)
    assert e_sat == pytest.approx(3.780, abs=5e-4)
    e_a = ps.actual_kpa(e_sat, 90.0)
    assert e_a == pytest.approx(3.402, abs=5e-4)
    assert ps.slope_kpa(28.0, *ESAT, PSY.published("slope.k")) == pytest.approx(0.220, abs=5e-4)
    t4 = (28.0 + RNL.published("kelvin_offset")) ** 4
    assert RNL.published("sigma.hourly") * t4 == pytest.approx(1.681, abs=5e-4)
    humidity = (RNL.published("humidity.a"), RNL.published("humidity.b"))
    cloudiness = (RNL.published("cloudiness.a"), RNL.published("cloudiness.b"))
    assert lw.humidity_factor(e_a, *humidity) == pytest.approx(0.082, abs=5e-4)
    assert lw.cloudiness_factor(0.8, *cloudiness) == pytest.approx(0.730, abs=5e-4)
    rnl = lw.net_longwave(t4, e_a, 0.8, RNL.published("sigma.hourly"), humidity, cloudiness)
    assert rnl == pytest.approx(RNL.published("example19.rnl_night"), abs=5e-4)
    # 0.100 MJ m-2 per hour is about 28 W m-2.
    assert rnl * 1e6 / 3600 == pytest.approx(27.9, abs=0.2)


def test_the_afternoon_hours_and_the_cap() -> None:
    hour_angle = np.array([0.5, 0.95, 1.1, 1.3])
    window = lw.before_sunset(
        hour_angle, 1.7, RNL.published("night.omega_early"), RNL.published("night.omega_late")
    )
    assert window.tolist() == [False, True, True, False]
    cloudiness = (RNL.published("cloudiness.a"), RNL.published("cloudiness.b"))
    assert lw.cloudiness_factor(np.array([1.2, 1.0]), *cloudiness).tolist() == [1.0, 1.0]
    assert lw.cloudiness_factor(RNL.published("night.rs_rso_overcast"), *cloudiness) == (
        pytest.approx(0.055)
    )


def test_psychrometric_constant_and_density_at_sea_level() -> None:
    p = ps.pressure_kpa(
        0.0, *(PSY.published(f"pressure.{k}") for k in ("p0", "t0", "lapse", "power"))
    )
    assert p == pytest.approx(101.3)
    gamma = ps.psychrometric_kpa(
        p, PSY.published("cp"), PSY.published("epsilon"), PSY.published("lambda")
    )
    assert gamma == pytest.approx(PSY.published("gamma_per_kpa") * p, rel=2e-3)
    # Example 19's gamma at 8 m is 0.0673 kPa/°C.
    p8 = ps.pressure_kpa(
        8.0, *(PSY.published(f"pressure.{k}") for k in ("p0", "t0", "lapse", "power"))
    )
    assert PSY.published("gamma_per_kpa") * p8 == pytest.approx(0.0673, abs=1e-4)
    rho = ps.air_density(p, 20.0, PSY.published("density.r"), PSY.published("density.virtual"))
    assert rho == pytest.approx(3.486 * p / (1.01 * 293.0), rel=1e-3)
    assert 1.18 < rho < 1.21
