---
id: hughes2017
citation: Hughes, G., McRoberts, N. & Burnett, F. J. 2017. Resolution of Probabilistic Weather Forecasts with Application in Disease Management. Phytopathology 107 (2):158-162
doi: 10.1094/PHYTO-07-16-0256-R
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 29 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [general]
processes: [warning scores, forecast evaluation]
records: []
datasets: []
files: [10-1094-phyto-07-16-0256-r.pdf]
---

# Hughes, McRoberts & Burnett 2017: resolution of probabilistic weather forecasts

From SRUC (Edinburgh) and UC Davis. Not the paper behind the engine's `hughes2017.scoring` (Hughes & Burnett 2017, Phytopathology 107:1136), but the same authors' companion.

## What it holds

- Shows that expected mutual information gives one yardstick for both disease forecasts and weather forecasts (abstract).
- Evaluation of a disease predictor cannot compare predictions with outcomes once treatment changes them (l. 57).
- Disease example: Vincelli and Lorbeer (1988a), 4 years, 204 forecasts of Botrytis squamosa spore episodes (l. 89, 143). H(O) = 0.973 nits, H(O|F) = 0.887, IM = 0.086 nits, normalized 0.088 (l. 97-98, 269).
- Weather example: Vincelli and Lorbeer (1988b), 527 rainfall forecasts in seven categories (l. 136, 140-142). UNC = 0.486, REL = 0.045, RES = 0.158, DS = 0.373 nits (l. 201-202, 224).
- Divergence skill score DSS = (RES - REL)/UNC = 0.232 (l. 229); Brier skill scores of 30.9, 27.8, 27.6% quoted from Vincelli and Lorbeer (l. 233).
- For single forecasts: specific information H(obar) - H(o_k) and relative entropy D_KL(o_k || obar) (l. 143-146).
- Disease forecasts are Bayesian posteriors from the table, so no reliability term (l. 171).
- Nothing is fitted. Hughes is also an author of hughes2013 and yuen2002.

## Dependence

- Information-theoretic scores on published forecasts (Vincelli & Lorbeer 1988); nothing fitted. A reference-role method; it links nothing.

## Bearing (2026-10-08)

- Clear and a method: scoring weather forecasts and disease forecasts on one scale, for comparing the engine's forecast-driven warnings.
