---
id: cheraiet2021
citation: Cheraïet, A., Naud, O., Carra, M., Codis, S., Lebeau, F. & Taylor, J. 2021. Predicting the site-specific distribution of agrochemical spray deposition in vineyards at multiple phenological stages using 2D LiDAR-based primary canopy attributes. Computers and Electronics in Agriculture 189:106402
doi: 10.1016/j.compag.2021.106402
read: 2026-10-26, in full from the HAL author manuscript, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; Eqs 3-9 (pp. 12-16) and Tables 4 and 6 (pp. 19, 22) read in the page images by the agent, the tables also by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Hérault]
processes: [spray deposition, canopy size, leaf wall area, LiDAR]
records: [cheraiet2021.deposit_deciles]
datasets: [cheraiet2021.herault]
files: [cheraiet2021.pdf (the 2026-10-25 other-sources drop)]
---

# Cheraïet et al. 2021: spray deposit deciles from LiDAR canopy size

Tracer deposits on collectors through nine vineyard plots and four stages a year, 2016 and
2017, give the deciles of the deposit distribution; each decile falls exponentially with
leaf wall area (nine univariate fits) or with canopy height, width and beam interception
(nine multivariate fits), calibrated on 2017 and validated on 2016.

## What it holds

- **Trials** (l. 305-326, 344-364, 1393): 2016 at Mas Piquet (Grabels, four plots) and 2017
  at Domaine Chapitre (Villeneuve-lès-Maguelone, five plots), seven varieties, four surveys a
  year from BBCH 14 to 85 (the abstract says eight fields, l. 61).
- **Sprayer and tracer** (l. 370-387, 417-481): Precijet at 0.5 MPa, 5.5 L/min, 5 km/h,
  150 L/ha; tartrazine read at 427 nm on PVC collectors of 0.004 m², a 0.4 m by 0.1 m grid in
  2017.
- **LiDAR** (l. 566-580, 610-620): SICK LMS100, 541 beams a scan at 50 Hz, ±30 mm; canopy
  height and width by a Bayesian point-cloud classifier; IBR = NBI/NBE × 100 (Eq. 3,
  l. 648); LWA = 2 VH × 10,000 / RS (Eq. 4, l. 685).
- **Models** (l. 733-774): decile j of deposit y_ij = U_j exp(-λ_j LWA_i) (Eq. 5) and
  y_ij = M_j exp(-(α_j VH_i + β_j VW_i + γ_j IBR_i)) (Eq. 6); called log-linear, printed as
  exponentials; the fitting method is not stated. Variables chosen stepwise by AICc with
  VIF below 5 (l. 337-340, 792).
- **Calibration 2017 (n 40), validation 2016 (n 16)** (l. 717, 1042, 1214): univariate
  R² 0.69-0.82 in calibration and 0.66-0.85 on validation (Table 4); multivariate R²
  0.81-0.93 in calibration, validation nRMSEp 10-24 % and bias -1.5 to -3.2 % (Table 6, the
  model underestimates every decile).
- **Coefficients** (Tables 4 and 6, page images): the record holds all 54; D1 U 740.6,
  λ 2.35e-4; mean model U 1789.88, λ 2.40e-4; D5 M 2055.62, α 0.55, β 0.34, γ 1.81.
- **Discrepancies:** the abstract's R² 0.76 against Table 6's 0.79; Fig. 3's 0.79 against
  Table 4's 0.80 for D5; reference years that differ from the text.

## Dependence

- **Fitted to** `cheraiet2021.herault`: observed deposits and scans, no model in the data.
  The tracer method is credited to Codis et al. 2018 (l. 471).
- **Builds on** the leaf wall area dose metric (EPPO 2016) and the LiDAR indicators of the
  same group (Cheraïet 2019, 2020); the held cheraiet2024 and codis2024 notes credit this
  paper with the sampling protocol and indicators, which it does print (l. 168-200, 257-297).

## Bearing (2026-10-26)

- For Agrarium's fungicide-protection strand (the 10-20 search): a printed, validated
  deposit-against-canopy rule by decile, a new form (`canopy-deposition-decay`), kin to
  nothing the engine runs. The deposit a leaf gets as the canopy grows is what a protection
  model needs; the deciles give the spread, not only the mean.
