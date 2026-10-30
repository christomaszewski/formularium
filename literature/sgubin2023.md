---
id: sgubin2023
citation: Sgubin, G., Swingedouw, D., Mignot, J., Gambetta, G.A., Bois, B., Loukos, H., Noël, T., Pieri, P., García de Cortázar-Atauri, I., Ollat, N. & van Leeuwen, C. 2023. Non-linear loss of suitable wine regions over Europe in response to increasing global warming. Global Change Biology 29(3):808-826
doi: 10.1111/gcb.16493
read: 2026-10-30, in full, models and inputs; Supplementary Text 1 (phenology equations) and Table 1 (garbled) not available; figures are plots; by a reading agent and note writer (claude-sonnet-5-5); 29 of 29 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Europe]
processes: [climate projection, bias adjustment, phenology, suitability index, hydrothermic index, dryness index, varietal turnover]
records: []
datasets: []
files: [dr1030_sgubin2023.pdf (from Chris's Pieri collection, library/inbound/pieri-2026-10-27/2023-sgubin-10-1111-gcb-16493.pdf)]
---

# Sgubin et al. 2023: a fuzzy suitability index for European wine regions under warming, with a seasonal precipitation-temperature term for disease risk

Six downscaled, bias-adjusted climate series (3 GCMs x 2 RCMs) under RCP4.5 and RCP8.5 drive four phenological models for five cultivar clusters; a product of three indices gives suitability S.

**Read this first.** The disease term SZ is the hydrothermic index HyI, a seasonal sum of precipitation times temperature, not a downy mildew infection model (l. 493, 671). It is used as a proxy "to prevent the risk of severe plant diseases". There is no validation of SZ against disease. The phenological equations are in the Supplementary Text, which this copy lacks.

## What it holds

- **Climate (l. 248, 273):** CMIP5 CNRM-CM5, EC-EARTH, MPI-ESM-LR; CORDEX EUR-11 regional models CCLM4-8-17 and SMHI at 0.11 degree (12.5 km); CDF-t bias adjustment calibrated on EURO4M MESAN (historical 1980 to 2005, projections 2006 to 2100). Variables: mean, minimum, maximum temperature and precipitation.
- **Phenology (l. 74, 292, 288):** four model types (linear and non-linear, sequential and non-sequential), named in the text as the degree-day models BRIN (García de Cortázar-Atauri et al. 2009), GFV (Parker et al. 2013) and GSR (Parker et al. 2020), the sigmoid UNIFORC and UNICHILL (Chuine 2000) and the curvilinear Wang-Engel (1998); which type each belongs to is in the garbled Table 1; budburst, flowering, veraison, maturity from 1980 to 2100. Maturity is 200 g/L sugar (l. 292). Clusters: Chardonnay (early to mid), Syrah and Merlot (middle), Cabernet-Sauvignon (mid to late), plus early (10 days before Chardonnay) and late (10 days after Cabernet-Sauvignon) (l. 288).
- **Suitability:** S = SM x SP x SZ, each 0 to 1 (Eq. 2); suitable where S > L = 0.65 (l. 710).
  - **SM (maturity timing, l. 619, 624-625):** 1 if the mean temperature of the 30 days before maturity lies between 15 and 22 C, falling linearly over 25 days beyond; the window of full suitability is bounded by 10 August and 10 November (l. 622); 0 if maturity falls before 15 July or after 5 December.
  - **SP (water, l. 648-662):** DI = W0 + sum over budburst to veraison of (P - k ET0), W0 = 200 mm reset at budburst, k = 0.5 constant (l. 650-653), ET0 from Hargreaves-Samani on simulated air temperature (l. 655); SP = 0 for DI < -100 mm, rising linearly to 1 at 100 mm (limits from Fraga et al. 2013).
  - **SZ (disease, l. 671, 687, 691-692):** HyI = c x sum over budburst to maturity of (P x T), P in mm per day and T daily mean in C; c = (DOY_MAT - DOY_BUD) / 152 (days from 1 April to 30 August); SZ = 0 for HyI > 7500 C mm and 1 for HyI < 2600 C mm, linear between (Fig. 1c; limits from Malheiro 2010, Fraga 2013).
- **Results (l. 86, 905-906, 902, 951):** area loss in traditional regions 3.9 % per degree below 2 C of global warming and 17.1 % per degree above; phenological models are 52.5 +- 5.6 % of the spread (RCP4.5); varietal turnover keeps area loss at 4.7 % rather than 18.8 % (middle varieties, RCP8.5, 2020-39).
- **Limits stated (l. 1054, 1064):** soil water reset each year, no stomatal regulation, no heat waves or spring frost; no soil, urban or market constraints.

## Dependence

- HyI and DI are the Branas (1974) and Riou et al. 1994 indices of the earlier Malheiro, Santos and Fraga suitability studies; the downy mildew link is Carbonneau 2003 as cited (l. 493). No shared equation with the engine's downy mildew models (Goidanich, Kennelly, Magarey) or with the truth's.
- Phenology models are held as parker2013 (GFV) and parker2020 (GSR); BRIN, UNIFORC and Wang-Engel are not held. Authors Pieri, García de Cortázar-Atauri, van Leeuwen and Ollat are shared with several held notes (a flag only).

## Bearing (2026-10-30)

- **For the truth:** the "disease" is a seasonal P x T index with thresholds 2600 and 7500 C mm, scaled by season length. It could drive a coarse climate-risk map, not an epidemic simulation. It is a form worth recording as a reference piece, not a downy mildew model.
- **For Agrarium's climate side:** a worked chain from bias-adjusted regional climate to phenology to a water index (DI) with printed constants (k 0.5, W0 200 mm, Hargreaves ET0); and a source for the statement that phenological model spread dominates uncertainty beyond 2 C of warming.
- **Not shown:** any downy mildew result under these climates.
