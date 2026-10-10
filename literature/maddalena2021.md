---
id: maddalena2021
citation: Maddalena, Giuliana, Russo, Giuseppe & Toffolatti, Silvia L. 2021. The study of the germination dynamics of Plasmopara viticola oospores highlights the presence of phenotypic synchrony with the host. Frontiers in Microbiology 12:698586
doi: 10.3389/fmicb.2021.698586
read: 2026-10-09, in full, by a reading agent (claude-haiku-5-5); 59 quotes checked by scripts/verify_quotes.py; dependence judged by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Veneto]
processes: [oospores, primary infection]
records: []
datasets: [maddalena2021.montorio]
files: [maddalena2021-oospore-germination.pdf]
---

# Maddalena et al. 2021: four seasons of oospore germination at Montorio

## What it holds

- **Source:** oospores from an untreated plot of 13-year-old Corvina on Kober 5BB at
  Montorio (Verona). Leaves were sampled at the end of October in four consecutive years;
  the calendar years are not printed.
- **Storage:** in nylon bags on the vineyard soil (MT), or at 5 °C and 65 % RH on wet sand
  (MTc). 20 fragments a bag; 1,200 oospores plated a bag.
- **Assays:** twice a week for 35 weeks, mid-November to mid-July, at 20 °C, counting
  germination 1-14 days after incubation (G at 14 dai, and cumulative). Daily temperature
  and rain came from a station in the vineyard.
- **Observed:** MT germination rose during dormancy to 3.4-9.5 % at 61-120 days from
  October. Viable MTc oospores (trypan blue, year 4) were 9 % at 0 days, 17 % at 60 and
  30 % at 120.
- **Modelled (their fits, not data):**
  - **Maturation length (DFO50):** 117 days for MT (bootstrap 112-122) and 151 for MTc
    (138-164), from a probit GLMM (pseudo-R² 0.9925).
  - **T50 after maturation:** 6-7 days for MT, from a logit GLM.
- **Printed mismatches:** the text and Tables 1-2 disagree in three places, for example
  0.02-2.6 % in the text against a maximum of 1.2 % in Table 1 for MT at 1-30 days.
- **Not printed:** the models' coefficients, the base of their sum of temperatures, the
  station's identity and the years.

## Dependence

- No engine model is computed or fitted. Rossi et al. 2008 is cited as a study only. The
  lead that EPI was run in Franciacorta belongs to Maddalena et al. 2022, not this paper.
- The germination data are independent of the engine's `rossi2008pp.discs` (Piacenza).

## Bearing (2026-10-09)

- Field oospore germination over four seasons with station weather: data for TRUTH-METHOD's
  oospore-season row, outside the engine's calibration. A truth could fit its maturation
  rule to these counts.
