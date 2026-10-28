# Request: sunlight through a vine row (Agrarium D61)

From Agrarium's session on `agents` (ckt), 2026-10-28, at Chris's word (D61, decided as
recommended: "Sure go for it"). For an `ingest` session: papers stay with you (D40). Search
worldwide; training systems beyond vertical shoot positioning (VSP) are welcome.

## Why

Agrarium's truth knows the sun's position every half-hour, direct and diffuse light, slope and
horizon, each field's row direction and each vine's leaf area. It does not know how sunlight
gets into a vine row. Several of its values are that quantity in disguise, each `assumed`:
- which sporangia sit in sun (`f3.sun_exposed_share`);
- which low leaves primary infection reaches (`host.lower_canopy_fraction`);
- how much the sun warms and dries the canopy.

And SWEB's claim that the first sunlit layer takes 94 % of the sunshine (Magarey 2006, p. 377,
citing Smart & Robinson 1991) is assumed, not computed. One sourced model of light in a
hedgerow vineyard would replace these.

## What to read and settle

1. **Models of light interception by hedgerow vineyards:** their equations and parameters,
   in full. For example Riou et al. 1989 and its successors, Louarn et al. 2008 (light
   interception 20-67 %, leaf area density 4.2-6.7 m²/m³, held only as a mention in
   Agrarium's research_notes/truth-phenology-growth), Gladstone & Dokoozlian, Prieto, Oyarzun,
   Cohen, and any 3D or porous-hedgerow model with printed equations. For each: inputs (sun
   elevation and azimuth, row azimuth, canopy height, width and porosity, row spacing, leaf
   area density, leaf angles), outputs (intercepted fraction, sunlit area, light by depth),
   where it was validated and against what, and the error.
2. **Grapevine leaf angle distributions** and extinction coefficients (k, the G-function,
   Campbell's ellipsoidal parameter) as measured, by cultivar, training system and season;
   clumping or porosity factors for vine rows.
3. **Open measurements to check against:** light (PAR or global) transmitted through or
   intercepted by vine canopies at known sun angles, with canopy dimensions; and what ICOS
   IT-Lsn's vineyard radiation measures (`datasets.py` has it from D60).
4. **Kinship:** whether any of these shares an equation, implementation or calibration data
   with the engine's models (`world/engine_models.json` in Agrarium), by the kinship rule.

## What to deliver

On a branch `ingest/canopy-light-d61`, following `literature/INGESTING.md`: formulations in
`catalogue.py` with every parameter, equation modules where the form is complete, datasets
in `datasets.py`, a note in `literature/` for each paper read, and a short answer note
(`literature/requests/canopy-light-d61-answer.md`) naming the models that can be built and what
each needs. Part 1 first if delivering in parts.
