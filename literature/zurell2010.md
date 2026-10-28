---
id: zurell2010
citation: Zurell, D., Berger, U., Cabral, J.S., Jeltsch, F., Meynard, C.N., Münkemüller, T., Nehrbass, N., Pagel, J., Reineking, B., Schröder, B. & Grimm, V. 2010. The virtual ecologist approach: simulating data and observers. Oikos 119:622-635
doi: 10.1111/j.1600-0706.2009.18284.x
read: 2026-10-27, lightly: abstract, introduction, the approach (section 2.3), past uses in species distribution modelling and the discussion of limitations. Read as chapter 2 of Zurell's 2011 PhD thesis (University of Potsdam), which says an article with equivalent content was published as the Oikos paper; the Oikos PDF was not obtained, so wording may differ, and the line numbers below are those of the thesis text. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 17 of 17 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [virtual ecologist, virtual species, synthetic data, observer model, species distribution model, model comparison, sampling design]
records: []
datasets: []
files: [syn1027_zurell2010.pdf (the 2026-10-27 drop; Zurell's thesis chapter 2)]
---

# Zurell et al. 2010: the virtual ecologist, a simulated truth and a simulated observer to test methods

A review of the "virtual ecologist" approach: simulate a species or ecosystem (the truth), simulate how an observer samples it, analyse the sample, and score the result against the known truth. No record: a review of method.

**Read this first.** Read as the thesis chapter that carries "equivalent content", not the published Oikos article; wording may differ slightly and line numbers are the thesis's. The authors include Meynard and Grimm, whose other papers are `meynard2013`, `meynard2019` and `grimm2005`.

## What it holds

- **Definition** (l. 992, 994): the "virtual ecologist" approach uses "simulated data and observer models" to mimic real species and how they are observed; the virtual data are analysed and "the results are evaluated against the 'true' simulated data".
- **Core claim** (l. 1028): "The virtue of this approach is its ability to rigorously test method performance against a known truth."
- **Two uses** (l. 1108): testing and improving sampling schemes and methods, and testing and comparing models.
- **Four elements** (l. 1130): a virtual ecological model of the species or ecosystem including the key processes relevant to the question, a virtual sampling model, statistical modelling, and evaluation.
- **Model comparisons by VE** (l. 1319, 1328): several studies tested alternative modelling algorithms; most virtual species were made from simple descriptive models and only a few from mechanistic ones.
- **A generator setting moves the result** (l. 1364, cited from Zurell et al. 2009): projection skill under climate change depends strongly on the virtual species' dispersal ability and extinction rate.
- **Ranking can depend on the virtual species** (l. 1545, cited from Berger et al. 1999): deviations from the movement behaviour built into the virtual species "might lead to a different ranking of the observation errors". The only statement on ranking sensitivity in this chapter.
- **Limits** (l. 1538, 1542): the benefit "depends on the quality of the ecological model" and ignores complexity it does not cover; sample sizes found in a virtual world are "only lower bounds" (cited from Wunder et al. 2008).
- **Asymmetry** (l. 1547-1550): "Generally, VE is better at discrediting methods than at corroborating them." A failure in the virtual world probably fails in the real one, unless deficits cancel the virtual world's biases; success "does not guarantee" real-world success.
- **Same-model VE** (l. 1557, 1559): the approach "may seem a bit circular" (Hirzel et al. 2001 sampled from the type of model they tested), but "even if one samples from the same (statistical) model, running VE is worthwhile", as a minimum test.
- **Design rule** (l. 1584): when the question concerns process dynamics, a more mechanistic virtual ecosystem is needed.

## What TRUTH-METHOD says of it

TRUTH-METHOD (The question): "The *virtual ecologist* simulates the truth and the observer, then tests sampling designs against the truth (Zurell et al. 2010)." Table: "the virtual ecologist" (status snippet).

Verdict: **confirmed, with additions** (read as a thesis chapter).
- Truth plus observer plus scoring against the truth: l. 992-994, 1130.
- Sampling designs **and** model comparison (l. 1108), not designs alone.
- Two limits TRUTH-METHOD does not cite: VE is better at discrediting than corroborating (l. 1547-1550), and same-model VE is defended as a minimum test (l. 1559).
- It does **not** say that the way the virtual species is generated decides which method wins; that is Meynard and Kaplan's claim (`meynard2013`, abstract only), with only a hint here (l. 1364, 1545).

## Dependence

- Reviews others (Hirzel et al. 2001, Zurell et al. 2009, Berger et al. 1999, Wunder et al. 2008, none read). Shared authors with `meynard2013`/`meynard2019` (Meynard) and `grimm2005` (Grimm, Berger, Jeltsch): flags.

## Bearing (2026-10-27)

- **TRUTH-METHOD:** safe to cite for the virtual-ecologist structure; add that VE discredits better than it corroborates. This is the stance for D58 and D60: a simulator can show that a variable or method fails, not that it is real; synthetic outcomes test robustness and never establish a feature.
- **D45:** a same-model check is a minimum test (l. 1559), not evidence on real data; a model fitted on the truth passing it says only that it can recover the truth's own form.
- **Not shown:** the size of any generator effect on a ranking, or a plant-disease use.
