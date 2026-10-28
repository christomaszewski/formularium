---
id: bregaglio2012
citation: Bregaglio, S. 2012. Definition and implementation of plant disease simulation models in interaction with crop models, aiming at forecasting the impact of climate change scenarios on crop production. PhD thesis, Scuola di Dottorato Terra, Ambiente e Biodiversita, Universita degli Studi di Milano (XXIV cycle). Chapter 3 is Bregaglio, S., Donatelli, M., Confalonieri, R., Acutis, M. & Orlandini, S. 2010. An integrated evaluation of thirteen modelling solutions for the generation of hourly values of air relative humidity. Theoretical and Applied Climatology 102:429-438
doi: 10.13130/bregaglio-simone-ugo_phd2012-02-10 (thesis); 10.1007/s00704-010-0274-y (chapter 3 paper)
read: 2026-10-27, lightly: chapter 3 only (abstract, introduction, methods, sites, results, conclusions; lines 1235-1970 of the extracted text; the rest of the thesis, including the leaf-wetness and climate-change chapters, not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Italy, Spain, Portugal]
processes: [relative humidity, dew point, daily-to-hourly disaggregation, humidity estimation, model comparison, fuzzy composite indicator, weather generator components]
records: []
datasets: []
files: [syn1027_bregaglio2012.pdf (the 2026-10-27 drop)]
---

# Bregaglio 2012 (chapter 3, Bregaglio et al. 2010): thirteen ways to make hourly relative humidity from daily weather, scored at 22 sites

A PhD thesis whose chapter 3 compares 13 deterministic "modelling solutions" that build hourly air relative humidity (RH) from daily temperature, with or without daily RH, against hourly station records. No record: a method comparison, with no disease model in the chapter.

**Read this first.** Only chapter 3 was read. The methods are deterministic daily-to-hourly estimators (components of the CLIMA weather generator software), not stochastic generators. Every hour from 1 March to 31 October is scored together: no hours above an RH threshold are scored. The station sources are not stated in the pages read (l. 1573-1599).

## What it holds

- **Aim** (l. 1257-1271): hourly RH is a key input of fungal epidemic models, directly or through leaf-wetness models, and is often missing from historical series and climate scenarios, so it must be generated. Thirteen modelling solutions (MS) are scored on "a large dataset including several sites and years".
- **The methods** (Table 1, l. 1367-1381; text l. 1479-1545): all build hourly air temperature from Tmax and Tmin by a cosine (Campbell 1985; Eq. 1), then RH as vapour pressure over saturation (Eq. 2). MS 1 to 6 differ in the dew point: MS 1 a daily value from Tmin (Bekele et al. 2007, Eq. 3), MS 2 the same with an hourly path, MS 3 the daily minimum temperature itself, MS 4 Hubbard et al. 2003, MS 5 Linacre 1992 (a quadratic in Tmax plus a Tmin term; confirmed at l. 6635), MS 6 Ephrat et al. 1996 with a maximum dew point fitted on five Sicilian and Spanish sites. MS 7 interpolates between observed daily RHmax and RHmin (Waichler et al. 2003). MS 8_0 to 8_5 take dew point as Tmin minus a constant of 0 to 5 degC (Allen et al. 1998).
- **Sites and period** (Table 4, l. 1573-1599): 22 stations in Italy, Spain and Portugal, one to five years each between 2003 and 2008 (Campogalliano 2007 and 2008 is the only 2008 entry), 1 March to 31 October only; days with missing data dropped.
- **Validation design** (l. 1620-1670, 1760-1800): all hours pooled per site and year, then a fuzzy composite indicator (IRH) of four modules (accuracy, correlation, pattern of residuals by hour, day of year and temperature, robustness across sites and years). Limits: RMSE 12 or less favourable and 20 or more unfavourable (l. 1767); EF 0.1 or less unfavourable and 0.4 or more favourable (l. 1777). No hold-out design is described in the pages read; MS 6 was fitted on five sites (l. 1495-1510) and the constant of MS 8 was swept from 0 to 5 on the same data.
- **Table 7, mean over sites and years** (l. 1857-1869): MS 7 (observed daily RHmax and RHmin): RMSE 11.25 %RH, EF 0.705, R 0.858 (l. 1863). Best MS without them, MS 5: RMSE 16.77, EF 0.319, R 0.725 (l. 1861). MS 3 (dew point = Tmin): RMSE 19.01, EF 0.02, R 0.663 (l. 1859), "no better than the mean". MS 8_5: RMSE 19.70, EF -0.863 (l. 1869).
- **Ranking** (l. 1838-1854): IRH 0.025 for MS 7, 0.340 for MS 5; MS 2 and MS 1 third and fourth; MS 3 11th of 13. The authors say the Tmin proxy "led to large errors in different aspects".
- **Humidity statistics checked:** hourly RH over all hours (RMSE, EF, R, residual patterns by hour, day of year and temperature). None on hours at or above 90 % RH, dew point itself, daily cycle shape beyond the hour-of-day residual pattern, or monthly means (grep of the chapter for 90 %, saturation and threshold found no such scoring).
- **Authors' conclusion** (l. 1962): such analyses show which method is preferable given the data on hand; this is "the first step" of validating each link from hourly RH to a disease model.

## Dependence

- Builds on the CLIMA software components AirTemperature and EvapoTranspiration, on FAO-56 (Allen et al. 1998), ASAE 1998 saturation vapour pressure, and the five dew point methods above; the fuzzy indicator extends Bellocchi et al. 2002. The 2010 paper is the same text as chapter 3. Shared authors with `bregaglio2013` and other Bregaglio notes here (a flag, not a dependence); Donatelli and Confalonieri also author the leaf-wetness chapter 4 (not read).

## Bearing (2026-10-27)

- **D45:** does not bear on the finding. It is a check of deterministic estimators, not of a generator, and it scores all hours together; nothing here is a check on humid hours. It does show the common premise (dew point = Tmin) is the worst of the poor methods (EF 0.02, l. 1859).
- **D60, filling missing RH:** a ranking of ready fillers on 22 sites in Italy, Spain and Portugal in the growing season (March to October): if daily RHmax and RHmin exist, use them (EF 0.705, l. 1863); if not, a Tmax and Tmin dew point (Linacre) reaches only EF 0.32 (l. 1861), and the other 11 methods are below. The scores are whole-sample, so a filler passing here is not shown fit for hours at or above 90 % (`eccel2011` tests that, and fails it at half its sites).
- **Not shown:** any rain-conditioned humidity, any effect on a disease or wetness model, any site north of 45.8 N (Varese) or outside Europe.
