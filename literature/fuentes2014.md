---
id: fuentes2014
citation: Fuentes, S., Poblete-Echeverría, C., Ortega-Farias, S., Tyerman, S. & De Bei, R. 2014. Automated estimation of leaf area index from grapevine canopies using cover photography, video and computational analysis methods. Australian Journal of Grape and Wine Research 20(3):465-473
doi: 10.1111/ajgw.12098
read: 2026-10-28, leaf angle, extinction, porosity and light measurements; by a reading agent and note writer (claude-sonnet-5-5); 7 of 7 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Chile, South Australia]
processes: [leaf area index, cover photography, canopy porosity, clumping index]
records: []
datasets: []
files: [dr1028_fuentes2014.pdf (the 2026-10-28 requests drop)]
---

# Fuentes et al. 2014: LAI, porosity and clumping of vines from cover photographs and video

Cover-photograph LAI with automated analysis in Merlot (Chile) and Chardonnay (South Australia), checked against allometric LAI and LAI-2000. The method is that of debei2016 (VitiCanopy).

## What it holds

- **Equations** (l. 199, 207, 218-219): ff = 1 - tg/tp; Phi = 1 - ff/fc; LAI_M = -fc ln(Phi) / k with k = 0.7 (Herwitz et al. 2004) and a clumping index at zenith Omega(0).
- **Clumping** (l. 331, 348): Omega(0) = 0.986 (Chile Merlot) and 0.976 (Chardonnay DDRE), so LAI_M = effective LAI.
- **Method** (l. 209): nadir photographs 3.9 m above ground.
- **Not printed:** values of Omega by stage; hedgerow beam clumping.

## Dependence

- Same algorithm as debei2016. Borrows Macfarlane et al. 2007 and Herwitz et al. 2004 (k).

## Bearing

- k = 0.7 is assumed, not measured. Omega near 1 is for nadir views and does not give a row factor for oblique beams.
