---
id: krause2005
citation: Krause, A. & Guestrin, C. 2005. Near-optimal nonmyopic value of information in graphical models. Conference on Uncertainty in Artificial Intelligence (UAI) 2005 (venue, year and pages are not printed in the text: the file has no running head; "UAI 2005" is the main session's knowledge, not checked)
doi: 
read: 2026-10-21, lightly (the whole text, 7 PDF pages, with the appendix proofs skimmed; the two-column layout is interleaved in the text layer, so line numbers mix the columns), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py; the equations were not checked in the page images; figure values not readable from the text layer
status: read
diseases: []
crops: []
regions: [USA, California, Berkeley (indoor sensor network); USA, California, San Francisco Bay area (highway traffic)]
processes: [sensor placement, value of information, information gain, submodular optimisation, graphical model, sampling, budgeted selection]
records: []
datasets: []
files: [krause2005uai.pdf (the 2026-10-21 drop)]
---

# Krause & Guestrin 2005: greedy information gain in graphical models

Shows that choosing the most informative subset of variables in a discrete graphical model is submodular when the observed variables are conditionally independent given the hidden ones, so greedy gets (1 - 1/e), and that sampled entropies keep this up to an error epsilon. No record: a method.

**Read this first.** The models are discrete hierarchical Bayesian networks, not a covariance matrix. The guarantee needs the observations to be conditionally independent given the hidden variables; without that, information gain is not submodular (XOR example, l. 151-159). The sample bounds are "very loose for practical applications" (l. 389-391). Experimental values are in Figures 2-3 only. Text-layer line numbers mix the two columns, and the paper itself says "Theorem 10" at l. 390 where it means Lemma 10.

## What it holds

- **Criterion and condition** (Eq. 2.4, l. 124; Proposition 2, l. 167-171): information gain I(V; A) = H(V) - H(V | A), the drop in uncertainty about the unobserved variables. It is submodular and non-decreasing when the observed variables S are independent given the hidden variables U (l. 168); joint entropy is a special case. Joint entropy puts sensors at the border of the field (l. 109, cited to Guestrin, Krause & Singh 2005).
- **Greedy and its guarantee** (Algorithm 1, Proposition 5, l. 232; Theorem 6, l. 249): choose the variable that maximises H(X | A), less H(X | U) for a sensor. It gets (1 - 1/e) of the optimum with O(L |W|) conditional-entropy computations for L sensors from W candidates. The budgeted version, with partial enumeration of d >= 3 starting sets, has the same factor in O(|W|^(d+2)) computations (Theorem 7, l. 239-245). No constant better than (1 - 1/e) is possible unless P = NP (Theorem 9, l. 319). An online guarantee for any other algorithm comes from the greedy set's value (Remark 8, l. 258).
- **Sampling** (Algorithm 3, Lemma 10, l. 298-305; Theorem 11, l. 319-329): conditional entropies are estimated from samples of the model. With absolute error epsilon on the gains, greedy gets (1 - 1/e) OPT - 2 L epsilon with high confidence (l. 315). The result needs polynomial sampling and inference, as in discrete polytrees and bounded treewidth. Subset selection by value of information is NP^PP-complete even on polytrees (cited, l. 53).
- **Experiments** (p. 6-7, l. 357-501): indoor temperature, 30 s samples from 6 am to 8 pm over 5 days from 28 February 2004, tested on the next 2 days (l. 399-403); Bay Area highway traffic, 77 detector stations, 5-minute aggregates, 18 days with the last 2 held out (l. 398-411). Scored by test-set misclassification on the hidden aggregate nodes, against the entropy criterion and random subsets (number of random draws not printed). Five information-gain sensors gave a prediction accuracy that entropy-chosen sensors did not reach even with 20 (l. 357). On traffic, the average information gain of random subsets was slightly higher than that of greedy entropy subsets (l. 487).

## Dependence

Builds on Nemhauser, Wolsey & Fisher 1978 (greedy), Krause & Guestrin 2005 IJCAI (nonmyopic value of information, NP^PP-hardness), Krause & Guestrin 2005 technical report (budgets), Sviridenko 2004 and Khuller, Moss & Naor 1999 (budgeted maximisation), Feige 1998 and Deshpande et al. 2004 (the sensor data). The ancestor of `krause2008` and `krause2009`. Shared authors only a flag.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): a precursor to greedy mutual information (`krause2008`) and value of information (`krause2009`); little new to take.

- **Takeable:** the budgeted greedy with partial enumeration for site costs, and the sampled-entropy route when a model has no closed form, with its error cost 2 L epsilon. Held-out days for scoring and random subsets as a baseline are the same habits as in the later papers.
- **Not shown:** a Gaussian covariance model, a field of tens of thousands of targets, any decision or alert objective, a re-plan.
