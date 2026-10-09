---
id: anderson2007
citation: Anderson, Martha C., Norman, John M., Mecikalski, John R., Otkin, Jason A. & Kustas, William P. 2007. A climatological study of evapotranspiration and moisture stress across the continental United States based on thermal remote sensing: 1. Model formulation. Journal of Geophysical Research 112 (Atmospheres, D10):D10117 (article number; 17 pages)
doi: 10.1029/2006JD007506
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 34 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [United States]
processes: [evapotranspiration, surface energy balance]
records: []
datasets: []
files: [Journal of Geophysical Research  Atmospheres - 2007 - Anderson - A climatological study of evapotranspiration and moisture.pdf]
---

# Anderson et al. 2007: ALEXI, model formulation for continental ET

From USDA-ARS (Beltsville), the University of Wisconsin and the University of Alabama in Huntsville.

## What it holds

- ALEXI deduces ET from the morning rise in radiometric temperature seen by GOES, using the series two-source TSEB of Norman et al. 1995 (l. 107) and a slab boundary-layer closure (l. 177). It works only under clear sky, about 30% of days (l. 314).
- T_RAD = f T_C + (1-f) T_S (l. 115); canopy transpiration is a Priestley-Taylor term with alpha_C 1.3 (l. 791); G = 0.31 R_NS (l. 786). t1 = 1.5 h and t2 = 5.5 h after sunrise (l. 172); z1 = 50 m (l. 875).
- The new part is a cloud filler: root-zone and surface water pools are set on clear days by inverting a logistic stress curve with Wf = 800, m = 12 (l. 253), then run forward on cloudy days. The curve matches a qualitative summary, not a fit (l. 236).
- Daily totals use EF = 1.1 lE2/(R_N2 - G2) (l. 898).
- Validation: 10 eddy-covariance towers, Walnut Creek, Iowa, DOY 167-189 of 2002 (l. 562), closure-corrected (l. 573). Gap-filled hourly lE RMSD 60 W m-2, 19% (l. 569; Table 4 prints 58, l. 707); clear-sky points 30 W m-2, 10% (l. 572); daily ET 1.7 MJ m-2 d-1, 11% (l. 576).
- Worst days: undetected cloud and warm-air advection (l. 609).
- Nothing on canopy wetness or interception; it is a field-scale ET method.

## Dependence

- It computes the two-source energy balance of Norman et al. 1995, Priestley-Taylor and a slab boundary layer; validated on SMEX02 towers in Iowa.
- No author of an engine model.

## Bearing (2026-10-08)

- Clear. Its two-source equations (canopy and soil temperatures from radiometric temperature) are printed in full: what a truth would need to make leaf temperature from the energy balance, as ALEX does for wetness.
