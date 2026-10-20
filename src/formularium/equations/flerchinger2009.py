"""Downward longwave radiation from air temperature, humidity and cloud cover: Dilley &
O'Brien's clear sky with Unsworth & Monteith's cloud correction, as Flerchinger et al. 2009
tested them (Water Resour. Res. 45:W03423).

    w = 465 e_o / T_o                                    (precipitable water, cm)
    L_clr = 59.38 + 113.7 (T_o / 273.16)^6 + 96.96 sqrt(w / 2.5)    (W m-2)
    eps_clr = L_clr / (sigma T_o^4)                      (back-calculated, as the paper did)
    eps_a = (1 - 0.84 c) eps_clr + 0.84 c                (Unsworth & Monteith 1975)
    L_d = eps_a sigma T_o^4

e_o in kPa, T_o in K, c the cloud fraction 0-1. Where cloud is not observed the paper takes
it from the clearness index k, linearly from c = 1 at k_cld to c = 0 at k_clr (after
Campbell 1985), with k_cld = 0.15 and k_clr = 0.80 the optimum for this pair (Table 9).

**How it was checked.** Read 2026-10-19 on the page images of pp. 2-3 (Tables 1-2), 8
(Tables 9-10) and the erratum of 2017 (p. 14). The erratum corrects Table 1: Dilley's last
term is 96.96 sqrt(w/2.5), not sqrt(w/25), and w = 465 e_o/T_o, not 4650 e_o/T_o. This module
uses the corrected forms.

**What it is not.** It gives the downward flux, not the net: the paper does not print a
net longwave. A canopy's net longwave at night is eps_s (L_d - sigma T_s^4), and T_s is not
the air temperature on a clear night. Its errors: RMSD 24.5 W m-2 for 30-min or hourly
values over 14 sites (7,920 days; Table 10), 26.9 W m-2 at 7 independent sites (Table 12);
midnight RMSD 25.0-25.6 W m-2 for the five best pairs, with cloud from the 24-hour window of
sunshine around each hour (p. 10).

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "flerchinger2009.dilley_unsworth"


def _a(x: np.ndarray) -> np.ndarray:
    return np.asarray(x, dtype=np.float64)


def precipitable_water(e_o_kpa: np.ndarray, t_o_k: np.ndarray, coefficient: float) -> np.ndarray:
    """Table 1, note c (as corrected): w = 465 e_o / T_o, in cm (Prata 1996)."""
    return coefficient * _a(e_o_kpa) / _a(t_o_k)


def dilley_clear_sky(
    t_o_k: np.ndarray, w_cm: np.ndarray, a: float, b: float, c: float, t_ref: float, w_ref: float
) -> np.ndarray:
    """Table 1 (as corrected): L_clr = 59.38 + 113.7 (T_o/273.16)^6 + 96.96 sqrt(w/2.5), W m-2."""
    return a + b * (_a(t_o_k) / t_ref) ** 6 + c * np.sqrt(_a(w_cm) / w_ref)


def clear_sky_emissivity(l_clr: np.ndarray, t_o_k: np.ndarray, sigma: float) -> np.ndarray:
    """eps_clr = L_clr / (sigma T_o^4), the back-calculation of p. 3 (para 13)."""
    return _a(l_clr) / (sigma * _a(t_o_k) ** 4)


def unsworth_emissivity(eps_clr: np.ndarray, cloud: np.ndarray, k: float) -> np.ndarray:
    """Table 2: eps_a = (1 - 0.84 c) eps_clr + 0.84 c (Unsworth & Monteith 1975)."""
    cloud = _a(cloud)
    return (1.0 - k * cloud) * _a(eps_clr) + k * cloud


def downward_longwave(eps_a: np.ndarray, t_o_k: np.ndarray, sigma: float) -> np.ndarray:
    """Eq 1-2's Stefan-Boltzmann form with the near-surface air temperature: eps_a sigma T_o^4."""
    return _a(eps_a) * sigma * _a(t_o_k) ** 4


def cloud_from_clearness(k: np.ndarray, k_cld: float, k_clr: float) -> np.ndarray:
    """p. 3, para 10 (Campbell 1985): c = 1 at k <= k_cld, 0 at k >= k_clr, linear between."""
    return np.clip((k_clr - _a(k)) / (k_clr - k_cld), 0.0, 1.0)
