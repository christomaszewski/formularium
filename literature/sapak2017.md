---
id: sapak2017
citation: Sapak, Z., Salam, M.U., Minchinton, E.J., MacManus, G.P.V., Joyce, D.C. & Galea, V.J. 2017. POMICS: a simulation disease model for timing fungicide applications in management of powdery mildew of cucurbits. Phytopathology 107(9):1022-1031
doi: 10.1094/PHYTO-11-16-0413-R
read: 2026-10-20, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5); not read in full
status: read
diseases: [powdery mildew (Podosphaera xanthii)]
crops: [zucchini (cucurbits)]
regions: [Queensland, Australia]
processes: [conidial germination, latent period, secondary infection cycles, logistic severity, fungicide reduction factor, spray timing]
records: []
datasets: []
files: [sapak_2017.pdf (the 2026-10-20 drop)]
---

# Sapak et al. 2017: POMICS, a weather-driven powdery mildew model for zucchini

A simulation of Podosphaera xanthii on zucchini. Germination follows hourly temperature and VPD thresholds. The latent period follows temperature, severity follows a logistic curve, and each fungicide spray reduces severity in the next cycle.

## What it holds

- **Germination:** four thresholds on hourly temperature and VPD (eq. 1, l. 88-96). The latent period is set by temperature thresholds (eq. 2, l. 120-126). Severity follows a logistic curve (eq. 3, l. 133-135). The reduction factor follows Caffi et al. 2012 (eq. 4, l. 148).
- **Fungicide effect:** an application can reduce severity by 90% (l. 198).
- **Validation:** two natural-infection datasets gave mean differences of 0.02 and 0.05 on a 0 to 5 scale (abstract, l. 27-28).
- **Field trials:** Bowen, North Queensland, spring 2008 (l. 159). Gatton, autumn 2011 (l. 120-121). Gatton, spring 2011 (l. 153).
- **Parameters:** nine, listed in Table 2 (l. 164).

## Dependence

- Reduction factor from Caffi et al. 2012 (l. 148).
- Germination from Reuveni and Rotem 1974 (l. 39-41).
- Latent period and infection cycles from van Maanen and Xu 2003, and de Vallavieille-Pope et al. 2000 (l. 46-50).
- Risk index from Gubler et al. 1999 (l. 129). Severity scale from MacManus and Akem 2008 (l. 95).

## Bearing (2026-10-20)

- Strand t3 (powdery mildew), with a link to t1 (spray timing). The structure is a template to refit for grapevine powdery mildew, not a grape formulation. A growers' engine could take the spray-reduction rule as a hypothesis to test.
- Not read in full.
