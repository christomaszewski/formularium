---
id: haasbroek2006
citation: Haasbroek, Pieter Daniel. 2006. Verfyning en verbetering van 'n donsige skimmel waarskuwingsmodel vir die Wes-Kaap (Refinement and improvement of a downy mildew early warning disease model for the Western Cape). M.Sc. Agric. thesis (Agrometeorology), Universiteit van die Vrystaat, Bloemfontein, November 2006
doi:
read: 2026-10-09, contents, methods, results and discussion in full, literature review skimmed, in Afrikaans, by a reading agent (claude-haiku-5-5); 89 quotes checked by scripts/verify_quotes.py; dependence judged by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Western Cape]
processes: [primary infection, infection, sporulation, leaf wetness, forecasting, decision support]
records: []
datasets: [haasbroek2006.westerncape]
files: [wc-haasbroek-donsskimmel-msc.pdf]
---

# Haasbroek 2006: refining a warning model in the Western Cape

A Mediterranean-climate counterpart to Catalonia. It refines a vendor's model rather than
fitting a new one.

## What it holds

- **Starting model:** Metos-2, the Metos programme (Pessl, Austria) run on hourly inputs,
  used at Nietvoorbij since 1995. It says only yes or no.
  - **Primary infection:** 10 mm of rain in 24 h and hourly air temperature of 10 °C or
    more, the 10:10:24 family (credited to Magarey et al. 1994a and Magarey & Wachtel
    1991).
  - **Secondary infection:** 20:00-05:00, RH >= 92 % for 4 h (from Madden et al. 2000), 2 of
    those 4 h with wetness above 0.3, mean 13 °C or more (Magarey & Wachtel 1991).
- **The refined model (DSVW):**
  - **Risk classes:** four instead of yes/no: 0, 1-34, 35-74 and 75-100 %.
  - **Primary scores:**
    - rain from 2.5 mm, a threshold taken from growers' reports;
    - mean temperature from 6 °C;
    - wetness hours up to 15 or more.
  - **Secondary:** RH lowered to 90 %, with temperature classes at 11, 13 and 15 °C.
  - **Leaf wetness:** a regression in powers of 1/RH and of T (to the fifth) replaces the
    sensor, fitted to Nietvoorbij's 2002 sensor data. R² 0.70 in fitting, 0.252 on September-December
    2003.
- **Field data:**
  - weekly disease in untreated plots at Nietvoorbij, 6 November 2002 to 19 February
    2003 (100 leaves, visual);
  - monthly disease classes, 1998-2003;
  - hourly weather at Nietvoorbij, Môrewag (Paarl) and four Robertson stations.
- **Validation:** none against dated infections. DSVW gives 43 primary and 79 secondary
  infection days against Metos-2's 9 and 19 over six season rows (Table 5.1). The
  cumulative Nietvoorbij 2002-03 figure is 84 in the text, while Table 5.2's weekly totals
  sum to 96.
- **Primary infections** come mainly in September-October, secondary ones from November.
- **Not studied:** sporangia survival in heat (sunlight is said to inactivate sporangia).
  Dew is discussed, not modelled.

## Dependence

- Metos-2's primary rule is the 10:10:24 family, the form of the engine's
  `magarey2010.rules`. Its secondary thresholds come from Madden et al. 2000 and Magarey &
  Wachtel 1991.
- DSVW keeps Metos-2's structure and moves its thresholds into classes. Its 15 °C bound and
  wetness classes come from Lalancette et al. 1988a,b.
- The wetness polynomial is fitted to the station's own sensor, close in kind to the
  engine's `cooptera.logistic_wetness` (a model fitted on station sensors).

## Bearing (2026-10-09)

- Not a truth family: kin to the engine through Magarey's rules, and untested against
  observed infections.
- Its weekly and monthly disease records with hourly weather are a Mediterranean-climate
  pattern for history matching (`haasbroek2006.westerncape`). The 2002-03 season is the
  one with weekly data.
- Shows what the METOS rules ([metos2026](metos2026.md)) looked like in 2006.
