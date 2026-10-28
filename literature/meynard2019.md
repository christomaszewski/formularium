---
id: meynard2019
citation: Meynard, C., Leroy, B. & Kaplan, D.M. 2019. Testing methods in species distribution modelling using virtual species: what have we learnt and what are we missing? Ecography 42(12):2021-2036
doi: 10.1111/ecog.04385
read: 2026-10-27, lightly: abstract, the appendix table of major conclusions per topic (response shape, specialisation, resolution, prevalence), the simulation-approach sections (threshold versus probabilistic) and the evaluation-metric caveat; dispersal and software sections skimmed. Read from the authors' open-archive deposit. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [virtual species, species distribution model, synthetic data, threshold simulation, probabilistic simulation, model performance, review]
records: []
datasets: []
files: [syn1027_meynard2019.pdf (the 2026-10-27 drop)]
---

# Meynard et al. 2019: a review of what virtual-species studies have shown about which models do well

Reviews studies that test species-distribution models on virtual species: a known suitability function, converted to presence and absence, sampled, modelled and scored against the known truth. No record: a review.

**Read this first.** Every fact below is the authors' summary of **other** studies; no number from a primary study is in the text read, and no size is given for how much a generator changes a ranking. Read as the authors' open-archive deposit, with a column of citations interleaved in the text layer.

## What it holds

- **Definition** (l. 52): virtual species are "simulations involving a fictitious species" for which the occurrence-environment relationship is known (the virtual ecologist idea).
- **Response shape moves the scores** (l. 158, cited): threshold responses are easier to predict as presence and absence than linear, Gaussian or combined ones.
- **A generator that favours some methods** (l. 170, cited): statistical models designed for one response type (threshold, linear, Gaussian) "tend to perform better" when the virtual species has that response.
- **Classification scores can hide calibration problems** (l. 174, cited): a model may fit response curves that do not match the real ones yet classify well.
- **Specialisation** (l. 179, cited): specialist species are more predictable than generalists.
- **Scaling and generator** (l. 194, cited): scaling studies using a probabilistic approach are under-represented and "may lead to different conclusions than" threshold studies.
- **Prevalence** (l. 197, 207, cited): strong effect of sample bias when sample prevalence differs from species prevalence; threshold studies do not separate rarity (prevalence) from specialisation (niche breadth) and other confounders. The table also says prevalence seems influential mainly above 90 % or below 10 % (table row near l. 197-199).
- **The threshold approach** (l. 345, 354, 249, cited from Meynard and Kaplan 2013): it turns a complex suitability function into a 0/1 probability function, so the true probability of occurrence differs from the suitability the authors think they simulated, and it "will inadvertently confound several" factors. A common mistake is to compare the original suitability with predicted probabilities (l. 336).
- **Scoring advice** (l. 634-636, cited): a model that predicts probability 0.5 correctly is "wrong half the time" if scored on presence and absence; compare true and predicted probabilities instead.

## What TRUTH-METHOD says of it

Not cited in TRUTH-METHOD. It is the same authors' review and the best available stand-in for Meynard and Kaplan 2013 (abstract only; see `meynard2013`) on "how the virtual species is generated biases which method looks best".

Verdict: **supports the claim in a qualitative form.** Across the literature the generator's response shape changes how predictable the species is (l. 158) and models built for a response type do better on it (l. 170), and threshold generators confound prevalence with niche breadth (l. 207, 249). No size is given for a change of ranking in the text read.

## Dependence

- Reviews Hirzel et al. 2001, Meynard and Kaplan 2012 and 2013, Thibaud et al. 2014 and others (none read here except `thibaud2014`). Kaplan and Meynard also wrote `meynard2013`: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 1 and 5:** the generator's form favours methods that share it. This is the argument for the kinship rule and for several unrelated families, and why scores should be reported family by family.
- **D45, D60:** a model fitted on one family's output is the "model designed for that response"; a synthetic outcome should be a stochastic draw, scored on probabilities, not a thresholded label.
- **Not shown:** a measured ranking change from one generator to another; that is in the primary studies, not in this review.
