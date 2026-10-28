---
id: magarey2006
citation: Magarey, R. D., Russo, J. M. & Seem, R. C. 2006. Simulation of surface wetness with a water budget and energy balance approach. Agricultural and Forest Meteorology 139:373-381
doi: 10.1016/j.agrformet.2006.08.016
read: 2026-10-19, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 38 of 38 quotes found at their lines by scripts/verify_quotes.py; pp. 375-377 (Eqs 1-15, Table 2 lines) checked in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [New York, Geneva, Adelaide]
processes: [leaf wetness duration, SWEB, canopy water balance, dew, rain interception, energy balance]
records: [magarey2006.sweb]
datasets: []
files: [1-s2.0-S0168192306002371-main.pdf (the 2026-10-19 drop, supplied by Chris 2026-10-19)]
---

# Magarey, Russo & Seem 2006: SWEB, a surface wetness model from a water budget and an energy balance

The main paper of the SWEB model that `kim2005`, `dallamarta2006`, `gil2015` and `kudinha2014`
run or cite. Its companion, `magarey2006b`, holds the vineyard comparison.

## What it holds

- **Structure** (l. 28, 83-111): a big-leaf canopy at mean canopy height, four modules:
  surface distribution, water budget, energy balance and a transfer coefficient.
- **Wetness** (Eqs 1-2, l. 148-153): the canopy is wet when the index of wet surface area
  Wind exceeds a threshold Wth = 0.1 "of leaves or other plant units". Not a humidity rule.
- **Surface distribution** (Eqs 3-5): Wind = (S/C)^0.67 (S water stored, C capacity); the actual
  wet fraction is W = Wind x Wmax, with Wmax = p Wf + (1 - p) Wd for wettable and
  non-wettable leaves. Wmax = 0.5 for grapes, "since tests in the lab showed immature grape
  leaves are highly wettable and mature leaves are non-wettable" (l. 229). Wf, Wd and p are not
  printed.
- **Water budget** (Eqs 6-8): C = LAI x Cl, Cl = 0.02 cm per unit leaf area, "a commonly
  accepted value" credited to Noilhan & Planton 1989 (l. 187); it depends on age and species
  (Hall et al. 1997). The same paper says one grape study found 0.018 (Hoppmann & Wittich 1997)
  and the authors' own preliminary lab studies 0.02 (unpublished; p. 378). Storage S = I + Dp -
  E; rain intercepted as I = (1 - exp(-0.5 LAI)) P (Eq 8, after Norman & Campbell 1983).
- **Energy balance** (Eqs 9-15): Tanner & Fuchs 1968's combination formula (l. 110), evaporation
  E = Ep W (Eq 11), by day from the aerodynamic term only (net radiation ignored: the first sunlit
  layer absorbs 94 % of the solar radiation, l. 122); at night dew Dp = Delta/(lambda (Delta +
  delta)) x 0.5 Rnc (Eq 12), the canopy mid-height flux being half the total (l. 298). Transfer
  coefficient h = c Uc^0.5 with c = W cf + (1 - W) cd (Eqs 13-14), cd = 8.7 and cf = 2.0 from
  controlled tests on an artificial leaf (Magarey et al. 2005a, `magarey2005b`); canopy wind Uc from a
  log profile with a = 1.3, roughness length Z/10 and displacement 2/3 Zc (Eq 15).
- **Inputs:** canopy air temperature and humidity at canopy height, rain above the canopy, wind
  above the canopy, canopy net radiation (night only) (l. 110-115).
- **Sensitivity** (Sect. 3, Fig. 1, l. 324-341): run at 20 °C, 75 % RH, 1.5 m/s, 2 mm of rain in
  the first 10 min, 10-min steps, net radiation zero. LAI and Wmax matter most. LAI 1 to 4:
  130 to 650 min (text; Fig. 1A reads about 150 to 640). Wmax 0.2 to 1: 670 to 110 min (text; the
  figure puts 670 at Wmax 0.1 and about 340 at 0.2, so the text range is shifted). Crop height
  matters little at vine heights (Fig. 1C about 240 to 140 min over 0.1 to 2 m). Cl matters
  little above 0.01 (Fig. 1D). Figure values are read by eye, about +/- 10 min.
- **Validation** (Sect. 4, Table 3): visual wetness (15 tagged leaves per vine, 3 vines, 5 canopy
  positions) at Geneva NY 1997 and 1998 and Adelaide 1998. SWEB mean 6.3, 5.5 and 1.2 h
  (visual 6.9, 5.1 and 2.0 h, from `magarey2006b`); mean absolute error 1.5, 0.8 and 0.7 h.
  The text gives 1.5-1.8 h and 0.9 h (l. 366-368): it conflicts with the table. The table's
  mean-error sign for 1998 is a minus on the page image that the text layer drops.
