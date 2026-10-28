---
id: vernon2010
citation: Vernon, I., Goldstein, M. & Bower, R.G. 2010. Galaxy formation: a Bayesian uncertainty analysis. Bayesian Analysis 5(4):619-670
doi: 10.1214/10-BA524
read: 2026-10-27, lightly: abstract, sections 1 to 3 on the sources of uncertainty and the implausibility measures, the Wave 1 cut-offs, Table 3 and the later waves; the emulator construction, appendices and the results of waves 4 and 5 not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 18 of 18 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [history matching, implausibility, emulator, model discrepancy, Bayes linear, computer model, uncertainty analysis]
records: []
datasets: []
files: [syn1027_vernon2010.pdf (the 2026-10-27 drop)]
---

# Vernon, Goldstein and Bower 2010: history matching a 17-input galaxy-formation model by ruling out implausible inputs

Applies Bayes linear history matching to the Galform galaxy-formation simulator: emulate its outputs from runs, then discard every input whose emulated output is too far from the data, given the model's discrepancy and the data's error, over several waves. No record: a method applied to astronomy (not agriculture or disease).

**Read this first.** The data are astronomical luminosity functions compared with Galform runs, not synthetic data. The variance terms (model discrepancy, observation error) were set by elicited expert judgement (l. 568, 897), so the result is only as good as those judgements.

## What it holds

- **What it does** (l. 15, 19): Bayes linear history matching "to identify the subset of the input space" that gives acceptable matches, handling input, function (emulator), observational, forcing-function and structural (model discrepancy) uncertainty.
- **The model** (l. 302): Galform has 17 uncertain inputs.
- **The rule** (l. 799, 819): implausibility measures the match relative to the tolerance allowed for model discrepancy; discard an input x "unless I(x) < c", with the cut-off c chosen from the fraction of space removed and unimodality arguments.
- **Where 3 comes from** (l. 823-824): the 3-sigma rule of Pukelsheim (1994) when the error is unimodal and continuous: if x is a correct input, implausibility is below 3 with probability "greater than" 0.95 (cited).
- **What the authors used** (l. 2667-2673, Table 3 at l. 2862-2865): 3 or more by the 3-sigma argument, but "unnecessarily conservative", so cut-offs of 2.7 (second maximum) and 2.3 (third maximum) in Wave 1, ruling out about 85.1 % of the input space (the table prints 14.9 % remaining after wave 1). Table 3: wave 1 993 runs, 5 active variables, 14.9 % of space remaining; wave 2 1414 runs, 8 active, 5.9 %; wave 3 1620 runs, 1.6 %; wave 4 2011 runs, 10 active, a maximum-implausibility cut-off of 3.2 added, 0.26 %.
- **What a match means** (l. 490-491): an acceptable match "does not mean that the model is" correct or that the matching parameters are the true values; history matching rules out, it does not certify a best fit.
- **Judgement in the variances** (l. 568, 897): the method relies on elicited judgement of the order of magnitude of discrepancy terms; the filter is built from subjective judgements about the function, the discrepancy and the observation error.

## What TRUTH-METHOD says of it

TRUTH-METHOD part 2: "History matching keeps every input whose output is not implausible against the data, given the model's known inadequacy and the data's error (Craig et al. 1997; Vernon et al. 2010)", and implausibility is "the distance between data and simulation, divided by the combined spread of observation error, model discrepancy and the ensemble". The reference table lists "Implausibility cut-off of 3" with status `memory`.

Verdict: **confirmed, with two details to record.**
- The cut-off of 3 is the 3-sigma rule (P greater than 0.95, l. 823-824), so `memory` can become `read`.
- The authors themselves used 2.7 and 2.3 (l. 2670), with 3.2 for the maximum implausibility from wave 4 (l. 2865), and removed 85.1 % of the space in wave 1 (l. 2673).
- Their variances were elicited judgements (l. 568, 897), and a match is not a certificate (l. 490-491).

## Dependence

- Craig et al. 1996 and 1997 for the implausibility measure and Bayes linear history matching; Pukelsheim 1994 for the 3-sigma rule (all cited, not read). Goldstein is an author of the Craig papers: a shared-author flag with TRUTH-METHOD's other history-matching reference.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 2:** record the cut-off as the 3-sigma rule and say that the authors relaxed it to 2.7 and 2.3. A match proves nothing about the truth, only what is ruled out.
- **D58:** a simulator can be history-matched to rule out inputs, the same role as "the simulator screens candidate variables"; the real data judge what survives.
- **Not shown:** a case with an agricultural or disease model, or with a discrepancy variance set from data instead of judgement.
