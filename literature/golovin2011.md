---
id: golovin2011
citation: Golovin, D. & Krause, A. 2011. Adaptive submodularity: theory and applications in active learning and stochastic optimization. Journal of Artificial Intelligence Research 42:427-486 (as given in the paper's own reference list, l. 2086, and its footnote, l. 48; the copy read is arXiv:1003.3967v5 of 6 December 2017, which has its own pagination)
doi: 
read: 2026-10-21, in full for the abstract, Sections 1-5 (definitions, adaptive greedy, guarantees for maximisation, data-dependent bounds), Section 6 (sensor application), Section 10 (experiments) and Sections 11-14 (adaptivity gap, hardness, related work, conclusions); the statements of the cover theorems 13 and 14; the appendix proofs and Sections 7-9 (set cover, viral marketing, active learning) not read; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py; the equations were not checked in the page images; figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [USA, California, Berkeley (indoor sensor network); USA, California, highway I-880 South]
processes: [adaptive submodularity, adaptive greedy, sequential sensor selection, sensor failure, mutual information, lazy evaluation, data-dependent bound, submodular optimisation]
records: []
datasets: []
files: [golovin2011.pdf (the 2026-10-21 drop)]
---

# Golovin & Krause 2011: adaptive submodularity and the adaptive greedy policy

Defines adaptive submodularity (an item's expected gain does not grow as more items are picked and their states seen) and shows that greedy selection which observes each outcome before the next pick is within (1 - 1/e) of the best adaptive policy. No record: a method. Printed page = PDF page (1-60+ in this version).

**Read this first.** The copy read is the arXiv version (v5, 2017), with its own page numbers; the journal citation is the paper's own, from its reference list and footnote, and no DOI is printed. The sensor experiments are scored on the empirical covariance that built the objective: no held-out data, no random baseline (Section 10). The only adaptivity in the sensing application is a reaction to sensor failure, not to the values observed (l. 1622-1623). Figure 5 holds the timings and bounds; there is no table.

## What it holds

- **Model** (p. 4-5, l. 176, 230): unknown item states form a realization phi with a known prior p(phi). Adaptive maximisation (Eq. 1, l. 230): a policy picks at most k items under every realization, maximising the expected reward f_avg. Adaptive min-cost cover is Eq. 2 (l. 238).
- **Definitions** (p. 7-8, l. 354-390): the conditional expected marginal benefit of an item e given the partial realization psi is Delta(e | psi) (Eq. 8, l. 354). Adaptive monotonicity: Delta >= 0 (l. 381-383). Adaptive submodularity (Definition 3, l. 386-390): Delta(e | psi) does not increase as psi grows. It is defined relative to the distribution p(phi) and may hold for one and fail for another (l. 398). Classical submodularity gives the non-adaptive (1 - 1/e) bound (l. 300, cited to Nemhauser et al. 1978).
- **Adaptive greedy** (Algorithm 1, p. 9, l. 443-488): pick the item with the highest Delta(e | psi), observe its state, update psi, repeat; with item costs, the rule is Delta / c(e) (l. 453). It is the classic greedy plus an observation and a conditioning step after each pick. The accelerated version (Algorithm 2, p. 10, l. 531-549) keeps a priority queue of stale gains and gives the same set, because Delta is non-increasing; the speedup is "roughly 4 to 40" (l. 507).
- **Guarantee** (Theorem 5, p. 11, l. 563-568): for an alpha-approximate greedy policy stopped after l items, f_avg(pi_[l]) > (1 - e^(-l/(alpha k))) f_avg(pi*_[k]); with l = k and alpha = 1 this is (1 - 1/e) of the best adaptive policy with k items. An absolute error epsilon on Delta costs l epsilon, so Delta can be estimated from posterior samples (l. 577-585). If the prior used satisfies c p <= p' <= d p, greedy keeps the guarantee as a d/c-approximate policy (l. 469).
- **Online bound** (Lemma 6, p. 12, l. 613-618): after observing psi, any policy picking at most k items gains at most the sum of the k largest Delta(e | psi); computable during the run.
- **Cover and hardness** (p. 14, 33): min-cost cover within a squared-log factor for the average cost (Theorem 13, l. 712) and within a log factor for the worst-case cost (Theorem 14, l. 745). The adaptivity gap can be Omega(n / log n) for min-sum cover (Theorem 25, l. 1822). Without adaptive submodularity, adaptive maximisation is hard to approximate within O(|E|^(1-eps)) (Theorem 26, l. 1855). It fails for items that act synergistically given observations, and where picking changes the world (l. 428).
- **Sensors with failures** (Theorem 16, p. 17, l. 882; Eq. 26-27, p. 30, l. 1616-1628): with independent per-location states and a monotone submodular f-hat, adaptive greedy gets (1 - 1/e). The objective is the entropy reduction from the readings of the selected sensors that work. With independent failures a non-adaptive policy is at most a factor (1 - 1/e) worse than the adaptive one (Asadpour et al. 2008, l. 1810). For a Gaussian the posterior covariance does not depend on the observed values (l. 1622-1623), so adaptivity here reacts only to failures.
- **Experiments** (Section 10, p. 29-31, l. 1585-1673): Intel Research Berkeley, 46 sensors, 30 s samples for 5 days from 28 February 2004, empirical covariance, failure probability 50 % in the timing plots; and I-880 South traffic speed, 357 sensors, working days 6 AM to 11 AM for one month (l. 1635-1640). Lazy evaluation sped up the temperature set by a factor of about 3.5 to 7 and the traffic set by 30 to 38 (l. 1650-1651); the data-dependent bounds were tighter than the worst-case bound (l. 1670). Timings run on a 2.26 GHz dual core with 4 GB RAM; values are in Figure 5 only.

## Dependence

Builds on Nemhauser, Wolsey & Fisher 1978, Wolsey 1982, Minoux 1978 (lazy evaluation), Feige 1998, Asadpour et al. 2008 (stochastic submodular maximisation), Krause & Guestrin 2005, 2007 and 2009a (`krause2005`, `krause2009`), Deshpande et al. 2004 (the Gaussian sensor model and data) and Leskovec et al. 2007 (`leskovec2007`). Shared author Krause with the other placement notes is only a flag.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): the mid-season re-plan.

- **Takeable:** the adaptive greedy loop (pick a node site, observe, condition, pick the next) as the frame for a mid-season re-plan, with Theorem 5 as its guarantee when the objective is adaptive monotone submodular under the prior, and Lemma 6 as a bound computed along the run. Lazy evaluation carries over.
- **Caveat that decides its use:** a GP posterior variance does not depend on the observed values, so for a variance or mutual-information objective adaptive greedy returns the same placement as non-adaptive greedy, apart from sensor failures. Adaptivity gains arise only when the objective depends on the observations, for example risk above a threshold, the probability that a parcel exceeds an alert level, or failures. That the objective is then adaptive submodular is not shown here and would have to be argued.
- **Not shown:** a re-plan on field data, a continuous (Gaussian) value-dependent objective, held-out scoring, a vineyard-sized candidate set (the largest here is 357 sensors).
