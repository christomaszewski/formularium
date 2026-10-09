---
id: metos2026
citation: METOS by Pessl Instruments. Disease models: grapevine (FieldClimate). Web page, https://metos.global/en/disease-models-grapevine/, as served on 2026-10-09
doi:
read: 2026-10-09, the whole page, in its raw text (curl, tags stripped), by the main session
status: read
diseases: [downy mildew, powdery mildew, black rot, grey mould, anthracnose, phomopsis, grape berry moth]
crops: [grapevine]
regions: [general]
processes: [primary infection, sporulation, infection, ascospore release, risk index, degree days, decision support]
records: []
datasets: []
files: []
---

# METOS (Pessl Instruments): FieldClimate's grapevine models

A vendor's description of the models behind iMETOS stations' alarms. It gives rules, not
equations, and cites reviews rather than the papers the rules were fitted to.

## What it holds

- **Downy mildew, primary infection:**
  - "as long as the leaves are wet, or the relative humidity after the rain does not fall
    below 70%";
  - "Sporangia can develop within 16 to 24 hours depending on the temperature";
  - "A continuous rain of 5 mm is interpreted as a strong rainfall that can spread
    zoospores".
- **Downy mildew, secondary infection (sporulation):**
  - "warmer than 12 °C and relative humidity is over 95%"; production rises "with
    temperatures up to 23 °C";
  - finished at "an accumulated hourly temperature of more than 50 °C ... 4 hours with
    13 °C or 3 hours with 17 °C";
  - reset to 0 "when relative humidity falls below 50%"; above 29 °C "no sporulation can
    take place".
  - The infection step itself is shown as weak, moderate and severe curves reaching 100 %;
    its rule is not given.
  - Literature: Ash 2000, Gessler et al. 2011, Kennelly et al. 2007, Koledenkova et al.
    2022, all reviews or field biology, none a model.
- **Powdery mildew:**
  - **Ascospore infection:** "approximately 2.5 mm of rainfall ... followed by a minimum
    of 8 to 12 hours of leaf wetness and temperatures between 10 to 15°C".
  - **Californian risk model:**
    - Start: "Three days in a row with a minimum of six consecutive hours of temperature
      between 21 and 30'c".
    - Each day: +20 points for "6 or more consecutive hours between 21 and 32°C", -10
      otherwise or when the temperature "exceeds 32°C or goes below 21°C".
    - Reading: 0-30 not reproducing, 40-50 moderate (about 15 days a generation), over 60
      every 5 days.
  - **Pessl's variant:** the same, but "Leaf wetness longer than 8 hours leads to a
    decrease of 10 points". Here 0-20 means not reproducing, 20-60 moderate, and over 60
    calls for shorter spray intervals.
- **Black rot:** Spotts 1977 as modified by Molitor 2009 (dissertation, Geisenheim). Spotts's
  criteria met once is light, 150 % moderate, 200 % severe. The criteria are not given.
- **Grey mould:** "wet points" from wetness and temperature, starting at 38,400 points (30 %
  risk). "each wet period with about 4000 wet points increases the risk by 10%"; "each dry
  period reduces the risk by ⅕". Cites Broome et al. 1995 among others.
- **Grape berry moth (Lobesia botrana):** degree-days "> 8°C up to 24°C per hour divided by
  24"; egg hatch "after 66 degree days".
- **Anthracnose, Phomopsis:** rule sketches (2-40 °C, RH above 90 % or wetness; 5-35 °C,
  rain over 2 mm).

## Dependence

- **Nothing on the page shows what any rule was fitted to.** The downy mildew sources are
  reviews.
- **Sporulation** runs only between 12 and 29 °C at RH over 95 %. That is the engine's
  temperature-band form (`sporulation-temperature-bounds`, `lalancette1988.sporulation_bounds`),
  strictly.
- **The Californian model** is the engine's `gubler1999.powdery_index` (the UC Davis
  index). This page states its rules, which Formularium had only from Cooptera's code. Pessl's
  variant adds a wetness penalty: a variant of an engine model.
- **The grey-mould "wet points"** cite Broome 1995 but are not Broome's index as the engine
  runs it (`broome1995.botrytis`).
- **Bregaglio et al. 2022** took MISFITS's default parameters "from the METOS service"
  (RHnM 70 %, PrecZ 5 mm). These are the same 70 % and 5 mm as here, so MISFITS's defaults
  trace to this vendor ([bregaglio2022](bregaglio2022.md)).
- Molitor 2009 shares an author with the engine's `molitor2014.shoots`: a flag only.

## Bearing (2026-10-09)

- **Not a truth family:** the infection rule is not stated, the data behind it are unknown,
  and its sporulation shares the engine's form.
- **A comparator:** iMETOS alarms are what many growers act on. A FieldClimate-style alarm
  policy is a candidate baseline for spray timing in Agrarium's M4.
- **For Cooptera:** a secondary statement of the UC Davis powdery index rules (the primary,
  Gubler et al. 1999, is not held); black rot (Spotts 1977, Molitor 2009) and Lobesia
  degree-days for diseases and pests it does not yet cover.
