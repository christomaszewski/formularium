---
id: moyer2014
citation: Moyer, M. M., Gadoury, D. M., Wilcox, W. F. & Seem, R. C. 2014. Release of Erysiphe necator ascospores and impact of early season disease pressure on Vitis vinifera fruit infection. American Journal of Enology and Viticulture 65:315-324
doi: 10.5344/ajev.2014.13111
read: 2026-10-20, in full, Table 1 and Eq. 2 with Table 3 in the page images (pp. 2, 5), by a reading agent (claude-haiku-5-5); 59 of 59 quotes found at their lines by scripts/verify_quotes.py; Eq. 2 read in the page image by the main session
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [New York, New Jersey, Washington, North Carolina]
processes: [ascospore release, primary inoculum, fruit infection, spray timing]
records: [moyer2014.ascospore_release]
datasets: [moyer2014.cleistothecia]
files: [moyer_2014.pdf (the 2026-10-20 drop)]
---

# Moyer et al. 2014: when overwintered powdery mildew ascospores are released

Cleistothecia from New York were stored outdoors at four US sites and assayed through
winter and spring, 2005-2009; a complementary log-log model of degree-days and rain events
describes the season's cumulative release. A dose-response field trial links early
inoculum to fruit disease.

## What it holds

- **Release model** (Eq. 2, l. 296-298, page image p. 319): release = 1 - exp[-exp(-3.335 +
  0.00222 DD0 + 0.150287 PDE)], DD0 degree-days base 0 °C from 1 January, PDE days with rain
  >= 2.5 mm and a maximum above 0 °C (l. 287-289). Fitted on New York populations
  overwintered in New York (l. 185-187): R² 0.96, RMSE 0.08 (l. 300-301). Elsewhere: NJ R²
  0.87, RMSE 0.14; WA 0.75, 0.15; NC 0.80, 0.19 (l. 340-342); NY with non-NY populations
  0.71, 0.22 (l. 343). Other bases, starts and rain terms did not help (l. 303-305).
- **Timing:** 50 % of the season's release came 42, 24 and 35 days before and 9 days after
  Chardonnay budbreak in New York, 2006-2009 (l. 346-348); 3-15 days before in Washington
  (l. 349-351); half was released before budbreak in 85 % of site-years (l. 447-449). An
  early cohort (9 September) reached 50 % up to 21 days before a late one (20 October)
  (l. 358-360).
- **Dose and fruit:** in 2002 full-season fruit severity Y = -0.88 + 1.85 log10(cleistothecia
  per vine), R² 0.96 (l. 394); naturally derived bark densities of 133, 534 and 2,867
  cleistothecia/kg gave 11.4, 21.9 and 47.7 % cluster disease in 2003 (Table 3, l. 315-317).

## Dependence

- Its own assays; no model dated the data. The rain threshold (>= 2.5 mm, maximum above
  0 °C) and the degree-day base are credited to Gadoury and Pearson 1990 (l. 169-170), the
  same 2.5 mm the engine's Thiessen 2018 rule uses: the same form for release days. The
  cloglog link follows Rossi et al. 2010 and others (l. 199-201).
- Gadoury, Wilcox and Seem are authors of the engine's Kennelly pieces; Moyer of Ferguson
  2014's hardiness model: flags.

## Bearing (2026-10-20)

- Recorded as `moyer2014.ascospore_release` with the dataset `moyer2014.cleistothecia`. Kin
  report against the engine's list (cooptera@6f8d0a2): same form as
  `thiessen2018.ascospores` (ascospore-release-rule), as expected, plus author flags.
- For Cooptera: a release curve that says how much of the season's ascospore load is
  already out by a date, which Thiessen's day rule does not; for Agrarium, a primary
  inoculum schedule for a powdery mildew truth, development families only while it shares
  Thiessen's release-day form.
