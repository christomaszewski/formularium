---
id: lange2019
citation: Lange, S. 2019. Trend-preserving bias adjustment and statistical downscaling with ISIMIP3BASD (v1.0). Geoscientific Model Development 12:3055-3070
doi: 10.5194/gmd-12-3055-2019
read: 2026-10-27, lightly: abstract, section 2 (data), parts of section 3 (bias adjustment of bounded variables, the hurs settings, the cross-validation design), the results summary and conclusions; searched for humidity treatment, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [none]
processes: [bias adjustment, quantile mapping, statistical downscaling, trend preservation, bounded variables, relative humidity, cross-validation]
records: []
datasets: []
files: [syn1027_lange2019.pdf (the 2026-10-27 drop)]
---

# Lange 2019: ISIMIP3BASD, a trend-preserving quantile-mapping bias adjustment for ten daily climate variables including daily mean relative humidity

A bias-adjustment and downscaling method for global climate-model output, tested on four CMIP5 models against a reanalysis-based reference. No record: a method; the reference is a model-based product (EWEMBI), not station data.

**Read this first.** It adjusts daily means on a 2 degree grid (hurs is daily mean relative humidity), and its reference (EWEMBI) is a merged, bias-corrected product that includes reanalysis data (l. 64-72); where its humidity comes from is in Frieler et al. 2017, not read. No hourly variable is adjusted, so hours at or above 90 % RH are not a target and are not scored. The paper has no discussion of humidity beyond treating it as a bounded variable.

## What it holds

- **Variables** (Table 1, l. 118-130): ten daily variables, one of which is daily mean near-surface relative humidity (hurs, %). The others are precipitation, snowfall, pressure, two radiation terms, wind speed and three temperatures.
- **Humidity treatment** (l. 108-112, 195-203, 270-278): hurs is a bounded variable, adjusted by parametric quantile mapping with beta distributions and fixed bounds of 0 and 100 % (l. 112), and a modified event-likelihood adjustment. Table 2 for hurs: lower threshold 0.01 and upper threshold 99.99 %, beta distribution, "bounded" trend preservation, no detrending (l. 203). The thresholds fix the frequency of values near the bounds: for hurs, the frequency of near-saturated DAILY mean RH (99.99 % or more), not of hours above 90 % (l. 270-278).
- **Data** (l. 64-72, 102-108): reference EWEMBI, 0.5 degree daily, 1979-2016, merged and bias-corrected from reanalysis (ERA-Interim) and other sources; simulation data from four CMIP5 models (GFDL-ESM2M, HadGEM2-ES, IPSL-CM5A-LR, MIROC5), historical plus rcp85, on a 2 degree grid; 1980-2015 for training and 2064-2099 for application.
- **Validation design** (l. 741-755): cross-validation with odd-numbered years of 1980-2015 for training and even-numbered years for application, then swapped; judged by absolute errors of the 5th, 50th and 95th percentile of daily values per calendar month and grid cell (l. 727, 821-823), against the ISIMIP2b method.
- **Result** (l. 821-835): in most calendar months and grid cells ISIMIP3 adjusts biases better than ISIMIP2b for all ten variables; "the greatest gains are found for hurs, rlds, rsds, and sfcWind". No single number is printed in the text; the evidence is in figures (Fig. 7 to 9), not read.
- **Downscaling** (l. 903-905): the stochastic spatial downscaling from 2 to 0.5 degrees adjusts spatial variability better than interpolation for hurs, tas, tasmax and tasmin.
- **Humidity statistics checked:** quantiles (5th, 50th, 95th) of daily mean RH against a reanalysis-based product. None on hours at or above 90 %, dew point, daily cycle or wet spells; no station data.

## Dependence

- Reference EWEMBI (Lange 2019a; ERA-Interim based). Builds on the ISIMIP2b method (Frieler et al. 2017; Hempel et al. 2013) and on the event-likelihood adjustment of Switanek et al. 2017 (as cited). CMIP5 outputs. Single author.

## Bearing (2026-10-27)

- **D45:** not a check on humid hours and not a generator. It is a daily-mean bias adjustment judged against a merged reanalysis-based reference, so it says nothing on whether adjusted humidity keeps the right number of hours at or above 90 %.
- **D60:** a quantile-mapping recipe for bounded daily RH (beta distributions with bounds 0 and 100 %), the likely first step if a generator or reanalysis is bias-corrected to station climate; an hourly step (disaggregation, then a check of the 90 % hour count as in `eccel2011`) would still be needed. The code is public on Zenodo (l. 960-962).
- **Not shown:** the effect of the correction on hourly RH, on spells or on any disease output; a station-based reference.
