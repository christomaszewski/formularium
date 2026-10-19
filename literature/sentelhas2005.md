---
id: sentelhas2005
citation: Sentelhas, P. C., Gillespie, T. J., Batzer, J. C., Gleason, M. L., Monteiro, J. E. B. A., Pezzopane, J. R. M. & Pedro, M. J., Jr. 2005. Spatial variability of leaf wetness duration in different crop canopies. International Journal of Biometeorology 49:363-370
doi: 10.1007/s00484-005-0259-1
read: 2026-10-19, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 55 of 55 quotes found at their lines by scripts/verify_quotes.py; Table 5 and Figs 3-4 read in the page images by the reading agent
status: read
diseases: []
crops: [grapevine, apple, coffee, maize, muskmelon]
regions: [Iowa, Ontario, Sao Paulo, Jundiai, Piracicaba]
processes: [leaf wetness duration, wetness sensor, canopy position, turfgrass reference]
records: []
datasets: []
files: [Spatial_variability_of_leaf_wetness_dura.pdf (the 2026-10-19 drop, supplied by Chris 2026-10-19)]
---

# Sentelhas et al. 2005: wetness hours at the top and bottom of five canopies

Sensors in apple, coffee, maize, grape and muskmelon canopies against a turfgrass sensor at 30 cm.

## What it holds

- **Sensors** (l. 88-96): Campbell 237 plates, 2-3 coats of latex, heat-treated 60-70 °C for 12 h,
  inclined 30-45°; wet when the reading is at or below about 9,000 (unit printed as k, read as
  kOhm, not checked).
- **Grape** (l. 163-170, 230): cv. Niagara Rosada, north-south hedgerow at Jundiai SP, Brazil,
  24 October 2003 to 14 January 2004 (68 days as printed; the calendar span is longer), sensors at
  160 cm (top) and 60 cm (bottom), 30° facing south, logged every 20 min. Mean wetness 8.48 h at the
  top and 8.33 h at the bottom (Table 2), a 9-minute difference. Dew days: 6.34 and 5.88 h
  (Table 3). Rain days: 12.41 and 12.83 h (Table 4). Turf overestimates grape wetness by 6-7 %
  (r 0.98 top, 0.82 bottom); fits: top y = -0.004 + 0.948x, bottom y = -1.963 + 1.150x. Against turf
  (Table 5): mean difference 0.47 h (MAD 0.92) at the top and 0.62 h (MAD 2.65) at the bottom.
- **Other crops** (Table 2): apple top 8.67, middle 8.25, bottom 6.78 h (about 2 h shorter at
  the bottom, agreeing with Wittich 1995); coffee 7.84 top and 9.29 bottom (conical shape);
  maize 14.50 top and 13.53 inside. Overall errors against turf 0.83 to 1.58 h (MAE).
- **Recommendation:** at least two sensors, top and bottom (Huber & Gillespie 1992, cited).
- **Not printed:** drying times, canopy density numbers, sensor error against a visual truth, the
  data.
- **Garbles:** printed day counts are below the calendar spans for apple, muskmelon, coffee and
  grape, without a reason; Table 5's text layer is scrambled.

## Is it the same data as `sentelhas2004`?

Yes, for the grape. The thesis (`sentelhas2004`) has the same place (Jundiai), cultivar (Niagara
Rosada), dates (24 October 2003 to 14 January 2004, 68 days) and the same 8.48 h at the top
against 8.33 h at the bottom, and turf reading about 6 % above the canopy. That note says chapters 3
to 6 of the thesis are his 2004 papers on sensors and spatial variability, so this paper is
probably one of them; I did not compare the chapter text with this paper's. Count it once, not
twice, as evidence.

## Dependence

- No process model; a sensor comparison. The turf reference and threshold method follow
  Sentelhas et al. 2004b and Kim et al. 2002 (cited). Gillespie and Gleason are co-authors; Gleason
  lent sensors and data to the thesis. Flags only.

## Bearing (2026-10-19)

- **Canopy position in grapes:** one trellised hedgerow, no difference in the daily hours between
  160 and 60 cm (9 min), a small one on dew days (28 min) and the reverse on rain days (the bottom
  25 min longer). Apple shows the opposite, a 2 h shorter wetness at the bottom. So a vertical
  gradient is crop-specific; for grape one wetness per vine is defensible.
- **Density:** no leaf area index is printed for any canopy, so nothing here tests
  micro.density_drying_slowdown; the grape hedgerow is described as well ventilated (l. 515-517).
- **Station sensor:** turf at 30 cm reads 6-7 % longer than the grape canopy (mean difference 0.5
  to 0.6 h a day, Table 5), which bears on micro.station_lai (a plate over grass treated as
  LAI 1.0).
- **RH:** none tested.
