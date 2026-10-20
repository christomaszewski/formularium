---
id: lione2024
citation: "Lione, G., Giraudo, M. & Gonthier, P. 2024. Modelling the front dynamics of invasive plant pathogens through the analysis of spatial gradients. Journal of Plant Pathology 106:1697-1713"
doi: 10.1007/s42161-024-01704-1
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [Heterobasidion irregulare (forest), Ophiostoma novo-ulmi (elm)]
crops: [forest trees, elm]
regions: [Italy (Sabaudia), Sweden (Gotland)]
processes: [spatial gradient, invasion front direction, Monte Carlo validation, open-source R script]
records: []
datasets: []
files: [lione_2024.pdf (the 2026-10-20 drop)]
---

# Lione et al. 2024: DirGrad, the direction of a disease gradient

DirGrad is an open-source R script that finds the compass direction of a disease gradient, and so the likely invasion front. It is validated in silico by Monte Carlo and on two case studies, one forest and one elm.

## What it holds

- In silico: 20 sites placed at random, and a bootstrap of 104 iterations (l. 197, 201).
- Case studies: Heterobasidion irregulare in a forest at Sabaudia, Central Italy, and Ophiostoma novo-ulmi across Gotland, with first foci in 2005 and surveys to 2013 (abstract l. 25-29; l. 105-107).
- The algorithm is released as a user-friendly open-source script (l. 29-30). Its location is not in the text read.

## Dependence

- The authors' linear gradient model of incidence along an octant direction (l. 126-130).
- Gonthier et al. 2014 on the H. irregulare invasion (l. 96). Menkis et al. 2015 on the Gotland survey (l. 108).

## Bearing (2026-10-20)

- Strand t6 (regional spread). The direction test could locate the source of a vineyard incidence front, if incidence is mapped at site level.
- It was tested on forest and elm, not vines, and gives no grapevine numbers. Not read in full.