- **Leaf wettability** can change drying time by up to 8 h (Huber 1988, cited, l. 425); Wmax
  0.06 to 0.2 for some species (Brain & Butler 1985; Norman & Campbell 1983, cited).
- **Authors' remark** (l. 445): at LAI 1.0 even 0.5 mm of rain nearly saturates the canopy
  (from Eq 8).
- **Code:** available on request from the first author; no licence (l. 425).
- **Not printed:** Wd, Wf and p; the symbol whose value depends on crop type (l. 311, blank in
  the text and the page image); the operational time step; any comparison with an RH threshold;
  (an earlier version also listed "consistent units for Eqs 9-10"; the units are consistent:
  see the record, checked 2026-10-19 against magarey2005chapter).

## The 94 % (2026-10-28, for Agrarium D61)

- The "94 %" is on printed page 375 (the left-hand text under the page header "375"), not 377: "the first sunlit leaf layer in a grape canopy absorbs 94% of the incoming solar radiation (Smart and Robinson, 1991)". It is the stated reason for ignoring net radiation by day (third assumption). No number or figure of the SWEB paper tests it.
- Smart & Robinson 1991 is the handbook "Sunlight into Wine" (Hyde Park Press, Adelaide, 88 pp as the reference list prints it); no open copy found, so what it says is not read. A web search found no passage with 94 %.
- A likely origin, my inference and not read: `smart1990` (l. 98-101) says only about 6 % of PAR (400-700 nm) is transmitted by a leaf (Smart 1987b), so 94 % of PAR is not transmitted. That is not-transmitted, not absorbed (reflectance of the leaf is in it), and it is PAR, not total solar radiation. Measured leaf PAR reflectance and transmittance in `mabrouk1997` Table 1 are 12.2 % and 8.1 % (absorbed about 80 %); Riou et al. 1989 use 0.20 reflection for all wavelengths (5 % visible, 40 % near infrared).

## Dependence

- **Borrowed, none in the catalogue:** Tanner & Fuchs 1968 (energy balance), Bird et al. 1960
  (transfer coefficient), Norman & Campbell 1983 (interception), Noilhan & Planton 1989 (Cl),
  Deardorff 1978 (Eq 3, per the reading), Monteith & Unsworth 1990 and Landsberg & James 1971
  (wind profile). All credited, not read here.
- **Calibration:** cd and cf were fitted to the controlled tests of Magarey et al. 2005a
  (`magarey2005b`), whose data are not reproduced here. The visual observations are the
  validation, not a fit; no model produced them.
- **Authors:** the same people wrote `magarey2005b` and `magarey2006b`: a flag, not a dependence.
  `dhakar2025` computes SWEB's evaporation module and c weighting (`borrows`).

## Bearing (2026-10-19)

For the truth's wetness, against the assumed micro.* parameters and the engine's RH >= 90 %
stand-in:

- **Not an RH rule.** Wetness here is the wet-area index above 0.1. No comparison with an RH
  threshold is printed. As stored water (own calculation): S/C > 0.1^(1/0.67) = 0.032, which is
  0.0064 mm at LAI 1.0 and 0.013 mm at LAI 2.0 with Cl = 0.2 mm per LAI. micro.wet_threshold_mm
  (0.02 mm, range 0.005-0.05) is the same order.
- **Storage.** Cl = 0.02 cm is 0.2 mm per unit LAI; micro.storage_mm_per_lai is 0.25 (0.1-0.5).
  Grape lab values in `magarey2006b` are 0.016 to 0.022 cm.
- **Interception.** 1 - exp(-0.5 LAI) is 0.39 at LAI 1, 0.63 at 2, 0.78 at 3 (own
  calculation). micro.interception (0.6, range 0.3-0.9) equals it near LAI 1.8, and is constant
  where SWEB's rises with LAI.
- **Density.** SWEB's LAI effect is all storage and interception (wetness 130 to 650 min for LAI 1
  to 4, text). It has no separate density term, so micro.density_drying_slowdown (0.4 per unit
  LAI above 1) has no counterpart; with storage already scaling with LAI, it may count density
  twice (own reading).
