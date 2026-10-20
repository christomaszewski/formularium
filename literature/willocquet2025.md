---
id: willocquet2025
citation: "Willocquet, L., Bregaglio, S., Ferrise, R., Kim, K. H. & Savary, S. 2025. DYNAMO-A: a generic simulation model coupling crop growth and disease epidemic. PLoS ONE 20:e0321261"
doi: 10.1371/journal.pone.0321261
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: [annual crop, rice, wheat]
regions: [general]
processes: [crop growth, polycyclic epidemic in the canopy, disease-induced senescence, yield loss, biotroph and necrotroph scenarios]
records: []
datasets: []
files: [willocquet_2025.pdf (the 2026-10-20 drop)]
---

# Willocquet et al. 2025: DYNAMO-A, crop growth coupled to an epidemic

A generic simulation model that couples a daily crop-growth model with a polycyclic canopy epidemic for an annual crop. Its equations and parameters are printed, but only hypothetical scenarios are run.

## What it holds

- Equations (1) to (13) cover growth, leaf area, the epidemic and disease-induced senescence. Growth with disease is at (13) (l. 227, 430-433).
- Parameters in Table 2 (l. 516-518), taken from rice and wheat models (l. 559-563).
- Scenarios: a biotrophic and a necrotrophic ideotype, in two production situations (l. 37-41; Table 2 scenario parameters, l. 583).
- No field validation appears in the text read. Results are scenario runs only.

## Dependence

- Builds on the RICEPEST and WHEATPEST crop-loss platforms, and on the GENEPEST generic model (l. 152).
- Rice and wheat disease parameters from earlier studies (l. 559-563).

## Bearing (2026-10-20)

- Strand t5 (damage and economics). The link from disease to green leaf area and assimilate diversion to yield is a loss term a vineyard simulator could copy.
- The parameters are for rice and wheat, so a vine model would need its own parameters and calibration. Not read in full.
