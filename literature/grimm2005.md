---
id: grimm2005
citation: Grimm, V., Revilla, E., Berger, U., Jeltsch, F., Mooij, W.M., Railsback, S.F., Thulke, H.-H., Weiner, J., Wiegand, T. & DeAngelis, D.L. 2005. Pattern-oriented modeling of agent-based complex systems: lessons from ecology. Science 310:987-991
doi: 10.1126/science.1116681
read: 2026-10-27, lightly: the motivation, patterns for model structure (the Medawar zone), for contrasting alternative theories and for parameters; a six-page reprint in a three-column layout, read in reading order, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 16 of 16 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [pattern-oriented modelling, agent-based model, model structure, parameter uncertainty, model selection]
records: []
datasets: []
files: [syn1027_grimm2005.pdf (the 2026-10-27 drop)]
---

# Grimm et al. 2005: pattern-oriented modelling, several observed patterns at several scales to fix a model's structure and parameters

A review of ecological agent-based models, arguing that matching several patterns seen in real systems, at different scales, is how to choose a model's structure and fix its parameters. No record: a method, argued with examples.

**Read this first.** The support is argument and worked examples (beech forest, rabies, fish schooling, coyote, trout, Anasazi), not a measured comparison: the paper gives no figure for how much a second pattern narrows parameter uncertainty. The reprint prints "Volker Grimm et al." on its cover; the full author list is from the article's first page. Some quotes are single-column fragments.

## What it holds

- **The premise** (l. 102-104): for complex systems "a single pattern observed at a" specific scale and hierarchical level is not sufficient "to reduce uncertainty in model" structure and parameters.
- **The remedy** (l. 118-120): in pattern-oriented modelling multiple patterns observed in real systems "at different hierarchical levels and scales" are used systematically "to optimize model complexity" and to reduce uncertainty.
- **The payoff argument** (l. 160-164): a model's payoff depends on its usefulness and its "structural realism", the ability to make independent predictions that match observations; designed for one pattern a model is too simple, driven by all available data too complex. An argument by diagram (Fig. 1), not measured.
- **A claim, not a result** (l. 170-173): guided by multiple patterns at different scales, a model is likely to end "up in the Medawar zone" of intermediate complexity.
- **Gap in practice** (l. 160): the authors found few agent-based models in other disciplines "explicitly addressing multiple pat-" terns.
- **Fish schooling** (l. 250): one pattern (nearest-neighbour distance) could not separate nine theories; a second (polarisation) falsified several. The value of the second pattern is shown by example only.
- **Coyote model** (l. 258): an individual-based model reproduced an array of patterns with "no fine-tuning of parameter values" taken from the literature.
- **Anasazi model** (l. 367-368): parameters fitted to patterns, then tested on independent predictions, "strong indicators of" the model's structural realism.

## What TRUTH-METHOD says of it

TRUTH-METHOD part 2: "A model fitted to one pattern at one scale is barely constrained; several patterns at different scales constrain both its structure and its parameters (pattern-oriented modelling, Grimm et al. 2005)." Status snippet.

Verdict: **confirmed, by argument and examples, with no measured gain.** The first half is the paper's own wording (l. 102-104); the second half is its definition of the method (l. 118-120). "Barely constrained" is TRUTH-METHOD's phrase. The idea that a structure is tested by independent predictions of held-out patterns (l. 160, 367-368) echoes part 7's real-world checks.

## Dependence

- Reviews the authors' own earlier models (several of the ten authors wrote the examples). Applies to ecology; no equation is borrowed.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 2:** safe to cite for the idea; do not cite it for any size of effect. Several patterns constrain a family better than one is argued, not measured here.
- **D58:** supports judging a candidate model on more than one real pattern, and on patterns not used to fit it (l. 367-368), before it is believed.
- **Not shown:** a gain from a second pattern in any number, or any use with plant disease or with training on synthetic data.
