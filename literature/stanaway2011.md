---
id: stanaway2011
citation: "Stanaway, M. A., Mengersen, K. L. & Reeves, R. 2011. Hierarchical Bayesian modelling of early detection surveillance for plant pest invasions. Environmental and Ecological Statistics 18:569-591"
doi: 10.1007/s10651-010-0152-x
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: []
crops: [banana]
regions: [Australia (Cairns, Queensland)]
processes: [Bayesian incursion model, colonisation time and spread, per-plant detectability over time, plants inspected per visit, reporting probability, early detection surveillance]
records: []
datasets: []
files: [stanaway_2010.pdf (the 2026-10-20 drop)]
---

# Stanaway et al. 2011: Bayesian early-detection surveillance for pest invasions

A hierarchical Bayesian model of an incursion, its per-plant detectability and survey absence records. It is applied to an early-detection programme for banana pests in Cairns.

## What it holds

- **Detectability:** per-plant detectability rises on a logistic curve with time since colonisation (l. 259-274). A visit that inspects n plants sees the pest with probability 1 - (1 - D)^n (l. 308). The pest is then reported with probability omega (l. 314).
- **Priors:** detectability reaches 0.5 after 24, 125 and 653 days at the 5, 50 and 95 % quantiles (l. 366-367). Visit-to-visit noise is normal on the logit scale, with variance 0.1 (l. 371-374).
- **Effort, in simulation:** scenario A has 20 sites, visited six-monthly, with 20 plants per visit (l. 464-468). The probability that the district is colonised falls from a prior 0.62 to 0.44. With 10 sites it is 0.47, and with 40 it is 0.39 (l. 490-491, Table 2 at l. 503).
- **Banana data:** 272 sites on 326 occasions, averaging 19 plants per occasion, July 2003 to June 2008 (l. 565-567). The colonisation probability falls from a prior 0.38 to 0.090 (Table 3, l. 624).
- **No measured detection rate:** the observation parameters are "poorly identified by the data" (l. 322). Per-plant detectability is a prior, not a field estimate.

## Dependence

- Uses the hierarchical framework of Wikle (2003) (l. 90, 178).
- The detectability curve is "similarly shaped" to the Ricker model of Hooten et al. (2007), here an inverse logit (l. 267-269).
- Priors are elicited from managers and ecologists, with no named source (l. 330).
- The surveillance records come from Biosecurity Queensland (l. 822).

## Bearing (2026-10-20)

- Serves t2 (observation). The logistic detectability curve and the 1 - (1 - D)^n effort term (l. 274, 308) are a shape a vineyard observation model could take. The per-plant values would need vineyard data, since the priors are for banana pests in Queensland.
- Not read in full.
