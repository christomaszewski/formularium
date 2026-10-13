---
id: fabre2024
citation: Fabre, Frédéric, Delbac, Lionel, Poeydebat, Charlotte & Zaffaroni, Marta. 2024. Quantification and modeling of grapevine yield loss as a function of the severity of downy mildew on foliage and cluster. bioRxiv preprint 2024.02.28.582447 (not peer reviewed)
doi: 10.1101/2024.02.28.582447
read: 2026-10-13, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Bordeaux, Couhins, Latresne]
processes: [yield loss, damage function, season severity, cluster infection, moisture risk]
records: []
datasets: []
files: [fabre2024_biorxiv.pdf]
---

# Fabre et al. 2024: a damage function for downy mildew, from the Bordeaux trials

A bioRxiv preprint (fetched 2026-10-12) that turns the Couhins and Latresne trials of
`savary2009` (plus a 2008 season) into a yield-loss model: the second measured damage
function held here after `jermini2010`, and the first with a weather term.

## What it holds

- **Data:** the 2006-2008 seasons at Couhins (planted 1982) and Latresne (2003), Cabernet
  franc on double Guyot, six blocks, 18 plots of 50 vines a site, three spray levels
  (continuous: nine downy and nine powdery mildew sprays on a calendar; l. 131-151);
  severities of downy mildew, powdery mildew, black rot and Botrytis on six vines a plot
  at stages 53, 57, 75, 77, 79, 85 and 89, on a 0, 1, 5-100 % scale (l. 159-168); cluster
  weight per vine and potential alcohol from 60 berries a plot (l. 270-278; alcohol missing
  in 7 of 108 plots); black rot excluded (106 of 108 scores zero, l. 283); stations within
  300 m (l. 137). Relative AUDPC (eq. 1, trapezoids over the seven stages, l. 261-267):
  unsprayed downy mildew on foliage 13-29 %, with limited sprays 0.6-12 %; on clusters
  31-66 % in 2007-2008 and under 1.3 % in 2006; powdery mildew on foliage 0.6-7.3 %
  (l. 421-431, 481-484).
- **The model** (eq. 2, Cousens 1985's form with a beta cdf): cluster yield per vine ~
  negative binomial with mean Y0(s,y)(1 − pml)[1 − I(DA/100; αY1, αY2(s,y))] + Y0 pml,
  fitted in Stan to the 108 plot-season combinations (l. 319-341, 398-401); M0 one
  damage shape, M2 one per site-season, M3 the shape αY2 = αYmax·I(MRr; αHY1, αHY2) as a
  function of a season moisture risk index (l. 347-361). Table 3 (M3): pml 0.04 (90 %
  interval 0.02-0.07), αY1 1.32 (1.03-1.78), αYmax 25.9, αHY1 6.87, αHY2 2.60, β 0.0099;
  Y0 from 593 g (Couhins 2008) to 1,469 g (Latresne 2006) per vine (l. 614, 676-682).
  Doubling foliage AUDPC from 5 to 10 % costs 49 g (Couhins) and 27 g (Latresne) in the
  dry 2006 and 273-286 g in 2007 and 2008 (l. 623-632); on clusters, model M0, 113 g (66-144)
  of 1,000 g, adjusted R² 0.77 (l. 557-564). Alcohol falls 0.86, 0.27 and 0.19 degrees
  per doubling in 2006-2008, numbers given only in the discussion (l. 825-832), which also
  mixes M2 and M3 values (l. 841-844).
- **The moisture index:** a six-class daily risk from rain and humidity "derived from Bove
  et al. 2020" with class rules credited to Lalancette 1987 (class 0: no rain and mean RH
  under 70 %; the rules overlap at 5 mm; l. 368-383), averaged over stages 53-79 (fixed
  Julian days 130-216 for the 30-year series, l. 1142); Couhins 1993-2022 mean 1.55, 99 %
  quantile 2.44 (l. 386-387); relative index by season 0.47, 0.91, 0.89 at Couhins and
  0.42, 0.80, 0.82 at Latresne (l. 415-417).
- **Cited:** Carisse 2016's data refitted with M0 in the supplement (109 g, 54-140; l.
  851, 1347); Leroy et al. 2013's losses above 80 % in 14 of 23 Bordeaux years without
  control (l. 763); Maddalena et al. 2021 and Kennelly et al. 2005 on cluster infection
  and ontogenic resistance (l. 860-862); Jermini et al. 2010 on carry-over (l. 900).

## Dependence

- **Fitted to** the Bordeaux trial, observed (the same 2006-2007 observations as
  `savary2009`, whose equations are not used), with Carisse 2016's series as a second
  fit. The moisture classes are borrowed rules (Bove et al. 2020, Lalancette 1987), not
  engine equations; Bove et al. 2020 shares Savary and Rossi as authors (`bove2020`: flag).
- **Engine pieces:** none computed. The damage function is the kind of relation Agrarium's
  yield layer needs and no tool runs.
- **Authors:** Poeydebat (`poeydebat2025`), Delbac (`savary2009`): flags.

## Bearing (2026-10-13)

- The damage function for a Bordeaux truth: yield loss from foliage AUDPC with a shape
  that steepens in wet seasons, and a floor pml of 4 % at total loss; the cluster model
  gives about 11 % of yield per doubling of cluster AUDPC from 5 to 10 %. A preprint, so
  values may move at publication; `jermini2010` (Merlot, Ticino) is the published
  comparison.
