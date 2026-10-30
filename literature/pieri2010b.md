---
id: pieri2010b
citation: Pieri, P. 2010. Modelling radiative balance in a row-crop canopy: Cross-row distribution of net radiation at the soil surface and energy available to clusters in a vineyard. Ecological Modelling 221(5):802-811
doi: 10.1016/j.ecolmodel.2009.07.028
read: 2026-10-30, in full; Eqs 1-21 and Figs 1-8 read in page images (pp. 803-809), Eqs 11-12 also at 300 dpi; by a reading agent and note writer (claude-sonnet-5-5); 54 of 54 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Bordeaux, Medoc]
processes: [net radiation, shadow of a row, row porosity, view factors, longwave radiation, diffuse radiation, soil albedo, cluster zone energy]
records: []
datasets: []
files: [dr1030_pieri2010b.pdf (the 2026-10-30-missing drop, from Chris)]
---

# Pieri 2010 (cross-row): net radiation at any point of the inter-row, and at cluster height, from row shadows and view factors

The second paper by page order (it was accepted 2009-07-21, the other 2009-11-20, and the other cites it as "in press"). It replaces the whole-soil average with a position x between two rows: a sunlit-or-shaded function delta(x) from the row's shadow, three porosity zones in the row, point view factors for the diffuse and longwave light, and a diffuse-fraction fit. Validated at the height of the radiometers, 0.27 m, taken as cluster height.

## What it holds

