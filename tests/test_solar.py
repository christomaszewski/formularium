"""NOAA's solar position: the solstices, the azimuth, NOAA's document, and Cooptera's copy."""

from __future__ import annotations

from datetime import UTC, datetime

import numpy as np

from formularium.equations import solar

LAT, LON = 41.42, 1.80  # the Penedès


def _day(month: int, day: int, year: int = 2027) -> np.ndarray:
    t0 = datetime(year, month, day, tzinfo=UTC).timestamp()
    return t0 + np.arange(0, 86400, 60)


def _year(year: int) -> np.ndarray:
    t0 = datetime(year, 1, 1, tzinfo=UTC).timestamp()
    t1 = datetime(year + 1, 1, 1, tzinfo=UTC).timestamp()
    return np.arange(t0, t1, 600.0)


def test_noon_sun_at_the_solstices() -> None:
    # 90 - latitude + declination: 72.0 degrees in June, 25.1 in December.
    assert abs(solar.elevation_deg(_day(6, 21), LAT, LON).max() - 72.0) < 0.5
    assert abs(solar.elevation_deg(_day(12, 21), LAT, LON).max() - 25.1) < 0.5
    midnight = datetime(2027, 6, 21, 0, tzinfo=UTC).timestamp()
    assert solar.elevation_deg(np.array([midnight]), LAT, LON)[0] < 0


def test_the_sun_rises_east_crosses_south_and_sets_west() -> None:
    elev, az = solar.position_deg(_day(3, 20), LAT, LON)
    up = np.flatnonzero(elev > 0)
    assert abs(az[up[0]] - 90.0) < 2.0
    assert abs(az[np.argmax(elev)] - 180.0) < 1.0
    assert abs(az[up[-1]] - 270.0) < 2.0
    # Morning and afternoon mirror each other about the meridian.
    noon = np.argmax(elev)
    assert abs((az[noon - 120] - 180.0) + (az[noon + 120] - 180.0)) < 2.0


def test_the_azimuth_matches_the_suns_direction_as_a_vector() -> None:
    t = _day(6, 21)[::15]
    elev, az = solar.position_deg(t, LAT, LON)
    decl, ha = solar.declination_and_hour_angle(t, LON)
    lat = np.radians(LAT)
    # The sun's unit vector in east, north, up, from the hour angle and declination.
    east = -np.cos(decl) * np.sin(ha)
    north = np.cos(lat) * np.sin(decl) - np.sin(lat) * np.cos(decl) * np.cos(ha)
    up = np.sin(lat) * np.sin(decl) + np.cos(lat) * np.cos(decl) * np.cos(ha)
    lit = up > 0.05
    vector_az = np.degrees(np.arctan2(east, north)) % 360.0
    gap = (az[lit] - vector_az[lit] + 180.0) % 360.0 - 180.0
    assert np.abs(gap).max() < 0.01
    assert np.allclose(elev[lit], np.degrees(np.arcsin(up[lit])), atol=1e-6)


def _noaa_as_printed(t: np.ndarray) -> np.ndarray:
    """NOAA's document, transcribed again from the PDF read 2026-10-07: 366 in leap years."""
    days = t / 86400.0
    whole = np.floor(days)
    hours = (days - whole) * 24.0
    date = whole.astype("datetime64[D]")
    year_start = date.astype("datetime64[Y]")
    doy = (date - year_start.astype("datetime64[D]")).astype(np.int64) + 1
    year = year_start.astype(np.int64) + 1970
    leap = (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0))
    gamma = 2 * np.pi / np.where(leap, 366.0, 365.0) * (doy - 1 + (hours - 12) / 24)
    eqtime = 229.18 * (
        0.000075
        + 0.001868 * np.cos(gamma)
        - 0.032077 * np.sin(gamma)
        - 0.014615 * np.cos(2 * gamma)
        - 0.040849 * np.sin(2 * gamma)
    )
    decl = (
        0.006918
        - 0.399912 * np.cos(gamma)
        + 0.070257 * np.sin(gamma)
        - 0.006758 * np.cos(2 * gamma)
        + 0.000907 * np.sin(2 * gamma)
        - 0.002697 * np.cos(3 * gamma)
        + 0.00148 * np.sin(3 * gamma)
    )
    ha = np.radians((hours * 60 + eqtime + 4 * LON) / 4 - 180)
    lat = np.radians(LAT)
    cos_zenith = np.sin(lat) * np.sin(decl) + np.cos(lat) * np.cos(decl) * np.cos(ha)
    return 90 - np.degrees(np.arccos(np.clip(cos_zenith, -1, 1)))


def test_noaas_document_except_for_leap_years() -> None:
    common = _year(2027)
    assert np.abs(solar.elevation_deg(common, LAT, LON) - _noaa_as_printed(common)).max() < 1e-9
    # Dividing by 365 in a leap year, as both tools always have, costs up to 0.30 degrees of
    # elevation at the Penedès in 2028 (0.298 measured 2026-10-07).
    leap = _year(2028)
    assert np.abs(solar.elevation_deg(leap, LAT, LON) - _noaa_as_printed(leap)).max() < 0.31


def test_cooptera_s_copy_agrees() -> None:
    # `solar_elevation` in Cooptera's models/sun.py at cooptera@e8e3963, run from its source on
    # 2026-10-07 at 41.42 N, 1.80 E: scalar math, a second copy of the same formulas.
    cooptera = {
        1813578720: 72.02650526166029,  # 2027-06-21 11:52 UTC
        1829389800: 25.160016995598426,  # 2027-12-21 11:50 UTC
        1837148400: 10.957920812426067,  # 2028-03-20 07:00 UTC
        1791387000: 19.99192566304076,  # 2026-10-07 15:30 UTC
    }
    t = np.array(list(cooptera), dtype=np.float64)
    assert np.allclose(solar.elevation_deg(t, LAT, LON), list(cooptera.values()), atol=1e-9)
