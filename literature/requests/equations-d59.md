# Request: two equation modules for Agrarium's F3 (D59)

From Agrarium's session on `agents` (ckt), 2026-10-26, at Chris's word ("send the ingest
request"). For an `ingest` session: it needs the papers, and D40 keeps them with you.

Agrarium is building F3, a development family of the truth whose downy mildew shares nothing
with Rossi's lineage (Agrarium PLAN 15, D59). Two of its records cannot be built from what
Formularium holds. Please add both as equation modules, following `literature/INGESTING.md`
and the steps in CLAUDE.md ("Adding a formulation"), on a branch `ingest/equations-d59`.

## 1. `lalancette1988.infection`: equation 5

Lalancette, Ellis & Madden 1988, Phytopathology 78:794-800, eq. 5: infection efficiency
(lesions per zoospore) by temperature and wetness duration. The record holds the eight
parameters (k.b0, k.b1, k.b2, k.offset, rho.b1, rho.b2, rho.b3, m; W is wet hours minus 1)
but not the equation itself.

- Add `equations/lalancette1988.py` with `FORMULATION = "lalancette1988.infection"`: eq. 5 as
  a pure numpy function of temperature (°C) and wetness duration (h), every parameter an
  argument, no defaults.
- Read the equation from the page image, not from text extraction and not from a later copy:
  the record's flags list Brazilian copies that differ from eq. 5 (Hamada 2008, Reis 2013,
  Monteiro 2012 and 2015, Embrapa's Boletim 38, Rodrigues 2019, Alves 2015).
- Test it against numbers the paper prints (a table, or values stated in the text or read
  from a figure, with which), and say where each came from. If none can be checked, mark the
  test `xfail(strict=True)` with what is missing.
- The paper's range is 5-30 °C, on *V. labrusca* 'Catawba' in chambers: keep that in the
  record's flags.

## 2. `tranmanhsung1990.pom`: the rain index IJ

Tran Manh Sung, Strizyk & Clerjeau 1990, Plant Disease 74:120-124. The record holds
T = a·IJ + b (a = -0.21, b = 117.9) and the severity line, but not how IJ is computed: rain
counted between limits set from climatic normals (42-year), accumulated by month since
21 September, and January's index mapped to the date.

- Add `equations/tranmanhsung1990.py` with `FORMULATION = "tranmanhsung1990.pom"`: IJ from
  daily (or monthly) rain and the normals' limits, all as arguments, and the date from IJ.
- Put the normals and limits the paper prints in the record as `Published` values, with
  where each is printed. Ronzon 1987 (the thesis, `literature/ronzon1987`) may print them
  more fully; say which source each value comes from.
- Test against the paper's own years: printed IJ values and maturity dates, if any.
- Its structure tag becomes `rain-index-oospore-date` once formularium#49 (branch
  `d32-pom-tag`, Agrarium D32, decided 2026-10-26) merges; leave the tag to that PR.

## Not asked

Anything about which nights sporulate, the dose, or the oospores: Chris decided those in
D59 (made-up rules in Agrarium, and no oospore model in F3 for now).

When the branch is pushed, Chris or his other sessions open the pull request. Agrarium builds
F3's other pieces meanwhile and registers the family once eq. 5 is merged and pinned.
