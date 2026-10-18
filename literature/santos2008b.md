---
id: santos2008b
citation: Santos, Eduardo Alvarez, Sentelhas, Paulo Cesar, Pezzopane, Jose Eduardo Macedo, Angelocci, Luiz Roberto & Monteiro, Jose Eduardo Boffino Almeida. 2008. Spatial variability of leaf wetness duration in cotton, coffee and banana crop canopies. Scientia Agricola 65 (special issue):18-25
doi:
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 51 of 51 quotes found at their lines by scripts/verify_quotes.py; text layer only (Figs 2-4 read from their printed regression labels; Fig. 1 not rendered)
status: read
diseases: []
crops: [cotton, coffee, banana]
regions: [Brazil, Piracicaba]
processes: [leaf wetness duration, canopy position, wetness sensor, station-to-canopy]
records: []
datasets: []
files: [eduardo_2008_2.pdf (the 2026-10-18 drop)]
---

# Santos et al. 2008b: leaf wetness by position in cotton, coffee and banana

Wetness duration measured at several positions inside three crop canopies at Piracicaba, SP
(546 m) and regressed on a turfgrass station less than 2 km away (two flat plates at 45
degrees facing south, 30 cm above the grass; Sentelhas et al. 2004b protocol, l. 159-169).
The companion of `santos2008` (same issue); no DOI is printed. No vine.

## What it holds

- **Crops and periods** (l. 104-154): cotton 29 November 2005 to 14 February 2006 (78 days,
  LAI 1-3, cylinders at 15 degrees facing southwest); coffee, 4 years old, 1.6 m tall, rows 3.5
  m apart, 1 April to 23 June 2006 (74 days; flat plates at 45 degrees at 0.35, 1 and 1.65 m,
  facing northeast and southwest); banana LAI 6, 30 May to 13 July 2006 (45 days; cylinders
  at 15 degrees facing west at 2.3 and 3.3 m).
- **Mean daily wetness by position** (Table 1, l. 179-214): cotton top and lower third both 9.1 h;
  coffee top 12.3 h, inside 13.3, middle third NE 12.7, lower third NE 14.0, middle and lower
  third SW 14.0 and 14.1 h; banana lower third 14.2 h, upper third 16.1 h (Table 1 labels the
  coffee SW positions "SE", read as SW).
- **Onset and dry-off** (Table 2, l. 187, 237, 271-276): coffee onset mean absolute difference
  from the top 44-118 min (mean 78), dry-off 18-85 min (mean 46); cotton onset 16 min earlier
  at the top and dry-off 4 min later; banana onset 96 min earlier at the upper third.
- **Regressions on the turfgrass wetness** (h, Figs 2-4, l. 293-388): cotton top y = 1.01x,
  R² 0.88; cotton lower third y = 1.04x, R² 0.82; coffee top y = 1.05x, R² 0.80; coffee
  middle third NE y = 0.83x + 3.08, R² 0.74; coffee inside y = 0.77x + 4.25, R² 0.65; lower
  third NE y = 0.69x + 5.91, R² 0.55; middle third SW y = 0.69x + 5.96, R² 0.52; lower third
  SW y = 0.70x + 5.85, R² 0.58; banana upper third y = 0.85x + 5.90, R² 0.74, lower third y =
  0.93x + 2.91, R² 0.69. Coffee top about 5 % longer than the turfgrass (l. 402).
- **Position** (abstract, l. 30-33, 219): in coffee the lower parts stay wet longest (middle
  third facing southwest 1.3 h more than facing northeast); in banana the upper third; in
  cotton no difference. The turfgrass relates well only to the top or upper third.
- **Cited** (l. 203, 244, 267): young coffee 1.5 h longer at the lower third (Sentelhas et al.
  2005); apple 8.7 h at the top and 6.8 h at the lower third; tomato east-facing sensors dried
  off 20 min later (Lau et al. 2000).
- **Not printed:** the station's own mean wetness; a DOI; data availability.

## Dependence

- No model; the regressions are the paper's own (a station to canopy relation, compare
  `penaquinones2020` for temperature). The reference protocol and the station approach are
  Sentelhas et al. 2004b and 2005's; shared authors with `santos2008` (a flag).

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take.

- **Bias:** a representativeness bias rather than an instrument bias: the same weather gives
  wetness durations that differ with sensor position by 0 h (cotton) to 1.9 h (banana) and
  1.3 h (coffee, by aspect). In coffee a sensor inside the canopy reads 1 h longer than the top, and one at the
  lower third 1.7 h longer.
- **Noise:** the scatter about the station line (R² 0.5-0.9); onset scatter 44-118 min.
- **Drift, failure, threshold:** not studied.
- **Kind of result:** a field result for three crops over 45-78 days each at one region, one
  sensor type per crop. Not a vine: it says where in a canopy a wetness sensor should sit,
  and that a station on grass does not stand in for it.
- **Can it run:** not as a model; the lines are printed, for these crops.
