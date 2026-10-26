---
id: legler2013
citation: Legler, S. E., Caffi, T. & Rossi, V. 2014 (online 2013-10-29). A model for the development of Erysiphe necator chasmothecia in vineyards. Plant Pathology 63:911-921
doi: 10.1111/ppa.12145
read: 2026-10-22, in full (11 pages, two columns interleaved; the text layer replaces every decimal mark with a control character, so numbers are read as printed, and the equation coefficients were read from the page image of PDF p. 2), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [Italy, Po Valley, Germany, Baden-Württemberg, Australia, South Australia]
processes: [powdery mildew, chasmothecia, overwintering inoculum, temperature response, rain-splash dispersal, model validation]
records: []
datasets: []
files: [gd1021_legler2013.pdf (the 2026-10-22 drop)]
---

# Legler et al. 2014: a temperature-driven model of Erysiphe necator chasmothecia maturation and rain-splash dispersal

Three temperature-driven stage rates (yellow, brown, black) move chasmothecia to maturity, and rain of 0.2 mm or more disperses the black ones; checked on trap and leaf counts from 38 vineyards. The id uses the online year (2013); the printed year is 2014.

**Read this first.** There is no ascospore release model in this paper: every ascospore statement is cited from Rossi et al. 2010 (`rossi2010`, l. 41-42). What is modelled is the maturation of the overwintering bodies and their dispersal onto the bark by rain splash. The start date of each vineyard's run was fitted by an iterative procedure that minimises the residuals (l. 112), so the fit statistics below are partly on fitted data and the model does not predict when chasmothecia begin. Every decimal mark is a control character in the text layer (0.95 prints as 0 then a control character then 95; 15.4 as 15 control 4): numbers here are decoded, and integers without the control character are real integers. The equations at l. 129-150 lose their decimals and minus signs; the coefficients below were read from the page image. The plus-or-minus sign is lost in the mean values at l. 249-252 and 444-456.

## What it holds

- **Structure:** four states, white, yellow, brown and black (mature) chasmothecia, advancing at rates R(ye), R(br) and R(bl) set by air temperature T (l. 118). Black chasmothecia are dispersed by rain splash whenever there is measurable rain, 0.2 mm or more (printed "02 mm"; the page image shows 0.2 mm; l. 123). The model starts at the first primordia, when white = 1, the total produced (l. 112). Built in Powersim Studio 8 by systems analysis.
- **Equations** (PDF p. 2, l. 129-150; unnumbered; rates are the first derivatives of the Legler et al. 2012 development equations in Teq and time t, l. 125; T in degC):
  - R(ye): y = 10 (4.06 Teq^0.61 (1 - Teq))^1.46 exp(-(0.1 (24.68 Teq^1.42 (1 - Teq))^0.37) exp(-(1 (3.32 Teq^0.78 (1 - Teq))^6.57) t)), Teq = (T - 5) / 30, so 5 to 35 degC (l. 135).
  - R(br): y = 10 (Teq^-0.07 (1 - Teq))^0.16 exp(-(0.1 (2960 Teq^4.6 (1 - Teq))^0.07) exp(-(0.3 (1.78 Teq^0.14 (1 - Teq))^1.24) t)), Teq = (T - 10) / 20, so 10 to 30 degC (l. 142).
  - R(bl): y = 100 (4.22 Teq^1.36 (1 - Teq))^1.95 exp(-(1.82 Teq^1.61 (1 - Teq))^1.25 exp(-(2.77 Teq^0.84 (1 - Teq))^4.15 t)), Teq = (T - 10) / 20 (l. 150).
  - The unit of t is not given in the facts read.
- **Start date:** it ranged from 7 August to 30 September between vineyards, almost two months (l. 299). The abstract suggests a temperature drop to values favourable for ascocarp production over 2 to 4 days in the week or two before the start probably triggered production (l. 21).
- **Data:** 38 commercial vineyards: the Po Valley, northern Italy (34, 2005 to 2010), Baden-Württemberg (2, 2010) and South Australia (Riverland and Langhorne Creek, 2011) (l. 170-176; l. 15 gives 2005 to 2011). Dispersed chasmothecia were trapped in 31 Italian vineyards with 13 cm plastic funnels, five a vine on three vines (15 funnels), filters changed every 2 weeks until leaf fall (l. 177, 181); 26 of these were used to validate (l. 389). In eight vineyards (2009 to 2011) chasmothecia on leaves were counted, from 12 leaves sampled from the untreated plot every 5 to 9 days (l. 212). Maximum trapped: 15.4 and 13.2 per cm2 of trap surface (Tebano 2007; C.S. Pietro 2009; l. 314). Black chasmothecia per cm2 of leaf in the eight vineyards: 107 (Travazzano 2009), 110 (Piacenza 2010), 59, 20, 50, 27, 158 (Loxton 2011) and 59 (l. 292).
- **Fit to trap counts** (26 vineyards, l. 441): aggregate R2 0.95, standard error of the estimate 0.097, concordance coefficient 0.97, Nash-Sutcliffe 0.94, W 0.98, EF 0.94, mean absolute error 0.12 (W and EF as labelled in the paper).
- **Fit to leaf counts** (8 vineyards, l. 451): R2 0.91, concordance 0.95, Nash-Sutcliffe 0.90, W 0.98, EF 0.90, mean absolute error 0.18.
- **Misses and limits:** overestimation of dispersed chasmothecia came in rain-free periods; missing splashing rain was a main cause (l. 571). Dispersal is mostly by rain splash and also leaf flutter (Gadoury and Pearson 1988; Cortesi et al. 1995, cited; l. 560). How rainfall rate, intensity and duration change the number detached and dispersed is not known (l. 662). Temperature alone is an acceptable driver, with indices between 0.90 and 0.97; initiation of chasmothecia, which depends on density and heterothallic mating, is not modelled (l. 650).
- **Cited, not modelled** (Rossi et al. 2010): chasmothecia overwinter and release ascospores the next spring, mainly between budbreak and bloom, repeatedly, causing primary leaf infections (l. 41-42). Millions of chasmothecia per hectare (l. 38).

## Dependence

- **Borrows** the development equations (the Teq forms) from Legler et al. (2012; controlled conditions); the trap method from Gadoury and Pearson (1988); the systems-analysis structure from Leffelaar (1993); goodness-of-fit indices from Nash and Sutcliffe (1970) and Madden et al. (2007). Ascospore release conditions are cited from Rossi et al. (2010), held as `rossi2010`, and not modelled. Shared authors with `rossi2010` (Rossi, Caffi, Legler): a flag.
- **Fitted to** its own trap and leaf counts (none published; counts are in the figures) with the start date fitted per vineyard. Not part of the engine's models.

## Bearing (2026-10-22)

- **Chasmothecia maturation:** answered, with three temperature rate equations (T in degC, 5 to 35 and 10 to 30 degC ranges) that are pure functions of an array of temperatures and a time, so they could be written as a non-engine formulation candidate, with the start date as an input. **Ascospore release:** not answered; the paper contains no release parameters. Use `rossi2010` for primary inoculum timing.
- **Dispersal rule:** chasmothecia reach the bark by rain splash when rain is 0.2 mm or more; this is the rule for the overwintering bodies, not for the spores that infect leaves. The paper itself says how rain intensity and duration matter is unknown.
- **Validated on** trap counts in 26 vineyards and leaf counts in 8, mostly Po Valley, with the start date fitted per vineyard on the same observations; no vineyard outside the 38, no Penedès or Spanish vineyard, and no test of a start date predicted from weather. Kind of result: a mechanistic model with fit indices of 0.90 to 0.97, in part on fitted data.
