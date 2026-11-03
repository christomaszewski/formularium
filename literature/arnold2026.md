---
id: arnold2026
citation: Arnold, G., Possamai, T., Prado, E., Schlemmer, E., Wiedemann-Merdinoglu, S. & Avia, K. 2026. Pyramided resistance ensures grapevine (Vitis spp.) protection during high downy mildew (Plasmopara viticola) epidemic pressure. bioRxiv preprint
doi: 10.64898/2026.02.11.705294
read: 2026-11-03, in full (methods, results and weather skimmed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 10 of 10 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [France (Colmar, Alsace)]
processes: [primary infection event, incubation, first sporulation, resistance loci, Rpv pyramiding, severity scoring]
records: []
datasets: []
files: [dr1103_arnold2026.pdf (the 2026-11-03 drop)]
---

# Arnold et al. 2026: the 2024 Colmar downy mildew epidemic on INRAE ResDur resistant populations

A bioRxiv preprint scoring leaf damage on resistant and susceptible vines at Colmar after the severe 2024 season, with the dates of the first infection event and the first sporulation.

**Read this first.**
- The 2 May infection event is a weather rule applied to station data (rain and mean temperature), not an observation. Only the 13 May sporulation was observed.
- The paper cites the Alsace bulletin (BSV) only for the season's severity (l. 220). The Alsace bulletin of 15 May 2024 says the first spots were found on 13 May (`bsv.france_viticulture`, read 2026-11-03 in that bulletin, not in this paper): the same day.
- It is a preprint; the scoring is one date.

## What it holds

- **Season (l. 214):** persistent rain and moderate temperature at Colmar in 2024, "highly conducive".
- **First infection event (l. 216):** 2 May 2024, when cumulative rainfall was above 10 mm and mean temperature above 10 C, named as thresholds for primary inoculum release. The line does not say which variant of the rule (10-10 or 3-10) it is.
- **First sporulation (l. 218):** observed 13 May 2024, 11 days after the infection event (arithmetic, not printed).
- **Scoring (l. 183):** one date, 2 September 2024; severity as the share of leaf area with symptoms. Per-genotype values are 4 vines averaged (l. 781).
- **Result (l. 35):** susceptible controls 66.6 % symptomatic leaves; Rpv1/3.1 below 16.1 %; the Rpv1/3.1/10 pyramid 4.9 %.
- **Fungicide (l. 177):** treatments on the susceptible controls on two dates only, 3 June and 21 June 2024.
- **Weather (l. 177):** Colmar station daily rain and temperature, shown in Figure 1; not printed as a table.
- **Severity of the year (l. 220):** called one of the most severe outbreaks recorded in Alsace, citing the Alsace bulletin (a citation, not measured here).
- **Data (l. 444, 781):** per-genotype leaf damage (%) is in Supplementary File 7, which covers the INRAE ResDur populations on 2 September 2024; licence all rights reserved.

## Dependence

- Rpv scoring only; no model is computed. Weather is the Colmar station's. The infection-event rule is applied, not fitted. Lead noted by the reader: Possamai et al. 2026 and Rockel 2025 (list of Rpv loci).

## Bearing (2026-11-03)

- **Cooptera (Penedès) and Agrarium, season check:** one Alsace year with a dated rule-based infection event, an observed sporulation 11 days later and an end-of-season severity; field evidence for an incubation and first-symptom date in a mild spring. Kind of evidence: a field observation with a rule-derived start.
- **Agrarium, resistant varieties (a future option):** a high-pressure year where the Rpv1/3.1/10 pyramid kept 4.9 % against 66.6 % on susceptible vines; per-genotype data in Supplementary File 7.
- **Real outcomes:** a row in literature/real_outcomes_2026-11-03.csv (INRAE Colmar 2024, susceptible controls unsprayed until 3 June; first sporulation 13 May).
