---
id: delbac2026
citation: Delbac, Lionel, Smits, Nathalie, Mérot, Anne & Fermaud, Marc. 2026. 1941-2023 overall annual intensity indicator data for grapevine pests and diseases over three French vineyard regions. Data in Brief 64: 112397 (online 16 December 2025)
doi: 10.1016/j.dib.2025.112397
read: 2026-10-22, in full (Europe PMC full text PMC12813327, no figures) by the main session; the dataset's grade table, scale and read-me opened (Recherche Data Gouv, doi 10.57745/HM3HBE)
status: read
diseases: [downy mildew, powdery mildew, black rot, grey mould, rotbrenner, grapevine moths]
crops: [grapevine]
regions: [France, Bordeaux, Gironde, Champagne, Marne, Vaucluse]
processes: [season severity, warning service, history matching]
records: []
datasets: [delbac2026.grades]
files: [PMC12813327.xml (Europe PMC full text, the 2026-10-22 drop)]
---

# Delbac et al. 2026: 83 years of yearly disease and pest grades in three French vineyard regions

A data paper. The French agricultural warning service's bulletins and yearly summaries were read and each year given one grade per disease or pest, 1941-2023, for Bordeaux (Gironde), Champagne (Marne) and Vaucluse. No formulation.

**Open data.** Recherche Data Gouv, doi 10.57745/HM3HBE, licence Etalab 2.0 (open, attribution). The paper is CC BY 4.0 (l. 7, 24).

## What it holds

- **The scale** (Table 3, l. 233-254): 0 no epidemic; 1-3 local epidemics (1 almost non-existent, 2 medium in susceptible sites or untreated areas only, 3 severe there); 4-6 general epidemics (4 widespread with low damage, 5 generalized or high pressure, 6 exceptional pressure with significant damage).
- **Coverage** (Table 1, l. 42-118): seven organisms (downy and powdery mildew, black rot, grey mould, rotbrenner, *Lobesia botrana*, *Eupoecilia ambiguella*). Downy mildew in Bordeaux has 83 graded years, median 2; Champagne 64 years, median 3. 1,297 grades awarded and 447 NA in all (l. 255).
- **Sources** (l. 191-192): the regional warning bulletins, which were based on "observations, trapping and/or modelling". Bordeaux mostly from the yearly summaries; Champagne from *Le Vigneron Champenois*; the most complete span is 1960-2023.
- **Region notes** (l. 153-157): in Bordeaux downy mildew "is always present, but tends to be localized"; in Vaucluse "mildews are the main recurring diseases, often reported as widespread and/or very severe".
- The method follows Zwankhuizen & Zadoks's five-grade scale for potato late blight (l. 231).

## Dependence

- The grades are read from bulletins that were partly based on modelling (l. 191). The models are unnamed, so the grades may carry a warning model's view, as `bregaglio2022`'s bulletin classes do. No formulation is fitted to them in this paper.

## Bearing (2026-10-22)

- **For Agrarium's history matching** (TRUTH-METHOD part 2): a season-level severity series with no gaps for downy mildew in Bordeaux, and one for a Mediterranean region (Vaucluse). It is the test the autumn-inoculum question lacked (`dm.primary_dose_scale`; Sarejanni's and Rouzet & Jacquin's patterns). With a reanalysis (ERA5 or E-OBS) for each region, one can check whether autumn and winter rain predict the next season's grade. The grades are ordinal, with three regions and up to 83 years.
- **For Cooptera:** a yearly check of season-level risk in three regions, coarse but long. Grades say "local" or "general", not dates.
