---
id: djuikem2024
citation: Djuikem, C., Grognard, F. & Touzeau, S. 2024. Impact of ontogenic changes on the dynamics of a fungal crop disease model motivated by coffee leaf rust. Journal of Mathematical Biology 88(3):30
doi: 10.1007/s00285-024-02053-4
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [coffee leaf rust]
crops: [coffee]
regions: []
processes: [ontogenic resistance, sporulation by leaf age, basic reproduction number, backward bifurcation]
records: []
datasets: []
files: [djuikem2024.pdf (the 2026-10-25 other-sources drop)]
---

# Djuikem et al. 2024: an SEIR-U model with young and mature leaves, for coffee leaf rust

A theoretical ODE model of a fungal disease on a perennial host, with young and mature leaves and a spore class, motivated by coffee leaf rust, with no field data.

## What it holds

- **Model:** a coffee-rust ODE system with young and mature leaf classes, a spore class U and
  berries B (system (1), Figure 1; l. 230-246). Young leaves sporulate at 5 spores per leaf
  per day (gamma1) and mature leaves at 7 (gamma2) in the baseline (Table 1, l. 289-312).
- **Most parameters are assumed:** Table 1 marks most rates as "Assumed"; the sporulation
  rates come from Bock (1962) (ref2, l. 312). No fitted parameters are printed.
- **Threshold:** R0 is the spectral radius of F V^-1 (Eq. 12, l. 700). A global stability
  result for the disease-free state holds when R0 is at or below a bound xi < 1 (Theorem 5,
  l. 708).
- **Backward bifurcation** (Table 4 values, l. 1203-1268): a saddle-node near R0 = 0.79 and a
  backward transcritical bifurcation at R0 = 1 (l. 1257-1259). At R0 = 0.88 the system has
  two endemic equilibria, one of them stable (l. 1266-1268). The paper ties the backward case
  to young leaves sporulating more than mature ones (abstract; conclusion, l. 1416-1425).

## Dependence

- **Builds on** the ontogenic-resistance idea (Calonnec et al., 2018, l. 132), and on earlier
  models of fungi on perennial hosts: Burie et al. (2008) on vineyard mildew (l. 106),
  Mammeri et al. (2014a) (l. 107) and Desprez-Loustau et al. (2019) (l. 113).
- No borrowed equation or dataset is named in the parts read.

## Bearing (2026-10-26)

- classes.tsv names no search for this key. The form carries host age through the
  sporulation rate of each leaf class, which a vineyard model with leaf-age classes could
  copy in outline.
- Its rates are assumed or taken from coffee sources, and it has no vine data. The paper was
  not read in full; the bifurcation sections were read only at their headline results.
