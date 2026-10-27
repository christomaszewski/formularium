---
id: fernandezgonzalez2012
citation: Fernández-González, M., Rodríguez-Rajo, F. J., Jato, V., Aira, M. J., Ribeiro, H., Oliveira, M. & Abreu, I. 2012. Forecasting ARIMA models for atmospheric vineyard pathogens in Galicia and Northern Portugal: Botrytis cinerea spores. Annals of Agricultural and Environmental Medicine 19(2):255-262
doi:
read: 2026-10-26, a light reading by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; the text is two-column and the Table 4 page was rendered to check a blank cell
status: read
diseases: [grey mould]
crops: [grapevine]
regions: [Cenlle, Amares]
processes: [airborne spores, spore trap, time-series forecast, phenology]
records: []
datasets: []
files: [fernandezgonzalez2012.pdf (the 2026-10-25 other-sources drop, from Minerva USC)]
---

# Fernández-González et al. 2012: Botrytis spore counts at Cenlle and Amares forecast by ARIMA

Three seasons of Hirst-type trap counts of Botrytis cinerea spores at a Galician and a
Portuguese vineyard, their timing against the vines' stages and weather, and ARIMA models
with a humidity or rainfall term that forecast the daily count from its own past. The
2007 Cenlle season is the one `fernandezgonzalez2009` reads.

## What it holds

- **Sites** (l. 25-29, 110-132): Lanzoni VPPS-2000 traps at 2.5 m (Cenlle, Ourense) and 5 m
  (Amares, Braga), 2005-2007; 60 vines in three varieties for stages; season totals 16,145
  (Cenlle) and 1,858 (Amares) spores in 2007, lows of 1,700 (2005) and 800 (2006); sampling
  interrupted for about a week each September at Cenlle (l. 125-127).
- **Peaks** (l. 194-201): Cenlle 415 spores/m³ on 27 April 2007 and 203 on 16 June 2006;
  Amares 79 on 18 June 2007.
- **Weather links** (l. 264-267, 302-338): seasonal rain 123.8 mm (Cenlle 2007) and 155 mm
  (Amares 2007); Spearman r 0.823 with the previous day's count at Cenlle; relative humidity
  four and five days earlier r 0.212 and 0.274.
- **Models** (l. 268-272, 356-369): Cenlle ARIMA(0,2,2) with RH four days earlier, MA1 1.476
  (SE 0.137), MA2 -0.476 (0.063), RH-4 -0.009 (0.005, P 0.051), adjusted R² 0.69; Amares
  ARIMA(1,2,3) with RH three days and rain two days earlier, AR1 -0.967, MA1 0.604, MA2
  0.917, MA3 -0.522, RH-3 -0.002, rain-2 0.010, R² 0.73.
- **Check** (l. 376-383): forecast against observed by t-test, P 0.682 (Cenlle, N 526) and
  0.883 (Amares, N 549); the fit and test windows are not said to differ.
- **Not printed:** intercepts, error variances, the fit window, the ARIMA software, Table 4's
  units; Table 1's Cenlle 2007 stage-0 cells are blank.

## Dependence

- Fitted to its own trap and station series (observed); no model dated them. The forecast
  is tested on the same study's counts. Same group and site as `fernandezgonzalez2009`
  (Cenlle 2007) and `fernandezgonzalez2011`: a shared series, so any record from either
  would share calibration data with the other.

## Bearing (2026-10-26)

- For the observation strand (the 10-20 search): a spore-count forecast from the count's
  own past, with weather adding little; the stage-dated peaks are the useful data for a
  Botrytis inoculum operator. No record: the time-series form fits no process tag, and the
  2009 note holds the same series.
