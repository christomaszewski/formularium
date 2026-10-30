---
id: meteofrance2026hourly
citation: Météo-France. 2026. Données climatologiques de base - horaires: CLIMATOLOGIE_Donnees_horaires_descriptif.pdf (created 2026-06-03), H_descriptif_champs.csv (2026-03-24), and the dataset's page on data.gouv.fr (Licence Ouverte 2.0)
doi:
read: 2026-10-29, in full (the descriptif PDF, 6 pages; the field list; the dataset page's description); Météo-France's open-data wiki pages "Données climatologiques" and "Documentation sur le contenu des données publiques" read by a web-fetch agent and found silent; by the main ingest session
status: read
diseases: []
crops: []
regions: [France]
processes: [weather data, time stamps]
records: []
datasets: []
files: [dr1029_meteofrance2026hourly.pdf (the 2026-10-29 requests drop; with the field list and the dataset page's text beside it)]
---

# Météo-France's hourly climatological data: what the stamps say, and where the documents are silent

What Météo-France says about AAAAMMJJHH, T, U and RR1 in "Données climatologiques de base -
horaires", for Agrarium's D65 (`literature/requests/station-stamps-d65.md`).

**Read this first.** The zone is stated on the dataset's page, not in the field description. T
is an instant. Nothing says which hour RR1 covers, whether U is an instant, or that anything
changed between 2000 and 2022.

## What it holds

- **AAAAMMJJHH:** "date de la mesure (année mois jour heure)" (descriptif, p. 1; field list).
- **Zone:** "Les heures sont exprimées en UTC pour la métropole et en FU pour l'outre-mer" (the
  dataset's description on data.gouv.fr, read 2026-10-29). In the field list only the radiation
  and sunshine fields say "en heure UTC" (GLO, DIR, DIF, UV, INFRAR, INS), beside "TSV"
  variants.
- **T:** "température sous abri instantanée" (descriptif; field list: "température sous abri
  instantanée (en °C et 1/10)"). TN and TX are the minimum and maximum "dans l'heure".
- **U:** "humidité relative (en %)", with no qualifier. UN and UX are the minimum and maximum "dans
  l'heure".
- **RR1:** "quantité de précipitation tombée en 1 heure (en mm et 1/10)". DRR1 is its duration in
  minutes.
- **Quality codes:** 9 filtered, 0 protected, 1 validated, 2 doubtful (descriptif, last page).

## Silent

- Whether the stamp ends the hour, as for RR1 (the hour ending at HH, or starting at it).
- Whether U is an instant, and at what minute T is taken.
- Any change of zone, sampling, automation or time base between 2000 and 2022. The open-data
  wiki's pages are silent too.

## Dependence

- None: a provider's documentation.

## Bearing (2026-10-29)

- For metropolitan France, read AAAAMMJJHH as UTC (stated) and T as an instant (stated). The
  documents give no change that would make 2018-2022 differ from 2000-2001.