- **Balance** (Eqs 1-5, p. 803): Rns = RS down - RS up + RL down - RL up; shortwave net (1 - a) RG,soil with vegetation reflection neglected; RL down = A eps_v sigma Tv^4 + B Ra; RL up = (1 - eps_s) RL down + eps_s sigma Ts^4; so Rns = (1 - a) RG,soil + eps_s (A eps_v sigma Tv^4 + B Ra - sigma Ts^4). Emissivities are not given a value in this paper (0.98 in Paper I).
- **Soil albedo** (Eqs 6-7, p. 804): a = alpha1 beta + alpha2 exp(-alpha3 beta), beta the solar elevation in degrees (Llasat & Snyder 1998); at the site a = 0.001 beta + 0.3 exp(-0.021 beta).
- **Row shadow** (Eqs 8-12, Fig. 1, p. 804): parallelepiped row, spacing D, width L, top height h1, base height h2. phi = phi_s - phi_r; d1 = h1 sin(phi)/tan(beta) and d2 = h2 sin(phi)/tan(beta). Shade limits x1 and x2 (Eqs 11-12) are printed as impossible fractions; the case rules (A-C) fit x1 = D - L/2 - d1 and x2 = D + L/2 - d2 modulo D (our reading). Shaded for x > x1 or x < x2; whole inter-row shaded below a limit elevation beta_L.
- **Shortwave at x** (Eq. 13): (RS down - RS up)(x) = (1 - a)[Rd + (RG - Rd) delta(x)]. delta = 1 sunlit, = p where the beam crosses foliage, 0 if opaque.
- **Porosity** (Sec. 2.3, Figs 2-3, p. 805-806): from pictures of the shadow on the soil, in five strips cut by the beams tangent to two ellipses; three regions of constant projected gap fraction p = 0.2 (core), 0.5, 0.7 (outer) (Fig. 3, page image); p = 0 for solar elevation above 65 deg (l. 284); leaf density highest at the row centre, after Schultz 1995. Mean P-bar for diffuse light 0.25 (l. 328).
- **View factors** (Eqs 14-16, Fig. 4): RL down = F_soil,v eps_v sigma Tv^4 + F_soil,sky Ra; F_soil,v(x) = 1/2 (sin Phi1 - sin Phi2) for an infinite strip (Ozisik 1981); F_soil,sky = 1 - F_soil,v. Phi2 = pi/2 for the next row in the same direction and for the nearest row in the opposite direction. F_soil,v about 0.7 between 0.2 and 1.1 m, higher under the rows (Fig. 4B). Phi1 and Phi2 are defined only in Fig. 4A.
- **Diffuse** (Eqs 18-19): Rd/RG = min(1, 1.09 - 2.44 (RG/RG0)^2 + 1.084 (RG/RG0)^3), RG0 extraterrestrial. Rd,soil(x) = (P-bar F_soil,v + (1 - F_soil,v)) Rd.
- **Full model** (Eqs 17, 20, p. 806-807): Rns(x) = (1 - a)[(P-bar F + (1 - F)) Rd + (RG - Rd) delta(x)] + eps_s (F eps_v sigma Tv^4 + (1 - F) Ra - sigma Ts^4(x)). Eq. 17 has eps_sky sigma Tsky^4 where Eq. 20 has Ra: the same thing.
- **Atmosphere** (Eq. 21, p. 807): Ra = (1 - 0.261 exp(-7.77e-4 Ta^2)) sigma Ta^4, Idso & Jackson 1969, Ta at 6 m. As printed, with Ta in K the exponential is exp(-64) and emissivity 1 (arithmetic, not printed): the original takes (Ta - 273.16)^2. Code it that way.
- **At sensor height** (Sec. 2.7): the shadow at 0.27 m is found by changing h1 and h2; upward fluxes see the whole soil of three inter-rows, with beams through foliage weighted by porosity; soil temperature taken as the lower or higher of the two nearest measured values in shade or sun. Height effect on shortwave up to 350 W m-2 (over) and more than 500 (under), 600 at position 1; on longwave up to 100 W m-2.
- **Site** (Sec. 3): Chateau Talbot, Medoc (45 deg 10' N, 0 deg 45' E), 1997 (days 202-232), Merlot on 3309, 7 years, Guyot double cordon; vines 1 m, rows 1.3 m (7700/ha), nearly N-S; base of foliage 0.4 m, "vegetation height" 1.3 m, width 0.4 m; LAI 2.3 (12 plants). Rg at 6 m (CIMEL CE 180). Five Crouzet net radiometers at 0.27 m at 0.08, 0.27, 0.65, 1.03, 1.17 m from the west row, on a tram at 2 m/min on a 12 m rail. Soil temperature at 0, 0.3, 0.6, 0.9, 1.2 m from the west row, depths 0.01-0.35 m and 1 m. Air temperature T-type at 0.5 m mid inter-row; leaf temperature taken as air (error below 15 W m-2).
- **Validation** (Figs 7-8, p. 808-809): 30 min, days 210-215, n = 260 (Fig. 8) and days 212-214 (Fig. 7); calculated against measured y = a x + b, r2: position 1 0.78x - 9.9 (0.78); 2 0.98x + 2.9 (0.92); 3 0.93x + 13.9 (0.95); 4 1.02x + 5.2 (0.91); 5 0.93x - 0.6 (0.86) (page image). Position 1, under the west row, underestimated by up to 200 W m-2 (about 20 %), put down to the gap fraction at the row base; positions 2-5 "excellent", deviations below radiometer accuracy; night and the cloudy day 212 "perfect". No RMSE or MAE printed.

## Dependence

- Own shadow and view-factor equations in the family of Riou et al. 1989 (`riou1989.row_interception`), Annandale 2004 and Oyarzun 2007; it replaces Riou's interception with shadow geometry and does not restate Riou's equations. Its Eq. 15 is the standard strip factor (Ozisik 1981), normalised: Phi1 = pi/2, Phi2 = -pi/2 gives 1 (arithmetic, not printed).
- Eq. 18 refits `pieri2003.row_interception` Eq. 3 (1.09, -2.69, 1.28) with 1.09, -2.44, 1.084 and names no data. At RG/RG0 = 0.7 they give 0.266 and 0.211 (arithmetic, not printed).
- Calibration: porosity and P-bar from pictures at the same plot; soil albedo fitted at the site; validated on the same plot.
- Same author as `pieri2003` and Riou 1989; Gaudillere is cited elsewhere (`cortazar2009`): flag only.

## Bearing (2026-10-30)

- Gives the sunlit fraction and the net radiation at a point near the row base, where clusters hang; riou1989, pieri2003 and carrasco2008 (the held notes searched) do not. It does not give sunlit leaf area by depth, nor leaf wetness.
- For Agrarium: delta(x) at the cluster height is a mechanistic source for a sun-exposed share of the fruit zone; it says nothing about the upper canopy.
