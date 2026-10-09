---
id: gleason1994
citation: Gleason, M. L., Taylor, S. E., Loughin, T. M. & Koehler, K. J. 1994. Development and Validation of an Empirical Model to Estimate the Duration of Dew Periods. Plant Disease (Special Report) 78(10):1011-1016
doi: 10.1094/PD-78-1011
read: 2026-10-08, in full, the equations on the rendered pages, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [Iowa, Kansas, Nebraska, Illinois]
processes: [leaf wetness, dew]
records: []
datasets: []
files: [10-1094-pd-78-1011.pdf]
---

# Gleason et al. 1994: an empirical model of dew duration (CART/SLD)

From Iowa State University.

## What it holds

- Empirical dew-period model fitted to hourly data from Ames, Iowa, 11 June to 7 Sept 1990 (l. 158).
- Truth is Campbell Model 237 wetness grids, painted, 900 kohm threshold (l. 146).
- Hours 8 a.m. to 7 p.m. and days with measurable rain were deleted from the fit (l. 162, 166).
- CART thresholds: dew point depression 3.7 C, wind 2.5 m/s, RH 87.8% (l. 341-345). The text prints 2.46 m/s for category 4 (l. 345); Fig. 2 prints 2.5.
- Two stepwise linear discriminant equations for the uncertain hours; thresholds 14.4674 (l. 357) and 37.0000 (l. 362). Roots and squares are lost in the text; the rendered PDF shows them.
- Validated at 13 stations in IA, KS, NE, IL, 17 April to 31 October 1992 (l. 306); 17,487 hours, 1,502 nights (l. 336, 337).
- Hours correct 83.5% against 78.6% for RH > 90% (l. 394); nights within 2 h 76.0% against 67.2% (l. 402, 403).
- No other model dates or builds the data. Rain, irrigation and cloud cover are left for later (l. 666).

## Dependence

- Its own data: development at Ames in 1990, validation at 13 stations in 1992. It splits first on dew-point depression (3.7 °C), then on wind and RH (87.8%) with two discriminant functions: thresholds on humidity, the engine's form (`rh-threshold-wetness`).
- Gleason is an author of the engine's `sentelhas2008.wetness`: a flag. Under D19 it was kin for that.

## Bearing (2026-10-08)

- **Held out by structure, not by its author** (Agrarium's candidates). Its category 4 prints 2.46 m/s in the text and 2.5 in Fig. 2, so categories 3 and 4 overlap as printed.
