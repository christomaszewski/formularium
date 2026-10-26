---
id: nefti2024oeno
citation: Nefti, O., Chartier, N., Merot, A., Peyrard, T. & Delière, L. 2024. To what extent can a phase-out of pesticides in viticulture be achieved? Learning from the efforts of a large farm network after 10 years. OENO One 58(2):1-16
doi: 10.20870/oeno-one.2024.58.2.7885
read: 2026-10-25, lightly (abstract, the methods summary on levers, the results on pesticide reduction levers and the fungicide discussion; about lines 60-200, 325-380 and 680-700 of 1034; trajectory clusters and figures not read), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [grapevine]
regions: [France]
processes: [pesticide reduction, decision support systems, fungicide reduction levers, treatment frequency index, DEPHY network]
records: []
datasets: []
files: [dr1025_nefti2024oeno.pdf (the 2026-10-25 drop)]
---

# Nefti et al. 2024: 31 % of 331 French DEPHY winegrowing systems name a decision support system among their fungicide-cutting levers

A paper on pesticide reduction in the 343-farm DEPHY winegrowing network after ten years, with the share of systems quoting each lever for cutting fungicide.

**Read this first.** The 31 % is self-reported lever use by the network's extension engineers, counting a system that quoted a lever "at least once" (l. 192); it is not a share of sprays decided by a model, nor a compliance rate. The DEPHY farms are volunteers committed to cutting pesticide use, so 31 % is an upper bound for the French average (the reading agent's reading, l. 338). Only parts of the paper were read; trajectory clusters and figures were not.

## What it holds

- **Sample:** lever answers are available for 331 of the 343 DEPHY winegrowing systems; a system counts as using a lever if it was quoted at least once (l. 192).
- **Fungicide levers (share of 331 systems):** reduced doses 76 %, vineyard inspections 63 % (l. 334); foliage thinning 59 %, spraying techniques and equipment 45 %, decision support systems (DSS) 31 %, fragmented plot protection 30 % (l. 338).
- **The authors' reading of DSS use:** the network's winegrowers use DSS to decide whether treatment is needed and the dose, so the lever concerns whether and how much, not only when (l. 687).
- **Cited:** the mean TFI of French vineyards is 12.4 (Simonovici and Caray 2021); fungicides are about 81 % of it per the held note `fouillet2024` (l. 127).

## Dependence

- The same 343-farm DEPHY dataset as `nefti2024data` (doi 10.57745/2HITDV); the lever answers are the network engineers' records. The two are not independent of each other. Authors Nefti, Chartier, Peyrard and Delière are shared with `nefti2024data`, and Merot with `merot2020` and `fouillet2024`; flags only.

## Bearing (2026-10-25)

- **Compliance with decision support (grower.dss_compliance):** 31 % of 331 French DEPHY systems name a DSS among their fungicide-cutting levers (l. 338, 192). Supports the order of magnitude of DSS use among committed low-input growers, an upper bound for French growers; kind: self-report by extensionists, France, the DEPHY network after ten years. It says nothing on how closely an alert is followed.
- **What a DSS decides:** whether and how much to spray (l. 687), consistent with a grower model in which a warning changes the dose or the decision to spray more than the date.
- **Not shown:** spray counts, intervals, delay, Catalonia.
