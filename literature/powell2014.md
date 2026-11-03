---
id: powell2014
citation: Powell, S. 2014. The spatial variation of minimum near-surface temperature in complex terrain: Marlborough vineyard region, New Zealand. PhD thesis, University of Canterbury
doi: 10.26021/9174
read: 2026-11-03, abstract and passages found by grep (not in full), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 7 of 7 quotes found at their lines by scripts/verify_quotes.py; closes the 2026-10-21 and 2026-10-26 leads
status: read
diseases: []
crops: [grapevine]
regions: [New Zealand (Marlborough)]
processes: [minimum temperature, frost, cold-air pooling, katabatic drainage, ridge-top wind, decoupling, spatial variability]
records: []
datasets: []
files: [dr1103_powell2014.pdf (the 2026-11-03 drop)]
---

# Powell 2014: spatial variation of minimum temperature across the Marlborough vineyard region

A PhD thesis on night minima in complex terrain, from a network of automatic weather stations (nine in the statistics below) over 2009-2011 and WRF model runs.

**Read this first.**
- Only passages found by grep were read, not the thesis in full. The wind statements are observed; the drainage-wind mechanism is partly modelled.
- Ridge-top wind is not surface wind. The thesis says that it is a poor test of whether the surface is calm, so a regional-wind threshold cannot be copied onto a screen-height threshold.

## What it holds

- **Spread of Tmin among stations:** the mean standard deviation (sigma) of Tmin across nine stations over all nights of 2009-2011 was 1.7 °C (l. 3532). Shares of nights: 20 % with sigma under 1 °C, 51 % at 1 to 2 °C, 22 % at 2 to 3 °C, 7 % above 3 °C (l. 3532).
- **Largest spread:** variations of up to 13 °C recorded by the network of privately owned stations (l. 2656), hills to valleys.
- **Cold nights and ridge-top wind:** in all areas except Ward, cold nights are more common when ridge-top wind is moderate to strong, above 5 m/s (l. 3925). They are infrequent in light ridge-top winds under 5 m/s, though these make up 34 % of nocturnal winds at the ridge-top stations (l. 3927-3928). The reason given is shelter, which decouples the surface.
- **Persistence under strong wind:** cold air in the slightly concave lower Wairau Valley floor near Fairhall persisted despite winds of 15 m/s on surrounding ridge tops (l. 1417).
- **Author's definition:** stable nights are anticyclonic, with ridge-top wind under 5 m/s (l. 5223); katabatic winds are assumed to develop with clear skies (l. 5225). This is the author's modelling assumption, not an observation.
- **Table 6.1 (l. 4701):** a row for Fairhall, 3.6 °C, 6 am on 3 October 2010, wind 1.3 m/s. Other columns are garbled by layout, not used.

## Dependence

- Own station-network observations (2009-2011) and WRF runs. Thompson 1986 (Niagara cold-air pools) and Doran 1991 (ridge-top wind and drainage) are cited and are leads to check.

## Bearing (2026-11-03)

- **micro.calm_wind_ms (3.5) and micro.decoupling_wind_ms (2) in Agrarium:** the 3.5 and 2 m/s are screen-height values; here 5 m/s is a ridge-top value and frost is more common above it. Observation, one region. Evidence against using regional wind alone to switch pools off; it does not give a surface threshold.
- **micro.coldpool_max_c (4):** a network spread of 1.7 °C on average and above 3 °C on only 7 % of nights, with a maximum of 13 °C over hills and valleys. The 4 °C is within the range, not a hollow-depth deficit.
- **No per-metre value:** the thesis gives none in the passages read.
