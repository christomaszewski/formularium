# Request: SWEB's canopy wind, Eq 15 against Fig. 1C (Agrarium D56)

From Agrarium's session on `agents` (ckt), 2026-10-27, at Chris's word ("ok let's proceed", D56
as recommended). For an `ingest` session: this is a paper, and D40 keeps it with you.

## Why

`magarey2006.sweb` (Magarey, Russo & Seem 2006, Agric. For. Meteorol. 139:373-381) is the first
wetness model Agrarium builds into the truth and the first filler of missing wetness in real
datasets (Agrarium D60). It needs the wind inside the canopy from the wind above, Eq 15, which
does not close as printed. Agrarium's arithmetic (its `research_notes/deep-research-10-25/
canopy-flow.md`, not the paper): reading `(1 − Zc)/Z` as `1 − Zc/Z` gives 0.324 U_Z at Zc 150 cm
and Z 200 cm, the value that reproduces Fig. 1A-1B by trial; but it varies about 22 times from
Zc 10 to 200 cm, where Fig. 1C appears to vary about 3 times. Eq 15's source, Landsberg & James
1971, was not obtained.

## What to read and settle

1. **Eq 15 as printed**, every symbol and unit, in the page image (p. 375-377), and what the
   text says Zc, Z and U_Z are (canopy height, measurement height, wind at Z).
2. **Fig. 1C**: its axes, units and the heights it uses (Zc, and Z if stated), and the curve's
   values read off at as many points as the figure allows, with how they were read.
3. **Whether `1 − Zc/Z` reproduces Fig. 1C** at Fig. 1C's own heights, within reading error.
   If not, whether any other reading of Eq 15 does, and whether the text says.
4. **Landsberg & James 1971** (if it can be had: Journal of Applied Ecology 8:729-741, "Wind
   profiles in plant canopies: studies on an analytical model"): the equation Eq 15 takes, as
   printed there.

## What to deliver

On a branch `ingest/sweb-canopy-wind-d56`, following `literature/INGESTING.md`: the findings as
a flag on `magarey2006.sweb` in `catalogue.py` (the reading, marked a reading, not a print), and
the note in `literature/` updated. If no reading reproduces Fig. 1C, say so: Agrarium then takes
canopy wind as 0.35-0.5 of the wind above from three vineyards' measurements, registered
`estimate` (D56).
