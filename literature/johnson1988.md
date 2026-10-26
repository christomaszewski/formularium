---
id: johnson1988
citation: Johnson, D. A., Alldredge, J. R. & Fisher, R. 1988. Spatial pattern of downy mildew in hop yards. Phytopathology 78:1389-1395
doi: 10.1094/phyto-78-1389
read: 2026-10-25, in full (7 pages, two columns interleaved; results and discussion read in detail), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [hop downy mildew]
crops: [hop]
regions: [United States, Washington, Yakima Valley]
processes: [spatial pattern, aggregation, secondary spread, prevailing wind, semi-variogram, primary spikes]
records: []
datasets: []
files: [dr1025_johnson1988.pdf (the 2026-10-25 drop)]
---

# Johnson et al. 1988: where hop downy mildew sits in a hop yard, by hill, in a mild year

Six hop yards were assessed hill by hill and the pattern of diseased hills was tested with several statistics; there is no dispersal kernel.

**Read this first.** An analogue and a weak one for distance. Hop downy mildew (Pseudoperonospora humuli) is a downy mildew, but the unit is a hill of shoots, and the disease is counted as primary and secondary spikes, not leaf lesions. The 1985 epidemic was mild (0.2 to 1.6 % of hills diseased, l. 243). The hills stand on a square grid, so there is no along-row against across-row contrast to test (l. 54-55), and the semi-variograms looked alike in all directions (l. 152).

## What it holds

- **Site:** six hop yards in the Yakima Valley, Washington, in 1985; a section of 2.9 to 4.1 ha of each was assessed one to four times, at 10 to 25 day intervals, in May and June (l. 27-30, 243).
- **Layout:** hills in a regular square pattern about 3.13 m between centres (l. 54-55). Semi-variograms looked similar in all directions, so the direction of spread could not be determined (l. 152).
- **Pattern:** infected shoots were aggregated within the hill (abstract, l. 18-22); more secondary infections were found in hills that already had primary spikes, but nearly 33 % of the secondary spread went to hills without primary spikes (l. 240).
- **Prevailing wind:** no evidence for an increase in aggregation in the direction of the prevailing winds, from the south-west (l. 22-23, 260).
- **The authors' reasons (not tested here; the second rests on a personal communication):** sporangia of P. humuli are short-lived once detached, so those carried downwind in dry weather soon die (l. 262, 228); wind at ground level during spring rain in the valley can come from any direction (l. 228).

## Dependence

- Own field survey. Methods are standard spatial statistics (the reading agent records them as after Campbell and Madden type methods): negative binomial fits, Morisita's index, Greig-Smith blocks, doublet analysis and semi-variograms. No model of dispersal.

## Bearing (2026-10-25)

- **dm.wind_stretch_per_ms 0.3 [0-0.6]:** no downwind aggregation was seen in a mild year (l. 22-23, 260), and the authors give a reason that has to do with survival and wind direction in rain, not wind speed. It is a weak negative from one crop and one year at low incidence. It gives no number per m/s.
- **dm.splash_fraction 0.5 [0.2-0.8]:** nearly 33 % of secondary spread reached hills without a primary spike (l. 240), so most of it stayed in hills that already had one, which fits a large local share of spread; but a hill is 3.13 m across and the paper does not separate splash from short eddies, so it fixes no fraction. Hop analogue; pattern analysis, not a kernel.
- **dm.row_barrier 2 [1-4]:** nothing, because the grid is square and the direction of spread could not be found (l. 54-55, 152).
