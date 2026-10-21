---
id: tasaki2020
citation: Tasaki, Y. (田﨑陽介) & Yoshida, I. (吉田郁政) 2020. 情報の価値 Value of Information に基づく逐次型調査地点最適化 (English title as printed Sequential optimal sampling placement based on value of information). 土木学会論文集 A2 (応用力学) Journal of Japan Society of Civil Engineers, Ser. A2 (Applied Mechanics) 76(2):I_67-I_75 (応用力学論文集 Vol. 23; Japanese text with an English abstract)
doi: 10.2208/jscejam.76.2_I_67
read: 2026-10-21, in full (Japanese main text: introduction, method with equations, synthetic example with a human comparison, conclusion; English abstract; references not read), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 39 of 39 quotes found at their lines by scripts/verify_quotes.py; figures read by caption only; DOI from OpenAlex, not printed in the text
status: read
diseases: []
crops: []
regions: [Japan (authors' institution; the example is a synthetic 32 m x 32 m field with no real site)]
processes: [value of information, sequential sampling placement, Gaussian process regression, kriging, particle swarm optimisation, decision cost, synthetic field]
records: []
datasets: []
files: [tasaki2020.pdf (the 2026-10-21 drop)]
---

# Tasaki & Yoshida 2020: sequential placement of survey points by value of information on a Gaussian-process field

Chooses, five at a time, where to sample next on a spatial field by the expected cost reduction of the new observations (value of information, VoI), with a Gaussian process (GPR) and particle swarm optimisation (PSO), and compares it with human layouts on one synthetic soil-contamination field. No record.

**Read this first.** The text layer loses the glyphs of Equations (3), (7), (8), (10), (12) and (14) and parts of (1); their forms below are partly inferred and marked, not copied. The one example is a single synthetic realisation, with the true field parameters given to the GPR, and the paper warns that a wrong autocorrelation distance can fail to identify the field (l. 376-378). The proposed layout has a higher cumulative VoI than every human layout, but the paper says this is natural because it is chosen by optimising VoI (l. 322, 380): that comparison is circular. No error metric (RMSE, missed area) is given in the text read. Figure values are not in the text layer. The reading agent's summary said four rounds of five; the text says 5 initial points plus three rounds of 5 added, 20 in all (l. 295-296), and that is used here.

## What it holds

- **Problem** (l. 17, 19-20, 36, 103): sampling plans have mostly been designed by experience; the Ministry of the Environment guideline gives a 5-point even layout (cited). The method counts both uncertainty and the risk of exceeding a threshold x0. The decision is whether the value exceeds x0 within an evaluation region.
- **Decision cost** (Eq. 1 and the unnumbered pair beneath it, PDF p. 2, l. 88-100; garbled in part): at each evaluation point the cheaper of "no action" and "action" is taken, with expected costs C11 P11 + C12 P12 and C21 P21 + C22 P22. Type I error (no action when needed) has P12 = 1 - P11 and type II error (action when not needed) P21 = 1 - P22 (l. 88). Example costs C11, C12, C21, C22 = 0, 10, 2, 2, "assumed" and to be set with stakeholders on a real site (l. 288-289).
- **Field model** (Eq. 4, PDF p. 3, l. 163-173; l. 86-87): GPR, which the authors call closely related to kriging and under some conditions equivalent to it (the English abstract says kriging, l. 478). Posterior covariance M^k = M^0 - M^0 (M^0 + R)^-1 M^0 with R the observation error (minus sign confirmed from the raw glyphs).
- **Value of information** (Eq. 9 and Eq. 11, PDF p. 3, l. 145-147, 174-176): the reduction in total expected cost from the new observation is RR = J(k+1) - J(k), and VoI is its expectation, E[J(k+1)] - J(k). The expected cost after the next observation is an integral over the predictive distribution of the candidate-point estimate (Eq. 12, garbled). A direct integral is impractical in high dimension (l. 187); using the reproducing property of the normal distribution it reduces to one dimension (l. 193, cited from Rasmussen & Williams).
- **Optimiser** (Eqs. 13-14, PDF p. 4, l. 217-218; l. 300-302): global optimisation by PSO, because the problem has local optima (Kennedy & Eberhart 1995, cited). Five new points per round make 10 variables (5 points x 2 coordinates), with 150 particles and 150 iterations.
- **Example** (l. 246, 250, 256, 279, 293-296): a synthetic 2-D field of 32 m x 32 m, mean 0.0, SD 1.0 and autocorrelation distance 8.0 m; a value of 1.0 or more counts as contamination, and the true contaminated area splits into three regions. The procedure starts from the guideline's 5 points, then adds 5 points three times, to 20 points in all. The covariance function's shape is not stated.
- **Human comparison** (l. 299, 301, 303, 310, 314): 18 students and 3 others took part (21 people), 12 estimates are shown. They found at most 2 of the 3 sources; those who found only the central source tended to sample only near it. The proposed placement identified the sources better in Figures 3-4, including the two small side regions (l. 312).
- **Cumulative VoI** (l. 380): the proposed layout is higher at every step in Figure 6 (values only in the figure).
- **Limitation** (l. 376, 378): field parameters were set to their true values; a sensitivity test showed the autocorrelation distance matters strongly, and wrong values sometimes failed to identify the field. In a real problem the field parameters must also be estimated.

## Dependence

- The VoI formulation is Yoshida et al. (2019) (ref 18, as cited); GPR from Rasmussen & Williams (2006); PSO from Kennedy & Eberhart (1995). VoI in monitoring elsewhere is cited to Malings & Pozzi (2018) and others. None recorded in the catalogue. A shared author with Yoshida et al. (2019) is only a flag.

## Bearing (2026-10-21)

For Agrarium's D48 study: decision-focused (value of information) placement and the mid-season re-plan. This is a worked spatial VoI with a re-plan after each round.

- **Takeable:** the structure. VoI is the expected cost reduction of the next observations, taken on a spatial Gaussian process with a two-action cost table (no action or action, type I and type II errors); placement is sequential, five points a round, after each round the GPR is updated with what was seen (the re-plan), and the five new points are chosen jointly by PSO over 10 coordinates. This maps onto "which parcels to add a node on, given the spray decision and the costs of a missed against a needless spray".
- **Not shown:** any vineyard or any real field, any random or greedy baseline (the only comparison is human layouts), any error metric, any repeat over random fields, any robustness to an estimated rather than true covariance (the paper says it matters), or any sensor menu. Greedy mutual-information guarantees do not apply here, since VoI is not submodular (see `krause2009`). The kind of result is a method demonstration on one synthetic field.
