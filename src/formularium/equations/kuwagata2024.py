"""One-layer energy balance of dew on a plant canopy (Kuwagata, Maruyama, Kondo & Watanabe 2024).

Eqs 1-28 of Agric. For. Meteorol. 354:109911, each as printed, in SI units: fluxes in W m-2,
temperatures in K, specific humidity in kg/kg, Delta = dq_SAT/dT in 1/K, rho in kg m-3, cp
in J kg-1 K-1, l in J/kg, exchange velocity k_L in m/s, dew W in mm (Eq 7 gives m/s of water;
times 1000 for mm/s). Effective radiation R_eff = R_d - sigma* T^4 is the driver throughout.

**How it was checked.** Every equation was read on the page images of the accepted
manuscript, pp. 5-15 (lines 111-335), 2026-10-19. The tests evaluate each one at a point,
check the approximate solution (Eqs 12-24) against itself and against a brute-force maximum
of Eq 14, and compare with the paper's printed rates (l. 508-511).

**Not printed in the paper,** so the caller passes it: q_SAT(T) and its slope Delta (Eq 11
defines Delta; no formula for q_SAT is given, only p_s = 1013 hPa, l. 164); cp, rho and l.

**Two printing errors found** (own derivation, 2026-10-19; each function follows the print):
- **Eq 19's two forms differ in sign.** rho {Delta R_eff + 4 sigma* T^3 (1 - rh) q} /
  (4 sigma* T^3) equals minus k_L0 cp rho^2 (1 - rh) q / (4 sigma* T^3) by Eq 17. Eq 15 gives
  the maximum condensation rate, positive, with the first form (`g2`); `g2_second_form`
  computes the second as printed.
- **Eq 21's numerator lacks k_Lm.** It prints {R_eff - l rho (1 - rh) q}, whose second term
  is J m-3, not W m-2; Eq 12 at k_L = k_Lm has l rho k_Lm (1 - rh) q. `canopy_temperature_at_klm`
  follows the print; `approximate_canopy_temperature` (Eq 12) at k_Lm gives the other.

**The exchange velocity k_L** is not printed here: "an empirical equation that considers
the effects of both natural and forced convection (Watanabe and Mizutani, 1996) as in
Maruyama et al. (2023)" (l. 263-266), with DL = 0.1 m. Maruyama et al. 2023 (J. Agric.
Meteorol. 79:28-37, Eqs 1-3, p. 30, read in the page image) print the leaf boundary-layer
conductance g_a = (lambda/D_L)(0.8 + 0.6 Re'^0.5) x 2, Re' = (Re^2 + Gr)^0.5, Re = u D_L / nu,
Gr = g D_L^3 |T_c - T_a| / (T_0 nu^2), naming g_a in m/s and lambda "the thermal conductivity
of the air (W m-1 K-1)". As printed the units do not close: lambda/D_L is W m-2 K-1, and
m/s needs a further division by rho cp. `maruyama_conductance` follows the print. Neither
paper prints lambda, nu, g or T_0. Kuwagata corrects the 2 m wind to the canopy top by
u = u_2m ln[(h - d)/z0] / ln[(z_obs - d)/z0], h = 1 m, d = 0.67 h, z0 = 0.1 m (l. 287-290).

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "kuwagata2024.canopy_dew"


def _a(x: np.ndarray) -> np.ndarray:
    return np.asarray(x, dtype=np.float64)


# -- 2.1.1 The one-layer model (Eqs 1-7) ----------------------------------------------------


def downward_radiative_flux(
    s_d: np.ndarray, l_d: np.ndarray, albedo: float, transmittance: float, emissivity: float
) -> np.ndarray:
    """Eq 2: R_d = (1 - r - tau) S_d + epsilon L_d (W m-2)."""
    return (1.0 - albedo - transmittance) * _a(s_d) + emissivity * _a(l_d)


def sigma_star(emissivity: float, sigma: float) -> float:
    """Eq 3: sigma* = epsilon sigma."""
    return emissivity * sigma


def heat_budget_residual(
    r_d: np.ndarray,
    t_s: np.ndarray,
    t_l: np.ndarray,
    h_l: np.ndarray,
    le_l: np.ndarray,
    s_star: float,
) -> np.ndarray:
    """Eq 1: R_d + sigma* T_S^4 - (H_L + lE_L + 2 sigma* T_L^4); zero when it balances."""
    return _a(r_d) + s_star * _a(t_s) ** 4 - (_a(h_l) + _a(le_l) + 2.0 * s_star * _a(t_l) ** 4)


def sensible_heat(cp: float, rho: float, k_l: np.ndarray, t_l: np.ndarray, t: np.ndarray):
    """Eq 4: H_L = cp rho k_L (T_L - T) (W m-2)."""
    return cp * rho * _a(k_l) * (_a(t_l) - _a(t))


def latent_heat(
    lat: float,
    rho: float,
    beta: float,
    k_l: np.ndarray,
    q_sat_tl: np.ndarray,
    rh: np.ndarray,
    q_sat_t: np.ndarray,
) -> np.ndarray:
    """Eq 5: lE_L = l rho beta k_L {q_SAT(T_L) - rh q_SAT(T)} (W m-2; negative condenses)."""
    return lat * rho * beta * _a(k_l) * (_a(q_sat_tl) - _a(rh) * _a(q_sat_t))


def effective_radiation_residual(
    r_eff: np.ndarray,
    t: np.ndarray,
    t_l: np.ndarray,
    h_l: np.ndarray,
    le_l: np.ndarray,
    s_star: float,
) -> np.ndarray:
    """Eq 6 (Eq 1 with T_S = T_L): R_eff - {H_L + lE_L + sigma* (T_L^4 - T^4)}.

    Eqs 4-6 are solved numerically for T_L (l. 152); the caller's root finder zeroes this."""
    return _a(r_eff) - (_a(h_l) + _a(le_l) + s_star * (_a(t_l) ** 4 - _a(t) ** 4))


