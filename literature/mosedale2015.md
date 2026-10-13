---
id: mosedale2015
citation: Mosedale, Jonathan R., Wilson, Robert J. & Maclean, Ilya M. D. 2015. Climate change and crop exposure to adverse weather: changes to frost risk and grapevine flowering conditions. PLoS ONE 10(10):e0141218
doi: 10.1371/journal.pone.0141218
read: 2026-10-13, a light reading by a reading agent (claude-haiku-5-5); 30 of 30 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [Cornwall, England]
processes: [phenology, budburst, flowering, frost risk, climate projection]
records: []
datasets: []
files: [mosedale2015_plos.pdf]
---

# Mosedale, Wilson & Maclean 2015: frost and flowering weather for Cornish vineyards

Published phenology models run unchanged (Parker's flowering and veraison sums, García
de Cortázar-Atauri's budbreak, Caffarra & Eccel's chilling-forcing form) on a thousand
generated 30-year weather series for one 5 km cell in Cornwall, to count frost after
budbreak and cold or wet days at flowering, with seven growers interviewed on what they
fear. A projection paper; nothing fitted.

## What it holds

- **Growers:** seven interviews in Cornwall and south Devon; all named rain or cold at
  flowering, frost after budburst and cool summers (l. 141-164).
- **Weather:** UKCP09 weather generator, 1,000 sequences of 30 years per period and
  scenario (A1FI, A1B, B1), cell 2050070 at a commercial vineyard, with a 1960-2011
  record of unnamed source (l. 176-202).
- **Models** (Tables 1-2): spring-warming sums, budbreak base 5 °C from day 1 to 318 °C·d
  (`cortazar2009.budburst`'s form), flowering and veraison base 0 °C from day 60 to
  1,217 and 2,547 (`parker2013.gfv`'s Chardonnay); the winter-chill form of
  `caffarra2010.chardonnay` with a 0.005, c 2.8, co1 176, co2 0.015, dormancy break at
  79 chilling units, flowering at 25 forcing units, chilling from 1 October for the
  long Cornish season (l. 224-280). Literature values, not refitted (l. 243-245).
- **Measures:** frost as Tmin at or below 0 °C after budbreak; an adverse flowering day as
  mean below 15 °C or rain above 5 mm, risk as ten or more such days within a week
  either side (l. 298-306).
- **Results** (Tables 3-4): baseline 734 seasonal degree-days, frost probability 0.03,
  adverse flowering in 39 % of years; by 2070-2099 (medium) 1,444 degree-days, frost
  0.22 with the spring-warming models (budbreak 45 d earlier by 2080, flowering 19-20 d,
  veraison 37 d) but falling with the winter-chill model (budbreak only 7 d earlier, as
  warm winters delay dormancy break); adverse flowering down to about one year in ten
  (l. 359-461).

## Dependence

- **Computes** the three published models as cited; nothing fitted. The frost and
  flowering definitions are the authors'.

## Bearing (2026-10-13)

- The two model families disagree by 38 d on budbreak under warming: the clearest
  printed example of why the chilling question matters for a frost-risk truth, even if
  Cornwall is far from the Penedès.
