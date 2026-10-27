# Answer to inputs-d60.md: parts 1 and 2 (part 3 is inputs-d60-sensors.md)

2026-10-27, by an `ingest` session. Three strand agents (claude-sonnet-5-5) searched for models,
datasets and sensors, starting from what Formularium already held; every quote they cite was
found at its line by `scripts/verify_quotes.py`. No data file was downloaded. Delivered as one
branch; the request allowed parts.

## Part 1: models of the physical inputs

**Most of what exists is already held,** and this pass added little:

- **Leaf wetness:** the held models stand (SWEB, `magarey2006`, now runnable by a reading of
  Eq 15, branch `ingest/sweb-canopy-wind-d56`; Sentelhas's Penman-Monteith and threshold models;
  CART, Kim, Gleason, Shin, Amir, Lulu, Henshall; Dhakar 2025; Kuwagata 2024). New: threshold
  rules on cashew (`coulibaly2024`; the same form as the engine's humidity stand-in, so kin by
  form), a second reading of Kim's New Zealand vineyard work (`kim2007nzpp`; its wetness model's
  equations are not printed), dew from net radiative loss in rice (`luo1996`, independent of the
  engine). Searches found nothing under Bregaglio, Hornero, Montone, Pedro & Gillespie, Weiss or
  Huber & Gillespie.
- **Net and longwave radiation:** net radiation over a Chilean Cabernet Sauvignon vineyard from
  station data (`carrasco2008`; 30-min MAE under 40 W m⁻², RMSE under 61; one coefficient fitted
  on another vineyard); Brunt longwave coefficients for cotton and sesame (`duarte2026`). The held
  Dilley-Unsworth (`flerchinger2009`) and FAO-56 remain the validated choices.
- **Cloud from station data:** a cloud index from humidity and clearness (`herrero2012`, a
  2500 m site); night cloud interpolation (`gubler2012`, abstract only).
- **Not covered:** in-canopy temperature, humidity and wind from the station's, and rain splash,
  beyond what is held (`kleb2022`, `kleb2026thesis`, the canopy-flow and canopy-water notes of
  `research_notes/deep-research-10-25` in Agrarium). Seven papers were not obtained (Park 2019,
  Gama 2022, Gillespie 2021, Wang 2019, Solis 2021, Lee 2014, Savage 2012); a permission check
  refused one archive fetch, which was not worked round.

## Part 2: measurements to weigh the models by

**No open vineyard dataset was found with measured leaf wetness, radiation and in-canopy sensors
together beside a station.** Records added to `datasets.py`, best first:

| Dataset | What | Licence | Download now |
|---|---|---|---|
| `icos2024.lison` | a Veneto vineyard flux tower: four-component radiation, T, RH, wind, rain, 30 min, 2015-2024; no wetness | CC BY 4.0 | yes |
| `icos2016.arzelle` | a Franciacorta vineyard flux tower, 30 min, 2016-2024; variables not read | CC BY 4.0 | yes |
| `colucci2026.italy` | capacitive leaf wetness with weather at seven Italian sites | CC BY-NC 4.0 | yes |
| `arpav.veneto` | electronic-leaf wetness and radiation at vineyard stations, hourly, 2010-2025 | CC BY 4.0 | yes |
| `agroclim.inrae` | leaf wetness and radiation at INRAE stations, hourly, 1983-2025 | Etalab 2.0 | yes |
| `meteogalicia.galicia` | hours wet and radiation, hourly, 2024-2026 | attribution | yes |
| `callesen2026.southtyrol` | a grassed vineyard's fluxes and "ancillary meteorological data", 30 min; variables not read | CC BY 4.0 | yes |
| `bastos2024.vineyard` | hourly vineyard water-vapour loss, 2022; variables not stated | CC BY 4.0 | yes |
| `jenkins2023.yolo` | in-canopy wind, T, RH on one potted vine, 2 min, August 2020 | CC BY 4.0 | yes |
| `divine2024.diezma` | a Davis station with radiation and IoT wetness nodes, hourly, 2023-24 | CC BY 4.0 | yes |
| `leeson2025.whim` | wetness and net radiation above a bog, 15 min, 2003-2023 (not a crop) | OGL v3 | yes |
| `vonderwaydbrink2020.quillow` | wetness, T, RH in wheat, 2020; no radiation | CC BY 4.0 | yes |
| `gagliardi2022.turrialba` | wetness, T, RH under coffee shade, plot means, 2017 | CC0 | yes |
| `ameriflux2023.usnsa` | a California vineyard flux tower, 30 min, 2023-2025; variables not read | CC BY 4.0 | yes |
| `tasmania2024.botrytis` | wetness, T, RH at 1.2 m beside Tasmanian vineyards, 2009-2019 | on request | no |
| `mathieu2025.rully` | a Burgundy vineyard flux tower with net radiation, from 2024 | restricted | no |
| `grapex2018.lodi` | the GRAPEX vineyard experiment, four-component radiation, 2013-2017 | no repository | no |

For weighting wetness models, the open sets with measured wetness are the networks (ARPAV,
AgroClim, MeteoGalicia), Colucci, DIVINE and Whim Bog; for radiation and its partition at a
vineyard, ICOS IT-Lsn. Still to read: ICOS's product documents (sensor heights), Callesen's
variable list, the licences of Enviroweather, FEM/Trentino, ARPAE, SIAR and the Portuguese networks.
The strands' tables: `/srv/papers/drop/2026-10-27-inputs-d60/reading/{models,data}/LEADS.md` on
`agents`.
