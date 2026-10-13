"""The monthly-mean regressions, against the coefficients their sources print."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations.monthly_regression import stage_doy

FRAGA = FORMULATIONS["fraga2016.monthly_regression"]
DIDEVARASL = FORMULATIONS["didevarasl2026.monthly_regression"]


def test_fragas_alvarinho_budburst_is_eq_1_with_table_5s_numbers() -> None:
    # Table 5 (p. 804): Alvarinho budburst k = 123.68, alpha = -6.10 on TminFeb-Mar (Eq. 1).
    k = FRAGA.published("budburst.alvarinho.k")
    a = FRAGA.published("budburst.alvarinho.alpha")
    assert (k, a) == (123.68, -6.10)
    x = np.array([0.0, 1.0, 10.0])
    assert stage_doy(k, (a,), (x,)) == pytest.approx([123.68, 117.58, 62.68])


def test_fragas_merlot_veraison_is_eq_6_with_table_6s_numbers() -> None:
    # Table 6 (p. 805): Merlot veraison k = 554.83, alpha = -5.62 on TmaxJun-Jul,
    # beta = -13.94 on TmeanMar-Apr (Eq. 6).
    k, a, b = (FRAGA.published(f"veraison.merlot.{p}") for p in ("k", "alpha", "beta"))
    assert (k, a, b) == (554.83, -5.62, -13.94)
    doy = stage_doy(k, (a, b), (np.array([28.0, 30.0]), np.array([14.0, 15.0])))
    assert doy == pytest.approx([554.83 - 5.62 * 28 - 13.94 * 14, 554.83 - 5.62 * 30 - 13.94 * 15])


def test_fragas_fourteen_varieties_are_all_held() -> None:
    names = {p.name for p in FRAGA.parameters}
    varieties = {n.split(".")[1] for n in names}
    assert len(varieties) == 14
    for v in varieties:
        assert {f"budburst.{v}.k", f"flowering.{v}.alpha", f"veraison.{v}.beta"} <= names


def test_didevarasls_budburst_is_table_4s_line() -> None:
    # Table 4: DOY = 12.468353 + 1.520173 (Jun-1 TX) + 2.505555 (Oct-1 TN)
    #   - 0.023587 (Oct-1 PR) + 0.019851 (Dec-1 PR).
    k = DIDEVARASL.published("budburst.k")
    cs = tuple(
        DIDEVARASL.published(f"budburst.{n}")
        for n in ("jun_prev_tmax", "oct_prev_tmin", "oct_prev_precip", "dec_prev_precip")
    )
    assert k == 12.468353 and cs == (1.520173, 2.505555, -0.023587, 0.019851)
    xs = (np.array([28.0]), np.array([12.0]), np.array([60.0]), np.array([80.0]))
    expected = 12.468353 + 1.520173 * 28 + 2.505555 * 12 - 0.023587 * 60 + 0.019851 * 80
    assert stage_doy(k, cs, xs) == pytest.approx([expected])


def test_the_sum_refuses_mismatched_terms() -> None:
    with pytest.raises(ValueError):
        stage_doy(1.0, (1.0, 2.0), (np.zeros(2),))
    with pytest.raises(ValueError):
        stage_doy(1.0, (), ())
