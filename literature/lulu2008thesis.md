---
id: lulu2008thesis
citation: Lulu, Jorge. 2008. Duração do período de molhamento em vinhedo de 'Niagara Rosada' e sua relação com a ocorrência de míldio (Plasmopara viticola). Tese de doutorado, Escola Superior de Agricultura 'Luiz de Queiroz', Universidade de São Paulo, Piracicaba (advisor P. C. Sentelhas)
doi: 
read: 2026-10-10, the chapters with measurements, models and downy mildew in full (Portuguese), the literature review skimmed, by a reading agent (claude-haiku-5-5); 89 quotes checked by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [São Paulo]
processes: [leaf wetness, season severity]
records: [sentelhas2008.wetness]
datasets: [lulu2008.jundiai]
files: [lulu2008_usp_thesis.pdf]
---

# Lulu 2008 (thesis): leaf wetness in a Niagara Rosada vineyard, and downy mildew

Chapters 2 and 3 are [lulu2008spatial](lulu2008spatial.md) and
[lulu2008turf](lulu2008turf.md).

## What it holds

- **Site:** IAC Jundiaí (715 m), São Paulo; Campbell 237 flat plates at 45° in the vineyard
  (1.6 m and 1.0 m) and a turf reference at 30 cm, 30°; 11 November 2005 to 5 March 2006.
- **Chapter 2:** no significant difference in wetness between canopy positions; the top,
  south-west face is longest; vineyard against turf R² 0.86-0.89 (all days).
- **Chapter 3:** four wetness models on turf: hours above 90 % RH, dew-point depression
  (2.0 and 3.8 °C), CART and Penman-Monteith. All days: CART R² 0.82 (mean error -1.09 h),
  RH > 90 % R² 0.84, dew-point depression R² 0.82, Penman-Monteith 0.69.
- **Chapter 4 (downy mildew):** 3 August 2006 to 26 April 2007, six pruning dates, 20
  plants a plot, scores every 7 days. Severity by date is in figures only. Gompertz fits
  leaves best, monomolecular bunches; the best in-sample regressions (leaves R² 0.72,
  bunches 0.80) use wetness duration and mean temperature. Not tested on independent data.
- **Printed slips:** Table 3.4 repeats Table 3.3; one c index does not follow from its d
  and R².

## Dependence

- The RH > 90 % and dew-point-depression models are the forms of the engine's
  `sentelhas2008.wetness`, on Jundiaí data only (no overlap with Sentelhas 2008's four
  sites). Sentelhas, the advisor, is an author of the engine's record: a flag.

## Bearing (2026-10-10)

- Measured canopy against reference wetness, and downy mildew under six pruning dates in
  a subtropical vineyard: context for a truth's wetness and its seasons.
