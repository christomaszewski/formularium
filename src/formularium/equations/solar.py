"""Where the sun is: its elevation and azimuth at a place, at each UTC instant.

NOAA's general solar position formulas, the "low accuracy" set: a Fourier series for the
equation of time and the declination (usually credited to Spencer 1971; memory), then the
hour angle and the zenith. Good to a fraction of a degree, which is ample for telling night
from day, scaling sunshine, and asking whether the sun has cleared a horizon.

**How it was checked.**
- NOAA's document (General Solar Position Calculations, gml.noaa.gov/grad/solcalc/
  solareqns.PDF) was read on 2026-10-07. Its coefficients are the ones below.
- **Leap years** divide by 366, as the document says (fixed 2026-10-07; Chris's decision).
  Agrarium's and Cooptera's copies before it always divided by 365, which put the sun up
  to 0.30 degrees of elevation wrong at 41.42° N in 2028. Common years are unchanged, bit
  for bit.
- **One departure from it:** the document's azimuth,
  cos(180 - θ) = -(sin lat cos φ - sin decl) / (cos lat sin φ), puts the noon sun in the
  north if taken literally. The azimuth here is pvlib's analytical form
  (`solar_azimuth_analytical`, source read): its cosine from the zenith, latitude and
  declination, signed by the hour angle.
- The tests check the solstices' noon elevations, sunrise, noon and sunset azimuths at an
  equinox, the azimuth against the sun's direction worked out as a vector, the document
  transcribed again, and Cooptera's scalar copy (`models/sun.py`) in a common year.

The arithmetic is otherwise Agrarium's `world/sun.py`, moved unchanged.
Vectorised over an array of UTC times given as seconds since the Unix epoch.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "noaa.solar-position"

_DAY = 86400.0


def elevation_deg(epoch_seconds: np.ndarray, latitude: float, longitude: float) -> np.ndarray:
    """Solar elevation in degrees (negative below the horizon) at each UTC instant."""
    return position_deg(epoch_seconds, latitude, longitude)[0]


def declination_and_hour_angle(
    epoch_seconds: np.ndarray, longitude: float
) -> tuple[np.ndarray, np.ndarray]:
    """The sun's declination and hour angle, in radians, at each UTC instant."""
    t = np.asarray(epoch_seconds, dtype=np.float64)
    days = t / _DAY
    # Day of year (1-based), the year's length, and the hour, in UTC; 1970-01-01 is day 1.
    whole = np.floor(days)
    hours = (days - whole) * 24.0
    dt = whole.astype("datetime64[D]")
    year = dt.astype("datetime64[Y]")
    year_start = year.astype("datetime64[D]")
    year_days = ((year + np.timedelta64(1, "Y")).astype("datetime64[D]") - year_start).astype(
        np.float64
    )
    doy = (dt - year_start).astype(np.int64) + 1
    g = 2.0 * np.pi / year_days * (doy - 1 + (hours - 12.0) / 24.0)
    equation_of_time = 229.18 * (
        0.000075
        + 0.001868 * np.cos(g)
        - 0.032077 * np.sin(g)
        - 0.014615 * np.cos(2 * g)
        - 0.040849 * np.sin(2 * g)
    )
    declination = (
        0.006918
        - 0.399912 * np.cos(g)
        + 0.070257 * np.sin(g)
        - 0.006758 * np.cos(2 * g)
        + 0.000907 * np.sin(2 * g)
        - 0.002697 * np.cos(3 * g)
        + 0.00148 * np.sin(3 * g)
    )
    solar_minutes = hours * 60.0 + equation_of_time + 4.0 * longitude
    return declination, np.radians(solar_minutes / 4.0 - 180.0)


def position_deg(
    epoch_seconds: np.ndarray, latitude: float, longitude: float
) -> tuple[np.ndarray, np.ndarray]:
    """Solar elevation and azimuth (clockwise from north) in degrees at each UTC instant."""
    declination, hour_angle = declination_and_hour_angle(epoch_seconds, longitude)
    lat = np.radians(latitude)
    cos_zenith = np.sin(lat) * np.sin(declination) + np.cos(lat) * np.cos(declination) * np.cos(
        hour_angle
    )
    zenith = np.arccos(np.clip(cos_zenith, -1.0, 1.0))
    denom = np.sin(zenith) * np.cos(lat)
    with np.errstate(invalid="ignore", divide="ignore"):
        cos_az = (np.cos(zenith) * np.sin(lat) - np.sin(declination)) / denom
    cos_az = np.where(np.abs(denom) < 1e-12, 1.0, np.clip(cos_az, -1.0, 1.0))
    # The hour angle wrapped to (-pi, pi]: negative before solar noon, so the sun is east.
    ha = np.angle(np.exp(1j * hour_angle))
    azimuth = np.degrees(np.sign(ha) * np.arccos(cos_az) + np.pi) % 360.0
    return 90.0 - np.degrees(zenith), azimuth
