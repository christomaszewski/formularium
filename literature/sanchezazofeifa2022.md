---
id: sanchezazofeifa2022
citation: Sanchez-Azofeifa, A., Sharp, I., Green, P. D. & Nightingale, J. 2022. Calibration of co-located identical PAR sensors using wireless sensor networks and characterization of the in situ fPAR variability in a tropical dry forest. Remote Sensing 14(12):2752
doi: 10.3390/rs14122752
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; Equation 1 checked in the page image, Equation 2 from the text layer only; regression figures not rendered
status: read
diseases: []
crops: []
regions: [Costa Rica, Santa Rosa National Park]
processes: [PAR sensor, sensor drift, recalibration interval, co-located sensors, wireless sensor network, sensor error]
records: []
datasets: []
files: [arturo_2022.pdf (the 2026-10-18 drop, second pass)]
---

# Sanchez-Azofeifa et al. 2022: five pairs of co-located PAR sensors in a dry forest, and how often to recalibrate

Five pairs of identical Apogee SQ-110 quantum sensors under a forest canopy, one of each pair on the manufacturer's calibration and one newly calibrated at NPL, compared over 8 to 13 months, and what that says about drift and recalibration. No record. The file key is `arturo_2022`; the drift used is the manufacturer's figure, assumed, not measured.

## What it holds

- **Network** (l. 166-169): 13 self-powered nodes with air temperature, RH, soil moisture and one SQ-110 at 1.3 m above the floor.
- **Pairs** (l. 209-213): five pairs, April 2015 to November 2015 (8 months, node 1) or April 2016 (13 months, node 4). One resident sensor on the manufacturer's calibration (5 %), one new sensor calibrated at NPL (2.5 %).
- **Manufacturer's specification** (l. 174, 236): cosine response +/-5 % at 75 degrees; temperature response 0.06 +/- 0.06 % per degC away from 20 degC; non-stability below 2 % per year. These are datasheet figures.
- **Drift is assumed** (l. 295, 303): taken as the manufacturer's under 2 % per year, cumulative and one-directional, not measured. NPL sensors calibrated March 2015; resident sensors assumed calibrated about September 2012.
- **Agreement** (Table 1, l. 313-314, 418): fit gradients node 4, 0.9461 (5.4 %) and 0.9148 (8.5 %); node 5, 1.0043 (-0.4 %) and 0.9100 (9.0 %). Eq. 2 requires |1 - gradient| below the root sum of squares of the calibration and drift uncertainties (l. 289); Table 2 (l. 325) totals 8.3 % (resident drift 6 % over 3 years, calibration 5 %, NPL calibration 2.5 %, NPL drift 1 % over 0.5 years). The paper reads the residual gradients as consistent with drift (l. 424-436).
- **Scatter** (l. 413-414): paired RMSE 130 to 220 uE at mean PAR about 500 uE for four nodes; node 5 331 uE, bimodal in senescence above 1200 uE (one sensor shadowed, one lit).
- **Recalibration** (l. 34, 644, 654): about every 4 years keeps an SQ-110 within the 10 % GCOS calibration requirement (4 years 10 months from 2.5 % calibration, 4 years 4 months from 5 %, at 2 % per year); the 3 % GCOS stability requirement would need every 18 months. A hypothetical 1 % per year sensor lengthens the interval (l. 658; not measured).
- **Exclusion** (l. 233): timesteps with tPAR above iPAR dropped as cloud artefacts. No failure, outage or replacement count is printed.
- **Eq. 1** (l. 245-247, page image): printed as 1 - flux fPAR = 1 - tPAR/iPAR, which read literally gives the transmittance; flagged, not corrected. fPAR medians 0.909 above 5 m/s wind and 0.949 below 3 m/s (l. 544-546).
- **Data** (l. 198, 773): free at Enviro-Net (enviro-net.org); no licence printed.

## Dependence

- fPAR formula after Widlowski 2010 and Putzenlechner et al.; clear-sky calculator of Walter; manufacturer calibration against a LI-COR 1800-02; NPL calibration by a co-author's laboratory. No model shaped the data.

## Bearing (2026-10-18)

Strand 5 (sensor error).

- **Drift:** the number to take is 2 % per year as an upper datasheet bound, labelled assumed. The measurement here is the gradient between two sensors after years, 5 to 9 % low for the resident sensor, with calibration error mixed in; it cannot split drift from the initial offset.
- **Recalibration:** a 10 % tolerance is reached in about 4 years at 2 % per year; a 3 % tolerance in 18 months.
- **Failure:** nothing printed.
- **Relevance:** a light sensor under a forest, not a temperature, RH or wetness sensor; no wetness estimate. The method (paired sensors, a gradient test against a combined uncertainty) could be applied to two wetness or temperature loggers in a vineyard.
