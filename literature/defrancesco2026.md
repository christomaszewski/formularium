---
id: defrancesco2026
citation: "De Francesco, A., Pintossi, A., Simonetto, A., Weber, I. D., Gervasio, P. & Gilioli, G. 2026. Modelling the phenology of the grapevine leafhopper Erasmoneura vulnerata. Pest Management Science (online 2026)"
doi: 10.1002/ps.71105
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: [grapevine]
regions: [Franciacorta, northern Italy]
processes: [stage-structured phenology, degree-day development, fecundity, trap monitoring]
records: []
datasets: []
files: [francesco_2026.pdf (the 2026-10-20 drop)]
---

# De Francesco et al. 2026: a phenology model for Erasmoneura vulnerata

A stage-structured model of the grapevine leafhopper's life stages, with non-linear temperature-driven development and two fecundity functions. It was fitted to monitoring in Franciacorta, northern Italy, in 2024 and 2025.

## What it holds

- Thirteen population series, seven from the 2024–2025 campaign and six from Duso et al., used for calibration and validation (l. 124–131).
- Calibration: mean absolute error of 3.31 on cumulative values, slightly over 3% (l. 343–346).
- Validation: mean absolute error of 5.13 days on timing, and 3.06 on value (l. 459–461).
- Adults were counted by a YOLO v8 detector, which read 9% fewer than manual counts (l. 136–140).

## Dependence

- Six series from Duso et al. (ref 11) were added to the calibration data (l. 124–129).
- Adult counts use the YOLO v8 model (ref 19). Temperature comes from ERA5-Land (l. 183).

## Bearing (2026-10-20)

- Serves t7 (insect pests). A stage-structured model with separate fecundity for overwintered and summer adults could set monitoring windows in a vine pest engine. Its validation error in timing is 5 days or so.
- Not read in full.
