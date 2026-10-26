---
id: heilman1996
citation: Heilman, J.L., McInnes, K.J., Gesch, R.W., Lascano, R.J. & Savage, M.J. 1996. Effects of trellising on the energy balance of a vineyard. Agricultural and Forest Meteorology 81:79-93
doi: 10.1016/0168-1923(95)02312-7
read: "2026-10-25, lightly: the wind passages, methods and discussion of the USDA-ARS reprint; Figs. 2-4 are scatter plots with no numbers in the text, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [United States, Texas]
processes: [canopy flow, wind, drag coefficient, turbulent intensity, trellising, hedgerow, row direction, energy balance]
records: []
datasets: []
files: [dr1025_heilman1996.pdf (the 2026-10-25 drop)]
---

# Heilman et al. 1996: in Texas hedgerows the drag coefficient did not depend on wind direction

A trellising comparison for the vineyard energy balance, with wind profiles between and above rows in two years.

**Read this first.** The wind profiles and the direction results are in figures (Figs. 3 and 4); the text states findings but prints no wind ratios. The equation for the drag coefficient (Eq. 5) and the McInnes et al. 1996 conductance passage are letter-spaced in the text layer, so the form used below is the reading agent's and that passage is not used. The result that drag does not depend on direction contradicts Hicks (1973), which the paper cites.

## What it holds

- **Site and canopy:** Chardonnay near Lamesa, Texas (33.5 N, 102 W), 6 years old in 1992; vertical bilateral cordon trellis, rows 3 m and vines 1.7 m apart, row azimuth 160 degrees from north, cordon wire at 1.0 m and catch wires at 1.25 and 1.5 m (l. 110-114). In 1992 the vines were dense hedgerows 1.6 m high and 0.4 m wide with little foliage below the cordon wire (l. 115). In 1993 they grew outward and downward to open hedgerows, plant width averaging 1.5 m (l. 117-118), and leaf area index was 55% higher (l. 668).
- **Wind measurements:** cup anemometers midway between the rows at 0.4 to 4.7 m (1992) and 0.4 to 4.2 m (1993), and above the row at 1.7 to 4.7 m (l. 205). Profiles are plotted only; no ratios are printed.
- **Turbulent intensity (1993, open hedgerows):** highest midway between rows for cross-row wind, lowest for down-row wind (l. 605); higher within the vineyard than above it (l. 606).
- **Drag coefficient:** no consistent dependence on wind direction for either dense or open hedgerows (l. 608). C_D is defined as 2 (u*/V_h)^2. Mean values at 3 m were 0.0542 (open, 1993) and 0.0516 (dense, 1992), not significantly different at the 10% level (l. 610).
- **Cited from Hicks (1973):** the drag coefficient doubled as the wind moved from parallel to perpendicular to the rows, and evapotranspiration differed by 10 to 20% between those directions (l. 68-70). Cited from Weiss and Allen (1976a): turbulent intensity was greatest when the wind was perpendicular to the rows (l. 71).

## Dependence

Contrasts its result with Hicks (1973) and Weiss and Allen (1976), both cited. It cites McInnes et al. 1996 on soil-surface conductance by wind direction (not used here). The C_D definition is the usual momentum-flux one; no model is borrowed.

## Bearing (2026-10-25)

- **dm.row_barrier (2, range 1-4):** the aerodynamic across-to-along ratio is not settled: about 2 for drag in Hicks (cited here) and for roughness in `alfieri2016ams`, about 1 in these Texas hedgerows. The assumed 2 is inside that spread, but all three are momentum measurements; none is a dispersal ratio, and none followed spores.
- **Canopy wind (SWEB Eq 15):** no usable ratio; the profiles are in figures. SWEB credits Heilman et al. 1994 (a different paper, not obtained) for its direction remark.
- Kind of result: measurement (Texas, 3 m rows, hedges 1.6 m).
