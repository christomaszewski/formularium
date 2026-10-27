---
id: kuwagata1990
citation: Kuwagata, T., Sumioka, M., Masuko, N. & Kondo, J. 1990. The daytime PBL heating process over complex terrain in central Japan under fair and calm weather conditions. Part I: Meso-scale circulation and the PBL heating rate. Journal of the Meteorological Society of Japan 68(6):625-638
doi: 10.2151/jmsj1965.68.6_625
read: 2026-10-26, a targeted light reading (the radiation terms and the appendix formulas) by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; Eqs 8-20 and A2-A6 (printed pp. 628-629, 636) read in the page images by the agent, Appendix C-D (p. 636) also by the main session
status: read
diseases: []
crops: []
regions: [central Japan]
processes: [downward longwave radiation, precipitable water, solar radiation from sunshine, boundary layer heat budget]
records: [kuwagata1990.downward_longwave]
datasets: []
files: [kuwagata1990.pdf (the 2026-10-25 other-sources drop, from J-STAGE)]
---

# Kuwagata et al. 1990: the daytime boundary-layer heat budget, with Kondo's longwave formula in an appendix

A heat-budget study of the daytime boundary layer over central Japan from routine station
data on eight fair spring days. Read for its Appendix D: the empirical downward longwave
formula of Kondo, Nakamura & Yamazaki 1990 (Tenki, in Japanese, then in press), which
`kuwagata2024` cites for the effective radiation its dew model needs. The formula is printed
here with every coefficient.

## What it holds

- **Budget** (Eqs 8-10, l. 169-196): Q_s = Q_syn-adv + Q_local-adv + H + Q_rad + Q_con over
  0600-1500 JST (32400 s), Q_con zero in fair weather; T_v = T (1 + 0.608 q).
- **Radiation terms** (l. 251-327): Q_rad -27 W m⁻² over 0-3000 m from Katayama 1967; net
  radiation R_net = (1 - γ) S↓ + ε L↓ - ε σ T_s⁴ with γ 0.15 and ε 0.97 (Eq. 20); f_R 0.87;
  ΔT_s 5 °C assumed; σ 5.67e-8 W m⁻² K⁻⁴ (l. 569).
- **Solar from sunshine** (Eq. A2, p. 636): S↓/S_f↓ = 0.719 N/N0 + 0.281 for 0 < N/N0 ≤ 1,
  0.172 at N/N0 = 0, used at the 34 of 55 stations without a pyranometer (l. 637-639).
- **Clear-sky solar** (Eq. A3, p. 636; Kondo & Miura 1985, Kondo et al. 1990): needs the
  solar constant, not printed; turbidity B 0.02 and albedo 0.15 assumed; precipitable water
  log10 ω̄ = 0.0312 T̄_d - 0.0963 (Eq. A4), no source given.
- **Downward longwave** (Eqs A5-A6, p. 636): L↓ = σ T̄_a⁴ [1 - (1 - L_f↓/(σ T̄_a⁴)) c_d];
  L_f↓/(σ T̄_a⁴) = 0.74 + 0.19 x' + 0.07 x'², x' = log10 ω̄∞; c_d = 0.03 X_n³ - 0.30 X_n² +
  1.25 X_n - 0.04 with X_n = S↓total/S_f↓total; log10 ω̄∞ = 0.0315 T̄_d - 0.1836; T̄_a the
  daytime mean screen temperature (mean of 06 and 15 JST), ω̄∞ the effective precipitable
  water in cm, T̄_d the daytime mean dew point in °C.
- **Data and check** (l. 99-111, 341-342): 55 JMA stations, 281 AMeDAS sites, 8 aerological
  stations, eight spring days of 1986-1987; Q_s differs from radiosonde values by 73 W m⁻²
  day to day and 8 W m⁻² in the 8-day mean.

## Dependence

- **Computes** Kondo, Nakamura & Yamazaki 1990's solar and longwave formulas (credited at
  l. 316, 595, 629-639; the reference is "to be published", in Japanese, not held) and Kondo
  & Miura 1985's clear-sky solar; the heat budget is the authors' own. Kondo again
  (`kuwagata2024`, `kondo1996` cited there).
- No fit of its own to record: the formulas' data are Kondo's, not described here.

## Bearing (2026-10-26)

- For the sweep's longwave need (the 10-18 search and `kuwagata2024.canopy_dew`): a daytime
  downward-longwave estimate from screen temperature, dew point and the sunshine ratio as
  the cloud term, with coefficients; kin by form to `flerchinger2009.dilley_unsworth`. It is
  a daytime formula (mean of 06 and 15 JST): its use at night, where dew forms, is the
  reader's inference, not the paper's.
