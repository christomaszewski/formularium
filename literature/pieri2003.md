---
id: pieri2003
citation: Pieri, P. & Gaudillère, J. P. 2003. Sensitivity to training system parameters and soil surface albedo of solar radiation intercepted by vine rows. Vitis 42(2):77-82
doi: 10.5073/vitis.2003.42.77-82
read: 2026-10-26, a light reading by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py; Eqs 1-7 and the Fig. 4 inset (printed pp. 78-81) read in the page images by the agent, Eqs 3-7 and the inset also by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Bordeaux]
processes: [radiation interception, row geometry, diffuse radiation, albedo, transpiration]
records: [pieri2003.row_interception]
datasets: [pieri2003.bordeaux_diffuse]
files: [pieri2003.pdf (the 2026-10-25 other-sources drop)]
---

# Pieri & Gaudillère 2003: the radiation a vine row catches, from its view factor

The Riou et al. 1989 row-interception model, run every 30 min over an average Bordeaux
year for 200 combinations of row spacing, height, width, azimuth and albedo, is summarised
in closed forms: the season's interception ratio is linear in the square root of the view
factor between neighbouring rows, with a sinusoidal azimuth term and a factor for row shape
and soil albedo. A diffuse-fraction fit on Bordeaux data drives it.

## What it holds

- **Inputs** (l. 77-80, 105, 131, 139): 10-day sums of global radiation, 1961-1990 means at
  44°40' N; one representative day per 10-day period; PET 640 mm (1986-1999, Penman);
  reference geometry w 0.35 m, Hf 1.2 m, leaf albedo 0.25, soil albedo 0.18, row porosity
  0.33 (l. 106-126).
- **Eq. 1** (l. 86): f = tan(½ atan(Hf / (D - w))), the view factor of Ozisik 1981.
- **Eq. 2** (l. 101): transpiration = Rgv / ((1 - a) Rg) × PET, after Riou et al. 1994.
- **Eq. 3** (l. 143-145, page image): Rd/Rg = min(1, 1.09 - 2.69 (Rg/Rg0)² + 1.28
  (Rg/Rg0)³), r² 0.93, n 121 daily pairs measured at Bordeaux over two years, source not
  named (l. 140).
- **Eq. 4** (l. 230-235): Rgv / ((1 - a) Rg) = C [(-0.16 + 1.17 √f) - A(f)(1 - sin θ)], r²
  0.999 over n 200 simulations (D/Hf 0.5-10, θ 0-90°), θ the row azimuth (0° E-W); A(f) =
  0.0246 f/b² exp(-f²/2b²), b 0.274, r² 0.998, n 10 (Fig. 4 inset only); C = 1 at the
  reference shape and albedos.
- **Eq. 5-6** (l. 252-256): fs = tan(½ atan(w/Hf)); C = 0.544 + 1.04 (as - 0.18) + 1.209
  √fs, so Rgv / ((1 - a) Rg) = C [(-0.16 + 0.17 √f) - A(f)(1 - sin θ)], r² > 0.98; the 0.17
  is printed where Eqs 4 and 7 have 1.17.
- **Eq. 7** (l. 289-292): Rgv = Rg [0.54 - 0.6 (al - as) + 0.8 √f] [(-0.16 + 1.17 √f) -
  A(f)(1 - sin θ)], r² > 0.98 for every system.
- **Results** (p. 79): N-S rows insensitive to date, E-W rows peaking near the equinox;
  transpiration 437 mm at D/Hf 1 and 286 mm at 2 for N-S rows, E-W rows 5 and 12 % less;
  azimuth changes the season's ratio by at most 0.055, at D/Hf about 2.
- **Not printed:** the sinusoidal coefficients behind α, the Penman inputs, the training
  systems' D, Hf and w beyond the reference, the extra-atmospheric radiation formula.

## Dependence

- **Computes** Riou et al. 1989's interception model (l. 37, 53-55), not held and not
  re-derived here, and Riou et al. 1994's transpiration formula; Eqs 4-7 are fitted to that
  model's outputs: fitted with a model, which has no record to name.
- **Eq. 3 fitted to** `pieri2003.bordeaux_diffuse`, observed daily pairs.
- Same group as `lebon2004.leaf_development` (Lebon et al. 1995 is cited), and Gaudillère
  is an author of the engine's `cortazar2009.brin` and `cortazar2009.budburst` (kin report
  2026-10-26): flags only, no shared equation or data.

## Bearing (2026-10-26)

- For Agrarium's canopy physics (the 10-18 search's terrain and canopy strand): a closed
  form for a row's seasonal interception from spacing, height, width, azimuth and albedo,
  and a Bordeaux diffuse-fraction fit of the clearness-index form. Kin by form to the
  engine's clearness-index partition if one is listed; the row form is new.
