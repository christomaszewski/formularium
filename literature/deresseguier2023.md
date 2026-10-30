---
id: deresseguier2023
citation: de Rességuier, L., Pieri, P., Mary, S., Pons, R., Petitjean, T. & van Leeuwen, C. 2023. Characterisation of the vertical temperature gradient in the canopy reveals increased trunk height to be a potential adaptation to climate change. OENO One 57(1):41-55
doi: 10.20870/oeno-one.2023.57.1.5365
read: 2026-10-30, in full; Tables 1-4 read from the text; by a reading agent and note writer (claude-sonnet-5-5); 27 of 27 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France, Bordeaux, Saint-Émilion]
processes: [vertical temperature gradient, canopy air temperature, trunk height, cover crop, tillage, frost, heat wave, soil moisture, Canopy Winkler Index]
records: []
datasets: []
files: [dr1030_deresseguier2023.pdf (from Chris's Pieri collection, the inbound folder: 2023-resseguier-10-20870-oeno-one-2023-57-1-5365.pdf)]
---

# de Rességuier et al. 2023: air temperature at 30, 60, 90 and 120 cm in a vine row, five years, cover crop against tillage

Hourly min and max temperatures from 24 shielded loggers in two adjacent Merlot parcels near Saint-Émilion, 2016-2020, with the vertical gradient explained by soil moisture, sky, mean temperature and wind.

**Read this first.** Two parcels 20 m apart, one vineyard, VSP at 6000 vines per ha; the sensors are on posts in the row, daily extremes only (hourly min and max, not a time series of hourly means). No humidity, wind or leaf wetness was measured in the canopy; wind is the station's, at 10 m. Soil moisture is a model output (Lebon et al. 2003), not a measurement.

## What it holds

- **Site and vines:** dry-farmed Saint-Émilion, flat, 36 m, sandy-clay; Merlot planted 1972, 6000 vines per ha, simple Guyot, VSP, first wire 45 cm (bunch height), trimmed at 1.6 m; rows NW-SE, 1.4 m between rows and 1.2 m between vines; the cover crop strip is 0.9 m wide, soil under the row tilled in both (l. 164-196).
- **Sensors:** Tinytag Talk2 TK-4023 loggers with PB-5005 thermistor probes in RS3 shields, three replicates at 30, 60, 90 and 120 cm on vine posts, in the same or adjacent rows, up to 20 m apart (l. 199-210). Hourly Tn and Tx 2016-2020, daily Tn from 18:00 to 18:00 and Tx from 06:00 to 06:00 (UTC); 4.9 % of records removed as outliers and replaced by the mean of same-height, same-treatment sensors (l. 211-227). Weather station at 100 m: Tn and Tx at 1.7 m, insolation, rain, wind at 10 m.
- **Indices:** Canopy Winkler (sum of mean T above 10 C, 1 April to 31 October); DTR August-September; the GSR model (sum of daily mean above 0 C from day 91; Merlot reaches 220 g per L at 2962 degree-days).
- **Soil moisture model (Lebon et al. 2003, adapted):** row angle -25 (cover crop) and -10 (tilled) degrees, latitude 44.92, row spacing 1.4 m, minimum foliage porosity 10 % and 25 %, soil albedo 0.18, holding capacity 200 mm, foliage 1.15 m high and 0.45 m wide, cover on 64 % of the inter-row with its own 30 mm reserve; grass conductance follows FTSW like the vine's (l. 224-250).
- **Mean gradients over the growing season (Table 2, 120 minus 30 cm):**
  - Tn: +0.3 +/- 0.1 C (cover crop), 0.0 +/- 0.1 C (tilled).
  - Tx: -1.1 +/- 0.3 C (cover crop), -0.8 +/- 0.4 C (tilled); 90 minus 30: -0.9 and -0.6; 60 minus 30: -0.4 and -0.2.
  - Canopy Winkler: -73 +/- 31 and -65 +/- 41 degree-days (69 between heights on average); GSR delay to 220 g per L is 3 days (cover crop) and 2 days (tilled).
  - DTR August-September: -0.8 and -0.4 C.
- **Seasonal pattern:** strong Tn gradient from November to May with cooler air near the ground, up to 2.7 C in April in the cover crop; small reverse gradient June to October; Tx gradient substantial April to September, up to 2.7 C, with a few inversions (l. 306-358).
- **Drivers (Table 3, mixed models, 120 minus 30 cm gradient):** simulated soil moisture is the strongest, drier soil gives a larger gradient (slope on moisture: Tn cover crop -0.1448, Tx cover crop +0.238, Tn tilled -0.0736, Tx tilled +0.2632, all p < 0.001, with the gradient taken as 120 minus 30 and signs as printed). Clear sky enlarges both gradients, more in the cover crop. Cooler mean T enlarges the Tn gradient, warmer mean T the Tx gradient. Wind enlarges the gradients except for Tn in the cover crop.
- **Cover crop against tillage at 30 cm (Fig. 4):** cover crop minima lower and maxima higher, up to 2.2 C, on average 0.4 C (Tn) and 0.3 C (Tx), largest in summer.
- **Extremes:** frost night 27 April 2017, gradient 1.7 C (cover crop) against 0.9 C (tilled), 0.5 C colder at 45 cm in the cover crop; heat wave 23 July 2019, tilled 0.8 C cooler than cover crop in the bunch zone. Over 2016-2020, 67 days with Tn below -2.5 C at 30 cm (cover crop) against 50 (tilled), and 56 days above 35 C against 47.
- **Table 4 (extreme days, 120 minus 30 cm):** Tn +0.8 (cover crop) and +0.3 (tilled) C; Tx -1.6 and -1.3 C. At 90 minus 30 cm: +0.5, +0.2 and -1.3, -0.9; at 60 minus 30: +0.3, +0.1 and -0.7, -0.5.
- **Limits:** the authors did not consider roughness or leaf area density profile; results apply to this VSP, 6000 vines per ha; trunk-height effect is inferred from heights, not tested with different trunks.

## Dependence

- Follows deresseguier2020 (held) for the Canopy Winkler Index and logger protocol; soil moisture from Lebon et al. 2003 (not held), whose radiation interception is that of riou1989 and riou1994; GSR from Parker et al. 2020 (not held). Shares authors (de Rességuier, van Leeuwen, Mary, Petitjean) with deresseguier2020 and Pieri with the Bordeaux microclimate papers.

## Bearing (2026-10-30)

- **In-canopy air temperature:** a measured vertical profile in the vine row, with magnitudes by weather, soil and ground cover, directly bearing on Agrarium's in-canopy temperature (the bunch zone at 30 to 60 cm sits up to 1.4 C cooler at night and up to 1.1 to 1.4 C warmer by day than at 1.2 m, on extreme days up to 1.6 C). A simulated canopy temperature should reproduce these signs and sizes; the figures are for extremes, not hourly values.
- **Cover crop effect:** grassed rows have larger gradients than tilled (night colder, day warmer) in the lowest 30 cm; the paper's own inference that this is exposure to frost and heat.
- **Not shown:** humidity or leaf wetness in the canopy, hourly profile shape beyond two example days, wind in the canopy.
