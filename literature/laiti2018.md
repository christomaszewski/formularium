---
id: laiti2018
citation: Laiti, L., Giovannini, L., Zardi, D., Belluardo, G. & Moser, D. 2018. Estimating hourly beam and diffuse solar radiation in an Alpine valley: a critical assessment of decomposition models. Atmosphere 9:117
doi: 10.3390/atmos9040117
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 57 of 57 quotes found at their lines by the main session; Eqs 5-8 (p. 6) and Eq. 9 and Table 2 (p. 7) read in page images by the reading agent; Table 5 checked by the main session in the text layer; Table 1, Eq 7 and Table 5 re-read on the page images (pp. 5, 6, 10) on 2026-10-19 for the units of t and h
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

## The units of t and h (2026-10-19)

- **Printed nowhere in the paper.** Eq 7 names t "the apparent solar time" and h only by symbol
  (p. 6); Table 1's caption names them "local apparent time" and "solar elevation" (p. 5); Table 5
  has no units (p. 10). The only degree sign in the methods is the horizon profile's 1° resolution.
- **The sources were not obtained.** Ridley, Boland & Lauret 2010 (Renew. Energy 35:478, the BRL)
  and Lauret, Boland & Ridley 2013 (Renew. Energy 49:124, the brl.* values) are Elsevier; HAL lists
  both (hal-00919000, hal-00917859) without files.
- **Citing papers disagree** (each read only for its BRL passage): `kathilankal2014` restates
  Ridley's coefficients on sin β; `pashiardis2021` refits the BRL with AST in hours; `boland2025`, by
  a BRL author, names "Apparent Solar Time (AST), solar altitude" without units; `malu2023`
  (held) gives AST [h] and β [°] for a BRL-derived model.
- **It matters** (own calculation, kt 0.7, Kt 0.65, ψ 0.7, t 12): h = 60° gives kd 0.267 with the
  original coefficients and 0.205 with the local ones; h in radians gives 0.217 and 0.144.
- **Can it run:** not until the units are read at Ridley 2010 or Lauret 2013, or asked of the
  first author; the record's flag says so.

## The BRL's sources read (2026-10-22)

- **Ridley, Boland & Lauret 2010** (`ridley2010`, the in-press proof) states only the solar
  altitude's unit, degrees (l. 243). It does not state AST's (l. 246).
- **Lauret, Boland & Ridley 2010** (`lauret2010`, CS-BIGS 3:108-117, the BRL's earlier fit)
  does not state AST's unit in its text either. But its Fig. 1 (p. 114, read by the main
  session in the page image at 300 dpi) plots the model for "AST=8.5", "AST=12.5" and
  "AST=16.5", beside solar elevations α = 20, 40, 60.
  - **AST is in hours of the day,** centred near noon. The solar elevation is in degrees.
  - This is the authors' own figure, so the unit is inferred from their legend, not printed
    in words.
- **The coefficients are that fit's.** Laiti's "original" set (a0 -5.32, a1 7.28, a2 -0.03, a3
  -0.0047, a4 1.72, a5 1.08; Table 5) is printed as Lauret 2010's Eq. 10 on the same page as the
  figure: -5.32 + 7.28 kt - 0.03 AST - 0.0047 α + 1.72 KT + 1.08 φ, read in the page image.
  Ridley et al. 2010's least-squares set differs: -5.38, 6.63, +0.006, -0.007, 1.75, 1.31, with
  the signs read from its page image by the reader.
  - The record credits Lauret 2013, which was not read; it may reprint the 2010 fit.
  - Either way, the coefficients Laiti calls original are the ones whose authors plot AST in
    hours and α in degrees.
- **What it settles here:** Laiti's t in hours and h in degrees is the reading the BRL's
  authors use. Of the 2026-10-19 calculation, h = 60° with the original coefficients gives
  kd 0.267 and with the local ones 0.205.
  - Lauret 2013, with the brl.* values Laiti cites, is still not obtained.
  - Before clearing the record's flag, confirm that Laiti fitted with the same convention.
    Pashiardis 2021 and Malu 2023 also take AST in hours.

