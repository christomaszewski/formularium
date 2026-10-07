"""Magarey, Sutton & Thayer's generic infection model: the wetness an infection needs.

The temperature response is a beta function of three cardinal temperatures,

    f(T) = (t_max - T) / (t_max - t_opt) * ((T - t_min) / (t_opt - t_min)) ** a,
    a = (t_opt - t_min) / (t_max - t_opt),

which is 1 at t_opt and 0 at t_min and t_max. An infection needs w_min / f(T) hours of
wetness at a mean temperature T.

**How it was checked.** The paper was read on 2026-10-07, in the copy Cooptera holds
(Phytopathology 95:92-100; the Cooptera session read it, and the Agrarium session checked
the same lines):
- **Eq. 1** prints W(T) = Wmin / f(T) ≤ Wmax. "The parameter Wmax provides an upper boundary
  on the value of W(T) because wetness is not always a rate-limiting factor." Where Wmax
  is unknown, the paper gives Wmax = 3.8 + 3.0 Wmin (r = 0.71, RMS = 6.0 h, 64 studies).
- **Eq. 2** prints f(T) as above, "if Tmin ≤ T ≤ Tmax and 0 otherwise": Yin et al.'s
  temperature response. This module computes it operation for operation.
- **Table 2** gives each pathogen's parameters; the catalogue holds the grape rows.

**Two readings this module makes,** which the paper leaves open:
- **No cap.** These functions return Wmin / f(T) uncapped, and a caller with a Wmax applies
  it. Brischetto et al. 2021 give no Wmax for *P. viticola* (their Figure 2's 2 h and 4, 21
  and 30.2 °C are in the catalogue).
- **None outside the cardinal range.** The paper does not say how the cap meets f(T) = 0.
  Read literally, W could be held at Wmax even below Tmin or above Tmax. Here no infection
  is possible outside (t_min, t_max): the requirement is infinite.

The tests also hold this module to Cooptera's own transcription to 1e-12.

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
