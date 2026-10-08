---
id: zapata2015
citation: Zapata Rojas, Diana Maribel. 2015. Modelling the key phenological stages and dormancy of individual grapevine cultivars. MSc thesis, Washington State University
doi:
read: 2026-10-08, in full except reference lists and figures, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: [grapevine]
regions: [Washington]
processes: [phenology, dormancy]
records: []
datasets: []
files: [related-zapata-2015-thesis.pdf]
---

# Zapata 2015: phenological stages and dormancy of grapevine cultivars (thesis)

An MSc thesis at Washington State University, chaired by Gerrit Hoogenboom, with Melba Salazar-Gutierrez, Markus Keller and Claudio Stöckle on the committee.

## What it holds

- MSc thesis (Washington State University, May 2015), chair G. Hoogenboom, two parts (l. 1-30, 107-153).
- Part 1: stage-specific, cultivar-specific base temperature (Tb) and degree-day requirement for budbreak, bloom and veraison of 17 cultivars, field data 1990-2013 at Prosser, Washington (l. 742-754).
- Tb is the value that minimises the spread of DD across years (l. 846); means 7.2, 8.7 and 11.0 C with 116, 319, 633 DD (l. 115).
- Five parameter sets compared; best chain starts 1 January and uses stage-specific Tb (l. 857-871). Errors 3-14 d (budbreak), 1-6 d (bloom), 3-12 d (veraison) (l. 1071, 1089-1105).
- Part 2: forced-budbreak cuttings of Cabernet Sauvignon and Chardonnay, 25 C, 2013-2015 (l. 2353-2375). Endodormancy starts 10 Sep 2013 and 16 Sep 2014 and ends 22 Oct to 12 Nov (l. 2501, 3124-3128).
- Chill requirement from an exponential fit: Dynamic Model 26-79 CP (Cabernet Sauvignon) and 24-69 CP (Chardonnay) (l. 3169); authors judge Utah and Chilling Hours unsuitable (l. 2814).
- Thermal models are the Arnold degree-day and published chill models; the new part is the fitted Tb, DD and chill ranges.
- Same data and parameters as the 2016 project report and Zapata et al. 2017; count as one source.

## Dependence

- Field dates at Prosser (1990-2013); no model dated them. It computes Arnold's degree-days with stage-specific base temperatures (Yang et al.'s minimum-variance method) and four chilling models (the Dynamic, Utah, Weinberger and Bennett models).
- Hoogenboom and Keller (committee) are authors of the engine's Ferguson 2014 cold-hardiness model: flags. Ferguson's data are cold hardiness at Prosser, not these phenology dates.
- Degree-day sums and chilling: the engine's forms.

## Bearing (2026-10-08)

- **Held out by structure,** as before; its link to Ferguson's group is a flag now, not kinship. Its 17-cultivar base temperatures and degree-day requirements are the same as the 2016 project report ([salazargutierrez2016](salazargutierrez2016.md)).
