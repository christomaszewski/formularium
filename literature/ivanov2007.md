---
id: ivanov2007
citation: Ivanov, V. Y., Bras, R. L. & Curtis, D. C. 2007. A weather generator for hydrological, ecological, and agricultural applications. Water Resources Research 43:W10406
doi: 10.1029/2006WR005364
read: 2026-10-27, lightly: abstract, the humidity section (2.5), the data section, the dew point results (4.5) and the summary, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 11 of 11 quotes found at their lines by scripts/verify_quotes.py; the text is two-column and interleaved, and the equations are partly garbled
status: read
diseases: []
crops: []
regions: [United States, New Mexico, Arizona, Oklahoma]
processes: [weather generator, hourly weather, dew point, storm arrival model, cloud cover, shortwave radiation, relative humidity]
records: []
datasets: []
files: [syn1027_ivanov2007.pdf (the 2026-10-27 drop)]
---

# Ivanov et al. 2007: an hourly point weather generator (the AWE-GEN precursor), validated on dew point monthly means at one arid site

Generates hourly precipitation, cloud cover, shortwave radiation, air temperature, humidity and wind from site-fitted stochastic models, with precipitation as the key driver. No record: a method; its source code is public (per the paper).

**Read this first.** Only Albuquerque results are shown in the paper; Tucson and Tulsa are in a technical report and a supplement (l. 425-428). Albuquerque is arid, "humid days are rare" (l. 501-504), so even a full humid-hour test would have had little to test there. No humidity check beyond monthly dew point statistics was printed.

## What it holds

- **Scope** (l. 12, 17): hourly step; rain, total cloud cover, incoming shortwave, air temperature, humidity and wind speed in one framework. Calibrated and validated on three airport stations, Albuquerque NM, Tucson AZ and Tulsa OK (l. 17), 30 to 35 years each (l. 917); Albuquerque January 1961 to December 1995 (l. 500).
- **Humidity model** (l. 310-350): daily dew point from daily minimum temperature by the Kimball et al. 1997 regression (l. 346), with an evaporative factor and an annual precipitation index; the dew point is then held nearly constant through the day (l. 326-330), so hourly RH follows only the air-temperature cycle. The evaporative inputs come from the previous day's values (l. 311-312). There is no rain-conditioned humidity process: precipitation drives cloud, radiation and temperature, and humidity follows through them.
- **Calibration of humidity** (l. 759-762): the monthly precipitation index is found iteratively by matching mean observed and simulated monthly dew point temperature (Albuquerque values 50 to 160, l. 762-766).
- **Validation shown** (l. 767-775): only monthly statistics of dew point (mean daily, mean daily maximum and minimum; Figure 9d to 9f), "since dew point temperatures exhibit little variability on any given day". The authors say simulated and observed dew point agree less than for air temperature (l. 773); no number is printed. The figures were not read.
- **Humidity statistics checked:** monthly dew point means and range at one arid station. None on RH distributions, hours at or above 90 %, daily RH cycle, or wet-spell lengths.
- **Limits stated** (l. 920-923): further studies are needed for wetter and colder climates; the spatial extension is not done; gap filling of observed series is named as a possible use (l. 906-907).
- **Design note** (l. 930-937): the authors point to remote sensing for near-surface humidity where it is not observed (Han et al. 2005, as cited).

## Dependence

- Builds on Curtis and Eagleson 1982 (cloud, radiation, temperature models and a doctoral dissertation by Curtis), on Kimball et al. 1997 for dew point, and on a rectangular-pulse Poisson storm model (l. 907). Fatichi, Ivanov and Caporali 2011 (not obtained) is its extension. Ivanov is also an author of Fatichi et al. 2011, the AWE-GEN paper on which `peleg2017` builds (a flag, not a dependence).

## Bearing (2026-10-27)

- **D45:** no check on humid hours. The one humidity check is monthly dew point at an arid site; the text itself says humid days are rare there. It leaves D45's finding standing.
- **D60:** a design to avoid, not copy: humidity as a near-constant dew point from Tmin does not make rain-conditioned saturated nights, which is what a vineyard wetness rule needs (compare `eccel2011`, where Tmin as the dew point overcounts hours at or above 90 % RH by 130 %). Useful: the hourly structure of a generator with rain as the driver, and the public code.
- **Not shown:** RH distribution, spells, anything in a humid climate, any disease model on its output.
