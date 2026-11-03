---
id: viret2014
citation: Viret, O., Gindro, K., Schaerer, S., Steinger, T., Wirth, J. & Jermini, M. 2014. Rapport d'activité 2013: Protection des végétaux [Activity report 2013: plant protection]. Agroscope Transfer No 29/2014
doi:
read: 2026-11-03, the oospore, model and first-spot rows of Table 12 (p. 37) and the text on them, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); the table was also read in the page image by the main session; 33 of 33 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland, Changins (Nyon, Vaud)]
processes: [oospore maturity, germination test, 140 C temperature sum, VitiMeteo, first oil spots, untreated control]
records: []
datasets: []
files: [dr1103_viret2014.pdf (the 2026-11-03 drop)]
---

# Viret et al. 2014: Changins oospore maturity, model date and first oil spots, 2003 to 2013

An Agroscope activity report whose Table 12 (p. 37) gives, for each year at Changins, the date oospores germinated within 24 h in the outdoor laboratory test, the date the 140 C temperature sum was reached, and the date of the first oil spot in the untreated control.

**Read this first.**
- The three rows are three kinds of evidence. The germination row and the first-spot row are observations by the Changins group (their own). The 140 C row is VitiMeteo's model, not an observation.
- The table prints 11 values under 10 year headers; the eleventh column is unlabelled. It is read as 2013 because the text says "pour les années 2003 à 2013" (for the years 2003 to 2013). The leads file reports that the 2011 report prints 2003 to 2011 identically and that a 2013 review gives full maturity on 30 April 2013.
- The values below are as the main session read them in the page image; the script-checked quotes are the text-layer lines of the same rows.
- Not independent of VitiMeteo (see Dependence). Cover authors as the reading JSON gives them ("authors as listed on the cover").

## What it holds

- **Oospore maturity, germination within 24 h (l. 2621):** 2003-04-23, 2004-04-15, 2005-05-02, 2006-05-11, 2007-04-30, 2008-05-05, 2009-05-04, 2010-04-12, 2011 "non atteinte" (not reached), 2012-04-25, 2013-04-30.
- **Model date, sum of daily mean temperature above 8 C from 1 January reaches 140 C (row "140° (>8° C)", l. 2631):** 2003-04-30, 2004-05-15, 2005-05-03, 2006-05-07, 2007-04-22, 2008-05-11, 2009-04-30, 2010-04-30, 2011-04-19, 2012-04-30, 2013-05-10.
- **First oil spot in the untreated control ("témoin", l. 2635):** 2003-05-26, 2004-06-11, 2005-06-06, 2006-05-22, 2007-05-29, 2008-05-26, 2009-05-25, 2010-05-18, 2011-05-16, 2012-05-14, 2013-05-17.
- **Model against test (arithmetic, not printed):** the model date is later than the test by 7 days in 2003, 30 in 2004, 1 in 2005, 6 in 2008, 18 in 2010, 5 in 2012 and 10 in 2013, and earlier by 4 days in 2006, 8 in 2007 and 4 in 2009. In 2011 the model reached 140 C on 2011-04-19 (l. 2631) but the test never reached germination within 24 h (l. 2621).
- **Mean test date (arithmetic):** the ten tested years, without 2011, average about 28 April (leap years ignored).
- The method of the test is not in this table. Dubuis et al. 2012 describe it (about 5 mm2 leaf pieces with oospores on soil tubes left outdoors; germination within 24 h at room temperature and 100 % RH).

## Dependence

- **Own observations** of the Changins group (Agroscope), Table 12 marked as such by the reading agent.
- **A model dated one row:** the 140 C row is VitiMeteo's temperature-sum rule. Dubuis et al. 2012 say the yearly Changins oospore test, the outdoor laboratory and the untreated control serve to validate VitiMeteo and let experts adjust it, so these observations were used in a model's validation. Leoni et al. 2026 also calibrate at Changins; a shared site is a flag, not a dependency.

## Bearing (2026-11-03)

- **literature/oospore_maturity_2026-11-03.csv (Agrarium D67):** adds eleven Changins laboratory-test rows, 2003 to 2013, with 2011 as "not reached" (a censored year, not a date), and eleven model rows (140 C) to be kept apart from observations. Kind of evidence: observation, dated by the group's own test; the 2013 column is inferred from position.
- **literature/real_outcomes_2026-11-03.csv:** adds eleven first-oil-spot dates in the untreated control at Changins, 2003 to 2013. Kind of evidence: field observation, in a series whose model was validated on it.
- **Question it bears on:** the Rossi oospore model starts the season too early in Germany. Changins gives a Swiss, tested maturity date for ten years, 2011 not reached (mean about 28 April; earliest 2010-04-12, latest 2006-05-11) to compare with the model's date, and the model-minus-test gaps above show how far a temperature sum alone can be from the test.
