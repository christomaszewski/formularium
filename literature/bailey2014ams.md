---
id: bailey2014ams
citation: "Bailey, B.N., Stoll, R., Mahaffee, W. & Pardyjak, E. 2014. The impact of canopy geometry on particle dispersion gradients in sparse agricultural canopies. AMS extended abstract, paper 173013 (symposium as given in the reading JSON: 21st Symposium on Boundary Layers and Turbulence, Leeds, 9-13 June 2014; not printed on the PDF)"
doi:
read: 2026-10-25, in full (a 4-page extended abstract), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 4 of 4 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [none (large-eddy simulation)]
processes: [dispersal, dispersal gradient, canopy deposition, canopy flow, wind, row spacing, leaf area index, large-eddy simulation, Lagrangian particle model]
records: []
datasets: []
files: [dr1025_bailey2014ams.pdf (the 2026-10-25 drop)]
---

# Bailey et al. 2014: in simulated vineyard rows, denser or closer rows cut the spores that reach a point downwind

A large-eddy simulation of airflow through resolved vine rows, with spores as passive particles; powdery mildew (Erysiphe necator) is the example.

**Read this first.** Model output, not measurement, from a 4-page extended abstract. The flow appears to run across the rows (particles approach each row and are deflected over it or into the trunk space; l. 217), but the text does not say so outright, and there is no along-row case. The long-range result is "not shown" (l. 243), and the downwind concentrations are in a figure that was not read.

## What it holds

- **Method:** large-eddy simulation with the canopy as a drag force (Eq. 1, F_i = c_d a u_i V) and the rows resolved. Spores are passive parcels moved by the resolved velocity plus a Gaussian sub-filter velocity (Eq. 2), with a constant settling drift velocity and no size distribution (l. 171-173).
- **Cases:** ten simulations, row spacing 1, 1.5, 2, 2.5 and 3 m, each at row leaf area index (LAI) 1 and 3 (l. 190, 194); a domain of about 18 x 18 x 6 m (l. 190); the volume-mean streamwise velocity held at 2 m/s (l. 198). The LAI range is cited from Johnson et al. 2003 as typical of vineyards (l. 198).
- **Result 1:** at a downstream point 8 m from the source, spore concentration falls as LAI rises and as row spacing falls (l. 229). The text says "tends to" and gives no numbers; they are in Figure 2.
- **Result 2:** increasing LAI or decreasing row spacing tended to reduce the probability of long-range particle transport (l. 245). The results are "not shown" (l. 243).
- A large share of particles that enter a row's foliage are deposited, leaving a low-concentration wake (l. 217-219).

## Dependence

LES with a scale-dependent dynamic Smagorinsky model (Stoll et al. 2006) and a stochastic Lagrangian particle model (Uliasz 1994), both cited. Authors are shared with `bailey2013`, `torkelson2022` and `miller2017` (a flag).

## Bearing (2026-10-25)

- **dm.row_barrier (2, range 1-4):** the only simulation in this strand with spores. It shows that rows act as a barrier to cross-row spore transport, stronger with denser or closer rows. It has no along-row case, so it gives no along-to-across dispersal ratio and no support for the value 2 or the range 1-4. Aerodynamic ratios are not dispersal ratios, and neither is a model with a constant settling velocity.
- Powdery mildew conidia are the example, not downy mildew sporangia.
- Kind of result: model (large-eddy simulation) in an extended abstract.
