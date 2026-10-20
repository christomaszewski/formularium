"""A leaf-wetness sensor's plate as a simplified mechanistic model, M1 and M2 (Dhakar et al. 2025).

Eqs 1-11 of Agric. For. Meteorol. 363:110399, each as printed. M1 is Eqs 2-10: dew by an
energy balance on a flat plate (Eqs 3-6), rain capped at 0.6 mm an event, evaporation by
SWEB's combination equation (Eqs 7-10). M2 adds Eq 11: no dew while the dew-point
depression exceeds DPDc. Eq 1 turns the sensor's raw counts into the 0-1 wetness it is
scored on. Units as Table 2 and the text print them: temperatures in °C, wind in m/s,
resistances in s/m, rho_a 1.293 kg m-3, Cp 1005 J kg-1 K-1, nu 15.1e-6 and kappa 2.15e-5
m2/s, D_wv 2.12e-5 m2/s; Uc in cm/min, c in cm^0.5 min^-0.5, Ep, Df, E and LW in mm.

**How it was checked.** Eqs 1-11 and Table 2 were read on the page images of pp. 3-5 (150
and 260 dpi), 2026-10-19.

**What the print leaves open,** each followed here as printed and flagged in the record:
- **Eq 3** sums three heat-transfer coefficients times A times DPD: dew grows with the
  dew-point depression and is never zero while DPD > 0 (M1 has no gate). Its 4 epsilon sigma
  T_air^3 term needs kelvin, and Table 2 gives T_air in °C; epsilon is not given a value.
  The text says the detailed dewfall equations are in Appendix A, which is in the online
  supplement, not held.
- **Eq 6,** Df = E_dew / A x 60 x 15, gives J m-2 per 15 min, not mm: no latent heat
  divides it as printed.
- **gamma** is printed as 2.4567 x 10^-1 Pa K^-1, about 270 times smaller than the
  psychrometric constant near sea level (about 66 Pa K-1). lambda (Eq 7) has no value.
- **Eq 7** mixes units (rho_a in kg m-3 and Cp in J kg-1 K-1 with h in cm/min and vapour
  pressures in kPa) and names Ep in mm.
- **Eq 8** weights Cf and Cd by Wmax; SWEB's Eq 14 weights them by the wet fraction W.
- **Eq 9** prints ln(Zc - Zd/Z0) and (1 + alpha (1 - Zc)/Zref)^-2, the second as SWEB's
  Eq 15 prints it; Zd and Z0 are listed as outputs (Table 3) with no rule printed.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "dhakar2025.leaf_wetness"


def _a(x: np.ndarray) -> np.ndarray:
    return np.asarray(x, dtype=np.float64)


def sensor_wetness(counts: np.ndarray, dry: float, span: float) -> np.ndarray:
    """Eq 1: (sensor value - 435) / 665, the PHYTOS 31's counts on a 0-1 scale (0.4 is wet)."""
    return (_a(counts) - dry) / span


def leaf_wetness(
    dewfall: np.ndarray, rain: np.ndarray, evaporation: np.ndarray, t_air
) -> np.ndarray:
    """Eq 2: LW = Df + Ri - E for T_air > 0 °C (mm); NaN at or below freezing, as excluded."""
    lw = _a(dewfall) + _a(rain) - _a(evaporation)
    return np.where(_a(t_air) > 0.0, lw, np.nan)


def boundary_resistance(ws: np.ndarray, d: float, nu: float, kappa: float, a: float, b: float):
    """Eq 4: r_B = d / (Nu kappa), Nu = 0.72 Re^0.6, Re = WS d / nu (s/m)."""
    re = _a(ws) * d / nu
    return d / ((a * re**b) * kappa)


def stomatal_resistance(n: float, pore_diameter: float, pore_length: float, d_wv: float) -> float:
    """Eq 5: r_S = 4 (L_p + pi D_p / 8) / (pi n D_p^2 D_wv) (s/m; D_p and L_p in m)."""
    return 4.0 * (pore_length + np.pi * pore_diameter / 8.0) / (np.pi * n * pore_diameter**2 * d_wv)


