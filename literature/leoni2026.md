---
id: leoni2026
citation: Leoni, S., Ruzzante, L., Fabre, A.-L., Kasparian, J., Wolf, J.-P. & Dubuis, P.-H. 2026. Climatic drivers of Plasmopara viticola oospore germination: integrating long-term monitoring into predictive modelling. OENO One 60(3), article 9963
doi: 10.20870/oeno-one.2026.60.3.9963
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5); every quote checked at its line by verify_quotes.py, key numbers checked by the main session; previously read 2026-10-07 by the session that recorded the engine's models
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland]
processes: [oospore maturation, oospore germination, primary infection]
records: [leoni2026.oospores, vitimeteo.oospores]
datasets: [leoni2026.changins]
files: [9963_Leoni_article_.pdf]
---

# Leoni et al. 2026: the GLM the engine runs for oospore maturity

## What it holds

- **Data:** oospore germination tests on Chasselas leaves at Changins (Nyon), systematic in
  2022-2024 (60 observations, 55 kept), plus 120 historical ones from 2004-2021: 175 in all.
- **Response:** MTG, the mean time to germination of a sample in the laboratory; oospores
  count as mature when MTG < 1.5 days, a threshold chosen against observed primary-infection
  dates in the field.
- **Phenology split:** before BBCH 13 rain and rainy days dominate the correlations (rho
  near -0.7), after it temperature, degree-days and VPD.
- **GLM (Table 1):** Poisson, log link, n = 96 before BBCH 13: intercept 2.36; cumulative
  precipitation since 1 January 0.00076 (p = 0.53; its unit not printed); rainy days since 1
  January -0.034 (p = 0.0041); degree-days above 8 °C since 1 January -0.0046 (p = 0.023).
  Null deviance 72.26 (df 95), residual 40.44 (df 92), AIC 307.68.
- **VitiMeteo's rule** as described: oospores mature at 140 degree-days above 8 °C from 1
  January; germination after 5 mm of rain in 48 h. Put into VitiMeteo-Plasmopara, the GLM
  placed primary infection right in 95 % of years against 80 %; median absolute error from 8
  to 4.5 days.
- Cites Rossi et al. 2002 (maturation stops with less than 5 mm of rain in three weeks) from
  the conference paper. Read 2026-10-09 ([rossi2002](rossi2002.md)): that paper prints no such
  rule. It correlates the first infections with March rain days and April's longest dry
  spell, and says nothing of maturation stopping. Leoni's citation is a misattribution.

## Dependence

- Shares degree-days above 8 °C from 1 January with VitiMeteo's rule, an input rather than
  an equation; the GLM replaces the 140 °C·day threshold inside VitiMeteo.
- Predictors, the BBCH 13 split and the MTG < 1.5 d threshold were chosen on the same data
  the model was scored on (no hold-out; the authors call for independent validation).

## Bearing (2026-10-09)

- Used by the engine (`leoni2026.oospores`); its published coefficients are now in the
  record. The fit and its tuning were done on the same Changins data, with no hold-out: a
  truth matched to Changins germination would share its data.
