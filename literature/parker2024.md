---
id: parker2024
citation: Parker, L.E., Zhang, N., Abatzoglou, J.T., Kisekka, I., McElrone, A.J. & Ostoja, S.M. 2024. A variety-specific analysis of climate change effects on California winegrapes. International Journal of Biometeorology 68(8):1559-1571
doi: 10.1007/s00484-024-02684-8
read: 2026-10-27, lightly: data and methods (climate data, varieties, AVAs, phenology models, Table 2 caption), Table 4 captions, limitations (Europe PMC full text; results prose skimmed), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine, Cabernet Sauvignon, Pinot Noir, Zinfandel, Chardonnay, Pinot Gris, Sauvignon Blanc]
regions: [United States, California]
processes: [dataset, phenology model, threshold model, growing degree days, chill completion, climate projection, model output as data, downscaled climate]
records: []
datasets: [parker2024.california_modelled]
files: [syn1027_parker2024calif.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Parker et al. 2024: threshold-model phenology of six California winegrapes in 12 AVAs, 1991-2020 and 2040-2069

An impact study whose released data are simulated stage dates and agroclimatic metrics, not observed phenology. No record: a method on gridded weather, with a dataset of model output.

**Read this first.** The budburst, flowering, veraison and maturity dates are the output of threshold models run on gridded weather and on climate-model scenarios, not field observations (l. 78). Only the contemporary weather is observation-based (a gridded product), and the future weather is downscaled model output. Another dataset paper in this strand (lacuevaperez2026) lists this set among phenology datasets without saying so; a figure caption here calls the contemporary climate "observed" (l. 221), which may have misled it (a guess).

## What it holds

- **Where to get it:** not stated in the lines read of the paper. The data.gov catalogue record "Data from: A variety-specific analysis of Climate Change effects on California winegrapes" (USDA Ag Data Commons) is cited from the reading agent's search and from lacuevaperez2026's Table 2; its licence was not opened. The paper itself is open access under CC BY 4.0 (l. 12).
- **Varieties and sites** (l. 72, 74): six varieties (three red, three white): Cabernet Sauvignon, Pinot Noir, Zinfandel, Chardonnay, Pinot Gris and Sauvignon Blanc; twelve American Viticultural Areas chosen to span California's climates.
- **Weather inputs** (l. 26): daily Tx, Tn, precipitation and reference evapotranspiration for 1991-2020 from the 4-km gridMET product (a gridded blend of PRISM and reanalysis); for 2040-2069 under RCP 4.5, 20 CMIP5 climate models statistically downscaled and bias-corrected (MACA) to gridMET.
- **Models** (l. 78-80): threshold models after Parker & Abatzoglou (2018) for chill completion, budburst, flowering, veraison and maturity. Thresholds (Table 2, l. 80): chilling degree days from Ferguson et al. 2014, growing degree days for the first three stages from Zapata et al. 2017, and BEDD for maturity from Gladstones 1992.
- **Other outputs** (l. 461): 14 general agroclimatic metrics per AVA, among them GDD, cold hardiness, chilling degree days, frost damage days and hot days.
- **How labels were made:** computed by model (threshold phenology models); none observed.
- **Authors' limit** (l. 466): the thresholds "come from trials conducted under different environmental conditions and outside of California" and may not be precise there. No validation of the simulated stage dates against California observations is described in the lines read.

## Dependence

- Ferguson et al. 2014 (held in Formularium as ferguson2014.prosser, per the reading agent), Zapata et al. 2017, Gladstones 1992 and Parker & Abatzoglou 2018 supply the thresholds and the model form; gridMET and MACA supply weather. These are phenology and heat-sum models of the kind the engine's phenology uses (GDD, chill sums), so the set is kin to those formulations, not independent of them.

## Bearing (2026-10-27)

- **Not real data: a synthetic-input example for D60, and a caution for D58.** The set is what a model-computed outcome looks like when released as data: it can say what the threshold models give under a climate, but not whether the thresholds are right. Under D58 it cannot judge a phenology variable; any model trained on it would learn the threshold models.
- **Use:** as a worked case of climate-scenario inputs (downscaled, bias-corrected weather) for stress-testing Agrarium's phenology and disease runs under a warmer climate, labelled synthetic as TRUTH-METHOD requires.
- **Not shown:** any comparison with observed stage dates in California.
