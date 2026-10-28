"""Riou, Valancogne & Pieri 1989's row interception against its own identities and limits."""

from __future__ import annotations

import numpy as np
import pytest

from formularium.catalogue import FORMULATIONS
from formularium.equations import riou1989 as riou

REC = FORMULATIONS["riou1989.row_interception"]
P = REC.published("porosity")
AF, AS = REC.published("leaf_albedo"), REC.published("soil_albedo")
D, H, W = (
    REC.published(k) for k in ("test.row_spacing", "test.foliage_height", "test.foliage_width")
)


def test_the_direct_cases_meet_at_their_bounds() -> None:
    """Eqs 22-26 join at lambda H = L, D - L, D and D + L (p. 445)."""
    eps = 1e-9
    for bound in (W, D - W, D, D + W):
        lam = bound / H
        below, above = riou.direct_fraction(np.array([lam - eps, lam + eps]), D, W, H, P)
        assert below == pytest.approx(above, abs=1e-6)


def test_eq_27_steps_from_eq_26_as_printed() -> None:
    lam = (2 * D - W) / H
    below, above = riou.direct_fraction(np.array([lam - 1e-9, lam + 1e-9]), D, W, H, P)
    assert below == pytest.approx((D - P**2 * (D - 2 * W)) / D)
    assert above == pytest.approx((D - P**3 * (D - W)) / D)


def test_a_sun_overhead_lights_only_the_top() -> None:
    assert riou.direct_fraction(np.array([0.0]), D, W, H, P)[0] == pytest.approx(W / D)
    assert riou.lit_height(np.array([0.0, 10.0]), D, W, H).tolist() == pytest.approx(
        [H, (D - W) / 10.0]
    )


def test_the_lower_face_takes_l_over_d_when_open() -> None:
    """Eq 17 normalised: no walls and no neighbour leave the face the whole sky."""
    # tall, narrow walls (h1 -> pi/2) and a far neighbour (h2 -> 0)
    assert riou.lower_face_diffuse(1e9, 1e-6, 1.0) == pytest.approx(1e-6 / 1e9, rel=1e-6)
    h = np.linspace(0.0, np.pi / 2, 4001)  # the closed form against the double integral
    a = np.linspace(0.0, np.pi, 4001)
    aa, hh = np.meshgrid(a, h)
    h1 = np.arctan(2 * H / W * np.sin(aa))
    h2 = np.arctan(H / (D - W / 2) * np.sin(aa))
    inside = (hh >= h2) & (hh <= h1)
    integral = np.trapezoid(np.trapezoid(np.cos(hh) * np.sin(hh) * inside, h, axis=0), a)
    assert riou.lower_face_diffuse(D, W, H) == pytest.approx(
        W / (np.pi * D) * 2 * integral, rel=2e-3
    )


def test_the_paper_canopy_diffuse_shares() -> None:
    """D 1.8, H 0.9, L 0.3 m, p 1/3 (p. 445): our arithmetic, not printed."""
    assert riou.upper_walls_diffuse(D, W, H) == pytest.approx(0.3615, abs=1e-4)
    assert riou.lower_face_diffuse(D, W, H) == pytest.approx(0.1189, abs=1e-4)
    assert riou.diffuse_fraction(D, W, H, P) == pytest.approx(0.4473, abs=1e-4)


def test_absorbed_and_reflected_match_their_unexpanded_forms() -> None:
    """p. 445 prints both Eq 28 and Eq 29 first as sums of the leaf and soil paths."""
    ri, rg = np.array([150.0, 300.0]), np.array([400.0, 700.0])
    nd = riou.diffuse_fraction(D, W, H, P)
    ra = (1 - AF) * ri + AS * nd * (1 - AF) * (rg - ri)
    rr = AF * ri + (1 - nd) * AS * (rg - ri) + 0.5 * nd * AS * (rg - ri) * AF
    assert riou.absorbed(ri, rg, nd, AF, AS) == pytest.approx(ra)
    assert riou.reflected(ri, rg, nd, AF, AS) == pytest.approx(rr)


def test_the_beam_ratio_of_north_south_rows_is_eq_6() -> None:
    """Eq 6 for north-south rows (a' = pi/2), since sin a cos h = cos(delta) sin t."""
    h, a = np.radians(40.0), np.radians(30.0)
    assert riou.beam_ratio(h, a, np.pi / 2) == pytest.approx(abs(np.cos(h) * np.sin(a) / np.sin(h)))


def test_wide_rows_are_refused() -> None:
    with pytest.raises(ValueError):
        riou.direct_fraction(np.array([1.0]), 1.0, 0.6, 1.0, P)
