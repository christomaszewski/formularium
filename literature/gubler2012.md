---
id: gubler2012
citation: Gubler, S., Gruber, S. & Purves, R.S. 2012. Uncertainties of parameterized surface downward clear-sky shortwave and all-sky longwave radiation. Atmospheric Chemistry and Physics 12:5077-5098
doi: 10.5194/acp-12-5077-2012
read: 2026-10-27, abstract only (and the introduction); the formulas and coefficients were not read; by a reading agent (model not recorded in its JSON) and a note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Switzerland, Alps]
processes: [longwave radiation, cloud transmissivity, clear-sky shortwave, radiation uncertainty]
records: []
datasets: []
files: [dr1027_gubler2012.pdf (the 2026-10-27 inputs-d60 drop)]
---

# Gubler et al. 2012: uncertainty of clear-sky shortwave and all-sky downward longwave parameterisations at six Swiss stations

Abstract only. Twelve clear-sky longwave formulas calibrated on station measurements; all-sky longwave by one of them with a cloud term.

## What it holds

- **Validation data:** six Alpine Surface Radiation Budget stations in Switzerland, hourly, 1996-2008 (l. 26), plus Payerne.
- **Method:** one of twelve calibrated clear-sky longwave parameterisations is used for all-sky, with cloud transmissivity from measured and modelled global shortwave by day (l. 29).
- **Night cloud:** the best night estimate interpolates linearly between the mean cloud transmissivity of the four afternoon hours before and the four morning hours after (l. 48).
- **Error (from the LEADS summary of the abstract, not in the facts):** calibrated LDR relative MBD below 5 %, RMSD below 10 %.
- Equations and coefficients: not read.

## Dependence

- None recorded from the abstract. Independent of the engine's wetness pieces.

## Bearing (2026-10-27)

- **What it supports:** a way to carry daytime cloud into the night (the case for dewfall and nocturnal wetness) from station global radiation; Alpine sites, so a lead rather than a calibrated input for vineyards.
- **Not shown:** any coefficient, any vineyard. Read the full text before use. Kind of result: a multi-station parameterisation comparison.
