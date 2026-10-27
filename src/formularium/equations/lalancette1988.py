"""Infection efficiency of Plasmopara viticola by temperature and wetness duration: Lalancette,
Ellis & Madden 1988, Phytopathology 78:794-800, equation 5.

    IE = k (1 + e^(-rho))^(1/(1 - m))                       (lesions per zoospore)
    k   = b0 + b1 T + b2 T^2 + offset
    rho = r W = c1 W + c2 W T + c3 W T^2,  W = wetness duration (h) - 1

T in °C. The paper's averaged-data values are k: -0.071, 0.018, -0.0005, offset 0.01; rho:
-0.24, 0.070, -0.0021; m = 1.2 (record `lalancette1988.infection`).

**How it was checked.** Read 2026-10-27 in the page image of p. 798 (equation 5), with
equations 2-4 (p. 795: the linearized Richards form ln[(IE/k)^(1-m) - 1] = -r W, W = wet
hours minus 1) and Table 1 (p. 796). The exponent is e^(-rho): several later copies print
e^(+rho), which makes IE fall as wetness lengthens (the record's flags list them). The
offset 0.01 was added to k by the authors so that no observed IE exceeded it (p. 795);
Fig. 2A's dashed line is k + 0.01.

**What it is not.** Fitted on V. labrusca 'Catawba' in growth chambers at 5-30 °C, 1-15 h of
wetness. Outside about 4.5-31.5 °C k is negative and so is IE: the function does not clip;
a tool decides what to do there. The printed coefficients are rounded (Table 1 gives the
same two figures); they put k's maximum at 0.091 at 18.0 °C, where the text prints 0.083 at
17.5 °C from the unrounded fit.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "lalancette1988.infection"


def asymptote(t_c: np.ndarray, b0: float, b1: float, b2: float, offset: float) -> np.ndarray:
    """k, the maximum infection efficiency at temperature T (equation 1 plus the offset)."""
    t = np.asarray(t_c, dtype=np.float64)
    return b0 + b1 * t + b2 * t**2 + offset


def rate(t_c: np.ndarray, c1: float, c2: float, c3: float) -> np.ndarray:
    """r, the Richards rate at temperature T (equation 3; rho = r W)."""
    t = np.asarray(t_c, dtype=np.float64)
    return c1 + c2 * t + c3 * t**2


def infection_efficiency(
    t_c: np.ndarray,
    wet_hours: np.ndarray,
    b0: float,
    b1: float,
    b2: float,
    offset: float,
    c1: float,
    c2: float,
    c3: float,
    m: float,
) -> np.ndarray:
    """Equation 5: lesions per zoospore after `wet_hours` of wetness at `t_c` °C."""
    w = np.asarray(wet_hours, dtype=np.float64) - 1.0
    rho = rate(t_c, c1, c2, c3) * w
    return asymptote(t_c, b0, b1, b2, offset) * (1.0 + np.exp(-rho)) ** (1.0 / (1.0 - m))
