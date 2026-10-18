---
id: vanderheyden2020
citation: Van der Heyden, H., Dutilleul, P., Charron, J.-B., Bilodeau, G. J. & Carisse, O. 2020. Factors influencing the occurrence of onion downy mildew (Peronospora destructor) epidemics: trends from 31 years of observational data. Agronomy 10:738
doi: 10.3390/agronomy10050738
read: 2026-10-18, in full, by a reading agent (claude-haiku-5-5); 60 of 60 quotes found at their lines by the main session; Table 1, Eq. 1 and Table 4 checked in page images by the reading agent
status: read
diseases: [onion downy mildew]
crops: [onion]
regions: [Quebec, Hemmingford]
processes: [epidemic onset, overwintering, season severity, logistic epidemic curve, discriminant analysis]
records: []
datasets: []
files: [herv__2020.pdf (the 2026-10-18 drop)]
---

# Van der Heyden et al. 2020: 31 years of onion downy mildew in Quebec

Weekly scouting of onion fields in south-western Quebec, 1987-2017, set against weather from
one station, to see which seasons' conditions go with earlier and heavier epidemics. It is
onion, not grapevine. No record.

## What it holds

- **Scouting** (l. 217-224): PRISME database, weekly, May to August, about 122 fields a season
  (about 70 % of the region's onion fields), at least 25 plants a field scored 1/0 for
  Peronospora destructor. Regional disease incidence (RDI) ran 0 to 33.25 %, with peaks in
  1990 and 2014 (l. 365-366); 33 % of affected fields in 2014 (abstract).
- **Weather** (l. 234-235): MELCC station at Hemmingford Four Winds, 70 m, 1986-2017. Sensors
  and shields not described. Variables in four groups: during the season (including DownCast
  sporulation periods, DC, and NHR_90, hours a day with RH above 90 %, which the paper does not
  call wetness), at harvest (15 August to 15 October in the text, to 1 October in Table 1),
  snow cover and the winter Hellmann number HL (sum of daily mean temperatures below 0 °C,
  15 October to 15 March in the text, November to March in Table 1).
- **Periods:** 1987-1996, 1997-2006, 2007-2017. ODM occurred in 5 of 10 years in period I
  (mean RDI 3.59 %) and in 11 of 11 in period III (9.55). First observation fell 93.8, 84.3
  and 63.4 days after 1 May by period; first observation, b10 and mid-time b were 30.4, 15.1
  and 11.3 days earlier in 2007-2017 than in 1987-1996 (abstract; r = -0.700, p = 0.0003).
- **Logistic curve** (Eq. 1, page 5): Y = K / (1 + exp(-r (t - b))), fitted per year; Table 3
  lists k, r, b with standard errors. The fits for 1993 and 2012 are degenerate (r 1.993 and
  2.021 per day, zero-width intervals). RMSE and R² of the 31 fits are described, not printed.
- **Weather by period (Table 2):** harvest mean temperature 17.30, 18.42, 18.81 °C; harvest
  minimum 7.28, 9.5, 10.5 °C; harvest rainfall 42.6, 90.9, 104.82 mm; Hellmann number -111.7,
  -98.97, -94.46 (less severe winters later; p = 0.0084); previous-year RDI 3.6, 0.1, 8.5.
- **Discriminant analysis:** all weather variables classify 70.6 % of years into their period;
  the stepwise subset (MTH, DS_PY, HL, TRH, RAD) classifies 93.5 % (90, 90 and 100 % by
  period). Both are in-sample; no hold-out is printed.
- **Oospores** (l. 1020-1047): the authors say the role of oospores is under-documented and
  that there is no clear evidence oospores in soil cause infection; infected immature bulbs
  may be an important primary inoculum. They cite McKay's 25-year experiment (oospores
  germinating up to 25 years after production). No oospore counts, survival rates or decay
  times for Quebec are printed.
- **Internal disagreements:** harvest window (l. 257 against Table 1, l. 307); snow cover in
  cm (l. 266) against mm (Table 1, l. 308); HL window (l. 272 against Table 1).
- **Not printed:** discriminant coefficients and classification matrices, Spearman
  coefficients, scouting dates by year, station sensor details, any leaf-wetness estimate.

## Dependence

- **Computes** DownCast (Jesperson & Sutton), as the count DC from station weather
  (l. 243-244); no other model. The logistic curve is generic.
- **Data:** scout observations; no model is said to have made them. Shared authorship with
  the cited onion downy mildew literature is a flag only.

## Bearing (2026-10-18)

For strand 1 (what the previous autumn and winter say about the next season's start):

- **What it shows about the previous autumn:** the seasons are grouped by period, and the
  periods differ in autumn and winter weather (warmer, wetter harvest weeks; milder winters;
  earlier first observation). It does not regress onset on autumn or winter variables, so there
  is no autumn-to-spring effect size or lag. The link is through group means, PCA loadings
  and an in-sample discriminant (93.5 %, five variables).
- **Not grapevine, not oospores:** the pathogen is Peronospora destructor on onion. Oospore
  survival is not measured; the authors cite it as a possibility and say the evidence that
  oospores cause infection is unclear.
- **Take for the sweep:** nothing to calibrate; the sweep can say that a rule linking autumn
  or winter weather to the next season's onset has, in a related downy mildew, only
  period-level support from one region. The Hellmann number and the RH > 90 % hour count
  are definitions only, with no fitted coefficients.
