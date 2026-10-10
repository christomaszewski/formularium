---
id: firanjsremac2018
citation: Firanj Sremac, Ana, Lalić, Branislava, Marčić, Milena & Dekić, Ljiljana. 2018. Toward a weather-based forecasting system for fire blight and downy mildew. Atmosphere 9(12):484
doi: 10.3390/atmos9120484
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 57 quotes checked by scripts/verify_quotes.py; Table 2 and the day-of-year pairs read by the main session
status: read
diseases: [downy mildew, fire blight]
crops: [grapevine]
regions: [Vojvodina]
processes: [primary infection, incubation, forecasting, season onset]
records: [rule_3_10]
datasets: [firanjsremac2018.vrsac]
files: [p22.pdf]
---

# Firanj Sremac et al. 2018: BAHUS-P on ECMWF forecasts at Vršac

## What it holds

- **Model:** BAHUS-P. The 3-10 rule (cited to Gessler et al. 2011) with the base raised to
  12 °C for Serbia; incubation by the "Milers" degree-day method from BAHUS's own
  references, not printed.
- **Inputs:** ECMWF HRES day-5 forecasts (9 km, 3-hourly) against the plant-protection
  service's stations; daily temperature r² above 0.7 at all seven stations, rain r² 0.02-0.42.
- **Observed (Table 2, VV, Vršac):** shoots at 10 cm and first symptoms. Šasla, untreated,
  except 2013 (Burgundac, treated) and 2018 (Župljanka):

  | Year | Shoots 10 cm | Symptoms | Model end of incubation (DOY) |
  |---|---|---|---|
  | 2012 | 16 May | 1 Jun (153) | 150 |
  | 2013 | 23 May | 5 Jun (156; text 153) | 149 |
  | 2014 | 20 Apr | 19 May (139) | 128 |
  | 2015 | 2 May | 4 Jun (155) | 145 |
  | 2016 | 2 May | 20 May (141) | 147 |
  | 2017 | 5 May | 6 Jun (157) | 134 |
  | 2018 | 18 Apr | 21 Jun (172) | 136 |

- The authors take the symptoms to be the first secondary infection. No skill scores.

## Dependence

- Computes the 3-10 rule, at 12 °C. Dalla Marta, Magarey & Orlandini 2005 is cited for
  over-prediction.

## Bearing (2026-10-09)

- Seven seasons of first symptoms in a continental Pannonian vineyard, with the date shoots
  reached 10 cm: a season-timing pattern outside the Mediterranean.
