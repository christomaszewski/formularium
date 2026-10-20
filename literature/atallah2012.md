---
id: atallah2012
citation: "Atallah, S. S., Gómez, M. I., Conrad, J. M. & Nyrop, J. P. 2012. An agent-based model of plant disease diffusion and control: grapevine leafroll disease. Selected paper, AAEA Annual Meeting, Seattle, 12-14 August 2012"
doi:
read: 2026-10-20, first pages and the located results, by a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [grapevine leafroll disease]
crops: [grapevine]
regions: [New York State (model vineyard)]
processes: [agent-based model, cellular automaton spread, age and infection states, roguing and replacing, bioeconomic control, net present value]
records: []
datasets: []
files: [atallah_2012.pdf (the 2026-10-20 drop)]
---

# Atallah et al. 2012: agent-based model of leafroll spread and roguing in a vineyard

A cellular-automaton and agent model of leafroll spread in a 5720-vine New York vineyard. It ranks roguing rules by vineyard half-life and by expected net present value.

## What it holds

- **Vineyard and runs (l. 449-451, 943, 781):** 5720 vines on a 44 by 130 grid, 1000 runs per experiment, simulated to year 50.
- **Start (l. 613):** 2 % of agents begin in a homogeneous age and infection state.
- **Half-life (l. 1051-1053):** non-age-structured roguing extends the expected half-life by 8 to 119 months over the baseline. Up to 34 months of gain remains under age-structured roguing when only 1 % of exposed vines are found by sampling (l. 1145-1147).
- **Economics (l. 1181-1184, 1190-1191):** the all-age strategy gives the lowest expected net present value despite the longest half-life. Targeting exposed vines gives 5 % more net present value than roguing all ages.
- **Damage input (l. 80-82):** the paper cites $25,000 to $40,000 per hectare over 25 years if New York vineyards leave leafroll uncontrolled.

## Dependence

Cellular-automaton rules follow Gilbert and Terna (2000) and Ozah et al. (2010) (l. 413, 465). Transmission follows Cabaleiro et al. (2008) (l. 631), and latency follows Pietersen (2006) (l. 512). Vine revenues come from leafroll literature and interviews with vineyard managers (l. 837).

## Bearing (2026-10-20)

- **Strand t5 (damage and economics), touching t6 (spread).** A within-vineyard spread rule (age-dependent latency, infection to neighbours) and a revenue model by age and state. The ranking of control rules by net present value is the useful output.
- **Not read in full.** The model is a simulation with stated assumptions, not field data. Its transmission and revenue figures are the paper's inputs and should not be taken as measured.
