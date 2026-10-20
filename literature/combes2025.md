---
id: combes2025
citation: Combes, M., Brown, N., Thompson, R. N., Mastin, A., Crow, P. & Parnell, S. 2025. Unlocking plant health survey data: an approach to quantify the sensitivity and specificity of visual inspections. PLOS Computational Biology 21(11):e1012957
doi: 10.1371/journal.pcbi.1012957
read: 2026-10-20, abstract, methods outline and the results' text, by the main session; the figures holding the per-surveyor values were not read
status: read
diseases: [acute oak decline]
crops: [oak]
regions: [United Kingdom]
processes: [visual inspection, detection sensitivity, specificity, survey design]
records: []
datasets: []
files: [combes_2025.pdf (the 2026-10-20 drop)]
---

# Combes et al. 2025: how often surveyors see what is there, measured

Twenty-three trained citizen-science surveyors scored up to 175 labelled oaks for three
symptoms of acute oak decline, against an expert who has followed the same trees for over
a decade; then Bayesian latent-class models estimate sensitivity and specificity without
such a reference.

## What it holds

- Sensitivity and specificity varied widely between symptoms and between surveyors
  (l. 443-444); sensitivity rose with how often a symptom appeared on a tree (l. 445-446),
  and the frequency effect differed by symptom (LR χ² 49.8, df 2) and the surveyor effect by
  symptom (LR χ² 106.6, df 44) (l. 446-448).
- Specificity exceeded sensitivity for 22 of 23 surveyors (l. 450): people miss more than
  they invent. Stem bleeds were the most reliable symptom; 3-5 mm beetle exit holes had high
  specificity and low sensitivity; bark cracks were near chance for many (l. 452-455).
- Without an expert reference, sensitivity and specificity could be estimated from two
  symptoms on as few as 80 trees at each of two sites of known higher (about 0.6) and lower
  (about 0.3) prevalence (l. 43; l. 458-460).

## Dependence

- Its own survey and an expert's long-term record; the latent-class method is the two-test,
  two-population design of its refs 34-35 (l. 256-263). No disease model.

## Bearing (2026-10-20)

- For Agrarium's scout operator (PLAN 7: per-leaf detection assumed 0.5-0.95, 'no one has
  measured how many young oil spots a scout misses'): the first measured form found for
  the question, on trees: detection rises with the number of symptoms present, misses
  outnumber false alarms, and both vary by observer and by how conspicuous the symptom is.
  A small young oil spot is in the exit-hole class (high specificity, low sensitivity),
  by analogy only. Not a vine study; per-surveyor values are in the figures, not read.
