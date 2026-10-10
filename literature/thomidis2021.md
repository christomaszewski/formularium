---
id: thomidis2021
citation: Thomidis, Thomas, Michos, Konstantinos, Chatzipapadopoulos, Fotis & Tampaki, Amalia. 2021. Evaluation of Two Predictive Models for Forecasting Olive Leaf Spot in Northern Greece. Plants 10:1200
doi: 10.3390/plants10061200
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [olive leaf spot]
crops: [olive]
regions: [Northern Greece, Chalkidiki, Potidea]
processes: [conidial germination, infection, leaf wetness, temperature response, incubation, severity, spray timing, model validation, warning system]
records: [magarey2005.generic]
datasets: []
files: [q174.pdf]
---

# Thomidis et al. 2021: two predictive models for olive leaf spot in Greece

A light read (the deep-research B list).

## What it holds

- Olive leaf spot (Venturia oleaginea), Northern Greece: two infection models tested against field symptoms in 2016, 2017 and 2018 (l. 15-27).
- Own germination trials: range 5 to 25 C, optimum 20 C (l. 19); at least 12 h of wetness (l. 20).
- Generic Magarey 2005 model on the paper's own parameters: Tmin 5 C, Tmax 25 C, Topt 20 C, Wmin 12 h, Wmax 24 h (l. 636-637).
- The generic model fitted symptom incidence better than the polynomial (l. 27).
- Table 1: generic first infections 15 May 2017 (l. 343) and 3 October 2018 (l. 344); polynomial 15 May 2016, 5 May 2017 and 2 October 2018 (l. 346-348).
- Risk threshold printed as 29 in the results (l. 322) and 30 in the methods (l. 675).
- Field data on request only (l. 732).

## Dependence

- Computes the Magarey et al. 2005 generic infection model: runs it as its risk model (l.633-637), with parameters Tmin 5, Tmax 25, Topt 20 C and Wmin 12, Wmax 24 h, fitted to this paper's own olive germination trials (l.596-616); then validates it in the field against symptom dates (l.661-702; Table 1; Figure 5). No equation or parameter from the Goidanich, Kennelly, Rossi or VitiMeteo models appears in the text. The polynomial (Obanor et al.) and the Villalta leaf-wetness rule (Venturia pirina, l.648-649) are not on the engine list. Shared author: none with engine-list papers.

## Bearing (2026-10-10)

- Gives a Magarey-type infection response run on field data with a stated validation rule (predicted day against observed symptom onset), a useful test of the engine's wetness-temperature logic on a non-grape host, but the engine must not be fitted to it.
