---
id: allen1998
citation: Allen, R. G., Pereira, L. S., Raes, D. & Smith, M. 1998. Crop evapotranspiration: guidelines for computing crop water requirements. FAO Irrigation and Drainage Paper 56. FAO, Rome
doi:
read: 2026-10-19, ch. 3 (atmospheric parameters, air humidity, radiation), ch. 4 (hourly time step, Example 19) and Annex 3 (atmospheric density), by the main session in FAO's HTML edition; Eqs 7, 8, 11, 13, 39, 3-5 and the hourly substitution read in their images
status: read
diseases: []
crops: []
regions: []
processes: [net longwave radiation, psychrometrics, saturation vapour pressure, reference evapotranspiration]
records: [allen1998.net_longwave, allen1998.psychrometrics]
datasets: []
files: [fao_toc.htm, fao_x0490e07.htm, fao_x0490e08.htm, fao_x0490e0k.htm (FAO HTML edition, open)]
---

# Allen, Pereira, Raes & Smith 1998 (FAO-56): net longwave radiation and the psychrometric constants

The lead Chris gave from memory for night net radiation, read at the source. The engine's
`fao56.eq47` (wind at 2 m) comes from the same document.

## What it holds

- **Eq 39** (ch. 3, image x0490e18): R_nl = σ[(T_max,K⁴ + T_min,K⁴)/2](0.34 − 0.14√e_a)(1.35 R_s/R_so −
  0.35), σ = 4.903 × 10⁻⁹ MJ K⁻⁴ m⁻² day⁻¹, R_s/R_so ≤ 1.0, T_K = T + 273.16. The humidity term
  "will be smaller if the humidity increases"; the cloudiness term "becomes smaller if the cloudiness
  increases". "Calibration of the coefficients in Equation 39 can be carried out" where longwave is
  measured. No source for the coefficients and no validation are printed in these chapters.
- **Hourly** (ch. 4): σT_hr,K⁴ replaces the mean, σ = 2.043 × 10⁻¹⁰ MJ m⁻² hour⁻¹. At night R_s/R_so is
  set to its value 2-3 h before sunset, the hour with (ω_s − 0.79) ≤ ω ≤ (ω_s − 0.52); "more
  approximate", 0.4-0.6 in humid and subhumid climates and 0.7-0.8 in arid and semiarid ones; 0.3
  "presumes total cloud cover".
- **Example 19** (N'Diaye, Senegal, 1 October, 02:00-03:00): 28 °C, RH 90 %, e° 3.780, e_a 3.402
  kPa, σT⁴ 1.681, (0.34 − 0.14√e_a) 0.082, R_s/R_so 0.8 assumed, R_nl = 0.100 MJ m⁻² hour⁻¹.
- **Psychrometrics:** Eq 7 P = 101.3((293 − 0.0065z)/293)^5.26; Eq 8 γ = c_pP/(ελ) = 0.665 × 10⁻³ P,
  λ 2.45 MJ kg⁻¹, c_p 1.013 × 10⁻³ MJ kg⁻¹ °C⁻¹, ε 0.622; Eq 11 e°(T) = 0.6108 exp(17.27T/(T +
  237.3)); Eq 13 Δ = 4098 e°/(T + 237.3)²; Eq 54 e_a = e° RH/100 hourly; Annex 3 ρ = 1000P/(T_Kv R) =
  3.486 P/T_Kv, R 287 J kg⁻¹ K⁻¹, T_Kv ≈ 1.01(T + 273).

## Dependence

- A guideline: its coefficients are credited to no paper in the passages read, so their data are not
  recorded. The engine's `fao56.eq47` is another equation of the same document, a reference piece:
  no dependence, a shared source.

## Bearing (2026-10-19)

- **Net longwave:** recorded as `allen1998.net_longwave` with `formularium.equations.allen1998`. It
  runs from the truth's weather, with R_s/R_so from the afternoon. It is the reference grass's net,
  not a canopy's, and FAO-56 prints no validation; Flerchinger et al. 2009's Dilley-Unsworth is the
  validated alternative.
- **Psychrometrics:** recorded as `allen1998.psychrometrics` (reference) with
  `formularium.equations.allen1998_psychrometrics`: one published source for the Δ, δ, λ, ρ and Cp
  that SWEB does not print. With them, SWEB's Eqs 1-14 reproduce its Fig. 1A and 1B.
