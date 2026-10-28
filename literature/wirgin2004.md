---
id: wirgin2004
citation: Wirgin, A. 2004. The inverse crime. arXiv:math-ph/0401050 (version 1, 28 January 2004; preprint, 10 pages, no journal version found)
doi: 
read: 2026-10-27, in full (10 pages), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [inverse problem, inverse crime, synthetic data, parameter reconstruction, non-uniqueness]
records: []
datasets: []
files: [syn1027_wirgin2004.pdf (the 2026-10-27 drop)]
---

# Wirgin 2004: a critique of the "inverse crime" rule, with three toy problems

Examines the warning that synthetic data should not be made with the same model that inverts them, using a polynomial problem and a plane-wave reflection from a mirror. No record: a short analytic critique, not support for the rule.

**Read this first.** A preprint, and a dissent: it argues the crime is not always trivial and need not always be avoided. The word "overconfident" is not in it. Three toy examples with one parameter from one datum (l. 286). The accented characters of its reference list are lost in the text layer.

## What it holds

- **Definition** (l. 18, cited): the inverse crime "occurs when the same (or very nearly the same) theoretical ingredients are employed to synthesize as well as to invert data".
- **Origin of the term** (l. 47, 49, cited): coined by Colton and Kress (1992, 1998), who give the reason "in order to avoid trivial inversion" and add that the synthetic data should come from a forward solver "which has no connection to the inverse solver". The stated worry is triviality, not overconfidence.
- **The paper's stance** (l. 20): the act "has been qualified as trivial and therefore to be avoided"; "Their judgement is critically examined herein."
- **Not always trivial** (l. 168, 195): in the polynomial example the inversion under the crime has roots besides the trivial one; in the mirror example it recovers the mirror and also other planes (non-unique solutions), so the crime can reveal ill-posedness.
- **The cost of avoiding it** (l. 234, 249): the relative error of the recovered parameter grows with the functional difference between the data-generating model and the inverting one ("the larger is the functional difference ... the larger is the relative error"), in a one-parameter toy.
- **"No connection"** (l. 262-263): with a data model unrelated to the inverting one, one can obtain reconstructions "that have 'no connection' to the actual" parameter.
- **Conclusion** (l. 264-265): whether the crime should always be avoided "is, negative".
- **Real data** (l. 309): the author sees no such risk with real data, "since the predictor for real data is unknown".

## What TRUTH-METHOD says of it

TRUTH-METHOD (The question): "Making synthetic data with the same model that inverts them is the *inverse crime* (Kaipio & Somersalo). It gives overconfident results. Avoiding it covers the discretisation and the noise model too, not only the equations." Its reference table pairs "Kaipio & Somersalo 2005/2007; Wirgin 2004" with "the inverse crime" (status snippet).

Verdict: **differs.**
- The paper does not support "overconfident results": the word is absent, and the term and its reason (triviality) are Colton and Kress's (l. 47-49).
- It criticises the rule (l. 20, 168, 264-265) and finds the opposite risk in a toy: the error of the recovered parameter grows as the two models differ (l. 249).
- Discretisation and noise models are not discussed.
- The overconfidence claim needs Kaipio and Somersalo 2007 (J. Comput. Appl. Math. 198:493-504, doi 10.1016/j.cam.2005.09.027), which could not be obtained.

## Dependence

- Colton and Kress, Inverse Acoustic and Electromagnetic Scattering Theory (1992, 1998), cited for the term and the rule. None shared in authors.

## Bearing (2026-10-27)

- **TRUTH-METHOD:** drop Wirgin as support for "overconfident", or cite it as the dissenting view that a very different truth loses accuracy (l. 249) and that the same-model test is a minimum check, not an error (l. 264-265). Keep Kaipio and Somersalo for the claim once read.
- **D45:** a model fitted on the truth's output committing the "crime" will recover the truth's parameters; Wirgin's point is that this check still has a use as a minimum test, not as evidence about real data.
- **Not shown:** a measure of over-confidence from the inverse crime, or anything beyond one-parameter toys.
