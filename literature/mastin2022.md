---
id: mastin2022
citation: "Mastin, A. J., van den Bosch, F., Bourhis, Y. & Parnell, S. 2022. Epidemiologically-based strategies for the detection of emerging plant pathogens. Scientific Reports 12:10972"
doi: 10.1038/s41598-022-13553-y
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [olive quick decline, ash dieback, citrus canker, huanglongbing, ramorum]
crops: [olive, citrus]
regions: [Italy (Apulia)]
processes: [visual inspection, detection lag, diagnostic sensitivity, sample size for pest freedom, PCR of vectors, pooled testing, testing cost]
records: []
datasets: []
files: [mastin_2022.pdf (the 2026-10-20 drop)]
---

# Mastin et al. 2022: visual inspection against host and vector testing for Xylella

A model of how many trees or insect vectors must be checked to declare Xylella fastidiosa ST53 absent in Apulian olive. It compares visual inspection with molecular tests on hosts and PCR on vectors.

## What it holds

- **Sample size for visual surveys:** 10,384 trees, all found asymptomatic, give 90 % confidence that prevalence is below 1 %. This uses best estimates of spread (0.0122 infections per infected host per day) and a 313-day presymptomatic period (l. 413-414, 439). About 80 % of hosts are infected by the time 10 % show symptoms (l. 411-412). Sample size curves against lag, growth and prevalence are in Figs 4B, 5A and 6A, not in the text.
- **Detection lag and sensitivity:** a host test with half the visual lag needs fewer samples only if its sensitivity is over 0.15 (l. 449-450). ELISA costs about 2.67 times a visual check. A perfect test would have to detect infection by 232 days to be cheaper (l. 454-456).
- **Vectors:** 3,106 vectors against 10,384 trees to declare prevalence below 1 % (l. 635-636). Single-vector PCR costs EUR 87,754 against EUR 56,902 for visual inspection. Pooling five vectors cuts the cost to EUR 19,444 (l. 637-640).
- **Visual sensitivity assumed:** visual detection is taken to be perfect after 313 days (l. 713-714). The paper calls this a best case and says little is known of the true sensitivity of visual inspection (l. 717-719).

## Dependence

- Builds on the group's earlier early-detection and pest-freedom work. That covers the pest-freedom method of Bourhis et al. 2019 (ref 11, l. 99), the cost of imperfect detection of Mastin et al. 2019 (ref 12, l. 131) and host and vector targeting of Mastin et al. 2017 (ref 13, l. 323).
- Spread rate and presymptomatic period are "mean estimates ... summarised in Ref.10" (Alonso Chavez et al. 2016, l. 406-407). The logistic growth pattern is cited to its ref 27 (Bourhis et al. 2019, l. 120).
- Host and vector prevalence and density are fitted to Apulian data from Ben Moussa et al. 2016 (ref 20) and Cornara et al. 2017 (refs 22, 28) (l. 314, Fig. 2).
- Costs come from Apulian surveillance estimates (Supplementary Table 2). The ELISA cost ratio is from a personal communication (l. 207-208, 454).

## Bearing (2026-10-20)

- Serves t2 (observation). The useful part for a simulator is the structure: detection lag, sensitivity and cost together set the sample size (l. 449-456). Its visual step is a best case with no sensitivity below 1 (l. 713-719), so a model should not copy it unchanged. The numbers are for olive, not grapevine.
- Not read in full.
