---
id: roubal2013
citation: Roubal, Christophe, Regis, S. & Nicot, Philippe C. 2013. Field models for the prediction of leaf infection and latent period of Fusicladium oleagineum on olive based on rain, temperature and relative humidity. Plant Pathology 62 (3):657-666
doi: 10.1111/j.1365-3059.2012.02666.x
read: 2026-10-08, in full, with the page images of Tables 1-4, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [olive scab]
crops: [olive]
regions: [Provence]
processes: [infection, latent period]
records: []
datasets: []
files: [10-1111-j-1365-3059-2012-02666-x.pdf]
---

# Roubal, Regis & Nicot 2013: field models of olive scab infection and latent period

From the regional plant protection service (Montfavet) and INRA Avignon. Olive, not grape.

## What it holds

- Ten-year field survey, one Grossane orchard (2 ha, Baux-de-Provence, France), 1999-2009 (l. 224) (l. 230) (l. 231); ten trees, 100 leaves per date, scored 1-3 times a week 1999-2004 (l. 258) (l. 260). Latent infections found by KOH clearing.
- 376 rain events were sorted into infectious or not: 134 infectious, 191 not, 51 dropped (l. 284) (l. 446).
- Sorting used thresholds from Chen & Zhang (below 6 C, RH>85% under 6 h) and Obanor et al. (10-20 C, over 12 h) (l. 295) (l. 297). Ambiguous rains were then sorted using the authors' own latent-period fit (l. 304) (l. 348). 71 of 134 infectious events came this way (l. 444) (l. 446).
- Latent period (days): Di = 364.76 - 89.57T + 9.12T^2 - 0.43T^3 + 0.0078T^4, T mean temperature since rain start (l. 460) (l. 462). R2 above 0.98 (l. 74). Printed digits give 16.3 d at 16 C against about 13 d on Fig. 5 (checked by the reading agent).
- Infection after rain: hours of RH>85% needed, as a function of mean temperature in rain; vapour-pressure curves (l. 541); coefficients only in Table 1, an image.
- Neural net: 2 inputs, 2 hidden neurons, all weights printed in Table 3 (l. 413) (l. 881); 2 errors in 325 events (l. 478). Activation is not printed.
- Validation at 40 sites 2009-2011: one miss, unpublished (l. 617).

## Dependence

- Its own ten-year survey of one orchard (1999-2009). **Its data are partly shaped by its own model:** ambiguous rains were sorted with the authors' latent-period fit, then the fit was redone on the enlarged set (l. 304, 348); 71 of 134 infectious events came this way (l. 444-446). A circularity within the paper, not a link to the engine.
- Its moisture input is hours of RH > 85% after rain begins: a humidity threshold standing for wetness, the engine's form (`rh-threshold-wetness`).
- No author of an engine model.

## Bearing (2026-10-08)

- **Held out by structure** through its RH-threshold wetness (Agrarium's candidates). Its quartic latent period, Di = 364.76 - 89.57T + 9.12T² - 0.43T³ + 0.0078T⁴ (l. 460), does not reproduce Fig. 5 at 16 °C (16.3 against about 13 days, the reading agent's check): use with care, and only between about 8 and 22 °C.
