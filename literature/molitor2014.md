---
id: molitor2014
citation: Molitor, Daniel, Junk, Jürgen, Evers, Danièle, Hoffmann, Lucien & Beyer, Marco. 2014. A High-Resolution Cumulative Degree Day-Based Model to Simulate Phenological Development of Grapevine. American Journal of Enology and Viticulture 65(1):72-80
doi: 10.5344/ajev.2013.13066
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Germany, Austria, Italy, Luxembourg]
processes: [phenology]
records: [molitor2014.shoots]
datasets: [molitor2014.mt60]
files: [Molitor_et_al_2013.pdf]
---

# Molitor et al. 2014: a degree-day model of grapevine phenology

From the Luxembourg Institute of Science and Technology (LIST). The source of the engine's `molitor2014.shoots`.

## What it holds

- Model: cumulative degree days (CDD) from observed budburst (BBCH 09) to each BBCH stage 11 to 89, with lower, upper and heat thresholds (l. 252).
- Best triplet 5, 20 and 22 degC (l. 252); one threshold gives 3 degC (l. 244) and two give 5 and 19 degC (l. 247).
- Normalised CV: 0.7511 for three thresholds against 0.8076, 0.7596 and 0.8398 for one, two and forcing units (l. 317).
- Mean CDD to BBCH 89 is 1719.8 degC d (l. 316).
- Data: 60 Muller-Thurgau series from six sites, 1995-2012 (l. 10); Cembra has 5 series, 2008-2012 (l. 125).
- Observed at 50% of vines; intervals two days to one week (l. 81).
- Check: leave-one-out on the same 60 series, 70.6% within 3 days and 95.8% within 7 days at 20 degC (l. 362, 372).
- No site-level provider map; no PHENOCLIM or Ramos data are named (l. 50).
- Dependence: the comparator forcing unit is Caffarra and Eccel 2009 (l. 232); no model dated the data.

## Dependence

- Its own 60 Müller-Thurgau series from six sites, 1995-2012 (Cembra only 2008-2012); no model dated them. The data providers are thanked but not mapped to sites. García de Cortázar-Atauri 2009 and Parker 2011 are cited only for their base temperatures.
- Validation is leave-one-out on the same 60 series.

## Bearing (2026-10-08)

- The engine's model; its record and dataset (`molitor2014.mt60`) are confirmed. Eq. 1 is missing from the text copy.
