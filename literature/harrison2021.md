---
id: harrison2021
citation: Harrison, R. G. & Burt, S. D. 2021. Quantifying uncertainties in climate data: measurement limitations of naturally ventilated thermometer screens. Environmental Research Communications 3:061005
doi: 10.1088/2515-7620/ac0d0b
read: "2026-11-04, the abstract and sections 4 and 5 (wind speed effects, radiation regimes), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: []
regions: [United Kingdom, Reading]
processes: [thermometer screen, radiation error, wind speed, time response, air temperature]
records: []
datasets: []
files: [dr1104_harrison2021.pdf (the 2026-11-04 drop)]
---

# Harrison & Burt 2021: a naturally ventilated screen's temperature error depends on wind speed

A University of Reading study of the difference between a naturally ventilated thermometer screen and a reference (Tdiff) at 20 s resolution, against wind speed and radiation.

## What it holds

- **Setting (l. 67):** measurements at 2 m height with instruments of the Reading University Atmospheric Observatory, UK, 20 s data (grep, l. 156).
- **Wind threshold (l. 198):** Tdiff is usually small (0.5 °C or less) whenever the low-level wind exceeds about 1 m/s.
- **Spread (l. 223):** the widest spread of Tdiff occurs at low wind, when u2 is below 1 m/s.
- **Regimes (l. 292, 297):** below 0.5 m/s, Tdiff is directly proportional to net radiation and direct radiation exchange dominates; above 1 m/s time response matters more.
- **Time constant (l. 67):** the screen thermometer's time constant rises as u^-0.5 and reaches at least 15 min when calm.
- **Calm and sunny (l. 359):** solar heating dominates the screen error.
- **Table (l. 343):** statistics are split at calm, u2 below 0.5 m/s. The table row is garbled in the text layer and its numbers are not used.

## Dependence

None recorded.

## Bearing (2026-11-04)

- **sense.station_shield_min_wind_ms:** supports a minimum wind of about 1 m/s for a naturally ventilated shield to keep temperature error within 0.5 °C, with radiation error dominating below 0.5 m/s. For Cooptera's station sensing and Agrarium's micro-climate inputs.
- Kind of evidence: a one-site field comparison at 2 m, not a vineyard canopy.
