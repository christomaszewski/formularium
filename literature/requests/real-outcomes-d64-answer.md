# Answer to real-outcomes-d64.md

2026-10-28, by an `ingest` session. Three reading agents (claude-sonnet-5-5) searched by region.
The main session rechecked every quote with `scripts/verify_quotes.py` and read the two tables
that carry the most rows in their page images: `chrelashvili1993` Table 1 and `brook1992`
Table 7.

## The seasons: `literature/real_outcomes_d64.csv`

**81 dated seasons in 12 countries,** from 24 sources: 22 held, 2 new.
- **Kind:** 77 are first symptoms and 4 are incidence onsets. None is an observed primary
  infection.
- **Treatment:** 51 untreated, 9 sprayed, 21 unknown.

| Country | Seasons | Sources | Notes |
|---|---|---|---|
| Brazil | 16 | czermainski2004, reis2013, pereira2018, camargo2017, wurz2023, reinehr2021, wurzsilicio2021, ferreira2024 | Bento Gonçalves 1995-2003 to the day; São Joaquim and Canoinhas sprayed, as ranges |
| Georgia | 16 | chrelashvili1993 | Kvareli, 1971-1986: "actual" first appearance (Table 1, p. 126), beside the Müller curve's prediction |
| New Zealand | 10 | brook1992 | Auckland 1971/72-1981/82, no fungicide (sulphur and carbaryl only); Table 7 also gives postulated primary-infection periods with their rain and temperature |
| Germany | 8 | gobbin2005, blaeser1978, eisenmann2023, ziakhan2022 | Rheingau 2000, 1977 sites, Neustadt 2021 (read by eye), Hohenheim 2020 |
| France | 7 | gobbin2005, douillet2023 | Grande Ferrade (Bordeaux) 2019-2021, Merlot, unsprayed until the first symptom, INRAE hourly station on site |
| Serbia | 7 | firanjsremac2018 | Vršac 2012-2018, printed coordinates, in-vineyard station |
| China | 6 | yu2022shelter | Shenyang 2016-2017: open field, rain shelter and sprayed plots |
| Romania | 3 | dina2023, comsa2023 | Murfatlar 2021-2022 (the untreated plots were wetted on purpose), Blaj 2021 |
| Greece | 3 | christoforides2026, rumbou2004 | Kavala 2024 is a bulletin date; Aghialos 2001-2002 rests on the held note only |
| South Africa | 2 | haasbroek2006 | Nietvoorbij and Môrewag 2002, onset between two weekly scores, station coordinates printed |
| South Korea | 2 | gyeonggi2011 | Gyeonggi ARES 2009-2010, untreated Kyoho, institute station |
| Australia | 1 | hug2005 | Caversham 2004, an upper bound only |

Caveats are in each row's `date_how`.
- Gobbin's dates are the first sampling of a survey that "started" when lesions were noticed.
- Several positions are geocoded (±5 km), as `position_how` says.
- `wurz2023`'s "first symptoms" were first-evaluation dates. The held note is corrected, and the
  rows give the symptom ranges.

## Weather sources

| Source | Reach and terms | Rows |
|---|---|---|
| DWD Open Data, Germany | opendata.dwd.de, hourly by station; CC BY 4.0 (its terms file) | German rows; distances not computed |
| Météo-France, data.gouv.fr | "Données climatologiques de base - horaires", hourly by département; Licence Ouverte 2.0 | Bordeaux, Blanquefort, Bommes, Gaillac |
| Agrarmeteorologie Rheinland-Pfalz | wetter.rlp.de, hourly agrometeorological stations; terms not checked | Neustadt 2021 (station within 1 km) |
| INRAE CIMEL station, La Grande Ferrade | hourly T, RH, rain, wetness; on request | Bordeaux 2019-2021 |
| Serbian PIS station VV, Vršac | not open as far as the paper says; on request | Vršac 2012-2018 |
| INMET, Brazil (BDMEP) | bdmep.inmet.gov.br, hourly in UTC; raw station data, no licence found | Garibaldi, Bento Gonçalves |
| Embrapa Uva e Vinho; Epagri/CIRAM; ESALQ | station summaries and data on request; ESALQ says its database is free online | Bento Gonçalves, São Joaquim, Canoinhas, Piracicaba |
| NIWA DataHub, New Zealand | registration, non-commercial or commercial-restricted licence; CliFlo closed 2024 | Auckland (station 450 m from the vineyard) |
| ARC Infruitec stations, South Africa | hourly T, RH, rain, wetness; by request | Nietvoorbij, Môrewag |
| Gyeonggi ARES station; KMA ASOS as fallback | institute data on request; KMA open data with registration | Gyeonggi |
| Paper loggers (Shenyang, Murfatlar, Blaj, Kavala, Hohenheim, Caversham) | in the papers only, as daily or monthly summaries | their rows |
| Not tested | NOAA ISD, Environment Canada, JMA AMeDAS, BoM/SILO (CC BY 4.0), GeoSphere Austria, HungaroMet (unreachable), INIA Uruguay and Chile | no rows yet |

None of these is Meteocat.

## Records

No source is a dataset in the `datasets.py` sense: the seasons are printed tables and text.
- New notes: `ferreira2024`, `wurzsilicio2021`.
- Sections added to 21 held notes, each "Dated seasons (2026-10-28, for Agrarium D64)".

## Not obtained, or not searched far enough

- **North America outside New York: none found.**
  - Madden 2000 (Ohio) has dated incidences but no onset.
  - Michigan, Virginia, Ontario and Quebec extension sources were not reached.
- **Japan and India: none.** Valarmathi & Ladhalakshmi 2020 (doi 10.20546/ijcmas.2020.907.194)
  was not read.
- **Austria, Hungary, Czech Republic, Slovakia, Slovenia, Croatia, Moldova, Bulgaria: none.**
  German advisory bulletins (DLR Mosel, DLR Rheinpfalz, the Bavarian LWG Weinbaufax) carry dated
  oil-spot reports each year. They were found by search, not read: the next place to look.
- **Uruguay, Chile, Argentina: none.**
- Koopman 2007 (Paarl, 2004-2006) was not read.
- Rumbou's ETH thesis was not fetched.
- Hoppmann's Geisenheim oil spots 1989-1995 are in figures only.
