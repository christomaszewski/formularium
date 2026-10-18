---
id: sanderson2022
citation: Sanderson, M. G., Teixeira, M. & Graça, A. 2022. Cold-air pooling in the upper Douro Valley: an observational study. Journal of Applied Meteorology and Climatology 61:1893-1904
doi: 10.1175/JAMC-D-21-0263.1
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; the TAF formula (journal p. 1897) and Table 2 (p. 1899) checked in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Portugal, upper Douro]
processes: [cold-air pooling, topographic amplification factor, cold-pool events]
records: [sanderson2022.taf]
datasets: [sanderson2022.stations]
files: [michael_2022_2.pdf (the 2026-10-18 drop)]
---

# Sanderson, Teixeira & Graça 2022: cold-air pooling in the upper Douro

An observational study for viticulture: where cold air pools in the valley from the terrain,
and how often and how strongly it does at one pair of vineyard stations.

## What it holds

- **Terrain index** (l. 260-270): TAF = W H / A (Whiteman 1990; Lundquist et al. 2008),
  W the valley width, H the height from the transect low point to the lower of the two local
  maxima, A the cross-sectional area by the trapezium rule. SRTM v4.1 at 90 m (l. 165);
  transects of 10 pixels (about 900 m) on tributaries and 20 pixels (about 1800 m) on the main
  channel (l. 231-233); down-valley gradient by least squares, tested at 5 %. Along the main
  channel most TAF values are 1.4 to 2.0, a few reaches 2.0 to 2.8 (l. 266-270). The text
  layer prints "TAF 5 WH/A"; the page image reads "=".
- **Stations** (l. 107-190, Table 1): nine Sogrape Vinhos stations in vineyards, 80 to 624 m,
  at 2 m, 15 min, fewer than 5 % missing; January 2011 to December 2017 (Pinhão-Porto from
  2014). Temperature, humidity and leaf-wetting sensors on each, but no humidity or wetness
  result is printed. The lead said hourly data; the paper says 15 min.
- **Events** (l. 255-368): a night with Leda 3 (163 m) at least 1 °C colder than Leda 2 (318 m),
  155 m apart, is a cold pool; strength is the largest difference; strong is above 4 °C.
  901 candidate nights, 67 rejected, 834 pools (32 % of nights). Strengths mostly 1 to 3 °C,
  greatest 5.5 °C; strong pools 4 % of events. Most in winter and early spring (January to
  March), fewest May to September; most peak 5 to 9 h before sunrise. Pools under about 30 m
  deep are not recorded (l. 174, 598).
- **Wind** (l. 488, 566): below about 4 m/s at Leda on pool nights; easterly or north-easterly
  at the hilltop Sairrão 1 more often on pool nights.
- **Not printed:** humidity, dew point, leaf wetness in pools; a TAF threshold for pooling; the
  units of the TAF gradient; the TAF at each station pair; supplementary Figs. S1 to S4 (not in
  the drop).
- **Reconciled:** Table 2's rows sum to 796, not the 834 of l. 368 (the 28 % marginal share
  fits 796); the abstract says seven categories, Table 2 has nine rows with two at zero;
  categories were assigned by eye.
- **Data:** station series not open ("commercially sensitive", l. 628); daily values in ECA&D
  (l. 122, 551); SRTM open.

## Dependence

- **Borrowed:** the TAF formula and mapping from Whiteman (1990) and Lundquist et al. (2008),
  with Arduini et al. (2017); the 1 °C threshold from Jemmett-Smith et al. (2018); the
  evolution categories by eye against Dorninger et al. (2011) and Mahrt & Heald (2015). None
  of these is a record here.
- **Data:** station observations; no model made them. Nothing is fitted, and the station
  events are not compared with TAF in the text read.

## Bearing (2026-10-18)

For strand 3 (the sensing and microclimate of the truth) and what Agrarium's truth can take:

- **What it gives:** a terrain index (TAF) from a public 90 m DEM that can say which vineyard
  cells are cooler at night than their neighbours, and the frequency, strength and timing of
  pools at one Douro reach (834 nights in seven years, mostly 1 to 3 °C, peaking 5 to 9 h before
  sunrise, winter-heavy). A cell's night minimum could be offset by a pool, but only as a
  distribution, not a fitted offset.
- **What it does not give:** humidity or leaf wetness in a pool. The sensors exist; nothing is
  reported. For a wetness model whose engine stand-in is RH ≥ 90 %, a pool's cooler air would
  raise relative humidity at a given dew point, but this paper cannot say by how much.
- **Season:** the pools are a winter and early-spring matter (January to March), few between
  May and September, the months of infection; the events are frost relevant more than
  wetness relevant.
- **Can it run:** TAF from the DEM yes (formula and radii printed, no coefficients); the
  event series no (data not open, 15 min).
