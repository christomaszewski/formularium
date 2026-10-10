---
id: tranmanhsung1990
citation: Tran Manh Sung, C., Strizyk, S. & Clerjeau, M. 1990. Simulation of the date of maturity of Plasmopara viticola oospores to predict the severity of primary infections in grapevine. Plant Disease 74(2):120-124
read: 2026-10-08, in full (OCR text, equations and tables on the page images) by a reading agent (claude-sonnet-5-5); 60 quotes checked by scripts/verify_quotes.py, the model and dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [oospore maturation, season severity]
records: [tranmanhsung1990.pom]
datasets: [tranmanhsung1990.bordeaux]
files: [PlantDisease74n02_120.PDF]
---

# Tran Manh Sung, Strizyk & Clerjeau 1990: POM, the date oospores mature

From INRA Bordeaux (Villenave d'Ornon; Tran Manh Sung, Clerjeau) and SESMA, Paris
(Strizyk). The byline prints the names in capitals (l. 4-6).

## What it holds

- **The model (POM):** the date of oospore maturity (DOM) from rain alone, counted from
  21 September, with no temperature (l. 559-560). Each day's rain is compared with two
  limits from the 1946-1987 normals (l. 109): Hm = monthly normal over its mean rainy days
  (l. 427) and HM from the normal plus its standard deviation (l. 433; the bracketing is
  ambiguous in print and on the page image). Rain between the limits counts in full, above
  HM as HM, below Hm as a lack (l. 437-439). The monthly index is
  Im(M) = [POS(M) - NEG(M)] + Im(M-1), NEG = |EXC - LAC| (l. 445).
- **Fit:** DOM, in days from 1 January, is T = A·IJ + B, with IJ the index at the end of
  January, A = -0.21 and B = 117.9 (l. 492), the mean of two fits (-0.24 and -0.19; l. 489,
  491) to three dates from the authors' own burial assay at an INRA Bordeaux vineyard:
  about 24 March 1985, 2 May 1986 and 24 March 1988 (l. 155-156).
- **Severity:** regional severity on a 1-4 scale, 1977-1988, over about 100,000 ha
  (l. 113-121), rated by the authors from the Plant Protection Service's bulletins
  (l. 114-116), correlates with IJ (r = 0.90, l. 474): S = 1.7 + 0.012·IJ (l. 508). Class
  limits at IJ = -17, 67 and 150 give limit dates of 1 May, 14 April and 27 March
  (l. 514-519).
- **Validation** is a posteriori, as the paper says (l. 69): the same twelve years fit and
  test the classes. The reading agent recomputed A, B and the severity fit from the
  printed tables; Table 3's dates match but for 1982 (one day).
- **Unstated:** what counts as a rainy day; whether LAC counts dry days; the maturation
  curve after the peak.
- **Garbled in the text copy:** Table 1's December 1979 value (-111 on the page image);
  Table 3's severity columns (read on the image).

## Dependence

- It takes EPI's idea, that rain counts only between limits set from climatic normals
  (Strizyk 1983; l. 566, 577), but computes none of EPI's equations. EPI's equations are
  printed in Ronzon 1987 ([ronzon1987](ronzon1987.md), `epi1983.corrected`), the thesis POM
  came from.
- Its maturity dates come from the authors' own assay; nothing was dated by a model. The
  severity ratings come from regional bulletins whose own basis is not stated (a flag:
  they may have leaned on EPI).
- DMCast (Park et al. 1997) computes POM's index for its rain term (read in Caffi et al.
  2007, eq. 6; see [caffi2007](caffi2007.md)). Neither is an engine model.
- No author of a model the engine runs.

## Bearing (2026-10-08)

- **Clear of the engine by every substantive test,** and its author list is read. It was
  "clear" before D27 too. What decides its use is its structure tag: as Formularium's
  vocabulary reads today, a regression of the maturity date on a weather index is "a
  fitted statistical model of weather" (`oospore-glm`), the tag of Leoni 2026's model,
  which the engine runs. Agrarium's PLAN 15 recommends a tag of its own (D32), which would
  make POM a candidate for an evaluation family's oospore maturation.
- Three fitted dates are thin, and it maps rain to one date, not a cohort curve: a truth
  needs an assumed spread around the date.
