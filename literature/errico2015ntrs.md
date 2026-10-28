---
id: errico2015ntrs
citation: Errico, R. & Privé, N. 2015. Development, validation, and application of OSSEs at NASA/GMAO. Conference presentation slides (36 slides), NASA Technical Reports Server 20150000376
doi: 
read: 2026-10-27, in full as slides: all slide text; the validation figures (real-versus-OSSE statistics) are images and were not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 12 of 12 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [OSSE, nature run, data assimilation, OSSE validation, observation error, twin experiment]
records: []
datasets: []
files: [syn1027_errico2015ntrs.pdf (the 2026-10-27 drop)]
---

# Errico and Privé 2015: slides on how the NASA GMAO OSSE is built, validated and criticised

A 36-slide deck by two of the authors of Errico et al. 2013 (Q. J. R. Meteorol. Soc. 139:1162-1178, doi 10.1002/qj.2027), giving the validation idea, the nature runs, the simulated observation errors and a list of criticisms with the authors' responses. No record: a review in slide form.

**Read this first.** These are conference slides, not the 2013 paper. The 2013 paper is paywalled and was not obtained (every route tried; see the strand's LEADS). Slide text carries no measured numbers on validation: the real-versus-OSSE statistics are in figures that were not read. The slide table of nature runs gives the ECMWF run as 35 km; `hoffman2016` gives about 26 km for the same T511 run (l. 206 there): the two disagree and neither was checked against ECMWF.

## What it holds

- **Validation principle** (l. 254-258): "As for any simulation, OSSE results apply to the assimilation" system only to the degree the OSSE "validates well with regard to relevant metrics". Validity is "first determined by carefully comparing" statistics that can be computed in both the real assimilation and the OSSE; validation and application are statistical.
- **Criticism of twins** (l. 331-333): the first "general criticism" listed is that the nature-run and assimilation models are "generally too alike, therefore underestimating model error and yielding overly-optimistic results". It is listed as a criticism to answer by design and validation, not as a result measured in the deck.
- **Past problems with some OSSEs** (l. 323, 325): very limited validation, unrealistic observation errors (for example no representativeness error), a deficient nature run, a reduced control observation set, very few case studies.
- **Simulated observation error** (l. 142, 236, 238): the GMAO OSSE adds random errors with tuned variances (some correlated) but "No mean errors added" and "No gross errors added"; real representativeness error is likely underestimated by the implicit component, so extra is simulated.
- **Authors' responses** (l. 350): design thoughtfully, validate carefully, beware of quick shortcuts, specify reasonable observation error statistics, "Avoid over-selling results".
- **Nature runs** (slide table, l. 105-115, found by grep and not among the reading agent's quotes): the table lists the ECMWF run at 35 km, 2 TB and the GMAO G5NR at 7 km, 2,500 TB.

## What TRUTH-METHOD says of it

TRUTH-METHOD's References table has no Errico entry (checked by search of the file). The strand took "Errico et al. 2013" as a source for the OSSE method (nature run unlike the forecast model; validate against real data). TRUTH-METHOD part 3 says an OSSE "is trusted only when the simulated impact of existing observations matches their real impact".

Verdict: **confirmed in kind, from slides, not from the 2013 paper.** The deck states the validation rule (l. 254-258) and the "too alike ... overly-optimistic" criticism (l. 331-333) in the direction TRUTH-METHOD uses. It holds no number on how large the optimism is, and it is not the paper the claim should cite. Read as 2015 slides standing in for the 2013 paper.

## Dependence

- Builds on Errico et al. 2013 (named on its validation-publications slide, not read) and on the GEOS-5 model and GSI assimilation system. Privé is also first author of `prive2023`: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 3:** the slides give the practitioners' own list of how OSSEs mislead (too-alike models, thin validation, observation errors with no bias or gross error, over-selling); simulated errors that lack bias and gross error also apply to Agrarium's simulated stations.
- **D60:** synthetic noise with no mean error and no gross error (l. 236-238) is the weakest form of synthetic input; use it for robustness checks, not to establish a feature.
- **Not shown:** how large the optimism is, or how the validation turned out: obtain the 2013 paper.
