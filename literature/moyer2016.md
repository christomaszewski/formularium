---
id: moyer2016
citation: Moyer, Michelle M., Gadoury, David M., Wilcox, Wayne F. & Seem, Robert C. 2016. Weather During Critical Epidemiological Periods and Subsequent Severity of Powdery Mildew on Grape Berries. Plant Disease 100(1):116-124
doi: 10.1094/PDIS-12-14-1278-RE
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [New York]
processes: [season severity]
records: []
datasets: []
files: [10-1094-pdis-12-14-1278-re.pdf]
---

# Moyer et al. 2016: weather in critical periods and powdery mildew on berries

From Cornell (NYSAES Geneva).

## What it holds

- 30 years of untreated cluster severity on hybrids at NYSAES, Geneva NY, 1981 and 1983-2011: 0.2 to 50.5% (l. 14, 122); Chardonnay in 7 years 3.42 to 99.5% (l. 15-16, 129-131).
- Model development used 22 Rosette years, 1986-2007 (Table 1, l. 88-109). Weather came from the NOAA station at NYSAES with a Class A pan (l. 71, 74).
- Eq. 1: Log(severity) = 4.44 - 1.09 Epan + 0.01 DD10 (l. 261). Epan is mean daily pan evaporation, 1 June-31 July (mm); DD10 is degree-days base 10 C, 1 Aug-15 Sep the year before (l. 266-267).
- Eq. 2: Prob(Mild) = 1/(1+exp(-0.45 + (-0.02 DD10) + 1.98 Epan)) (l. 277); printed signs conflict with the text. Severe is >=9% for hybrids, >58% for Chardonnay (l. 169, 183-184).
- Severe if P(Severe) >= 0.29: sensitivity 1.0, specificity 0.66, AUC 0.86 (l. 281-284).
- RPA tree: Epan >= 6.07 mm is Mild; DD10 >= 450 is Severe; then Epan < 5.45 mm (l. 296-307). R2 0.61, AUC 0.89 (l. 294).
- Validation on hybrids: LRA sensitivity 0.83, specificity 0.50 (l. 320-321); RPA 0.40 and 0.33 (l. 329-330). Chardonnay: 1 error in 7 years (l. 295-297).
- Both fitted only to the lab's own harvest ratings and the station's weather. No model dated the data. The windows rest on Pearson and Gadoury's chasmothecia work (cited).
- Epan can be replaced by Penman-Monteith Eto (Allen et al. 1998), slope 1.06 (l. 234, 319).

## Dependence

- Thirty years of untreated severity at Geneva; logistic and tree models on pan evaporation and degree-days. Eq. 2's signs as printed contradict the text (dry years mild); the printed form is kept and flagged.
- Moyer, Gadoury, Wilcox and Seem are authors of engine models (Ferguson 2014; Kennelly 2005, 2007): flags. Under D19 it was kin for them.

## Bearing (2026-10-08)

- **A flag now, not kin.** A season-severity pattern for powdery mildew made outside the engine's models.
