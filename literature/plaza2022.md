---
id: plaza2022
citation: Plaza, Maria Pilar, Kolek, Franziska, Leier-Wirtz, Vivien, Brunner, Jens Otto, Traidl-Hoffmann, Claudia & Damialis, Athanasios. 2022. Detecting airborne pollen using an automatic, real-time monitoring system: evidence from two sites. International Journal of Environmental Research and Public Health 19:2471
doi: 10.3390/ijerph19042471
read: 2026-10-18, LIGHT (the text layer: abstract, methods, results on reliability, classification, correlation, discussion; Table 1), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py; no page images or figures
status: read
diseases: []
crops: []
regions: [Germany, Augsburg]
processes: [airborne particles, automatic sampler, sensor error, data gaps, misclassification]
records: []
datasets: []
files: [maria_2022.pdf (the 2026-10-18 drop)]
---

# Plaza et al. 2022: an automatic pollen monitor against a Hirst trap

A BAA500 automatic monitor (Hund; "PoMo") at two Augsburg sites, one 1.5 m above ground
since May 2015 and one 4 m since August 2017, against a Hirst-type trap (0.6 m³ h-1, calibrated
weekly, l. 172-179). Pollen, not spores of pathogens, but an automatic spore sampler of the same
class.

## What it holds

- **Sampler** (l. 185-187): a virtual impactor, airflow up to 6 m³ h-1, 3 m³ per 3-hour
  period, 24 m³ a day; images classified by software.
- **Gaps** (l. 400-405, 915, Table 1): data-flow interruptions 5-10 % within the main season,
  steady over time; whole-day failures above 10 % in most years; a median of 17 and 19 days
  without data in the main season at the two sites (15 pollen types), with some types 1 against
  54 days between sites (Alnus). One monitor was online about 75 % of the time, mostly
  breakdowns of more than 7 days; the Hirst trap about 100 %.
- **Classification** (l. 456-472): one site 993,081 objects checked and 145,699 identified
  automatically; accuracy 85.9 % across 15 taxa (below 80 % for Populus, Quercus, Salix and
  Tilia; above 98 % for Corylus, Picea, Plantago, Taxus, Urticaceae); the other site 83.9 %
  (Populus below 40 %). Misclassification differs by up to almost 30 % between the sites
  (l. 933). Of 58,200 non-pollen objects 87 % were correct, 9 % of spores were called "No
  Pollen" (l. 661).
- **Against the trap** (l. 48-50, 711): daily concentrations r = 0.53-0.55 (significant, weak);
  season start a median 3 days later, peak 5 days later, end 14 days later; the Hirst trap
  reads consistently lower than the monitor in annual total and peak.
- **Not printed:** the second site's object count in the part read (l. 456); data availability.

## Dependence

- The recognition library is Hund's commercial one; the Hirst method is the European
  Aerobiology Society's; the season definition is Persson's. No equation or model.
  Weaker than Oteros et al.'s correlations, which it cites.

## Bearing (2026-10-18)

For strand 5 (sensor error): what an observation model in Agrarium could take (a spore trap
as the observation of airborne inoculum; compare `douillet2023`).

- **Failure:** the main result. An automatic sampler is off for whole days: 17-19 median days
  in a main season, 5-10 % of the time within the days it runs, uptime about 75 % at one site.
  A model could drop days at random at about 10-20 % and in runs of a week, not independently.
- **Bias:** a count that differs from the reference trap in a consistent direction (the trap
  reads lower) and a timing bias of several days (start 3 days, end 14 days late).
- **Noise:** the daily correlation r about 0.54 with the trap, so daily counts carry large
  scatter; misclassification of 15-30 % for some types by site.
- **Threshold, drift:** not given.
- **Kind of result:** a field result, two sites, a commercial instrument; not a datasheet.
- **Can it run:** not as a model; the rates are printed.
