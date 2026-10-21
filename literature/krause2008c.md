---
id: krause2008c
citation: Krause, A., McMahan, H. B., Guestrin, C. & Gupta, A. 2008. Robust submodular observation selection. Carnegie Mellon University School of Computer Science technical report CMU-ML-08-100, January 2008 (the copy read; the journal version, Journal of Machine Learning Research 9:2761-2801, 2008, is the main session's knowledge and is not checked)
doi: 
read: 2026-10-21, Sections 1-11 (abstract, problem, hardness, Saturate, tightness, examples, extensions, experiments, objective reduction, related work, conclusions) of the long version (technical report, with appendices); appendices A-C (proofs, scalarisation, examples of submodular functions) not read in detail; by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 28 of 28 quotes found at their lines by scripts/verify_quotes.py; the equations were not checked in the page images; figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [USA, California, Berkeley (indoor); USA, Pacific Northwest; USA, California, a lake near UC Merced; a water distribution network of a US metropolitan area, not named]
processes: [sensor placement, robust optimisation, worst-case objective, submodular optimisation, Gaussian process, kriging variance, covariance uncertainty, sensor failure, Saturate]
records: []
datasets: []
files: [krause2008robust.pdf (the 2026-10-21 drop)]
---

# Krause, McMahan, Guestrin & Gupta 2008: Saturate, placement that maximises the worst of several objectives

Chooses k sites to maximise the worst of m monotone submodular objectives (several covariance models, scenarios or failure sets), with an algorithm that keeps the worst-case score of the optimum at the price of a logarithmic factor more sensors. No record: a method. Printed page = PDF page - 4 (a cover, keywords, abstract and a blank page precede page 1).

**Read this first.** This is the long technical-report version; the journal citation is not printed in the file. Almost all results are in Figures 6-12, not tables. Section 8.1 scores placements on the training covariance, with no held-out data. Only Section 8.5 (covariance-model uncertainty) scores on held-out data, 2 days of test data (l. 1500-1502). The guarantee is a bicriterion one: Saturate may use up to alpha k sensors, though the experiments call it with alpha = 1 (l. 430).

## What it holds

- **The problem** (Eq. 2.2, p. 4, l. 240): maximise over |A| <= k the minimum over i of F_i(A), the F_i being normalised, monotone, submodular objectives. Examples: minimising the largest GP kriging variance, F_s(A) = sigma_s^2 - sigma^2_{s|A} (Eq. 6.1, p. 9, l. 496); a worst case over covariance models or parameter settings, F_theta(A) = I(X_A; X_U | theta) (l. 534); outbreak scenarios (l. 607); failed sensors, F_B(A) = F(A \ B), worst case over at most k' failures (l. 631). The GP posterior variance depends on the chosen set, not on the observed values (l. 489).
- **Why greedy fails:** the minimum of submodular functions is generally not submodular (l. 269); greedy can be arbitrarily bad on the worst-case objective (l. 64), for example scoring 2 eps against an optimum of 1 at k = 2 (Table 1, l. 283). Theorem 3 (p. 6, l. 315): unless P = NP no polynomial algorithm that respects the size limit k approximates the maximum within any positive factor.
- **Saturate** (Algorithm 2, p. 7, l. 401-417; Theorem 5, l. 391): binary search on a score level c. At each level it truncates every F_i at c, averages them (Eq. 4.1-4.2, p. 6-7, l. 333-362) and runs greedy submodular cover (Algorithm 1, l. 348). The result has min_i F_i at least the optimum for size k, with at most alpha k sensors, alpha = 1 + log(max_s sum_i F_i(s)). The cost is O(|V|^2 m log(sum_i F_i(V))) evaluations (l. 423), and 10-15 iterations usually sufficed (l. 441). Lazy evaluation with a priority queue speeds it up (l. 437). Theorem 6 (p. 9, l. 457): alpha cannot be improved unless NP is in DTIME(n^(log log n)). F_i are assumed integral (relaxed in Section 7.1 at a cost linear in the number of high-order bits kept).
- **Extensions** (p. 14-17): non-uniform site costs g(s) by cost-benefit greedy (l. 761); path, communication and knapsack costs (Proposition 7, l. 796); a posterior-variance threshold form that guarantees sigma^2_{i|A} <= c at every i (l. 748); a worst-case against average-case trade-off, max F_wc s.t. F_ac >= c_ac (Eq. 7.3, l. 849; Theorem 8, l. 914), whose sweep gives approximately Pareto-optimal sets; for sensor failures the factor improves from O(log |V|) to O(log(k log |V|)) (l. 661).
- **Experiment 8.1, minimax kriging variance** (p. 18, l. 930-1105): three data sets. [T] temperature, 52 sensors at Intel Research Berkeley, 46 candidate locations, empirical covariance of 5 days (l. 933-938). [P] Pacific Northwest precipitation, 167 locations, empirical covariance of 50 years (l. 939). [L] a lake, 86 locations, a nonstationary GP trained on one scan (l. 940). Saturate was "drastically better" than greedy, "very close" to simulated annealing (best of 10 random trials, l. 951), strictly better than it on [P] for 30 or more sensors (l. 960), and 5-10 times faster for larger problems (l. 962-963). Optimising the maximum variance still gave a comparable average variance, not the reverse (l. 1103-1105).
- **Experiment 8.2, robust design** (p. 20, l. 1108-1232): Michaelis-Menten kinetics, 20 experiments, Bayesian A-optimality; Saturate reached an efficiency of 69 %, the robust SDP design 52 %, for the large parameter range (l. 1227-1229).
- **Experiment 8.3, water network** (p. 22-23, l. 1235-1431): 12,527 nodes, adversarial scenarios affecting at least 10 % of the network, 3424 scenarios (l. 1325), objectives Z1 detection time and Z2 population affected. For Z1, greedy "did not improve the objective at all" (l. 1330), because the best achievable F_i(V) is constant. Pareto curves have knees (values in figures only).
- **Experiments 8.4 and 8.5** (p. 25-26, l. 1433-1505): with failures, the failure-robust placement quickly approaches no-failure greedy as sensors are added (Fig. 11 only). For covariance uncertainty, four empirical covariance models from four 6-hour periods of 5 days of [T] training data (l. 1491); Saturate maximises the minimum normalised variance reduction. On 2 held-out days the average RMS error was "roughly equal" to greedy on the all-day model, but the maximum RMS error was larger for greedy, especially for six sensors or fewer (l. 1503-1505; Fig. 12 only).
- **Not covered:** the sequential (adaptive) setting is left as future work (l. 1733); Saturate selects before any measurement.

## Dependence

Builds on Nemhauser, Wolsey & Fisher 1978 (the greedy bound, Theorem 2 here, cited), Wolsey 1982 (greedy submodular cover), Das & Kempe 2007 (submodularity of variance reduction), Krause, Singh & Guestrin (`krause2008`) and Krause & Guestrin 2005 (`krause2005`), Leskovec et al. 2007 (`leskovec2007`, outbreak detection), Flaherty et al. 2006 (robust design baseline), Sacks & Schiller 1988 and Wiens 2005 (annealing baseline). Intel Berkeley temperature and Pacific Northwest precipitation data of the kind used in `krause2008` (46 and 167 candidate locations here). Shared authors only a flag.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): scoring placements and robustness across seasons, with the greedy MI method as the base case.

- **Takeable as is:** SATURATE for a placement that must hold up over several covariance models, seasons (one F_i per season or season class) or failure sets (one F_B per lost node). The F_i must be monotone submodular on the same candidate sites, which variance reduction and mutual information under a given covariance are. It needs only the covariance matrices, and its lazy cost is linear in the number m of objectives.
- **What to decide:** m (how many seasons or models), whether to accept alpha > 1 extra sensors or fix alpha = 1 as the paper's experiments did, and a normalisation of the F_i. Worst-case over seasons will favour the worst season; the worst-case/average-case trade-off (Eq. 7.3) gives a dial.
- **Not shown:** a 2-D field with tens of thousands of targets (the largest GP candidate set is 167 locations); an alert or threshold objective (the objectives are variance and information); mid-season re-planning. Held-out scoring is shown only in 8.5, and the result is a figure.
