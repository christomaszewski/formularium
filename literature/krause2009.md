---
id: krause2009
citation: Krause, A. & Guestrin, C. 2009. Optimal value of information in graphical models. Journal of Artificial Intelligence Research 35:557-591 (journal, volume and pages as printed on the first page; DOI from OpenAlex, 2026-10-21, not printed in the text)
doi: 10.1613/jair.2737
read: 2026-10-21, in full (title, abstract, Sections 1-9; appendix proofs skimmed for what they establish, references not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 57 of 57 quotes found at their lines by scripts/verify_quotes.py; the equations were not checked in the page images; figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [Intel Research Berkeley indoor sensor network (country not printed in the text); building lighting testbed (place not stated)]
processes: [value of information, decision theory, conditional planning, dynamic programming, sensor scheduling, sensor placement, submodular optimisation, chain graphical model, hotspot detection]
records: []
datasets: []
files: [jair2009.pdf (the 2026-10-21 drop)]
---

# Krause & Guestrin 2009: optimal value of information on a chain

Gives exact dynamic programs for choosing which variables of a chain graphical model to observe, by decision-theoretic value of information, as a fixed subset or as a plan that reacts to the values seen. It proves the general problem intractable and value of information not submodular. No record: a method. Printed page = 556 + PDF page.

**Read this first.** The exact algorithms need a chain (or a tree with a constant number of leaves); the paper has no 2-D spatial experiment and no Gaussian-process placement. The only chain experiment on sensor data is a time-scheduling task (24 hours of one day) that is learned from, and scored on, the same series: no held-out score, no random baseline (l. 998). Complexity expressions are garbled in the text layer ("61 n3" is n^3/6, l. 539, 805-808). Proposition 9's proof numbers are garbled and were reconstructed (l. 1792-1795). Figures 3 and 5 hold the experimental values; none are in tables.

## What it holds

- **Setting** (Eq. 1, p. 559, l. 149): choose a set A of observed variables to maximise the expected reward R of the posterior over all variables, summed over the values x_A that could be seen. A conditional plan (Eq. 2, p. 560, l. 169) lets the next observation depend on the values already seen. Observations are priced by a penalty C_j subtracted from the reward or by an integer cost beta_j against a budget B (l. 334).
- **Reward catalogue** (p. 561-562, l. 230-311): residual entropy (l. 230); decision-theoretic value of information R_j = max over actions a of the expected utility EU_j(a | x_A) (l. 267); a margin between the best and runner-up max-marginals (l. 279); weighted conditional variance -w_j Var(X_j | x_A) (l. 290); the hotspot reward P(X_j in C_j | x_A), the probability that X_j lies in a critical region C_j (l. 301); and the conditional mean (l. 311). Rewards are summed over variables (Eq. 3, p. 565, l. 431).
- **Chain assumption** (l. 348, 394): X_i is independent of the rest given its neighbours, so the reward decomposes over the sub-chains between consecutive observed variables (l. 404). Non-stationary transitions are allowed (l. 353). For a Gaussian linear chain the same subset DP applies when the inference is tractable (l. 544).
- **Exact subset selection** (Algorithm 1, p. 566, l. 501-519; Theorem 1, l. 539): dynamic programming over sub-chains (recursion on p. 565, l. 490) selects the optimal subset for budget B in (n^3/6 + O(n^2)) B evaluations of expected local rewards. The budget need not be split between sub-chains for subset selection (l. 524).
- **Exact conditional planning** (Algorithm 2, p. 570, l. 741-780; Theorem 2, l. 805-808): the optimal plan costs d^3 B^2 (n^3/6 + O(n^2)) evaluations with smoothing, d^3 B (n^3/6 + O(n^2)) with filtering, and d^3 (n^4/6 + O(n^3)) with filtering and no budget; d is the largest domain size of the discrete variables. The plan is a table of polynomial size, run by one lookup per decision (l. 793, 801). Subset selection is only about a factor d B cheaper (l. 814). Trees with a constant number of leaves keep it polynomial (l. 845).
- **Hardness** (p. 573): computing decision-theoretic value of information is #P-complete for Naive Bayes and hard to approximate unless P = NP (Theorem 3, l. 909); subset selection is NP^PP-complete on discrete polytrees (Theorem 5, l. 927) and for two dependent chains (Corollary 7, l. 1098).
- **Not submodular** (Proposition 9, p. 584, l. 1507, 1517; example l. 1783-1795): decision-theoretic value of information is monotone (Proposition 8, l. 1154) but not submodular, even for Naive Bayes, so greedy has no (1 - 1/e) guarantee. Counterexample: binary class, two conditionally independent observations each right with probability 3/4, utility +1 right, -3 wrong, 0 abstain; the value is 0 for the empty set and for each observation alone, but 6/16 for both (reconstructed, garbled in the text).
- **Several sensors, one chain each** (Algorithm 4, p. 579, l. 1241-1253): coordinate ascent. Each sensor's schedule is re-optimised with Algorithm 1 while the other sensors are fixed at their most recent observation, which lowers the objective (Proposition 8, l. 1161). It converges to a local optimum with no performance guarantee (l. 1225) and is at least as good as scheduling the sensors independently (l. 1229). The naive reward is exponential in the number of chains; sampling (Hoeffding, l. 1214) or approximate inference (l. 1219) is suggested.
- **Experiments** (p. 574-580): (a) hourly indoor temperature at Intel Research Berkeley, 19 days, 10 bins of 2 K, pseudo counts 0.5, 53 series from three adjacent sensors, four time-of-day transition sets, k of 24 hours chosen (l. 986-995); optimal beat greedy and uniform spacing by "several percent" of expected entropy decrease when k is below about half the candidates (l. 999; Fig. 3a only); (b) CpG islands in three gene loci: with 6 observations, 25 % lower classification error than greedy (l. 1029); (c) entity tagging on 50-word sequences: three of 50 labels raise mean F1 by more than five percent (l. 1049); (d) a building lighting testbed, three sensors, Algorithm 4: one observation per sensor gives utility close to continuous sensing, and network lifetime could rise by a factor of 3 (l. 1273, 1282, 1327; Fig. 5). No run times in seconds anywhere.

## Dependence

Builds on Krause & Guestrin 2005 (`krause2005`, the UAI version and a previous version of this paper), Krause, Singh & Guestrin (`krause2008`), Krause et al. 2008 (`krause2008b`), Nemhauser et al. 1978 (greedy), Singhvi et al. 2005 (the lighting testbed), Deshpande et al. 2004 (the Intel Berkeley data) and Boyen & Koller 1998 (approximate inference). Shared authors with the other placement notes are only a flag. No crop or disease model.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48), the decision-focused (value of information) method and the mid-season re-plan. This is the decision-theoretic source; its exact algorithms do not run on a field.

- **Not usable as is on the vineyard:** a 2-D field of correlated vines is not a chain or a few-leaf tree, selection is NP^PP-complete beyond that, and value of information is not submodular, so a greedy node choice has no guarantee from this paper (l. 1507). Greedy guarantees hold for submodular surrogates (mutual information, variance reduction); see `krause2008`.
- **Takeable:** (1) time as a chain at one site, for scheduling when a node or manual check is made, by Algorithm 1 (subset) or 2 (plan); (2) Algorithm 4 as a heuristic for several nodes (no guarantee, local optimum); (3) the reward catalogue, in particular the hotspot reward P(X_j in C_j | x_A), which matches "is a parcel above an alert threshold", and the best-action reward max_a EU_j for an alert versus no-alert decision.
- **Not shown:** any spatial placement, any held-out score, any run time, a sensor menu beyond a cost per observation. The kind of result is a complexity map plus a small chain demonstration.
