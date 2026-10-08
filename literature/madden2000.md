---
id: madden2000
citation: Madden, L. V., Ellis, M. A., Lalancette, N., Hughes, G. & Wilson, L. L. 2000. Evaluation of a disease warning system for downy mildew of grapes. Plant Disease 84(5):549-554
read: 2026-10-08, in full by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, the computed models read by the main session (l. 88-125)
status: read
diseases: [downy mildew]
crops: [grapevine, Vitis labrusca]
regions: [Ohio]
processes: [infection, sporulation, survival, spray decisions]
records: [lalancette1988.sporulation_bounds, blaeser1979.survival, lalancette1988.infection]
datasets: []
files: [PDIS.2000.84.5.549.pdf]
---

# Madden et al. 2000: an Ohio downy mildew warning system

From the Ohio State University, Rutgers and the University of Edinburgh. It evaluates
Neogen's EnviroCaster in Ohio, 1989-1995 (l. 17). No DOI is printed in the text copy.

## What it holds

- **What the system computes:** Lalancette et al.'s infection model (l. 27) and sporulation
  model, both from chamber tests on Catawba (l. 61-66); sporulation predicted for each
  nightly period of RH ≥ 92% (l. 79, 92-96); sporangial death "at a rate dependent on
  temperature and vapor pressure deficit", taken from Blaeser & Weltzien because it is
  unknown for *V. labrusca* (l. 102-109). No coefficients are printed.
- **Rules:** a spore load over the last 12 sporulation periods (l. 112); classes at 25% and
  50% (l. 131); wet periods with dry gaps under 4 h merged (l. 137); spray when infection
  and spore load are both moderate or high, at least 14 days after the last spray (l. 74).
  No oospore or overwintering component.
- **Field test:** Catawba 1989-1991 and Reliance 1992-1995 (l. 88). Incidence in unsprayed
  plots reached 0.685 in 1989 and 0.864 in 1992, and was 0 in 1991 and 1993. Sprays fell
  by 20 to 75% (median 55%) against the calendar, with similar incidence. Nothing was
  fitted to these data.

## Dependence

- **It computes engine pieces:** Lalancette's sporulation model, whose 10-30 °C bound the
  engine computes (`lalancette1988.sporulation_bounds`), and Blaeser & Weltzien's survival,
  which the engine's Rossi 2008 and Brischetto 2020 borrow (`blaeser1979.survival`). Its
  nightly RH ≥ 92% sporulation is the form of Caffi 2013's dark moist hours.
- Madden, Ellis and Lalancette wrote both the models and this test: one group, a flag.

## Bearing (2026-10-08)

- **Kin, now for substantive reasons:** D20 called it kin through shared authors; under
  D27 it stays kin through the equations it computes (Agrarium's D31).
- Its Ohio incidence by year is an evaluation of a policy with a known model, not data a
  truth should be fitted to.
