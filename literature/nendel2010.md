---
id: nendel2010
citation: Nendel, Claas. 2010. Grapevine bud break prediction for cool winter climates. International Journal of Biometeorology 54(3):231-241
doi: 10.1007/s00484-009-0274-8
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5), which read Eqs 1-6 on the page image; 29 of 29 quotes found at their lines by scripts/verify_quotes.py; Table 1 (p. 235) read in the page image by the main session; held since 2026-10-07 without a note
status: read
diseases: []
crops: [grapevine]
regions: [Germany, France, Luxembourg, Slovakia, Czechia]
processes: [phenology, budburst]
records: [nendel2010.budbreak]
datasets: [nendel2010.coolwinter]
files: [2010-nendel-10-1007-s00484-009-0274-8.pdf]
---

# Nendel 2010: budbreak by a heat sum whose start and threshold minimise its variation

Riesling and Müller-Thurgau at 13 cool-winter sites: degree-days by the single-triangle
method from a start day and above a threshold, both chosen so that the sum at budbreak
varies least across years. A threshold model, with the fitting rule as its contribution.

## What it holds

- **Data** (`nendel2010.coolwinter`): 20 site-variety series of BBCH 09 within 1967-2008
  (Table 1, p. 235); four sites record BBCH 07, taken as BBCH 09 minus two days
  (l. 142-148); Trier's temperatures lapse-corrected at 0.65 °C per 100 m (l. 151).
- **Model** (`nendel2010.budbreak`): daily degree-days by Zalom et al. 1983's single
  triangle (Eq. 1, l. 61), summed from day d; d in 1-90 and the threshold in 0-12 °C
  chosen to minimise the coefficient of variation of the sum (Eqs 5-6, l. 111-132), the
  threshold read at the crossing of two lines fitted to the CV curve (l. 164-170).
  Prediction: the target sum, less 0.5 degree-days a day, unexplained (l. 200).
- **Table 1:** Riesling thresholds 5.2-6.5 °C, starts 14 February to 12 March, sums
  166-242 °C·d, means 5.9 °C, 1 March, 186.1 °C·d (CV 0.100); Müller-Thurgau means 5.9
  °C, 1 March, 180.3 °C·d (CV 0.122). Local parameters predict 0.6 d late, ±2.6 d
  (Riesling) and ±3.2 d (Müller-Thurgau); the general model leave-one-out ±4.6 d
  (l. 287-293; the abstract rounds to ±2.5 and ±4.5, l. 31-32). Sites 60 km apart differ
  by more than 5 d (l. 401). 2007 excluded at several sites (l. 483).
- **Chilling** algorithms (Cannell & Smith 1983, Cesaraccio et al. 2004) gave no gain, no
  numbers printed (l. 504).

## Dependence

- **Borrows** the single-triangle degree-day (Zalom et al. 1983); fitted to the
  institutions' observed dates. Kin by form to `cortazar2009.budburst` and
  `molitor2014.shoots`; the CV criterion is the one `ramos2017`, `ramos2018` and
  `chacon2021` use for the base (as the SD of the sum).

## Bearing (2026-10-13)

- A threshold model; its number for Agrarium is the error floor of such models at their
  best (±2.6 d locally, ±4.6 d transferred) and the lesson that the start day matters as
  much as the base.