- **Dew.** Night only, from half the canopy net radiation. At -100 W m-2 (assumed, not printed)
  and Delta/(Delta + gamma) near 0.7 the ceiling is about 0.05 mm per hour (own calculation).
  micro.dew_rate_mm_h_per_c (0.05 mm/h per °C) times micro.leaf_cooling_c (2.5 °C) is 0.125 mm/h,
  above that ceiling. SWEB has no leaf-cooling or dew-point input; its dew is set by radiation.
- **Errors.** 0.7-1.5 h a day against visual wetness at three site-years (table), canopy
  humidity and temperature measured in the vineyard. A truth built on SWEB needs canopy net
  radiation at night, which a weather generator without longwave cannot give.
- **Can it run:** from this paper with stated choices; see the record's flags (completed 2026-10-19 on branch ingest/sweb-complete: Wmax set directly, the units of Eqs 9-10 consistent at a second source, 10-min steps in the sensitivity runs, hourly in the validation and every later use).

## Equations module (2026-10-19)

- Eqs 1-15 re-read on the page images (pp. 375-377; Eq 15 at 300 dpi) and computed as printed in
  `formularium.equations.magarey2006`, with Table 1's order for the budget.
- **Eq 15 as printed is not dimensionally sound:** [1 + α((1 − Zc)/Z)]⁻² with Zc and Z in cm. At
  Zc 150 cm and Z 200 cm it makes Uc 574 times U_Z; at Zc 50 cm the log ratio is negative. `amir2016`
  (Eq 24) and `dhakar2025` (Eq 9) print the same form.
- **Fig. 1 checks the rest** (own calculation, FAO-56's constants): the sensitivity case dries in one
  10-min step with Eq 15 as printed, against about 150 min in Fig. 1A. With the canopy wind set to
  0.3 U_Z (by trial), Eqs 1-14 give 150, 320, 480, 650 min for LAI 1-4 (Fig. 1A about 150, 310, 480,
  640) and 680, 350, 180, 110, 110 min for Wmax 0.1-1.0 (Fig. 1B about 670, 340, 180, 110, 110).
  Fig. 1C asks for a canopy wind about three times larger at Zc 2 m than at 0.1 m. Fig. 1D cannot be
  reproduced: the printed budget makes the wet time proportional to Cl.
- **Eq 12's sign:** Dp has Rnc's sign and Eq 7 adds it; no sign convention is printed. The module
  adds condensation when Rnc < 0 (Eq 9's convention), a reading.
- **Can it run:** not as printed: Eqs 1-14 run; the canopy wind does not, and no source read prints
  one that closes. Net radiation at night now has recorded estimates (`flerchinger2009`, `allen1998`).

## Eq 15 against Fig. 1C (2026-10-27)

For Agrarium D56 (literature/requests/sweb-canopy-wind-d56.md), read in the page images of
pp. 377-378.
- **Eq 15 as printed:** Uc = U_Z (ln[(Zc − D_Z)/Z0] / ln[(Z − D_Z)/Z0]) [1 + α ((1 − Zc)/Z)]^−2,
  with Uc the wind at the canopy's average height, Zc the canopy height, U_Z the wind at the
  reference height Z (cm, cm/min), D_Z = 2/3 Zc, Z0 "1/10Z", α = 1.3, chosen as intermediate
  between wind along and across the rows (Heilman et al. 1994) and "also dependent upon crop
  type".
- **Fig. 1C** is not a wind curve: it plots the simulated wetness duration against Zc (0.1 to
  2 m): about 240, 230, 200, 185 and 140 min, read by eye. The sensitivity case is 20 °C, 75 %,
  U_Z 1.5 m/s, 2 mm of rain; the reference height Z is not printed.
- **What Fig. 1C asks of the canopy wind:** run through Eqs 1-14 (Formularium's module), 0.13,
  0.14, 0.18, 0.19 and 0.33 U_Z at those heights, about 2.5-fold.
- **No reading reproduces it within 20 min.** `1 − Zc/Z` gives 430, 390, 330, 260 and 160 min
  (Z0 = Zc/10, Z 3 m); with Z0 = Z/10, as printed, the wind of canopies below about 0.6 m is
  negative. Landsberg & James's form [1 + α(1 − z/Zc)]^−2, at mid-canopy, gives 300, 280,
  240, 210 and 140 min (Z 2 m). The test `test_fig_1c_is_not_reproduced_by_any_reading_of_eq_15`
  keeps the check. Landsberg & James 1971 was not obtained.

## Bearing (2026-10-27)

- As D56 says for this case: Agrarium takes the canopy wind from measurements (0.35-0.5 of the
  wind above in three vineyards), registered `estimate`. Fig. 1C's own runs imply a lower wind,
  0.13-0.33 U_Z.

