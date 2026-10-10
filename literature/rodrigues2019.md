---
id: rodrigues2019
citation: Rodrigues, Lucas Alves, de Oliveira, Evandro Chaves, Alves, Maria Emília Borges, de Sales, Ramon Amaro, Cunha Junior, Jadier de Oliveira, Posse, Robson Prucoli et al. 2019. Analysis of climatic risk favorability of grapevine fungal disease occurrence for Santa Teresa, Espírito Santo State, Brazil
doi: 
read: 2026-10-09, methods and results in full, the equations in the page images, by a reading agent (claude-haiku-5-5); 30 quotes checked by scripts/verify_quotes.py; the coefficients compared with lalancette1988.infection and broome1995.botrytis by the main session
status: read
diseases: [downy mildew, grey mould]
crops: [grapevine]
regions: [Espírito Santo]
processes: [infection, climatic risk, leaf wetness]
records: [lalancette1988.infection, broome1995.botrytis]
datasets: []
files: [br_santa_teresa_favourability_2019.pdf]
---

# Rodrigues et al. 2019: climatic risk of downy mildew and grey mould at Santa Teresa

## What it holds

- **Data:** INMET station at Santa Teresa (ES), 2007-2016; annual rain 1,664 mm.
- **Downy mildew:** a Lalancette-based EI, printed (page image, p. 3) as (-0.061 + 0.018T -
  0.0005T²) x (1 + e^(-0.24 LWD + 0.07 LWD x T²))^(-5). Against eq. 5: intercept -0.061,
  no +0.01, e^(+ρ), T² where the source has T, and the -0.0021WT² term dropped.
- **Botrytis:** Broome's logit, printed with intercept +2.6479. The source, and the engine,
  have -2.647866.
- **Wetness:** LWD and wet-period temperature come from hours of RH at or above 90 %,
  cited to Sentelhas et al. 2004, whose authors' later threshold method the engine runs
  (`sentelhas2008.wetness`).
- **Results:** downy mildew high on 93 % of days; Botrytis medium on 68 % and never high.
  A 20 mm rain rule would spray 6.5 times against 15 (downy mildew).
- The authors state the models are not validated for Santa Teresa.

## Dependence

- Misprinted copies of Lalancette's and Broome's equations; Broome's is an engine model.
- RH >= 90 % as wetness: the engine's `rh-threshold-wetness` form.

## Bearing (2026-10-09)

- Context only; an example of copied equations drifting.
