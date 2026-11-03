---
id: lalancette1987
citation: Lalancette, N., Ellis, M. A. & Madden, L. V. 1987. Estimating infection efficiency of Plasmopara viticola on grape. Plant Disease 71:981-983
doi: 10.1094/PD-71-0981
read: 2026-11-03, abstract only (APS's abstract page; the full text was refused), by a reading agent (claude-sonnet-5-5) and the main session; 3 of 3 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine, Vitis labrusca]
regions: [Ohio]
processes: [infection efficiency, zoospores per sporangium, inoculum retention]
records: []
datasets: []
files: [dr1103_lalancette1987.html (the 2026-11-03 drop)]
---

# Lalancette, Ellis & Madden 1987: zoospores per sporangium and infection efficiency

The groundwork for `lalancette1988infection`: how many sporangia a leaf holds, how many
zoospores they release, and what share infect.

**Read this first.** Abstract only. The per-temperature zoospore counts and the method are in
the full text, which APS refused this VM.

## What it holds

- **Method (abstract, l. 70):** a relation between leaf area and the inoculum volume a leaf
  retains without runoff gives the sporangia applied; zoospore release from sporangial
  suspensions was counted in vitro at several temperatures; potted Catawba vines (V. labrusca)
  were inoculated at several concentrations.
- **Zoospores (l. 70):** "an average of seven zoospores per sporangium" at incubation
  temperatures of 5-25 °C (the dash garbled in the text layer).
- **Infection efficiency (l. 70):** about 6 % for each inoculum concentration, though severity
  rose with concentration.

## Dependence

- Its own counts and inoculations; no model shaped the data. The 1988 model
  (`lalancette1988infection`) builds on it.

## Bearing (2026-11-03)

- **Agrarium F3:** `f3.zoospores_per_sporangium` (6, guessed): seven on average is the measured
  value; 6-7 is well supported, with `keil2007`'s nucleus counts (4.3 at 15 °C, 5.9 at 27.5 °C).
- **Unit of the 6 %:** reckoned from the zoospores applied, so per zoospore, as the 2026-10-22
  pass flagged for the 1988 model; a per-sporangium efficiency would be about seven times larger.
  The abstract does not print the unit: the full text would settle it.
