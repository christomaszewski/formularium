---
id: miller2017
citation: Miller, N.E., Stoll, R., Mahaffee, W.F. & Pardyjak, E.R. 2017. Mean and turbulent flow statistics in a trellised agricultural canopy. Boundary-Layer Meteorology 165:113-143
doi: 10.1007/s10546-017-0265-y
read: 2026-10-25, abstract only (Springer preview page), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 3 of 3 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [United States, Oregon]
processes: [canopy flow, wind, row orientation, wind direction, channelling, displacement height, turbulence statistics]
records: []
datasets: []
files: []
---

# Miller et al. 2017: in an Oregon vineyard the wind between the vines is steered along the rows, whichever way it blows above

Meteorological data from one trellised vineyard, analysed by the angle between the above-canopy wind and the rows; only the abstract was read. (The reading JSON lists three authors; the page lists a fourth, Pardyjak.)

**Read this first.** Abstract only. It prints no speeds, ratios or lengths. The dense-or-sparse finding is the authors' reading of turbulence statistics, not a wind ratio.

## What it holds

- Analysis of meteorological data from an Oregon vineyard shows that the canopy strongly influences the flow by channelling the mean flow into the vine-row direction, regardless of the above-canopy wind direction (l. 41).
- As the above-canopy flow rotates from row-parallel towards row-orthogonal, the canopy displacement height increases and the canopy-top shear length scale decreases. The stress tensor, turbulent kinetic energy budget and energy spectra also vary with direction (l. 41).
- The trellised canopy acts like a sparse canopy when the flow is row-aligned and like a dense canopy when it is row-orthogonal (l. 41). The abstract adds that sonic anemometry cannot resolve all scales of motion within the canopy.

## Dependence

None recorded. The same Oregon vineyard is in Miller, Stoll and Mahaffee 2015 and 2018 (not obtained). `everard2020` cites its dense-or-sparse finding, and `vendrame2016egu` reports the same channelling in an Italian hedgerow. Authors are shared with `bailey2013`, `bailey2014ams` and `torkelson2022` (a flag).

## Bearing (2026-10-25)

- **dm.row_barrier (2, range 1-4):** the clearest statement that air inside the canopy travels along the rows and that across-row flow meets a dense canopy. It supports the direction of the barrier, not the value 2. It is an aerodynamic result; an aerodynamic ratio is not a dispersal ratio.
- **Canopy wind (SWEB Eq 15):** a single mid-canopy ratio hides a direction dependence. SWEB's alpha of 1.3 is described there as an intermediate value because the profile differs with direction (cited from the held `magarey2006` as read in this strand's leads, not re-checked here).
- Kind of result: measurement, in an abstract.
