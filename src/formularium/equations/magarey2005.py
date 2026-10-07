"""Magarey, Sutton & Thayer's generic infection model: the wetness an infection needs.

The temperature response is a beta function of three cardinal temperatures,

    f(T) = (t_max - T) / (t_max - t_opt) * ((T - t_min) / (t_opt - t_min)) ** a,
    a = (t_opt - t_min) / (t_max - t_opt),

which is 1 at t_opt and 0 at t_min and t_max. An infection needs w_min / f(T) hours of
wetness at a mean temperature T, and none is possible outside (t_min, t_max). The 2005
paper also caps the requirement at a w_max; Brischetto et al. 2021 give none for
*Plasmopara viticola*, so these functions apply no cap. A caller with a w_max applies it.

**How it was checked.** The 2005 paper was not read: APS refused the fetch on 2026-10-07.
The form is the one Cooptera transcribed (`standalone/brischetto.py`) and Agrarium wrote
(`world/downy_mildew.py`); the tests hold this module to Cooptera's values to 1e-12. The
parameters Brischetto et al. 2021 give for *P. viticola* (2 h; 4, 21 and 30.2 °C) were
read in their Figure 2's caption and are in the catalogue.

The arithmetic is Agrarium's, operation for operation, so its numbers do not change.
Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "magarey2005.generic"


def _response(t: np.ndarray, t_min: float, t_opt: float, t_max: float) -> np.ndarray:
    return (
        (t_max - t)
        / (t_max - t_opt)
        * ((t - t_min) / (t_opt - t_min)) ** ((t_opt - t_min) / (t_max - t_opt))
    )


def temperature_response(t: np.ndarray, cardinal: tuple[float, float, float]) -> np.ndarray:
    """f(T): 1 at the optimum, falling to 0 at the cardinal minimum and maximum."""
    t_min, t_opt, t_max = cardinal
    t = np.asarray(t, dtype=np.float64)
    inside = (t > t_min) & (t < t_max)
    tc = np.clip(t, t_min + 1e-9, t_max - 1e-9)
    return np.where(inside, _response(tc, t_min, t_opt, t_max), 0.0)


def required_wet_hours(
    t: np.ndarray, cardinal: tuple[float, float, float], w_min: float
) -> np.ndarray:
    """Hours of wetness an infection needs at mean temperature T: w_min / f(T), inf outside."""
    t_min, t_opt, t_max = cardinal
    t = np.asarray(t, dtype=np.float64)
    inside = (t > t_min) & (t < t_max)
    tc = np.clip(t, t_min + 1e-9, t_max - 1e-9)
    response = _response(tc, t_min, t_opt, t_max)
    with np.errstate(divide="ignore"):
        return np.where(inside, w_min / response, np.inf)
