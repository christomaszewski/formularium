"""Lalancette, Ellis & Madden 1988's equation 5 against what the paper prints."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import lalancette1988 as la

REC = FORMULATIONS["lalancette1988.infection"]
K = tuple(REC.published(f"k.{n}") for n in ("b0", "b1", "b2", "offset"))
RHO = tuple(REC.published(f"rho.{n}") for n in ("b1", "b2", "b3"))
M = REC.published("m")


def _ie(t, wet):
    return la.infection_efficiency(t, wet, *K, *RHO, M)


def test_the_curve_starts_at_a_32nd_of_k_and_rises_to_k() -> None:
    # At 1 h of wetness W = 0, so IE = k 2^-5 (m = 1.2); long wetness tends to k (own calculation).
    t = np.array([10.0, 15.0, 20.0, 25.0])
    k = la.asymptote(t, *K)
    assert _ie(t, 1.0) == pytest.approx(k / 32)
    assert _ie(t, 200.0) == pytest.approx(k, rel=1e-6)
    assert np.all(np.diff(_ie(20.0, np.arange(1.0, 16.0))) > 0)  # e^(-rho): it rises


def test_the_rate_against_the_printed_maximum_and_zeros() -> None:
    # p. 796: r peaks at 0.36 at 16.9 °C and is 0 at 3.8 and 30 °C. The printed, rounded
    # coefficients give 0.343 at 16.7 °C and zeros at 3.9 and 29.5 °C.
    t = np.linspace(0, 35, 35001)
    r = la.rate(t, *RHO)
    assert r.max() == pytest.approx(0.36, abs=0.02)
    assert t[r.argmax()] == pytest.approx(16.9, abs=0.3)
    zeros = t[np.where(np.diff(np.sign(r)))[0]]
    assert zeros == pytest.approx([3.8, 30.0], abs=0.6)


def test_the_asymptote_against_the_printed_maximum_and_zeros() -> None:
    # p. 795-796: k (without the 0.01 offset) peaks at 0.083 at 17.5 °C, 0 at 4.6 and 30.4 °C.
    # Table 1 prints the coefficients to two figures; they give 0.091 at 18.0 °C and zeros
    # at 4.5 and 31.5 °C, so the tolerances are the rounding's.
    t = np.linspace(0, 35, 35001)
    k = la.asymptote(t, *K[:3], 0.0)
    assert k.max() == pytest.approx(0.083, abs=0.01)
    assert t[k.argmax()] == pytest.approx(17.5, abs=0.6)
    zeros = t[np.where(np.diff(np.sign(k)))[0]]
    assert zeros == pytest.approx([4.6, 30.4], abs=1.2)
