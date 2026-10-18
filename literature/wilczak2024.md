---
id: wilczak2024
citation: Wilczak, J. M., Akish, E., Capotondi, A. & Compo, G. P. 2024. Evaluation and Bias Correction of the ERA5 Reanalysis over the United States for Wind and Solar Energy Applications. Energies 17:1667
doi: 10.3390/en17071667
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full
status: read
diseases: []
crops: []
regions: [contiguous United States]
processes: [reanalysis bias, quantile mapping, wind speed correction, solar irradiance]
records: []
datasets: []
files: [james_2024.pdf (the 2026-10-18 drop)]
---

# Wilczak et al. 2024: ERA5 bias correction for wind and solar over the US

ERA5 irradiance and wind are compared with observation networks and corrected by quantile
  mapping (solar) and linear regression (wind).

## What it holds

- **Bias:** ERA5-derived solar power is high by 23 % on average in winter; wind power is low by
  20 % on an annual basis (l. 19-21).
- **Extremes:** at 10 days duration, the largest negative solar anomaly events are 62 % greater
  in ERA5 than observed (l. 26-27).
- **Correction:** quantile-quantile mapping for solar and linear regression of wind speed,
  designed to avoid inflating variability (l. 31-34); observations 1998 to 2020 (l. 180).

## Dependence

- ERA5, quantile mapping and linear regression, as the record states.

## Bearing (2026-10-18)

- s2: shows that ERA5 smooths variability and that a quantile map, not a mean shift, is the
  repair for a bounded variable such as irradiance. A sweep generator could take the quantile-
  map method for radiation and wind. Not read in full.
