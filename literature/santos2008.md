---
id: santos2008
citation: Santos, Eduardo Alvarez, Sentelhas, Paulo Cesar, Gillespie, Terry James & Lulu, Jorge. 2008. Performance of cylindrical leaf wetness duration sensors in a tropical climate condition. Scientia Agricola 65 (special issue):1-9
doi:
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 56 of 56 quotes found at their lines by scripts/verify_quotes.py; text layer only (Figs 3-6 from the text layer and regression labels, not rendered)
status: read
diseases: []
crops: [turfgrass]
regions: [Brazil, Piracicaba]
processes: [leaf wetness duration, wetness sensor, sensor error, sensor orientation, threshold]
records: []
datasets: []
files: [eduardo_2008.pdf (the 2026-10-18 drop)]
---

# Santos et al. 2008: cylindrical leaf wetness sensors against flat plates

Inexpensive cylindrical wetness sensors (acrylic tube, two nickel spirals 1 mm apart; Weather
Innovations, Ontario) against the standard flat plate (Campbell 237) at 45 degrees, over
mowed turfgrass at Piracicaba, SP (546 m), 93 days of the dry season, July to October 2005.
No DOI is printed. Not the same paper as `sentelhas2008`.

## What it holds

- **Setup** (l. 85-175): sensors 30 cm above the soil facing south, painted with white latex
  and oven-treated (65 °C, 12 h), read every 5 s and averaged over 15 min; daily wetness
  counted from 12:15 to 12:00. The first 40 days all cylinders horizontal; 53 days for the
  angles 0, 15, 30, 45 and 60 degrees.
- **Threshold** (l. 121, 154, 191, 174): wet when the ratio of signal to excitation voltage
  Vs/Vx passes a threshold. Laboratory thresholds 1.2e-4 (flat plate) and 3e-4 (cylinder),
  about 9,000 kOhm in the response test; in the field an individual threshold per sensor from
  the mean signal in the dry period (values not printed).
- **Time response** (l. 206-208): cylinder 73 s on average, flat plate 12 s, all under 3 min.
- **Spread among sensors** (l. 304-324): coefficient of variation of daily wetness of the
  horizontal cylinders 3.2-33.7 %, mean 9.7 %; onset differences -25.7 to +26.2 min and dry-off
  -10.4 to +21.9 min; mean absolute difference 29.5 min at onset and 13 min at dry-off. A
  single threshold for all sensors gave mean differences of -70.3 to +111.2 min, specific
  thresholds -38.5 to +54.1 min (Table 2, l. 221-226).
- **Against the flat plate** (Tables 3-4, Fig. 6, l. 397-513): mean daily wetness 9.0 h (flat)
  and 8.6 h (cylinders, 7.8-9.4 h by angle). Regressions of cylinder on flat plate: slope
  1.01-1.07, intercepts -1.02, -1.70 and -1.46 h at 0, 15 and 45 degrees (none printed at 30
  and 60), R² 0.92-0.96, index of agreement 0.96-0.99. Cylinders at most angles start wetness
  24.6-28.4 min later and end it 18.0-22.5 min later; at 60 degrees the onset is 8.3 min
  earlier. The authors explain it by slower heating and cooling of the cylinder (l. 527).
- **Recommendation** (l. 536): cylinders at 15 to 30 degrees to horizontal.
- **Cited** (l. 40, 112, 479): in a temperate climate cylinders gave about 2 h more wetness than
  flat plates (Sentelhas et al. 2006); vertical cylinders on onion 2-3 h less (Gillespie & Duan
  1987).
- **Garbled** (l. 414): the text says the intercepts do not differ from zero; the printed
  ones do not agree.
- **Not printed:** a height comparison (30 cm only); a DOI; data availability.

## Dependence

- No model. The 45 degree flat plate standard is Sentelhas et al. 2004b's, the paint and heat
  treatment follow Gillespie & Kidd 1978 and Gillespie & Duan 1987. Shared authors with
  `santos2008b` and the cited Elora study (a flag).

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take.

- **Bias:** a wetness-duration bias that depends on the sensor and its tilt: cylinders
  at most angles read about 0.4 h less per day than the flat plate here (8.6 against 9.0 h),
  the opposite sign to the temperate Elora result (about 2 h more). Onset about 25 min later
  and dry-off about 20 min later. So the sign is not transferable between climates.
- **Noise:** daily coefficient of variation of 9.7 % (3-34 %) among identical sensors; onset
  and dry-off scatter of about ±26 and ±20 min.
- **Threshold:** the central finding. Wetness is a threshold on a signal ratio, and the
  threshold choice changes onset by -70 to +111 min with one threshold for all sensors against
  -39 to +54 min with one per sensor.
- **Drift, failure:** not studied.
- **Kind of result:** a field result at one site over 93 dry-season days, with a laboratory
  calibration of the thresholds and the response time. No datasheet figures.
- **Can it run:** not as a model; the ranges only.
