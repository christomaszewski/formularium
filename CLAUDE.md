# Formularium

Published crop and disease model formulations, their kinship graph and their tests,
shared by Agrarium and Cooptera. Created 2026-10-07 (Agrarium PLAN 15, decisions D22 to
D24). `main` is the default branch; work reaches it by pull request, merged with a merge
commit, never a squash or rebase: both tools pin commits by id.

## What belongs here, and what does not

- **Here: what was published, and how each fact was checked.**
  - A formulation's source, DOI, authors, borrowed equations, structure and flags.
  - Its published parameter values, with units and where the source prints them.
  - Its equations, as pure numpy functions.
  - Tests against the source's own numbers.
- **Not here: what a tool chooses.**
  - Which formulations a tool runs.
  - The ranges a tool draws parameters from, assumed or widened. Agrarium keeps those in
    its parameter registry.
  - How a tool uses an equation: Agrarium's per-vine population process, Cooptera's
    episodes and policy.
- **The repository is public** (D25, 2026-10-07; MIT licence). Nothing goes in that could not
  be shown to anyone.
- **Never here:**
  - **PDFs.** They are copyrighted. A record says where a paper is held.
  - **Weather data**, Meteocat's above all: tests use the source's own numbers.
  - **The sealed evaluation family's spec.** Agrarium commits only its salted hash.

## Rules

- **Ids never change once used.**
  - A new published formulation is `<first author's surname><year>.<what it computes>`,
    ASCII, lower case: `lalancette1988.infection`.
  - One made by a tool is `<tool>.<what>`.
  - Older ids that predate the scheme stay as they are.
- **Equations take parameters as arguments, never defaults.** Each tool passes its own.
  - Pure functions of arrays: no I/O, numpy only.
  - Vectorised, since Agrarium calls them for tens of thousands of vines per step.
- **A change to an existing equation's numbers is a change to both tools.** Say so in the
  commit, and expect both tools' pins to move only after their own checks pass:
  - Agrarium's M1 reference test and rerun check;
  - Cooptera's MIRA and Gelida scores.
- **Every claim says how it was checked:** `read`, `trail`, `snippet`, `memory`
  (records.AUTHOR_SOURCES).
  - A search summary is never `read`.
  - An author list read in a citing paper's references is `read`, and the source says
    where.
  - When a check contradicts a record, fix the record.
- **Kinship leans to linking** (people.py). Wrongly linking only holds out too much;
  wrongly separating lets a lineage be scored against itself.
- **Adding a formulation:**
  1. Write its record in `catalogue.py`, with the source, the authors and how they were
     checked.
  2. If it has equations, add `equations/<module>.py` naming it in `FORMULATION`.
  3. Test the equations against numbers the source prints. If the source is not yet
     read, mark that test `xfail(strict=True)` with what is missing, so filling it in
     forces the marker off.
  4. Run `stemma.kin` against each tool's list and say in the PR what it is kin to.

## How we work

The habits of Agrarium's CLAUDE.md apply here:
- checks before code;
- decisions are Chris's, recommended once, recorded when decided;
- plain, short sentences; numbers with units; ISO dates.

## Commands

```sh
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
```

Python 3.12, uv, ruff (line length 100), pytest. Tests are offline.
