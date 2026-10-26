---
id: thomas1988
citation: Thomas, C.S., Marois, J.J. & English, J.T. 1988. The effects of wind speed, temperature, and relative humidity on development of aerial mycelium and conidia of Botrytis cinerea on grape. Phytopathology 78:260-265
doi: 10.1094/Phyto-78-260
read: "2026-10-25, lightly: methods and results (a scan read through OCR); the sponge regression checked on the page image, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: [Botrytis bunch rot]
crops: [grapevine]
regions: [United States, California]
processes: [wind, evaporative potential, relative humidity, aerial mycelium, conidia, canopy flow, wetness drying]
records: []
datasets: []
files: [dr1025_thomas1988.pdf (the 2026-10-25 drop)]
---

# Thomas et al. 1988: in a lab tube, evaporation from wet berry-sized sponges rises steeply with wind between 0 and 0.6 m/s

A growth-chamber study of Botrytis on berries at three wind speeds, with a regression for the evaporative potential of the air, and a field check in two vineyards.

**Read this first.** The evaporation is from water-saturated sponges of berry size in a 2.2 cm tube, not from leaves. In the printed regression the squares were lost by the text scan ("5.667 X (WS)"); the page image prints WS squared, and the printed 0.8 g/h maximum agrees with the squared form (arithmetic below). The wind range is 0 to 0.6 m/s, the range of wind found at cluster height in the vineyards, not the regional wind above the canopy.

## What it holds

- **Lab design:** five berries (or berry-sized foam sponges) in a 20.3 cm by 2.2 cm acrylic tube, with a fan giving 0, 0.3 or 0.6 m/s; relative humidity (RH) 69, 90 and 94% from salt solutions (l. 85); temperatures 16, 21, 26 and 30 degC (l. 93, by grep).
- **Evaporative potential (EP):** grams of water evaporated per hour from the saturated sponges, weighed after 7 h at 0.6 m/s and 23 h at 0 or 0.3 m/s (l. 131). EP ranged from 0 to 0.8 g/h over the lab treatments (l. 277).
- **Regression (unnumbered, l. 303):** EP = 0.2565 - 0.0028 RH + 5.667 WS^2 - 0.055 WS^2 RH, with EP in g/h, RH in % and WS in m/s. It explained 96% of the variation (l. 308). Temperature was not significant and is not in it. The squares are read from the page image.
- **Arithmetic from the regression (not printed; the note writer re-ran it):** at RH 90%, EP is 0.005, 0.069 and 0.263 g/h at 0, 0.3 and 0.6 m/s; at RH 69%, 0.063, 0.232 and 0.737 g/h.
- **Field, 1986:** two vineyards (Zinfandel and Chenin blanc); temperature, RH and wind recorded hourly at cluster level in leaf-removal and control canopies (l. 162). The maximum hourly wind speeds were 0.58 m/s (leaf removal) and 0.28 m/s (control), so the in-canopy range sits inside the lab range (l. 376). No wind above the canopy is given.

## Dependence

Companion to `english1989` (the same varieties and year, probably the same plots; shared authors: a flag). The regression is fitted to its own lab data; no outside equation.

## Bearing (2026-10-25)

- **micro.evap_wind_per_ms (0.3 added share of evaporation per m/s of regional wind, assumed):** the shape is not linear. EP at RH 90% grows from 0.069 to 0.263 g/h between 0.3 and 0.6 m/s (arithmetic, not printed), a rise of about 3.8 times for a doubling of wind. It is a sponge in a tube at 0 to 0.6 m/s, and the paper gives no regional wind. It supports "wind speeds up drying" at in-canopy speeds, and cannot calibrate a per-m/s share of regional wind.
- **Canopy wind (SWEB Eq 15):** gives in-canopy absolute wind only (0.28 and 0.58 m/s at most, hourly), no ratio to the open wind.
- Kind of result: laboratory regression (sponges) plus a field range.
