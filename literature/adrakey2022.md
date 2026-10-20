---
id: adrakey2022
citation: Adrakey, H.K., Gibson, G.J., Eveillard, S., Malembic-Maher, S. & Fabre, F. 2022. Bayesian inference for spatio-temporal stochastic transmission of plant disease in the presence of roguing: a case study to estimate the dispersal distance of Flavescence dorée. bioRxiv (preprint) doi 10.1101/2022.12.14.520426
doi: 10.1101/2022.12.14.520426
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [Flavescence dorée]
crops: [grapevine]
regions: [Bordeaux, France]
processes: [dispersal kernel, roguing, data augmentation MCMC, spatio-temporal transmission]
records: []
datasets: []
files: [adrakey_2022.pdf (the 2026-10-20 drop), adrakey_2023.pdf (the published version, the 2026-10-20 drop)]
---

# Adrakey et al. 2022: Flavescence dorée dispersal with roguing (preprint)

A Bayesian spread model, fitted to two snapshot maps of three Bordeaux fields, gives a dispersal scale of 22.9 m for Flavescence dorée. Roguing is built into the model.

## What it holds

- Scale parameter 22.9 m, 95% credible interval 20.1 to 26.5 m, for Model 18, a power-law kernel with b = 6 (l. 653, 714-719; Table 3).
- Half of new infections fall within 10.5 m of a source, and 80% within 22.2 m (l. 38). Heavy-tailed kernels fit best (l. 36-38).
- FD was first detected in the area in 2014, in the GDON surveillance (l. 364). The two snapshots of field status are from October (l. 324). Field F1 was removed in winter 2018 (l. 330).

## Dependence

- Builds on data augmentation and MCMC for plant epidemics, on the GDON regional surveillance records, and on S. titanus mark-capture flight estimates, cited for comparison.

## Bearing (2026-10-20)

- Strand t6 (regional spread), and t7 for the vector context. A simulator could take the dispersal scale and kernel shape for Flavescence dorée with roguing. It comes from one vector-borne site and a preprint that has not been peer reviewed.
- Not read in full.
- The published version is Adrakey et al. 2023, PLOS Computational Biology, doi
  10.1371/journal.pcbi.1011399 (a copy in the 2026-10-20 drop): same data and results
  (half of new infections within 10.5 m, 80 % within 22.2 m), checked by a note writer.

