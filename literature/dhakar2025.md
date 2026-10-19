---
id: dhakar2025
citation: Dhakar, R., Amogi, B. R., Kothawade, G. S. & Khot, L. R. 2025. Simplified mechanistic model for estimating leaf wetness. Agricultural and Forest Meteorology 363:110399
doi: 10.1016/j.agrformet.2025.110399
read: 2026-10-19, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py; Table 2 and Eqs 3-11 read in the page images by the reading agent
status: read
diseases: []
crops: []
regions: [Washington]
processes: [leaf wetness duration, dew, rain interception, evaporation, wetness sensor]
records: [dhakar2025.leaf_wetness]
datasets: [dhakar2025.awn]
files: [1-s2.0-S016819232500019X-main.pdf (the 2026-10-19 drop, supplied by Chris 2026-10-19)]
---

# Dhakar et al. 2025: a simplified mechanistic leaf wetness model for a sensor plate

A lighter relative of SWEB (`magarey2006`): dew from an energy balance on a flat plate, rain capped
at 0.6 mm, evaporation as in SWEB, fitted to a dielectric wetness sensor at one station and
checked at ten.

## What it holds

- **Data** (Sect. 2.1-2.2, l. 147-196): ten AgWeatherNet stations, Washington State, 15-min,
  January 2019 to February 2023; PHYTOS 31 at 45°, raw counts 435 (dry) to 1100 (wet), normalised
  (counts - 435)/665, wet at 0.4 (701 counts); ATMOS 41 weather at 1.5-2 m. Mean recorded wetness
  0.62 +/- 0.27; wet events mostly midnight to 10:00 (about 50 %), 14 % in the hour after midnight.
- **M1** (Eqs 2-10): LW = Df + Ri - E for air above 0 °C. Dew Df from a heat balance on the plate with
  boundary-layer and stomatal-like resistances (Eqs 3-6); rain Ri capped at 0.6 mm per event
  (Sentelhas et al. 2006); evaporation E = Ep W with Ep from the Tanner & Fuchs combination equation
  and c = Wmax Cf + (1 - Wmax) Cd (SWEB's, l. 238-245, 265), a wind profile (Eq 9), and W = Wf x
  Wmax. Wet when LW > 0 mm; 15-min steps, daily duration = wet intervals / 4.
- **M2** (Eq 11): M1 with dew set to zero when the dew-point depression exceeds DPDc.
- **M3, M4:** DPD < 2.2 °C (1.8, 2.0 and 2.2 tried) and RH > 95 % (85, 90 and 95 tried; the 90 %
  result is not printed).
- **Parameters** (Table 2, Morris bounds then Bayesian value): alpha 0.5-2.0 -> 1.41; Cd 5-10 ->
  4.23; Cf 1-3 -> 1.78; DPDc 1.5-5.0 °C -> 1.85; Wmax 0-1 -> 0.718; Wf 0-1 -> 0.368; N 15e7-30e7 ->
  25e7 m-2; Dp 6-7 um -> 6.23; Lp 1-3 um -> 2.5. Fixed: Zref 0.2 m, Zc 0.15 m, plate 0.12 by
  0.07 m.
- **Fit:** Bayesian optimisation (scikit-optimize), maximising the F1 score, on Havillah alone.
- **Results:** abstract: M2 daily R2 0.84, RMSE 1.13 h, MAE 0.34 h. By station: M2 RMSE 0.76-1.95 h,
  MAE 0.2-0.81 h; M1 RMSE 0.76-2.14 h; M3 and M4 MAE 2.0-7.03 h and RMSE 4.53-10.16 h in the
  results text; M4 accuracy 75-80 %, M3 60-75 %. Slight underestimation of duration; soil, frost
  and snow not modelled. Morris ranking for dew: Tair, Tdew, wind, plate size, Lp, N, Dp.
- **Compared with:** SWEB MAE 1.5-1.8 h, Sentelhas 2006 about 1 h and Rao et al. 1998 1.8 h are quoted
  from the literature, not rerun. It needs no leaf area index (l. 483).
- **Data** on request; no code or licence (l. 459).

## Dependence

- **Computes** SWEB's evaporation module and c weighting (`magarey2006`); DPDc 2.2 °C from
  `sentelhas2008` (a value); the 0.6 mm cap from Sentelhas et al. 2006.
- **Fitted** to Havillah's sensor, which is also in the validation; the M3 and M4 thresholds were
  chosen on the same sensor data. Its Cd and Cf replace SWEB's lab values (8.7 and 2.0).
- Shared authors with SWEB: none (the authors are Washington State University's, AgWeatherNet's
  and ICAR-IARI's); the dependence is the borrowed equations and form.

## Conflicts and garbles

- Table 2's Cd 4.23 lies outside its printed bounds 5-10; DPDc is 1.85 °C in Table 2 and 2.2 °C
  in the text, and the paper does not say which M2 used; the text says the fitted values are in
  Table 1, they are in Table 2.
- The abstract gives M3 and M4 MAE as 10.16 and 7.03 h; the results give MAE 2.0-7.03 h and RMSE
  4.53-10.16 h, so the abstract's 10.16 h looks like an RMSE.
- The text cites Eq 9 for the Wmax-for-c choice where Eq 8 is meant. Wmax here is the sensor
  plate's wet fraction, not SWEB's canopy quantity. Fig. 8's caption calls the d-index the
  Nash-Sutcliffe efficiency. The sensor's output is called mV and raw counts.

## Bearing (2026-10-19)

- **It models a sensor, not a canopy.** A plate 0.12 by 0.07 m at 0.15 m over ground, no leaf area
  index; its numbers bear on how a wetness sensor behaves (the truth's observation of wetness),
  and on dew from an energy balance, not on a vine canopy's storage or interception.
  micro.storage_mm_per_lai, micro.density_drying_slowdown and micro.interception have nothing to
  compare with; the 0.6 mm cap per event is a sensor's, not LAI-scaled.
- **RH rule.** M4 uses RH > 95 % against the sensor; 90 % was tried and its result is not printed,
  so no verdict on the engine's RH >= 90 %. The empirical rules miss 2.0-7.0 h a day against the
  mechanistic model's 0.2-0.8 h (daily MAE, one sensor type, Washington State). That suggests
  an RH rule is poor at the daily scale at these stations, but the 90 % variant is not printed.
- **Dew.** Dew is gated on the air's dew-point depression being under DPDc (1.85 or 2.2 °C). The
  engine's dew needs a leaf cooled below the dew point (micro.leaf_cooling_c, 2.5 °C): different
  gates, and neither is tested here against a vine leaf (own reading).
- **Can it run:** the equations and Table 2 are printed, with the Cd and DPDc conflicts.
