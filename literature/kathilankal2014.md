---
id: kathilankal2014
citation: Kathilankal, J. C., O'Halloran, T. L., Schmidt, A., Hanson, C. V. & Law, B. E. 2014. Development of a semi-parametric PAR (Photosynthetically Active Radiation) partitioning model for the United States, version 1.0. Geoscientific Model Development 7:2477-2484
doi: 10.5194/gmd-7-2477-2014
read: 2026-10-19, only the passage restating the BRL model (Sect. 3, Eq 2), by the main session in the text layer
status: read
diseases: []
crops: []
regions: [United States]
processes: [diffuse fraction, PAR partitioning]
records: []
datasets: []
files: [gmd2014.pdf (open access, fetched 2026-10-19)]
---

# Kathilankal et al. 2014: a restatement of the BRL model's predictors

Read only for how it writes the BRL (Ridley et al. 2010), to find the units of its time and
elevation predictors for `laiti2018.brl_bolzano`.

## What it holds

- The predictors of the BRL "include daily clearness index (Kt), sine of the solar elevation angle
  (sin β), persistence index (ψ) and apparent solar time (AST)", and its Eq 2 writes kd = 1/(1 +
  exp(−5.38 + 6.63kt + 0.006 AST − 0.007 sin β + 1.75Kt + 1.31ψ)): Ridley 2010's coefficients on
  sin β. No unit for AST is given.

## Bearing (2026-10-19)

- It disagrees with other restatements (β in degrees in `malu2023`'s BRL-derived model; AST in hours
  in `pashiardis2021`). A third party's restatement settles nothing: the units stay unread until
  Ridley 2010 or Lauret 2013 is obtained.
