---
id: savary2009
citation: Savary, Serge, Delbac, Lionel, Rochas, Amélie, Taisant, Guillaume & Willocquet, Laetitia. 2009. Analysis of nonlinear relationships in dual epidemics, and its application to the management of grapevine downy and powdery mildews. Phytopathology 99(8):930-942
doi: 10.1094/PHYTO-99-8-0930
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Bordeaux, Couhins, Latresne]
processes: [epidemic progress, cluster infection, season severity, spray timing]
records: []
datasets: []
files: [savary2009_phyto.pdf]
---

# Savary et al. 2009: foliage drives cluster disease, in Bordeaux field epidemics

Fetched 2026-10-12 from a Wayback capture of the APS PDF. Two seasons of downy and
powdery mildew on leaves and clusters at two Bordeaux vineyards under three spray levels,
fitted with a logistic leaf curve and a cluster-transfer equation; the design `fabre2024`
reuses for its yield-loss work.

## What it holds

- **Trials:** Couhins and Latresne, about 7 km apart, Cabernet franc on double Guyot at
  1.80 × 1.10 m, 2006 and 2007 (l. 41-46); randomised blocks, six replicates, 18 plots of
  100 m² a site (l. 56-59); unprotected, limited (three sprays against each disease from
  stage 66 or 55) and continuous (nine each from stage 16) protection (l. 52-84); severity
  as percent area on leaves and clusters of six vines a plot at seven crop stages from 53
  to 89 (l. 97-116); weather stations under 300 m: 2006 rain 970 mm at Couhins and 716 at
  Latresne, 2007 485 and 950 mm, mean maxima 25.4 and 23.6 °C (l. 49-51, 216-225). Weather
  enters no equation.
- **Severities:** unprotected downy mildew on foliage reached 35-69 % by site-year, powdery
  0.5-28 % (l. 241-246); the ranges are called typical of the 1995-2005 warning bulletins
  (unpublished, l. 608-609).
- **Models:** eq. 1, logistic leaf progress x_L(t) = 1/{1 + [(1 − x0)/x0] exp(−r t)} with
  r 0.01-0.11 per day (Table 4; e.g. downy mildew Couhins 2006 unprotected r = 0.052 ±
  0.004; l. 174, 409, 442); eq. 2, dx_C/dt = t_c x_L (1 − x_C), the cluster rate driven by
  foliage severity, t_c zero outside crop stages 2 to 5 (l. 145-163), fitted to 14 of 16
  cases, R² 0.75-0.99 for downy mildew, t_c 0.007-0.374 (ten times larger in 2007 than
  2006) and 0.039-1.269 for powdery mildew (l. 416-429, 475-494, 675); eq. 3, 70 logistic
  regressions of a cluster-severity threshold on foliage severity by date: for downy
  mildew at stage 4 and threshold 0 %, odds ratio 12.4 per percentage point (95 % bounds
  1.18-131) (l. 195-201, 508-509). r was lower under limited protection in all 15
  comparable cases (l. 775).
- **Cited:** cluster ontogenic resistance (Kennelly et al. 2005) excludes late foliage as a
  cluster source (l. 188-194); sexual-cycle inoculum through the season after Kennelly
  et al. 2007 and Gobbin et al. 2005 (l. 766).

## Dependence

- **Its own field data** and equations; no engine model is cited for a value or computed
  (the text names none of Rossi, Lalancette, Magarey, Goidanich). `fabre2024` reuses the
  sites and design.
- **Authors:** Savary and Willocquet wrote `bove2020`, `bove2021` (the Savary-type model
  structure): flags.

## Bearing (2026-10-13)

- A Bordeaux severity record with weather for four site-years, unprotected and sprayed:
  a pattern a truth's epidemic layer could be matched to, with the structural finding
  that cluster disease follows foliage disease within crop stages 2-5. Nothing for the
  engine's process models.
