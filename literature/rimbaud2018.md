---
id: rimbaud2018
citation: Rimbaud, L., Papaïx, J., Rey, J.-F., Barrett, L.G. & Thrall, P.H. 2018. Assessing the durability and efficiency of landscape-based strategies to deploy plant resistance to pathogens. PLoS Computational Biology 14(4):e1006067
doi: 10.1371/journal.pcbi.1006067
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [cereal rusts (simulated)]
crops: [cereals (simulated)]
regions: [none (simulation)]
processes: [resistance deployment, pyramiding, cultivar mixtures, mosaics, landscape spread, pathogen evolution]
records: []
datasets: []
files: [rimbaud_2018.pdf (the 2026-10-20 drop)]
---

# Rimbaud et al. 2018: landsepi, a model for landscape resistance deployment

A spatial stochastic model, the R package landsepi, for landscape-scale resistance deployment against rusts. It scores epidemiological and evolutionary outcomes together.

## What it holds

- **Strategies:** rotations, cultivar mixtures, mosaics and pyramiding. Quantitative traits act on infection rate, latent period, propagule production and infectious period (abstract, l. 23-38).
- **Rust parameters** (Table 1, l. 318-339): 120 days per year (l. 324). Maximal expected infection rate 0.40 per spore (l. 335). Minimum latent period 10 days (l. 336). Maximal infectious period 24 days (l. 338).
- **Scope:** simulation only, with no field validation. The full comparison of the four strategies is left to later work (l. 47-50).
- **Data:** within the paper and its Supporting Information, and the code is in landsepi v0.0.2 on CRAN (l. 46-52).

## Dependence

- The authors' own landsepi model, in the R package (l. 39-40, 50-52).
- Rust life-history parameters set in S1 Text (l. 287-288).

## Bearing (2026-10-20)

- Strand t6 (regional spread), for resistance deployed across a landscape. It is not a grape paper. A growers' engine could take the idea that mixtures and mosaics trade efficiency against durability, but no number transfers.
- Not read in full.
