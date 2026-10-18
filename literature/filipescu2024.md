---
id: filipescu2024
citation: Filipescu, E., Colucci, G. P. & Trinchero, D. 2024. Design and implementation of a capacitive leaf wetness sensor based on capacitance to digital conversion. IEEE Transactions on AgriFood Electronics 2(2):244-251
doi: 10.1109/TAFE.2024.3401252
read: 2026-10-18, LIGHT, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; an author manuscript from the Politecnico di Torino repository (IEEE postprint); Equation 9 checked in the page image, Equations 1-4 from the text layer only; Figures 13-14 read by eye from the rendered page
status: read
diseases: []
crops: [grapevine]
regions: [Italy, Piedmont]
processes: [leaf wetness, capacitive sensor, sensor drift, dew point, wetness hours]
records: []
datasets: []
files: [elena_2024.pdf (the 2026-10-18 drop, second pass)]
---

# Filipescu, Colucci & Trinchero 2024: a capacitive leaf wetness sensor and one season in a vineyard

A two-sided printed-circuit capacitive wetness sensor read by a capacitance-to-digital converter (FDC2112), calibrated in a chamber and an immersion bath, then run for one season among grape leaves and compared with dew hours from air temperature and humidity. No record: a device paper; the file key is `elena_2024`. The site is not printed.

## What it holds

- **Sensor** (l. 233, 279, 294, 307): FR-4 board (dielectric constant 4.29, 0.36 mm), strips and gaps 6 mil (about 0.15 mm), conditioning circuit Lc 10 uH and Cc 15 pF. Table I (l. 268-270): simulated 611 pF; measured top 625, 636, 623 pF and bottom 609, 628, 636 pF for three boards.
- **Calibration** (l. 312-324): dry and 95 % RH at 23 degC differ by 1.13 pF (top) and 2.10 pF (bottom), read as no RH dependence; 0 degC with dew, and full immersion, differ by 2.77 and 3.22 pF; capacitance is linear in the wetted share (50 % against 50 % rotated, about 0.11 pF, l. 322). Twelve units, 25, 50, 75 % and full immersion (l. 402).
- **Drift** (l. 324, 398): about 3 pF between the start and end of a 3600 s full immersion; the authors call it not significant. This is a bench test over an hour, not a field drift rate; no field drift is reported.
- **Energy** (l. 492, 501): 5.15 mWs per measurement with the boost regulator (7.73 mWs without, l. 418); 20 % of the batteries used over the season.
- **Field** (l. 492, 500): grapevine, March to late October 2023, one season; the site and sensor height are not printed.
- **Wetness hours** (l. 567-584; Figure 13, read by eye, plus or minus about 5 h, not printed): hours per month with the sensor above 50 % wetness, March to October, top about 55, 38, 146, 80, 67, 28, 54, 197 (total about 665); bottom about 52, 80, 181, 86, 68, 36, 61, 172 (about 736). Dew hours from the air sensor's dew point, about 19, 15, 84, 24, 13, 10, 20, 77 (about 262). The text says the sensor records more wetness than the dew-point method (l. 584). No dew-point threshold is printed (l. 571).
- **Cited** (l. 72-77, 662): wetness as the time the temperature-dew point difference is below a threshold, the threshold not printed, after Sentelhas et al. 2008 (RH as an LWD estimator); dew point by Bosen 1958's approximation.
- **Not printed:** any data release or licence, Table III values (not read), a field drift per year, the site.

## Dependence

- Capacitance and inductance per unit length are recomputed after Ghione & Naldi 1983 (l. 185); water permittivity 78.57 from Drake et al. The strip geometry is the group's own earlier design (Filipescu et al. 2023). Calibration is against a chamber and a bath, no other model. The authors are shared with `colucci2026`, which uses this sensor as ground truth: a shared-author flag, and a shared sensor.

## Bearing (2026-10-18)

Strand 5 (sensor error), with strand 4 (measured vineyard microclimate).

- **Drift:** only about 3 pF over 3600 s of immersion; nothing per year. Not a rate to put in an observation model.
- **Threshold, not an RH one:** hours are counted at a sensor reading above 50 %, so the observed wetness depends on this cut as well as on the sensor. Moving it moves the hours, as the 20 % to 40 % labels do in `colucci2026`.
- **Against a dew-point proxy:** one season, chart reads, about 665 and 736 sensor hours against about 262 dew hours, so the sensor counts roughly 2.5 to 2.8 times as many (my division of the chart reads). The proxy is the dew point, not RH >= 90 %. Direction for the engine's stand-in: it likely undercounts wetness hours after rain and from soil evaporation, which the dew point cannot see (Figure 14, 28 to 31 August 2023); the size is not established by a printed number.
- **Kind of result:** a bench calibration plus one season at one unnamed site.
