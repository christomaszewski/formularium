---
id: rossouw2016
citation: Rossouw, C. J. 2016. Mancozeb rainfastness and residue thresholds for control of Venturia inaequalis. MSc (Agric) thesis, Stellenbosch University, 82 pp.
doi:
read: 2026-10-26, a targeted light reading (summary, the wash-off and deposition chapters' methods and results, the benchmark table) by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; the Fig. 5 caption (printed p. 53) read in the page image by the agent and the main session
status: read
diseases: [apple scab]
crops: [apple]
regions: [Stellenbosch]
processes: [rain wash-off, fungicide residue, spray deposition, mancozeb]
records: [rossouw2016.mancozeb_washoff]
datasets: [rossouw2016.stellenbosch]
files: [rossouw2016.pdf (the 2026-10-25 other-sources drop, from SUNScholar)]
---

# Rossouw 2016: mancozeb lost from apple leaves as a saturating function of rain

Mancozeb and a fluorescent pigment sprayed on apple seedlings, then rained on at 5 mm/h
for 0, 1, 5, 10 or 15 mm: the share lost rises to a plateau of about a third of the
manganese residue and 60 % of the pigment coverage, fitted as y = A exp(Bx) + C. The only
rain wash-off fit held; the host is apple, not vine.

## What it holds

- **Setup** (l. 1800-1840, 1874, 1987): apple seedlings, five trees and four repeats; rain at
  5 mm/h from a 5.6 W nozzle at 200 kPa (about 2.7 L/min); 15, 60, 120 and 180 min for 1, 5,
  10 and 15 mm (15 min at 5 mm/h is 1.25 mm; measured volumes not reported).
- **Wash-off fits** (Fig. 5 caption, p. 53; l. 2010-2016, 2503-2505): %Mn-loss = -31.886
  exp(-0.181 x) + 32.236, R² 0.722; %FPC-loss = -67.073 exp(-0.118 x) + 61.401, R² 0.849;
  the residues themselves Mn (mg/kg) = 90.095 exp(-0.456 x) + 196.521, R² 0.651, and FPC% =
  3.472 exp(-0.301 x) + 3.211, R² 0.660; x the rain in mm; plateau losses 32.2 and 61.4 %.
  Mn-ion loss 11.95 % after 1 mm (l. 101); the Discussion's 5 and 19 % at 1 and 5 mm do
  not match the Results' 11.95 and 26.32 %.
- **Deposition** (l. 1921-1925, 2450-2453): Hoerl curves y = A x^B exp(Cx) of pigment
  coverage against spray volume per formulation, R² 0.56-0.79 (Pennfluid A 21.080, B 2.677,
  C -1.655, R² 0.760).
- **Benchmark** (l. 2864-2865, 3194-3198): pigment coverage 0.29 % at 0.15× to 8.28 % at
  1× concentration on Golden Delicious leaves, coverage = 8.67 × concentration - 0.80
  (R² 0.973); Pearson r between coverage and Mn residue 0.779 or 0.799 (l. 1951, 2031).
- **Not printed:** n per fit, standard errors, the raw wash-off data; a footnote's unit is
  garbled (l. 3201).

## Dependence

- **Fitted to** `rossouw2016.stellenbosch`: observed residues and coverages, no model in
  the data. The Hoerl form is Daniel & Wood 1971's (cited); Hunsche et al. 2006's 55 and
  80 % losses at 1 and 5 mm are cited for comparison (l. 2140). Fourie's group again
  (`brink2005`, `brink2006`): a flag.

## Bearing (2026-10-26)

- For Agrarium's fungicide-protection strand (the 10-20 search's wash-off question): a
  printed saturating wash-off curve per mm of rain, for mancozeb on apple seedlings at one
  intensity; the vine study (Cabras et al. 2001) stays closed. A new form,
  `rain-wash-off`, kin to nothing the engine runs.
