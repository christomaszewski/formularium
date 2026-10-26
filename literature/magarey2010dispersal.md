---
id: magarey2010dispersal
citation: Magarey, P. A. & Wicks, T. J. 2010. Toward establishing low input regimes in Australian viticulture 2: observations on the spread of downy mildew from a single source. Proceedings of the 6th International Workshop on Grapevine Downy and Powdery Mildew, Bordeaux, 4-9 July 2010 (eds Calonnec et al.), pp. 103-105
doi:
read: 2026-10-10, in full in an OCR of the proceedings, figures and equations in the page images, by a reading agent (claude-haiku-5-5); 42 quotes checked by scripts/verify_quotes.py; 2026-10-25, re-read for primary inoculum and dispersal by a reading agent (claude-sonnet-5-5), every quote found at its line by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [South Australia]
processes: [dispersal, secondary infection]
records: []
datasets: [magarey2010dispersal.nuriootpa]
files: [gdpm2010_proceedings_6th_bordeaux.pdf]
---

# Magarey & Wicks 2010: downy mildew spreading from one source

## What it holds

- **Event:** vines inoculated at SARDI near Nuriootpa on 14 November 1989; oil spots on 23
  November; one secondary event, 3 mm of night rain at a minimum of 17 °C on 29 November,
  in an unsprayed vineyard.
- **Gradient downwind** (Table 2): over 70 % of leaves at 4 m, 43 % at 8 m, 12 % at 20 m,
  about 1 % at 20-34 m; 54 oil spots per leaf at the source, 7 per infected leaf at 4 m.
  One oil spot about 300 m away.
- **Multiplication:** about 4,500 oil spots gave 60,000-90,000 in the next generation.
- Figure 1's exponential trend line has no printed equation. No rule of thumb (10:10:24)
  is printed: not the source of the engine's `magarey2010.rules`.

## Dependence

- None. Magarey is an author of engine models: a flag.

## Bearing (2026-10-10)

- A measured one-source, one-event gradient: a check for the truth's dispersal kernel,
  which is assumed (`kernel.mixture`).

## Bearing (2026-10-25)

Re-read for the row direction (`dm.row_barrier`).
- **An across-row datum:** Row 1, about 3 m across the row from the source row, had incidence
  50, 50, 20, 40 and 5 % where the source row had 100, 80, 50, 25 and 15 %; the text says the
  vine 3 m across showed the incidence seen 8 m downwind and the severity seen 4 m downwind.
  So a metre across counts as about 2.7 m along by incidence and 1.3 m by severity
  (arithmetic, not printed). The wind ran along the rows, so across-row and crosswind are
  confounded; one event.
- **The line gradient:** the exposure −ln(1 − incidence) falls with an e-folding length of
  7-11 m along Rows 2-4 over 4-34 m (arithmetic). A line gradient from one source vine is the
  kernel integrated across the wind, not a kernel scale.
