# Answer to canopy-light-d61.md

2026-10-28, by an `ingest` session. Two reading agents (claude-sonnet-5-5) read; the main
session checked Riou et al. 1989's equations in its page images, wrote the record and the
module, and re-ran every quote check (123 quotes, all found at their lines).

## 1. Models that can be built

**One is built: Riou, Valancogne & Pieri 1989** (`riou1989`).
- Record `riou1989.row_interception`; code in `formularium.equations.riou1989`, with tests.
- The row is a porous box: foliage height H, width L, wall porosity p, rows D apart.
- Its inputs: sun elevation and azimuth, row azimuth, the direct and diffuse radiation on the
  ground, leaf and soil albedo.
- Its outputs: direct and diffuse radiation intercepted, absorbed and reflected per unit ground,
  and the sunlit height of each wall. It gives no leaf area by depth.
- Its parameters: p = 1/3 (from photographs), leaf albedo 0.20, soil albedo 0.18. Test canopy:
  D 1.8 m, H 0.9 m, L 0.3 m.
- Two equations are not as printed:
  - Eq 17, diffuse light on the foliage's lower face, lacks a 1/π; the module normalises it and
    integrates it in closed form.
  - Eq 27 steps from Eq 26 at λH = 2D − L, and is kept as printed.
- Validated on one north-south plot at Latresne (Bordeaux), six September days: daily absorbed
  27-180 W/m² calculated against 29-180 measured (Table I).
- Pieri & Gaudillère 2003 fitted closed forms to its runs; that record now names it in
  `calibrated_with`.

**One can be built in part: Gijzen & Goudriaan 1989** (held; read again in full).
- A turbid medium in rectangular rows: Ld (m²/m³), a mean leaf projection Oav from leaf-angle
  classes, and the path through the foliage along any ray (Eqs 1-10). The diffuse integral is
  Eq 19.
- The direct-beam sunlit fraction is left to Goudriaan 1977 and not printed.
- It is the only held model that takes a leaf angle distribution and gives light by position in
  the row.

**Not buildable from print:**
- Prieto et al. 2020 (3D radiosity on mock-ups; daily intercepted fraction RMSE 4 %).
- Louarn et al. 2008 (3D reconstruction and virtual photographs).
- Mabrouk et al. 1997 (3D turbid medium; only a closed form with c 0.29-0.33 is printed).
- Oyarzun et al. 2007 (not obtained). Campos et al. 2017 restate its fIPAR equations in part.

## 2. Leaf angles, extinction and porosity, as measured

- **Leaf inclination** (from horizontal):
  - Sultana on an overhead trellis: 63° at flowering, 57° in berry growth.
  - Open Lyre and GDC Merlot: 53-58°, plagiophile-like.
  - Napa Cabernet Sauvignon VSP: 58-79° by irrigation and nitrogen.
  - Grenache and Syrah on four training systems: 33-50° (`louarn2008`).
- **Extinction coefficient:** the only k measured for direct and diffuse light separately is the
  Sultana pergola's (`garciadecortazar2005`): direct 0.48 at noon and 0.67-0.71 over the day,
  diffuse 0.70, consistent with a spherical distribution. No hedgerow k, no fitted G-function
  and no Campbell x for vines were found.
- **Porosity and clumping:**
  - Foliage gaps 14-44 % across eight Merlot canopies (`mabrouk1998`).
  - Effective porosity 0.15-0.54 by plot and date, from inverting the Oyarzun model
    (`campos2016`).
  - Beer's law holds in a row only when W + H tan θ ≥ D (`lopezlozano2012`).
  - The near-1 clumping index from cover photographs (`fuentes2014`) is not a row clumping
    factor.

## 3. Measurements to check against

- No open dataset of light transmitted through vine canopies was found.
- What exists is tables and figures in papers: Lopez-Lozano's sun angles with ceptometer
  readings, Garcia de Cortazar's transmission with LAI, Campos's canopy dimensions, and Mabrouk
  1997's interception at four hours of one day.
- **ICOS IT-Lsn** (`icos2024.lison`, updated):
  - SW_IN, SW_OUT and LW only, 2015-2025;
  - no PAR, no diffuse, no below-canopy sensor;
  - rows 2.2 m apart, 0.5 m wide, 2 m high.
  - It can drive a model, not test one.

## 4. Kinship

None of these models shares an equation, implementation or calibration data with the engine's
39 models. The flags are:
- the sun's position, standard astronomy, as in `noaa.solar_position`;
- authors only: Gaudillère, of `pieri2003`, wrote `cortazar2009`'s records.

## 5. SWEB's 94 %

Magarey 2006's sentence is on p. 375, not 377. It cites Smart & Robinson 1991, a handbook not
obtained. Likely origin (inference): a leaf transmits only about 6 % of PAR (`smart1990`), so
94 % is PAR not transmitted, reflection included. Measured leaf absorption is about 80 %
(`mabrouk1997`, Riou's albedo 0.20). As "absorbed solar radiation" 94 % is too high.

## Not obtained

- Oyarzun, Stöckle & Whiting 2007, Agric. For. Meteorol. 142:12-24
  (10.1016/j.agrformet.2006.10.004).
- Charles-Edwards & Thorpe 1976, Ann. Bot. 40:603-613.
- Jackson & Palmer 1979, Ann. Bot. 44:381-383.
- Acta Hort. 584:7 (2002).
- Smart & Robinson 1991; Smart 1985; Williams & Ayars 2005; Goudriaan 1977.