def dew_rate(e_l: np.ndarray, rho_w: float) -> np.ndarray:
    """Eq 7: dW/dt = -E_L / rho_w (m of water per s; E_L in kg m-2 s-1)."""
    return -_a(e_l) / rho_w


# -- 2.1.2 Critical humidity and the largest rate (Eqs 8-11) -------------------------------


def critical_rh(q_sat_tl00: np.ndarray, q_sat_t: np.ndarray) -> np.ndarray:
    """Eq 8: rh_cr = q_SAT(T_L00) / q_SAT(T); no condensation below it."""
    return _a(q_sat_tl00) / _a(q_sat_t)


def canopy_temperature_still(r_eff: np.ndarray, t: np.ndarray, s_star: float) -> np.ndarray:
    """Eq 9: T_L00 = {R_eff / sigma* + T^4}^(1/4), the canopy temperature at k_L = 0."""
    return (_a(r_eff) / s_star + _a(t) ** 4) ** 0.25


def max_rate_saturated(
    r_eff: np.ndarray, slope: np.ndarray, cp: float, lat: float, rho_w: float
) -> np.ndarray:
    """Eq 10: dW/dt at rh = 1 and k_L = inf: -{R_eff Delta / (cp + l Delta)} / rho_w (m/s).

    Monteith (1961)'s expression (l. 195). Delta is Eq 11's dq_SAT/dT."""
    slope = _a(slope)
    return -(_a(r_eff) * slope / (cp + lat * slope)) / rho_w


# -- 2.1.3 The approximate solution (Eqs 12-14) --------------------------------------------


def approximate_canopy_temperature(
    r_eff: np.ndarray,
    t: np.ndarray,
    rh: np.ndarray,
    q_sat_t: np.ndarray,
    slope: np.ndarray,
    k_l: np.ndarray,
    s_star: float,
    rho: float,
    cp: float,
    lat: float,
) -> np.ndarray:
    """Eq 12: T_L - T = [R_eff - l rho k_L (1 - rh) q] / {4 sigma* T^3 + rho (cp + l Delta) k_L}.

    Returns T_L (K). Valid for |T_L - T| < 5 °C (l. 198)."""
    t, k_l = _a(t), _a(k_l)
    gap = (_a(r_eff) - lat * rho * k_l * (1.0 - _a(rh)) * _a(q_sat_t)) / (
        4.0 * s_star * t**3 + rho * (cp + lat * _a(slope)) * k_l
    )
    return t + gap


def approximate_sensible_heat(cp: float, rho: float, k_l: np.ndarray, t_l_hat, t) -> np.ndarray:
    """Eq 13: H_L = cp rho k_L (T_L - T) with Eq 12's T_L."""
    return sensible_heat(cp, rho, k_l, t_l_hat, t)


