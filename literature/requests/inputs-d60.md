# Request: models, measurements and sensors for filling real datasets' weather (Agrarium D60)

From Agrarium's session on `agents` (ckt), 2026-10-27, at Chris's word (D60, decided; "ok let's
proceed"). For an `ingest` session: papers stay with you (D40). Search worldwide, and search
downy mildew under its other names (Plasmopara viticola, Peronospora, Rebenperonospora,
mildiou, peronospora della vite, mildiu).

## Why

Real records of downy mildew rarely carry the weather a prediction model needs: MIRA (Cooptera's
main outcome set) has hourly temperature, humidity and rain only. Agrarium D60 fills the missing
inputs (leaf wetness, radiation, canopy microclimate) from each dataset's own weather with
several physical models per quantity, weighted by how well each fits measurements from matching
conditions, and fills only what sensors that exist or are being developed could provide.

## Three parts, each its own delivery

### 1. Models of the physical inputs, with validation

For each quantity: leaf wetness duration (beyond what Formularium holds: `magarey2006.sweb`,
Dhakar 2025, Kuwagata 2024, the RH >= 90 % stand-in), dew, net and longwave radiation and its
partition, cloud from station data, in-canopy temperature, humidity and wind against the
station's, rain interception and splash. For each model found:
- the equations and every parameter, as `literature/INGESTING.md` asks;
- what it was validated against: where, which canopy (and vines especially), sensor type,
  height and placement, the error reported;
- its inputs, so Agrarium can tell which datasets it can fill.

### 2. Measurements to weigh the models by

Open datasets with measured leaf wetness, radiation or in-canopy microclimate beside ordinary
station weather, vineyards first, any crop canopy next: site, years, step, sensors and their
placement, licence, where to get it. Colucci's dataset is held already (`colucci2026`).

### 3. What sensors provide, by tier

What a farm or an agricultural station network typically measures, and what exists or is being
developed: leaf-wetness sensors (types, how they differ from real leaves), radiation, wind,
in-canopy loggers, soil moisture, automated spore traps (volumetric, qPCR), canopy imagery
(drone, satellite LAI). For each: whether common, cheap and emerging, or research only; its
accuracy and placement; and the source of the claim (a network's station list, a review, a
maker's sheet). Agrarium tiers each variable by this (D60) and sources it as costs are.

## What to deliver

On a branch `ingest/inputs-d60`, following `literature/INGESTING.md`: formulations in
`catalogue.py`, datasets in `datasets.py` (as for D58), a note in `literature/` for each paper
read, and part 3 as a note (`literature/sensors-d60.md`) with its sources. Deliver part by part
if that is easier: part 1 for wetness first.
