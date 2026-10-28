"""POM, the date oospores mature from a rain index: Tran Manh Sung, Strizyk & Clerjeau 1990,
Plant Disease 74:120-124 (from Ronzon's 1987 thesis, where it was built).

For each day d of a month, with Rd the day's rain (mm) and the month's limits Hm < HM:
    Hm < Rd <= HM : POS(d) = Rd
    Rd < Hm       : LAC(d) = Hm - Rd          (a dry day lacks the whole Hm)
    Rd > HM       : EXC(d) = Rd - HM, POS(d) = HM
For the month: POS(M) = sum POS(d); NEG(M) = |sum EXC(d) - sum LAC(d)|;
    Im(M) = POS(M) - NEG(M) + Im(M - 1),
counted from 21 September. IJ is the index at the end of January, and
    T = A IJ + B
is the date of maturity (DOM) in days from 1 January (A = -0.21, B = 117.9).

The limits come from climatic normals (42 years, 1946-1987, at Bordeaux): Hm = RM / the
month's average number of rainy days; HM "= RM + the standard deviation of RM divided by the
number of rainy days in the month" (p. 122). That sentence can be read (RM + SD) / n, a daily
amount like Hm, or RM + SD / n; the page image has no brackets. The paper prints neither the
normals nor the limits. Ronzon 1987 (p. 93) takes the minimum the same way from 1951-1985
normals and the maximum as 18 / NJM = 9 mm, from the EPI model. So the limits are arguments.

**How it was checked.** Read 2026-10-27 in the page images of pp. 122-124 (the rules, Tables 1
and 3) and Ronzon's p. 93. A day exactly at Hm is neither POS nor LAC in the paper's rules; here
it counts as LAC = 0 (no effect). With T rounded to the nearest day on a 365-day calendar,
January's indices in Table 1 give 11 of Table 3's 12 dates exactly and 1982 a day late, and the
three limit indices give the printed 1 May, 14 April and 27 March.

**What the printed tables need (checked 2026-10-27 on Bordeaux-Merignac's daily rain).** Hm as
printed, RM over the rainy days, does not give indices of the printed size: a dry day then lacks
5-9 mm and January falls to -37 to -668. Hm as the month's mean daily rain, RM over the days in
the month, with HM = 9 mm, gives Table 1 within MAE 17 (January r = 0.98) and Ronzon's Tableau
25 within MAE 17. So pass rainy_days = the days in the month to lower_limit to reproduce the
paper; the record's flag gives the numbers. The rules themselves (a dry day lacks the whole Hm,
the count from 21 September) are as Ronzon prints them (p. 94).

Parameters are arguments, never defaults: each tool passes its own.
"""

from __future__ import annotations

import numpy as np

FORMULATION = "tranmanhsung1990.pom"


def month_terms(rain_mm: np.ndarray, hm: float, hm_max: float) -> tuple[float, float, float]:
    """POS(M), sum EXC(d) and sum LAC(d) for one month's daily rain."""
    rd = np.asarray(rain_mm, dtype=np.float64)
    pos = np.where((rd > hm) & (rd <= hm_max), rd, 0.0) + np.where(rd > hm_max, hm_max, 0.0)
    exc = np.where(rd > hm_max, rd - hm_max, 0.0)
    lac = np.where(rd < hm, hm - rd, 0.0)
    return float(pos.sum()), float(exc.sum()), float(lac.sum())


def month_index(rain_mm: np.ndarray, hm: float, hm_max: float, previous: float) -> float:
    """Im(M) = POS(M) - |EXC(M) - LAC(M)| + Im(M - 1)."""
    pos, exc, lac = month_terms(rain_mm, hm, hm_max)
    return pos - abs(exc - lac) + previous


def maturation_indices(months: list[np.ndarray], limits: list[tuple[float, float]]) -> list[float]:
    """Im at the end of each month, from the first (21-30 September) on; limits per month."""
    out, im = [], 0.0
    for rain, (hm, hm_max) in zip(months, limits, strict=True):
        im = month_index(rain, hm, hm_max, im)
        out.append(im)
    return out


def maturity_day(ij: np.ndarray, a: float, b: float) -> np.ndarray:
    """T = A IJ + B: the date of oospore maturity in days from 1 January (1 January = 1)."""
    return a * np.asarray(ij, dtype=np.float64) + b


def upper_limit_daily(rm: float, sd: float, rainy_days: float) -> float:
    """HM read as (RM + SD) / n, a daily amount (the reading this module's author prefers)."""
    return (rm + sd) / rainy_days


def lower_limit(rm: float, rainy_days: float) -> float:
    """Hm = RM / the month's average number of rainy days."""
    return rm / rainy_days
