---
id: meynard2013
citation: Meynard, C.N. & Kaplan, D.M. 2013. Using virtual species to study species distributions and model performance. Journal of Biogeography 40:1-8
doi: 10.1111/jbi.12006
read: 2026-10-27, abstract only, as copied on a project page (the paper itself was not obtained: Wiley refused, and the open-archive record holds no file), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 7 of 7 quotes found at their lines by scripts/verify_quotes.py
status: snippet
diseases: []
crops: []
regions: []
processes: [virtual species, species distribution model, synthetic data, threshold simulation, probabilistic simulation, model performance]
records: []
datasets: []
files: []
---

# Meynard and Kaplan 2013: how a threshold turns a virtual species' probability of occurrence into noise-free data, and why scores come out too high

Argues that the common way of making virtual-species data, presence whenever a simulated probability exceeds a threshold, misleads, and that a probabilistic draw should be used instead. No record: a method paper, read as an abstract only.

**Read this first.** Abstract only (status snippet): the case-study numbers are not available. The measured companion is Meynard and Kaplan 2012 (Ecography 35:499-509, doi 10.1111/j.1600-0587.2011.07157.x), also not obtained. Every statement below is the abstract's claim, not a checked result.

## What it holds

- **The practice criticised** (l. 5): "Often a threshold strategy is used to generate virtual occurrences", where presence always occurs above a simulated probability value and never below.
- **Two effects** (l. 6-7): it translates "any shape of simulated species response into a threshold one" and "eliminates any stochasticity from the species occupancy pattern".
- **The remedy** (l. 9): a probabilistic approach "avoids convergence issues with some of the most common" species distribution models, and lets one ask about the shape of functional responses; the threshold response is a particular case within it.
- **Central claim** (l. 10): threshold-based virtual-species studies "generate over-optimistic performance measures" that lack classification error or mix sampling and modelling error.
- **Consequence** (l. 12): low model performance "may be interpreted as due to sample bias or poor model choice, rather than being related to fundamental biological" responses.
- **Evidence** (l. 14): a case study comparing threshold and probabilistic simulation; its numbers are not in the abstract.

## What TRUTH-METHOD says of it

TRUTH-METHOD, The question: "How the virtual species is generated biases which method looks best (Meynard & Kaplan 2013)." Table: "how a virtual species is made biases the comparison" (status snippet).

Verdict: **differs in emphasis (abstract only).**
- The abstract says the threshold generator gives over-optimistic performance measures (l. 10) and misleads on causes (l. 12).
- It does **not** say the generator changes which method wins.
- That dependence is documented elsewhere: Meynard et al. 2019 (`meynard2019`, models built for a response type do better on it) and Thibaud et al. 2014 (`thibaud2014`, a GLM wins on GLM-made species).
- Whether the full paper's case study shows a change of winner is unchecked. The status stays snippet.

## Dependence

- None stated in the abstract. Kaplan and Meynard also wrote `meynard2019` (a shared-author flag).

## Bearing (2026-10-27)

- **TRUTH-METHOD:** keep the citation for "over-optimistic scores when the synthetic truth has no noise"; reword the claim about which method looks best, or cite `meynard2019` and `thibaud2014` for it.
- **D60:** a noise-free generated outcome (l. 7) makes every score too high; synthetic outcomes need a stochastic draw, and are a robustness test, not evidence for a feature.
- **Not shown:** the size of the over-optimism, or any effect on the ranking of methods.
