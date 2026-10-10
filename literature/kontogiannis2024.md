---
id: kontogiannis2024
citation: Kontogiannis, Sotirios, Koundouras, Stefanos & Pikridas, Christos. 2024. Proposed fuzzy-stranded-neural network model that utilizes IoT plant-level sensory monitoring and deep learning inference engine for downy mildew. Computers 13:63
doi: 10.3390/computers13030063
read: 2026-10-10, the model review and results (LIGHT), equations 1-4 in the page image, by a reading agent (claude-haiku-5-5); 29 quotes checked by scripts/verify_quotes.py; equations 1-4 checked in the page image (p. 3) by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Greece]
processes: [forecasting]
records: [epi1983.corrected, goidanich.incubation, rule_3_10, rossi2008pp.dormancy]
datasets: []
files: [p11.pdf]
---

# Kontogiannis et al. 2024: a fuzzy neural network, with a review of downy mildew models

## What it holds

- **Its review prints, among others:**
  - EPI (eqs 1-3, cited to Stryzik): Ep = 2·[k(√Ri - √(0.95 Rm))] + 0.2·[√(Ri·Ti) -
    √(0.95 Rm Tm)] - [(1.5 RDm/18) log10(Rd/RDd)], k 1.2, 1, 0.8 by month; Ec = 0.012 ·
    [¼(5 RHnight + 3 RH10-18h)² √Ti - RH²10-18h √Tm]/100; first infection when EPI > -10.
    This differs from Ronzon 1987's printing (see the flag on `epi1983.corrected`).
  - DMCast's oospore maturity (eq. 4): a normal density with μ = 118 - 0.3 Ra and σ = 13.5
    + 0.02 Ra.
  - Rossi et al. 2008's hydro-thermal time table, with M = 1 when VPD ≤ 4.5 hPa, and the
    UR model's rules.
- **Its own model:** trained on fuzzy labels built from Bove et al.'s simulated table, so
  model output; about 90 % agreement with those labels.
- Its 2023 "validation" compares with the Goidanich index (GI ≥ 100 after 10 mm in 72 h
  from 1 May), computed by the authors.

## Dependence

- Computes Goidanich's index and the 3-10 rule; learns labels from a simulation.

## Bearing (2026-10-10)

- None as a model. A second printing of EPI and DMCast's maturity curve, both of which
  differ from their sources' (EPI) or are unread at source (DMCast).
