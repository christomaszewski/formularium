---
id: gobbin2006
citation: Gobbin, D., Rumbou, A., Linde, C. C. & Gessler, C. 2006. Population genetic structure of Plasmopara viticola after 125 years of colonization in European vineyards. Molecular Plant Pathology 7(6):519-531
doi: 10.1111/j.1364-3703.2006.00357.x
read: 2026-10-09, in full by a reading agent (claude-haiku-5-5), the publisher's open copy; the counts, diversity, FST and isolation-by-distance figures checked in the text by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Europe, Greece, Italy, France, Switzerland, Germany]
processes: [epidemic structure, population genetics, dispersal]
records: []
datasets: [gobbin2006.europe]
files: []
---

# Gobbin et al. 2006: P. viticola's population structure across Europe

The survey behind [rossi2013](rossi2013.md)'s genotype patterns, analysed for population
genetics. Its own results are diversity, mating and differentiation. The epidemic-structure
figures Rossi, Caffi & Gobbin 2013 quote are cited here from Gobbin et al. 2005 and Rumbou
& Gessler 2004 and 2006, not measured.

## What it holds

- **Sampling:**
  - **Plots and lesions:** 32 plots (Germany 2, Greece 11, France 3, Italy 10,
    Switzerland 6), 2000-2002, 135 samplings, 8,991 lesions. Two Greek plots sampled in two
    years make 34 populations.
  - **When:** in Greece from about a week after the first May rain; in central Europe
    weekly from 1 May.
  - **Which lesions:** every oil spot when vines had under four on average, otherwise 1-3
    per vine.
  - **Treatment:** plots untreated except four, with the vineyards around them sprayed.
  - **Markers:** four microsatellites (ISA, GOB, CES, BER).
- **Genotypes:** 3,910 after removing those shared between plots, 23 to 464 per
  population. The text's arithmetic does not close (4,246 - 216 is 4,030, and Table 1
  sums differently).
- **Diversity** (EH): Europe 0.77; Greece 0.68 (0.28-0.96) against central Europe 0.85
  (0.39-0.97), P = 0.02. Greek populations are less diverse, as with bottlenecks.
- **Mating:** 25 of 34 populations in Hardy-Weinberg equilibrium at all loci. They mate
  randomly: oospores are the overwintering population.
- **Differentiation:**
  - FST 0 to 0.137, mean 0.030; 93.4 % of 561 pairs significant.
  - Isolation by distance in central Europe: slope 3.5 × 10^-5 per km, R² 0.46.
  - None within Greece: R² 0.01, P = 0.13, with sea and mountains as barriers.
  - Examples: Fra2-Fra3, 40 km apart, FST 0.07; Ita2-Ita3, 1 km apart, not differentiated.
- **Cited, not measured here:**
  - 85 % of genotypes found once or twice;
  - one or two dominant genotypes per epidemic, under 1 % of genotypes, making 4.3-95 % of
    severity;
  - asexual spread under 20 m per cycle, "though larger distances cannot be excluded";
  - oosporic infections from May to late October.
  The sources are Gobbin et al. 2005, Rumbou & Gessler 2004 ([rumbou2004](rumbou2004.md))
  and 2006.
- **Garbled or inconsistent in the text:** Gre11's genotype count (79 or 129); Italy's
  total (1,264 or 1,364); "2-22 sampling dates per plot" against plots sampled once.

## Dependence

- No formulation. The data are the dataset `gobbin2006.europe`.
- Gessler and Rumbou share no work with the engine's models. Gobbin co-wrote
  [rossi2013](rossi2013.md) with Rossi and Caffi: a flag.

## Bearing (2026-10-09)

- **For history matching, the epidemic-structure numbers need Gobbin et al. 2005**
  (*Plant Pathology* 54:522-534, not held) and Rumbou & Gessler 2004 (held). This paper
  gives the frame: oospore populations random-mating, Greek ones less diverse and
  separated.
- **Between-vineyard spread is low:** a truth simulating several parcels (cooperative
  scale, M7) should keep inoculum mostly local.
