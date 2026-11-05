---
id: schmidt2022
citation: Schmidt, D., Kahlen, K., Bahr, C. & Friedel, M. 2022. Towards a Stochastic Model to Simulate Grapevine Architecture: A Case Study on Digitized Riesling Vines Considering Effects of Elevated CO2. Plants 11(6):801
doi: 10.3390/plants11060801
read: "2026-11-04, the methods and results on cardinal temperatures and internode appearance rate (Europe PMC full-text XML), by a reading agent and a note writer; 3 of 3 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [Germany, Geisenheim]
processes: [leaf appearance, phenology, development days, Wang-Engel, cardinal temperatures, internode]
records: []
datasets: []
files: [dr1104_schmidt2022.xml (the 2026-11-04 drop)]
---

# Schmidt et al. 2022: Riesling leaf appearance in development days, with Wang-Engel cardinal temperatures

A Geisenheim study of digitised Riesling shoots under ambient and elevated CO2 that fits cardinal temperatures for budburst-to-leaf stages and then the rate at which new internodes (leaves) appear.

## What it holds

- **Setting:** Riesling vines in the VineyardFACE at Geisenheim, Germany, 2018 and 2019, with hourly air temperature from a station at the site; phenology ratings of shoots and 3D digitising of six vines (l. 24, outside the quoted lines, grep).
- **Cardinal temperatures (l. 123):** for predicting growth stages, Tbase = 10.8 °C, Topt = 19 °C and Tupper = 24.7 °C, in the Wang-Engel development-day function (grep, l. 123). Fit: R2 = 0.8837 for phenology and 0.8797 for apex rank in training (grep, l. 123).
- **Leaf appearance rate (l. 170):** 1/IAR is 1.285 cumulative development days (CDD) per rank, so one new leaf per 1.285 CDD. The mean rate is 0.7784 ranks/CDD with a standard deviation of 0.081 ranks/CDD (grep, l. 170); the Bayesian phenology model gave a slope of 1.289 (grep, l. 170). CDD are days at the optimum temperature.
- **Stages (l. 40):** modified E-L stages 7 to 18 are counted by leaves separated; E-L 12 is "5 leaves separated" (l. 11); they correspond to BBCH 11 to 16.
- **Linear range (grep, l. 168):** a linear link between apex rank and CDD was assumed up to the highest observed rank, 23.
- **Year and CO2:** model performance was not affected by removing the year and CO2-treatment factors (grep, l. 170).

## Dependence

- Wang and Engel's temperature response for the development-day function. Riesling shoots digitised in the VineyardFACE; validated on Geisenheim 1986 to 1987 plastochron data, as the reading agent reports. The cardinal temperatures are the authors' own fit.

## Bearing (2026-11-04)

- **host.primary_after_budburst_days:** a leaf appearance rate for Riesling of 1.285 development days per leaf, with a Wang-Engel temperature response (Tbase 10.8 °C, Topt 19 °C, Tupper 24.7 °C). It turns a count of leaves needed for first susceptibility into days after budburst for Agrarium.
- Kind of evidence: a fitted field measurement on one cultivar in one German site over two seasons; its cardinal temperatures differ from other varieties' (a lead the reading agent flags: Chardonnay Tbase 0.24 °C in a cited paper, unchecked).
