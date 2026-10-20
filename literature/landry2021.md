---
id: landry2021
citation: Landry, C., Abadie, C., Bonnot, F. & Vaillant, J. 2021. A spatio-temporal stochastic model for an emerging plant disease spread in a heterogeneous landscape. International Journal of Computer Applications 174(16)
doi:
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [black leaf streak (Pseudocercospora fijiensis)]
crops: [banana]
regions: [Martinique, French West Indies]
processes: [spatio-temporal spread, power-law dispersal kernel, landscape receptivity, rainfall effect, data-augmented MCMC]
records: []
datasets: []
files: [landry_2021.pdf (the 2026-10-20 drop)]
---

# Landry et al. 2021: spatio-temporal model of black leaf streak in Martinique

A stochastic colonization model fitted by data-augmented MCMC to black leaf streak presence-absence on a 1 km grid. It has a power-law dispersal kernel and a rainfall term.

## What it holds

- **Survey:** a 1 km grid over Martinique (about 1,228 km2). Survey weeks ran from September 2010 to May 2012, 83 weeks in all (l. 258-259, 272-273).
- **Dispersal and rainfall:** power-law decay beta 1.991 (SE 0.655) (l. 353). Rainfall effect gamma -2.124 (SE 1.454) (l. 354).
- **Landscape:** receptivities r1 to r5 with posterior means and SEs (Table 2, l. 349-355). For r1, 5.58e-03 (SE 2.98e-03) (l. 355).
- **Reenactment:** the model reconstructs the invasion (section 3.3, l. 350-356).
- **Data:** the text read has no data-availability statement and no repository.

## Dependence

- Power-law kernel with data-augmented MCMC, from earlier spread and inference work (l. 36-40).
- The authors' own black leaf streak survey in Martinique.

## Bearing (2026-10-20)

- Strand t6 (regional spread). The kernel form and the rainfall term could be refit to vineyard presence data. A simulator could take the form, but not these banana values.
- Not read in full.
