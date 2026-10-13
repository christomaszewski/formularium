"""A stage's day of year as a linear function of monthly temperature means.

Fraga et al. 2016 (J. Agric. Sci. 154:795-811, Eqs 1-6) fit, for each variety and stage,

    DOY = k + alpha * x1 (+ beta * x2),

where x1 and x2 are means of daily Tmin, Tmax or Tmean over a window of calendar months
(budburst on the January-March or February-March minima, flowering on the March-April
maxima, veraison on two windows). Tables 5-7 print k, alpha and beta for 14 varieties; the
catalogue holds them (`fraga2016.monthly_regression`). Didevarasl et al. 2026 (Int. J.
Biometeorol. 70:273, Table 4) print the same form for Cannonau with up to six monthly
terms, temperatures and precipitation (`didevarasl2026.monthly_regression`), and run
through the same sum.

No heat is summed to a threshold: the date is read straight off the season's monthly
means, so the form can only be applied once those months have passed.

**How it was checked.** Fraga's equations (p. 802) and Tables 5-7 (pp. 804-805) were read
in the page images on 2026-10-13 (literature/fraga2016); Didevarasl's Table 4 in the
publisher's HTML (literature/didevarasl2026). The tests hold the sum to the printed
coefficients.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

FORMULATION = "fraga2016.monthly_regression"


def stage_doy(
    intercept: float, coefficients: Sequence[float], predictors: Sequence[np.ndarray]
) -> np.ndarray:
    """k + sum(c_i * x_i): the day of year, one value per season.

    `coefficients` are the printed alpha, beta, ... in days per unit of their predictor;
    `predictors` the matching monthly means (°C) or totals (mm), each an array over
    seasons of the same shape.
    """
    if len(coefficients) != len(predictors):
        raise ValueError("one coefficient per predictor")
    if not predictors:
        raise ValueError("at least one predictor")
    out = np.full(np.shape(predictors[0]), float(intercept))
    for c, x in zip(coefficients, predictors, strict=True):
        out = out + float(c) * np.asarray(x, dtype=float)
    return out
