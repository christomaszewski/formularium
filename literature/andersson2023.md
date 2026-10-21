---
id: andersson2023
citation: Andersson, T.R., Bruinsma, W.P., Markou, S., Requeima, J., Coca-Castro, A., Vaughan, A., Ellis, A.-L., Lazzara, M.A., Jones, D., Hosking, S. & Turner, R.E. 2023. Environmental sensor placement with convolutional Gaussian neural processes. Environmental Data Science 2:e32
doi: 10.1017/eds.2023.22
read: 2026-10-21, lightly: abstract, introduction, the ConvGNP and data sections, the acquisition-function, oracle and greedy-placement experiments and the conclusions (appendices not in the drop), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Antarctica]
processes: [sensor placement, neural process, Gaussian process, mutual information, greedy acquisition, non-stationary covariance, random baseline]
records: []
datasets: []
files: [andersson2023.pdf (the 2026-10-21 drop)]
---

# Andersson et al. 2023: greedy MI-type placement with a neural-process emulator on Antarctic temperature

Fits a convolutional Gaussian neural process (ConvGNP) to ERA5 daily temperature anomaly over Antarctica, then places 10 new sensors one at a time by information-type acquisition functions, and compares with distance and random heuristics and with GPs. No record: a method.

**Read this first.** The "truth" is ERA5, a reanalysis, so a model field. The formulas of the acquisition functions (JointMI, MarginalMI, DeltaVar, ContextDist) are in Supplementary Appendix F, which is not in the drop; only verbal definitions were read (l. 395-416). Eq. 2 is partly garbled in the text layer. The RMSE and NLL curves (Figs. 4 and 7) are figures; the text gives only a few numbers.

## What it holds

- **Model** (Eq. 1, p. 5, l. 254): the ConvGNP gives a joint Gaussian over targets with a non-stationary covariance (l. 256) learned from data; predictions scale linearly in the number of targets, where a GP is cubic (l. 271).
- **Data and splits** (l. 156, 163, 302-303, 348-349, 419-420): 25 km ERA5 daily 2 m temperature anomaly; training tasks 1950 to 2013, validation 2014 to 2017, test 2018 to 2019; the starting network is the 79 stations active on 15 February 2009.
- **Greedy rule** (Eq. 2, p. 7, l. 385; l. 501-515): the acquisition value of each of S = 1,365 search sites on a 100 km grid (l. 418) is averaged over J = 10^5 dates sampled every 14 days from 2014 to 2017 (l. 420); the maximiser is added, a missing observation is filled with the model mean, and this repeats to K = 10 placements (l. 513).
- **Oracle test** (l. 467-469, 481-482): ConvGNP acquisition against the true gain when ERA5 is revealed at the site: Pearson r 0.90 (JointMI vs joint NLL), 0.93 (MarginalMI vs marginal NLL), 0.93 (DeltaVar vs RMSE); Kendall tau 0.74, 0.82 and 0.84.
- **Placement test** (l. 513, 516-518, 532, 536, 541-542): revealing ERA5 at proposed sites on 243 test dates (2018 to 2019). Model-based criteria beat ContextDist (distance to the nearest sensor) on their own metric from the 5th placement; by placement 10 ConvGNP criteria beat the GP criteria. Random is 5 placements, shown with their standard error. DeltaVar RMSE gain is 0.79 C for the Gibbs GP and 0.77 C for the ConvGNP, while the Gibbs GP starts 0.60 C worse.
- **Limits** (l. 523-524, 555-559): a stationary EQ-kernel GP collapses to ContextDist; cost enters only through a toy Pareto example of DeltaVar against ContextDist, with an unfitted cost model.

## Dependence

- Builds on the ConvGNP of Gordon et al. 2020 and the U-Net, on greedy submodular placement (Krause et al. 2008; budgets from Sviridenko 2004 and Krause et al. 2006), and on GP baselines. Data: ERA5 and BedMachine. No shared-author flag with other notes here.

## Bearing (2026-10-21)

For Agrarium's placement-methods study (PLAN 15, D48): greedy MI-type acquisition with a learned emulator, as an alternative to a covariance matrix.

- **Method:** the only paper here that compares MI-type greedy placement with random (5 draws, l. 536) and a distance heuristic on held-out dates (243 test dates, l. 532), with an oracle check of the acquisition values (r = 0.90 to 0.93, l. 467-469). The emulator (non-stationary, auxiliary inputs) is the part Agrarium would replace with simulated seasons.
- **Scale:** 1,365 candidate and target sites and 10^5 dates per acquisition (l. 418, 420); no run times in the text, and the GP is called cubic (l. 116).
- **Not shown:** a guarantee, sensor cost in the objective, measured field data, a re-plan beyond one site at a time.
