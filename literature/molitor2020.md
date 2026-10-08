---
id: molitor2020
citation: Molitor, Daniel, Machwitz, Miriam, Dam, Doriane, Bossung, Christian, Junk, Jürgen & Beyer, Marco. 2020. Tätigkeitsbericht 2020 BioViM: Schaderreger-Monitoring und Ableitung ökologischer und umweltschonender Rebschutzstrategien im Weinbau (annual report, IVV and LIST), with appended papers including Molitor et al.'s BotRisk (Int. J. Biometeorol.) and UniPhen (Agric. For. Meteorol. 291:108024)
doi: none
read: 2026-10-08, the report's wetness and Peronospora sections and appendices, the BotRisk and UniPhen papers in full, by a reading agent (claude-sonnet-5-5); 87 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [Botrytis bunch rot, downy mildew]
crops: [grapevine]
regions: [Luxembourg, Germany]
processes: [phenology, season severity, leaf wetness sensing]
records: [molitor2014.shoots]
datasets: []
files: [related-biovim2-2020-compilation.pdf]
---

# Molitor et al. 2020: the BioViM2 annual report, with BotRisk and UniPhen

The 2020 report of the BioViM2 project (IVV Remich and LIST, Luxembourg), in German, with six papers by Molitor and co-authors appended; the reading covered the report's wetness and Peronospora sections and the BotRisk and UniPhen papers.

## What it holds

- The file is the BioViM2 annual report for 2020 (IVV Remich and LIST), with the BotRisk and UniPhen papers appended.
- The report has no leaf-wetness or Peronospora model. Six canopy stations were fitted in 2020, five capacitive wetness sensors each, logged every minute (l. 596, 616, 626). The data are "still being evaluated" (l. 1686). A transfer function to the ASTA station is planned (l. 1790).
- The Peronospora trial is Pinot gris at Remich, inoculated 2020-05-19 (l. 524); first symptoms 2020-06-24 (l. 1412); last leaf severity 0.37 to 17.36 % (l. 1413). The analysis is remote sensing by PLSR (l. 1432).
- BotRisk is for Botrytis on Riesling, not Peronospora. It uses 21 cases: 3 sites x 7 years (l. 2068); Remich 2010-2016 (l. 2183). No wetness input.
- Its target is the CDD7;18;24 after BBCH 65 at 5 % severity, a clock defined in Molitor et al. 2016 and 2014b (l. 2144). The regression has intercept 951.476 (l. 2495) and five temperature or rain terms; adjusted R2 0.6325 (l. 2516).
- UniPhen fits 10/20/30 °C thresholds to Remich phenology, 2012-2018, 11 cultivars, six vines each (l. 3741, 3854, 3799).
- Müller-Thurgau (Rivaner) data of 2014b are not used. The 2014b model was calibrated for it (l. 3813); UniPhen calls its own data "independent" (l. 3990).
- Cross-validation: 53 % within 3 days, 82 % within 7 days (l. 4033).

## Dependence

- **UniPhen computes the engine's phenology equation:** the three-threshold degree-day sum of Molitor et al. 2014 (the engine's `molitor2014.shoots`, here "2014b", lower and upper thresholds 5 and 20 °C), refitted with 10, 20 and 30 °C on its own Remich data, 2012-2018, 11 cultivars (l. 3741-3854). It calls those data independent of the 2014 Müller-Thurgau series (l. 3990): a borrowed equation, not shared data.
- **BotRisk** times Botrytis on Riesling by the same degree-day function (CDD7;18;24 after flowering, from Molitor et al. 2016 and 2014b; l. 2144), regressed on five weather terms (intercept 951.476, adjusted R² 0.6325; l. 2495, 2516), fitted to 21 site-years at Geisenheim, Remich and Deidesheim.
- Molitor, Junk and Beyer are authors of the engine's phenology model: one group, flags.

## Bearing (2026-10-08)

- **UniPhen and BotRisk are kin by a borrowed equation** (the engine's degree-day function), and by form; a truth's phenology should not use them. The report's six canopy wetness stations (five capacitive sensors each, 1-min logging) are a dataset to ask for, once evaluated.
