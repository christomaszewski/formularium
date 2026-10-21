---
id: teichmann2024
citation: Teichmann, F., Pichlhöfer, A., Sulejmanovski, A. & Korjenic, A. 2024. Measurement Errors When Measuring Temperature in the Sun. Sensors 24:1564
doi: 10.3390/s24051564
read: 2026-10-21, lightly: abstract, Sections 1-4, Tables 1-2 and figure captions; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 26 of 26 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Austria, Vienna]
processes: [sensor error, radiation error, radiation shield, ventilated shield, wind, air temperature]
records: []
datasets: []
files: [teichmann2024.pdf (the 2026-10-21 drop)]
---

# Teichmann et al. 2024: radiation error of ventilated and non-ventilated temperature shields, against wind

Non-ventilated and fan-ventilated shields and bare probes in front of a white and a black south facade in Vienna, summer 2023, against a shaded reference.

**Read this first.** Table 2 (errors by wind bin) was not checked cell by cell in the text layer; only the figures the text states in prose are used here (l. 521-525). Figures were read from captions and text, not images. The reference is a shaded air sensor under the test stand; the authors still ask for a better one (l. 573-576), and the ventilated shield is not error-free.

## What it holds

- **Set-up** (l. 116-124, 179): a test stand at TU Wien, 8 July to 27 August 2023; per facade a non-ventilated shield, a fan-ventilated shield (about 3 m s-1 at the sensor, l. 115), a bare air probe and a surface probe at 30 cm. Probes +/-0.1 degC and +/-0.5 %rh at 23 degC (l. 165); PT1000 +/-0.3 degC (l. 167).
- **Peaks** (l. 243-247): on 21 August the bare probes read 42.2 and 42.3 degC while the reference peaked at 36.5 degC; non-ventilated shields reached 37.8 to 38.4 degC, ventilated 36.4 and 36.6 degC.
- **Deviation from reference** (l. 305-309): non-ventilated 2.9 and 3.2 degC on 27 July and 4.1 and 4.8 degC on 21 August; ventilated 1.9 and 2.0 degC on 27 July.
- **Full period, Table 1**: non-ventilated minus ventilated 95 % fractile 0.63 degC (black) and 1.13 degC (white) (l. 429, 433). 95 % of errors within +/-2.4 degC (non-ventilated) and +/-1.3 degC (ventilated) on the white facade; +/-2.0 and +/-1.5 degC on the black (l. 571-573).
- **Wind** (l. 439, 522): highest wind 5.4 m s-1. Non-ventilated radiation error below 0.2 degC under 1 m s-1 and 0.56 (black) and 0.82 (white) degC up to 2 m s-1. Sub-1 degC accuracy only at high wind, above 4 m s-1 (l. 555).
- **Not printed:** price; any RH above 90 %, rain or wet test (cloudless summer days only, l. 17-18); drift; failure or data loss. Humidity was not used in the analysis.

## Dependence

- None recorded. The ventilated shield is the authors' own 2022 design (l. 103-112). Cited, not used: Nakamura & Mahrt (ref 9), Lin et al. (ref 7), Kurzeja (ref 8), Richardson et al. (ref 16).

## Bearing (2026-10-21)

Sensor menu of D48 and its observation operators.

- **Error model supported:** a positive air-temperature bias that rises with sun and falls with wind: a draw from the 95 % ranges above, or a rule in radiation and wind (the prose values at 1 and 2 m s-1). A fan shield cuts the 95 % range from about 2.4 to 1.3 degC (white facade). This agrees in kind with nakamura2005.
- **Not measured:** RH or wetness errors, wet periods, price, drift, data loss, packet delivery. The surfaces are building facades with strong reflected heat, not a vine canopy, so magnitudes are an upper case.
- **Kind of result:** a field experiment, one site, one summer, with a shaded reference that is itself imperfect.
