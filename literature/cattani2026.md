---
id: cattani2026
citation: Malvessi Cattani, Amanda, Zeder, Yanick, Graf, Elias, Schwendimann, Andreas, Coronelli, Roberta, Smit-Sadki, Tara, Burdet, Jean-Philippe, Alfonso, Esteban, Jaccard, Augustine, Niederberger, Erny & Rienth, Markus. 2026. Automated air-flow cytometry enables real-time monitoring of Plasmopara viticola sporangia in vineyards. Applied and Environmental Microbiology 92(4)
doi: 10.1128/aem.02152-25
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; held since 2026-10-07 without a note
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Changins, Nyon, Vaud, Switzerland]
processes: [airborne inoculum, spore detection, sporangia, dispersal, disease assessment]
records: []
datasets: []
files: [2026-cattani-10-1128-aem-02152-25.pdf]
---

# Malvessi Cattani et al. 2026: an air-flow cytometer counts sporangia in real time

Changins's test of the SwisensPoleno Jupiter (holographic imaging, fluorescence, a random
forest classifier) against a Hirst trap and qPCR over two seasons: a real-time sporangia
sensor a truth could treat as an observation of airborne inoculum, with its errors.

## What it holds

- **Classifier:** trained on 11 leaf-derived data sets (8 field, 3 artificial), 43,000 raw
  events cut to about 5,000 after cleaning and a 15-40 µm size filter; random forest with
  balanced class weights, 20 % held out: weighted accuracy 0.75, F1 0.73 over seven
  classes; sporangia and oospores are not separable (l. 273-287, 483-493).
- **2023 pilot** (Changins, August-September, 60 days): inlets at 1.5 and 2.5 m at two
  stations, a Hirst trap at St2 (the Fig. 4 caption says both); R² against the trap only
  0.10-0.30 (l. 316-325, 551-553); Hirst counts correlated with temperature (Spearman r
  0.68) and RH (−0.79) (l. 521-522); disease at the end 64 % of leaves (St1) and 30 % (St2)
  (l. 584-585). The Hirst trap's own relative uncertainty is about 80 % at 10 spores/m³
  (l. 576-578).
- **2024 season** (late April to mid-September, 140 days, BBCH 14 to 89): two instruments
  with 2.5 m inlets in a non-treated and a conventionally sprayed zone, a Hirst trap at
  2.2 m, qPCR of the trap's tape (standard curve R² 0.9949), 17 disease assessments of 100
  leaves a station timed by the Agrometeo risk model, weather from a station 150 m away
  with leaf wetness estimated from the dew point (l. 327-341, 422-450, 610-620). Over the
  season: DNA against Hirst r 0.47; instruments against DNA 0.54 and 0.53, against Hirst
  0.44 and 0.42; the two instruments agree at 0.97 (l. 626-652); nothing significant
  before BBCH 57; r 0.63-0.64 against DNA from bloom to berry touch; from veraison to
  ripening 0.83-0.81 against DNA and 0.94-0.93 against Hirst (l. 654-666). Temperature was
  the strongest correlate of DNA (r 0.64), RH none (l. 710-713). First symptoms near the
  instruments in early June; nearly 100 % of untreated leaves symptomatic by the end
  (l. 702, 732).
- **Inconsistencies:** r = 0.82 between DNA and severity appears only in the abstract
  (l. 31); the conclusion's "up to 0.9" against 0.94 (l. 917); 5 % against 4.5 % of
  slides scanned (l. 358, 501); the 24.69 scaling factor is not derivable from the printed
  sums (l. 502).

## Dependence

- **Observed counts and scores**; the 2024 assessment dates and the leaf-wetness input were
  set by the Agrometeo downy mildew model (VitiMeteo's Swiss form, l. 440-450), so the
  disease series' timing is model-chosen, not the counts.
- **Cited:** the Agrometeo model uses a modelled sporangium density, not measured spores
  (l. 109-111); Lázaro et al.'s 43 % fewer sprays under decision support (l. 898-901);
  Muthukumar et al. 2025 on inlet height (l. 840).
- **Authors:** Alfonso, Burdet, Rienth: `alfonso2025`, `rienth2019`, `rienth2021` flags.

## Bearing (2026-10-13)

- An observation operator for airborne sporangia with stated accuracy: fair agreement
  late in the season under high pressure, none before bloom; the Hirst reference itself
  is 80 % uncertain at low counts. For a truth, the useful numbers are the correlations
  by phenological window and the temperature link; the Agrometeo-timed assessments are not
  an independent disease series.
