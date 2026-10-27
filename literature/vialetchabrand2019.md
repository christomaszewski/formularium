---
id: vialetchabrand2019
citation: Vialet-Chabrand, S. & Lawson, T. 2019. Dynamic leaf energy balance: deriving stomatal conductance from thermal imaging in a dynamic environment. Journal of Experimental Botany 70(10):2839 (last page not in the metadata read)
doi: 10.1093/jxb/erz068
read: 2026-10-26, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full; Europe PMC JATS text, one paragraph per line, no page numbers
status: read
diseases: []
crops: [wheat]
regions: []
processes: [leaf energy balance, stomatal conductance, thermal imaging, transpiration]
records: []
datasets: []
files: [vialetchabrand2019.xml (the 2026-10-25 other-sources drop)]
---

# Vialet-Chabrand & Lawson 2019: a dynamic leaf energy balance for stomatal conductance from thermograms

A method for deriving stomatal conductance from leaf temperature under changing light, with
black and white aluminium references, tested on wheat in a controlled phenotyping set-up.

## What it holds

- **Method:** a dynamic energy balance for the leaf (Eqs 8-11), a boundary-layer conductance
  from the black and white references (Eq 15), and a stomatal model fitted by Bayesian
  inference in Stan (l. 117). Fitted parameters are reported with 95 % credible intervals.
- **Plants and step:** winter wheat (Triticum aestivum) in a controlled platform, with a light
  step from 0 to 430 umol m-2 s-1 for 1 h (l. 129-131). The aluminium references were stepped
  from 0 to 300 umol m-2 s-1 (l. 136).
- **Results:** the leaf temperature RMSE is 0.069 C for the step changes (l. 148) and 0.098 C
  under fluctuating air temperature and humidity (l. 156). Conductance in the dark ranged from
  0.001 to 0.092 mol m-2 s-1 (l. 148). The replica check is shown in Figure 3 (l. 134-137);
  no replica error figure is printed in the text read.

## Dependence

- **Builds on** the Penman-Monteith combination equation (l. 24), the dynamic stomatal model of
  Vialet-Chabrand et al. (2017b) (l. 106), the heated leaf replica of Brenner & Jarvis (1995, l. 171)
  and the replica conductance of Lehmann & Or (2015) (l. 120), and Stan (Carpenter et al. 2017)
  (l. 117, 198).

## Bearing (2026-10-26)

- classes.tsv names no search for this key. A vineyard model that needs leaf conductance from
  thermal images could take the energy-balance equations, but not the parameters: they are for
  wheat in a controlled platform, with no vine or field data.
- The paper was not read in full. The supplement (algorithm S1, Figures S5 to S8) is not held.
