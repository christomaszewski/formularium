---
id: temfack2026
citation: Temfack, D. 2026. A Hybrid Mechanistic-Data-Driven Approach for Grapevine Downy Mildew Risk Prediction. Master's thesis, Artificial Intelligence and Data Engineering, Department of Information Engineering, Università di Pisa (discussed 2026-07-22; supervisors Cimino, M.G.C.A. and Calabrese, P.; Bracaloni, S.; repository record etd-07022026-165116)
doi:
read: 2026-10-27, abstract only (a university thesis repository record; the thesis is embargoed until 2096), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 6 of 6 quotes found at their lines by scripts/verify_quotes.py; no thesis text read
status: snippet
diseases: [downy mildew (Plasmopara viticola)]
crops: [grapevine]
regions: [Italy, Tuscany]
processes: [hybrid model, grey-box, mechanistic engine, CatBoost, ERA5 gap filling, station-grouped cross-validation, decision support, forecasting]
records: []
datasets: []
files: []
---

# Temfack 2026: Rossi-engine states as features for a CatBoost downy mildew risk model in Tuscany (thesis, abstract only)

A master's thesis in the wAIne project: an open-source decision support system whose core is a Rossi (2008) mechanistic engine, with the engine's internal states fed as features to a gradient-boosted regressor. No record: a thesis, not a formulation.

**Read this first.** Abstract only; the thesis is not consultable, so there is no sample size, no label description and no number from the thesis beyond "small, not statistically significant". The author's name is hidden on the repository page and is taken from an OpenAlex record, not from the page. It is a thesis, not peer reviewed.

## What it holds

- **Crop and disease, place** (l. 2): grapevine downy mildew in Tuscan vineyards; daily risk; 2025 season.
- **Real data** (l. 2): a 2025 Tuscan season with station weather; ERA5 reanalysis fills gaps in the station weather ("ERA5 weather gap-filling"); a claimed reproducible multi-modal corpus (weather, hyperspectral imagery) with a quality audit. Its availability and licence are not stated.
- **Labels:** not described in the abstract, so a dependence of the labels on the engine cannot be excluded.
- **Synthetic or augmented data:** no synthetic-trained model; real data augmented by a reanalysis for weather gaps (l. 2). The mechanistic engine is deployed on a cloud platform with a bud-burst gate.
- **Hybrid design** (l. 2): "A hybrid grey-box model then feeds the engine's internal states as engineered features into a CatBoost regressor."
- **Validation and score** (l. 2): "Under station-grouped cross-validation on the 2025 Tuscan season, the hybrid improves on a weather-only baseline only by a small, not statistically significant margin". Grouping is by station within one season, so no held-out year; no figures printed.
- **Other channels** (l. 2): "the hyperspectral channel does not help at the sparse coverage available".
- **Transfer** (l. 2): "the Rossi thresholds, calibrated for the Po Valley, are crossed far too early under Tuscan weather and require regional recalibration", named the strongest empirical result.

## Dependence

- Builds on Rossi et al. 2008 (the primary-infection model family; Po Valley calibration). The ML model takes that engine's states as inputs, so it depends on the engine's formulation. A lead for the full text: ask the repository staff or the wAIne project.

## Bearing (2026-10-27)

- **D45 (a model fitted on a formulation is kin to it) and D58:** the only vine hybrid found. Features that are an engine's states make the learned model kin to that engine, and the gain over weather alone was small and not significant on station-grouped folds in one season: a hint that engine states add little to weather for a learned model, not a measured ceiling.
- **D60:** an example of real station data augmented by ERA5; no estimate of the cost of the gap filling is in the abstract. The Po Valley to Tuscany timing result fits the project's transfer caution.
- **Not shown:** any number, the labels, a held-out year; read the full text before any use.
