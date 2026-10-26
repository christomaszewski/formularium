---
id: rossi2019
citation: Rossi, V., Sperandio, G., Caffi, T., Simonetto, A. & Gilioli, G. 2019. Critical Success Factors for the Adoption of Decision Tools in IPM. Agronomy 9:710
doi: 10.3390/agronomy9110710
read: 2026-10-25, lightly (abstract and sections 4.4 to 4.7 on timeliness, benefits and trust, about lines 470-570 of 1100; the rest skimmed by grep), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine, multiple crops]
regions: [Europe, Italy]
processes: [decision tools, adoption, timeliness, trust, vite.net, spray savings, treatment cost]
records: []
datasets: []
files: [dr1025_rossi2019.pdf (the 2026-10-25 drop)]
---

# Rossi et al. 2019: a review of what makes decision tools succeed in IPM, with cited vite.net savings and a 12-hour decision interval for grape downy mildew

A review of the critical success factors for the adoption of decision tools (DT) in integrated pest management, across crops, with grape examples in its sections on timeliness, benefits and trust.

**Read this first.** A review, not a measurement: every grape number below is cited from other work (Rossi and Salinari 2014, closed and not obtained here; a project report, ref. 124) and is also in the held note `pertot2016`, so the two are one source, not two. The 12-hour decision interval is the authors' statement of practice, not a measured delay from a warning to a spray. Only abstract and sections 4.4 to 4.7 were read.

## What it holds

- **Decision interval:** the authors state that decisions on grape downy mildew control are taken every 12 h during the most critical periods of the season, so a decision tool must deliver information at that interval (l. 485). Their text, not their data.
- **vite.net, organic vineyards across Italy:** a saving of 195 EUR/ha/year, with fungicides cut by an average of 24 % against standard organic practice (cited to Rossi and Salinari 2014) (l. 549).
- **vite.net across Europe:** with the same quality as standard practice, fungicide savings of 31.5 % (IPM) and 43.7 % (organic), about 200 EUR/ha/year lower disease-management cost (cited to a project report, ref. 124) (l. 552).
- **Cost of mildew treatment:** treatments against downy and powdery mildew might reach 500 EUR/ha/year; a DT is cited as cutting pesticide applications by 30 %, equal to about 150 EUR/ha/year (cited to Caffi and colleagues) (l. 564).
- **Why growers deviate:** for intensive crops, farmers are more prone to increase the number of treatments to minimise the risk of yield loss; viticulture is named as an exception where DTs were adopted (cited) (l. 556).

## Dependence

- A review; the saving figures are cited from Rossi and Salinari 2014 (Computers and Electronics in Agriculture 100:88-99) and a project report, and repeat the numbers of the held note `pertot2016`. Rossi and Caffi are also authors of other held notes (`caffi2010`); flag only.

## Bearing (2026-10-25)

- **Delay from a warning to a spray (grower.delay_warning_to_spray):** no measured value. The nearest is the statement that downy mildew decisions are taken every 12 h at the most critical times (l. 485), which supports a decision step of 12 h in the tool, not a time for the grower to act on it.
- **Savings when a tool is followed (grower.dss_saving):** 24 % fewer fungicides and 195 EUR/ha/year in Italian organic vineyards, 31.5 % (IPM) and 43.7 % (organic) across Europe (l. 549, 552). Kind: cited field comparisons, not new data.
- **Cost (spray.cost_per_pass):** mildew treatments might reach 500 EUR/ha/year (l. 564). At 5 to 7 passes a year, 90 EUR/ha a pass gives 450 to 630 EUR/ha (arithmetic, not printed), the same order. Both mildews and product are in the cited figure; it is not a per-pass cost.
- **Deviation:** growers of intensive crops add sprays to limit yield-loss risk (l. 556), a reason a grower model might spray more than a model advises.
