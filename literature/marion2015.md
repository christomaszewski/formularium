---
id: marion2015
citation: Marion, B. 2015 (year from the DOI; no year or journal printed in the text). A model for deriving the direct normal and diffuse horizontal irradiance from the global tilted irradiance. Solar Energy (from the DOI), volume and pages not printed
doi: 10.1016/j.solener.2015.10.024
read: 2026-10-18, first pages and the located results, by a triage agent and a note writer (claude-haiku-5-5, claude-sonnet-5-5); not read in full; an author manuscript (a DOE accepted manuscript, l. 58-59), with no year, journal, volume or pages printed
status: read
diseases: []
crops: []
regions: [Cocoa Florida, Eugene Oregon, Golden Colorado]
processes: [irradiance separation, tilted irradiance, DNI, DHI]
records: []
datasets: []
files: [r_10_1016_j_solener_2015_10_024.pdf (the 2026-10-18 drop)]
---

# Marion 2015: GTI-DIRINT, direct and diffuse irradiance from tilted-plane measurements

DIRINT is changed to take global tilted irradiance (GTI) instead of horizontal, and iterated until a Perez-transposed GTI matches the measurement (l. 12-15, 106-108).

## What it holds

- **Method:** clearness index from GTI divided by I0 times the cosine of the incidence angle (Eq. 2, l. 93); DHI from Eq. 3 (l. 101); iteration with a relaxation coefficient (Eq. 4, l. 114-123); stop when the GTI difference is at most 1 W/m2 or after 30 iterations (l. 127); a different branch for incidence angle of 90 degrees or more (l. 143-147).
- **Iterations:** at Eugene, 44 degree tilt, hourly, about 50 % of cases needed 3 iterations and about 10 % hit the limit of 30, with a mean absolute difference of 2.9 W/m2 (l. 129-134).
- **Result:** at a 10 degree tilt the deviations equal those of DIRINT on GHI; larger tilts, up to 44 degrees at Eugene, raise them but stay reasonable (l. 16-19). Sites: Cocoa, Eugene and Golden (l. 66).
- **Not in the first 150 lines:** the RMSD and bias tables.

## Dependence

- Modifies DIRINT (Perez et al. 1992), which improves DISC (Maxwell 1987); uses the Perez et al. 1990 tilted-surface model (l. 62-75, 108-109).

## Bearing (2026-10-18)

- Strand s3 (slope-facing radiation) and s5 (sensor input): a simulator with a tilted-plane pyranometer on a slope could recover direct and diffuse parts with it; code is not given in the first pages.
- Not read in full.
