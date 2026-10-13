"""Didevarasl et al. 2026's Cannonau regressions: the same sum as Fraga's.

Table 4 prints budburst, bloom and veraison as linear functions of monthly temperature
means and precipitation totals (literature/didevarasl2026). The catalogue holds the
coefficients under `didevarasl2026.monthly_regression`; the arithmetic is
`monthly_regression.stage_doy`, re-exported here so the record names its own module.
"""

from __future__ import annotations

from formularium.equations.monthly_regression import stage_doy

FORMULATION = "didevarasl2026.monthly_regression"

__all__ = ["FORMULATION", "stage_doy"]
