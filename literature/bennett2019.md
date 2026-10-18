---
id: bennett2019
citation: Bennett, A. R., Hamman, J. J. & Nijssen, B. 2019. MetSim v2.0.0: a flexible and extensible framework for the estimation and disaggregation of meteorological data. Geoscientific Model Development Discussions (preprint gmd-2019-179)
doi: 10.5194/gmd-2019-179
read: 2026-10-18, LIGHT (the discussion preprint: abstract, Sect. 1-2, option table, Sect. 4-5, code availability), by a reading agent (claude-haiku-5-5); 20 of 20 quotes found at their lines by scripts/verify_quotes.py; no page image checked
status: read
diseases: []
crops: []
regions: [Stehekin, Washington, USA]
processes: [disaggregation, hourly weather, relative humidity]
records: []
datasets: []
files: [andrew_2019_2.pdf (the 2026-10-18 drop)]
---

# Bennett et al. 2019: MetSim, estimation and disaggregation of meteorology

An open Python framework that estimates and disaggregates sub-daily shortwave, longwave,
pressure, specific and relative humidity, vapour pressure, precipitation and temperature from
daily Tmin, Tmax and precipitation (l. 17-18). It follows MTCLIM (Thornton & Running 1999)
and Bohn et al. 2013 (l. 166), and reproduces the VIC 4.2 preprocessor. No record: an
estimator driven by daily weather, not a generator, and no humidity check against observations.

## What it holds

- **Humidity** (l. 193-198): vapour pressure interpolated linearly between saturation values
  at Tmin, "corrected" so it never exceeds saturation at the disaggregated temperature
  (l. 196); specific and relative humidity then follow from temperature and pressure.
- **Other:** flat-cell solar geometry (l. 163); cloud from the daily temperature range and
  dew point from seasonal precipitation (l. 125); shortwave scaled by rain_scalar 0.75 above
  sw_prec_thresh 0 (l. 287-289); tday_coef 0.45 (l. 291); equations referred to Bohn et al.
  2013 and not printed.
- **Test:** NRMSE below 0.02 against the VIC 4.2 preprocessor for one cell near Stehekin,
  January 1949, hourly (l. 356-367); Table 2 (l. 691-692): RH 0.0179, specific humidity
  0.0086, vapour pressure 0.0074, temperature 0.0072, shortwave 0.0024. No observation is
  used.
- **Code:** GitHub UW-Hydro/MetSim (l. 448), Zenodo 10.5281/zenodo.3247806 (l. 450); licence
  not printed.

## Dependence

- A shared implementation of MTCLIM and the VIC 4.2 preprocessor, whose output is the test
  reference (a model's output as reference, not calibration).

## Bearing (2026-10-18)

For Agrarium's sweep (thousands of seasons of hourly weather driving a leaf-wetness model
whose engine counterpart is RH ≥ 90 %):

- **Variables and co-variation:** hourly temperature, humidity, radiation, pressure and
  rain from daily inputs; wind appears in the test table, direction not discussed. Rain
  only dims shortwave. It is not a generator.
- **Near saturation or wet hours:** not validated on humidity near saturation, nor on wet
  hours, nor against any observation. Its only humidity statement is the cap at saturation
  (l. 196), which means RH never exceeds 100 %.
- **Where fitted and tested:** one VIC sample cell near Stehekin, Washington, January 1949.
- **Code and licence:** GitHub and Zenodo; licence not printed in the text read.
- **Can it run:** yes, but it is an estimator of MTCLIM defaults, not shown to fit any
  humidity series.
