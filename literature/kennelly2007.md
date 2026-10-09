---
id: kennelly2007
citation: Kennelly, M. M., Gadoury, D. M., Wilcox, W. F., Magarey, P. A. & Seem, R. C. 2007. Primary infection, lesion productivity, and survival of sporangia in the grapevine downy mildew pathogen Plasmopara viticola. Phytopathology 97(4):512-522
doi: 10.1094/PHYTO-97-4-0512
read: 2026-10-09, by the main session, the survival, lesion-productivity, heat and soil-trial sections in full (an Internet Archive capture of the publisher's PDF, 11 pages); the trigger section skimmed
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [New York, South Australia]
processes: [sporangia survival, sporulation, oospores, primary infection]
records: [kennelly2007.trigger, kennelly2007.lesion_decline]
datasets: [kennelly2007.loxton]
files: []
---

# Kennelly et al. 2007: primary infection, lesion productivity and sporangia survival

The paper behind the engine's primary trigger, and behind the field survival that
[kennelly2007php](kennelly2007php.md) summarises. Fieldwork at Geneva, New York, and Loxton,
South Australia.

## What it holds

- **The trigger:** rain > 2.5 mm, temperature > 11 °C, past E-L stage 12, credited to
  Gadoury. It is the engine's `kennelly2007.trigger`. Shoots were susceptible from E-L
  stage 5.
- **Sporangia survival in the canopy** (Loxton, Chardonnay, November-December 2003):
  - **Method:**
    - Shoots on field vines, and potted vines set inside the field canopy, were made to
      sporulate overnight in wet bags.
    - Leaf discs were sampled at 1-4 h intervals from sunrise.
    - Sporangia were rehydrated for 15-30 min and scored by germination (empty sporangia)
      within 4 h at 21 °C, at least 100 per disc.
    - The sporangia were **attached**, still on the lesions.
  - **Clear, warm, dry days** (5 days, average high 30.6 °C, SE 1.2; average RH 24 %,
    SE 1.9): viability "decreased significantly in the first few hours after sunrise, and
    no sporangia were viable after 6 to 8 h of exposure" (Fig. 6).
  - **Cooler, more humid weather** (average high 24.4 °C, SE 5.2; RH 86.6 %, SE 6.2):
    viability "decreased only modestly during the 8-h exposure" (Fig. 7).
  - **DMCast's survival model,** from Blaeser & Weltzien's laboratory study, "tended to
    overpredict spore viability" on both kinds of day. Observed = -1.46 + 0.764 ×
    predicted germination (%), R² 0.73 (eq. 3).
  - Motile zoospores lasted up to 7 h after all sporangia had germinated.
- **Lesion productivity** (Loxton): ln(relative sporulation % + 1) = 4.757 - 0.496 × the
  event's number, R² 0.77 (eq. 1). Lesion age alone did not reduce yield; an eighth
  sporulation gave under a fifth of a first's sporangia per mm².
- **Heat:**
  - On 15 November 2003 Loxton reached 42.8 °C, averaging 36.9 °C from 08:00 to 20:00
    with 4 h above 40 °C.
  - Visible lesions that had not yet sporulated lost the capacity: over 100 leaves gave
    zero or trace sporangia for 25 days.
  - Leaves still incubating were not affected in the same way.
- **Oospore infections all season** (Geneva; Table 3):
  - **Method:** trap seedlings over vineyard soil, removed after each rain.
  - **2004:** infections from 21-24 May to 30 September-6 October, up to 88.8 % of
    seedlings (8-15 September).
  - **2005:** the same pattern in new soil.
  - **Carry-over:** soil collected in 2004 still infected seedlings through 2005.

## Dependence

- **The engine's model:** the trigger is `kennelly2007.trigger`.
- **Independent of the engine:** the survival, productivity and heat data. P. A. Magarey
  (the fact sheet's author) is a co-author, a flag.
- **The survival result tests the Blaeser & Weltzien lineage** that DMCast, Brischetto 2020
  and the truth's F1 use.

## Bearing (2026-10-09)

- **D30's field check,** read at the source, and corrected:
  - Kennelly's sporangia were attached, on lesions; Zachos's were detached.
  - Brischetto 2020's attached equation (eq. 1, 9.27 - 1.12x + 0.04x²) never gives a
    lifetime under about 34 h (x = 14), and the detached one (eq. 2) never under 2.9 days.
  - Neither can produce "none viable after 6 to 8 h". Both fail.
- **A candidate sporulation formulation:** `kennelly2007.lesion_decline` (each sporulation
  yields less), for a truth whose lesions now sporulate for a fixed number of days
  (Agrarium's `dm.sporulating_days`, assumed).
- **Oospores germinate from May to October and survive more than a season in soil,**
  agreeing with Gobbin and Koopman.
