"""SWEB: surface wetness from a water budget and an energy balance (Magarey, Russo & Seem 2006).

Eqs 1-15 of Agric. For. Meteorol. 139:373-381, each as printed, in the paper's units
(Table 2): water depths in cm, rates in cm/min, time in minutes, wind in cm/min, heights in
cm, vapour pressures in mbar, Delta and delta in mbar/°C, lambda in J/g, rho in g/cm³, Cp in
J/(g °C), net radiation in J/(min cm²), c in cm^0.5 min^-0.5.

**How it was checked.** Every equation was read on the page images of pp. 375-377 (150 and
300 dpi, 2026-10-19), and Table 1's order of calculation on p. 375. The tests evaluate each
formula at a point and run the sensitivity case of p. 378 against Fig. 1.

**What the paper does not print,** so a caller passes it: Delta(T), delta, lambda, rho and
Cp (FAO-56's, in `allen1998_psychrometrics`, are one published choice); the time step (10
min in the sensitivity runs, hourly in the validation); and the canopy net radiation at
night, an input the authors measured.

**Eq 15 as printed is not dimensionally sound.** Its second factor is
[1 + alpha (1 - Zc)/Z]^-2 with Zc and Z in cm; Amir 2016 and Dhakar et al. 2025 print it the
same way. `canopy_wind` computes it as printed. At Zc = 150 cm and Z = 200 cm the factor is
about 1000, and the sensitivity case then dries in minutes, not the 150 min of Fig. 1A (see
the tests). No form that reproduces the authors' runs is printed in any source read, so none
is given here: the canopy wind is the caller's until a source settles it.

**Three readings `step` makes,** each where the paper leaves a choice open:
- **The budget's order** is Table 1's: interception and dew are added to the previous
  store (step 5, "initial canopy water budget"), the wet area comes from that store (step 6),
  evaporation is taken from it (steps 9-10), and both stores are held within 0 and C, as
  Eq 7's "for 0 < S < C" says. Eq 14's W is the one step 6 gives, though its text says "in
  previous time step".
- **The sign of the dew term.** Eq 12 gives Dp with the sign of Rnc, and Eq 7 adds Dp.
  The paper names Rnc "canopy net radiant flux density" with no sign convention; in Eq 9 a
  positive Rn adds to evaporation. `step` takes Rnc in Eq 9's convention (positive into the
  canopy) and adds the condensation -Eq 12 when Rnc < 0, nothing otherwise. Rnc is used only
  at night (p. 375); the caller passes zero by day. What counts as night is not printed.
- **Equality in Eqs 1-2.** SW = 1 for Wind > Wth and 0 for Wind < Wth; Wind = Wth is in
  neither. `surface_wetness` counts it dry.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "magarey2006.sweb"


def surface_wetness(w_ind: np.ndarray, w_th: float) -> np.ndarray:
    """Eqs 1-2: 1 where the wet-area index exceeds the threshold, else 0 (equality dry)."""
    return (np.asarray(w_ind, dtype=np.float64) > w_th).astype(np.float64)


def wet_area_index(s: np.ndarray, c: np.ndarray, exponent: float) -> np.ndarray:
    """Eq 3: Wind = (S/C)^0.67, the index of the canopy's wet surface area."""
    return (np.asarray(s, dtype=np.float64) / np.asarray(c, dtype=np.float64)) ** exponent


def wet_fraction(w_ind: np.ndarray, w_max: float) -> np.ndarray:
    """Eq 4: W = Wind x Wmax, the actual fraction of the canopy surface that is wet."""
    return np.asarray(w_ind, dtype=np.float64) * w_max


def max_wet_area(p: float, w_f: float, w_d: float) -> float:
    """Eq 5: Wmax = p Wf + (1 - p) Wd (Wf, Wd and p are printed nowhere found)."""
    return p * w_f + (1.0 - p) * w_d


def storage_capacity(lai: np.ndarray, c_l: float) -> np.ndarray:
    """Eq 6: C = LAI x Cl, the canopy's maximum water storage (cm)."""
    return np.asarray(lai, dtype=np.float64) * c_l


def interception(lai: np.ndarray, rain: np.ndarray, k: float) -> np.ndarray:
    """Eq 8: I = (1 - exp(-0.5 LAI)) P, rain intercepted (cm), after Norman & Campbell 1983."""
    return (1.0 - np.exp(-k * np.asarray(lai, dtype=np.float64))) * np.asarray(rain)


def potential_evaporation_full(
    rn: np.ndarray,
    rho: float,
    cp: float,
    h: np.ndarray,
    slope: np.ndarray,
    lam: float,
    psy: float,
    e_sat: np.ndarray,
    e_air: np.ndarray,
) -> np.ndarray:
    """Eq 9, Tanner & Fuchs's combination formula with the radiation term (cm/min).

    SWEB uses it only through Eqs 10 and 12: daytime net radiation is ignored (p. 377)."""
    slope = np.asarray(slope, dtype=np.float64)
    return (
        slope
        / (lam * (slope + psy))
        * (np.asarray(rn) + rho * cp * (np.asarray(h) / slope) * (np.asarray(e_sat) - e_air))
    )


