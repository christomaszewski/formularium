---
id: wolkovich2017
citation: Wolkovich, E.M., Burge, D.O., Walker, M.A. & Nicholas, K.A. 2017. Phenological diversity provides opportunities for climate change adaptation in winegrapes. Journal of Ecology 105:905-912
doi: 10.1111/1365-2745.12786
read: 2026-10-27, lightly: the captions of Figures 2 and 3, the discussion of data gaps and the data accessibility statement (the review prose skimmed; the KNB deposit was not opened), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [United States, California, Davis]
processes: [dataset, phenology, common garden, budburst, flowering, veraison, review, genetic basis of phenology]
records: []
datasets: [wolkovich2017.davis]
files: [syn1027_wolkovich2017.pdf (the 2026-10-27 drop)]
---

# Wolkovich et al. 2017: a mini-review of winegrape phenology that deposits a 70-variety common-garden table for 2015

A review in the Journal of Ecology on phenological diversity as a climate-adaptation resource, whose data accessibility statement names a deposit of observed stage dates for 70 varieties in one garden. No record: a review, with a dataset behind two figures.

**Read this first.** The dataset itself (KNB deposit) was not opened; what is below is what the paper says of it in two figure captions and its data statement. The "maturity" in it is the estimated day 22 degrees Brix is reached (l. 145), not a grower's harvest date. One garden, one year.

## What it holds

- **Where to get it** (l. 313-314): KNB Data Repository, "Variety phenology", https://doi.org/10.5063/f1rf5s05. The same entry also carries the Daux et al. 2012 harvest-date data (l. 313; held in Formularium as daux2012.harvest_dates). The deposit's licence and file size were not read.
- **Variables** (l. 141-146): day of year of budburst (Eichhorn-Lorenz stage 4), 50 % flowering, 50 % veraison (rapid sugar accumulation) and "maturity", measured as the estimated day 22 degrees Brix is reached, for 70 grape varieties under a common climate; genetic data for the same plants are mapped beside them (Fig. 3 caption, l. 202-203).
- **Site and year** (l. 146, 203): a common garden of grape varieties planted at Davis, California; data collected in 2015. One site, one year.
- **Gaps** (l. 202): some variety-by-stage cells are empty ("Tips without bubbles represent where data were unavailable for a particular stage and variety").
- **How labels were made** (l. 306-308): observed by people, student collectors noted in the acknowledgements; the maturity date is an estimate from sugar sampling.
- **The authors' data caution** (l. 250, 254): almost all phenology data come from lower temperatures (often below 30 C), a gap under warming; harvest dates from different vineyards and varieties are not comparable because growers pick at different sugar levels (l. 254-258).
- **Why a common garden** (l. 258-259): it is needed to separate environmental from genetic components of phenology.

## Dependence

- Not computed from a model; the "maturity" is a field-estimated sugar threshold. The Fig. 2 climatic drivers are summarised from Jones 2015 and Nemani et al. (l. 147-149), not part of the deposit. None recorded otherwise.

## Bearing (2026-10-27)

- **Not a D60 input tier; a variety-contrast check for phenology (real-data side of D58).** Observed stage dates for 70 varieties under one climate separate variety from weather: they could test whether a simulated phenology model's varietal parameters (thermal sums) rank varieties the way real stages do, in one year.
- **Cannot train a weather response.** One site and one year means no year-to-year or multi-site signal and no weather in the deposit as far as the paper shows.
- **Limits:** deposit unopened, licence unknown, the maturity date is estimated, a review rather than a data paper.
