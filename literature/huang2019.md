---
id: huang2019
citation: Huang, Y., Zhao, H., Jiang, Y., Lu, X., Hao, Z. & Duan, H. 2019. Comparison and Analysis of Different Discrete Methods and Entropy-Based Methods in Rain Gauge Network Design. Water 11:1357
doi: 10.3390/w11071357
read: 2026-10-21, lightly: abstract, Sections 1 to 5 with the tables and figure captions (text layer partly overlaid), by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [China, Beijing, Haihe Basin, Chaobai River]
processes: [sensor placement, entropy, joint entropy, mutual information, greedy ranking, discretisation, kriging error, rain gauges]
records: []
datasets: []
files: [huang2019.pdf (the 2026-10-21 drop)]
---

# Huang et al. 2019: three entropy objectives and three discretisations for adding rain gauges

Compares three entropy-based greedy objectives (HC, HT, MIMR) under three ways of binning the data, for 40 and 60 gauges in a Chinese catchment. No record: a method comparison.

**Read this first.** The text layer carries two overlaid versions of much of Sections 2 to 5 (a "FOR PEER REVIEW" draft and the final layout), so line numbers need care. Equations 1, 3, 6, 7, 8 and 12 to 16 are garbled; two printed identities disagree (Eq. 6 has a leading minus sign; Eq. 7 reads H(X,Y)-H(Y) where the definition gives H(X,Y)-H(X)) (garbled/unreconciled). The 40 against 45 gauge stability point (l. 1171-1178, 1277-1282) cannot be assigned to methods from the text layer. The existing network is one random draw of 25 gauges (l. 418), with no repetition. Per-network kriging errors are only in Fig. 8.

## What it holds

- **Data** (l. 390, 397, 417, 476, 487): 136,000 km2, 200 gauges, daily June to October rainfall 2006 to 2016 without 2014 (1530 days, 1196 after a correlation screen above 0.5); PERSIANN-CCS satellite rainfall on 909 pixels of 4 km. 25 random gauges are the assumed existing network (l. 418), the rest serve as truth.
- **Discretisation** (l. 156-163): A1 (rounding, bin width 1), SC (Scott), ST (Sturges).
- **Objectives** (l. 253-263, 279): HC (conditional joint entropy), HT (joint entropy minus mutual information, from Alfonso et al.), MIMR (joint entropy, redundancy and mutual information, from Li et al.); greedy ranking to 40 or 60 gauges, giving 9 networks per size.
- **Share of entropy kept** (l. 780, 948, 1415): A1 at least 97.5 % (the authors call a 90 % or 95 % threshold then meaningless); SC 89 % to 93 %; ST 71 % to 79 %.
- **Kriging error** (l. 1232): ordinary-kriging relative error across the nine 60-gauge networks falls from 4.5 % to 2.5 % (Fig. 8). MIMR is more accurate than HC and HT (l. 1442).
- **Recommendation** (l. 1447): MIMR with SC discretisation for rainy-season gauge design. Layouts differ more with discretisation at 40 gauges than at 60 (l. 652); HT is the least sensitive (l. 680).

## Dependence

- Entropy after Shannon (1948); discretisations after Scott and Sturges; HT after Alfonso et al. (ref 22), MIMR after Li et al. (ref 23), HC after ref 32; kriging after Krige. Remote-sensing pixels (PERSIANN-CCS) enter the spatial index. Shared authors: none checked.

## Bearing (2026-10-21)

Greedy mutual-information and entropy placement, and scoring placements, for Agrarium's placement-methods study (PLAN 15, D48).

- **Representative-site clustering:** none. No clustering and no representative; sites are added greedily by an entropy score. This is the entropy comparison for that arm: three entropy objectives are compared with one another, scored by entropy share, a satellite-based spatial index and kriging error. No random layout or clustering method is in the comparison.
- **Takeable:** the result that the binning rule changes both the layout and what an "entropy share" threshold means; a score on real data (kriging error on the unselected gauges) beside the entropy score. Not shown: a repeat over draws of the existing network, or a random baseline.
- **Kind of result:** a method comparison on one catchment and one season set, scored on the gauges not selected.
