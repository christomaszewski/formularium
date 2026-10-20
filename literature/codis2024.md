---
id: codis2024
citation: "Codis, S., Cheraiet, A., Delpuech, X., Carra, M., Ribeyrolles, X., Trinquier, E., Vergès, A. & Naud, O. 2024. TechnodoseViti: Experimental modelling for the prediction of phytosanitary product deposits within the plant canopy in viticulture. Application to dose expression and precision viticulture. Innovations Agronomiques 88: 29-43"
doi: 10.17180/ciag-2024-vol88-art03-GB
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: [grapevine]
regions: [Languedoc, France]
processes: [spray deposition, LiDAR canopy descriptors, height, thickness, porosity, deposit deciles, multivariate models, dose expression, technological scenarios, precision spraying]
records: []
datasets: []
files: [codis_2024.pdf (the 2026-10-20 drop)]
---

# Codis et al. 2024: LiDAR canopy descriptors predict spray deposit in vines

A multivariate model of spray deposit, by decile across the canopy, from LiDAR height,
thickness and porosity, built on wide-row vines in 2016 and 2017. It also sets doses as a
share of the full dose by canopy size, and scores four sprayer and dose-decision scenarios
for savings. Plant protection products in general: no disease is named.

## What it holds

- Models: nine deciles of leaf deposit, each a multivariate function of canopy height,
  thickness and porosity (l. 262 to 267). Built on 2017 data and checked on 2016 data,
  wide rows (l. 262 to 264). Narrow-row data lack one or two seasons (l. 286 to 288).
- Dose: with the pneumatic arch sprayer used every four rows, the full approved dose is
  needed once vegetation reaches 80 cm; above 90 cm the recommended dose no longer gives the
  reference deposit (l. 477 to 480). A multi-row sprayer gives "considerable" savings.
- Scenarios (higher risk): scenario 1 to 2 saves over 40% of product; 2 to 3 saves 4.6%;
  3 to 4 saves almost 10% (l. 619 to 627). Scenario 2 moves dose decisions to the estate,
  3 to plot level.
- Web simulator: developed in the project (abstract).

## Dependence

- Builds on the LiDAR vegetation indicators of Cheraiet et al. (2019, 2020, 2021) and on the
  univariate models of Pergher et al. (2008), Llorens et al. (2011) and Codis et al. (2019)
  that it improves on (l. 273 to 275). No dataset from another group is recorded.

## Bearing (2026-10-20)

- Strand t1 (fungicide protection). This is the most direct source here for a vineyard
  simulator's dose term: a dose set as a share of the full dose by canopy height,
  thickness and porosity, with deposit deciles for the spread of coverage.
- Savings are for a set risk level, not a disease result, and no disease is measured. The
  narrow-row model is not yet tested. Not read in full.
