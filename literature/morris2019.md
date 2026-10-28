---
id: morris2019
citation: Morris, T.P., White, I.R. & Crowther, M.J. 2019. Using simulation studies to evaluate statistical methods. Statistics in Medicine 38(11):2074-2102
doi: 10.1002/sim.8086
read: 2026-10-27, lightly: abstract, introduction, section 2 (the review of practice), the ADEMP sections 3.1 to 3.5, parts of sections 4 and 5 (paired data, number of repetitions) and the discussion; the performance-measure formulas and the worked example not read. Read from Europe PMC's full-text XML (open access), converted to one paragraph per line, so line numbers are of that conversion. By a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [simulation study design, ADEMP, Monte Carlo error, data-generating mechanism, review of practice, pre-registration]
records: []
datasets: []
files: [syn1027_morris2019.xml (Europe PMC full text, the 2026-10-27 drop)]
---

# Morris et al. 2019: a tutorial on planning and reporting simulation studies (ADEMP), with a count of how they are done

Sets out what a simulation study of statistical methods should state, as five parts (Aims, Data-generating mechanisms, Estimands, Methods, Performance measures: ADEMP), after reviewing 100 randomly chosen studies from one volume of one journal. No record: a method and a measured review of practice.

**Read this first.** The subject is evaluating statistical methods (estimators, tests), not simulators of biology or engines. ADEMP is a reporting structure, not evidence on when synthetic truths mislead. The counts are for one volume of one journal (Statistics in Medicine, volume 34, 2015) and the XML conversion's lines are cited, not a page layout.

## What it holds

- **Premise** (l. 9): "While widely used, simulation studies are often poorly designed, analyzed, and reported." Their strength is that "some 'truth' ... is known", so properties such as bias can be measured.
- **The review** (l. 71): 100 randomly selected simulation studies from Statistics in Medicine volume 34 (2015), split among three reviewers with a cross-check.
- **Where the parameters came from** (l. 116): 97 of 100 simulated from a parametric model; of those 97, 27 based parameter values on data, one partly on data, and "the remaining 69 on no data".
- **What was targeted** (l. 142): 64 targeted an estimand, 21 a null hypothesis, eight a selected model, three predictive performance and four something else; of the 64, 51 stated the estimand.
- **Monte Carlo error** (l. 248, 295): 93 of 100 "did not mention Monte Carlo SEs"; of 87 reporting the number of repetitions, four gave any justification.
- **Design guidance** (l. 104-105, 114): the data-generating mechanism may be simple, realistic, or deliberately unrealistic to stretch a method to breaking point; results are specific to the scenarios simulated, so use more than one mechanism; a listed pitfall is "failing to distinguish between what the simulator can know and what the estimator can know".
- **Paired comparison** (l. 223): use the same simulated data for every method so Monte Carlo error affects methods alike.
- **Protocols** (l. 403, 410): the two main shortcomings are unclear design and no Monte Carlo uncertainty; write detailed protocols before the code, with the weak point that protocols "could be written after-the-fact".
- **ADEMP** (l. 9): defining "aims, data-generating mechanisms, estimands, methods, and performance measures".

## What TRUTH-METHOD says of it

TRUTH-METHOD part 6: "Simulation studies are often poorly designed and reported. Morris, White & Crowther (2019) set out what each should state: Aims, Data-generating mechanisms, Estimands, Methods and Performance measures (ADEMP), with Monte Carlo standard errors." Table: "ADEMP" (status snippet).

Verdict: **confirmed, and the paper backs the first sentence with counts.** The abstract sentence is at l. 9; the ADEMP expansion matches (l. 9); 69 of 97 parametric studies used parameters from no data (l. 116), 93 of 100 omitted Monte Carlo standard errors (l. 248), and 4 of 87 justified their repetitions (l. 295). It also supports paired comparison (l. 223) and protocols before code (l. 410), and names the weakness that TRUTH-METHOD's committed-before-runs rule answers.

## Dependence

- None recorded; the review's data are in the journal's supplementary file (not downloaded). Earlier review: Burton et al. 2006 (cited, not obtained).

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 6:** safe to cite for ADEMP and for the poor state of practice. Agrarium's training experiments should state each of the five parts and report Monte Carlo standard errors.
- **D58, D60:** a synthetic outcome has a known truth by construction (l. 9), which is its strength and its limit; 69 of 97 studies took parameters from no data (l. 116), the practice that makes a synthetic result a statement about the simulator.
- **Not shown:** that following ADEMP prevents a misleading synthetic truth.
