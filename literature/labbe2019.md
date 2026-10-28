---
id: labbe2019
citation: Labbé, T., Pfister, C., Brönnimann, S., Rousseau, D., Franke, J. & Bois, B. 2019. The longest homogeneous series of grape harvest dates, Beaune 1354-2018, and its significance for the understanding of past and present climate. Climate of the Past 15:1485-1501
doi: 10.5194/cp-15-1485-2019
read: 2026-10-27, lightly: abstract, sections 1-2 (the series, its sources, homogenisation, interpolation), section 3 statistical models, Table 5 and the data availability statement (sections 4-5 on climate reading and blocking not extracted; two-column text layer), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 20 of 20 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Burgundy, Beaune]
processes: [dataset, phenology, grape harvest date, historical climatology, temperature reconstruction, homogenisation, regression]
records: []
datasets: [labbe2019.beaune]
files: [syn1027_labbe2019beaune.pdf (the 2026-10-27 drop)]
---

# Labbé et al. 2019: the 664-year Beaune series of grape harvest dates, and its fit to Paris spring-summer temperature

A climate-history paper that publishes a homogenised archival series of the opening day of the grape harvest at Beaune, 1354-2018, and fits it to Paris April-July temperature. No record: a dataset (one value a year).

**Read this first.** A harvest date is a collective or grower decision, not a ripeness measurement (l. 46-48, paraphrased): the paper compares the official opening with the actual start reported in newspapers for modern years (l. 238-246). Dates before 1718 were shifted by 7 days to fit the later regime (l. 246), and 61 dates before 1645 are interpolated (l. 251). Temperature is Paris, not Beaune.

## What it holds

- **Where to get it** (l. 64, 731-734): the Euro-Climhist platform of the University of Bern (page not opened by the reading agent or the note writer), together with the Paris April-July temperature series 1659-2018; the reconstruction is in the journal supplement. The data licence is not stated in the paper.
- **Licence** (l. 4): the paper is CC BY 4.0 (Copernicus); the licence of the Euro-Climhist data is not stated in the paper.
- **Years and site** (l. 43, 110): 664 years, 1354-2018, for the Beaune territory in Burgundy, vineyards between 220 and 300 m. One value per year (the harvest start as day of year); Table 5 SD of the observed series is 9.37 days (l. 572).
- **Regimes** (l. 47-50): average harvest start 28 September from 1354 to 1987; harvests began 13 days earlier over 1988-2018 (31 years).
- **Source quality** (l. 131-134): the older Dijon series has 132 differences with the archives from 1385 to 1879, mismatches of 5-10 days in 17 years, 10-20 days nine times and over 20 days in seven years.
- **How the series was made** (l. 238-251): archives and newspapers; the official ban date and the actual start differ (r = -0.833 for the actual start against Paris April-July temperature over 1980-2007, against -0.789 for the official date, l. 242); 7 days added before 1718 (l. 246); the homogenised series correlates with Paris April-July temperature at r = 0.76 over 1658-2018 (l. 250), against 0.74 for the raw one (l. 251).
- **Forward model** (l. 340-346): harvest date (day of year) from monthly Paris temperature, March to July: intercept 396.75 days, then -0.624, -1.259, -2.200, -2.773 and -1.655 days per degree C. Calibrated 1659-1850, evaluated 1851-2018 (l. 340).
- **Scores, evaluation 1851-2018** (Table 5, l. 568-572): linear model correlation 0.832 (calibration 0.726), a log-transformed model 0.843 (0.731), the same model driven by the EKF400 reanalysis ensemble 0.720 (0.651); evaluation bias +1.06, +0.48 and -1.46 days; the fits reproduce less spread than the record (SD 6.91 and 7.10 days against 9.37).
- **How labels were made:** observed by people (archival and newspaper dates), then homogenised and interpolated by the authors; no weather model made the dates.

## Dependence

- Temperature: Paris series since 1659 (Rousseau). Two of the fits are driven by climate-model output (the CCC400 simulation and the EKF400 reanalysis, l. 362-380); the series itself uses no model. Builds on Labbé & Gaveau's Beaune and Dijon archive work (l. 131-134, 252). Related, from the reading agent's lead and not checked in this paper: Daux et al. 2012 (held in Formularium as daux2012.harvest_dates). None recorded otherwise.

## Bearing (2026-10-27)

- **Not a D60 input tier; a real long outcome for a ripening or phenology check (real-data side of D58).** The published slopes (about -1.3 to -2.8 days per degree C of April-July temperature, l. 344-346) are a real-data target for the climate sensitivity of a harvest-start or ripening model run on a long synthetic weather series; they test the trend in the mean, not stage timing.
- **Limits:** harvest start is a decision; one wine territory; temperature from Paris, monthly; an out-of-period test (1851-2018), not an out-of-site one; 7-day shift and interpolation are the authors' judgement.
- **Not shown:** daily weather, a disease, a phenological stage other than harvest start.
