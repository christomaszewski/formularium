---
id: otero2023
citation: Otero, M., Basile, B., Onrubia, J. & Pijuan, J. 2023. Use of artificial intelligence for the prediction of microbial diseases of grapevine and optimisation of fungicide application. 22nd GiESCO International Meeting, Cornell University, Ithaca, USA, 2023
doi: 10.5281/zenodo.8275448
read: 2026-11-03, in full (5 pages; the figures are not text), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 8 of 8 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Spain (L'Aranyó, Lleida), Portugal (Quinta do Bomfim), Italy (Mirabella Eclano)]
processes: [machine learning, Naive Bayes, risk classes, untreated plots, weekly scoring, spray count, fungicide]
records: []
datasets: []
files: [dr1103_otero2023.pdf (the 2026-11-03 drop)]
---

# Otero, Basile, Onrubia & Pijuan 2023: Naive Bayes risk classes for grapevine mildews, with untreated plots at L'Aranyó

A GiESCO conference paper on the VitiGEOSS early-warning service: machine-learning models trained on weekly scores of untreated plots at three sites, one of them in Catalonia (Lleida, not Penedès).

**Read this first.**
- The first author as printed is Marta Otero (Eurecat, Lleida); the corresponding author is Boris Basile (Naples), so the work is often cited as Basile. The reading file was keyed "basile2023"; the byline order is Otero, Basile, Onrubia, Pijuan.
- L'Aranyó is in Segarra, Lleida (Costers del Segre), not the Penedès. It had the lowest rain and the highest wind of the three sites (l. 142).
- The text gives no dates, scores or spray numbers: those are in figures only (garbled or absent as text). The F1 is a score of a site-specific classifier, not a validated process model, and the reading agent found no out-of-site test.

## What it holds

- **Sites and years (l. 43):** three sites, Quinta do Bomfim (Portugal), L'Aranyó (Spain) and Mirabella Eclano (Italy); six plots in all; weekly field visits from March to October 2021 and 2022.
- **Untreated subplots (l. 105):** no spray until a damage threshold was reached; 20 vines in 4 blocks per subplot.
- **Scoring (l. 107):** 100 leaves per treatment inspected every 7 days for the share of leaves affected and the share of leaf area affected. These were turned into low, medium and high risk levels (l. 109).
- **Weather at L'Aranyó (l. 142, 149):** lowest rain and highest mean wind speed of the three sites; 2022 was hot and dry with low rain, and disease was not detected in some plots (l. 149). No temperatures or rain totals are given in the text.
- **Model result (l. 157):** the best of eight machine and deep learning models was Naive Bayes; short-term prediction F1 of 90 % for downy mildew and 79 % for powdery mildew. Adding phenological-stage variables raised precision by up to 9 % (l. 157).
- **Spray count (l. 168):** following the model's spray recipes would cut applications by 20 % on average against actual practice (Figure 2A, a figure), and water by 21 % per campaign. Historical products and doses of 2021 and 2022 were collected (l. 110); the numbers are in Figure 2 only.
- **Baseline rule named (l. 27):** the "3-10 rule" (air above 10 °C, shoots of at least 10 cm, at least 10 mm of rain in 24 to 48 h) is described as the most widespread way to plan the first spray.
- **Data:** the paper cites no dataset. The DOI is a Zenodo record of the paper; the reading agent listed the data as "none published", and the record's file list was not checked beyond the paper, so no open data are shown.

## Dependence

- Data-driven models fitted to the authors' own plot data (VitiGEOSS service). No process model is borrowed. A shorter earlier version (FAIA 356:164-167, 2022, 10.3233/FAIA220333) was not fetched. Shared authors with other notes are only a flag.

## Bearing (2026-11-03)

- **Cooptera E7 (spray timing against a warning rule):** a Catalan comparison for a learned risk-class rule. It claims 20 % fewer sprays than practice at three sites pooled, but the per-site counts are in a figure and the baseline is the growers' practice, not a calendar or a process model.
- **Local data:** untreated, weekly-scored plots at L'Aranyó in 2021-22 exist, but the text prints no dates or severities and no data are open. They do not give Penedès first-spot dates or severity.
- **Kind of evidence:** a conference paper with a site-specific classifier; F1 90 % has no out-of-site test.
