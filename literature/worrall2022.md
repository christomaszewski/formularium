---
id: worrall2022
citation: Worrall, G. & Judge, J. 2022. In-Season Crop Progress in Unsurveyed Regions using Networks Trained on Synthetic Data. arXiv:2212.06896v1 [cs.LG] (preprint)
doi: 10.48550/arXiv.2212.06896
read: 2026-10-27, lightly: abstract, the data and synthetic-generation sections, the training-set design, Table 5 and the conclusions (Tables 6 and 7, per zone, not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [maize]
regions: [United States, Iowa, Illinois, Argentina]
processes: [synthetic data, weather generator, crop growth model, radiative transfer, phenology, crop progress, LSTM, transfer to unsurveyed regions]
records: []
datasets: []
files: [syn1027_worrall2022.pdf (the 2026-10-27 drop)]
---

# Worrall & Judge 2022 (maize, not vine): networks trained on US surveys plus synthetic crop progress, scored on Argentine reports (preprint)

Links a stochastic weather generator, the DSSAT maize model and a PROSAIL-style radiative-transfer model to make synthetic crop-progress series with satellite NDVI for 11 Argentine corn zones, trains a bidirectional LSTM on US survey data, synthetic data, or both, and scores it on real Argentine weekly progress reports. No record: a method; a preprint; maize phenology, not disease.

**Read this first.** A preprint (not peer reviewed), maize crop progress and not a vine or an image. The labels of the synthetic part are computed by DSSAT, so the network inherits that model's phenology, and the authors report a zone where the synthetic data did not match local cultivars and hurt (l. 739, 742). The score is a net F1 on weekly reports of growth stage, by zone. The per-zone tables were not read.

## What it holds

- **Generator** (l. 44, 329 to 331): a Richardson-type spatial stochastic weather generator (Wilks), the DSSAT CSM-IXIM maize model and the PROSAIL-style SPART radiative-transfer model, linked, producing synthetic crop progress and NDVI and growing-degree-day histograms.
- **Numbers** (l. 498, 502): US survey set (Usur), 315 district-seasons (Iowa 2003 to 2020, Illinois 2003 to 2017); synthetic set (Asyn), 1,188 zone-seasons for the 11 Argentine zones. Two further sets combine the US data with synthetic data for the single target zone (Asyn1 Usur) or for all 11 (Asyn Usur).
- **Test** (l. 234): real Argentine weekly crop-progress reports for the 2019/20 and 2020/21 seasons, used only for evaluation and never for development or hyperparameter choice.
- **Net F1, overall** (Table 5, l. 1536 to 1540): US survey data only 0.677; synthetic only 0.618; US plus synthetic for the one target zone 0.723; US plus synthetic for all zones 0.736 (+8.7 % over 0.677, the abstract, l. 55); the in-region reference, trained and tested on US surveys in Iowa, 0.898.
- **Reading** (l. 53, 55, 56): synthetic data improved performance in 9 of 11 zones; overall performance was "only 21 % lower" than the best case (trained and tested in the US Midwest).
- **Where it failed** (l. 739, 742): in Zone III, 2020/21, synthetic data poorly aligned with in-situ progress reduced performance; the authors trace it to synthetic growing degree days to maturity not matching the local cultivars.

## Dependence

- DSSAT CSM-IXIM and SPART/PROSAIL produce the synthetic labels and inputs; the cultivar parameters came from a field study in Argentina (per the reading agent). A stopping rule used validation-loss divergence because no real validation data exist in the target region (per the reading agent).

## Bearing (2026-10-27)

- **D60 (synthetic inputs for real data; synthetic outcomes test robustness):** a worked case where a linked weather generator, a crop model and an RT model supplied the missing region, and the mix was judged on held-out real reports from seasons never used in development. Synthetic alone (0.618) was below US-only (0.677) and the mix (0.736) above it, a +0.06 gain in net F1 (arithmetic, not printed). This is the evaluation shape D60 asks for.
- **D45:** the synthetic labels come from DSSAT, so the network is kin to DSSAT; the real Argentine reports are what show it carries over.
- **Not shown:** a vine, disease or canopy imagery task, error bars, or a score by zone (Tables 6 and 7 not read).
