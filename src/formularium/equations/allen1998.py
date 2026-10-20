"""FAO-56's net outgoing longwave radiation, Eq 39, and its hourly form (Allen et al. 1998).

    R_nl = sigma T_K^4 (0.34 - 0.14 sqrt(e_a)) (1.35 R_s/R_so - 0.35)

- **Daily** (ch. 3, Eq 39): T_K^4 is the mean of T_max,K^4 and T_min,K^4, sigma = 4.903e-9
  MJ K-4 m-2 day-1, R_s/R_so limited to 1.0.
- **Hourly** (ch. 4, "Hourly time step"): sigma T_hr,K^4 replaces the mean, and sigma =
  2.043e-10 MJ m-2 hour-1. **At night** R_s/R_so is set to its value 2-3 h before sunset,
  the hour whose hour angle omega lies in (omega_s - 0.79) <= omega <= (omega_s - 0.52);
  or, more approximately, 0.4-0.6 in humid and subhumid climates and 0.7-0.8 in arid and
  semiarid ones; 0.3 "presumes total cloud cover".
- T_K = T + 273.16; e_a in kPa. R_nl is positive for a loss: R_n = R_ns - R_nl (Eq 40).

**How it was checked.** Read 2026-10-19 in FAO's HTML edition (fao.org/4/x0490e/,
x0490e07.htm and x0490e08.htm); Eq 39 and the hourly substitution are images there
(x0490e18, 24, 25 and 26.gif), read in the images. Example 19 (N'Diaye, Senegal, 02:00-03:00,
1 October) prints a night value the tests reproduce: 28 °C, e_a 3.402 kPa, R_s/R_so 0.8
assumed, R_nl = 0.100 MJ m-2 hour-1.

**What it is not.** It is the net longwave of the reference grass surface at air
temperature: the surface's own temperature, emissivity and the sky's cloud are folded into
the two empirical factors. FAO-56 prints no validation of them. Its night cloudiness comes
from the afternoon's sunshine, not from a cloud observation.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "allen1998.net_longwave"


def cloudiness_factor(rs_rso: np.ndarray, a: float, b: float) -> np.ndarray:
    """1.35 R_s/R_so - 0.35, with R_s/R_so limited to 1.0 as Eq 39 requires."""
    return a * np.minimum(np.asarray(rs_rso, dtype=np.float64), 1.0) - b


def humidity_factor(e_a_kpa: np.ndarray, a: float, b: float) -> np.ndarray:
    """0.34 - 0.14 sqrt(e_a), e_a in kPa."""
    return a - b * np.sqrt(np.asarray(e_a_kpa, dtype=np.float64))


def net_longwave(
    t_k4_mean: np.ndarray,
    e_a_kpa: np.ndarray,
    rs_rso: np.ndarray,
    sigma: float,
    humidity: tuple[float, float],
    cloudiness: tuple[float, float],
) -> np.ndarray:
    """Eq 39 given the period's mean T_K^4: sigma T^4 (0.34 - 0.14 sqrt(e_a)) (1.35 Rs/Rso - 0.35).

    Hourly, `t_k4_mean` is T_hr,K^4 and sigma 2.043e-10 MJ m-2 h-1; daily, the mean of
    T_max,K^4 and T_min,K^4 and sigma 4.903e-9 MJ m-2 day-1."""
    return (
        sigma
        * np.asarray(t_k4_mean, dtype=np.float64)
        * humidity_factor(e_a_kpa, *humidity)
        * cloudiness_factor(rs_rso, *cloudiness)
    )


def before_sunset(omega: np.ndarray, omega_s: np.ndarray, early: float, late: float) -> np.ndarray:
    """The hours 2-3 h before sunset: (omega_s - 0.79) <= omega <= (omega_s - 0.52), radians."""
    omega = np.asarray(omega, dtype=np.float64)
    return (omega >= np.asarray(omega_s) - early) & (omega <= np.asarray(omega_s) - late)
