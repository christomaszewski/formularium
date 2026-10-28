---
id: brynjarsdottir2014
citation: Brynjarsdóttir, J. & O'Hagan, A. 2014. Learning about physical parameters: the importance of model discrepancy. Inverse Problems 30:114007
doi: 10.1088/0266-5611/30/11/114007
read: 2026-10-27, lightly: abstract, introduction, the Simple Machine example (sections 3.1 to 3.3, results with and without a discrepancy term); extrapolation, theory and discussion skimmed. The authors' preprint dated 9 June 2014 was read, not the published version. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [model discrepancy, calibration, Gaussian process, synthetic data, bias, over-confidence]
records: []
datasets: []
files: [syn1027_brynjarsdottir2014.pdf (the 2026-10-27 drop)]
---

# Brynjarsdóttir and O'Hagan 2014: ignoring model discrepancy gives wrong parameters with narrow intervals

A toy calibration where the true process is known and the simulator is deliberately a poorer model of it, to show what happens to the fitted parameter with and without a model-discrepancy term. No record: a method with a measured toy result.

**Read this first.** Read as the authors' preprint (9 June 2014); the published paper's wording and numbers may differ. The result is a one-parameter toy with a smooth, one-signed discrepancy, not a measurement on a real system.

## What it holds

- **The claim** (l. 24, 31): an analysis that ignores model discrepancy "may lead to biased and over-confident parameter estimates and" predictions; only with realistic priors on the discrepancy are the true parameter values recovered.
- **Design** (l. 271, 282): synthetic data are simulated "from the true" process zeta(x) = theta x / (1 + x/a) with theta = 0.65 and a = 20; the simulator ignores the loss term, eta(x, theta) = theta x. Measurement error has standard deviation 0.01; n = 11, 31 and 61 observations. The truth is known, so the bias is measurable.
- **No discrepancy term** (l. 315-317): theta is estimated at 0.562 (90 % interval 0.551 to 0.573) for n = 11, 0.564 (0.557, 0.571) for n = 31 and 0.565 (0.560, 0.569) for n = 61, against a true 0.65 outside every interval. The interval narrows with n while the estimate stays about 0.085 below the truth (arithmetic, not printed).
- **In the authors' words** (l. 329-330): "with more and more data from the true process we become more and more sure about the wrong value". Predictions fail too: the posterior for the true value misses even for interpolation (l. 335); the bias persists as n grows (l. 102, 104).
- **An uninformative discrepancy is not enough** (l. 632, 634): a zero-mean Gaussian-process discrepancy gives theta 0.552 (0.477, 0.626) at n = 11 and 0.533 (0.458, 0.607) at n = 61: still low, with the interval no longer shrinking.
- **An informative one is** (l. 663, 665): a prior that encodes known properties of the discrepancy (negative, zero at x = 0, smooth) gives 0.631 (0.610, 0.661) at n = 11 and 0.638 (0.624, 0.659) at n = 61, covering 0.65. Intervals now stabilise without tending to zero (l. 668).

## What TRUTH-METHOD says of it

TRUTH-METHOD part 2: "Ignoring that inadequacy gives biased and overconfident fits (Kennedy & O'Hagan 2001; Brynjarsdottir & O'Hagan 2014)." Its table: "ignoring discrepancy biases parameters" (status snippet).

Verdict: **confirmed, and this is the paper that says it.** The abstract sentence at l. 24 is the claim, and the toy example measures it (l. 315-317, 335). Two limits TRUTH-METHOD should keep: the result is a toy where the true process is known; and a discrepancy term alone did not remove the bias (l. 632-634), only an informative prior did (l. 663-665). Read as a preprint.

## Dependence

- Builds on the Kennedy and O'Hagan 2001 framework (Gaussian-process discrepancy, calibration parameter): see `kennedy2001`. Shares O'Hagan as an author with that paper: a flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 2:** use this paper, not Kennedy and O'Hagan, for "biased and over-confident". It supports an explicit discrepancy variance in history matching, and warns that the variance must be informed, not merely present.
- **D45:** a parameter fitted against a simulator's output with no discrepancy term will be tight and wrong in the same way, whether the target is real data or a truth from a kin formulation; the interval narrowing with n is the warning sign.
- **Not shown:** that the bias is this size in a plant-disease simulator, or that a discrepancy prior can be elicited for one.
