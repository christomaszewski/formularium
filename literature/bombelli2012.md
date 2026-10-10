---
id: bombelli2012
citation: Bombelli, E. C., Wright, E. R., Moschini, R. C., López, M. V., Fabrizio, María del Carmen, Barberis, J. G. & Rivera, M. C. 2012. Modelado computacional de datos epidemiológicos para predecir enfermedades de cultivos con base meteorológica [Computational modelling of epidemiological data to predict crop diseases from weather]. 10° Simposio sobre la Sociedad de la Información, SSI 2012 (41 JAIIO), pp. 322-334
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 24 of 24 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [alternaria leaf spot, downy mildew, late blight]
crops: [blueberry, highbush blueberry]
regions: [Argentina, San Pedro, Concordia, Gualeguaychú]
processes: [severity, epidemic rate, senescence, leaf wetness, degree-days, logistic regression, spray timing, season severity]
records: []
datasets: []
files: [argentina_unlp_doc.pdf]
---

# Bombelli et al. 2012: models of Alternaria leaf spot on blueberry

A light read (the deep-research B list).

## What it holds

- Alternaria tenuissima leaf spot on highbush blueberry (cv. O'Neal) at three Argentine sites, 2008/09 and 2009/10 (l. 17-20).
- Logistic models of the epidemic rate: senescence alone gave 93.8 per cent correct, and the best ordinal model 86.2 per cent (l. 22-24, 688).
- Predictors: days with minimum temperature above 16 C and maximum below 36 C (l. 513), and rain days with RH above 65-85 per cent (l. 520).
- Epidemic onset at 170 degree-days from 1 July, base 12.5 C (l. 398).
- Thresholds are given as ranges in the methods but fixed in Cuadro 4 (l. 514, 637).

## Dependence

- No model the engine runs is computed or fitted here; the study is on Alternaria, not downy mildew. Shared form only: (a) a degree-day onset counted from a fixed date with a 12.5 C base (l. 397-398), not the engine's 5 C from 1 January; (b) a rain-day count with an RH threshold of 65-85 per cent as a wetness proxy (l. 520, 640). Cited only: Madden et al. 2000 (l. 80-88, ref 5), a downy mildew warning-system evaluation. N. Lalancette is a co-author of Madden et al. 2000, a flag only.

## Bearing (2026-10-10)

- Not downy mildew: an Alternaria method paper. Its shared forms (a fixed-date degree-day onset and a rain-plus-RH wetness count) are noted; it offers method, not data, for the truth.