def potential_evaporation(
    rho: float,
    cp: float,
    h: np.ndarray,
    slope: np.ndarray,
    lam: float,
    psy: float,
    e_sat: np.ndarray,
    e_air: np.ndarray,
) -> np.ndarray:
    """Eq 10: Ep from the aerodynamic term of Eq 9 alone (cm/min of water)."""
    slope = np.asarray(slope, dtype=np.float64)
    return (
        slope
        / (lam * (slope + psy))
        * (rho * cp * (np.asarray(h) / slope) * (np.asarray(e_sat) - e_air))
    )


def evaporation(ep: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Eq 11: E = Ep W (cm/min)."""
    return np.asarray(ep) * np.asarray(w)


def potential_condensation(
    rnc: np.ndarray, slope: np.ndarray, lam: float, psy: float, share: float
) -> np.ndarray:
    """Eq 12 as printed: Dp = Delta / (lambda (Delta + delta)) x 0.5 Rnc (cm/min).

    It has Rnc's sign; see the module's note on how `step` adds it."""
    slope = np.asarray(slope, dtype=np.float64)
    return slope / (lam * (slope + psy)) * share * np.asarray(rnc)


def transfer_coefficient(c: np.ndarray, u_c: np.ndarray) -> np.ndarray:
    """Eq 13: h = c Uc^0.5 (cm/min), after Bird et al. 1960."""
    return np.asarray(c) * np.sqrt(np.asarray(u_c, dtype=np.float64))


def shape_scale(w: np.ndarray, c_f: float, c_d: float) -> np.ndarray:
    """Eq 14: c = W cf + (1 - W) cd, between film and drop constants."""
    w = np.asarray(w, dtype=np.float64)
    return w * c_f + (1.0 - w) * c_d


def canopy_wind(
    u_z: np.ndarray,
    z_c: float,
    z: float,
    alpha: float,
    displacement_share: float,
    roughness_share: float,
) -> np.ndarray:
    """Eq 15 exactly as printed (cm/min), with D_Z = 2/3 Zc and Z0 = Z/10 as stated.

        Uc = U_Z (ln[(Zc - D_Z)/Z0] / ln[(Z - D_Z)/Z0]) [1 + alpha ((1 - Zc)/Z)]^-2

    `displacement_share` is the 2/3 and `roughness_share` the 1/10. The second factor is
    not dimensionless as printed (1 - Zc, with Zc in cm); this function does not repair it.
    """
    d_z = displacement_share * z_c
    z0 = roughness_share * z
    log_ratio = np.log((z_c - d_z) / z0) / np.log((z - d_z) / z0)
    return np.asarray(u_z, dtype=np.float64) * log_ratio * (1.0 + alpha * ((1.0 - z_c) / z)) ** -2


def step(
    s_prev: np.ndarray,
    rain: np.ndarray,
    rnc: np.ndarray,
    lai: np.ndarray,
    u_c: np.ndarray,
    slope: np.ndarray,
    e_sat: np.ndarray,
    e_air: np.ndarray,
    *,
    dt_min: float,
    c_l: float,
    w_max: float,
    w_th: float,
    wind_exponent: float,
    interception_k: float,
    dew_share: float,
    c_d: float,
    c_f: float,
    rho: float,
    cp: float,
    lam: float,
    psy: float,
) -> tuple[np.ndarray, np.ndarray]:
    """One time step in Table 1's order: the new store S (cm) and the surface wetness SW.

    Inputs per step: rain above the canopy (cm in the step), canopy net radiation (J min-1
    cm-2, positive into the canopy; zero by day), canopy wind Uc (cm/min, the caller's: see
    the note on Eq 15), and Delta, e*, e_a at canopy temperature and humidity (mbar/°C, mbar).
    """
    cap = storage_capacity(lai, c_l)  # 1. Eq 6
    intercepted = interception(lai, rain, interception_k)  # 3. Eq 8
    dew = np.maximum(-potential_condensation(rnc, slope, lam, psy, dew_share), 0.0)  # 4. Eq 12
    s_i = np.clip(np.asarray(s_prev) + intercepted + dew * dt_min, 0.0, cap)  # 5. Eq 7
    with np.errstate(divide="ignore", invalid="ignore"):
        w_ind = np.where(cap > 0, wet_area_index(s_i, cap, wind_exponent), 0.0)  # 6. Eq 3
    w = wet_fraction(w_ind, w_max)  # 6. Eq 4
    h = transfer_coefficient(shape_scale(w, c_f, c_d), u_c)  # 8. Eqs 13-14
    ep = potential_evaporation(rho, cp, h, slope, lam, psy, e_sat, e_air)  # 9. Eq 10
    s = np.clip(s_i - evaporation(ep, w) * dt_min, 0.0, cap)  # 10. Eqs 11 and 7
    with np.errstate(divide="ignore", invalid="ignore"):
        w_ind = np.where(cap > 0, wet_area_index(s, cap, wind_exponent), 0.0)  # 11. Eq 3
    return s, surface_wetness(w_ind, w_th)  # 12. Eqs 1-2
