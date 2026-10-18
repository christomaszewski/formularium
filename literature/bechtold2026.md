---
id: bechtold2026
citation: Bechtold, M., Poschlod, B., Otto, C., Volkholz, J., Büchner, M. & Zabel, F. 2026. A global hourly ISIMIP3 climate forcing dataset for impact modeling. Earth System Science Data 18:6637-6648
doi: 10.5194/essd-18-6637-2026
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [global]
processes: [disaggregation, hourly weather, wet hours, heat index, analogue profiles]
records: []
datasets: []
files: [michel_2026.pdf (the 2026-10-18 drop)]
---

# Bechtold et al. 2026: a global hourly ISIMIP3 dataset made with Teddy

A 0.5 degree global hourly dataset made by disaggregating ISIMIP3 daily archives with Teddy and
  WFDE5 analogue profiles; its own accuracy is not tested in the paper.

## What it holds

- **Product:** ISIMIP3a and ISIMIP3b daily archives, 0.5 degree, historical 1850 to 2014 and
  scenarios to 2100 (l. 64-65, 102-104); open on the ISIMIP repository, DOIs
  10.48364/ISIMIP.736682 and 10.48364/ISIMIP.170328 (l. 42-44).
- **Method:** analogue-based hourly profiles from WFDE5, daily mass and energy preserved,
  inter-variable timing kept (l. 32-34).
- **Applications:** the fraction of wet hours, hours of dangerous heat index, onshore wind-
  power hours and photovoltaic potential, for MPI-ESM under SSP3-7.0 (l. 34-39); reduced
  spatial coherence is listed as a limit (l. 40).

## Dependence

- Builds on Teddy v1.1 (Zabel and Poschlod 2023, already a note), WFDE5, ISIMIP3a and 3b.

## Bearing (2026-10-18)

- s2: a ready global hourly product with RH-consistent temperature and wet-hour fraction, from
  climate models; a sweep needing hourly weather for a place could use it, but it keeps no
  vineyard-scale structure and no validation of wet hours is in this paper. The paper itself is
  CC BY 4.0 (l. 3-4); the data licence was not seen. Not read in full.
