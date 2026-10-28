---
id: atlas2015
citation: Atlas, R., Hoffman, R.N., Ma, Z., Emmitt, G.D., Wood, S.A. Jr, Greco, S., Tucker, S., Bucci, L., Annane, B., Hardesty, R.M. & Murillo, S. 2015. Observing system simulation experiments (OSSEs) to evaluate the potential impact of an optical autocovariance wind lidar (OAWL) on numerical weather prediction. Journal of Atmospheric and Oceanic Technology 32:1593-1613
doi: 10.1175/JTECH-D-15-0038.1
read: 2026-10-27, lightly: abstract, introduction, the OSSE-system description, the results summary and caveats, and a keyword search for twin, calibration and validation, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [OSSE, nature run, data assimilation, wind lidar, numerical weather prediction, OSE calibration]
records: []
datasets: []
files: [syn1027_atlas2015.pdf (the 2026-10-27 drop)]
---

# Atlas et al. 2015: an OSSE for a proposed space wind lidar (OAWL), global and hurricane

An observing-system simulation experiment for a wind lidar that has not flown: simulated lidar winds are assimilated into NCEP's system against an ECMWF nature run, and the forecast gain is measured against that nature run. No record: a method applied to one proposed instrument.

**Read this first.** TRUTH-METHOD cites "Atlas et al. 2015" without saying which paper. This is the J. Atmos. Oceanic Technol. OSSE paper. A second 2015 paper by Atlas, Bucci, Annane, Hoffman and Murillo on hurricane OSSEs (Mar. Technol. Soc. J. 49(6):140-148, doi 10.4031/MTSJ.49.6.3) could not be obtained and is not read. This paper has nothing on identical or fraternal twins.

## What it holds

- **Design** (l. 38-39): the global OSSE uses the ECMWF T511 nature run and NCEP's operational GDAS at T382, so the nature run and the forecast model are different models. A regional OSSE embeds a hurricane nature run in the HWRF assimilation system with 9 km and 3 km domains.
- **Calibration, in one sentence** (l. 98-104, cited from Atlas 1997): "It is essential that" every element of the OSSE process is realistic and "each element is verified and calibrated by comparison" with real-data OSEs. The paper reports no OSE-versus-OSSE comparison of its own, and none is possible: the instrument does not exist.
- **Definitions and history** (l. 87, 132, cited from the review it builds on): OSEs are data-denial experiments with real data, OSSEs the same with simulated data; the methodology dates from Atlas et al. 1985a.
- **Result** (l. 910-912): at forecast hour 144 (day 6) the OAWL impact on the 500 hPa anomaly correlation is about 2.8 % (Northern) and 2.9 % (Southern Hemisphere extratropics), reported as statistically significant. The tropical wind improvement decays as forecasts lengthen. A figure, not a validation: no real instrument judges it.
- **Hurricanes** (l. 909): OAWL data in the regional assimilation improved the HWRF intensity forecast; in the global assimilation it improved track. Sample sizes are small, and the operational systems used have since been replaced (caveats, l. 914-928).
- **One stated direction of bias** (l. 922): the control experiment's observations were simulated without realistic errors; the authors say adding such errors "might be expected to make" the lidar data even more valuable. 

## What TRUTH-METHOD says of it

TRUTH-METHOD's reference table lists "NOAA OSSE reports; Halliwell et al. 2014 (ocean OSSE); Atlas et al. 2015" for "identical and fraternal twins; calibrating an OSSE against OSEs" (status snippet).

Verdict: **differs, and unresolved.** This paper says nothing on twins (no twin discussion found by keyword search). It supports only the calibration half, in the single sentence at l. 98-104, and reports no calibration of its own. Its design is a different-model pair (l. 38-39), which fits the fraternal-twin idea but is not described as such. Whether the other 2015 Atlas paper is the one meant is unchecked.

## Dependence

- Builds on Atlas 1997 and Atlas et al. 1985a for the method, on the ECMWF T511 nature run of Andersson & Masutani 2010, and on NCEP's GDAS (Kleist et al. 2009). Several authors (Atlas, Hoffman) also wrote `hoffman2016`: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD:** cite this paper only for "each element verified and calibrated by comparison with real-data OSEs" (l. 102), not for twins. The calibrated fraternal-twin OSSE is the method's own shape: different nature-run and forecast models, then a comparison with reality.
- **Not shown:** an OSSE prediction later checked against the flown instrument. The gain is a simulation result only.
