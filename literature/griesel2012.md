---
id: griesel2012
citation: Griesel, S., Theel, M., Niemand, H. & Lanzinger, E. 2012. Acceptance test procedure for capacitive humidity sensors in saturated conditions. WMO CIMO TECO-2012, Brussels, Belgium, 16-18 October 2012
doi:
read: "2026-11-04, the abstract, introduction and field test section, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: []
regions: [Germany]
processes: [humidity sensor, saturation, capacitive sensor, sensor drift]
records: []
datasets: []
files: [dr1104_griesel2012.pdf (the 2026-11-04 drop)]
---

# Griesel et al. 2012: capacitive humidity sensors read wrongly at and above saturation

A conference paper of the German weather service (Deutscher Wetterdienst, Hamburg, as printed) that proposes an acceptance test for capacitive humidity sensors in saturated air, after field tests showed errors near 100 %RH.

**Read this first.** A WMO instrument conference paper. The sensors tested are not named in the facts read, so this bears on the class of sensor, not on a model.

## What it holds

- **Readings above 100 %RH (l. 19):** in long saturation, capacitive sensors tend to give readings well above 100 %RH and beyond tolerance.
- **Field test (l. 46):** deviations up to +-20 %RH, growing with lower temperature, higher humidity and sensor life time.
- **Near condensation (l. 48):** close to 100 %RH some sensors became inaccurate; the deviation grew with falling temperature.
- **Long wet spells (l. 103):** after long periods above 95 %RH the sensors shift.
- **Saturation test (l. 241):** some sensors read up to 130 %RH.

## Dependence

None recorded.

## Bearing (2026-11-04)

- **f3.zachos_saturated_rh:** capacitive sensors can read above 100 %RH (up to 130 %RH in the test, l. 241) and drift after spells above 95 %RH, so a station's humidity near saturation needs a bias or clip, for Cooptera's stations and Agrarium's wetness inputs.
- Kind of evidence: a national weather service's field and laboratory tests, reported at a WMO conference.
