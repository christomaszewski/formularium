---
id: orlandi2015
citation: Orlandi, F., Bonofiglio, T., Aguilera, F. & Fornaciari, M. 2015. Phenological characteristics of different winegrape cultivars in Central Italy. Vitis 54:129-136
doi: not printed
read: 2026-10-14, a LIGHT reading by a reading agent (claude-haiku-5-5), the full text layer plus the rendered pages for the forcing equation (p. 131), Tables 1-3 and Fig. 4; 42 of 42 quotes found at their lines by scripts/verify_quotes.py; the Fig. 4 coefficients were read from the rendered page by the reading agent and not checked by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Umbria, Marsciano]
processes: [phenology, flowering, harvest, berry sugar]
records: []
datasets: []
files: [fabio_2015.pdf]
---

# Orlandi et al. 2015: flowering, harvest and berry sugar of five cultivars at Marsciano

Flowering and harvest dates and berry sugar of Chardonnay, Grechetto, Cabernet, Merlot
and Sangiovese on one farm near Marsciano (Umbria, 256 m), 2000 to 2012, with a
spring-warming degree-day sum and partial-least-squares regressions of berry sugar at
harvest on weather. There is no model of the stage dates.

## What it holds

- **Site and data** (l. 77-118): farm at 256 m, weather station at 229 m, just over 2 km
  away. Flowering is 50 % of flowers open (BBCH 65); harvest is the first date mean berry
  sugar reaches 18 °Babo (l. 94, 105). Yearly dates are not printed.
- **Table 1** (13-year mean and SD, l. 199-203; the table labels its columns day of year
  but prints calendar dates):

  | Cultivar | Flowering (SD, d) | Harvest (SD, d) | Sugar °Babo (SD) |
  |---|---|---|---|
  | Chardonnay | May 16 (3.46) | August 30 (5.06) | 19.2 (0.89) |
  | Grechetto | May 15 (2.10) | September 16 (6.56) | 19.5 (0.71) |
  | Cabernet | May 25 (3.62) | September 29 (6.09) | 19.9 (1.15) |
  | Merlot | May 23 (2.96) | September 8 (4.27) | 20.1 (1.20) |
  | Sangiovese | May 20 (3.29) | September 3 (7.02) | 18.6 (1.31) |

  The Grechetto, Cabernet and Merlot rows are from the text layer (l. 200-202). The mean
  flowering day is 140 (20 May) and the mean harvest day 258 (15 September) (l. 235-237).
- **Spring-warming sum** (p. 131; l. 155-175, 227-228): daily degree-days Rf above a base
  Tb, summed from a start date t0. Tested starts 15 February (day 46), 1 March (60) and
  15 March (74); bases 0, 1, 2, 3, 5, 7, 10, 12 °C (l. 170-172). The best start is
  15 March and the best base 0 °C, chosen by the lowest coefficient of variation of the
  sum (the text ties it to berry sugar at harvest, l. 175), not by error on stage dates.
  Daily sums by the method of Arnold 1960 (l. 152).
- **Sums** (l. 229-237): from 15 March to flowering 823 °Cd (Grechetto) to 1,010 (Cabernet);
  to harvest 3,244 (Chardonnay) to 3,845 (Cabernet); mean flowering to harvest
  2,674 ± 208. Chardonnay needs under 2,410, Sangiovese and Cabernet over 2,800 (l. 240-242).
- **PLS models of mean annual berry sugar at harvest** (l. 251-252, 360-364; Fig. 4,
  coefficients read from the rendered page; order: intercept, April rain Pp_A, July
  mean maximum Tmax_J, degree-days to flowering GDD_f):
  - A, all cultivars: −15.302, −0.399, +0.700, +0.264; R² 0.90, Q² 0.81.
  - B, white: −12.518, −0.262, +0.756, +0.204; R² 0.82, Q² 0.68.
  - C, red: −16.961, −0.437, +0.618, +0.302; R² 0.78, Q² 0.64.
  - Model A deviation 0.3 % (2010) to 4.1 % (2001); B 0.4 % (2005) to 3.7 % (2007)
    (l. 375-376).
- **Trends:** Sangiovese flowering is the only evident increasing trend (test Z 2.32,
  l. 229); harvest Z −1.78 (Cabernet) and −1.90 (Sangiovese) (l. 236-237).
- **Not printed:** yearly dates, any budburst or veraison date (l. 435), the PLS
  coefficients in the text.

## Dependence

- **Borrowed form:** the spring-warming sum with a 0 °C base is from Parker et al. 2011,
  who started on day 60 (l. 155, 164-167). Parker's flowering sum is about 1,200 °Cd against
  about 1,000 here, and the maturity sum is 2,500 to 2,700 against 3,200 to 3,800
  (l. 383-387); compared in the discussion only.
- **Fitted to:** the authors' own observations and the station record. No model produced
  or dated them.

## Bearing (2026-10-14)

- **No stage-date model:** a degree-day sum with a start and base picked by the spread of
  the sum, and regressions of sugar on weather. Not a truth candidate. No record.
- **Weak check set only:** the Table 1 means of flowering and harvest for five cultivars
  in Umbria.
