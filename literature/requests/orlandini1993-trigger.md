# Request: what Orlandini et al. 1993 mean by "once minimum temperature stays above 10 °C"

From Agrarium's session on `agents` (ckt), 2026-10-27, at Chris's word ("write the ingest
request"). For an `ingest` session: it needs the paper, and D40 keeps it with you.

## Why it matters

Agrarium's family F3 (PLAN 15, D59) starts its primary infections with Orlandini et al. 1993's
trigger, record `orlandini1993.trigger` (Vitis 32, p. 620): ">= 8 mm within any 24-h period",
"once the minimum temperature stays above 10 °C", shoots 100 mm long. Agrarium read the
temperature clause as **the air above 10 °C through the same 24 h in which the rain fell**. With
that reading F3 fails one of its anchors (W2, bunches infected before flowering after a wet
April, as at Gelida in 2020): April's cold rain spells trigger almost nothing. Another reading
is **a season's start**: once the nights have stayed above 10 °C, any 8 mm in 24 h triggers.
Which the paper means changes F3, so Agrarium will not choose without the text.

## What to read and settle

From the page image of p. 620 and the pages around it (Materials and methods, the description of
PLASMO's primary infection), and from Goidanich 1959 if the paper credits the rule to him and you
can reach it:
1. **The temperature clause.** Its exact words, and which of these it is, or another:
   - (a) the minimum over the 24 h of the rain is above 10 °C;
   - (b) a seasonal start: from the first day, or the first run of days (how many?), whose
     minimum stays above 10 °C, every later 8 mm in 24 h triggers;
   - (c) the minimum of the day of the rain, or of some other window.
   Whether it is daily minima, hourly temperatures, or the mean.
2. **The rain clause.** "Any 24-h period" (a running window) or a calendar day; whether one rain
   event can trigger more than once.
3. **The shoot clause.** 100 mm: how the paper measures or estimates it (observed, or a heat
   sum), if it says.
4. **What ends the primary season** in PLASMO, if the paper says (oospores exhausted, a date).
5. **Where the rule comes from.** The record says it is credited to Goidanich 1959. If the paper
   shows it is the 3-10 rule (10 °C, 10 cm shoots, 10 mm of rain; Baldacci 1947) or borrows from
   it, say so: the engine runs `rule_3_10`, so the record would need `borrows`.

## What to deliver

On a branch `ingest/orlandini1993-trigger`, following `literature/INGESTING.md`:
- the record's `flags` gaining each answer, with its page and the quotation, and how it was read;
- any parameter the answers add (a run of days, say) as a `Published` value with where it is
  printed;
- `borrows` or a flag if the rule is the 3-10 rule's;
- a note in `literature/` for what was read.

No code is needed. Agrarium changes its trigger itself, with a check written first.
