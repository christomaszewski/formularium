---
id: puelles2024
citation: Puelles, M., Arbizu-Milagro, J., Castillo-Ruiz, F. J. & Peña, J. M. 2024. Predictive models for grape downy mildew (Plasmopara viticola) as a decision support system in Mediterranean conditions. Crop Protection (2024), doi:10.1016/j.cropro.2023.106450
doi: 10.1016/j.cropro.2023.106450
read: 2026-10-09, in full in the authors' manuscript (University of La Rioja; journal, volume and pages not printed in it), by a reading agent (claude-haiku-5-5); 60 quotes checked by scripts/verify_quotes.py; the model sections (2.2.1-2.2.4, 3.1.3, 3.2) re-read by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [La Rioja]
processes: [oospores, primary infection, infection, incubation, sporulation, validation]
records: [puelles2024.ur]
datasets: [puelles2024.rioja]
files: [puelles2023_cropprot.pdf]
---

# Puelles et al. 2024: the engine's UR rules, and four models in Rioja

The source of the engine's `puelles2024.ur`. Cooptera holds the journal version; this is
the authors' manuscript.

## What it holds

- **Sites:**
  - eight Rioja vineyards (Tempranillo, Graciano; 452-552 m), 2018-2019;
  - visits every 5-7 days, more often when models signalled;
  - at least 40 untreated vines a plot, beside an agroclimatic station.
- **Goidanich (section 2.2.1):** T >= 10 °C, shoots of 10 cm and 10 mm of rain in 24-48 h
  (Baldacci 1947); then daily incubation from mean RH and T (Goidanich et al. 1957), summed
  to 100 %. Secondary counting after 120 min of wetness. No table printed.
- **Milvit:** incubation from Müller & Sleumer's values, 100 units to symptoms, sporulation
  potential up to 150 and then down to 225; germination at RH > 98 %; sporulation at RH >=
  90 % and 12-29 °C.
- **VitiMeteo-Plasmopara (3.1.3):**
  - oospores mature at 140-160 °C·days above 8 °C;
  - germination at RH > 80 % or 8 h of wetness, with rain > 5 mm in 48 h;
  - infection at 50 °C·h;
  - Milvit's incubation score;
  - sporulation at RH > 92 % and T > 12 °C for 4 h in the dark.
- **UR model (2.2.4, 3.2):** "the same algorithm as the Goidanich model to predict primary
  infection cycles", adjusted:
  - **Oospores:** sum (Tm - 8) from 1 January to 140-160 °C (Gehmann et al. 1987); 160 °C
    chosen "(data not shown)".
  - **Germination:** rain > 5 mm in 48 h (Dubuis et al. 2012), at T >= 12 °C (Gessler et
    al. 2011); host susceptible from 10 cm shoots.
  - **Infection:** Σ degree·hours > 50 °C during leaf wetness (Eq. 2; Dubuis et al. 2012):
    "two hours at 25 °C or four hours at 12.5 °C".
  - **Sporulation:** RH > 95 % or wetness, 12-29 °C, 4 h of darkness.
  - **Spore death:** more than 6 h above 30 °C (Blaeser & Weltzien 1979).
  - **Incubation:** Goidanich's, unchanged.
- **Results:**
  - Plot-seasons where predicted and observed infection blocks matched: UR 9 of 16 (6 of
    8 in 2018, 3 of 8 in 2019), Goidanich 2, VitiMeteo 2, Milvit 1 (Table 5).
  - Regression of predicted on observed blocks: R² 0.78 for Goidanich, 0.8643 for UR.
  - Average distance from y = x: 1.6412 against 0.5757 (Table 6). The regressions' n is
    not printed.
  - Text and Table 4 disagree in places (listed by the reader).

## Dependence

- **The UR model computes three engine models' equations or forms:**
  - Goidanich's incubation (the record's `borrows`);
  - the 3-10 conditions, which Cooptera's list does not name (flagged; Cooptera asked);
  - a VitiMeteo-type oospore threshold, wet degree-hours infection, and dark moist hours
    and temperature-band sporulation. The structure tags are now recorded.
- **Its oospore rule is Gehmann et al. 1987's** ([gehmann1987](gehmann1987.md)), the same
  form as `vitimeteo.oospores`.
- **Fitting:** the adjustments were tuned after mismatches on these plots and judged on
  the same plots (`puelles2024.rioja`). No data were held out.

## Bearing (2026-10-09)

- `puelles2024.ur` is kin to a truth using any of Goidanich's table, the 3-10 rule, a
  degree-day oospore threshold, wet degree-hours infection, or dark-hours sporulation.
- The eight Rioja plots are a Mediterranean pattern of first symptoms, but the visit
  schedule followed the models' signals.
