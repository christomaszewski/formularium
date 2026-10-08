---
id: kennelly2007php
citation: Kennelly, M. M., Gadoury, D. M., Wilcox, W. F., Magarey, P. A. & Seem, R. C. 2007. Addressing the gaps in our knowledge of grapevine downy mildew for improved forecasting and management. Plant Health Progress, 26 July 2007 (5th I. E. Melhus Graduate Student Symposium)
doi: 10.1094/PHP-2007-0726-03-RV
read: 2026-10-08, in full by a reading agent; the trigger record, sporangia survival and fruit resistance checked in the extracted text
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [New York, South Australia]
processes: [primary infection, oospores, sporulation, survival, fruit susceptibility]
records: [kennelly2007.trigger, kennelly2005.bunch_window]
datasets: []
---

# Kennelly et al. 2007 (PHP): gaps in downy mildew knowledge

A symposium summary of Kennelly's Phytopathology papers (95:1445-1452, 2005;
97:512-522, 2007). No equations.

## What it holds

- **Primary trigger:** rain > 2.5 mm with temperature > 11 °C after Eichhorn-Lorenz stage
  12; right in 24 of 29 site-years (1981-2004).
- **Oospores:** trap plants on infested soil were infected all season, most (> 75 %) in
  September.
- **Lesions:** sporulate abundantly 1-3 times, then yield falls sharply; age alone does not
  reduce yield over three weeks; lesions kept dry keep their potential.
- **Sporangia in the canopy:** on warm, dry days nearly all died within 8 h; on a cloudy
  day (27.8 °C, 72 % RH) about all were viable after more than 24 h.
- **Fruit:** Geneva NY, 2002-03, Chardonnay, Riesling, Concord, Niagara: resistance begins
  about 1 week after bloom (100 degree-days, base 10 °C); berries and pedicels resistant
  by 2-3 weeks (200-300 degree-days).
- Criticises DMCast for taking sporangial survival from one laboratory study.

## Dependence

- The trigger is the engine's `kennelly2007.trigger`, and the fruit window its
  `kennelly2005.bunch_window`: the same work, not independent.
- The field survival of sporangia and the decline of lesion yield are other parts of the
  study, not engine equations; their authors are the engine's (a flag).

## Bearing (2026-10-08)

- Field sporangia survival (8 h dry and warm; more than 24 h cloudy) is a check for a
  truth's survival formulation, independent of Brischetto 2020's laboratory model unless
  Brischetto was fitted to these data (not shown).
- Oospore infections continuing all season agree with Gobbin's genotyping
  ([rossi2013](rossi2013.md)).
