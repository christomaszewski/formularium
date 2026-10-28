"""Solar radiation intercepted by a vine row: Riou, Valancogne & Pieri 1989, Agronomie 9:441-450.

The row is a porous box of foliage height H, width L and wall porosity p, in rows D apart
(L < D/2). The sun enters through lambda, the ratio of the beam on a vertical wall to the beam on
the ground (Eqs 1-2):
    lambda = |cos h cos(a - a') / sin h|
with h the sun's elevation, a its azimuth from south and a' the azimuth of the row's normal
(pi/2 for north-south rows, 0 for east-west).

Direct light intercepted per unit ground, as a fraction of the direct beam on the ground Ih
(Eqs 22-27, p. 445):
    lambda <= L/H                    : (lambda H + L) / D
    L/H < lambda <= (D-L)/H          : [lambda H + L - p (lambda H - L)] / D
    (D-L)/H < lambda <= D/H          : [D - p (lambda H - L)] / D
    D/H < lambda <= (D+L)/H          : [D - p (2D - L - lambda H)] / D
    (D+L)/H < lambda <= (2D-L)/H     : [D - p (2D - L - lambda H) - p^2 (lambda H - D - L)] / D
    beyond, to lambda = 3D/H         : [D - p^3 (D - L)] / D            (Eq 27)
Diffuse light intercepted, as a fraction of the diffuse on the ground Rd (uniform sky, Eq 21):
    nd = (1 - p) nH + L/D + p nLi
    nH = (D - L)/D (1 - tan(i0/2)),  i0 = arctan((D - L)/H)              (Eq 16)
    nLi: the lower face of the foliage, between the elevations h2 (the next row) and h1 (its own
         walls), tan h1 = (2H/L) sin a, tan h2 = H/(D - L/2) sin a     (Eqs 17-19)
Absorbed and reflected, with leaf albedo af and soil albedo as, Rg = Ih + Rd (Eqs 28-29):
    Ra = (1 - af) [(1 - as nd) Ri + as nd Rg]
    Rr = [af - (1 - nd) as - 0.5 nd as af] Ri + [(1 - nd) as + 0.5 nd as af] Rg
The paper's values: p = 1/3, af = 0.20, as = 0.18; its test canopy D 1.8, H 0.9, L 0.3 m.

**How it was checked.** Read 2026-10-28 in the page images of pp. 443-445 (Eqs 1-29). Cases 1-5
of the direct beam meet at their bounds (algebra, and a test). Two things are not as printed:
- Eq 17 has no 1/pi, so an unobstructed lower face would take pi L/D of the diffuse light, and
  Eq 20 does not follow from it. Here nLi is Eq 17 normalised so that an open face takes L/D:
  nLi = (L/(pi D)) * integral over a in [0, pi] of (sin^2 h1 - sin^2 h2) da, which integrates
  to (L/D) [1/sqrt(1 + kd^2) - 1/sqrt(1 + kw^2)], kw = 2H/L, kd = H/(D - L/2) (our
  derivation, not printed).
- Eq 27 does not join Eq 26 at lambda H = 2D - L (Eq 26 gives D - p^2 (D - 2L) there), and the
  paper prints Eq 27's range only as "up to lambda <= 3D/H". Here Eq 27 is used beyond
  (2D - L)/H, as printed, and the step is left in.
The model gives the row's interception and the lit height of its walls (Eq 8), not leaf area by
depth. Validated at Latresne (Bordeaux), north-south rows, six September days: daily absorbed
27-180 W/m2 calculated against 29-180 measured (Table I). The record is `riou1989.row_interception`.

In the code, w is the foliage width L.

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "riou1989.row_interception"


def beam_ratio(elevation: np.ndarray, azimuth: np.ndarray, normal_azimuth: float) -> np.ndarray:
    """lambda = |cos h cos(a - a') / sin h| (Eqs 1-2); angles in radians, a from south."""
    h = np.asarray(elevation, dtype=np.float64)
    a = np.asarray(azimuth, dtype=np.float64)
    return np.abs(np.cos(h) * np.cos(a - normal_azimuth) / np.sin(h))


def lit_height(lam: np.ndarray, d: float, w: float, h: float) -> np.ndarray:
    """X = (D - L) / lambda, the sunlit height of a wall (Eq 8), at most H (Eq 9)."""
    lam = np.asarray(lam, dtype=np.float64)
    with np.errstate(divide="ignore"):
        x = np.where(lam > 0, (d - w) / lam, np.inf)
    return np.minimum(x, h)


def direct_fraction(lam: np.ndarray, d: float, w: float, h: float, p: float) -> np.ndarray:
    """The direct beam intercepted per unit ground, as a fraction of Ih (Eqs 22-27)."""
    if not w < d / 2:
        raise ValueError("the model assumes L < D/2 (p. 445)")
    lh = np.asarray(lam, dtype=np.float64) * h
    out = np.select(
        [lh <= w, lh <= d - w, lh <= d, lh <= d + w, lh <= 2 * d - w],
        [
            lh + w,
            lh + w - p * (lh - w),
            d - p * (lh - w),
            d - p * (2 * d - w - lh),
            d - p * (2 * d - w - lh) - p**2 * (lh - d - w),
        ],
        default=d - p**3 * (d - w),
    )
    return out / d


def upper_walls_diffuse(d: float, w: float, h: float) -> float:
    """nH, the diffuse share taken by the two walls if they were solid (Eq 16)."""
    i0 = np.arctan((d - w) / h)
    return float((d - w) / d * (1 - np.tan(i0 / 2)))


def lower_face_diffuse(d: float, w: float, h: float) -> float:
    """nLi, the diffuse share reaching the foliage's lower face (Eq 17, normalised; see above)."""
    kw, kd = 2 * h / w, h / (d - w / 2)
    return float(w / d * (1 / np.sqrt(1 + kd**2) - 1 / np.sqrt(1 + kw**2)))


def diffuse_fraction(d: float, w: float, h: float, p: float) -> float:
    """nd = (1 - p) nH + L/D + p nLi (Eq 21)."""
    return (1 - p) * upper_walls_diffuse(d, w, h) + w / d + p * lower_face_diffuse(d, w, h)


def intercepted(
    direct_h: np.ndarray,
    diffuse_h: np.ndarray,
    lam: np.ndarray,
    d: float,
    w: float,
    h: float,
    p: float,
) -> np.ndarray:
    """Ri, radiation intercepted per unit ground (W/m2), from Ih and Rd on the horizontal."""
    ih = np.asarray(direct_h, dtype=np.float64)
    rd = np.asarray(diffuse_h, dtype=np.float64)
    return direct_fraction(lam, d, w, h, p) * ih + diffuse_fraction(d, w, h, p) * rd


def absorbed(ri: np.ndarray, rg: np.ndarray, nd: float, a_leaf: float, a_soil: float) -> np.ndarray:
    """Ra = (1 - af) [(1 - as nd) Ri + as nd Rg] (Eq 28)."""
    ri = np.asarray(ri, dtype=np.float64)
    return (1 - a_leaf) * ((1 - a_soil * nd) * ri + a_soil * nd * np.asarray(rg))


def reflected(
    ri: np.ndarray, rg: np.ndarray, nd: float, a_leaf: float, a_soil: float
) -> np.ndarray:
    """Rr = [af - (1 - nd) as - 0.5 nd as af] Ri + [(1 - nd) as + 0.5 nd as af] Rg (Eq 29)."""
    ri = np.asarray(ri, dtype=np.float64)
    k = (1 - nd) * a_soil + 0.5 * nd * a_soil * a_leaf
    return (a_leaf - k) * ri + k * np.asarray(rg)
