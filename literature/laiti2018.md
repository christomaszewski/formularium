---
id: laiti2018
citation: Laiti, L., Giovannini, L., Zardi, D., Belluardo, G. & Moser, D. 2018. Estimating hourly beam and diffuse solar radiation in an Alpine valley: a critical assessment of decomposition models. Atmosphere 9:117
doi: 10.3390/atmos9040117
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 57 of 57 quotes found at their lines by the main session; Eqs 5-8 (p. 6) and Eq. 9 and Table 2 (p. 7) read in page images by the reading agent; Table 5 checked by the main session in the text layer
status: read
diseases: []
crops: []
regions: [Bolzano, Adige Valley, Italy]
processes: [diffuse fraction, decomposition models, solar radiation separation, sky view factor, complex terrain]
records: [laiti2018.brl_bolzano]
datasets: [laiti2018.bolzano]
files: [lavinia_2018.pdf (the 2026-10-18 drop)]
---

# Laiti et al. 2018: decomposition models in an Alpine valley

Thirteen published hourly separation models (and three locally recalibrated) tested against
four years of measured direct and diffuse irradiance at Bolzano airport.

## What it holds

- **Station** (l. 152-174): Bolzano city airport, 46.458 °N, 11.329 °E, 265 m, 2011-2014; two
  CMP11 pyranometers (global and diffuse) and a pyrheliometer for direct; 1-min data to
  15 min to hourly; horizon at 1° azimuth; sky view factor 0.788; ESRA clear-sky model with
  Linke turbidity 1.5. 10,310 valid hours (solar elevation 7° or more, shadowed hours
  excluded for the validation); 2,098 hours are orographically shadowed.
- **Result** (abstract, conclusions): the literature models average about 27 % (diffuse) and
  14 % (beam) MAE, RMSE about 37 % and 20 %; the locally calibrated logistic model BRL-loc.
  reaches 20 % and 12 %, rMBE 0.00 % and rRMSE 32.29 % for diffuse (Table 3). Literature models
  overestimate diffuse (often above 10 %) and underestimate direct (often above 5 %).
- **Erbs 1982** (Table 3, l. 430): diffuse rMBE 7.35 %, rMAE 26.95 %, rRMSE 37.23 %, R 0.817;
  direct (Table 4) rMBE -4.18 %, rRMSE 21.20 %. Its equation is not printed here.
- **Shadowed hours:** diffuse MBE 27 % against 7 % unshadowed, RMSE 50 % against 37 %;
  direct MBE -21 % against -3 %. The observed kd is up to 18 % below a flat-terrain value at
  kt about 0.8 (Eq. 9, a sky-view-factor rescaling after Ridley et al.).
- **BRL** (Eq. 7, Lauret et al. 2013): kd = 1 / (1 + exp(a0 + a1 kt + a2 t + a3 h + a4 Kt +
  a5 psi)), with t apparent solar time, h solar elevation, Kt the daily clearness index and
  psi the persistence index of Eq. 8. Table 5 (l. 498-508), original and local (Bolzano):
  a0 -5.32 / -6.67, a1 7.28 / 6.72, a2 -0.03 / 0.06, a3 -0.0047 / -0.0072, a4 1.72 / 2.01,
  a5 1.08 / 2.47. Table 5 also gives RUIZ-I (four coefficients) and RUIZ-II (seven).
- **Local fit:** robust least squares with a null MBE on the same 10,310 hours that validate
  it; no hold-out is stated.
- **Disagreement:** Table 1 cites RUIZ-II as [15] (Reindl et al. 1990); the reference list
  gives Ruiz-Arias et al. 2010 (ref 18).
- **Not printed:** the equations and coefficients of the other literature models (Erbs, Orgill,
  Reindl, Louche, Torres, DISC, Skartveit, DIRINT); data release or licence.

## Dependence

- **Borrows** the BRL form (Lauret et al. 2013) and the Ruiz-Arias et al. 2010 forms,
  refitted to Bolzano. The persistence index psi is shared by DIRINT, Skartveit II and BRL.
- **Data:** its own station (EURAC). Used by others: DIRINT and BRL in Meteonorm, RUIZ-I in
  HelioClim, Skartveit I in HelioMont.

## Bearing (2026-10-18)

For the sweep's radiation inputs and for valley sites:

- **What it offers:** a measured hourly error for Erbs (rRMSE 37 % for diffuse, 21 % for direct)
  in a narrow valley, and a logistic form with printed original and local coefficients.
  Shadowed hours inflate diffuse bias fourfold, so a separation fitted on open sites
  overstates diffuse in a valley.
- **Limits:** one station and four years; the local fit is in-sample; no humidity or wetness.
- **Take:** a site-level error band for the diffuse fraction on a hillside vineyard; the local
  coefficients are Bolzano's and not for other places.
