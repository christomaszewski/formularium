---
id: wallach2016
citation: Wallach, D., Mearns, L.O., Ruane, A.C., Rötter, R.P. & Asseng, S. 2016. Lessons from climate modeling on the design and use of ensembles for crop modeling. Climatic Change 139:551-564
doi: 10.1007/s10584-016-1803-1
read: 2026-10-27, lightly: abstract, sections 2.1 to 2.6 (selection, relatedness, number, statistical model, repository, weighting) and the passages on uncertainty and the ensemble mean; the other sections skimmed. It replaces a triage note of 2026-10-18 (first pages and the located results, by a triage agent and a note writer, claude-haiku-5-5 and claude-sonnet-5-5), whose 2026-10-18 Bearing is kept below; line numbers here are of the 2026-10-27 text copy. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 9 of 9 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [wheat]
regions: []
processes: [crop model ensembles, model relatedness, model dependence, model-as-truth, ensemble spread, multi-model ensemble]
records: []
datasets: []
files: [wallach_2016.pdf (the 2026-10-18 drop; the 2026-10-27 drop fetched the same file)]
---

# Wallach et al. 2016: relatedness and truth-versus-ensemble questions for crop model ensembles

A perspective that carries lessons from climate ensembles to crop-model ensembles (AgMIP). No record: a perspective, with no measured model-as-truth test. This note reads the same paper as `wallach2016`, for the relatedness and ensemble-statistics passages.

**Read this first.** A perspective, not a measured study; the wheat results are cited from other AgMIP papers. It reports no model-as-truth test in crop models.

## What it holds

- **Framing** (l. 81): climate and crop modelling are both fields with many groups building different models of the same system; the paper transfers climate-ensemble lessons to crop models.
- **Closely related models** (l. 151): including them "brings the risk of giving undue weight to a" single modelling approach.
- **A caution for structure tags** (l. 154-155, cited from Palosuo et al. 2011, Martre et al. 2015, Li et al. 2015): crop models with similar equations for processes such as photosynthesis are one way to find relatedness, but "it has not been found that structural similarity leads to similarity in simulated values in crop" ensembles.
- **Dependence by output** (l. 157, cited from Bishop and Abramowitz 2013): examine the covariance in model errors as the measure of dependence.
- **Two sampling hypotheses** (l. 182-186, cited): "truth plus error" (models right on average, each with a random error) against "indistinguishable" (models and truth drawn from the same distribution). The authors say the topic "has not been addressed in the crop modeling community" (l. 186).
- **Common bias** (l. 396, 434): biases shared across models "may cause the truth to fall outside of the ensemble spread"; the ensemble mean may not be best if common biases are present across modelling groups (cited from Bukovsky 2015).
- **Real-data result** (l. 438-439, cited from Martre et al. 2015, AgMIP wheat): with several outputs considered, the mean and median of the ensemble were better predictors "than even the best individual model", the median slightly better than the mean.

## What TRUTH-METHOD says of it

Not cited in TRUTH-METHOD. Verdict: **not in TRUTH-METHOD; no measured crop-model over-confidence figure.**
- It reports no model-as-truth test for crop models (l. 186).
- Its cited finding that structural similarity did not generally give similar outputs (l. 154-155) is a caution for the structure tags in TRUTH-METHOD's kinship rule, and favours measuring dependence from outputs.
- It supports reporting an ensemble rather than the best single model, on real data (l. 438-439, cited).

## Dependence

- Reviews Palosuo et al. 2011, Asseng et al. 2013 and 2014, Martre et al. 2015, Li et al. 2015 and Bishop and Abramowitz 2013 (all cited, none read). Asseng and Wallach also contributed to the AgMIP papers it cites: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 1 and 4:** check the structure tags against output similarity (the earlier `wallach2016` note says relatedness is the dependence question Formularium tracks); the paper itself gives no test.
- **D45:** a fitted model that is "close" to the truth by structure may not be close in output, or the reverse; the output-covariance measure is the cheaper check.
- **Not shown:** any over-confidence figure from a crop-model model-as-truth test; none was found in this strand.

## Bearing (2026-10-18)

- **Strand s6 (methods):** the relatedness of models in an ensemble is the same dependence question Formularium tracks. A simulator could take the relatedness criteria when it counts how independent its ensemble members are.
- Triage-grade: not read in full.
