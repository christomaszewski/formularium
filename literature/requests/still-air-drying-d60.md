# Request: how leaves dry in still air, and what a station's 0 m/s means (Agrarium D60, SW9)

From Agrarium's session on `agents` (ckt), 2026-10-28, at Chris's word ("Sure go for it").
For an `ingest` session: papers stay with you (D40).

## Why

SWEB (`magarey2006.sweb`) dries leaves through wind alone: its transfer coefficient is
h = c Uc^0.5 (Eq 13), zero in still air. Against Colucci's measured leaf wetness (Agrarium's
SW8 and SW9, docs/SWEB-REPORT.md), SWEB stayed wet 8-16 h a day too long at stations reading
0 m/s for 43-85 % of hours. A floor on the wind its drying sees, 0.5 m/s, halved the error.
The best floor in the table is 1.0 m/s, but taking it from the table would fit SWEB to seven
stations. Agrarium needs the floor from sources.

## What to read and settle

1. **Anemometers' starting speeds:** for the cup and sonic anemometers on agricultural
   stations (Davis, Campbell, Gill, Young and the like; Colucci's stations if their make is
   given), the speed below which they read 0, from makers' sheets or field tests. And how a
   station's hourly 0 m/s is reported: the mean of readings at or below the threshold, or
   still air.
2. **Free and mixed convection from leaves:** the heat or mass transfer coefficient of a leaf
   in still air (Nusselt numbers for free convection on flat plates and leaves, e.g. in
   Campbell & Norman, Monteith & Unsworth, Gates, Schuepp's review), and when it takes over
   from forced convection. In SWEB's units (cm/min) if possible, or the equations and values
   to get there.
3. **Wetness models that dry in still air:** any leaf-wetness model whose drying term does not
   vanish at zero wind, with its form and parameters.
4. **Measured wind inside vine canopies at low station wind,** if any: what the leaves feel
   when the station reads calm.

## What to deliver

On a branch `ingest/still-air-drying-d60`, following `literature/INGESTING.md`: notes in
`literature/`, any formulation in `catalogue.py`, and a short answer note
(`literature/requests/still-air-drying-d60-answer.md`) giving a sourced value or range for
the floor, or the free-convection coefficient, with how each was checked.
