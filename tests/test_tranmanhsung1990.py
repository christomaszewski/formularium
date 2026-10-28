"""POM's rain index and date of maturity against Tran Manh Sung et al. 1990's tables."""

from __future__ import annotations

import datetime as dt

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import tranmanhsung1990 as pom

REC = FORMULATIONS["tranmanhsung1990.pom"]
A, B = REC.published("a"), REC.published("b")

# Table 1, January's index (IJ), and Table 3, the date of maturity, 1977-1988 (pp. 123-124).
IJ = {
    1977: 175,
    1978: 31,
    1979: -23,
    1980: 128,
    1981: -16,
    1982: 86,
    1983: 144,
    1984: 33,
    1985: 141,
    1986: -19,
    1987: -71,
    1988: 189,
}
DOM = {
    1977: (3, 22),
    1978: (4, 21),
    1979: (5, 3),
    1980: (4, 1),
    1981: (5, 1),
    1982: (4, 9),
    1983: (3, 29),
    1984: (4, 21),
    1985: (3, 29),
    1986: (5, 2),
    1987: (5, 13),
    1988: (3, 19),
}


def _date(t: float) -> tuple[int, int]:
    d = dt.date(1977, 1, 1) + dt.timedelta(days=round(t) - 1)  # 365-day calendar, as printed
    return d.month, d.day


def test_the_dates_of_table_3_from_the_indices_of_table_1() -> None:
    days = {y: float(pom.maturity_day(ij, A, B)) for y, ij in IJ.items()}
    exact = [y for y in IJ if _date(days[y]) == DOM[y]]
    assert len(exact) == 11 and 1982 not in exact  # 1982: 99.84 gives 10 April, printed 9 April
    for y in IJ:
        printed = dt.date(1977, *DOM[y]).timetuple().tm_yday
        assert abs(round(days[y]) - printed) <= 1


def test_the_limit_dates_of_the_severity_classes() -> None:
    # p. 123: IJ of -17, 67 and 150 give 1 May, 14 April and 27 March.
    for ij, printed in ((-17, (5, 1)), (67, (4, 14)), (150, (3, 27))):
        assert _date(float(pom.maturity_day(ij, A, B))) == printed


def test_a_month_by_the_rules() -> None:
    # Own example: Hm 4, HM 10 mm; days 0, 2, 4, 6, 15 mm. POS 6 + 10 = 16; LAC 4 + 2 = 6
    # (4 mm is neither); EXC 5; Im = 16 - |5 - 6| + 3 = 18.
    rain = np.array([0.0, 2.0, 4.0, 6.0, 15.0])
    assert pom.month_terms(rain, 4.0, 10.0) == (16.0, 5.0, 6.0)
    assert pom.month_index(rain, 4.0, 10.0, previous=3.0) == pytest.approx(18.0)
    assert pom.maturation_indices([rain, rain], [(4.0, 10.0)] * 2) == pytest.approx([15.0, 30.0])


# Bordeaux-Mérignac (Météo-France station 33281001), daily rain in mm, 21 September 1983 to
# 31 January 1984, from Météo-France's "données climatologiques de base quotidiennes" (Licence
# Ouverte 2.0, read 2026-10-27). Monthly normals 1946-1987 from the same series: RM (mm) and
# the mean number of days with rain >= 0.1 mm.
MERIGNAC_1983_84 = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.3,
        0.0,
        0.0,
        0.0,
        0.2,
        0.0,
        1.5,
        2.3,
        2.4,
        14.8,
        1.2,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.6,
        3.4,
        0.0,
        0.0,
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.8,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.1,
        0.0,
        1.7,
        24.8,
        6.8,
        2.4,
        1.7,
        0.0,
    ],
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        12.4,
        0.3,
        3.0,
        6.6,
        0.0,
        0.1,
        0.0,
        11.0,
        21.9,
        9.5,
        12.5,
        3.4,
        11.8,
        39.3,
        1.1,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.2,
        0.0,
    ],
    [
        0.0,
        0.0,
        7.9,
        0.8,
        2.2,
        7.7,
        1.7,
        1.1,
        0.0,
        0.0,
        6.5,
        6.5,
        4.9,
        10.3,
        3.9,
        0.5,
        3.0,
        14.2,
        5.4,
        5.2,
        6.9,
        13.6,
        36.5,
        6.0,
        0.4,
        15.1,
        8.4,
        1.7,
        5.6,
        8.1,
        6.4,
    ],
]
RM = {9: 77.13, 10: 84.8, 11: 96.31, 12: 109.3, 1: 96.6}
RAINY_DAYS = {9: 12.74, 10: 13.24, 11: 15.38, 12: 17.14, 1: 16.69}
DAYS = {9: 30, 10: 31, 11: 30, 12: 31, 1: 31}
TABLE1_1984 = [-26, -75, -126, -79, 33]  # September 1983 to January 1984 (p. 123)


def test_the_station_reproduces_table_1_with_hm_the_mean_daily_rain() -> None:
    """Hm = RM / days in the month and HM = 9 mm (Ronzon p. 93) give 1984's column within 6.

    The paper and Ronzon print Hm = RM / the mean number of rainy days; read so, the same days
    give indices of a different size (the next test). See the record's flag.
    """
    assert all(
        len(m) == DAYS[k] - (20 if k == 9 else 0)
        for m, k in zip(MERIGNAC_1983_84, DAYS, strict=True)
    )
    limits = [(RM[m] / DAYS[m], 9.0) for m in DAYS]
    got = pom.maturation_indices([np.array(m) for m in MERIGNAC_1983_84], limits)
    assert [round(x) for x in got] == [-26, -77, -129, -77, 39]
    assert max(abs(round(g) - p) for g, p in zip(got, TABLE1_1984, strict=True)) <= 6


def test_hm_over_rainy_days_does_not_give_the_printed_size() -> None:
    limits = [(RM[m] / RAINY_DAYS[m], 9.0) for m in DAYS]
    got = pom.maturation_indices([np.array(m) for m in MERIGNAC_1983_84], limits)
    assert got[0] == pytest.approx(-60.5, abs=0.5)  # ten dry days at Hm = 6.05; printed -26
    assert got[-1] < -250  # printed 33
