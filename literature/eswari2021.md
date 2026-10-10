---
id: eswari2021
citation: Eswari, A. 2021. Weather based yield prediction and PDI model for grape production quality forecast in Tamil Nadu using mathematical modelling. International Journal of Current Microbiology and Applied Sciences 10(4):653-670
doi: 10.20546/ijcmas.2021.1004.066
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 53 quotes checked by scripts/verify_quotes.py; dependence judged by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Tamil Nadu]
processes: [forecasting, primary infection, infection]
records: []
datasets: []
files: [in_pdi_yield_2021_tamilnadu.pdf]
---

# Eswari 2021: weather regressions for yield and downy mildew PDI at Theni

## What it holds

- **Data:** 15 vineyards at Theni (Grape Research Station), four seasons of downy mildew
  incidence observed twice a week; season means 24.57, 28.03, 22.37 and 20.96 PDI.
- **PDI model (eq. 5):** PDI = 194.2031 - 3.7436 T - 0.8952 RH - 0.0059 rain; R² 0.484 from
  five yearly points and four parameters (one residual df). No coefficient is significant
  (t -0.670, -0.752, -0.091 against 12.706; F 0.312, p 0.828).
- **Validation:** called independent, on the same 2016-2020 years used to fit.
- **Infection rules, unsourced:** primary at 10 mm of rain in 24 h, 3 h of wetness and
  10 °C; secondary at RH above 92 % for 4 h and 13 °C. Wetness comes from RH and
  temperature by an unprinted formula.
- **Printed slips:** eq. 5 ends with the standard error (+3.839); eq. 6 drops the rainfall
  term the appendix fits; the appendix is not the pdex4 code the text names.

## Dependence

- No engine model is computed. The primary rule's numbers resemble the 3-10 rule's but no
  source is given. Caffi & Rossi 2010 is cited for a warning system, not computed.

## Bearing (2026-10-09)

- Not usable: the fit has no degrees of freedom to speak of. Recorded so that it is not read
  again.
