# Literature notes

One note per paper read for Formularium or for the tools that use it: what the paper
holds, how it was read, and what was concluded, dated. The notes outlive the question
that prompted them, so they are written for a reader working on another disease, crop or
region.

The repository is public. A note holds facts, numbers and short quotes, never the paper.
It says where a copy is held only as "held by Chris" or "open access", never a path;
`files` records only the names a copy was dropped under.

## A note's header

Each note starts with a header between two `---` lines, one `key: value` per line; lists
are written `[a, b]`. `tests/test_literature.py` checks it.

| Key | What it holds |
|---|---|
| `id` | the file's name without `.md`: `<first author's surname><year>` and, if needed, a word |
| `citation` | authors, year, title, journal, volume and pages, as read |
| `doi` | where one exists |
| `read` | when, how much, and by whom: "2026-10-08, in full", "sections 2.5 and 3.4", "by a reading agent, key figures checked" |
| `status` | how the note's facts were obtained: `read`, `trail` (from another record that says how it was read), `snippet` (a search summary or a tool's summary of a page) |
| `diseases`, `crops`, `regions`, `processes` | lists, for finding notes later |
| `records` | catalogue ids the paper supports (`catalogue.py`); each must exist |
| `datasets` | dataset ids it describes (`datasets.py`); each must exist |
| `files` | the names the paper was dropped under, so `scripts/coverage.py` can tell which papers in a drop have notes; never a path |

## A note's body

- **What it holds:** data (sites, years, cultivars, conditions, counts) and formulations
  (equations and values, with the table or page).
- **Dependence:** which other models it computes, which data it was fitted to, which
  models shaped its data, and whose authors it shares (Agrarium decisions D27 to D29).
- **Bearing:** what was concluded for Agrarium and Cooptera, with the date. Conclusions
  age; the facts above them should not.

Numbers garbled by text extraction are marked as such, never guessed.

## Index

| Note | Disease | Process | Region | Bearing, in a line |
|---|---|---|---|---|
| [brischetto2021](brischetto2021.md) | downy mildew | secondary infection | Italy | the engine's secondary infection; its Magarey parameters, read |
| [chen2019](chen2019.md) | downy mildew | season risk, regional data | Bordeaux | see the note |
| [fedele2025](fedele2025.md) | downy mildew | oospore dose | Italy | the truth's dose; calibrated with Rossi 2008's model |
| [franche2012](franche2012.md) | downy mildew | whole cycle in a DSS | France | mostly Rossi's chain; a few independent pieces |
| [jensen2025](jensen2025.md) | none | modelling review | global | Review of 146 models |
| [kang2025](kang2025.md) | none | image analysis | greenhouse | Off-topic |
| [kennelly2007php](kennelly2007php.md) | downy mildew | trigger, lesions, sporangia, fruit | New York | the engine's trigger and bunch window; field sporangia survival |
| [liu2026tarag](liu2026tarag.md) | none | decision support | China | Off-topic |
| [madden2024glmm](madden2024glmm.md) | none | statistics | general | A statistics tutorial |
| [magarey1991](magarey1991.md) | downy mildew | incubation and more | South Australia | incubation cubic fitted to Müller, Zachos and Rafaila |
| [magarey2005](magarey2005.md) | many | infection | general | the generic infection model; its grape rows' data |
| [magarey2007](magarey2007.md) | none | risk mapping | United States | Templates for Magarey's generic infection model, described without equations |
| [martre2014](martre2014.md) | none | crop growth | global | Off-topic, though its finding (an ensemble mean beats single models) is the argument… |
| [masson2011](masson2011.md) | none (climate models) | model dependence | global | why dependence is judged by components and behaviour |
| [mouafo2022](mouafo2022.md) | downy mildew | clade competition | Quebec | little for Europe |
| [peddicord2025](peddicord2025.md) | northern leaf blight, gray leaf spot | risk prediction | US Midwest | Uses a CART-style wetness tree (after Kim et al.) and RH >= 90% disease units |
| [peng2025](peng2025.md) | none | animal science | China | Off-topic |
| [pokovai2025](pokovai2025.md) | none | remote sensing | Hungary | Off-topic |
| [rafaila1968](rafaila1968.md) | downy mildew | incubation | Romania | an incubation independent of Goidanich's data |
| [roberts2017](roberts2017.md) | none | statistics | general | Block cross-validation for structured data |
| [rose2016](rose2016.md) | none | decision support | England and Wales | Why farmers use or ignore decision tools |
| [rossi2008](rossi2008.md) | downy mildew | primary infection, incubation | Italy | incubation eqs 8-9 from Rossi et al. 2002, after Goidanich |
| [rossi2013](rossi2013.md) | downy mildew | epidemic structure | Europe | Gobbin's genotype patterns, for history matching |
| [rotem1969](rotem1969.md) | many | irrigation | Israel | drip adds no leaf wetness; sprinkling does |
| [salinari2007](salinari2007.md) | downy mildew | season onset | Italy | a statistical onset model at one site |
| [steel2011](steel2011.md) | bunch rots | berry infection by temperature | New South Wales | two temperatures; points to Nair & Allen 1993 |
| [zachos1959](zachos1959.md) | downy mildew | incubation, oospores, conidia | Greece | an incubation independent of Goidanich's data |
| [zhang2025unet](zhang2025unet.md) | none | image analysis | China | Off-topic |
