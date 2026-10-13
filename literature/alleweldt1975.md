---
id: alleweldt1975
citation: Alleweldt, G. & Hofäcker, W. 1975. Einfluß von Umweltfaktoren auf Austrieb, Blüte, Fruchtbarkeit und Triebwachstum bei der Rebe. Vitis 14:103-115
doi:
read: 2026-10-13, in full (German), by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py; the correlations and the regression line (pp. 105-106) read in the page images by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Württemberg, Flein, Stetten]
processes: [phenology, budburst, flowering, shoot growth, soil temperature, fruitfulness]
records: [alleweldt1975.budburst]
datasets: [alleweldt1975.flein]
files: [alleweldt1975_vitis.pdf]
---

# Alleweldt & Hofäcker 1975: Riesling's budburst from the sum of daily maxima

Four years of Riesling at three Württemberg plots with grape-zone air and 20 cm soil
temperature recorded on site: which sum from 15 March tracks budburst, a forecast line
through the cumulative maxima, and the sums to flowering. From Hohenheim; the oldest
soil-temperature evidence the search found.

## What it holds

- **Data** (`alleweldt1975.flein`): Flein Steinboden (202 m), Flein Tonboden (208 m) and
  Stetten (253 m), Riesling on Kober 5 BB, 1969-1972 (the methods say 1968); budburst at
  the first leaflets, flowering at 25 % of caps shed; thermographs in the grape zone and
  at 20 cm, photocells, rain, soil water (l. 60-120).
- **Budburst** (`alleweldt1975.budburst`; p. 105): sums from 15 March to budburst
  correlate with the date at r 0.469 (means above 0 °C), 0.762 (daily maxima), 0.296
  (minima) and 0.541 (soil at 20 cm); late years 1969-1970 burst 58 days after 15 March
  at a mean of 6.7 °C, early years 1971-1972 at 40 days and 9.1 °C, from which the
  authors infer a 7-8 °C threshold (l. 138-154). The regression of the Tmax sum on the
  days gives y = 419.51 + 5.61x; budburst is where a year's curve crosses the line
  (figure, p. 106), with deviations up to 5 days (l. 156-202).
- **Flowering:** 9 June 1971 (Flein) to 3 July 1972 (Stetten), Stetten 4-10 days later
  (l. 207-211); budburst-to-flowering sums 533-993 °C (means), 863-1,462 (maxima),
  545-960 (soil) (l. 216-218); flowering expected after 550 °C of means or 850 °C of
  maxima, with temperatures above 15 °C most effective (l. 512-514); the phase 38 days
  in 1969-1970 and 59 in 1971-1972 (l. 220). Flowering date against the two weeks before
  it: r −0.441 (air), −0.733 (soil) (l. 266).
- **Growth and fruitfulness:** shoot length against light r 0.801, temperature 0.763, rain
  0.573 (l. 22, 349-352); inflorescences 1.8-2.6 per shoot, 145-221 flowers each, berry
  set 34-44 %, soil water the factor that matters (l. 338-465, 592).

## Dependence

- **Fitted to** the authors' own observations; cites Poenaru & Lazarescu 1959 (printed
  1969) for Romanian fixed sums and Horney 1966 for a bleeding-to-flowering sum. No
  engine model; kin by form to the degree-day pieces.

## Bearing (2026-10-13)

- A threshold form after all (a sum of maxima against a line), but the one place the
  search found soil temperature measured against budburst (r 0.54 against 0.76 for air
  maxima): the air maximum is the better predictor even with soil in hand.
