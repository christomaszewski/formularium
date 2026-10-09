---
id: broome1995
citation: Broome, J. C., English, J. T., Marois, J. J., Latorre, B. A. & Aviles, J. C. 1995. Development of an infection model for Botrytis bunch rot of grapes based on wetness duration and temperature. Phytopathology 85(1):97-102
doi: 10.1094/Phyto-85-97
read: 2026-10-08, in full (OCR text) by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, the model and dependence by the main session. Earlier read on 2026-10-07 (Agrarium's read-botrytis-powdery.md)
status: read
diseases: [Botrytis bunch rot]
crops: [grapevine]
regions: [California, Chile]
processes: [infection]
records: [broome1995.botrytis]
datasets: []
files: [10-1094-phyto-85-97.pdf]
---

# Broome et al. 1995: Botrytis infection by wetness and temperature

From UC Davis, the University of Missouri and the Pontificia Universidad Católica de Chile.
The source of the engine's `broome1995.botrytis`. The DOI is not printed in the text copy;
the one above is the file's name.

## What it holds

- **Data:** detached mature Red Seedless berries, two California isolates, wet for 4, 8,
  12, 16 or 20 h at 12, 16, 20, 24, 28 or 30 °C (l. 15-16, 70, 91); 30 berries per
  temperature and step, the experiment done three times (l. 91, 100). Berries were dried,
  held 6 days at 22 °C and scored for mycelium and conidia (l. 95, 98).
- Infection followed 4 h of wetness at every temperature, from about 9% at 12 °C to 37% at
  20 °C (l. 16, 308).
- **Model:** ln(Y/(1-Y)) = b0 + b1·W + b2·W·T + b3·W·T², W in hours and T in °C
  (l. 314-316). Combined fit, on the means of the three experiments (l. 242):
  b0 = -2.647866 (l. 214), b1 = -0.374927 (l. 216), b3 = -0.001511 (l. 220); **b2 is garbled**
  in the text copy ("06160ł", l. 218), so the earlier reading's 0.061601 is not confirmed.
  R² 0.78 (l. 381). The three experiments' b1 differ widely: -0.498932, -0.124354,
  -0.121506 (l. 188, 197, 206).
- **Field rules:** hourly logit ≤ 0 none, 0.01-0.5 low, 0.5-1.0 moderate, ≥ 1.0 high;
  spray at moderate or high (l. 157-159); a dry spell over 4 h stops the count (l. 161).
  No source or fit is given for these.
- **Validation** in central Chile (33-35° S), Thompson Seedless, 1991-1993: model-timed
  sprays 3.5 against 7.0 per vineyard in 1991-92 (l. 410), 3.0 against 4.7 in 1992-93
  (l. 426-427). The text shows no refit after the trials.

## Dependence

- Fitted to its own berry data, by Bulger et al. 1987's method (l. 139-140); no model dated
  the infections. It computes no earlier model.
- **Authors as read:** J. C. Broome, J. T. English, J. J. Marois, B. A. Latorre, J. C.
  Aviles. Cooptera's list records initials J., J., J., B. A., J. (trail); told to Cooptera.

## Bearing (2026-10-08)

- The engine's Botrytis model is now held and read. Its b2 must come from a clean copy
  (the page image), not the text copy. The low band prints 0.01-0.5 in the text and
  0.1-0.5 in Table 4's footnote.
- Biggs & Northover 1988's cherry model has its form (a logit polynomial in wetness and
  temperature): held out by structure. Agrarium's D34 recommends narrowing Broome's tag so
  that it stops covering other infection indices, such as Bacchus.
