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
