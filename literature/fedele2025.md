---
id: fedele2025
citation: Fedele, G., Maddalena, G., Furiosi, M., Rossi, V., Toffolatti, S. L. & Caffi, T. 2025. Relationship between the oospore dose in the leaf litter above the vineyard ground and primary infections by Plasmopara viticola. Frontiers in Plant Science 16:1524959
doi: 10.3389/fpls.2025.1524959
read: 2026-10-08, the author line and sections 2.5 and 3.4; 2026-10-25, in full (Figures 5 and 6 and Table 1 in the page images) by a reading agent (claude-sonnet-5-5), 30 of 30 quotes found at their lines by scripts/verify_quotes.py, and Figure 6, section 3.4 and Table 1 checked again by the main session; open access
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Italy]
processes: [oospores, oospore dose, oospore density, oospore germination, primary infection, primary season]
records: [fedele2025.dose]
datasets: []
files: [fpls-16-1524959.pdf]
---

# Fedele et al. 2025: oospore dose and primary infections

Three seasons (2021-2023) of potted-plot Merlot vines over experimental leaf litters of five
infestation levels at Piacenza: oospores per g of litter against primary lesions per plant.

**Read this first.** The dose regression is a power law, not a line in ln(dose). Figure 6A's
axes (page 12, page image) are "N. oospores/g (Ln)" and "N. lesions / plant (Ln)", and the
text calls it the regression "for the natural logarithm of oospore (x) and DM lesion (y)
numbers" (l. 424-425). So ln(lesions per plant) = −5.386 + 0.786 ln(oospores per g dry
litter), that is lesions per plant per season = 0.00458 × N^0.786 (arithmetic, not printed).
The printed line passes through (9, 1.69) and (13.4, 5.15) on the figure's axes, as that form
gives. Read as lesions = −5.386 + 0.786 ln N it gives about 3.7 lesions at 10⁵ oospores per g,
where the plants carried 21-69. The fit spans the litter means only, and the authors say the
dose did not predict the year: 2023 had the most oospores and the fewest lesions (l. 447-453).

## What it holds

- **Dose unit:** oospores counted under a stereomicroscope, per g of leaf litter, dry weight
  after 24 h at 65 °C (l. 217-218, 338).
- **Litter:** 200 g of leaf pieces per plot in a 2-4 cm layer (l. 156) on 0.6 × 0.6 m of
  cleared ground between two contiguous plants, 0.36 m² (l. 183, 193); about 556 g per m²
  (arithmetic, not printed). Five litters by the share of diseased leaves: LL0, LL25, LL50,
  LL75, LL100.
- **Plants:** Merlot, 0.6 m along the row, rows 2.1 m apart (l. 192); 96 leaves a plant at
  GS 65 (l. 429); leaf area not printed.
- **Doses:** 220 samples, 2,940 to 783,000 oospores per g (l. 470); middle half 33,605 to
  324,000 (l. 472). Year means of the five litters 6.25 × 10⁴ (2021), 4.37 × 10⁴ (2022) and
  4.72 × 10⁵ per g (2023; the exponent's superscript is lost in the text layer, l. 287).
  Litter of leaves with no visible disease (LL0) still held 9.19 × 10⁴ per g, three-year mean
  (l. 300).
- **Germination:** 0.30 ± 0.13 % in the bioassay in 2021, 0.01 % in 2022 and 2023 (l. 291-293);
  "<1 to 1.2 %" in the discussion (l. 513).
- **Observation:** every leaf of each plant from 1 April, weekly, twice weekly after rain
  (l. 290); infected leaves removed; to the end of the primary inoculum season, estimated with
  Rossi et al. (2008b)'s model (l. 284).
- **Lesions:** 33.6, 73.5 and 21.8 per plant in 2021, 2022 and 2023 (l. 404-405); LL100 plants
  had 4 times the lesions of LL0 plants (l. 409); about 2.44 lesions per affected leaf whatever
  the litter (l. 413): the dose changed how many leaves were infected, not lesions per leaf.
  Affected leaves rose from 8.6 per plant over LL0 to 28.7 over LL100 (l. 399).
- **Dose regression (section 3.4, Figure 6):** ln-ln, a = −5.386 (P = 0.044), b = 0.786
  (P = 0.012), R²adj 0.910 for total oospores; a = −2.662, b = 0.753, R²adj 0.924 for
  germinating oospores (l. 425-428). Table 1's correlations (lesions per plant with oospores
  0.941, P = 0.017; with germinating oospores 0.967, P = 0.007) have the p-values of five
  points: the five litter means pooled over years (inferred, not printed).
- **Timing:** 2021: buds broke in early April, no lesions until mid-June, most symptoms from
  mid-July to early August after 71 mm of rain in July (l. 319-321), when Rossi's model gave
  only "the last 10%" of the season's oospore dose as still available (l. 323). 2022: first
  lesions on 16 May. 2023: onset late May to mid-June, and a second onset in the first ten days
  of July after 14 mm on 30 June (l. 351).
- **The authors' caveat:** the experimental litters cannot be compared with natural ones
  (l. 477).

## Dependence

- **Calibrated with Rossi et al. 2008's model,** which set when observations stopped: a
  substantive dependency (`calibrated_with: rossi2008.primary`), found by an adversarial
  review on 2026-10-08.
- Shares authors with Caffi 2013 (a flag only).

## Bearing (2026-10-08)

- The dose formulation of Agrarium's development family F1. A truth using it alone, without
  Rossi's model, would still hold Rossi's model out of the engine.

## Bearing (2026-10-25)

- **Agrarium's truth uses the regression on the wrong scale.** Its registry records
  "lesions = a + b ln(oospores)" (from Cooptera's survey, row 20), and `world/downy_mildew.py`
  computes max(0, a + b ln(dose)) as lesions for each infection event. As published, lesions
  per plant per season = exp(a) × N^b. The two differ by a factor of about 4 at 15,000
  oospores per g, and the code's form gives no lesions below 946 per g (arithmetic, not
  printed). Fedele's fit is for a season's dose and its season of lesions, so splitting the
  season's total by each event's share of the dose matches it; applying the power law to each
  share does not.
- **The dose unit is oospores per g of dry leaf litter.** Agrarium's `dm.primary_dose_scale`
  (15,000) is therefore oospores per g of litter, inside natural leaf-residue counts and far
  below this paper's litters.
- **Cooptera decision 17:** after a dry spring, most of 2021's lesions came in July, when the
  model behind the observation window had almost no dose left (l. 319-323). The field ran
  later than the model's season end.
