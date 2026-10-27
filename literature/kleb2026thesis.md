---
id: kleb2026thesis
citation: Kleb, M. 2026. Site-specific forecasting and early detection of Plasmopara viticola in Vitis vinifera. PhD thesis, Universität Hohenheim
doi:
read: 2026-10-27, chapters 1-3 and 8 in the text layer and chapters 4-7 by OCR of the page images (PDF pp. 26-78), Tables 2-4 in the page images, by a reading agent (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py; for Agrarium and Cooptera D58
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Germany, Baden-Württemberg, Hohenheim]
processes: [canopy microclimate, leaf wetness, weather station, forecasting, thermography, inoculation]
records: []
datasets: [kleb2026.hohenheim_thesis, kleb2026.hohenheim2020]
files: [Dissertation_MelissaKleb_2026.pdf (the 2026-10-27 theses-d58 drop)]
---

# Kleb 2026: a thesis on canopy microclimate against station weather for downy mildew forecasting

The thesis behind `kleb2022` and `kleb2026`: chapter 4 is the 2022 paper and chapter 5 the 2026
preprint, word for word; chapter 6 adds a 2020 plot, chapter 7 an inoculation method.

**Read this first.** Chapters 4-7 are page images, read by OCR. The two chapters disagree on the
sensor layout (three vines per plot in ch. 4, four sites per plot in ch. 5) and on the station's
height (180 cm 75 m away, or a border station at 200 cm); the later chapter is taken.

## What it holds

- **Canopy against station, 2021 (ch. 4, pp. 24-33):** sensors at 100, 130 and 160 cm, every
  10 min. Daytime humidity in the canopy 1.7-3.4 points below the station's; at night 2.4
  points above it (canopy means 94.9-96.1 %). Daytime temperature 1.8-2.7 °C higher in the
  canopy, up to 6 °C. Leaf wetness (plot III only, counts): canopy 459 by day and 460 by night
  against the station's 512 and 622; the station passed the 460-count threshold every day, the
  canopy never on 19 days or nights, and the station stayed above it 2-3 h longer a day. No
  wetness hours or percent are tabulated.
- **Forecasts (ch. 5):** VitiMeteo levels from canopy and station data; agreement with observed
  disease r² 0.29 for the canopy average, 0.03 for the border station, 0.04 for a station 23 km
  away. The thesis puts the stations' over-calling down to their exposure, not distance (pp. 47, 80).
- **No wetness rule tested:** humidity of 90 % or rain as wetness is not compared with measured
  wetness anywhere. Chapter 6 calls a 2020 period wet above 435 counts, or by mean humidity
  above 85 % where they conflict, unvalidated.
- **2020 plot (ch. 6, pp. 55-60):** unsprayed 250 m² of Pinot Meunier, damage every 3rd day,
  first symptoms end of July, 30-40 % incidence a month later.
- **Data:** in figures only; the chapters' data statements say "Not applicable".

## Dependence

The VitiMeteo-Plasmopara classes (50, 100 and 200 degree-hours of wetness) are cited, not fitted.

## Bearing (2026-10-27)

- For Cooptera's stand-in (wet when humidity is at least 90 % or it rains): the canopy's night
  humidity averaged about 95 % while the canopy sensor stayed dry on 19 nights, so the rule would
  call wet nights the canopy did not have (an inference from Tables 3-4, not tested in the
  thesis). Station-based wetness ran 2-3 h a day longer than the canopy's.
- For D58: not obtainable; figures only, a managed vineyard, one site.
