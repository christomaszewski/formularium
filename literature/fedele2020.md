---
id: fedele2020
citation: Fedele, Giorgia, Bove, Federica, González-Domínguez, Elisa & Rossi, Vittorio. 2020. A Generic Model Accounting for the Interactions among Pathogens, Host Plants, Biocontrol Agents, and the Environment, with Parametrization for Botrytis cinerea on Grapevines. Agronomy 10 (2):222 (21 pp.)
doi: 10.3390/agronomy10020222
read: 2026-10-08, in full (ANOVA tables and figures skimmed), by a reading agent (claude-sonnet-5-5); 29 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [Botrytis bunch rot]
crops: [grapevine]
regions: [Piacenza]
processes: [biocontrol, infection, epidemic progress]
records: []
datasets: []
files: [10-3390-agronomy10020222.pdf]
---

# Fedele et al. 2020: a generic model of pathogens, hosts and biocontrol agents (Botrytis)

From the Università Cattolica (Piacenza).

## What it holds

- Fedele, Bove, González-Domínguez and Rossi (2020) extend the Jeger et al. biocontrol model and parametrize it for B. cinerea on grapevines (l. 19, 93).
- It is a simulation study: 981 runs, nine climate scenarios, no data of its own and no field check (l. 777, 1441).
- Infection rate b is the berries paper's equation 1, numbers unchanged: gamma 7.750, zeta 2.140, nu 0.469, rho 35.360, psi 40.260, Tmin 0, Tmax 30 C (l. 735, 724), driven by daily mean T and RH (l. 435).
- BCA growth GRO uses the form of the berries paper's equation 2 (l. 446); S1 = 6.416, 1.292, 0.469, 2.300, 0.048, Tmin 0, Tmax 35 (l. 737), with c, e and Tmin changed. S2-S9 and the survival settings are round numbers without a source (l. 738, 747).
- Latent infection is not modelled: 20% of berries are assumed affected on day 4 (l. 692).
- Strain and survival capability explain 91% of simulated variance in the cold, wet climate (l. 915).

## Dependence

- A simulation study (981 runs), no data of its own. **It copies Ciliberti et al. 2015 (berries)'s eq. 1 parameters** as its infection rate (l. 735) and builds a biocontrol curve from their eq. 2: a borrowed equation, within one group. Latent infection is an assumed 20% inflow.
- Fedele and Rossi are authors of engine models (Brischetto 2021): flags.

## Bearing (2026-10-08)

- A flag, not kin. Not a latent-infection model, as the earlier notes thought: a biocontrol model whose infection step is Ciliberti's.
