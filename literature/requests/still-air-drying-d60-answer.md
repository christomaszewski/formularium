# Answer to still-air-drying-d60.md

2026-10-28, by an `ingest` session. A reading agent searched and read; the main session
checked the key lines, Eq 7's page image and the arithmetic. Every quote was found at its line
by `scripts/verify_quotes.py`. Files, datasheet texts and the arithmetic scripts (`calc/`) are in
the drop `2026-10-28-requests/d60air`.

## Short answer

**A floor of 0.5 m/s on the station's wind, before the canopy factor, is sourced; 0.4-0.8 m/s
is the range to test.** Three lines of evidence support it:
1. FAO-56 limits u2 to at least 0.5 m/s "to account for the effects of boundary layer
   instability and buoyancy of air in promoting exchange of vapour at the surface when air is
   calm" (allen1998, Chapter 3, held). It is a convention for grass, not a leaf measurement.
2. A station's 0 m/s hides real wind below its anemometer's starting speed. Sentelhas et al.
   2006 blame a stalled anemometer at night for dew that starts too early, the same symptom as
   SWEB's.
3. SWEB's own calibration data dry in still air. Magarey et al. 2005's Eq 7 (p. 114, page
   image) gives SWD = 19.6 + 37.0 × 0.34^U min for 5 µl drops: 56.6 min at U = 0. Eq 13,
   h = c Uc^0.5, then forces h to zero there.
   - If drying time scales as 1/h, the still-air h equals SWEB's at a leaf wind of
     0.26-0.36 m/s (arithmetic, not printed).
   - A 0.5 m/s station floor gives 0.18-0.25 m/s at the leaf, with a canopy factor of
     0.35-0.5. That is the same order.

**Free convection does not justify the floor in SWEB's units.** A physical still-air
coefficient for a 0.1 m leaf, 7-22 cm/min, equals a forced wind of only 0.01-0.09 m/s.
SWEB's h is a calibrated drying scale, 2-9 times a flat plate's, so a physical free-convection
h added to it would barely move the result. Justify the floor as hidden wind plus FAO-56's
convention, not as free convection.

## 1. Anemometer starting speeds (makers' sheets)

| Instrument | Value | Source |
|---|---|---|
| Navis WSS-100 (Colucci's stations) | range 0.8 to 50 m/s; 1 s averaging | a distributor's copy of the sheet; calling 0.8 m/s a threshold is our inference |
| RM Young 05103 | starting threshold 1.0 m/s | Campbell Scientific brochure |
| Campbell/Met One 034B | starting threshold 0.4 m/s | Campbell Scientific brochure |
| Gill WindSonic (sonic) | 0.01 m/s | Gill sheet |
| Davis 6410 | range from 0.5 m/s | a retailer's text; no threshold printed |

No source states how a logger turns sub-threshold samples into an hourly mean. With 1 s
averaging, an hourly 0.0 needs every sample at 0, so the true wind stayed below the
threshold all hour (inference).

## 2. Free and mixed convection

From Muir 2019 (`muir2019`), which follows Monteith & Unsworth:
- forced, laminar: Nu = 0.6 Re^0.5;
- free, laminar: Nu = c Gr^0.25, with c = 0.5 or 0.23 by surface and sign;
- mixed: Nu^3.5 = Nu_forced^3.5 + Nu_free^3.5;
- free convection dominates when Gr/Re² < 0.1.

For a 0.1 m leaf at 1-5 K from the air, the mixed regime is about 0.02-0.4 m/s (arithmetic).
Campbell & Norman, Schuepp 1993, Nobel and Gates were not obtained.

## 3. Wetness models

- No wetness model read has a free-convection or zero-wind drying term.
- Penman-Monteith forms (Sentelhas 2004, 2006) use a forced-only rb, infinite at 0 m/s.
- Luo & Goudriaan 2004 use a 0.5 m/s minimum wind for dew on rice and say free convection takes
  over below 1 m/s.
- Pedro & Gillespie 1982 was not obtained.

## 4. Wind inside vine canopies

No measurement of in-canopy wind with the station calm was found. What the held notes give:
- mid-canopy wind is 0.37-0.7 of the wind above (`vendrame2017`, `everard2020`, read from
  figures);
- cluster-zone hourly maxima were 0.28-0.58 m/s (`thomas1988`).

Daudet et al. 1998 measured a leaf replica's boundary-layer conductance in a vineyard, but only
its abstract was obtained (doi 10.1016/s0168-1923(97)00078-6).

## For Agrarium

- Register `U = max(U_station, 0.5 m/s)` before the canopy factor:
  - status: sourced as a convention (FAO-56) and an instrument limit (makers' sheets);
  - range: 0.4-0.8 m/s;
  - not from Colucci's stations.
- An alternative is a floor on Uc of about 0.3 m/s, from Eq 7, read through SWEB's own
  constant. That rests on our arithmetic and an assumption that drying time scales as 1/h.
- Nothing here was added to `catalogue.py`: the floor is Agrarium's parameter, and no new
  formulation was read whole.
