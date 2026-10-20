"""FAO-56's atmospheric parameters: pressure, the psychrometric constant, saturation vapour
pressure, its slope and the density of air (Allen, Pereira, Raes & Smith 1998).

The constants SWEB (`magarey2006`) needs and does not print: Delta, delta, lambda, rho and
Cp. FAO-56 prints one value or formula for each:
- **Eq 7:** P = 101.3 ((293 - 0.0065 z) / 293)^5.26 (kPa; z in m);
- **Eq 8:** gamma = cp P / (epsilon lambda) = 0.665e-3 P (kPa/°C), with lambda = 2.45 MJ/kg,
  cp = 1.013e-3 MJ/(kg °C) and epsilon = 0.622;
- **Eq 11:** e°(T) = 0.6108 exp(17.27 T / (T + 237.3)) (kPa; T in °C);
- **Eq 13:** Delta = 4098 e°(T) / (T + 237.3)² (kPa/°C);
- **Eq 54:** e_a = e°(T_hr) RH_hr / 100 for an hourly step;
- **Annex 3, Eqs 3-5 and 3-7:** rho = 1000 P / (T_Kv R) = 3.486 P / T_Kv (kg/m³), R = 287
  J/(kg K), T_Kv ≈ 1.01 (T + 273).

**How it was checked.** Read 2026-10-19 in FAO's HTML edition (fao.org/4/x0490e/,
chapters 3 and 4 and Annex 3): the equations themselves are images there (x0490e0c, 0d, 0g,
0i and 43.gif), and each was read in its image. The tests check FAO-56's printed tables and
its Example 19.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "allen1998.psychrometrics"


def pressure_kpa(z_m: np.ndarray, p0: float, t0: float, lapse: float, power: float) -> np.ndarray:
    """Eq 7: mean atmospheric pressure (kPa) at elevation z (m): 101.3, 293, 0.0065, 5.26."""
    return p0 * ((t0 - lapse * np.asarray(z_m, dtype=np.float64)) / t0) ** power


def psychrometric_kpa(p_kpa: np.ndarray, cp: float, epsilon: float, lam: float) -> np.ndarray:
    """Eq 8: gamma = cp P / (epsilon lambda), kPa/°C (cp and lambda in MJ/kg units)."""
    return cp * np.asarray(p_kpa, dtype=np.float64) / (epsilon * lam)


def saturation_kpa(t_c: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
    """Eq 11: e°(T) = 0.6108 exp(17.27 T / (T + 237.3)), kPa."""
    t_c = np.asarray(t_c, dtype=np.float64)
    return a * np.exp(b * t_c / (t_c + c))


def slope_kpa(t_c: np.ndarray, a: float, b: float, c: float, k: float) -> np.ndarray:
    """Eq 13: Delta = 4098 e°(T) / (T + 237.3)², kPa/°C."""
    t_c = np.asarray(t_c, dtype=np.float64)
    return k * saturation_kpa(t_c, a, b, c) / (t_c + c) ** 2


def actual_kpa(e_sat_kpa: np.ndarray, rh_percent: np.ndarray) -> np.ndarray:
    """Eq 54: hourly actual vapour pressure, e°(T_hr) RH_hr / 100."""
    return np.asarray(e_sat_kpa) * np.asarray(rh_percent) / 100.0


def air_density(p_kpa: np.ndarray, t_c: np.ndarray, r_gas: float, virtual: float) -> np.ndarray:
    """Annex 3, Eqs 3-5 and 3-7: rho = 1000 P / (T_Kv R), T_Kv = 1.01 (T + 273); kg/m³."""
    t_kv = virtual * (np.asarray(t_c, dtype=np.float64) + 273.0)
    return 1000.0 * np.asarray(p_kpa) / (t_kv * r_gas)
