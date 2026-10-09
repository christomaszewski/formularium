---
id: anderson2001
citation: Anderson, M. C., Bland, W. L., Norman, J. M. & Diak, G. D. 2001. Canopy Wetness and Humidity Prediction Using Satellite and Synoptic-Scale Meteorological Observations. Plant Disease (Special Report) 85(9):1018-1026
doi: 10.1094/PDIS.2001.85.9.1018
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 28 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [potato late blight]
crops: [potato]
regions: [Wisconsin]
processes: [leaf wetness, dew, canopy humidity]
records: []
datasets: []
files: [10-1094-pdis-2001-85-9-1018.pdf, PDIS.2001.85.9.1018 (1).pdf]
---

# Anderson, Bland, Norman & Diak 2001: canopy wetness and humidity from satellite and synoptic data (ALEX)

From the University of Wisconsin. Two copies were dropped, byte-identical.

## What it holds

- Physical model ALEX, a simplified form of Norman's Cupid (l. 56); equations are in ref 2, not printed here.
- Dew forms when canopy-air vapour pressure exceeds saturation at leaf temperature (l. 117).
- Water film capped at 0.15 mm per unit leaf area, after Wilson et al.'s potato data (l. 99). Evaporation follows modeled net radiation divergence (l. 105).
- Roughness fraction was adjusted to agree over the six site-years of observations (l. 257).
- Inputs: ASOS/AWOS data interpolated on a 0.4 deg grid (l. 84), GOES radiation, in-field precipitation only.
- Dew check uses Wilson et al.'s four potato nights; peak dew low by 0.05 to 0.1 mm (l. 271).
- High-RH events at Hancock and Plover 1998-2000: duration right for 74% of 450 site-days, within 2 h for 89% (l. 322).
- No field data collected by the authors (l. 426). Gleason 1994 and Pedro and Gillespie 1982 are cited as other models (l. 110).

## Dependence

- ALEX is an energy-balance model from Norman's Cupid lineage; no equation is printed, only its rules (dew when in-canopy vapour pressure exceeds saturation at leaf temperature; a water film capped at 0.15 mm per unit leaf area).
- **A tuned constant:** surface roughness was "adjusted to give optimal agreement over the six site-years of observations", the same Hancock and Plover humidity data then used to test it (l. 257-258). Its field data came from Wilson et al., Stevenson and James.
- No author of an engine model; Gleason and Pedro & Gillespie are cited as other models.

## Bearing (2026-10-08)

- **Clear of the engine:** the physical wetness option unrelated to it, sun-driven drying included. Its full equations are in Anderson et al. 2000, not held; its test is not independent of its tuning.
