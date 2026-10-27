---
id: vendrame2017
citation: "Vendrame, N. 2017. Study of vegetation-atmosphere interactions over vineyards: CO2 fluxes and turbulent transport mechanics. PhD thesis, University of Padova, Doctoral Course in Crop Science, cycle XXIX (supervisor A. Pitacco)"
doi:
read: "2026-10-25, lightly: the turbulence chapters (site, methods, results, discussion); Fig. 5 read off the page image, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [Italy, north-east]
processes: [canopy flow, wind, wind profile, drag coefficient, leaf area density, momentum flux, row direction, seasonal canopy development]
records: []
datasets: []
files: [dr1025_vendrame2017.pdf (the 2026-10-25 drop)]
---

# Vendrame 2017 (PhD thesis): wind and drag in a Sauvignon Blanc hedgerow from bare canes to full leaf

The measured wind profile inside and above a vine hedge through the 2015 season, from the thesis chapter that became `vendrame2023`.

**Read this first.** A PhD thesis, not a peer-reviewed paper. The wind ratios come from Fig. 5 (U/u*), read by eye from the page image, so they are approximate, not printed. They assume the same u* at each height (not checked). Mean wind ratios were not split by wind direction; only the turbulence (ejection) statistics were. The leaf area density formula lost its fraction bar in the text (garbled): do not convert LAD to LAI from it.

## What it holds

- **Site and instruments:** Sauvignon Blanc hedgerow in north-east Italy (45 44 N, 12 45 E), rows at 35 to 125 degrees N, 2.2 m apart and 0.5 m wide; trunk space 0.7 m; the trellis, at 2 m, is taken as canopy height and the vines were hedged there (l. 1195-1196). Sonic anemometers (CSAT3, 20 Hz) stood in the middle of the inter-row at 0.5, 1, 1.5 and 2 m, with a reference at 4 m (2h) (l. 1215). All in-canopy values are inter-row-centre values.
- **Leaf area density (Table 3, per hedge volume 0.5 m wide, not per vineyard volume):** 1.1, 1.9, 2.3, 3.8, 6.8 and 8.8 m2 m-3 on 13 May, 19 May, 27 May, 4 June, 22 June and 7 July 2015 (l. 1265); the reading agent notes a canopy height of 1.0 to 2.0 m over these dates.
- **Drag:** the bulk drag coefficient at 2 m rose almost linearly with LAD, from about 0.02 for the empty canopy to 0.10 for the full canopy in neutral and stable conditions, and almost 0.14 in unstable conditions (l. 1328).
- **Momentum:** late in the season about 15% of the above-canopy momentum flux reached the trunk space (0.5 m) and about 20% reached 1 m (taken by the reading agent as mid-canopy) at full leaf, while about 90% of the 4 m flux was still present at 2 m (l. 1353).
- **Wind profile (Fig. 5, approximate, near-neutral):** at full leaf U/u* is about 6 at 4 m, 2.8 at 2 m, 2.2 at 1 m and 2.2 at 0.5 m; with no leaves about 9, 7.5, 6 and 4.8 (l. 1359). So at 1 m (mid-canopy) the wind is about 0.8 of that at the canopy top and about 0.37 of that at 4 m with full leaf, and about 0.67 of that at 4 m with no leaves (arithmetic on figure readings, not printed). Normalised wind fell at all heights as leaves grew (l. 1375). There is no clear inflection point at canopy top, except in the last period in unstable conditions (l. 1365).
- **Direction:** classes were diagonal (57 to 102 and 147 to 192 degrees N) and parallel (12 to 57 and 192 to 237 degrees N); only the ejection-quadrant profile was shown to differ between them (l. 2314). The author reads row-parallel wind as entering at canopy top without strong distortion and carrying momentum more efficiently along the profile, while across-row wind hits the row directly and brings strong sweeps (l. 2562).

## Dependence

Own measurements. Cites Miller, Stoll and Mahaffee (2015, not obtained) for a foliated vineyard "of similar architecture" (l. 1505). The same campaign is in `vendrame2016egu` and `vendrame2023` (not independent).

## Bearing (2026-10-25)

- **Mid-canopy to open wind (SWEB Eq 15):** the best measured set in this strand: about 0.37 of the 2h wind at full leaf (0.67 with no leaves), and about 0.8 of the canopy-top wind, for a 2 m hedge with rows 2.2 m apart, inter-row centre, directions pooled. The 0.3 U_Z found by trial for SWEB is a little below the full-leaf value. SWEB's Z (200 cm over a 150 cm canopy, per this strand's leads) is lower relative to its canopy than 2h here, so the match is not exact. Kind of result: measurement, read off a figure.
- **dm.row_barrier (2, range 1-4):** no across-to-along ratio of wind and nothing on spores; only that the turbulence structure differs for row-parallel wind. An aerodynamic ratio is not a dispersal ratio.
- A leafless-to-full change of 0.67 to 0.37 shows the ratio depends strongly on leaf density, so one fixed fraction is a season-average choice.
