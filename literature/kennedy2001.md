---
id: kennedy2001
citation: Kennedy, M.C. & O'Hagan, A. 2001. Bayesian calibration of computer models. Journal of the Royal Statistical Society, Series B 63(3):425-464
doi: 10.1111/1467-9868.00294
read: 2026-10-27, lightly: summary, overview, the sources of uncertainty and the definition of model inadequacy, the review of calibration practice, the model of section 4.2, the discussion of treating known inputs as unknown, and the Tomsk example results; the Gaussian-process algebra not read. Read from an author-circulated copy through OCR, with numbers checked against the OCR line only. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 20 of 20 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [Bayesian calibration, model discrepancy, Gaussian process, computer model, emulator, uncertainty analysis]
records: []
datasets: []
files: [syn1027_kennedy2001.pdf (the 2026-10-27 drop)]
---

# Kennedy and O'Hagan 2001: Bayesian calibration of a computer model, with a model-inadequacy term

Sets out a Bayesian way to fit a computer model's unknown inputs to field data while modelling the model's own inadequacy as a separate function. Illustrated on a Gaussian plume model of a real nuclear release at Tomsk and a simulated accident exercise. No record: a method with one measured example.

**Read this first.** Read through OCR of an author-circulated copy, not the journal page. Equation (5) and its symbols are OCR-garbled, and two table cells lost their decimal point ("042" is read as 0.42, "082" as 0.82). The strong statement TRUTH-METHOD attributes to it, that ignoring discrepancy gives biased and over-confident fits, is only hinted here; it is measured in `brynjarsdottir2014`.

## What it holds

- **Traditional calibration** (l. 14, 325, 328): calibration is "typically effected by ad hoc fitting"; best-fit calibration takes account of observation error, residual variation and inadequacy only implicitly, "through the measure of fit discrepancy", and because the fitted values are treated as known, predictions "take no account of the (remaining) parameter uncertainty".
- **The aim** (l. 19): the Bayesian technique attempts to correct for any inadequacy of the model "revealed by discrepancy between the observed data and the" best-fitting predictions.
- **Definition** (l. 129, 132-133): "No model is perfect. Even if there is no parameter uncertainty" there is inadequacy: the model discrepancy is the difference between the true mean of the real process and the code output at the true inputs.
- **The model** (l. 616, equation partly garbled): observation = a scale factor times the code at the inputs and parameters, plus an inadequacy function independent of the code, plus error.
- **A caution on fixing inputs** (l. 703-704, 715): fixing a parameter at its true physical value forces the misfit into the inadequacy function and "may also lead to" other calibrated parameters "being further from their true physical interpretations": a possibility, no numbers. Setting inputs to their "true" values invests the model with too much credibility.
- **Worked example, Tomsk, Table 1** (l. 1134-1149): the same 10 to 25 observations are used for three strategies. Prediction RMSE at n = 10, 15, 20 and 25: with inadequacy modelled (Strategy 2) 0.42, 0.41, 0.37 and 0.36 (l. 1148, "042" garbled); plug-in best fit without inadequacy (Strategy 3) 0.82, 0.79, 0.76 and 0.66 (l. 1149, "082" garbled); interpolating the data alone (Strategy 1) 0.75, 0.76, 0.86 and 0.79 (l. 1147). The code at prior-mean inputs gives RMSE 0.84 (l. 1137). Modelling inadequacy roughly halves the error at n = 25 (0.36 against 0.66, arithmetic, not printed).
- **With few observations** (l. 1142): a suitably calibrated code is more accurate than interpolating the data.
- **Data** (l. 22): a real nuclear release at Tomsk, and a more complex simulated nuclear accident exercise.

## What TRUTH-METHOD says of it

TRUTH-METHOD part 2: history matching keeps every input whose output is not implausible "given the model's known inadequacy and the data's error"; "Ignoring that inadequacy gives biased and overconfident fits (Kennedy & O'Hagan 2001; Brynjarsdóttir & O'Hagan 2014)". Its table: "model discrepancy". In "Why not the alternatives" it says full Bayesian calibration "needs data rich enough to learn the model's discrepancy".

Verdict: **confirmed for the term "model discrepancy"; only partly for "biased and overconfident".**
- The discrepancy function and its definition are here (l. 129-133).
- The paper names an over-confidence of traditional calibration, but it is about ignored parameter uncertainty (l. 328), not discrepancy; the bias claim is a possibility (l. 703-704), not measured.
- Its one example shows the error roughly halving when inadequacy is modelled (l. 1148-1149).
- "Needs data rich enough" is TRUTH-METHOD's own reasoning: the paper learns the discrepancy from 10 to 25 points in a low-dimensional problem (l. 1134).

## Dependence

- Gaussian plume model as the computer code; O'Hagan's earlier Gaussian-process work. O'Hagan is also an author of `brynjarsdottir2014`, the paper that measures the bias: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 2:** cite this paper for the discrepancy term and `brynjarsdottir2014` for "biased and over-confident". Both are statistical fits of a model to data with a known low-dimensional structure, not plant disease.
- **D45:** a fit that omits discrepancy has a worse prediction error here (0.66 to 0.82 against 0.36 to 0.42, l. 1148-1149); a model fitted on a simulator's truth has, by construction, no discrepancy to the truth to learn from.
- **Not shown:** that a discrepancy term can be learned from the few coarse anchors a disease engine has; TRUTH-METHOD's statement that it cannot is its own judgement.
