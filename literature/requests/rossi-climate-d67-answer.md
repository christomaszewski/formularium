# Answer to rossi-climate-d67.md

2026-10-29, by an `ingest` session. A reading agent (claude-sonnet-5-5) read Rossi et al. 2008
(Ecol. Model.) in full for the first time, reread eight held sources, and used its 12 OpenAlex
queries. The main session rechecked all 79 quotes (`scripts/verify_quotes.py`) and the passages
the flags rest on. No new paper was found, so there are no new notes. Four held notes gained a
section: `rossi2008`, `caffi2009`, `rouzet2003`, `franche2012`.

## Short answer

**No source shows Rossi's lineage starting too early in a mild oceanic climate or in Germany,
because none tests it there.** The model was built and validated in Italy only. Its start, 1
January with no cold term, rests on an assumption the authors state. The sources point at least
as much to other causes, which Agrarium can check: a two-lesion vineyard, the host's
susceptibility, and the start date used in the southern hemisphere.

## 1. Where it was built and validated

- **Rossi et al. 2008** (`rossi2008`): 43 natural epidemics in Emilia-Romagna, 1995-2006, first
  onset 11 May-29 June (pp. 485-486).
- **Caffi et al. 2009** (`caffi2009`): 100 vineyard-years in Piedmont, Lombardy, Emilia-Romagna,
  Marche, Basilicata and Sardinia, 1995-2007 (p. 537).
- **No site is in Germany or has Auckland's climate.** Caffi 2009 (p. 545) says its sites span
  climate classes that cover Europe's grape areas. That is a claim, not a test.
- **Bears on:** both Auckland and Germany, as an absence of evidence.

## 2. Tests outside northern Italy

- **None found for Rossi's model:** not in New Zealand, Australia, South Africa, Brazil, Germany,
  France, Switzerland, Spain or Portugal.
- **What does exist** tests Gehmann's degree-day rule from 1 January (VitiMeteo; Rioja's UR
  model, `puelles2024`), not Rossi's. At Changins, VitiMeteo's rule timed primary infection
  rightly in 80 % of years (`leoni2026`).
- **Bears on:** neither directly. A count from 1 January is not months early at Changins.

## 3. The starting day

- Rossi 2008 starts the count on 1 January in every climate (p. 482).
- It gives no southern-hemisphere rule.
- **Bears on:** Auckland. Brook's primary infections fell from November to early January
  (`brook1992`). A count from 1 January starts there in midsummer, and from 1 July in late
  winter: which one Agrarium used decides the comparison.

## 4. Winter cold and dormancy

- **Rossi 2008 (p. 482):** cold that breaks dormancy "is not included in the model because it is
  assumed that oospores must experience such a low temperature in the winter of temperate
  climates."
- **Rouzet & Jacquin 2003 (pp. 440-441,** one site in south-western France, stored leaves): "Dormancy
  seems to be lifted by low temperatures in autumn and early winter". Correlations improved when
  the count started after 60 cold days (Tmax 7-15 °C; `rouzet2003.cold_days`).
- **Franche 2012** (Aquitaine) used that start. It moved the start by about three weeks: 21 and 24
  January and 31 December.
- **Bears on:** Auckland. A mild winter may give fewer cold days, so a cold-day start would come
  later there. That is untested, and the effect seen in France was weeks, not months.

## 5. Other causes the sources support

- **Inoculum and detection at Auckland.**
  - Brook 1992: "Primary infections were invariably represented by one or two lesions in the
    vineyard". Recorded canes on six vines were read weekly; the first lesions fell on a
    recorded cane in only one season.
  - Rossi's seasonal oospore dose is one, so the model cannot say when the first of one or two
    lesions appears. An observer's 3 % of vines does not fit such a vineyard.
  - Bears on Auckland.
- **Early modelled infections that give no disease.**
  - In 30 validation cases (FPP 0.08) Rossi's model predicted an infection with no onset, 85 %
    of them within the first week of May (p. 488).
  - The cause given: little susceptible host before 5-6 leaves, and low-density early cohorts
    (p. 489).
  - Caffi 2009 (p. 542) found such false alarms most often in the warmest, driest regions: 0.31
    Sardinia, 0.23 Marche, 0.16 Basilicata.
  - If Agrarium's host is susceptible earlier than 5-6 leaves (`kennelly2006` found shoots
    susceptible from E-L 5), cohorts Rossi's validation would call false alarms become lesions.
  - Bears on both.
- **Weather and dates.**
  - Nothing read speaks to reanalysis weather in these places.
  - Brook's station was 450 m from the vines.
  - The German first-symptom dates were not reread here.

## Records changed

- `rossi2008.oospores`: two flags, the 1 January start with no cold term, and validation in Italy
  only.
- `rossi2008.primary`: two flags, the early false alarms with their cause, and the dose of one.

## Not obtained

- Galbiati & Longhin 1984 and Vercesi et al. 2010 (EJPP): not held; no open file.
- Revue suisse 2009 VitiMeteo paper and a JKI paper: the sites refused automated fetches.
- Hill 2000, and Gehmann 1987's body text.
