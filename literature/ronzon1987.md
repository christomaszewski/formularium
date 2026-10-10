---
id: ronzon1987
citation: Ronzon, Cécile (épouse Tran Manh Sung). 1987. Modélisation du comportement épidémique du mildiou de la vigne (Plasmopara viticola), étude de la phase sexuée. Thèse, Université de Bordeaux II, defended 29 April 1987 (supervisors S. Strizyk, M. Clerjeau). HAL tel-02856849
doi:
read: 2026-10-09, in full in an OCR (tesseract, French, 186 pages) by a reading agent (claude-haiku-5-5); 90 quotes checked by scripts/verify_quotes.py; EPI's corrected equations checked in the page images (pp. 49, 51) and the POM fitting passage in the text by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Bordeaux]
processes: [oospores, primary infection, forecasting, validation]
records: [epi1983.corrected, tranmanhsung1990.pom]
datasets: [ronzon1987.bordeaux, tranmanhsung1990.bordeaux]
files: [ronzon1987_these.pdf]
---

# Ronzon 1987: EPI tested, and the thesis that became POM

## What it holds

- **EPI (Strizyk):**
  - **Phases:** a winter potential-energy phase, monthly from October to March, from
    rain and temperature against 20-year normals; then a daily kinetic phase from relative
    humidity.
  - **Two versions printed:** the 1983 original, and the "Modèle 83 corrigé" (pp. 49, 51;
    record `epi1983.corrected`).
  - **What the correction changed:** rain distribution weighted in EN, more weight to
    daytime humidity, tighter humidity bounds, and the 19 °C temperature bound dropped as
    "injustifiée biologiquement".
- **EPI tested:** a posteriori on 1975-1982 and in real time 1983-1986, against the Plant
  Protection Service's attack classes. The end-of-March EPI flagged 1977 (exceptional
  attacks) and 1976 (no mildew); [-10, 0] is a critical zone (p. 51).
- **Oospore experiments:**
  - **Material:** Malbec in 1984 and 1985, Muscadelle in 1986, formed in chambers from
    25,000 sporangia/ml.
  - **Chambers:** weekly alternation of 10 °C and -5 °C at saturation matured them best;
    constant 25 °C and -5 °C inhibited.
  - **Peak germination:** 44 % (1985, Table 9) and 19 % (1986, Table 10).
  - **Buried in the vineyard:** an optimum of 25-30 % after about 4 months (1985) and 6.5
    months (1986).
  - **Germination time:** mature oospores germinated in 7 days at 20 °C and 13 at 15 °C;
    best at 20-25 °C, not at 10 or 30 °C.
- **POM, the thesis version:**
  - **Form:**
    - a monthly rain index compensating deficits and excesses against normals;
    - T/10 = A Im + B and v = C Im + D;
    - a normal-law maturity curve.
  - **Fit:** "Les coefficients A, B, C et D ont été déterminés à partir des valeurs
    réelles de T et v obtenues en 1986 et 1985". The coefficients themselves are not
    printed.
  - **Check:** 1984 (calculated optimum 17 April, observed 16 April).
- **Severity:** classes IG 1-4 from the optimum date, compared with observed classes
  1977-1986: six exact, four off by one (Table 27). No regression is printed.
- **PCOP (primary-infection dates):**
  - germination 7 days after maturity at 20-25 °C, 12 at 15 °C;
  - contamination needs T > 11 °C, high RH and rain;
  - spore release 7 days after contamination;
  - mean gap to observed foci, 1977-1986: 4.7 days.
- **Not legible:** tables 11-22 and 24-26 were not read from the page images; OCR-garbled
  values are marked in the reading, not used.

## Dependence

- **EPI:** Strizyk's own model, with no engine model computed. Its form (a potential index
  against normals) is not one the engine runs; tagged `potential-energy-index`.
- **POM:** the published version is Tran Manh Sung et al. 1990
  ([tranmanhsung1990](tranmanhsung1990.md)). The thesis's 1985 and 1986 dates are two of
  that paper's three.
- **Older sources it relies on:** Müller & Sleumer 1934 (incubation), Blaeser & Weltzien
  (wetness), Zachos 1959.
- Goidanich, Magarey, Lalancette and VitiMeteo do not appear.

## Bearing (2026-10-09)

- **D32:** POM's thesis fit rests on two years and one check, which is thinner than
  `tranmanhsung1990.bordeaux` suggests.
- **EPI** is a candidate season-potential model outside the engine's lineage, printed here
  in full. It needs 20 years of normals. Epicure's present thresholds are not printed
  anywhere we hold.
- Oospore maturation against chamber temperatures and burial is data for TRUTH-METHOD's
  oospore-season row.