def approximate_dew_rate(
    rho: float,
    k_l: np.ndarray,
    rh: np.ndarray,
    q_sat_t: np.ndarray,
    slope: np.ndarray,
    t_l_hat: np.ndarray,
    t: np.ndarray,
    rho_w: float,
) -> np.ndarray:
    """Eq 14: dW/dt = -rho k_L {(1 - rh) q_SAT(T) + Delta (T_L - T)} / rho_w (m/s)."""
    return (
        -rho * _a(k_l) * ((1.0 - _a(rh)) * _a(q_sat_t) + _a(slope) * (_a(t_l_hat) - _a(t))) / rho_w
    )


# -- 2.1.4 Physical parameters of the approximate solution (Eqs 15-24) ----------------------


def g1(t: np.ndarray, slope: np.ndarray, s_star: float, rho: float, cp: float, lat: float):
    """Eq 18: G1(T) = 4 sigma* T^3 / {rho (cp + l Delta)} (m/s)."""
    return 4.0 * s_star * _a(t) ** 3 / (rho * (cp + lat * _a(slope)))


def g2(r_eff, rh, t, q_sat_t, slope, s_star: float, rho: float) -> np.ndarray:
    """Eq 19, first form: rho {Delta R_eff + 4 sigma* T^3 (1 - rh) q} / (4 sigma* T^3)."""
    b = 4.0 * s_star * _a(t) ** 3
    return rho * (_a(slope) * _a(r_eff) + b * (1.0 - _a(rh)) * _a(q_sat_t)) / b


def g2_second_form(k_l0, rh, t, q_sat_t, s_star: float, rho: float, cp: float) -> np.ndarray:
    """Eq 19, second form as printed: k_L0 cp rho^2 (1 - rh) q / (4 sigma* T^3).

    Minus the first form (see the module's note)."""
    return _a(k_l0) * cp * rho**2 * (1.0 - _a(rh)) * _a(q_sat_t) / (4.0 * s_star * _a(t) ** 3)


def critical_exchange_velocity(r_eff, rh, t, q_sat_t, slope, s_star: float, rho: float, cp: float):
    """Eq 17: k_L0 = -[Delta R_eff / {(1 - rh) q} + 4 sigma* T^3] / (cp rho); none above it."""
    return -(_a(slope) * _a(r_eff) / ((1.0 - _a(rh)) * _a(q_sat_t)) + 4.0 * s_star * _a(t) ** 3) / (
        cp * rho
    )


def exchange_velocity_at_max(g_1: np.ndarray, k_l0: np.ndarray) -> np.ndarray:
    """Eq 16: k_Lm = G1 {(1 + k_L0 / G1)^(1/2) - 1}."""
    g_1 = _a(g_1)
    return g_1 * (np.sqrt(1.0 + _a(k_l0) / g_1) - 1.0)


def max_rate(g_1, g_2, k_lm, k_l0, rho_w: float) -> np.ndarray:
    """Eq 15: dW/dt|m = (G2/rho_w) [G1 {1 - 2 (k_Lm/k_L0)} - k_Lm] / (1 + k_Lm/G1) (m/s)."""
    g_1, k_lm = _a(g_1), _a(k_lm)
    return (_a(g_2) / rho_w) * (g_1 * (1.0 - 2.0 * (k_lm / _a(k_l0))) - k_lm) / (1.0 + k_lm / g_1)


def approximate_still_temperature(r_eff, t, s_star: float) -> np.ndarray:
    """Eq 20: T_L00 = T + R_eff / (4 sigma* T^3)."""
    t = _a(t)
    return t + _a(r_eff) / (4.0 * s_star * t**3)


def canopy_temperature_at_klm(
    r_eff, t, rh, q_sat_t, slope, k_lm, s_star: float, rho: float, cp: float, lat: float
) -> np.ndarray:
    """Eq 21 as printed: T + {R_eff - l rho (1 - rh) q} / {4 sigma* T^3 + rho (cp + l Delta) k_Lm}.

    The numerator lacks k_Lm (see the module's note); its units do not close."""
    t = _a(t)
    return t + (_a(r_eff) - lat * rho * (1.0 - _a(rh)) * _a(q_sat_t)) / (
        4.0 * s_star * t**3 + rho * (cp + lat * _a(slope)) * _a(k_lm)
    )


