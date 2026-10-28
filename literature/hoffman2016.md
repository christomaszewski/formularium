---
id: hoffman2016
citation: Hoffman, R.N. & Atlas, R. 2016. Future observing system simulation experiments. Bulletin of the American Meteorological Society 97:1601-1616
doi: 10.1175/BAMS-D-15-00200.1
read: 2026-10-27, lightly: introduction, the OSSE system components, the nature runs and the section on OSSE validation and calibration in full; the rest skimmed by keyword (identical twin, calibration, validation), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 22 of 22 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [OSSE, nature run, identical twin, OSSE validation, OSE calibration, data assimilation]
records: []
datasets: []
files: [syn1027_hoffman2016.pdf (the 2026-10-27 drop)]
---

# Hoffman and Atlas 2016: a forward-looking review of OSSE practice, nature runs and validation

A review of how OSSEs are built and checked now that operational forecast systems have changed: what the nature run must be, how it is kept unlike the forecast model, and how an OSSE is validated against real data-denial experiments. No record: a review; its validation numbers are in papers it cites.

**Read this first.** A review in two columns (quotes are single-column fragments), with no quantitative OSE-versus-OSSE numbers of its own; the numbers it relies on are in Casey et al. 2015 and Gelaro et al. 2014, cited and not read. It does **not** say that NCEP took its nature run from ECMWF to avoid an identical twin.

## What it holds

- **Premise** (l. 21, 23): an OSSE assimilates synthetic observations simulated from a "realistic nature run (NR) stipulated to represent the" true atmosphere; accurate quantitative results need every component of the system to be realistic.
- **Validation** (l. 141-142, cited from Atlas 1997): what "improves the interpretation of results is validation against a corresponding OSE"; the accuracy and impact of existing observing systems in simulation are compared with the real world.
- **Nature-run validity is purpose-specific** (l. 546-555): differences from reality are not showstoppers but must be documented (l. 549); a nature run may be valid for some OSSEs and not others (l. 551); data-assimilation and forecast statistics in the OSSE and in reality should be similar, ideally with no significant difference (l. 555).
- **Identical twins** (l. 566, 569-570): to keep the forecast and nature-run models from being too similar, parameterisations may be changed; in the earliest OSSEs (before the 1980s) the two models "were often the same" and this identical-twin set-up "typically led to overly optimistic OSSE forecast" impacts. The direction is stated without a split by data type.
- **Calibration** (l. 573, cited from Hoffman et al. 1990): OSSE impacts may be calibrated empirically by comparing an OSE and an OSSE data-denial experiment "to scale the OSSE" impact for a new observing system.
- **The joint system** (l. 206, 280): ECMWF's T511 nature run (26 km, 91 levels, free-running from 1 May 2005 to 1 June 2006), forecast with NCEP's Global Spectral Model (T382L64). No reason for the choice of centres is given.
- **Error-growth test** (l. 592-593): the GSM predicts the nature run better than the real atmosphere, but the difference in error growth is "small enough to conclude that there will be no twin problem", a judgement from temperature error growth (Fig. 3). Not a number.
- **Reality-to-simulation validation** (l. 591-592, 600, 603): run parallel OSE and OSSE at the start of the nature run, when it is closest to reality; adding a system should have nearly the same impact in both. After one correction of the random errors of simulated radiosondes, real and simulated RMS errors no longer differed significantly (cited from Casey et al. 2015); Fig. 4 compares perfect and error-added observations (l. 617).

## What TRUTH-METHOD says of it

TRUTH-METHOD's reference table: "Hoffman & Atlas 2016, BAMS | OSSEs evolving with forecast systems". Its question section: "NCEP avoided the identical twin by taking its nature run from ECMWF's model" (no source given).

Verdict: **confirmed for the table use; the NCEP sentence is not in this paper.**
- It is a review of OSSE practice with the ECMWF T511 and GMAO G5NR nature runs (l. 206).
- It names the ECMWF nature run and NCEP's forecast model (l. 206, 280) but never says this avoided the identical twin.
- On twins it says only that early identical twins "typically led to overly optimistic" impacts (l. 569-570), that the models should not be too similar (l. 566), and that error growth was close enough (l. 592-593).
- It gives the validation recipe that part 3 follows (l. 141-142, 573, 591-600).

## Dependence

- Atlas 1997; Hoffman et al. 1990 (calibration); Casey et al. 2015 and Gelaro et al. 2014 (G5NR validation), all cited and not read. Atlas is also an author of `atlas2015` and `halliwell2014`: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD:** the NCEP sentence needs a source or removal; this paper supports "overly optimistic" for identical twins, with no data-type direction (compare `halliwell2014` and `yu2019`, which differ on direction).
- **D45:** its error-growth comparison (l. 592-593) is the practitioners' test of "too alike"; `yu2019` shows below that matching error growth was not enough.
- **Not shown:** a measured size of the optimism, or an OSSE prediction checked against a later real observing system.
