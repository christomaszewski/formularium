---
id: caffarra2011
citation: Caffarra, Amelia & Eccel, Emanuele. 2011. Projecting the impacts of climate change on the phenology of grapevine in a mountain area. Australian Journal of Grape and Wine Research 17(1):52-61
doi: 10.1111/j.1755-0238.2010.00118.x
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which read Table 2 on the page image; 30 of 30 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Trentino]
processes: [phenology, climate projection]
records: []
datasets: []
files: [2011-caffarra-10-1111-j-1755-0238-2010-00118-x.pdf]
---

# Caffarra & Eccel 2011: the Chardonnay model projected over Trentino

The 2010 model (`caffarra2010.chardonnay`, called FENOVITIS here) run at ten Trentino
sites, five on the valley floor and five above 500 m, on HadCM3 A2 and B2 weather
downscaled to daily series. A projection paper; no new fit.

## What it holds

- **Model:** FENOVITIS as calibrated on the Veneto series (mean annual temperature 13.1
  °C) and validated on four stations (l. 200-203); chilling from 1 September, which the
  authors call arbitrary, and a budburst sub-model calibrated only on cold-winter
  stations (l. 434-439); the forcing sigmoid saturates above 25 °C, after Pouget's
  experiments (l. 395-398, 452).
- **Weather:** two downscaled series (San Michele at 210 m, Cles at 650 m; the table says
  228 m for San Michele) translated to the other sites by normalisation (l. 133-134,
  176-189); end-of-century warming about 2 °C (B2) and 4.5 °C (A2) (l. 203).
- **Observed check:** San Michele 1990-2000 veraison mean day 221, predicted 223 (A2) and
  224 (B2); Cembra 222 against 222 and 226 (l. 254-256). Figure 1's observed trends are
  significant except San Michele's budburst, slopes not printed (l. 112-113).
- **Projections** (Table 2, d/yr over 2000-2098): all stages advance at all sites;
  veraison −0.31 and −0.21 at San Michele, −0.36 and −0.23 at Cembra (A2, B2); San
  Michele 4 d earlier by the 2020s and 15 by the 2070s, Cembra 5 and 19 (l. 291-293);
  21-30 d by the 2090s (l. 299). Table 3: the advance rate rises 0.040 d/yr per °C of
  site mean temperature and falls 0.0002 d/yr per m of elevation (flowering, A2;
  l. 438). Veraison after 31 August is taken as the cold limit for quality wine (l. 223).

## Dependence

- **Computes** `caffarra2010.chardonnay` unchanged; nothing fitted.

## Bearing (2026-10-13)

- Only as the sensitivity of a chilling-forcing model to altitude: larger advances
  higher up, a point for any Penedès slope.
