---
id: gegoutpetit2019
citation: Gégout-Petit, A., Guérin-Dubrana, L. & Li, S. 2019. A new centered spatio-temporal autologistic regression model with an application to local spread of plant diseases. Spatial Statistics 31:100361
doi: 10.1016/j.spasta.2019.100361
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [esca]
crops: [grapevine]
regions: [Bordeaux, France]
processes: [esca spread, autologistic model, pseudo-likelihood estimation, neighbourhood selection]
records: []
datasets: []
files: [gegoutpetit2019.pdf (the 2026-10-25 other-sources drop)]
---

# Gégout-Petit et al. 2019: a centred autologistic model of Esca spread in one vineyard

A spatio-temporal autologistic model with centred coefficients, fitted by maximum
pseudo-likelihood to yearly Esca leaf symptoms in one Bordeaux vineyard, 2004 to 2017.

## What it holds

- **Data:** 1 980 Cabernet Sauvignon vines in 30 rows by 66 columns, planted 1989, with
  foliar Esca scored each August from 2004 to 2017; mean prevalence 9.5 %, between 1.8 and
  16.8 % a year (l. 1634, 1691-1697).
- **Model:** the logit of a vine's symptom probability has a past-year term (rho2) and
  neighbour terms for the year before and the same year, over elliptical neighbourhoods
  (Eq. 22, l. 1722). Twenty-five neighbourhood shapes were tested (l. 1725).
- **Best model** (Table 6, l. 1761): rho2 = 2.28 (SE 0.05), the same for every neighbourhood
  (l. 1735). The paper reads exp(2.28) = 9.7 as a risk multiplier for a vine that showed
  symptoms the year before (l. 1737). The neighbour term beta1 = 0.178 (SE 0.034) gives
  exp(0.178) = 1.19 per symptomatic neighbour the year before (l. 1772). beta0 = -3.04
  gives a spontaneous level of 0.05 (l. 1768).
- **Simulation check** (Tables 4-5, l. 1656-1667): with no covariate, the true model is
  picked in 474 of 500 runs at rho1 = 0.3 (Table 4, first row).

## Dependence

- **Builds on** the autologistic model of Besag (1974), its covariate extensions by
  Gumpertz et al. (1997) and Huffer & Wu (1998), the space-time forms of Zhu et al. (2008)
  and Zheng & Zhu (2008), and the centred parameterisation of Caragea & Kaiser (2009),
  Hughes et al. (2011) and Wang & Zheng (2013) (l. 89-104).
- **Shared data:** the vineyard is "vineyard 13 in Li et al. (2016)", the plot of an
  earlier join-count study (l. 1686-1691). This is shared data, not a shared model.

## Bearing (2026-10-26)

- classes.tsv names no search for this key. Its form is a spatial and past-year model of Esca spread, relevant to a
  vineyard disease module if one is added.
- A simulator could take the form (a past-year term plus a per-neighbour term), but the
  numbers are one vineyard's, fitted to leaf symptoms. The paper was not read in full.
