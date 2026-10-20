---
id: beasley2020
citation: "Beasley, E. M., Aristizábal, N., Bueno, E. & White, E. R. 2020. The spore of the beans: Spatially explicit models predict coffee rust spread in fragmented landscapes. bioRxiv 2020.10.16.343194 (preprint, not peer reviewed)"
doi: 10.1101/2020.10.16.343194
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [coffee leaf rust (Hemileia vastatrix)]
crops: [coffee]
regions: [simulated landscapes (no site)]
processes: [wind-borne spore dispersal, cellular automaton, random-walk spread, host clustering, deforestation, forest canopy inhibition, landscape prevalence]
records: []
datasets: []
files: [beasley_2020.pdf (the 2026-10-20 drop)]
---

# Beasley et al. 2020: coffee leaf rust spread in simulated fragmented landscapes

A simulation of coffee leaf rust in made-up landscapes, with a cellular automaton for spread
inside patches and a random walk between them. Clustering of the host is the main driver of
rust. Deforestation adds to it, most in landscapes where the host is already clustered.
Coffee, not grapevine, and no site data.

## What it holds

- Design: 3,750 simulations, one rust infection per run in a random coffee cell (l. 180).
  Factors: coffee clustering, deforestation clustering, and the share of deforested cover
  (abstract, l. 36 to 43).
- Outcome: final landscape rust prevalence from 0.1% to 55.0% (l. 260). The fitted
  distribution has an expected value of 0.075 (l. 262).
- Clustering of coffee is the main driver of rust spread and of outbreak size variance. Most
  outbreaks stay small (l. 357 to 360; abstract l. 38).
- The forest share and how it is spread matter at high coffee clustering (l. 361 to 363).
  Forest canopy inhibits spore movement in the model (abstract, l. 36).

## Dependence

- Starts from earlier field links between rust incidence and pasture cover (abstract, l. 31
  to 33), and from the wind-spore work of Avelino et al. (l. 129, 202).
  Simulation only; no shared model code or dataset from another group is recorded.

## Bearing (2026-10-20)

- Strand t6 (regional spread), by analogy. Host clustering, more than cover, sets how far a
  wind-borne disease runs. A regional spread model could weigh vineyard block clustering
  against cover.
- Off the point: coffee rust, simulated landscapes, no vine or weather data. Not read in
  full.
