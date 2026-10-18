---
id: pidoto2023
citation: Pidoto, R. & Haberlandt, U. 2023. A semi-parametric hourly space–time weather generator. Hydrology and Earth System Sciences 27:3957-3975
doi: 10.5194/hess-27-3957-2023
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 41 of 41 quotes found at their lines by scripts/verify_quotes.py; Eqs 20-23 and the Magnus coefficients (p. 3964) checked in the page image by the main session
status: read
diseases: []
crops: []
regions: [Germany]
processes: [weather generator, rainfall, hourly disaggregation, relative humidity]
records: [pidoto2023.hourly_generator]
datasets: [pidoto2023.germany]
files: [ross_2023.pdf (the 2026-10-18 drop)]
---

# Pidoto & Haberlandt 2023: an hourly space–time weather generator

A generator for flood-frequency work: rainfall as an alternating renewal process of wet
and dry spells with copulas, tuned to match spatial rainfall by simulated annealing; daily
temperature, relative humidity and global radiation by k-NN resampling of gridded daily
data; hourly values by MELODIST's deterministic forms.

## What it holds

- **Rainfall** (l. 176-260): wet spell duration lognormal (Eq. 6), dry spell duration and
  wet spell amount Weibull (Eq. 5, replacing a four-parameter kappa), a Khoudraji–Gumbel
  copula between them (Eqs 2-4), an exponential hyetograph with α = 1/3 (l. 233, from
  Callau Poduje & Haberlandt 2017), a Gaussian copula for the peak (Eq. 8). Three bivariate
  spatial criteria in the annealing (l. 253). Seasons: April-September and October-March
  (l. 579). No table of fitted values.
- **Non-rainfall** (l. 415-460, Eq. 19): weighted Euclidean k-NN on a daily feature vector
  of relative humidity, mean, minimum and maximum temperature and global radiation, with
  weights 1/j. No wind variable (l. 30-31, 39-40).
- **Hourly step** (Sect. 2.4, p. 3964): MELODIST (Förster et al. 2016) forms that need no
  hourly observations. Temperature by a cosine with the hour of maximum 2 h after solar
  noon (Eq. 20); RH = 100 es(Tdew)/es(T) (Eq. 21) with Magnus es (Eq. 22: 6.1078,
  17.08085, 234.175 above 0 °C; 6.1071, 22.4429, 272.44 below) and Tdew = Tmin held all day
  (l. 501-502); radiation by a flat-surface formula with 1370 W m-2 (Eq. 23, l. 505).
  Nothing printed caps RH at 100 % (l. 487).
- **Data** (l. 519-587): 400 catchments, 699 DWD sub-daily rainfall stations, window
  2006-2020 (l. 537); HYRAS v4.0 daily grids 1976-2015 (l. 551); 40 DWD reference stations
  for validation, 20 with radiation (l. 553-556); 100 realisations of 15 years (l. 573).
- **Fit and tests** (l. 786-818, 845): daily non-rainfall bias rarely above 5 % (l. 786);
  relative humidity has the greatest spread, April-July (l. 787), and is in part very poor
  before resampling (l. 790); after the hourly step, hourly means deviate, most for daily
  minima and winter humidity (l. 818); radiation is best (l. 845).
- **Not printed:** fitted rainfall parameters, the window w, the copula θ, the annealing
  schedule, es units. Software "on request" (l. 905); data are open (l. 897).

## Dependence

- **Shared implementation:** the hourly step is MELODIST (`forster2016.melodist`), so its
  hourly humidity is the same rule as MELODIST's H1.
- **Builds on** Haberlandt et al. 2008 and Callau Poduje & Haberlandt 2017 (l. 172-175,
  227-234); Magnus from Alduchov & Eskridge 1997; radiation from Liston & Elder 2006.
- **Data:** DWD stations and HYRAS. No model is said to have made them.

## Bearing (2026-10-18)

For Agrarium's sweep (thousands of seasons of hourly weather driving a leaf-wetness model
whose engine counterpart is RH ≥ 90 %):

- **Variables and co-variation:** hourly rainfall, temperature, relative humidity and global
  radiation; no wind, so no wind direction with rain. Humidity, temperature and radiation are
  resampled together and conditioned on the catchment rainfall state, so they follow rain
  at the daily step. Hourly humidity is only es(Tmin)/es(T(h)): it does not rise on a rainy
  hour.
- **Near saturation or wet hours:** not validated on humidity near saturation; no
  wet-hour statistic. Humidity is checked as monthly and hourly means.
- **Where fitted and tested:** Germany, 400 catchments; rainfall on 699 DWD stations
  (2006-2020), HYRAS 1976-2015, 40 reference stations for validation.
- **Code and licence:** R and Python, on request; no licence printed.
- **Can it run:** not from the paper. Coefficients of the rainfall model are not printed;
  only the hourly step is reproducible, because MELODIST is open.
