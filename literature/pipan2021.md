---
id: pipan2021
citation: Pipan, P., Hall, A., Rogiers, S. Y. & Holzapfel, B. P. 2021. Accuracy of interpolated versus in-vineyard sensor climate data for heat accumulation modelling of phenology. Frontiers in Plant Science 12:635299
doi: 10.3389/fpls.2021.635299
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 54 of 54 quotes found at their lines by the main session; Table 2 read by eye from a rotated page 6 image at 120 dpi (last digit uncertain)
status: read
diseases: []
crops: [grapevine]
regions: [Victoria, Australia, Yarra Valley, King Valley, Rutherglen]
processes: [temperature interpolation, heat accumulation, phenology, minimum temperature, sensor placement]
records: []
datasets: [pipan2021.victoria]
files: [paula_2021.pdf (the 2026-10-18 drop)]
---

# Pipan et al. 2021: SILO grid against in-vineyard loggers

Daily minimum and maximum temperature from SILO (Australia's interpolated 0.05° grid) against
a logger in each of four Victorian vineyards for four seasons, and what the difference does
to heat sums, indices and modelled phenology. No record: a comparison, not a formulation.

## What it holds

- **Sites** (l. 160-177): AYB (Yarra Burn, Yarra Valley; steep, top 446 m), DCW (Whitlands,
  King Valley; undulating, top 790 m), DCY (Coldstream; flat, 150 m) and DBR (Rutherglen;
  flat, 150 m; Shiraz, the others Chardonnay). Four seasons, 2015-16 to 2018-19; October to
  April; irrigated.
- **Loggers:** one Tinytag TGP-4500 (Gemini) per vineyard, manufacturer-calibrated, in a
  Stevenson screen fixed to the top of a trellis post, 30-min temperature, humidity and dew
  point. Accuracy and screen height not printed.
- **SILO:** smoothing splines of about 4,600 Bureau of Meteorology stations on a 0.05° grid
  (about 5 km); free online. Its licence and its error statistics are not printed.
- **SILO minus logger (Table 2, by eye):** minimum, AYB +0.71 to +0.93 °C and DCW -0.79 to
  -2.32 °C, significant in all four seasons; DCY -0.10 to +0.95 °C, significant in 2017-18
  only; DBR -0.09 to +0.22 °C, none. Maximum, AYB -0.63 to -1.07, DCW +0.05 to +1.17 and DCY
  -0.42 to -0.95 °C, none significant; DBR -0.28 to -1.81 °C, significant in 2015-16 and
  2017-18.
- **Reading:** SILO matched logger maxima everywhere except DBR, and minima only at the flat
  sites. The authors attribute AYB to cool-air pooling and thermal layers and say the 5 km
  pixel cannot represent AYB and DCW; they report no correlation between the coolness of a
  day and the logger-SILO minimum difference ("data not shown").
- **Downstream:** growing degree days (base 10 °C), Huglin index (K not printed), growing
  season mean and January mean temperature, and Hall et al. (2016) modelled budbreak and
  maturity (Tables 4-5). Season-to-season variation exceeds site differences; AYB budbreak
  range 5 days, DCW 15 days; AYB harvest range 17 days.
- **Data:** from the authors "without undue reservation"; article CC BY; no repository.

## Dependence

- Uses SILO output (not run by the authors) and the formulas of Amerine & Winkler (GDD), Huglin
  and Smart & Dry. The comparison with Hall et al. (2016) is against modelled dates; shared
  data with Hall et al. is not stated.

## Bearing (2026-10-18)

For strand 2 (a sweep needs weather where the vineyard is) and strand 4 (sensor placement):

- **What it shows:** an interpolated 5 km grid mean carries the vineyard's maximum but misses
  its minimum by 0.7-2.3 °C (about a degree either way) wherever the site has relief, with
  the sign depending on the site. Flat sites have no significant bias in the minimum in most seasons.
- **Take for the sweep:** weather generated or downscaled from gridded or station data
  should be given a site offset for minimum temperature, and a larger one on sloping or
  hollow sites; the offset is not a constant and cannot be read from the grid. A humidity or
  leaf-wetness hour count that rests on night-time temperature will move with it.
- **Take for sensor placement:** one logger per vineyard was enough to see the bias; it was
  not enough to say where inside the vineyard it comes from.
- **Limits:** four vineyards; temperatures only (humidity logged, not compared); Table 2
  values by eye.