def dew_energy(
    t_air: np.ndarray,
    dpd: np.ndarray,
    r_b: np.ndarray,
    r_s: float,
    slope: np.ndarray,
    *,
    emissivity: float,
    sigma: float,
    rho_a: float,
    cp: float,
    gamma: float,
    area: float,
) -> np.ndarray:
    """Eq 3: E_dew = [4 eps sigma T^3 + rho Cp / r_B + rho Cp Delta / {gamma (r_B + r_S)}] A DPD.

    As printed: W for A in m2. `t_air` enters the radiative term as given (it needs kelvin)."""
    r_b = _a(r_b)
    coefficient = (
        4.0 * emissivity * sigma * _a(t_air) ** 3
        + rho_a * cp / r_b
        + rho_a * cp * _a(slope) / (gamma * (r_b + r_s))
    )
    return coefficient * area * _a(dpd)


def dewfall(e_dew: np.ndarray, area: float, seconds: float, minutes: float) -> np.ndarray:
    """Eq 6 as printed: Df = E_dew / A x 60 x 15 (J m-2 in the 15 min; printed as mm)."""
    return _a(e_dew) / area * seconds * minutes


def interception(rain: np.ndarray, cap: float) -> np.ndarray:
    """2.3.1.3: the measured rain, up to 0.6 mm (per event: the caller sums an event)."""
    return np.minimum(_a(rain), cap)


def potential_evaporation(
    slope: np.ndarray,
    gamma: float,
    lam: float,
    rho_a: float,
    cp: float,
    c: float,
    u_c: np.ndarray,
    svp: np.ndarray,
    avp: np.ndarray,
) -> np.ndarray:
    """Eq 7 as printed: Delta / ((gamma + Delta) lambda) [rho Cp (c Uc^0.5 / Delta)(SVP - AVP)]."""
    slope = _a(slope)
    return (
        slope
        / ((gamma + slope) * lam)
        * (rho_a * cp * (c * np.sqrt(_a(u_c)) / slope) * (_a(svp) - _a(avp)))
    )


def shape_scale(w_max: float, c_f: float, c_d: float) -> float:
    """Eq 8: c = Wmax Cf + (1 - Wmax) Cd."""
    return w_max * c_f + (1.0 - w_max) * c_d


def canopy_wind(
    u_z: np.ndarray, z_c: float, z_ref: float, z_d: float, z_0: float, alpha: float
) -> np.ndarray:
    """Eq 9 exactly as printed: Uz (ln(Zc - Zd/Z0) / ln(Zref - Zd/Z0)) (1 + alpha (1 - Zc)/Zref)^-2.

    NaN where a logarithm's argument is not positive. Zd and Z0 have no printed rule."""
    with np.errstate(invalid="ignore", divide="ignore"):
        ratio = np.log(z_c - z_d / z_0) / np.log(z_ref - z_d / z_0)
    return _a(u_z) * ratio * (1.0 + alpha * (1.0 - z_c) / z_ref) ** -2


def evaporation(ep: np.ndarray, w_f: float, w_max: float) -> np.ndarray:
    """Eq 10 with W = Wf x Wmax (p. 5): E = Ep W."""
    return _a(ep) * (w_f * w_max)


def gated_dewfall(dewfall_mm: np.ndarray, dpd: np.ndarray, dpd_c: float) -> np.ndarray:
    """Eq 11 (M2): Df = 0 where DPD > DPDc, else Df."""
    return np.where(_a(dpd) > dpd_c, 0.0, _a(dewfall_mm))


def wet(lw: np.ndarray) -> np.ndarray:
    """2.3.1.5: 1 where the estimated LW is above 0 mm, else 0."""
    return (np.nan_to_num(_a(lw), nan=0.0) > 0.0).astype(np.float64)