def canopy_temperature_at_kl0(t, rh, q_sat_t, slope) -> np.ndarray:
    """Eq 22: T_L0 = T - (1 - rh) q_SAT(T) / Delta."""
    return _a(t) - (1.0 - _a(rh)) * _a(q_sat_t) / _a(slope)


def canopy_temperature_ventilated(t, rh, q_sat_t, slope, cp: float, lat: float) -> np.ndarray:
    """Eq 23: T_Linf = T - (1 - rh) q_SAT(T) / (cp/l + Delta)."""
    return _a(t) - (1.0 - _a(rh)) * _a(q_sat_t) / (cp / lat + _a(slope))


def approximate_critical_rh(r_eff, t, q_sat_t, slope, s_star: float) -> np.ndarray:
    """Eq 24: rh_cr = 1 + Delta R_eff / {4 sigma* T^3 q_SAT(T)}; Eqs 15-17, 21-22 hold above it."""
    return 1.0 + _a(slope) * _a(r_eff) / (4.0 * s_star * _a(t) ** 3 * _a(q_sat_t))


# -- 2.2 Reference and potential dew amounts (Eqs 25-27) ------------------------------------


def reference_dew(w0: np.ndarray, rate: np.ndarray, dt: float) -> np.ndarray:
    """Eq 25: W0(t + dt) = max[0, W0(t) + (dW/dt) dt], dW/dt at k_L from the wind."""
    return np.maximum(0.0, _a(w0) + _a(rate) * dt)


def potential_dew(wp: np.ndarray, rate_m_star: np.ndarray, dt: float) -> np.ndarray:
    """Eq 26: Wp(t + dt) = max[0, Wp(t) + (dW/dt|m*) dt]."""
    return np.maximum(0.0, _a(wp) + _a(rate_m_star) * dt)


def potential_rate(rate_m, rate_at_min_kl, rh, rh_cr) -> np.ndarray:
    """Eq 27: dW/dt|m* = dW/dt|m where rh >= rh_cr (27a), else dW/dt at k_L = c_hL u_min (27b)."""
    return np.where(_a(rh) >= _a(rh_cr), _a(rate_m), _a(rate_at_min_kl))


# -- 3.1.1 The fully ventilated canopy (Eq 28) ----------------------------------------------


def ventilated_residual(t_linf, q_sat_tlinf, t, rh, q_sat_t, cp: float, lat: float) -> np.ndarray:
    """Eq 28: T_Linf + (l/cp) q_SAT(T_Linf) - T - (l/cp) rh q_SAT(T); zero at the solution."""
    return _a(t_linf) + (lat / cp) * _a(q_sat_tlinf) - _a(t) - (lat / cp) * _a(rh) * _a(q_sat_t)


# -- The exchange velocity, from Maruyama et al. 2023 Eqs 1-3, and the wind (l. 287-290) -----


def maruyama_conductance(
    u: np.ndarray,
    dt_leaf_air: np.ndarray,
    d_l: float,
    conductivity: float,
    nu: float,
    g: float,
    t0: float,
    nusselt: tuple[float, float],
    sides: float,
) -> np.ndarray:
    """Maruyama et al. 2023 Eqs 1-3 as printed: (lambda/D_L)(0.8 + 0.6 Re'^0.5) x 2.

    Re' = (Re^2 + Gr)^0.5, Re = u D_L / nu, Gr = g D_L^3 |T_c - T_a| / (T_0 nu^2). With lambda
    a conductivity (W m-1 K-1), as printed, the result is W m-2 K-1, not the m/s printed."""
    re = _a(u) * d_l / nu
    gr = g * d_l**3 * np.abs(_a(dt_leaf_air)) / (t0 * nu**2)
    re_mixed = np.sqrt(re**2 + gr)
    a, b = nusselt
    return conductivity / d_l * (a + b * np.sqrt(re_mixed)) * sides


def canopy_top_wind(
    u_obs: np.ndarray, z_obs: float, height: float, displacement: float, z0: float
) -> np.ndarray:
    """l. 288: u = u_2m ln[(h - d)/z0] / ln[(z_obs - d)/z0], d = 0.67 h (m, m/s)."""
    d = displacement * height
    return _a(u_obs) * np.log((height - d) / z0) / np.log((z_obs - d) / z0)
