---
id: barrios2004
citation: Barrios, Gonçal & Reyes, Joan. 2004. Modelización del mildiu de la vid. Phytoma 164 (December 2004), 9 pages in the RuralCat reprint
doi:
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; the EPI table (p. 4) and the Goidanich table (p. 6) read in the page images by the main session; held since 2026-10-07 without a note
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Penedès, Vilafranca del Penedès, Tarragona, Catalonia]
processes: [oospore maturation, primary infection, incubation, forecasting, spray timing, season severity]
records: [goidanich.incubation]
datasets: [barrios2004.vilafranca]
files: [2004-barrios-url-barrios-reyes-2004-mildiu-penedes.pdf]
---

# Barrios & Reyes 2004: EPI's winter value against 21 Penedès springs, and the Goidanich table

The Catalan plant-health service's account (Servei de Sanitat Vegetal, DARP) of the two
models its warning stations ran: EPI's winter phase, checked against what happened at
Vilafranca del Penedès in every spring from 1984 to 2004, and Goidanich's daily
incubation table, printed in full. The project's own region; held since 2026-10-07.

## What it holds

- **EPI, winter phase** (Strizyk, first version 1983; the version used is Molot's, Progrès
  Agricole et Viticole 1986, 103(15-16), which holds the formulas; l. 144-148): from a
  20-30 year reference climate (monthly mean rain, temperature and rain days, l. 156-157)
  and each season's monthly and ten-day values, a sum from EPI = 0 in October to March
  (l. 159-163), read as the share of viable winter oospores on a scale of −20 to +20 (l.
  164): −20 to −10 very low risk, −10 to −5 weak with scattered primary outbreaks, −5 to
  5 medium, one rain enough for general outbreaks, 5 to 10 important, 10 to 20 very high
  (l. 169-176). No equation, coefficient or unit is printed.
- **The Penedès check** (p. 4, read in the image; `barrios2004.vilafranca`): weather from
  the INCAVI station at Vilafranca, a series of more than 70 years (l. 185-186); for each
  spring 1984-2004 (21 rows; the text says 20 years) the EPI value, the outcome in words
  ("scarce primary infections, late", "general primary infections from the first spring
  rains", with the rain in mm in some years) and a verdict: 17 correct, 2 partly correct
  (1992 at −4.71, 2001 at −19), 1 incorrect (1989, −12.08) and 1 very incorrect (1999,
  −16), the misses all low values before early general infections (l. 191-209, 227-260).
  In three positive years (1988, +3.13; 2003, +12.2; 2004, +8.06) rains of only 3-5 mm set
  off general primary infections, against the view that 10 mm are needed (l. 211-214);
  in 2004 the vines had barely 10 cm of growth (l. 273). EPI tells only the oospores'
  maturity; the spring's rain decides the incidence (l. 217).
- **Goidanich's table** (p. 6, read in the image; l. 305-373): the daily percentage of
  development for mean temperatures 12 to 25 °C in 0.25 °C steps, two columns for mean
  RH below and above 75 % (12 °C: 0.00 and 5.25; 20 °C: 14.20 and 20; 25 °C: 22.20 in
  the second column), summed from the day after a rain "near or above 10 litres" until
  100, when the oil spots appear (l. 316-326); a note says development is constant from
  25 °C, though the printed 24-25 °C rows fall (l. 371). The table's year and source are
  not printed; the 17 °C row is not monotonic and one cell prints "4,7o" (l. 348, 366).
  It is the table `lopezfrias2009` prints for the Canaries, by range and columns.
- **Stated thresholds, unsourced:** primary infection at about 10 °C with 10 cm shoots and
  10 mm of rain in a day (l. 44-45, the 3-10 rule in substance); zoospores need at least
  2 h of free water (l. 42, 60); incubation 4-21 d (l. 51); secondary spread best at
  20-25 °C with rain at night or dawn (l. 73-74).
- **Tarragona warnings 1985-2004** (l. 432-463): general treatments averaged 1.25 to 1.85
  a year by comarca (Camp de Tarragona 37 in 20 years, Conca de Barberà 35, Ribera d'Ebre
  30, Priorat 30, Terra Alta 25) against 4-5 sprays a year in traditional practice
  (l. 473).

## Dependence

- **Computes** EPI's winter model (Strizyk 1983, Molot 1986) on INCAVI weather and the
  Goidanich table; neither is fitted here. The outcomes column is the service's own
  judgement of each spring; who scored it and how is not printed.
- **Engine pieces:** `goidanich.incubation` (printed in full here, as a daily table
  summed to 100: the engine-list form) and the 3-10 rule in words; EPI is the engine's
  comparator model (`ronzon1987`, `sanna2014`).
- **Authors:** none shared with engine models.

## Bearing (2026-10-13)

- For Agrarium's Penedès truth: the 21 springs are an observed-outcome record from the
  region itself (dated by the service, not by a model), with EPI's own score: 17 of 21
  right, and its misses all under-forecasts. The 3-5 mm springs are the counter-case to
  the 10 mm primary-infection rule the engine's 3-10 pieces carry.
- Goidanich's table is on the engine's list; this copy confirms its form and the Catalan
  stations' use of it, so a truth must not run it (D27).
