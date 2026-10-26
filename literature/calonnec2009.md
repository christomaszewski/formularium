---
id: calonnec2009
citation: Calonnec, A., Cartolaro, P. & Chadoeuf, J. 2009. Highlighting features of spatiotemporal spread of powdery mildew epidemics in the vineyard using statistical modeling on field experimental data. Phytopathology 99:411-422
doi: 10.1094/PHYTO-99-4-0411
read: 2026-10-25, in full (two columns interleaved, so each quote is one line of one column; the distance equation, Table 3 and Fig. 6 also checked in the page images of PDF pp. 3, 6, 7 and 8), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [France, Bordeaux]
processes: [dispersal gradient, focus expansion, spread velocity, anisotropy, row direction, prevailing wind, vine vigour, logistic model, primary foci]
records: []
datasets: []
files: [dr1025_calonnec2009.pdf (the 2026-10-25 drop)]
---

# Calonnec et al. 2009: spatiotemporal spread of grape powdery mildew from single and natural foci in Bordeaux, with an along-row against across-row term

A logistic model of the probability that a leaf becomes infected at distance d from a focus and time t, fitted by maximum likelihood to counts from three inoculated plots and one naturally infected plot; the fits give a gradient slope b, a front velocity c and, for the natural plot, a row anisotropy a.

**Read this first.** Two cautions. First, this is an analogue: grape powdery mildew (Erysiphe necator), not downy mildew, with dry-air conidia and a different weather response. Second, the paper contradicts itself on which way the row anisotropy points, and this note does not resolve it.
- The distance equation (page image checked) is D = sqrt(dx^2 + a dy^2), with dx the distance within the row and dy across rows (l. 178). The text layer prints it garbled as "(dx + a dy)^2" with displaced superscripts.
- Table 4 gives a = 5.14 for all four foci of the natural plot (l. 580-582). With a above 1, a metre across rows counts as sqrt(5.14) = 2.27 m along the row (arithmetic, not printed), which makes across-row spread slower.
- The text says the opposite: "The disease spread faster along the between-rows direction, as indicated by the a value" (l. 411-412). The abstract and the discussion say the velocity of spread decreased along the row (l. 30-31, 556-557, 592).
- The single-focus fits agree with the text, not with the equation: pooled over plots, the row directions N and S (Fig. 6 marks the rows as running N-S) have the slowest velocity, 0.13 m per day, and steep gradients, 0.90 and 0.81 per m (Table 3, l. 443, 447), against 0.20 to 0.36 m per day for the other six directions (l. 444-446, 448-450).
- Either dx and dy are swapped in the printed equation, or dy was counted in row units, or a is applied the other way. The paper does not say. Do not use a = 5.14 as a row barrier until the authors are asked or plot P4 is refitted (the field data are not published with the paper).

## What it holds

- **Plots:** three artificially inoculated single-vine foci, P1 to P3, 49 vines each, Cabernet-Sauvignon, vines 1 m apart and rows 1.5 m apart, Martillac, Bordeaux, 1998 (l. 104-109). A naturally infected plot P4 of 330 vines at Couhins, 1999, rows 2 m apart and vines 1 m apart, with four primary foci F1 to F4 (l. 137-141, 145).
- **Model:** the probability that a leaf at distance d is infected between dates t(k-1) and t(k) is a difference of two logistics, p = 1/(1 + exp(K) exp(bd - bct)), with K related to the primary inoculum, b the rate at which severity falls with distance and c the velocity (page image of PDF p. 3; the parameters' meaning is in the Table 3 footnote, l. 483). It is a gradient of a logistic front, not a dispersal kernel.
- **Gradient:** b ran from 0.12 per m (P2, direction 7, west) to 1.99 per m (P1, direction 1, north) (l. 375-376; l. 454, 469), i.e. 1/b of 0.5 to 8 m (arithmetic, not printed). Whole experiment: K 6.08, b 0.44 per m, c 0.25 m per day, 4.0 days per metre (l. 434).
- **Velocity:** c was 0.1 to 0.27 m per day in areas of moderate vigour and up to 1.1 m per day in areas of high vigour (l. 19-20), as low as 0.04 where vigour was low (P1, direction 1; l. 351, 454). Vigour and the prevailing wind lowered b; row direction raised it (l. 344-348, 553).
- **Wind:** in the most homogeneous plot, P3, spread was 0.26 m per day for directions 2 to 3 (NE, E) against 0.15 for directions 6 to 7 (SW, W) (l. 355-356); the authors read this as about twice as fast with the prevailing wind. Along the rows the mean velocity stayed at 0.15 m per day (l. 359-360).
- **Directions in P3 (Table 3):** N b 0.86 and c 0.17 (l. 472); S, along the row, b 1.32 (the steepest) and c 0.10, 10.1 days per metre (l. 476); E b 0.46 and c 0.27 (l. 474); W b 0.78 and c 0.15 (l. 478).
- **Natural plot (Table 4):** F2 K 2.83, b 1.64 per m, c 0.06 m per day; F3 b 0.09 per m, c 1.77; F4 b 0.07 per m, c 1.8; all with a = 5.14 (l. 580-582). The model gives a probability of infection almost zero 6 m from the centre of F2 (l. 598).
- **Cited, not measured:** focus velocities of 0.09 to 0.9 m per day for wheat or oat crown rust (l. 537, the paper's refs 49 and 3).

## Dependence

- A logistic spatiotemporal model after Jeger (ref 29) and Van der Plank (ref 50), fitted by maximum likelihood to binomial counts. No dispersal kernel is fitted. The first two authors also wrote the held notes `calonnec2004` and `calonnec2008`: a shared author, a flag only. Field data are not published with the paper.

## Bearing (2026-10-25)

- **dm.row_barrier 2 [1-4]** (a metre across rows counts as this many along): the only fitted along-row against across-row term for a grape foliar fungus in vines, and it points both ways. Read as printed, a = 5.14 gives 2.27, inside the range and near the current 2. Read as the text, spread across the rows is faster than along them (Table 3, pooled over plots: E and W velocities 0.23 and 0.35 against 0.13 for N and S, l. 443, 445, 447, 449, so 1.8 to 2.7 times faster across; arithmetic, not printed), a factor below 1 in this parameter's terms. Vigour and wind are confounded with direction. Unresolved; powdery mildew, Bordeaux, a model fitted to field counts. It does not support a value.
- **dm.wind_scale_m 3 m [2-10] and dm.kernel_radius_m 40 m [20-80]:** the gradients (1/b of 0.5 to 8 m; infection nearly zero by 6 m from one natural focus) are the same order as the registered wind scale and well inside the kernel radius. They are logistic-front slopes for powdery mildew conidia, not kernels, and say nothing of the tail.
- **dm.wind_stretch_per_ms 0.3:** the paper has a prevailing-wind effect (0.26 against 0.15 m per day in one plot), by direction and not per m/s; no wind speed is among the facts read. It is an analogue and does not set the value.
