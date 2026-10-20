"""Every formulation either tool uses, with its record (records.py), in one namespace.

**Where the records come from** (rebuilt 2026-10-07, Agrarium decision D24):
- **The engine's models** are Cooptera's own list (`xema engine models --json`) at
  `cooptera@6d8d2d4`, relisted at `7b102e0`, under Cooptera's ids, with its sources,
  authors and how it checked them (`checked` names the PDF it holds, or the trail).
  Agrarium keeps a snapshot of that list (`world/engine_models.json`), and a test there
  fails if a record here drifts from it.
- **Their structure tags** are Agrarium's judgement (its `ENGINE_STRUCTURES`, moved here):
  assumed from each model's title and module, unless `structures_note` says more.
- **Roles** (process, observation, reference; Agrarium decision D26) are Agrarium's
  judgement too. Every record not marked otherwise is a `process`.
- **Added authors** are names Agrarium's earlier records held that Cooptera's list lacks
  (its `EXTRA_AUTHORS`, moved here), each group with how it was found.
- **The truth's formulations** that the engine does not list come from Agrarium's
  `world/formulations.py`. Where the truth and the engine use one model, the id and record
  are Cooptera's.
- **Read here:** Brischetto et al. 2021's Magarey parameters (Figure 2, 2026-10-07), and
  NOAA's solar position document.

How each author list was obtained is in `authors_from` (records.AUTHOR_SOURCES). A search
summary is never `read`.
"""

from __future__ import annotations

from .records import Added, Formulation, Published

FORMULATIONS: dict[str, Formulation] = {
    # -- The engine's models, from Cooptera's list at cooptera@7b102e0 --------------------
    "kennelly2007.trigger": Formulation(
        "Primary infection trigger: 2.5 mm in a day at a mean of 11 °C",
        (
            "Kennelly et al. 2007, Phytopathology 97: 512-522 (the paper credits the criterion to"
            " Gadoury et al. 1998 and 2000, whose authors it shares)"
        ),
        year=2007,
        authors=(
            "Kennelly, Megan M.",
            "Gadoury, David M.",
            "Wilcox, Wayne F.",
            "Magarey, Peter A.",
            "Seem, Robert C.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2007-kennelly-10-1094-phyto-97-4-0512.pdf",
        structures=("rain-temperature-trigger",),
        calibrated_on=("kennelly2006.chancellor",),
        calibration_note=(
            "Read 2026-10-09: Kennelly et al. 2007 (p. 513) say 'Using the reported data, a set"
            " of criteria was developed (7,8)' (Gadoury et al. 1998 and 2000) and evaluated it"
            " 'in addition to the Chancellor vineyard in Geneva where the original data used to"
            " develop the criteria were collected'; Kennelly et al. 2006 give fifteen years of"
            " those data. Evaluated in four Finger Lakes Chancellor vineyards, 2001-2003"
        ),
        flags=(
            "First printed by Gadoury, Seem & Wilcox 1997 (NYS IPM Project Reports; read"
            " 2026-10-09, literature/gadoury1997), from fifteen years of weather, vine growth and"
            " first disease: 5-6 flat leaves with clusters visible, 0.10 in (2.5 mm) of rain or"
            " more, and temperatures during the rain above 52 °F (11.1 °C). The engine's daily"
            " mean of 11 °C is not 'during the rain', and the growth stage is dropped.",
        ),
    ),
    "goidanich.incubation": Formulation(
        "Incubation of downy mildew by Goidanich's table",
        (
            "Goidanich et al. 1957, as transcribed in Porras Soriano 2006 (thesis, Universidad de"
            " Córdoba, Table 4.3), which the code cites"
        ),
        year=1957,
        authors=("Goidanich, G.", "Casarini, B.", "Foschi, S."),
        authors_from="trail",
        checked=(
            "the reference lists of Rossi et al. 2005 and 2008 (held); the thesis is not held"
        ),
        structures=("daily-incubation-table",),
        added_authors=(
            Added(
                ("Porras Soriano",),
                "trail",
                (
                    "the engine's table is Goidanich's as Porras Soriano 2006 (Table 4.3) prints "
                    "it; Cooptera names only the 1957 authors"
                ),
            ),
        ),
        calibrated_on=("goidanich1957",),
        calibration_note="the table is Goidanich et al. 1957's data (datasets.py)",
        flags=(
            "The same table, all 53 rows of both columns (12-25 °C by 0.25 °C, RH below and above"
            " 75 %, the non-monotonic 18.25 °C humid value included), is printed by López Frías"
            " et al. 2009 (Tenerife) and used by Puelles Ruiz de Gopegui 2020 (Rioja): a Spanish"
            " version in circulation (checked 2026-10-09 against Cooptera's incubation.py). How"
            " it derives from Goidanich et al. 1957's high- and low-humidity data is not shown"
            " by any of them.",
            "Casanova-Gascón et al. 2019 (Agronomy 9:738, Somontano, read 2026-10-10;"
            " literature/casanovagascon2019): run by growers there to date infections, its dates"
            " in 2016 and 2018 'were off by several weeks' against observed symptoms. No numbers"
            " are printed.",
            "Run in Spain by Pérez-Expósito et al. 2017 (VineSens, Ribeira Sacra) and Elbaile Mur"
            " 2016 (Somontano, Barrios et al. 2004's table); the 1961 Penedès warning service used"
            " a daily incubation step from 'the University of Bologna study', probably this table"
            " (Ticó Maluquer 2013; literature/perezexposito2017, elbailemur2016,"
            " ticomaluquer2013; light reads, 2026-10-10).",
        ),
    ),
    "rule_3_10": Formulation(
        "The 3-10 rule: 10 °C, shoots of 10 cm, 10 mm of rain",
        (
            "Baldacci 1947, as its Italian users state it (SOURCES.md §8); the policy's trigger "
            "until v0.7"
        ),
        year=1947,
        authors=("Baldacci, E.",),
        authors_from="trail",
        checked="Caffi et al. 2007's reference list (held); SOURCES.md §8",
        structures=("rain-temperature-trigger",),
    ),
    "rossi2008.primary": Formulation(
        "Primary infections cohort by cohort: germination to incubation",
        (
            "Rossi, Caffi, Giosuè & Bugiani 2008, Ecological Modelling 212: 480-491; sporangia"
            " survival as Blaeser & Weltzien 1979 fit it (D30)"
        ),
        year=2008,
        authors=("Rossi, Vittorio", "Caffi, Tito", "Giosuè, Simona", "Bugiani, Riccardo"),
        authors_complete=True,
        authors_from="read",
        checked="2008-rossi-10-1016-j-ecolmodel-2007-10-046.pdf",
        # Not goidanich.incubation since cooptera@7b102e0: eqs 8-9 cite it, not compute it.
        borrows=("rossi2008pp.dormancy", "blaeser1979.survival"),
        structures=(
            "hydro-thermal-oospore-cohorts",
            "wet-degree-hours-infection",
            "incubation-window",
        ),
        # Its incubation (eqs 8-9): two regressions on temperature at two humidity levels.
        calibrated_on=("goidanich1957", "laviola1986"),
        calibration_note=(
            "Read 2026-10-09: eqs 8-9 are Rossi et al. 2002's regressions (Atti Giornate"
            " Fitopatologiche 2002, 2:263-270, Fig. 2, p. 265, the same coefficients), 'adattate"
            " ai dati di Goidanich et al. (1957)' for that table's high and low humidity."
            " Sanna 2017 (thesis, pp. 75-76) says the same. Inferred, trail"
            " (2026-10-09): eq. 5's germination time, credited to Laviola et al. 1986 (p. 482),"
            " was fitted to their data (datasets.laviola1986); the fit is not stated"
        ),
    ),
    "rossi2008pp.dormancy": Formulation(
        "Oospore dormancy: the vapour-pressure-deficit moisture rule",
        "Rossi et al. 2008, Plant Pathology, doi:10.1111/j.1365-3059.2007.01738.x",
        year=2008,
        authors=("Rossi, V.", "Caffi, T.", "Bugiani, R.", "Spanna, F.", "Della Valle, D."),
        authors_complete=True,
        authors_from="read",
        checked=(
            "2008-rossi-10-1111-j-1365-3059-2007-01738-x.pdf, page images (literature/rossi2008pp)"
        ),
        structures=("hydro-thermal-oospore-cohorts",),
        calibrated_on=("rossi2008pp.discs", "laviola1986"),
        calibration_note=(
            "read 2026-10-12: the Gompertz on hydro-thermal time was fitted to leaf-disc"
            " infection by oospores sampled weekly at Asti, 1999-2003 (R2 0.887 pooled); the"
            " temperature rate is Laviola et al. 1986's polynomial and the moisture switch"
            " (VPD <= 4.5 hPa or rain) is Rossi & Caffi 2007's upper confidence limit"
        ),
        parameters=(
            Published(
                "vpd_max_hpa",
                4.5,
                "hPa",
                "eq. 4, p. 218 (M = 1 when R > 0 mm or VPD <= 4.5 hPa)",
                "read",
            ),
            Published(
                "gompertz_a", 15.9, "-", "abstract (pooled hydro-thermal time, +/- 2.63)", "read"
            ),
            Published("gompertz_b", 0.653, "per HT unit", "abstract (pooled, +/- 0.034)", "read"),
            Published(
                "laviola_t0",
                1330.1,
                "h",
                "eq. 3, p. 218 (t = 1330.1 - 116.19 T + 2.6256 T^2)",
                "read",
            ),
            Published("laviola_t1", -116.19, "h per degC", "eq. 3, p. 218", "read"),
            Published("laviola_t2", 2.6256, "h per degC^2", "eq. 3, p. 218", "read"),
        ),
    ),
    "blaeser1979.survival": Formulation(
        "Survival of sporangia, and 60 °C·h of wetness to infect",
        (
            "Blaeser & Weltzien 1979, Z. PflKrankh. PflSchutz 86: 489-498, Abb. 3 and summary:"
            " lifetime against the saturation deficit E (1 - RH/100) in mm, at most 6 h above"
            " 30 °C (Rossi et al. 2008 eq. 6 prints T (1 - RH/100))"
        ),
        year=1979,
        authors=("Blaeser, Marlene", "Weltzien, H. C."),
        authors_complete=True,
        authors_from="read",
        checked="1979-blaeser-url-blaeser-weltzien-1979-plasmopara.pdf",
        structures=("vpd-survival", "wet-degree-hours-infection"),
        structures_note=(
            "read 2026-10-09 (literature/blaeser1979): survival as a quadratic in the saturation"
            " deficit, infection as a constant temperature sum over the wet period"
        ),
        calibrated_on=("blaeser1978.survival", "blaeser1979"),
        calibration_note=(
            "Read 2026-10-09 in the paper (Z. PflKrankh. PflSchutz 86:489-498, by Marlene"
            " Blaeser and H. C. Weltzien; Cooptera's list reads it since cooptera@2ae3182): the"
            " survival"
            " curves (Abb. 3) were fitted to the laboratory survival tests that Blaeser &"
            " Weltzien 1978 describe (sporangia from potted Müller-Thurgau, 10-30 °C,"
            " 30-100 % RH), leaving out 100 % RH and 30 °C; the infection rule to Tab. 1's"
            " minimum wetness at 6-25 °C. That the 1979 fit used the 1978 tests is inferred: the"
            " paper cites them and shows the same grid of conditions"
        ),
        parameters=(
            Published("attached.c0_d", 9.27, "d", "Abb. 3, curve I, p. 493", "read"),
            Published("attached.c1_d_per_mm", -1.12, "d/mm", "Abb. 3, curve I, p. 493", "read"),
            Published("attached.c2_d_per_mm2", 0.04, "d/mm2", "Abb. 3, curve I, p. 493", "read"),
            Published("detached.c0_d", 5.67, "d", "Abb. 3, curve II, p. 493", "read"),
            Published("detached.c1_d_per_mm", -0.47, "d/mm", "Abb. 3, curve II, p. 493", "read"),
            Published("detached.c2_d_per_mm2", 0.01, "d/mm2", "Abb. 3, curve II, p. 493", "read"),
            Published(
                "max_life_above_30c_h", 6.0, "h", "summary, p. 489; 1978 summary, p. 155", "read"
            ),
            Published("infection.mean_degree_hours", 49.7, "°C·h", "Tab. 1 and p. 491", "read"),
            Published("infection.slope_degree_hours", 60.0, "°C·h", "Abb. 1, p. 491-492", "read"),
            Published("infection.intercept_h", -0.67, "h", "Abb. 1, p. 491-492", "read"),
        ),
        flags=(
            "Read 2026-10-09. Survival: y = c0 + c1·x + c2·x², y the maximum lifetime in days,"
            " x the saturation deficit 'S_d = E (1 - F/100) (Steubing 1965)' in mm, F the RH."
            " E is not defined in the text; as Steubing's saturation deficit it is the saturation"
            " vapour pressure in mm Hg (inferred). Rossi et al. 2008 (eq. 6) and Brischetto et"
            " al. 2020 (eqs 1-2) compute x as T·(1 - RH/100), T in °C, which is close to E's"
            " value only between about 10 and 25 °C.",
            "The fit leaves out 30 °C, 'da die relative Luftfeuchtigkeit keine Rolle spielt', and"
            " its points stop near x = 17 mm (Abb. 3's axis), so the curves are unsupported"
            " beyond that and above about 25 °C: both are U-shaped (curve II's"
            " minimum is 0.15 d at x = 23.5 mm) and rise beyond. The papers' own rule for heat"
            " is a lifetime of at most 6 h above 30 °C (the 1979 summary; the 1978 summary: 'bei"
            " 30° C liegt sie bei maximal 6 Std.'), and the 1979 calendars mark days with more"
            " than 6 h above 30 °C in the canopy.",
            "Infection: the least wetness that infected at least half the inoculated leaves at"
            " constant 6-25 °C; T·hours has mean 49.7 (s² = 23.55), and hours = -0.67 +"
            " 60.0/T (r = 0.993). The summary states 'mindestens 50 Gradstunden'.",
        ),
    ),
    "caffi2013.sporulation": Formulation(
        "Sporulation nights: three moist dark hours",
        "Caffi et al. 2013, Phytopathology 103: 64-73 (SOURCES.md §8)",
        year=2013,
        authors=("Caffi, Tito", "Gilardi, Giovanna", "Monchiero, Matteo", "Rossi, Vittorio"),
        authors_complete=True,
        authors_from="read",
        checked="2013-caffi-10-1094-phyto-04-12-0082-r.pdf, page images (literature/caffi2013)",
        structures=("dark-moist-hours-sporulation",),
        calibrated_on=("caffi2013.piedmont",),
        calibration_note=(
            "read 2026-10-12: the cut-off of 3 or more dark moist hours was chosen by a ROC"
            " analysis across 58 field assessments with new lesions at Grugliasco and Neive,"
            " 2008-2010 (AUROC 0.816; accuracy 0.85, sensitivity 0.91, specificity 0.67)"
        ),
        parameters=(
            Published("dark_moist_hours_min", 3.0, "h", "abstract and p. 68 (ROC cut-off)", "read"),
            Published("rh_min", 80.0, "%", "abstract, Methods p. 65, Table 3 footnote f", "read"),
            Published("wetness_min", 30.0, "min", "abstract and Table 3 footnote f", "read"),
            Published(
                "dark_start_hour", 20.0, "h", "Methods p. 65 (8:00 p.m. to 7:00 a.m.)", "read"
            ),
            Published("dark_end_hour", 7.0, "h", "Methods p. 65", "read"),
        ),
        flags=(
            "A moist hour is one with RH >= 80 %, rain > 0 mm OR wetness > 30 min in the"
            " abstract and Table 3; the Methods (p. 65) print the same three with AND and WD >"
            " 0.5 h. The paper does not resolve it (read 2026-10-12). No temperature bound belongs"
            " to the rule; the 10-30 C limits are cited from Lalancette et al. 1988.",
        ),
    ),
    "lalancette1988.sporulation_bounds": Formulation(
        "Sporulation only between 10 and 30 °C",
        (
            "Lalancette et al. 1988, doi:10.1094/Phyto-78-1316, as Brischetto et al. 2021 credit "
            "it (its Fig. 2 and its references label the two 1988 papers differently)"
        ),
        year=1988,
        authors=("Lalancette, N.", "Madden, L. V.", "Ellis, M. A."),
        authors_complete=True,
        authors_from="read",
        checked="1988-lalancette-10-1094-phyto-78-1316.pdf",
        structures=("sporulation-temperature-bounds",),
        flags=(
            "The authors call 10 and 30 °C 'arbitrarily chosen temperature extremes' and say"
            " true limits of 11 and 28 °C would give narrower, taller curves (read 2026-10-08,"
            " literature/lalancette1988sporulation).",
        ),
    ),
    "brischetto2020.survival": Formulation(
        "Survival of detached sporangia (written and tested; no run calls it yet)",
        (
            "Brischetto et al. 2020, doi:10.3389/fpls.2020.01187, equations 1 and 2, run as"
            " Blaeser & Weltzien 1979 fit them (D30)"
        ),
        year=2020,
        authors=("Brischetto, Chiara", "Bove, Federica", "Languasco, Luca", "Rossi, Vittorio"),
        authors_complete=True,
        authors_from="read",
        checked="2020-brischetto-10-3389-fpls-2020-01187.pdf",
        borrows=("blaeser1979.survival",),
        structures=("vpd-survival",),
        flags=(
            "Eq. 2 as printed (c2 = 0.02) never gives a detached sporangium less than 2.9"
            " days (at x = 11.75), and the hourly rate is capped at 1/24. Applied as"
            " Agrarium's truth applies it, it leaves 97 % alive after 8 h of Kennelly et al."
            " 2007's hot, dry day (36.5 °C, 15 % RH), where nearly all died in the canopy, and"
            " 72 % after 24 h at 20 °C and 30 % RH, where Blaeser & Weltzien 1978, cited by"
            " Brischetto, found death within 24 h (Agrarium"
            " scripts/diagnostics/sporangia_survival.py, 2026-10-08). With Rossi et al."
            " 2008's c2 = 0.01 the cap still leaves 71 % after 8 h.",
            "Kennelly's sporangia were attached, on lesions (Kennelly et al. 2007, read"
            " 2026-10-09), so eq. 1 is the like-for-like comparison: its lifetime never falls"
            " below about 34 h (x = 14), against none viable after 6-8 h of clear, dry days."
            " Kennelly found DMCast's survival model, from the same Blaeser & Weltzien study,"
            " overpredicted viability in the field.",
            "Read at the source 2026-10-09 (literature/blaeser1979): Blaeser & Weltzien 1979"
            " print c2 = 0.01 for detached sporangia (Abb. 3, curve II), so eq. 2's 0.02 is a"
            " transcription error and Rossi et al. 2008's 0.01 is right. Their index is the"
            " saturation deficit E·(1 - RH/100) in mm (E the saturation vapour pressure,"
            " inferred), not T·(1 - RH/100), which both Brischetto and Rossi compute. The cap of"
            " 1/24 an hour is Brischetto's construction (MOR = 1/(24·y)); the source gives"
            " maximum lifetimes in days, and at most 6 h above 30 °C. Blaeser & Weltzien 1978"
            " ('<24 h at 20 °C and 30 % RH' in Brischetto's discussion) show that only in a bar"
            " chart (Abb. 3, p. 159).",
            "Table 1 (p. 4, read in the page image 2026-10-10; literature/brischetto2020) gives"
            " VPD 11.6, 9.59 and 12.59 hPa at 22.4 °C and 57 %, 21.9 °C and 64.6 %, 23.0 °C and"
            " 55.77 %. Those are the saturation deficit E·(1 - RH/100) in hPa (11.6, 9.3, 12.4"
            " by Magnus), not the printed T·(1 - RH/100) (9.6, 7.8, 10.2), and the discussion"
            " defines VPD as the saturation deficit. Which the authors ran is not stated; the"
            " engine runs the printed form.",
            "Douillet 2023 (thesis, Bordeaux; literature/douillet2023, p. 96, read 2026-10-13)"
            " prints the hourly rate as (1/24)·(5.67 - 0.47·VPD + 0.01·VPD²) with VPD in hPa"
            " by Tetens, crediting Blaeser & Weltzien 1979 and Brischetto 2020: c2 = 0.01 as"
            " the source has it, but y/24 where Brischetto's is 1/(24·y). Which the thesis ran"
            " is not printed.",
        ),
        parameters=(
            Published("eq2.c0_d", 5.67, "d", "eq. 2", "read"),
            Published("eq2.c1", -0.47, "d", "eq. 2", "read"),
            Published("eq2.c2_as_printed", 0.02, "d", "eq. 2 (the source prints 0.01)", "read"),
        ),
    ),
    "brischetto2021.secondary": Formulation(
        "Secondary infection weather (partial: no severity)",
        "Brischetto et al. 2021, doi:10.3389/fpls.2021.636607",
        year=2021,
        authors=("Brischetto, Chiara", "Bove, Federica", "Fedele, Giorgia", "Rossi, Vittorio"),
        authors_complete=True,
        authors_from="read",
        checked="2021-brischetto-10-3389-fpls-2021-636607.pdf",
        borrows=(
            "magarey2005.generic",
            "caffi2013.sporulation",
            "lalancette1988.sporulation_bounds",
        ),
        structures=("magarey-wetness-response",),
        doi="10.3389/fpls.2021.636607",
        parameters=(
            # Figure 2's caption, (D): Magarey et al. 2005's model, its parameters estimated
            # from Blaeser & Weltzien 1979 and Caffi et al. 2016 (R² = 0.87). Read 2026-10-07.
            Published("w_min_h", 2.0, "h", "Figure 2 caption (D)", "read"),
            Published("t_min_c", 4.0, "°C", "Figure 2 caption (D)", "read"),
            Published("t_opt_c", 21.0, "°C", "Figure 2 caption (D)", "read"),
            Published("t_max_c", 30.2, "°C", "Figure 2 caption (D)", "read"),
        ),
        # Figure 2 caption (D), read 2026-10-07.
        calibrated_on=("blaeser1979", "caffi2016"),
        flags=(
            "Read 2026-10-09 (Materials and methods, Table 2 footnote 3): to score the model, the"
            " days with latent infections were counted with 'the equation of Orlandini et al."
            " (2008)' for incubation, as a function of temperature and RH (Orlandini, Massetti &"
            " Dalla Marta 2008, Comput. Electron. Agric. 64:149-161, the later PLASMO). That paper"
            " (read 2026-10-09) prints the form and bounds but not its coefficient fm, so the"
            " coefficient Brischetto et al. used is not traceable to it."
            " The evaluation, not the fitted parameters, used PLASMO's incubation, so the latent-"
            "infection days it was scored on depend on it: a truth using a PLASMO incubation"
            " would flatter this model in a comparison like theirs. If a later reading shows the"
            " parameters were tuned after that evaluation, make it calibrated_with (Agrarium,"
            " 2026-10-09).",
        ),
    ),
    "magarey2005.generic": Formulation(
        "Generic infection response to temperature and wetness",
        "Magarey et al. 2005, doi:10.1094/PHYTO-95-0092, with Brischetto's 4 / 21 / 30.2 °C",
        year=2005,
        authors=("Magarey, R. D.", "Sutton, T. B.", "Thayer, C. L."),
        authors_complete=True,
        authors_from="read",
        checked="2005-magarey-10-1094-phyto-95-0092.pdf",
        structures=("magarey-wetness-response",),
        doi="10.1094/PHYTO-95-0092",
        equations="magarey2005",
        # Read 2026-10-07 in the copy Cooptera holds: Table 2's grape rows, and the rule for
        # an unknown Wmax (p. 93). Table 2's columns: Tmin, Tmax, Topt (°C), Wmin, Wmax (h).
        parameters=(
            Published(
                "p_viticola.t_min_c", 1.0, "°C", "Table 2, Plasmopara viticola, grape", "read"
            ),
            Published(
                "p_viticola.t_max_c", 30.0, "°C", "Table 2, Plasmopara viticola, grape", "read"
            ),
            Published(
                "p_viticola.t_opt_c", 20.0, "°C", "Table 2, Plasmopara viticola, grape", "read"
            ),
            Published(
                "p_viticola.w_min_h", 2.0, "h", "Table 2, Plasmopara viticola, grape", "read"
            ),
            Published(
                "p_viticola.w_max_h", 14.0, "h", "Table 2, Plasmopara viticola, grape", "read"
            ),
            Published(
                "b_cinerea_berry.t_min_c", 10.0, "°C", "Table 2, Botrytis cinerea, grape", "read"
            ),
            Published(
                "b_cinerea_berry.t_max_c", 35.0, "°C", "Table 2, Botrytis cinerea, grape", "read"
            ),
            Published(
                "b_cinerea_berry.t_opt_c", 20.0, "°C", "Table 2, Botrytis cinerea, grape", "read"
            ),
            Published(
                "b_cinerea_berry.w_min_h", 4.0, "h", "Table 2, Botrytis cinerea, grape", "read"
            ),
            Published(
                "b_cinerea_berry.w_max_h", 10.0, "h", "Table 2, Botrytis cinerea, grape", "read"
            ),
            Published(
                "b_cinerea_flower.t_min_c",
                1.0,
                "°C",
                "Table 2, Botrytis cinerea, grape flower",
                "read",
            ),
            Published(
                "b_cinerea_flower.t_max_c",
                34.0,
                "°C",
                "Table 2, Botrytis cinerea, grape flower",
                "read",
            ),
            Published(
                "b_cinerea_flower.t_opt_c",
                25.0,
                "°C",
                "Table 2, Botrytis cinerea, grape flower",
                "read",
            ),
            Published(
                "b_cinerea_flower.w_min_h",
                1.0,
                "h",
                "Table 2, Botrytis cinerea, grape flower",
                "read",
            ),
            Published(
                "b_cinerea_flower.w_max_h",
                12.0,
                "h",
                "Table 2, Botrytis cinerea, grape flower",
                "read",
            ),
            Published(
                "w_max.intercept_h",
                3.8,
                "h",
                "p. 93: Wmax = 3.8 + 3.0 Wmin, for an unknown Wmax",
                "read",
            ),
            Published(
                "w_max.slope",
                3.0,
                "h/h",
                "p. 93: Wmax = 3.8 + 3.0 Wmin, for an unknown Wmax",
                "read",
            ),
        ),
        flags=(
            "Table 2's own rows were fitted to other data than the parameters the engine runs"
            " (calibrated_on records the engine's): its P. viticola row to Lalancette, Ellis &"
            " Madden 1988 (its ref. 43, 5-28 °C, 2-24 h wet, 20% incidence; datasets.py"
            " lalancette1988a), its grape Botrytis rows to Nair & Allen 1993 (ref. 56: berries"
            " 12-30 °C, flowers 5-30 °C, 20% incidence; nair1993). A formulation that runs"
            " Table 2's rows shares those data (Bregaglio et al. 2013 does). Its Botrytis Tmax"
            " of 35 °C is the paper's default where none was measured.",
        ),
        # As the engine runs it, with Brischetto 2021's parameters (its title says so). Table
        # 2's own rows were fitted to other data: see the flag and datasets.py.
        calibrated_on=("blaeser1979", "caffi2016"),
    ),
    "magarey2010.rules": Formulation(
        "Downy mildew rules of thumb: 10:10:24, sporulation, infection",
        (
            "Magarey 2010, Managing Downy Mildew (Winning the war!), GWRDC Innovators Network"
            " Module INO904, March 2010; the page's default disease layer"
        ),
        year=2010,
        authors=("Magarey, Peter A.",),
        authors_complete=True,
        authors_from="read",
        checked="2010-magarey-url-magarey-2010-gwrdc-managing-downy-mi.pdf",
        borrows=("noaa.solar_position",),
        structures=("rain-temperature-trigger",),
        flags=(
            "The fact sheet is held since 2026-10-10 (literature/magarey2010: Magarey, Managing"
            " Downy Mildew, GWRDC Innovators Network Module INO904, March 2010). Cooptera's"
            " docstring quotes it word for word (10:10:24, 45 °C-h, RH >= 98 % at >= 13 °C in 4"
            " h of darkness, 5-17 days). The sheet also asks that oospores in the top 1-2 cm of"
            " soil be wet for >= 16 h at >= 8 °C, which the module does not use.",
        ),
    ),
    "puelles2024.ur": Formulation(
        "UR mildiu rules (La Rioja)",
        "Puelles et al. 2024, Crop Protection, doi:10.1016/j.cropro.2023.106450",
        year=2024,
        authors=("Puelles, M.", "Arbizu-Milagro, J.", "Castillo-Ruiz, F.J.", "Peña, J.M."),
        authors_complete=True,
        authors_from="read",
        checked="2024-puelles-10-1016-j-cropro-2023-106450.pdf",
        borrows=("rule_3_10", "goidanich.incubation"),
        structures=(
            "wet-degree-hours-infection",
            "rain-temperature-trigger",
            "thermal-time-oospore-threshold",
            "dark-moist-hours-sporulation",
            "sporulation-temperature-bounds",
        ),
        structures_note=(
            "read 2026-10-09 (literature/puelles2024): the UR model is the Goidanich model (the"
            " 3-10 conditions and Goidanich's daily incubation) with oospores at 140-160 °C·days"
            " above 8 °C from 1 January, infection at 50 °C·h of wetness, and sporulation after"
            " 4 h dark at 12-29 °C and RH > 95 %"
        ),
        calibrated_on=("puelles2024.rioja",),
        calibration_note=(
            "read 2026-10-09: 'a maturity value of 160 °C was the most appropriate (data not"
            " shown)', on the study's own plots; the rule itself is credited to Gehmann et al."
            " 1987, the 50 °C·h to Dubuis et al. 2012 (read 2026-10-12: Dubuis prints both,"
            " literature/dubuis2012)"
        ),
        flags=(
            "The paper's UR model also computes the 3-10 conditions (T >= 10 °C, shoots >= 10 cm,"
            " 10 mm in 24-48 h, 'the same algorithm as the Goidanich model'): a borrowing"
            " Cooptera's list names since cooptera@2ae3182 (asked 2026-10-09). It adds germination"
            " after 5 mm in 48 h at 12 °C or more, and kills spores after 6 h above 30 °C"
            " (credited to Blaeser & Weltzien 1979).",
        ),
    ),
    "kennelly2005.bunch_window": Formulation(
        "Bunches past downy mildew four weeks after flowering",
        "Kennelly et al. 2005, Phytopathology 95: 1445-1452",
        year=2005,
        authors=(
            "Kennelly, Megan M.",
            "Gadoury, David M.",
            "Wilcox, Wayne F.",
            "Magarey, Peter A.",
            "Seem, Robert C.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2005-kennelly-10-1094-phyto-95-1445.pdf",
        structures=("bunch-susceptibility-window",),
        flags=(
            "The paper gives no fixed window for berries (read 2026-10-08, literature/"
            "kennelly2005): at Geneva berries stopped sporulating when inoculated later than 1"
            " to 2 weeks after bloom, pedicels stayed susceptible to 4 weeks, and relative"
            " severity fell with degree-days after bloom (Y = 1.008 - 0.379 log(X+1)). At"
            " Loxton, South Australia, berries stayed susceptible much longer. 'Four weeks"
            " after flowering' matches the pedicels.",
        ),
    ),
    "madden1999.detection_bound": Formulation(
        "What a clean sample of leaves rules out",
        (
            "Madden & Hughes 1999, Phytopathology 89: 1088-1103, eqs 12-13 (its leaf correlation "
            "from Madden, Hughes & Ellis 1995)"
        ),
        year=1999,
        authors=("Madden, L. V.", "Hughes, G."),
        authors_complete=True,
        authors_from="read",
        checked="1999-madden-10-1094-phyto-1999-89-11-1088.pdf",
        structures=("sampling-detection-bound",),
        role="observation",
        calibrated_on=("madden1995",),
    ),
    "cannon2001.sensitivity": Formulation(
        "A scout's imperfect detection (at 1.0 in the policy: no effect yet)",
        "Cannon 2001, Preventive Veterinary Medicine 49: 141-163, eq. 4.6",
        year=2001,
        authors=("Cannon, R.M.",),
        authors_complete=True,
        authors_from="read",
        checked="2001-cannon-10-1016-s0167-5877-01-00184-2.pdf",
        structures=("detection-sensitivity",),
        role="observation",
    ),
    "hughes2017.scoring": Formulation(
        "Scores of probabilistic warnings",
        "Hughes & Burnett 2017, Phytopathology 107: 1136-1143",
        year=2017,
        authors=("Hughes, Gareth", "Burnett, Fiona J."),
        authors_complete=True,
        authors_from="read",
        checked="2017-hughes-10-1094-phyto-01-17-0023-fi.pdf",
        structures=("warning-scores",),
        role="reference",
    ),
    "cortazar2009.budburst": Formulation(
        "Budburst by degree-days above 5 °C from 1 January",
        (
            "García de Cortázar-Atauri 2006, thesis, Table 11; the same values in García de "
            "Cortázar-Atauri, Brisson & Gaudillère 2009, Int. J. Biometeorol. 53: 317-326"
        ),
        year=2009,
        authors=("García de Cortázar-Atauri, Iñaki", "Brisson, Nadine", "Gaudillere, Jean Pierre"),
        authors_complete=True,
        authors_from="read",
        checked=(
            "2006-garcia-de-cortazar-url-garcia-de-cortazar-2006-thesis.pdf; "
            "2009-cortazar-atauri-10-1007-s00484-009-0217-4.pdf"
        ),
        structures=("degree-day-phenology",),
        calibrated_on=("phenoclim",),
        calibration_note=(
            "Table 11 is on p. 43 of the thesis's budburst article (PDF p. 64), read 2026-10-13"
            " in the page image (literature/cortazar2006); the 2009 paper's Table 8 prints the"
            " same values (literature/cortazar2009)."
        ),
        parameters=(
            Published(
                "gdd5_sum.cabernet_sauvignon",
                318.6,
                "°C·d",
                "thesis Table 11, GDD (5 °C) G_dc",
                "read",
            ),
            Published(
                "gdd5_sum.chasselas", 257.8, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
            Published(
                "gdd5_sum.chardonnay", 220.1, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
            Published(
                "gdd5_sum.grenache", 321.3, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
            Published("gdd5_sum.merlot", 265.3, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"),
            Published(
                "gdd5_sum.pinot_noir", 258.4, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
            Published(
                "gdd5_sum.riesling", 257.7, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
            Published(
                "gdd5_sum.sauvignon", 294.4, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
            Published("gdd5_sum.syrah", 265.3, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"),
            Published(
                "gdd5_sum.ugni_blanc", 284.7, "°C·d", "thesis Table 11, GDD (5 °C) G_dc", "read"
            ),
        ),
    ),
    "cortazar2009.brin": Formulation(
        "Budburst after chilling: Bidabe's cold actions, then forcing hours",
        (
            "García de Cortázar-Atauri, Brisson & Gaudillère 2009, Int. J. Biometeorol. 53: "
            "317-326, Eqs 3-6 and Table 8"
        ),
        year=2009,
        authors=("García de Cortázar-Atauri, Iñaki", "Brisson, Nadine", "Gaudillere, Jean Pierre"),
        authors_complete=True,
        authors_from="read",
        checked="2009-cortazar-atauri-10-1007-s00484-009-0217-4.pdf",
        borrows=("bidabe1965.cold_action", "richardson1974.forcing_hours"),
        structures=("chilling-dormancy", "degree-day-phenology"),
        calibrated_on=("phenoclim",),
    ),
    "bidabe1965.cold_action": Formulation(
        "A day's cold action, Q10^(-Tx/10) + Q10^(-Tn/10)",
        (
            "Bidabe 1965a (C. R. Acad. Agric. Fr. 49: 934-945) and 1965b (96e Congrès "
            "Pomologique, 51-56), as García de Cortázar-Atauri et al. 2009 cite them; not held"
        ),
        year=1965,
        authors=("Bidabe, B.",),
        authors_from="trail",
        checked="García de Cortázar-Atauri et al. 2009's references (held)",
        structures=("chilling-dormancy",),
    ),
    "richardson1974.forcing_hours": Formulation(
        "Growing degree hours after dormancy",
        (
            "Richardson et al. 1974 and 1975, as García de Cortázar-Atauri et al. 2009 cite them "
            "(the 1975 paper adds Anderson and Ashcroft); not held"
        ),
        year=1974,
        authors=(
            "Richardson, E. A.",
            "Seeley, S. D.",
            "Walker, D. R.",
            "Anderson, J.",
            "Ashcroft, G.",
        ),
        authors_from="trail",
        checked="García de Cortázar-Atauri et al. 2009's references (held)",
        structures=("degree-day-phenology",),
        structures_note="growing degree hours",
    ),
    "ramos2017.budburst": Formulation(
        "Budburst, bloom, veraison and harvest fitted in the Penedès",
        "Ramos 2017, Agricultural and Forest Meteorology 247: 104-115, Table 2",
        year=2017,
        authors=("Ramos, M.C.",),
        authors_complete=True,
        authors_from="read",
        checked="2017-ramos-10-1016-j-agrformet-2017-07-022.pdf",
        structures=("degree-day-phenology",),
        calibrated_on=("ramos2017.penedes",),
    ),
    "fraga2016.monthly_regression": Formulation(
        "Budburst, flowering and veraison dates as linear functions of monthly temperature"
        " means, per variety",
        (
            "Fraga, Santos et al. 2016, J. Agric. Sci. 154: 795-811, Eqs 1-6 (p. 802) and"
            " Tables 5-7 (pp. 804-805)"
        ),
        year=2016,
        authors=(
            "Fraga, H.",
            "Santos, J. A.",
            "Moutinho-Pereira, J.",
            "Carlos, C.",
            "Silvestre, J.",
            "Eiras-Dias, J.",
            "Mota, T.",
            "Malheiro, A. C.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2015-fraga-10-1017-s0021859615000933.pdf",
        doi="10.1017/S0021859615000933",
        structures=("monthly-temperature-regression",),
        calibrated_on=("fraga2016.portugal",),
        calibration_note=(
            "Each variety's k, alpha and beta are least-squares fits of its own observed series"
            " (Table 1's years), with the predictors chosen by forward-backward stepwise selection"
            " on the calibration varieties Fernão-Pires (white) and Castelão (red), whose own"
            " coefficients are not printed. Leave-one-out R²cv and RMSE per variety are in the"
            " same tables: budburst 0.32-0.93 and 2.3-6.7 d, flowering 0.50-0.93 and 2.7-4.9"
            " d, veraison 0.51-0.91 and 2.4-5.6 d; the 16-variety means 0.71, 0.83 and 0.78."
            " Read 2026-10-13 in the page images (literature/fraga2016)."
        ),
        equations="monthly_regression",
        parameters=(
            Published("budburst.alvarinho.k", 123.68, "DOY", "Table 5, Eq. 1", "read"),
            Published("budburst.alvarinho.alpha", -6.1, "d/°C", "Table 5, Eq. 1", "read"),
            Published("flowering.alvarinho.k", 291.44, "DOY", "Table 5, Eq. 2", "read"),
            Published("flowering.alvarinho.alpha", -7.89, "d/°C", "Table 5, Eq. 2", "read"),
            Published("veraison.alvarinho.k", 457.65, "DOY", "Table 5, Eq. 3", "read"),
            Published("veraison.alvarinho.alpha", -14.27, "d/°C", "Table 5, Eq. 3", "read"),
            Published("veraison.alvarinho.beta", -3.54, "d/°C", "Table 5, Eq. 3", "read"),
            Published("budburst.encruzado.k", 123.39, "DOY", "Table 5, Eq. 1", "read"),
            Published("budburst.encruzado.alpha", -5.88, "d/°C", "Table 5, Eq. 1", "read"),
            Published("flowering.encruzado.k", 293.56, "DOY", "Table 5, Eq. 2", "read"),
            Published("flowering.encruzado.alpha", -8.07, "d/°C", "Table 5, Eq. 2", "read"),
            Published("veraison.encruzado.k", 401.28, "DOY", "Table 5, Eq. 3", "read"),
            Published("veraison.encruzado.alpha", -3.84, "d/°C", "Table 5, Eq. 3", "read"),
            Published("veraison.encruzado.beta", -7.01, "d/°C", "Table 5, Eq. 3", "read"),
            Published("budburst.rabigato.k", 123.31, "DOY", "Table 5, Eq. 1", "read"),
            Published("budburst.rabigato.alpha", -6.51, "d/°C", "Table 5, Eq. 1", "read"),
            Published("flowering.rabigato.k", 298.45, "DOY", "Table 5, Eq. 2", "read"),
            Published("flowering.rabigato.alpha", -8.25, "d/°C", "Table 5, Eq. 2", "read"),
            Published("veraison.rabigato.k", 458.63, "DOY", "Table 5, Eq. 3", "read"),
            Published("veraison.rabigato.alpha", -10.18, "d/°C", "Table 5, Eq. 3", "read"),
            Published("veraison.rabigato.beta", -6.05, "d/°C", "Table 5, Eq. 3", "read"),
            Published("budburst.riesling.k", 117.22, "DOY", "Table 5, Eq. 1", "read"),
            Published("budburst.riesling.alpha", -5.09, "d/°C", "Table 5, Eq. 1", "read"),
            Published("flowering.riesling.k", 305.29, "DOY", "Table 5, Eq. 2", "read"),
            Published("flowering.riesling.alpha", -8.69, "d/°C", "Table 5, Eq. 2", "read"),
            Published("veraison.riesling.k", 407.18, "DOY", "Table 5, Eq. 3", "read"),
            Published("veraison.riesling.alpha", -6.08, "d/°C", "Table 5, Eq. 3", "read"),
            Published("veraison.riesling.beta", -6.21, "d/°C", "Table 5, Eq. 3", "read"),
            Published("budburst.trincadeira_pratas.k", 111.42, "DOY", "Table 5, Eq. 1", "read"),
            Published("budburst.trincadeira_pratas.alpha", -5.42, "d/°C", "Table 5, Eq. 1", "read"),
            Published("flowering.trincadeira_pratas.k", 267.7, "DOY", "Table 5, Eq. 2", "read"),
            Published(
                "flowering.trincadeira_pratas.alpha", -6.79, "d/°C", "Table 5, Eq. 2", "read"
            ),
            Published("veraison.trincadeira_pratas.k", 439.08, "DOY", "Table 5, Eq. 3", "read"),
            Published(
                "veraison.trincadeira_pratas.alpha", -12.42, "d/°C", "Table 5, Eq. 3", "read"
            ),
            Published("veraison.trincadeira_pratas.beta", -4.3, "d/°C", "Table 5, Eq. 3", "read"),
            Published("budburst.viosinho.k", 120.1, "DOY", "Table 5, Eq. 1", "read"),
            Published("budburst.viosinho.alpha", -5.69, "d/°C", "Table 5, Eq. 1", "read"),
            Published("flowering.viosinho.k", 285.96, "DOY", "Table 5, Eq. 2", "read"),
            Published("flowering.viosinho.alpha", -7.8, "d/°C", "Table 5, Eq. 2", "read"),
            Published("veraison.viosinho.k", 456.85, "DOY", "Table 5, Eq. 3", "read"),
            Published("veraison.viosinho.alpha", -9.028, "d/°C", "Table 5, Eq. 3", "read"),
            Published("veraison.viosinho.beta", -6.99, "d/°C", "Table 5, Eq. 3", "read"),
            Published("budburst.loureiro.k", 108.52, "DOY", "Table 7, Eq. 1", "read"),
            Published("budburst.loureiro.alpha", -4.76, "d/°C", "Table 7, Eq. 1", "read"),
            Published("flowering.loureiro.k", 248.18, "DOY", "Table 7, Eq. 2", "read"),
            Published("flowering.loureiro.alpha", -5.34, "d/°C", "Table 7, Eq. 2", "read"),
            Published("veraison.loureiro.k", 350.71, "DOY", "Table 7, Eq. 3", "read"),
            Published("veraison.loureiro.alpha", -4.5, "d/°C", "Table 7, Eq. 3", "read"),
            Published("veraison.loureiro.beta", -4.37, "d/°C", "Table 7, Eq. 3", "read"),
            Published("budburst.borracal.k", 143.2, "DOY", "Table 6, Eq. 4", "read"),
            Published("budburst.borracal.alpha", -9.48, "d/°C", "Table 6, Eq. 4", "read"),
            Published("flowering.borracal.k", 309.2, "DOY", "Table 6, Eq. 5", "read"),
            Published("flowering.borracal.alpha", -9.05, "d/°C", "Table 6, Eq. 5", "read"),
            Published("veraison.borracal.k", 488.75, "DOY", "Table 6, Eq. 6", "read"),
            Published("veraison.borracal.alpha", -3.24, "d/°C", "Table 6, Eq. 6", "read"),
            Published("veraison.borracal.beta", -12.81, "d/°C", "Table 6, Eq. 6", "read"),
            Published("budburst.grenache.k", 125.83, "DOY", "Table 6, Eq. 4", "read"),
            Published("budburst.grenache.alpha", -7.44, "d/°C", "Table 6, Eq. 4", "read"),
            Published("flowering.grenache.k", 294.55, "DOY", "Table 6, Eq. 5", "read"),
            Published("flowering.grenache.alpha", -8.16, "d/°C", "Table 6, Eq. 5", "read"),
            Published("veraison.grenache.k", 586.18, "DOY", "Table 6, Eq. 6", "read"),
            Published("veraison.grenache.alpha", -7.23, "d/°C", "Table 6, Eq. 6", "read"),
            Published("veraison.grenache.beta", -12.78, "d/°C", "Table 6, Eq. 6", "read"),
            Published("budburst.jaen.k", 136.47, "DOY", "Table 6, Eq. 4", "read"),
            Published("budburst.jaen.alpha", -8.09, "d/°C", "Table 6, Eq. 4", "read"),
            Published("flowering.jaen.k", 300.48, "DOY", "Table 6, Eq. 5", "read"),
            Published("flowering.jaen.alpha", -8.3, "d/°C", "Table 6, Eq. 5", "read"),
            Published("veraison.jaen.k", 388.39, "DOY", "Table 6, Eq. 6", "read"),
            Published("veraison.jaen.alpha", -1.57, "d/°C", "Table 6, Eq. 6", "read"),
            Published("veraison.jaen.beta", -9.87, "d/°C", "Table 6, Eq. 6", "read"),
            Published("budburst.merlot.k", 137.69, "DOY", "Table 6, Eq. 4", "read"),
            Published("budburst.merlot.alpha", -8.69, "d/°C", "Table 6, Eq. 4", "read"),
            Published("flowering.merlot.k", 309.54, "DOY", "Table 6, Eq. 5", "read"),
            Published("flowering.merlot.alpha", -8.92, "d/°C", "Table 6, Eq. 5", "read"),
            Published("veraison.merlot.k", 554.83, "DOY", "Table 6, Eq. 6", "read"),
            Published("veraison.merlot.alpha", -5.62, "d/°C", "Table 6, Eq. 6", "read"),
            Published("veraison.merlot.beta", -13.94, "d/°C", "Table 6, Eq. 6", "read"),
            Published("budburst.pinot.k", 129.85, "DOY", "Table 6, Eq. 4", "read"),
            Published("budburst.pinot.alpha", -8.05, "d/°C", "Table 6, Eq. 4", "read"),
            Published("flowering.pinot.k", 302.3, "DOY", "Table 6, Eq. 5", "read"),
            Published("flowering.pinot.alpha", -8.84, "d/°C", "Table 6, Eq. 5", "read"),
            Published("veraison.pinot.k", 419.65, "DOY", "Table 6, Eq. 6", "read"),
            Published("veraison.pinot.alpha", -2.75, "d/°C", "Table 6, Eq. 6", "read"),
            Published("veraison.pinot.beta", -9.98, "d/°C", "Table 6, Eq. 6", "read"),
            Published("budburst.tinta_francisca.k", 147.38, "DOY", "Table 6, Eq. 4", "read"),
            Published("budburst.tinta_francisca.alpha", -9.53, "d/°C", "Table 6, Eq. 4", "read"),
            Published("flowering.tinta_francisca.k", 307.12, "DOY", "Table 6, Eq. 5", "read"),
            Published("flowering.tinta_francisca.alpha", -8.61, "d/°C", "Table 6, Eq. 5", "read"),
            Published("veraison.tinta_francisca.k", 396.83, "DOY", "Table 6, Eq. 6", "read"),
            Published("veraison.tinta_francisca.alpha", -1.89, "d/°C", "Table 6, Eq. 6", "read"),
            Published("veraison.tinta_francisca.beta", -9.6, "d/°C", "Table 6, Eq. 6", "read"),
            Published("budburst.touriga_franca.k", 100.15, "DOY", "Table 7, Eq. 4", "read"),
            Published("budburst.touriga_franca.alpha", -3.64, "d/°C", "Table 7, Eq. 4", "read"),
            Published("flowering.touriga_franca.k", 229.63, "DOY", "Table 7, Eq. 5", "read"),
            Published("flowering.touriga_franca.alpha", -5.25, "d/°C", "Table 7, Eq. 5", "read"),
            Published("veraison.touriga_franca.k", 318.28, "DOY", "Table 7, Eq. 6", "read"),
            Published("veraison.touriga_franca.alpha", -1.09, "d/°C", "Table 7, Eq. 6", "read"),
            Published("veraison.touriga_franca.beta", -7.19, "d/°C", "Table 7, Eq. 6", "read"),
        ),
        flags=(
            "White varieties: budburst on the mean of daily Tmin over February-March (Eq. 1),"
            " flowering on Tmax over March-April (Eq. 2), veraison on Tmin over March-July (alpha)"
            " and Tmax over March-April (beta) (Eq. 3). Red: Tmin over January-March (Eq. 4),"
            " Tmax over March-April (Eq. 5), Tmax over June-July (alpha) and Tmean over March-April"
            " (beta) (Eq. 6). The abstract names other veraison windows than the equations.",
            "A retrospective form: the veraison windows end in July, after some veraison dates;"
            " the paper calls it prediction, not a forecast in season. The authors say the"
            " models need local calibration; applied to Loureiro (Vinhos Verdes) and"
            " Touriga-Franca (Douro) the budburst R²cv fell to 0.32 and 0.38.",
            "Trincadeira-das-Pratas (white, Table 5) is keyed trincadeira_pratas to keep it apart"
            " from the red Trincadeira; Pinot is printed without its colour.",
            "Compared with a 10 °C degree-day model on the two calibration varieties (Table 4):"
            " budburst R²cv 0.63 and 0.69 against 0.40 and 0.48; veraison 0.77 and 0.88"
            " against 0.31 and 0.53.",
        ),
    ),
    "didevarasl2026.monthly_regression": Formulation(
        "Budburst, bloom and veraison of Cannonau as linear functions of monthly temperature"
        " and precipitation, chosen by PLS screening and stepwise regression",
        "Didevarasl et al. 2026, Int. J. Biometeorol. 70: 273, Table 4 (with Table 2's statistics)",
        year=2026,
        authors=(
            "Didevarasl, Ali",
            "Deiana, Pierfrancesco",
            "Spano, Donatella",
            "Costa Saura, Jose M.",
            "Mercenaro, Luca",
            "Nieddu, Giovanni",
            "Trabucco, Antonio",
        ),
        authors_complete=True,
        authors_from="read",
        checked="the publisher's HTML (phenology/didevarasl2026_ijb.html in the 2026-10-12 drop)",
        doi="10.1007/s00484-026-03312-3",
        structures=("monthly-temperature-regression",),
        calibrated_on=("didevarasl2026.sardinia",),
        calibration_note=(
            "Fitted to the 47, 42 and 29 stage dates with weather from a 2.2 km ERA5 downscaling,"
            " not stations. Predictors screened by PLS (VIP above 1, repeated) on all"
            " observations, then bidirectional stepwise by AIC; leave-one-out validation after"
            " the screening, which the authors say may flatter it. In-sample RMSE 7, 5.5 and 4.5"
            " d, R² 0.43, 0.58 and 0.55. Read 2026-10-13 in the HTML (literature/didevarasl2026)."
        ),
        equations="didevarasl2026",
        parameters=(
            Published("budburst.k", 12.468353, "DOY", "Table 4", "read"),
            Published("budburst.jun_prev_tmax", 1.520173, "d/°C", "Table 4", "read"),
            Published("budburst.oct_prev_tmin", 2.505555, "d/°C", "Table 4", "read"),
            Published("budburst.oct_prev_precip", -0.023587, "d/mm", "Table 4", "read"),
            Published("budburst.dec_prev_precip", 0.019851, "d/mm", "Table 4", "read"),
            Published("bloom.k", 302.06883, "DOY", "Table 4", "read"),
            Published("bloom.apr_tmax", -5.67263, "d/°C", "Table 4", "read"),
            Published("bloom.dec_prev_tmin", -1.32845, "d/°C", "Table 4", "read"),
            Published("bloom.apr_tmin", 4.32647, "d/°C", "Table 4", "read"),
            Published("bloom.may_tmin", -4.97576, "d/°C", "Table 4", "read"),
            Published("bloom.mar_precip", -0.21747, "d/mm", "Table 4", "read"),
            Published("bloom.jun_precip", -0.15103, "d/mm", "Table 4", "read"),
            Published("veraison.k", 349.783, "DOY", "Table 4", "read"),
            Published("veraison.apr_tmax", -7.723, "d/°C", "Table 4", "read"),
            Published("veraison.may_tmin", -4.739, "d/°C", "Table 4", "read"),
            Published("veraison.jul_tmin", -8.076, "d/°C", "Table 4", "read"),
            Published("veraison.apr_tmean", 7.469, "d/°C", "Table 4", "read"),
            Published("veraison.jul_tmean", 5.483, "d/°C", "Table 4", "read"),
        ),
        flags=(
            "Units are not printed: the temperatures are monthly means of daily maxima (TX),"
            " minima (TN) or means (TM) in °C and PR the month's precipitation, inferred;"
            " '-1' marks the previous calendar year.",
            "Table 2's caption says five variables a stage; the printed budburst line has four"
            " terms and the bloom line six.",
            "Against the paper's own threshold models (Table 1, in-sample): GDD 6 and 4 d for"
            " bloom and veraison; the regressions 5.5 and 4.5 d; for budburst CH_GDH 7 d against"
            " the regression's 7 d.",
        ),
    ),
    "pinarey2021.gdd": Formulation(
        "Budburst and flowering by degree-days from a fitted start day and base, per variety",
        "Piña-Rey et al. 2021, Plants 10: 502, Eqs 1-2 (p. 13) and Tables 2-3 (p. 6)",
        year=2021,
        authors=(
            "Piña-Rey, Alba",
            "Ribeiro, Helena",
            "Fernández-González, María",
            "Abreu, Ilda",
            "Rodríguez-Rajo, F. Javier",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2021-pina-rey-10-3390-plants10030502.pdf",
        doi="10.3390/plants10030502",
        structures=("degree-day-phenology",),
        calibrated_on=("pinarey2021.ribeiro",),
        calibration_note=(
            "t0, Tb and F* fitted per variety and stage by simulated annealing in the"
            " Phenological Modelling Platform (Chuine et al.) on the 2008-2019 dates; each"
            " variety's set then tested on the other three (Table 2). The sets kept are"
            " Treixadura's for budburst and Godello's for flowering (Table 3), within 3 days in"
            " 60 % and 81 % of the other varieties' cases. Read 2026-10-13 in the page images"
            " (literature/pinarey2021)."
        ),
        parameters=(
            Published("budburst.albarino.t0", 62, "DOY", "Table 2 (p. 6)", "read"),
            Published("budburst.albarino.tb", 8, "°C", "Table 2 (p. 6)", "read"),
            Published("budburst.godello.t0", 49, "DOY", "Table 2 (p. 6)", "read"),
            Published("budburst.godello.tb", 5, "°C", "Table 2 (p. 6)", "read"),
            Published("budburst.loureira.t0", 79, "DOY", "Table 2 (p. 6)", "read"),
            Published("budburst.loureira.tb", 10, "°C", "Table 2 (p. 6)", "read"),
            Published("budburst.treixadura.t0", 49, "DOY", "Table 2 (p. 6)", "read"),
            Published("budburst.treixadura.tb", 5, "°C", "Table 2 (p. 6)", "read"),
            Published("flowering.albarino.t0", 27, "DOY", "Table 2 (p. 6)", "read"),
            Published("flowering.albarino.tb", 8, "°C", "Table 2 (p. 6)", "read"),
            Published("flowering.godello.t0", 52, "DOY", "Table 2 (p. 6)", "read"),
            Published("flowering.godello.tb", 6, "°C", "Table 2 (p. 6)", "read"),
            Published("flowering.loureira.t0", 71, "DOY", "Table 2 (p. 6)", "read"),
            Published("flowering.loureira.tb", 6, "°C", "Table 2 (p. 6)", "read"),
            Published("flowering.treixadura.t0", 52, "DOY", "Table 2 (p. 6)", "read"),
            Published("flowering.treixadura.tb", 7, "°C", "Table 2 (p. 6)", "read"),
            Published("budburst.treixadura.f_star", 228.503, "°C·d", "Table 3 (p. 6)", "read"),
            Published("flowering.godello.f_star", 626.092, "°C·d", "Table 3 (p. 6)", "read"),
        ),
        flags=(
            "Albariño's flowering Tb is 7 °C in Table 1 and the text but 8 °C in Table 2;"
            " Loureira's flowering t0 is 72 in Table 1 and 71 in Table 2.",
            "The triangular and UniFORC forms (Table 1) fitted no better; the GDD form was kept"
            " for its fewer parameters.",
        ),
    ),
    "ramos2018.gdd": Formulation(
        "Budbreak, bloom, véraison and maturity by degree-days from 20 March with a fitted base"
        " per stage, and a water term",
        (
            "Ramos, Jones & Yuste 2018, OENO One 52(1): 31-44, sections 3.1-3.2 (pp. 36-38) and"
            " Table 3 (p. 38)"
        ),
        year=2018,
        authors=("Ramos, M. Concepción", "Jones, Gregory V.", "Yuste, Jesús"),
        authors_complete=True,
        authors_from="read",
        checked="2018-ramos-10-20870-oeno-one-2018-52-1-2119.pdf",
        doi="10.20870/oeno-one.2018.52.1.2119",
        structures=("degree-day-phenology",),
        calibrated_on=("ramos2018.ribera",),
        calibration_note=(
            "The 20 March start comes from a partial least squares regression of budbreak on"
            " 10-day chill and heat units (Fig. 2); each stage's base temperature was then"
            " chosen to minimise the standard deviation of the degree-day sum over the 2004-2015"
            " dates (after Zapata et al. 2017), and the sums' means are the thresholds. The RMSE"
            " (budbreak 5.2-7.3 d, bloom 3.8-7.6, véraison 5.1-7.0, maturity 8.9-12.2) is"
            " in-sample. The water slopes are stepwise regressions of each plot's bloom and"
            " véraison dates on P minus ETc over 15 April to 30 May (R² 0.46-0.84). Read"
            " 2026-10-13 in the page images (literature/ramos2018)."
        ),
        parameters=(
            Published("budbreak.tempranillo.tb", 3.8, "°C", "p. 36 and p. 38, text", "read"),
            Published("budbreak.cabernet_sauvignon.tb", 4.7, "°C", "p. 36 and p. 38, text", "read"),
            Published("bloom.tempranillo.tb", 6.4, "°C", "p. 36 and p. 38, text", "read"),
            Published("bloom.cabernet_sauvignon.tb", 7.2, "°C", "p. 36 and p. 38, text", "read"),
            Published("veraison.tempranillo.tb", 13.4, "°C", "p. 36 and p. 38, text", "read"),
            Published(
                "veraison.cabernet_sauvignon.tb", 13.4, "°C", "p. 36 and p. 38, text", "read"
            ),
            Published("maturity.tempranillo.tb", 9.2, "°C", "p. 36 and p. 38, text", "read"),
            Published(
                "maturity.cabernet_sauvignon.tb", 10.5, "°C", "p. 36 and p. 38, text", "read"
            ),
            Published(
                "budbreak.tempranillo.gdd",
                250,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "bloom.tempranillo.gdd",
                425,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "veraison.tempranillo.gdd",
                398,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "maturity.tempranillo.gdd",
                410,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "budbreak.cabernet_sauvignon.gdd",
                205,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "bloom.cabernet_sauvignon.gdd",
                395,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "veraison.cabernet_sauvignon.gdd",
                386,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "maturity.cabernet_sauvignon.gdd",
                372,
                "°C·d",
                "p. 38, text (mean; the SD is printed)",
                "read",
            ),
            Published(
                "bloom.pa_cs.water_slope",
                0.18,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "bloom.pa_t.water_slope",
                0.17,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "bloom.pb_cs.water_slope",
                0.14,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "bloom.pb_t.water_slope",
                0.18,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "veraison.pa_cs.water_slope",
                0.16,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "veraison.pa_t.water_slope",
                0.16,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "veraison.pb_cs.water_slope",
                0.09,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
            Published(
                "veraison.pb_t.water_slope",
                0.12,
                "d/mm",
                "Table 3 (p. 38), P-ETc 15 Apr-30 May",
                "read",
            ),
        ),
        flags=(
            "The thresholds are printed as mean ± SD (Tempranillo budbreak 250 ± 45 °C·d); the"
            " SD is the spread over the twelve seasons, so a sum to the mean is the model.",
            "The discussion gives budbreak bases of 3.3-3.7 °C against the Results' 3.8 and 4.7"
            " °C; the footer prints 2017 for a 2018 issue.",
            "Degree-days capped at a 26 °C optimum (Parker et al. 2011) and the water slopes'"
            " intercepts are not printed.",
        ),
    ),
    "pola2017.monthly_regression": Formulation(
        "Goethe's budburst from the June-August mean, and the next stages' lengths from hours"
        " in a temperature band",
        (
            "Pola, Della Bruna, Back & Moreto 2017, Rev. Ciênc. Agrár. 40(1): 236-245, Quadro 2"
            " (p. 240) and Quadro 3 (p. 243)"
        ),
        year=2017,
        authors=(
            "Pola, Augusto C.",
            "Della Bruna, Emílio",
            "Back, Álvaro J.",
            "Moreto, Alexsander L.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="pola2017_rca.pdf (the 2026-10-12 drop's phenology folder)",
        doi="10.19084/RCA16061",
        structures=("monthly-temperature-regression",),
        calibrated_on=("pola2017.urussanga",),
        calibration_note=(
            "Least-squares lines on seven seasons, no hold-out: budburst (days from 1 August) on"
            " the July, June-July or June-August mean (R² 0.62, 0.72, 0.88; Se 3.5, 3.0, 2.0 d);"
            " budburst-to-bloom length on hours at 19-25 °C (nh) or 22-25 °C (NH) in the first 14"
            " days (R² 0.83, 0.90); bloom-to-harvest on the same counts over 30 to 70 days"
            " (R² 0.58-0.67). The sum of the same form as monthly_regression.stage_doy. Read"
            " 2026-10-13 in the page images (literature/pola2017)."
        ),
        parameters=(
            Published("budburst.jul.k", 82.65, "d from 1 Aug", "Quadro 2, eq. 6 (p. 240)", "read"),
            Published("budburst.jul.alpha", -2.98, "d/°C", "Quadro 2, eq. 6 (p. 240)", "read"),
            Published(
                "budburst.jun_jul.k", 116.1, "d from 1 Aug", "Quadro 2, eq. 7 (p. 240)", "read"
            ),
            Published("budburst.jun_jul.alpha", -5.24, "d/°C", "Quadro 2, eq. 7 (p. 240)", "read"),
            Published(
                "budburst.jun_aug.k", 157.34, "d from 1 Aug", "Quadro 2, eq. 8 (p. 240)", "read"
            ),
            Published("budburst.jun_aug.alpha", -7.87, "d/°C", "Quadro 2, eq. 8 (p. 240)", "read"),
            Published("budburst_to_bloom.nh14.k", 51.2, "d", "Quadro 3, eq. 10 (p. 243)", "read"),
            Published(
                "budburst_to_bloom.nh14.alpha", -0.17, "d/h", "Quadro 3, eq. 10 (p. 243)", "read"
            ),
            Published("budburst_to_bloom.NH14.k", 46.17, "d", "Quadro 3, eq. 9 (p. 243)", "read"),
            Published(
                "budburst_to_bloom.NH14.alpha", -0.4, "d/h", "Quadro 3, eq. 9 (p. 243)", "read"
            ),
            Published("bloom_to_harvest.nh30.k", 166.7, "d", "Quadro 3, eq. 12 (p. 243)", "read"),
            Published(
                "bloom_to_harvest.nh30.alpha", -0.18, "d/h", "Quadro 3, eq. 12 (p. 243)", "read"
            ),
            Published("bloom_to_harvest.nh70.k", 220.4, "d", "Quadro 3, eq. 15 (p. 243)", "read"),
            Published(
                "bloom_to_harvest.nh70.alpha", -0.14, "d/h", "Quadro 3, eq. 15 (p. 243)", "read"
            ),
        ),
        flags=(
            "A hybrid (Goethe) in humid subtropical Brazil (Urussanga, 19.4 °C mean, 234 chill"
            " hours a year), budburst in September: the signs and slopes transfer, the numbers"
            " do not.",
            "Hours in a band come from hourly temperatures interpolated between four daily"
            " readings; the daily mean is INMET's (Tmax + Tmin + T9 + 2 T21)/5.",
        ),
    ),
    "ruml2016.monthly_regression": Formulation(
        "Stage onsets of 20 cultivars as lines in the mean or maximum temperature of a period"
        " before the stage",
        "Ruml, Korać, Vujadinović, Vuković & Ivanišević 2016, J. Agric. Sci. 154: 186-206, Table 8",
        year=2016,
        authors=(
            "Ruml, M.",
            "Korać, N.",
            "Vujadinović, M.",
            "Vuković, A.",
            "Ivanišević, D.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="ruml2015_jas.pdf (the 2026-10-12 drop's phenology folder)",
        doi="10.1017/S0021859615000453",
        structures=("monthly-temperature-regression",),
        calibrated_on=("ruml2016.karlovci",),
        calibration_note=(
            "Onset date = k + alpha * T, T the mean daily temperature from 1 March to the onset"
            " (budburst), the daily maximum from 15 April to the onset (flowering), or the"
            " maximum over 1 April to 30 June (veraison) and 1 April to 31 August (harvest); the"
            " period was picked by correlation on the same 1986-2007 data and no hold-out is"
            " reported. R² 0.71, 0.85, 0.90 and 0.90 for the average cultivar. The catalogue"
            " holds the average and four international cultivars of Table 8's twenty. Read"
            " 2026-10-13 in the page image (literature/ruml2016)."
        ),
        parameters=(
            Published("budburst.average.alpha", -3.6, "d/°C", "Table 8 (p. 200)", "read"),
            Published("budburst.average.k", 133.0, "DOY", "Table 8 (p. 200)", "read"),
            Published("flowering.average.alpha", -3.1, "d/°C", "Table 8 (p. 200)", "read"),
            Published("flowering.average.k", 217.1, "DOY", "Table 8 (p. 200)", "read"),
            Published("veraison.average.alpha", -5.2, "d/°C", "Table 8 (p. 200)", "read"),
            Published("veraison.average.k", 332.9, "DOY", "Table 8 (p. 200)", "read"),
            Published("harvest.average.alpha", -7.4, "d/°C", "Table 8 (p. 200)", "read"),
            Published("harvest.average.k", 442.3, "DOY", "Table 8 (p. 200)", "read"),
            Published(
                "budburst.cabernet_sauvignon.alpha", -2.6, "d/°C", "Table 8 (p. 200)", "read"
            ),
            Published("budburst.cabernet_sauvignon.k", 130.0, "DOY", "Table 8 (p. 200)", "read"),
            Published(
                "flowering.cabernet_sauvignon.alpha", -2.9, "d/°C", "Table 8 (p. 200)", "read"
            ),
            Published("flowering.cabernet_sauvignon.k", 214.1, "DOY", "Table 8 (p. 200)", "read"),
            Published(
                "veraison.cabernet_sauvignon.alpha", -5.0, "d/°C", "Table 8 (p. 200)", "read"
            ),
            Published("veraison.cabernet_sauvignon.k", 322.9, "DOY", "Table 8 (p. 200)", "read"),
            Published("harvest.cabernet_sauvignon.alpha", -7.8, "d/°C", "Table 8 (p. 200)", "read"),
            Published("harvest.cabernet_sauvignon.k", 462.9, "DOY", "Table 8 (p. 200)", "read"),
            Published("budburst.merlot.alpha", -3.3, "d/°C", "Table 8 (p. 200)", "read"),
            Published("budburst.merlot.k", 132.6, "DOY", "Table 8 (p. 200)", "read"),
            Published("flowering.merlot.alpha", -3.2, "d/°C", "Table 8 (p. 200)", "read"),
            Published("flowering.merlot.k", 219.4, "DOY", "Table 8 (p. 200)", "read"),
            Published("veraison.merlot.alpha", -5.8, "d/°C", "Table 8 (p. 200)", "read"),
            Published("veraison.merlot.k", 342.6, "DOY", "Table 8 (p. 200)", "read"),
            Published("harvest.merlot.alpha", -8.5, "d/°C", "Table 8 (p. 200)", "read"),
            Published("harvest.merlot.k", 480.4, "DOY", "Table 8 (p. 200)", "read"),
            Published("budburst.chardonnay.alpha", -4.4, "d/°C", "Table 8 (p. 200)", "read"),
            Published("budburst.chardonnay.k", 134.4, "DOY", "Table 8 (p. 200)", "read"),
            Published("flowering.chardonnay.alpha", -3.4, "d/°C", "Table 8 (p. 200)", "read"),
            Published("flowering.chardonnay.k", 219.5, "DOY", "Table 8 (p. 200)", "read"),
            Published("veraison.chardonnay.alpha", -5.1, "d/°C", "Table 8 (p. 200)", "read"),
            Published("veraison.chardonnay.k", 319.1, "DOY", "Table 8 (p. 200)", "read"),
            Published("harvest.chardonnay.alpha", -8.3, "d/°C", "Table 8 (p. 200)", "read"),
            Published("harvest.chardonnay.k", 459.0, "DOY", "Table 8 (p. 200)", "read"),
            Published("budburst.pinot_noir.alpha", 4.0, "d/°C", "Table 8 (p. 200)", "read"),
            Published("budburst.pinot_noir.k", 134.3, "DOY", "Table 8 (p. 200)", "read"),
            Published("flowering.pinot_noir.alpha", -3.2, "d/°C", "Table 8 (p. 200)", "read"),
            Published("flowering.pinot_noir.k", 217.4, "DOY", "Table 8 (p. 200)", "read"),
            Published("veraison.pinot_noir.alpha", -5.4, "d/°C", "Table 8 (p. 200)", "read"),
            Published("veraison.pinot_noir.k", 322.7, "DOY", "Table 8 (p. 200)", "read"),
            Published("harvest.pinot_noir.alpha", -10.5, "d/°C", "Table 8 (p. 200)", "read"),
            Published("harvest.pinot_noir.k", 521.3, "DOY", "Table 8 (p. 200)", "read"),
        ),
        flags=(
            "The budburst and flowering windows end at the onset itself, so the fit is"
            " retrospective: the predictor is not known until the stage has happened.",
            "Pinot Noir's budburst slope is printed as 4.0 without a minus sign; the other"
            " nineteen cultivars and the average are negative.",
            "The summary's 74-90 % of variance explained overstates budburst (R² 0.71).",
        ),
    ),
    "schrader2020.days_remaining": Formulation(
        "Days remaining to budbreak from the date, soil thaw, photoperiod, heat and soil degree"
        " days and solar sum, refitted each day",
        (
            "Schrader, Domoto, Nonnecke & Cochran 2020, HortScience 55(12): 1912-1925, Table 6"
            " (p. 1923)"
        ),
        year=2020,
        authors=("Schrader, James A.", "Domoto, Paul A.", "Nonnecke, Gail R.", "Cochran, Diana R."),
        authors_complete=True,
        authors_from="read",
        checked="schrader2020_hortsci.pdf (the 2026-10-12 drop's phenology folder)",
        doi="10.21273/HORTSCI15367-20",
        structures=("days-remaining-regression",),
        calibrated_on=("schrader2020.iowa",),
        calibration_note=(
            "Elastic-net multiple regression (JMP) of days remaining on each day's predictors,"
            " all five cultivars pooled with a cultivar adjustment (Table 6 prints them: Marquette"
            " -1.98, Petit Ami 0.86, Frontenac -1.02, La Crescent -2.25, St. Croix 0). GDD10"
            " (hourly, no cap) and SDD5 (soil at 10.2 cm) are summed from soil thaw; solar in"
            " MJ/m². Training error 0.70 d (n 4,403 vine-days) against 5.27 d for cultivar plus"
            " GDD10 alone; validation on Marquette 2019, 1.92 d against 10.05 d. Bloom, veraison"
            " and harvest models are in the same table, not recorded here. Read 2026-10-13 in"
            " the page image (literature/schrader2020)."
        ),
        parameters=(
            Published(
                "budbreak.doy",
                -2.41136571255827,
                "d/d",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
            Published(
                "budbreak.soil_thaw_doy",
                0.152194171942409,
                "d/d",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
            Published(
                "budbreak.photoperiod",
                24.3727170859005,
                "d/h",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
            Published(
                "budbreak.gdd10_hourly",
                -0.134957195561917,
                "d/(°C·d)",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
            Published(
                "budbreak.sdd5",
                0.0804770431283008,
                "d/(°C·d)",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
            Published(
                "budbreak.solar_acc",
                0.0238725444616138,
                "d/(MJ/m2)",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
            Published(
                "budbreak.constant",
                -66.4256807364779,
                "d",
                "Table 6 (p. 1923), top budbreak model",
                "read",
            ),
        ),
        flags=(
            "A heat sum is among the predictors but no threshold triggers the prediction; the"
            " catalogue's first days-remaining form.",
            "Cold-climate hybrids in Iowa (chilling above 1,000 h every winter); three training"
            " seasons at one vineyard and one validation season.",
            "Units of the coefficients are not printed; those here are inferred from the"
            " predictors' definitions.",
        ),
    ),
    "chacon2021.gdd": Formulation(
        "Tempranillo and Chardonnay stages in La Mancha by degree-days from a PLS-chosen start"
        " with a fitted base per stage and a 22 °C cap",
        (
            "Chacón-Vozmediano, Martínez-Gascueña & Ramos 2021, Agron. Sustain. Dev. 41: 24,"
            " section 3.2 (p. 6) and Table 1"
        ),
        year=2021,
        authors=(
            "Chacón-Vozmediano, Juan Luis",
            "Martínez-Gascueña, Jesús",
            "Ramos, María Concepción",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2021-chacon-vozmediano-10-1007-s13593-021-00672-5.pdf",
        doi="10.1007/s13593-021-00672-5",
        structures=("degree-day-phenology",),
        calibrated_on=("chacon2021.lamancha",),
        calibration_note=(
            "Ramos 2017's method: the start from a PLS regression of bud break on 10-day chill"
            " and heat units, the base per stage by minimising the SD of the sum over the"
            " 2000-2019 dates, the sums' means as thresholds; RMSE in-sample (Tempranillo bud"
            " break 5.5 d, Willmott d 0.74). Read 2026-10-13 in the page image"
            " (literature/chacon2021)."
        ),
        parameters=(
            Published("budbreak.tempranillo.tb", 6.6, "°C", "section 3.2 (p. 6)", "read"),
            Published("bloom.tempranillo.tb", 6.4, "°C", "section 3.2 (p. 6)", "read"),
            Published("veraison.tempranillo.tb", 3.2, "°C", "section 3.2 (p. 6)", "read"),
            Published("maturity.tempranillo.tb", 12.5, "°C", "section 3.2 (p. 6)", "read"),
            Published("budbreak.chardonnay.tb", 0.0, "°C", "section 3.2 (p. 6)", "read"),
            Published("bloom.chardonnay.tb", 5.5, "°C", "section 3.2 (p. 6)", "read"),
            Published("veraison.chardonnay.tb", 1.1, "°C", "section 3.2 (p. 6)", "read"),
            Published("maturity.chardonnay.tb", 10.5, "°C", "section 3.2 (p. 6)", "read"),
            Published(
                "budbreak.tempranillo.gdd",
                180,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "bloom.tempranillo.gdd",
                431,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "veraison.tempranillo.gdd",
                1020,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "maturity.tempranillo.gdd",
                259,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "budbreak.chardonnay.gdd",
                276,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "bloom.chardonnay.gdd",
                479,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "veraison.chardonnay.gdd",
                1207,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published(
                "maturity.chardonnay.gdd",
                262,
                "°C·d",
                "section 3.2 (p. 6), mean (the SD is printed)",
                "read",
            ),
            Published("tmax_cap", 22.0, "°C", "section 3.2 (p. 6)", "read"),
            Published(
                "start_doy.tempranillo", 57, "DOY", "section 3.2 (p. 6): 26 February", "read"
            ),
            Published("start_doy.chardonnay", 70, "DOY", "section 3.2 (p. 6): 11 March", "read"),
        ),
        flags=(
            "Chardonnay's bud-break base is 0.0 °C and its veraison base 1.1 °C: the SD-minimising"
            " procedure drove them to the search bound.",
            "Projections use temperature only; the water index built for composition is not in"
            " the phenology model.",
        ),
    ),
    "caffarra2010.chardonnay": Formulation(
        "Chardonnay budburst by a bell-shaped chilling sum and a sigmoid forcing sum whose"
        " requirement falls with chilling, then flowering and veraison by the same forcing",
        (
            "Caffarra & Eccel 2010, Int. J. Biometeorol. 54: 255-267, Table 3 (p. 259) and"
            " Table 4 (p. 261)"
        ),
        year=2010,
        authors=("Caffarra, Amelia", "Eccel, Emanuele"),
        authors_complete=True,
        authors_from="read",
        checked="2010-caffarra-10-1007-s00484-009-0277-5.pdf",
        doi="10.1007/s00484-009-0277-5",
        borrows=("chuine2000.unified",),
        structures=("chilling-dormancy", "degree-day-phenology"),
        calibrated_on=("caffarra2010.conegliano",),
        calibration_note=(
            "ChillState = sum of 2 / (1 + exp(a (Tm - c)^2)) from 1 September; forcing from"
            " ChillState >= Ccrit as the sum of 1 / (1 + exp(-0.26 (Tm - 16.06))), the sigmoid"
            " fixed on Pouget 1968's Merlot data (Fig. 2); budburst when the forcing sum reaches"
            " Fcrit = co1 exp(co2 ChillState); flowering and veraison by the same forcing from"
            " the simulated previous stage to their own Fcrit. Six plus two parameters fitted by"
            " the Metropolis algorithm on Conegliano's 39 years, validated on four other series"
            " (budburst R² 0.36, flowering 0.79, veraison 0.69 within Conegliano; 33-52 % of the"
            " external variance beyond the site mean). Read 2026-10-13 in the page images"
            " (literature/caffarra2010)."
        ),
        parameters=(
            Published("chill.a", 0.005, "1/°C²", "Table 4 (p. 261)", "read"),
            Published("chill.c", 2.8, "°C", "Table 4 (p. 261)", "read"),
            Published(
                "forcing_requirement.co1", 176.26, "forcing units", "Table 4 (p. 261)", "read"
            ),
            Published(
                "forcing_requirement.co2", -0.015, "1/chilling unit", "Table 4 (p. 261)", "read"
            ),
            Published("chill.c_crit", 78.692, "chilling units", "Table 4 (p. 261)", "read"),
            Published("chill.t_c", 234, "d from 1 Sep", "Table 4 (p. 261)", "read"),
            Published("forcing.rate", 0.26, "1/°C", "Table 3, Eq. 2 (p. 259)", "read"),
            Published("forcing.t_half", 16.06, "°C", "Table 3, Eq. 2 (p. 259)", "read"),
            Published("flowering.f_crit", 24.71, "forcing units", "Table 4 (p. 261)", "read"),
            Published("veraison.f_crit", 51.146, "forcing units", "Table 4 (p. 261)", "read"),
        ),
        flags=(
            "The forcing response is Merlot's (Pouget 1968), not Chardonnay's; the chilling bell"
            " is a two-parameter cut of Chuine 2000's curve.",
            "Flowering and veraison were calibrated from simulated, not observed, starts; at"
            " Cembra (the mountain site) they ran late 85-91 % of the time.",
        ),
    ),
    "nendel2010.budbreak": Formulation(
        "Budbreak by single-triangle degree-days above a fitted threshold from a fitted start"
        " day, the pair chosen to minimise the heat sum's variation across years",
        "Nendel 2010, Int. J. Biometeorol. 54: 231-241, Eqs 1-6 (p. 232) and Table 1 (p. 235)",
        year=2010,
        authors=("Nendel, Claas",),
        authors_complete=True,
        authors_from="read",
        checked="2010-nendel-10-1007-s00484-009-0274-8.pdf",
        doi="10.1007/s00484-009-0274-8",
        structures=("degree-day-phenology",),
        calibrated_on=("nendel2010.coolwinter",),
        calibration_note=(
            "Start day (1-90) and threshold (0-12 °C) by minimising the coefficient of variation"
            " of the heat sum at budbreak (BBCH 09) across each site's years; the threshold read"
            " off the intersection of two lines fitted to the CV curve. Site values in Table 1"
            " (Riesling thresholds 5.2-6.5 °C, starts 14 February to 12 March, sums 166-242"
            " °C·d); the catalogue holds the means. Local parameters predict to about ±2.6"
            " (Riesling) and ±3.2 d (Müller-Thurgau); the general model leave-one-out ±4.6 d."
            " Read 2026-10-13 in the page image (literature/nendel2010)."
        ),
        parameters=(
            Published(
                "riesling.threshold",
                5.9,
                "°C",
                "Table 1 (p. 235), the mean row (1 March = day 60)",
                "read",
            ),
            Published(
                "riesling.start_doy",
                60,
                "DOY",
                "Table 1 (p. 235), the mean row (1 March = day 60)",
                "read",
            ),
            Published(
                "riesling.heat_sum",
                186.1,
                "°C·d",
                "Table 1 (p. 235), the mean row (1 March = day 60)",
                "read",
            ),
            Published(
                "muller_thurgau.threshold",
                5.9,
                "°C",
                "Table 1 (p. 235), the mean row (1 March = day 60)",
                "read",
            ),
            Published(
                "muller_thurgau.start_doy",
                60,
                "DOY",
                "Table 1 (p. 235), the mean row (1 March = day 60)",
                "read",
            ),
            Published(
                "muller_thurgau.heat_sum",
                180.3,
                "°C·d",
                "Table 1 (p. 235), the mean row (1 March = day 60)",
                "read",
            ),
        ),
        flags=(
            "Cool-winter sites only (Germany, France, Luxembourg, Slovakia, Czechia); sites 60"
            " km apart differ by more than 5 d. Four sites' BBCH 09 is BBCH 07 plus two days.",
            "Chilling algorithms (Cannell & Smith 1983, Cesaraccio et al. 2004) gave no gain,"
            " without printed numbers.",
        ),
    ),
    "chuine2000.unified": Formulation(
        "The Unified model: chilling and forcing sums with sigmoid responses, the forcing"
        " requirement falling with chilling",
        "Chuine 2000, J. Theor. Biol. 207: 337-347, as Caffarra & Eccel 2010 cite it; not held",
        year=2000,
        authors=("Chuine, Isabelle",),
        authors_from="trail",
        checked="Caffarra & Eccel 2010's references (held)",
        structures=("chilling-dormancy", "degree-day-phenology"),
    ),
    "ramos2022.gdd": Formulation(
        "Carignan's flowering, veraison and maturity in Rioja by degree-days from 15 March with"
        " a fitted base per stage, after 100 chill units",
        "Ramos & Martínez de Toda 2022, Int. J. Biometeorol. 66: 1067-1078, Results (p. 1071)",
        year=2022,
        authors=("Ramos, M. C.", "Martínez de Toda, F."),
        authors_complete=True,
        authors_from="read",
        checked="2022-ramos-10-1007-s00484-022-02258-6.pdf",
        doi="10.1007/s00484-022-02258-6",
        structures=("chilling-dormancy", "degree-day-phenology"),
        calibrated_on=("ramos2022.rioja",),
        calibration_note=(
            "Ramos 2017's method: chill portions (Dynamic Model) and degree hours from 1"
            " October, 100 chill units reached 15-25 March, heat from 15 March with the base per"
            " stage minimising the SD of the sum over 2008-2020, the sums' means as thresholds;"
            " RMSE 6.82, 5.16 and 8.71 d and Willmott d 0.57, 0.87, 0.68 on the same seasons."
            " The text also gives slopes of about 2.7 d of veraison and 3.65 d of maturity per"
            " °C of the previous period's mean, without equations. Read 2026-10-13 in the page"
            " image (literature/ramos2022)."
        ),
        parameters=(
            Published("flowers_separated.tb", 7.4, "°C", "Results, p. 1071", "read"),
            Published("veraison.tb", 6.3, "°C", "Results, p. 1071", "read"),
            Published("maturity.tb", 5.2, "°C", "Results, p. 1071", "read"),
            Published("flowers_separated.gdd", 1350, "°C·d", "Results, p. 1071", "read"),
            Published("veraison.gdd", 1690, "°C·d", "Results, p. 1071", "read"),
            Published("maturity.gdd", 2480, "°C·d", "Results, p. 1071", "read"),
            Published("start_doy", 74, "DOY", "Results, p. 1071: 15 March", "read"),
            Published("chill_threshold", 100, "CHU", "Methods (l. 175) and p. 1071", "read"),
            Published("tmax_cap", 26.0, "°C", "Methods (l. 182)", "read"),
        ),
        flags=(
            "The abstract's projected advances (5, 8, 11 d by 2050 under RCP4.5) differ from"
            " Table 3's (4, 6, 11); the flowering spread is 18 d in the abstract and 19 in the"
            " Results.",
            "The soil water that failed to move the dates is VSIM's, a model's.",
        ),
    ),
    "ramos2023.gdd": Formulation(
        "Verdejo, Viura and Sauvignon Blanc stages in Rueda by degree-days from 20 March with a"
        " fitted base per stage and variety",
        "Ramos & Yuste 2023, Agronomy 13: 146, Table 3 (p. 10)",
        year=2023,
        authors=("Ramos, María Concepción", "Yuste, Jesús"),
        authors_complete=True,
        authors_from="read",
        checked="2023-ramos-10-3390-agronomy13010146.pdf",
        doi="10.3390/agronomy13010146",
        structures=("degree-day-phenology",),
        calibrated_on=("ramos2023.rueda",),
        calibration_note=(
            "Ramos 2017's method with a 26 °C cap; the Verdejo set calibrated on two plots and"
            " validated on two others (RMSE 5.4, 3.7, 6.1 and 5.9 d for budbreak to ripening,"
            " Willmott d 0.84-1.0), Viura and Sauvignon Blanc on one plot each (RMSE 2.5-5.9"
            " d). Read 2026-10-13 in the page image (literature/ramos2023)."
        ),
        parameters=(
            Published("budbreak.verdejo.tb", 5.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "budbreak.verdejo.gdd",
                127,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("flowering.verdejo.tb", 5.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "flowering.verdejo.gdd",
                660,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("veraison.verdejo.tb", 5.8, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "veraison.verdejo.gdd",
                1765,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("ripening.verdejo.tb", 4.9, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "ripening.verdejo.gdd",
                2365,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("budbreak.viura.tb", 5.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "budbreak.viura.gdd",
                162,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("flowering.viura.tb", 5.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "flowering.viura.gdd",
                665,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("veraison.viura.tb", 5.7, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "veraison.viura.gdd",
                1882,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("ripening.viura.tb", 4.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "ripening.viura.gdd",
                2484,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("budbreak.sauvignon_blanc.tb", 6.1, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "budbreak.sauvignon_blanc.gdd",
                104,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("flowering.sauvignon_blanc.tb", 5.7, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "flowering.sauvignon_blanc.gdd",
                619,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("veraison.sauvignon_blanc.tb", 5.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "veraison.sauvignon_blanc.gdd",
                1593,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("ripening.sauvignon_blanc.tb", 3.4, "°C", "Table 3 (p. 10)", "read"),
            Published(
                "ripening.sauvignon_blanc.gdd",
                2471,
                "°C·d",
                "Table 3 (p. 10), mean (the SD is printed)",
                "read",
            ),
            Published("start_doy", 80, "DOY", "Table 3 caption: 20 March", "read"),
            Published("tmax_cap", 26.0, "°C", "Methods (l. 305)", "read"),
        ),
        flags=(
            "Table 3 calls the sums from DOY 80 cumulative to each stage, so the later"
            " thresholds include the earlier ones.",
            "Rueda is 700-930 m and dry (110 mm in the growing season); Table 4's projections"
            " reach 20-25 d of earlier ripening by 2050.",
        ),
    ),
    "ramos2023.regression": Formulation(
        "Rueda stage dates by stepwise regression on the previous period's temperature and"
        " water balance, with Verdejo's slopes printed",
        "Ramos & Yuste 2023, Agronomy 13: 146, Table 1 and section 3.3 (p. 8)",
        year=2023,
        authors=("Ramos, María Concepción", "Yuste, Jesús"),
        authors_complete=True,
        authors_from="read",
        checked="2023-ramos-10-3390-agronomy13010146.pdf",
        doi="10.3390/agronomy13010146",
        structures=("monthly-temperature-regression",),
        calibrated_on=("ramos2023.rueda",),
        calibration_note=(
            "Forward stepwise regressions (Statgraphics) of each stage's date on the mean,"
            " maximum and minimum temperature and P minus ETc of the period before it (from 20"
            " March to budbreak, then stage to stage). Table 1 prints only R² (Verdejo 0.51,"
            " 0.68, 0.45, 0.67; Viura 0.67, 0.56, 0.38, 0.60; Sauvignon Blanc 0.73, 0.47, 0.41,"
            " 0.55), the terms kept with their sign and share of variance; the text gives"
            " Verdejo's slopes: budbreak 6.6 d earlier per °C of the previous month's mean,"
            " flowering about 10, ripening about 4, veraison 1.6 d per °C of Tmin (0.5-2.7 by"
            " plot), and ripening 2.6 and veraison 1.9 d later per 10 mm of P minus ETc. No"
            " intercept, no validation. Read 2026-10-13 in the page image (literature/ramos2023)."
        ),
        parameters=(
            Published("budbreak.verdejo.alpha", -6.6, "d/°C", "section 3.3 (p. 8), text", "read"),
            Published(
                "veraison.verdejo.tmin_alpha", -1.6, "d/°C", "section 3.3 (p. 8), text", "read"
            ),
            Published(
                "veraison.verdejo.water", 0.19, "d/mm", "section 3.3: 1.9 d per 10 mm", "read"
            ),
            Published(
                "ripening.verdejo.water", 0.26, "d/mm", "section 3.3: 2.6 d per 10 mm", "read"
            ),
        ),
        flags=(
            "A sign-and-share table, not a model one can run: only the four Verdejo slopes above"
            " are printed as numbers, the 'about 10' and 'about 4' d per °C are not recorded.",
            "The budbreak window ends at budbreak; the period means are known only after the"
            " stage.",
        ),
    ),
    "parker2013.gfv": Formulation(
        "Flowering and veraison by degree-days above 0 °C from day 60 to a critical sum F* per"
        " variety (the GFV model), 95 and 104 varieties classified",
        "Parker et al. 2013, Agric. For. Meteorol. 180: 249-264, Eqs 1-2 (p. 252) and Tables 1-2",
        year=2013,
        authors=(
            "Parker, Amber",
            "Garcia de Cortázar-Atauri, Inaki",
            "Chuine, Isabelle",
            "Barbeau, Gérard",
            "Bois, Benjamin",
            "Boursiquot, Jean-Michel",
            "Cahurel, Jean-Yves",
            "Claverie, Marion",
            "Dufourcq, Thierry",
            "Gény, Laurence",
            "Guimberteau, Guy",
            "Hofmann, Rainer W.",
            "Jacquet, Olivier",
            "Lacombe, Thierry",
            "Monamy, Christine",
            "Ojeda, Hernan",
            "Panigai, Laurent",
            "Payan, Jean-Christophe",
            "Rodriquez Lovelle, Bernard",
            "Rouchaud, Eric",
            "Schneider, Christophe",
            "Spring, Jean-Laurent",
            "Storchi, Paolo",
            "Tomasi, Diego",
            "Trambouze, William",
            "Trought, Michael",
            "van Leeuwen, Cornelis",
        ),
        authors_complete=False,
        authors_from="trail",
        checked=(
            "2013-parker-10-1016-j-agrformet-2013-06-005.pdf (the author list from the reading"
            " agent's citation block, not re-read; Parker, Garcia de Cortázar-Atauri, Chuine and"
            " van Leeuwen confirmed in the page header)"
        ),
        doi="10.1016/j.agrformet.2013.06.005",
        structures=("degree-day-phenology",),
        calibrated_on=("parker2013.database",),
        calibration_note=(
            "F* fitted per variety by the Metropolis algorithm with t0 = day 60 and base 0 °C"
            " fixed from Parker et al. 2011; each variety's RMSE and efficiency are in the same"
            " tables (flowering RMSE under 7 d for all but one variety, veraison under 7 d for"
            " all but twelve; Tempranillo rests on one site, 5 and 11 observations). The"
            " catalogue holds thirteen of the varieties. Read 2026-10-13 in the page images"
            " (literature/parker2013)."
        ),
        parameters=(
            Published(
                "flowering.tempranillo.f_star", 1188, "°C·d", "Table 1 (pp. 251-252)", "read"
            ),
            Published("flowering.chardonnay.f_star", 1217, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.pinot_noir.f_star", 1219, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.riesling.f_star", 1249, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published(
                "flowering.cabernet_franc.f_star", 1245, "°C·d", "Table 1 (pp. 251-252)", "read"
            ),
            Published("flowering.merlot.f_star", 1269, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.chasselas.f_star", 1276, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.grenache.f_star", 1277, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.syrah.f_star", 1279, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.sauvignon.f_star", 1282, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("flowering.carignan.f_star", 1288, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published(
                "flowering.cabernet_sauvignon.f_star", 1299, "°C·d", "Table 1 (pp. 251-252)", "read"
            ),
            Published("flowering.mourvedre.f_star", 1354, "°C·d", "Table 1 (pp. 251-252)", "read"),
            Published("veraison.chasselas.f_star", 2374, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.tempranillo.f_star", 2484, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.pinot_noir.f_star", 2511, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.sauvignon.f_star", 2528, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.chardonnay.f_star", 2547, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.riesling.f_star", 2590, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.syrah.f_star", 2601, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.merlot.f_star", 2636, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published(
                "veraison.cabernet_sauvignon.f_star", 2689, "°C·d", "Table 2 (pp. 253-254)", "read"
            ),
            Published(
                "veraison.cabernet_franc.f_star", 2692, "°C·d", "Table 2 (pp. 253-254)", "read"
            ),
            Published("veraison.mourvedre.f_star", 2706, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.carignan.f_star", 2749, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("veraison.grenache.f_star", 2761, "°C·d", "Table 2 (pp. 253-254)", "read"),
            Published("t0", 60, "DOY", "Eq. 1-2 (p. 252)", "read"),
            Published("t_base", 0.0, "°C", "Eq. 2 (p. 252)", "read"),
        ),
        flags=(
            "Xarel·lo, Macabeo and Parellada are not among the 104 varieties; Grenache is"
            " 'Grenache' for flowering and 'Grenache noir' for veraison.",
            "The site effect quoted in the text for Syrah's veraison (13.96 %) is 3.28 % in"
            " Table 4.",
        ),
    ),
    "martinezluscher2016.sensitivity": Formulation(
        "Days of change per °C of the period's mean temperature for budburst, flowering and"
        " harvest intervals in Croatia",
        "Martínez-Lüscher et al. 2016, Front. Environ. Sci. 4: 48, Fig. 3 and p. 5",
        year=2016,
        authors=(
            "Martínez-Lüscher, Johann",
            "Kizildeniz, Tefide",
            "Vučetić, Višnja",
            "Dai, Zhanwu",
            "Luedeling, Eike",
            "van Leeuwen, Cornelis",
            "Gomès, Eric",
            "Pascual, Inmaculada",
            "Irigoyen, Juan J.",
            "Morales, Fermín",
            "Delrot, Serge",
        ),
        authors_complete=True,
        authors_from="read",
        checked="martinezluscher2016_fenvs.pdf (the 2026-10-12 drop's phenology folder)",
        doi="10.3389/fenvs.2016.00048",
        structures=("monthly-temperature-regression",),
        calibrated_on=("martinezluscher2016.croatia",),
        calibration_note=(
            "Linear regressions, all sites pooled, of each interval's length on its own mean"
            " temperature (Fig. 3); only the slopes are printed, no intercept, R² or n. A PLS of"
            " Riesling Italico's budburst at Mandicevac on daily chill portions and degree hours"
            " (Fig. 1) gave the windows: chilling 23 September to 27 February, warming 22 January"
            " to 1 May; an interpolated surface gives 0.03 d/°C for the chilling phase and -4.38"
            " d/°C for the warming phase. Read 2026-10-13 in the page image"
            " (literature/martinezluscher2016)."
        ),
        parameters=(
            Published("march_to_budburst.slope", -4.49, "d/°C", "p. 5, Fig. 3", "read"),
            Published("budburst_to_flowering.slope", -3.29, "d/°C", "p. 5, Fig. 3", "read"),
            Published("flowering_to_harvest.slope", -2.57, "d/°C", "p. 5, Fig. 3", "read"),
            Published("budburst.warming_phase.slope", -4.38, "d/°C", "p. 5, Fig. 2", "read"),
            Published("budburst.chilling_phase.slope", 0.03, "d/°C", "p. 5, Fig. 2", "read"),
        ),
        flags=(
            "The interval's own mean temperature is the predictor, so the line is read after the"
            " interval closes: a sensitivity, not a forecast.",
            "Weather is E-OBS gridded, not station; the greenhouse sensitivities (-1.5 to +0.2"
            " d/°C for Tempranillo in pots) are far smaller than the field ones.",
        ),
    ),
    "alleweldt1975.budburst": Formulation(
        "Riesling's budburst where the running sum of daily maxima from 15 March crosses a line"
        " rising with the days",
        "Alleweldt & Hofäcker 1975, Vitis 14: 103-115, p. 105 and the figure on p. 106",
        year=1975,
        authors=("Alleweldt, G.", "Hofäcker, W."),
        authors_complete=True,
        authors_from="read",
        checked="alleweldt1975_vitis.pdf (the 2026-10-12 drop's phenology folder)",
        structures=("degree-day-phenology",),
        calibrated_on=("alleweldt1975.flein",),
        calibration_note=(
            "Of the sums from 15 March to budburst, the daily maxima correlated best with the"
            " date (r 0.762, against 0.469 for the means above 0 °C, 0.296 for the minima and"
            " 0.541 for the 20 cm soil temperature); the regression of that sum (y, °C) on the"
            " days from 15 March (x) is y = 419.51 + 5.61 x, and budburst falls where a year's"
            " cumulative curve meets the line (the figure prints 419.519, r 0.762). Twelve"
            " site-years, deviations up to 5 d, no hold-out. Read 2026-10-13 in the page images"
            " (literature/alleweldt1975)."
        ),
        parameters=(
            Published(
                "line.intercept", 419.51, "°C", "p. 105 (419.519 in the figure, p. 106)", "read"
            ),
            Published("line.slope", 5.61, "°C/d", "p. 105", "read"),
            Published("start_doy", 74, "DOY", "p. 105: 15 March", "read"),
            Published("flowering.tmax_sum_after_budburst", 850, "°C", "p. 110", "read"),
            Published("flowering.t0_sum_after_budburst", 550, "°C", "p. 110", "read"),
        ),
        flags=(
            "A heat sum against a threshold that rises 5.61 °C a day: the sum of maxima, with no"
            " base, counts cold days too, which the authors say is why a fixed sum fails here.",
            "The soil temperature at 20 cm (r 0.541) is the only soil-temperature correlation"
            " the search found printed; it is not in the forecast.",
            "The authors infer from two pairs of years that budburst speeds up above 7-8 °C; no"
            " base temperature is fitted.",
        ),
    ),
    "garciatejera2022.spring_warming": Formulation(
        "Bud break, bloom, fruit set and veraison by the Spring Warming sum from 1 January to a"
        " critical sum per site and cultivar, run on daily or on monthly mean temperatures",
        (
            "García-Tejera et al. 2022, OENO One 56(4): 173-183, Eqs 1-5 (pp. 174-175) and Table 2"
            " (p. 178)"
        ),
        year=2022,
        authors=(
            "Garcia-Tejera, Omar",
            "Marcos-Matamoros, Raül",
            "Basile, Boris",
            "Mataffo, Alessandro",
            "Scognamiglio, Pasquale",
            "Prieto, Henar",
            "Mancha, Luis",
            "Cabral, Inês",
            "Queiroz, Jorge",
            "Valente, Joana",
            "Alves, Fernando",
            "González-Reviriego, Nube",
            "Hernández-Barrera, Sara",
            "Mata, Mercè",
        ),
        authors_complete=False,
        authors_from="read",
        checked=(
            "garciatejera2022_oeno.pdf (the 2026-10-12 drop's phenology folder); the author list"
            " as the reading agent transcribed it, cut at the fourteenth name"
        ),
        doi="10.20870/oeno-one.2022.56.4.5401",
        structures=("degree-day-phenology",),
        calibrated_on=("garciatejera2022.plots",),
        calibration_note=(
            "F* per site, cultivar and stage by inverse modelling of the daily Spring Warming"
            " sum (Hunter & Lechowicz 1992) with Tb 3.5 °C to bud break and 7.1 °C after, from"
            " Moncur et al. 1989, t0 1 January; the same F* then run on monthly means through"
            " the downscaling approach (Eqs 3-5): the month's rate (Tm - Tb) times the effective"
            " days n_days [1 - cdf(Tb; Tm, sigma_Tm)], the normal cdf from each site's"
            " historical records (sigma not printed). RMSD over all sites: daily 5.4, 5.0, 6.0,"
            " 6.4 d and monthly 6.7, 4.4, 6.0, 5.9 d for the four stages (Table 3); the two"
            " agree (slope 1.00, intercept -2.32, R² 0.99, Fig. 5). Read 2026-10-13 in the page"
            " images (literature/garciatejera2022)."
        ),
        parameters=(
            Published(
                "bud_break.raimat.tempranillo.f_star", 345, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published("bloom.raimat.tempranillo.f_star", 425, "°C·d", "Table 2 (p. 178)", "read"),
            Published(
                "fruit_set.raimat.tempranillo.f_star", 525, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "veraison.raimat.tempranillo.f_star", 1443, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "bud_break.raimat.chardonnay.f_star", 274, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published("bloom.raimat.chardonnay.f_star", 436, "°C·d", "Table 2 (p. 178)", "read"),
            Published(
                "fruit_set.raimat.chardonnay.f_star", 530, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "veraison.raimat.chardonnay.f_star", 1489, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "bud_break.vilarica.touriga_nacional.f_star",
                499,
                "°C·d",
                "Table 2 (p. 178)",
                "read",
            ),
            Published(
                "bloom.vilarica.touriga_nacional.f_star", 428, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "fruit_set.vilarica.touriga_nacional.f_star",
                525,
                "°C·d",
                "Table 2 (p. 178)",
                "read",
            ),
            Published(
                "veraison.vilarica.touriga_nacional.f_star",
                1648,
                "°C·d",
                "Table 2 (p. 178)",
                "read",
            ),
            Published(
                "bud_break.laorden.tempranillo.f_star", 514, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published("bloom.laorden.tempranillo.f_star", 434, "°C·d", "Table 2 (p. 178)", "read"),
            Published(
                "fruit_set.laorden.tempranillo.f_star", 636, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "veraison.laorden.tempranillo.f_star", 1430, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "bud_break.mirabella.aglianico.f_star", 534, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published("bloom.mirabella.aglianico.f_star", 478, "°C·d", "Table 2 (p. 178)", "read"),
            Published(
                "fruit_set.mirabella.aglianico.f_star", 718, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "veraison.mirabella.aglianico.f_star", 1954, "°C·d", "Table 2 (p. 178)", "read"
            ),
            Published(
                "t_base.bud_break",
                3.5,
                "°C",
                "section 4 (p. 175), after Moncur et al. 1989",
                "read",
            ),
            Published(
                "t_base.later_stages",
                7.1,
                "°C",
                "section 4 (p. 175), after Moncur et al. 1989",
                "read",
            ),
            Published("t0", 1, "DOY", "section 4 (p. 175): 1 January", "read"),
        ),
        flags=(
            "Raïmat is in Lleida, the nearest published Tempranillo and Chardonnay F* to the"
            " Penedès; four seasons (2017-2020) behind each F* there.",
            "A heat sum to a threshold driven by monthly means: Chris's monthly-mean theme in a"
            " threshold model, with 4-7 d of error either way.",
            "Raïmat's 2017 and 2019 had a monthly mean below Tb (the only such cases); La Orden"
            " 2017 missed fruit set and veraison by 21 and 17 d in both models.",
        ),
    ),
    "mesa2024.gdd": Formulation(
        "Catalan vineyard stages by degree-days from 1 January to fixed sums, used over the"
        " Empordà, Pla de Bages and Penedès PDOs",
        "Funes Mesa et al. 2024, OENO One 58(4), section 3.2 (p. 6)",
        year=2024,
        authors=(
            "Funes Mesa, Inmaculada",
            "Sánchez-Costa, Elisenda",
            "Aranda, Xavier",
            "Altava-Ortiz, Vicent",
            "Barrera-Escoda, Antoni",
            "Prohom, Marc",
            "Poyatos, Rafael",
        ),
        authors_complete=False,
        authors_from="read",
        checked=(
            "2024-mesa-10-20870-oeno-one-2024-58-4-7789.pdf (the first seven authors as printed;"
            " the list continues)"
        ),
        doi="10.20870/oeno-one.2024.58.4.7789",
        structures=("degree-day-phenology",),
        calibration_note=(
            "The sums rest on 'several phenological records (following the BBCH scale) over"
            " Catalonia from a few varieties (data not shown)', by the method of Ramos et al."
            " 2008; no dataset, variety or error is printed, so nothing is recorded as"
            " calibration data. Read 2026-10-13 in the page image (literature/mesa2024)."
        ),
        parameters=(
            Published(
                "t_base", 10.0, "°C", "section 3.2 (p. 6), after Winkler et al. 1974", "read"
            ),
            Published(
                "t_opt", 25.0, "°C", "section 3.2 (p. 6), after Anderson et al. 1986", "read"
            ),
            Published("t_top_as_printed", 3.0, "°C", "section 3.2 (p. 6): 'Tmax = 3 °C'", "read"),
            Published("budbreak.gdd", 406, "°C·d", "section 3.2 (p. 6), from 1 January", "read"),
            Published("flowering.gdd", 517, "°C·d", "section 3.2 (p. 6), from 1 January", "read"),
            Published("fruit_set.gdd", 798, "°C·d", "section 3.2 (p. 6), from 1 January", "read"),
            Published("pea_size.gdd", 1322, "°C·d", "section 3.2 (p. 6), from 1 January", "read"),
            Published("harvest.gdd", 1962, "°C·d", "section 3.2 (p. 6), from 1 January", "read"),
            Published("dormancy_restart.gdd", 107, "°C·d", "section 3.2 (p. 6)", "read"),
        ),
        flags=(
            "The upper threshold prints as 'Tmax = 3 °C', an evident misprint (Anderson et al."
            " 1986's sour-cherry model uses 36 °C); recorded as printed, not corrected.",
            "A single Catalan parameter set for every variety and PDO, with the data behind it"
            " unpublished: a regional default, not a fitted model. Table 2's Penedès baseline"
            " cycle of 287 d implies a budburst near 1 January, unexplained.",
            "Projections (MPI-ESM downscaled to 1 km, RCP4.5 and 8.5): flowering 8-45 d and the"
            " budburst-to-harvest cycle 7-68 d shorter by the 2090s; net water needs two to"
            " four times today's.",
        ),
    ),
    "pouget1988.budburst": Formulation(
        "Budburst when the sum from 1 January of each day's bud action, K t^c at the daily"
        " maximum and minimum averaged, reaches a cultivar constant S",
        (
            "Pouget 1988, Connaissance de la Vigne et du Vin 22: 105-123, pp. 107-111 (the rate"
            " law, the daily action and the sum) and Table VII (p. 116)"
        ),
        year=1988,
        authors=("Pouget, R.",),
        authors_complete=True,
        authors_from="read",
        checked="pouget1988_oeno.pdf (the 2026-10-12 drop's phenology folder; a scan, OCR'd)",
        structures=("degree-day-phenology",),
        calibrated_on=("pouget1988.bordeaux",),
        calibration_note=(
            "The rate of budburst V = 1000 / (days to 50 % budburst) follows V = K t^c between 5"
            " and 25 °C, from growth-chamber tests (Pouget 1967, 1969); the day's action is the"
            " mean of the actions at the maximum and the minimum, positive temperatures only,"
            " summed from 1 January at Bordeaux; budburst comes when the sum nears S, observed"
            " for the four references over 1961-1987 (Table V: Perle de Csaba 1,788 ± 38,"
            " Traminer 1,585 ± 41, Merlot 1,255 ± 12, Ugni blanc 1,089 ± 15). The other"
            " cultivars' S, c, K and threshold come from the fitted relations between the"
            " references' S and mean budburst day, c and S, log K and c, and threshold and c."
            " The threshold is the temperature at which V = 20 (50 days). Table VII read"
            " 2026-10-13 in the page image; the relations at their OCR lines"
            " (literature/pouget1988)."
        ),
        parameters=(
            Published(
                "perle_de_csaba.mean_budburst_day",
                63.5,
                "d from 1 Jan",
                "Table VII (p. 116)",
                "read",
            ),
            Published("perle_de_csaba.s", 1788, "action units", "Table VII (p. 116)", "read"),
            Published("perle_de_csaba.c", 1.285, "1", "Table VII (p. 116)", "read"),
            Published("perle_de_csaba.k", 2.27, "1", "Table VII (p. 116)", "read"),
            Published("perle_de_csaba.threshold", 5.6, "°C", "Table VII (p. 116)", "read"),
            Published(
                "chardonnay.mean_budburst_day", 66.89, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("chardonnay.s", 1703, "action units", "Table VII (p. 116)", "read"),
            Published("chardonnay.c", 1.345, "1", "Table VII (p. 116)", "read"),
            Published("chardonnay.k", 1.795, "1", "Table VII (p. 116)", "read"),
            Published("chardonnay.threshold", 6.1, "°C", "Table VII (p. 116)", "read"),
            Published(
                "traminer.mean_budburst_day", 72.12, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("traminer.s", 1585, "action units", "Table VII (p. 116)", "read"),
            Published("traminer.c", 1.442, "1", "Table VII (p. 116)", "read"),
            Published("traminer.k", 1.214, "1", "Table VII (p. 116)", "read"),
            Published("traminer.threshold", 7.0, "°C", "Table VII (p. 116)", "read"),
            Published(
                "chasselas.mean_budburst_day", 74.39, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("chasselas.s", 1475, "action units", "Table VII (p. 116)", "read"),
            Published("chasselas.c", 1.542, "1", "Table VII (p. 116)", "read"),
            Published("chasselas.k", 0.821, "1", "Table VII (p. 116)", "read"),
            Published("chasselas.threshold", 8.0, "°C", "Table VII (p. 116)", "read"),
            Published(
                "gamay.mean_budburst_day", 75.72, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("gamay.s", 1434, "action units", "Table VII (p. 116)", "read"),
            Published("gamay.c", 1.578, "1", "Table VII (p. 116)", "read"),
            Published("gamay.k", 0.711, "1", "Table VII (p. 116)", "read"),
            Published("gamay.threshold", 8.3, "°C", "Table VII (p. 116)", "read"),
            Published(
                "pinot_noir.mean_budburst_day", 77.44, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("pinot_noir.s", 1382, "action units", "Table VII (p. 116)", "read"),
            Published("pinot_noir.c", 1.623, "1", "Table VII (p. 116)", "read"),
            Published("pinot_noir.k", 0.595, "1", "Table VII (p. 116)", "read"),
            Published("pinot_noir.threshold", 8.7, "°C", "Table VII (p. 116)", "read"),
            Published(
                "syrah.mean_budburst_day", 78.78, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("syrah.s", 1342, "action units", "Table VII (p. 116)", "read"),
            Published("syrah.c", 1.658, "1", "Table VII (p. 116)", "read"),
            Published("syrah.k", 0.518, "1", "Table VII (p. 116)", "read"),
            Published("syrah.threshold", 9.0, "°C", "Table VII (p. 116)", "read"),
            Published(
                "chenin.mean_budburst_day", 79.72, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("chenin.s", 1312, "action units", "Table VII (p. 116)", "read"),
            Published("chenin.c", 1.684, "1", "Table VII (p. 116)", "read"),
            Published("chenin.k", 0.467, "1", "Table VII (p. 116)", "read"),
            Published("chenin.threshold", 9.3, "°C", "Table VII (p. 116)", "read"),
            Published(
                "riesling.mean_budburst_day", 79.83, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("riesling.s", 1309, "action units", "Table VII (p. 116)", "read"),
            Published("riesling.c", 1.687, "1", "Table VII (p. 116)", "read"),
            Published("riesling.k", 0.461, "1", "Table VII (p. 116)", "read"),
            Published("riesling.threshold", 9.3, "°C", "Table VII (p. 116)", "read"),
            Published(
                "merlot.mean_budburst_day", 81.22, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("merlot.s", 1255, "action units", "Table VII (p. 116)", "read"),
            Published("merlot.c", 1.702, "1", "Table VII (p. 116)", "read"),
            Published("merlot.k", 0.444, "1", "Table VII (p. 116)", "read"),
            Published("merlot.threshold", 9.4, "°C", "Table VII (p. 116)", "read"),
            Published(
                "semillon.mean_budburst_day", 81.33, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("semillon.s", 1263, "action units", "Table VII (p. 116)", "read"),
            Published("semillon.c", 1.727, "1", "Table VII (p. 116)", "read"),
            Published("semillon.k", 0.394, "1", "Table VII (p. 116)", "read"),
            Published("semillon.threshold", 9.7, "°C", "Table VII (p. 116)", "read"),
            Published(
                "cabernet_franc.mean_budburst_day",
                82.0,
                "d from 1 Jan",
                "Table VII (p. 116)",
                "read",
            ),
            Published("cabernet_franc.s", 1243, "action units", "Table VII (p. 116)", "read"),
            Published("cabernet_franc.c", 1.744, "1", "Table VII (p. 116)", "read"),
            Published("cabernet_franc.k", 0.368, "1", "Table VII (p. 116)", "read"),
            Published("cabernet_franc.threshold", 9.8, "°C", "Table VII (p. 116)", "read"),
            Published(
                "grenache.mean_budburst_day", 82.67, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("grenache.s", 1223, "action units", "Table VII (p. 116)", "read"),
            Published("grenache.c", 1.761, "1", "Table VII (p. 116)", "read"),
            Published("grenache.k", 0.344, "1", "Table VII (p. 116)", "read"),
            Published("grenache.threshold", 10.0, "°C", "Table VII (p. 116)", "read"),
            Published(
                "sauvignon.mean_budburst_day", 83.33, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("sauvignon.s", 1203, "action units", "Table VII (p. 116)", "read"),
            Published("sauvignon.c", 1.779, "1", "Table VII (p. 116)", "read"),
            Published("sauvignon.k", 0.32, "1", "Table VII (p. 116)", "read"),
            Published("sauvignon.threshold", 10.2, "°C", "Table VII (p. 116)", "read"),
            Published(
                "carignan.mean_budburst_day", 85.22, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("carignan.s", 1145, "action units", "Table VII (p. 116)", "read"),
            Published("carignan.c", 1.829, "1", "Table VII (p. 116)", "read"),
            Published("carignan.k", 0.262, "1", "Table VII (p. 116)", "read"),
            Published("carignan.threshold", 10.6, "°C", "Table VII (p. 116)", "read"),
            Published(
                "ugni_blanc.mean_budburst_day", 85.94, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("ugni_blanc.s", 1089, "action units", "Table VII (p. 116)", "read"),
            Published("ugni_blanc.c", 1.865, "1", "Table VII (p. 116)", "read"),
            Published("ugni_blanc.k", 0.223, "1", "Table VII (p. 116)", "read"),
            Published("ugni_blanc.threshold", 11.0, "°C", "Table VII (p. 116)", "read"),
            Published(
                "cabernet_sauvignon.mean_budburst_day",
                91.22,
                "d from 1 Jan",
                "Table VII (p. 116)",
                "read",
            ),
            Published("cabernet_sauvignon.s", 985, "action units", "Table VII (p. 116)", "read"),
            Published("cabernet_sauvignon.c", 2.0, "1", "Table VII (p. 116)", "read"),
            Published("cabernet_sauvignon.k", 0.133, "1", "Table VII (p. 116)", "read"),
            Published("cabernet_sauvignon.threshold", 12.2, "°C", "Table VII (p. 116)", "read"),
            Published(
                "mourvedre.mean_budburst_day", 93.06, "d from 1 Jan", "Table VII (p. 116)", "read"
            ),
            Published("mourvedre.s", 907, "action units", "Table VII (p. 116)", "read"),
            Published("mourvedre.c", 2.036, "1", "Table VII (p. 116)", "read"),
            Published("mourvedre.k", 0.116, "1", "Table VII (p. 116)", "read"),
            Published("mourvedre.threshold", 12.5, "°C", "Table VII (p. 116)", "read"),
            Published(
                "relation.log_k.intercept",
                2.57403,
                "1",
                "p. 117-118 (l. 772 of the OCR text)",
                "read",
            ),
            Published(
                "relation.log_k.slope_c",
                -1.72494,
                "1",
                "p. 117-118 (l. 772 of the OCR text)",
                "read",
            ),
            Published(
                "relation.s.intercept",
                3737,
                "action units",
                "p. 117 (l. 752 of the OCR text)",
                "read",
            ),
            Published(
                "relation.s.slope_d",
                -30.4138,
                "action units/d",
                "p. 117 (l. 752 of the OCR text)",
                "read",
            ),
            Published(
                "relation.c.intercept", 2.824, "1", "p. 117 (l. 762 of the OCR text)", "read"
            ),
            Published(
                "relation.c.slope_s",
                -0.000869,
                "1/action unit",
                "p. 117 (l. 762 of the OCR text)",
                "read",
            ),
            Published(
                "relation.threshold.intercept",
                -6.40,
                "°C",
                "p. 118 (l. 798 of the OCR text)",
                "read",
            ),
            Published(
                "relation.threshold.slope_c", 9.31, "°C", "p. 118 (l. 798 of the OCR text)", "read"
            ),
        ),
        flags=(
            "A heat sum to a threshold with a power-law response, no chilling term and a fixed"
            " 1 January start that the author says must be moved for other regions; the"
            " ancestor of RIOU (cortazar2009's eq. 2) and of BRIN's forcing idea.",
            "No forecast error is printed: 1-3 d is the observation error, 0-5 d the gap between"
            " dates from 30-year mean temperatures and observed means; cold spells after the"
            " sum is well along delay budburst and are not modelled.",
            "'17 années (1961 à 1987)' spans 27 calendar years; the scale's 'dix-huit années"
            " (1970-1988)' nineteen. Four references in the text, five starred in Table VII.",
        ),
    ),
    "bindi1997.growth": Formulation(
        "A whole-vine model: leaves appear at a rate linear in the day's mean temperature,"
        " bloom at 17 leaves, shoot leaf area a power of leaf number, biomass by radiation use"
        " efficiency, fruit growth after degree-day lags",
        (
            "Bindi, Miglietta, Gozzini, Orlandini & Seghi 1997, Vitis 36(2): 67-71, Table 1 and"
            " Fig. 1 (p. 68)"
        ),
        year=1997,
        authors=("Bindi, M.", "Miglietta, F.", "Gozzini, B.", "Orlandini, S.", "Seghi, L."),
        authors_complete=True,
        authors_from="read",
        checked="bindi_1997a.pdf (the 2026-10-14 drop; Vitis OJS galley)",
        doi="10.5073/vitis.1997.36.67-71",
        structures=(
            "rate-temperature-response",
            "degree-day-phenology",
            "growth-on-thermal-time",
            "allometry",
            "radiation-use-efficiency",
        ),
        calibrated_on=("bindi1997.mondeggi",),
        calibration_note=(
            "Leaf number rate RLF = (a + b Tmd)(1 + c SLN) with a -0.28, b 0.04, c -0.015 per"
            " day, credited to Miglietta et al. 1992; since the rate is linear in the daily mean"
            " and accumulates daily, the leaf count is a degree-day sum above a/b = 7 °C scaled"
            " by (1 + c SLN), and bloom at SLN > 17 is a heat-sum threshold: the engine's form"
            " for a stage, which is why degree-day-phenology is among the tags. Shoot leaf area"
            " SLA = d SLN^f (5.39, 2.13) and LAI = SLA NS / (COV PLA); fruit growth starts after"
            " LAG = 40 °C d above 10 °C from bloom and ends at MAT = 1,440; biomass is"
            " radiation times RUE 1.001 g/MJ cut by a quadratic in 0.25 Tmn + 0.75 Tmx, with"
            " interception 1 - exp(-0.5 LAI). Budburst is an observed input. Every constant"
            " comes from one Sangiovese season (1992); part II (literature/bindi1997b) validates on"
            " 1993-1994 and refits three constants for Cabernet Sauvignon. Table 1 read"
            " 2026-10-14 in the page image"
            " (literature/bindi1997)."
        ),
        parameters=(
            Published("rlf.a", -0.28, "leaf/d", "Table 1 (p. 68)", "read"),
            Published("rlf.b", 0.04, "leaf/d/°C", "Table 1 (p. 68)", "read"),
            Published("rlf.c", -0.015, "1/leaf", "Table 1 (p. 68)", "read"),
            Published("sla.d", 5.39, "m²? (see flag)", "Table 1 (p. 68)", "read"),
            Published("sla.f", 2.13, "1", "Table 1 (p. 68)", "read"),
            Published("bloom_leaf_number", 17, "leaves", "Fig. 1 box a (p. 68): SLN > 17", "read"),
            Published("cov", 0.75, "1", "Table 1 (p. 68)", "read"),
            Published("rue", 1.001, "g/MJ", "Table 1 (p. 68)", "read"),
            Published("k_extinction", 0.5, "1", "Table 1 (p. 68)", "read"),
            Published("lag", 40.0, "°C·d", "Table 1 (p. 68)", "read"),
            Published("mat", 1440.0, "°C·d", "Table 1 (p. 68)", "read"),
            Published("t_base", 10.0, "°C", "Table 1 (p. 68): TU = Tmd - Tb", "read"),
            Published("shoots_per_plant", 11, "shoots", "Table 1 (p. 68)", "read"),
            Published("planting_area", 3.0, "m²/plant", "Table 1 (p. 68)", "read"),
            Published("fbi_slope", 0.00443, "1/d", "Table 1 (p. 68)", "read"),
            Published("cabernet.sla.f", 2.06, "1", "Part II, Table 1 (p. 73)", "read"),
            Published("cabernet.rue", 0.691, "g/MJ", "Part II, Table 1 (p. 73)", "read"),
            Published("cabernet.fbi_slope", 0.00328, "1/d", "Part II, Table 1 (p. 73)", "read"),
        ),
        flags=(
            "SLA = 5.39 SLN^2.13 gives about 2,250 at 17 leaves, far above Fig. 2's 0-2 m²"
            " axis, so the printed units or form of the leaf-area relation do not reproduce"
            " the figure; the text calls it exponential. Not corrected.",
            "The units of a, b, c are not printed; the RLF base of 7 °C is arithmetic, not a"
            " printed base. K = 0.5 has no source.",
            "Parameterised on a single season of one vineyard, as the authors say; no shoot"
            " length, canopy height or susceptibility is modelled.",
        ),
    ),
    "tarara2009.canopy_logistic": Formulation(
        "Shoot length, leaves per shoot and shoot vegetative and fruit mass of Concord as"
        " logistic curves of degree-days above 10 °C from 1 January",
        (
            "Tarara, Blom, Shafii, Price & Olmstead 2009, HortScience 44(2): 334-340, Eq. 1 and"
            " Table 1 (pp. 336-337)"
        ),
        year=2009,
        authors=(
            "Tarara, Julie M.",
            "Blom, Paul E.",
            "Shafii, Bahman",
            "Price, William J.",
            "Olmstead, Mercy A.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="julie_2009.pdf (the 2026-10-14 drop)",
        doi="10.21273/HORTSCI.44.2.334",
        structures=("growth-on-thermal-time", "degree-day-phenology", "allometry"),
        calibrated_on=("tarara2009.prosser",),
        calibration_note=(
            "y = A / (1 + exp(-B (DD - D_A))), fitted by nonlinear least squares to 1,360"
            " destructively sampled shoots pooled over five seasons; A the asymptote, D_A the"
            " degree-days to half of it, B the rate, with standard errors and 95 % limits in"
            " Table 1. The clock is the engine's degree-day sum (base 10 °C from 1 January, no"
            " cap), and the day a shoot reaches a length is a degree-day threshold on this"
            " curve, which is why degree-day-phenology is among the tags. Vegetative mass is"
            " also a line in shoot length (0.678 SL - 7.25 g, R² 0.87) and in leaf number"
            " (4.431 LN - 8.31, R² 0.83). The fruit curves fit poorly by the authors' account."
            " Table 1 read 2026-10-14 in the page image (literature/tarara2009)."
        ),
        parameters=(
            Published("shoot_length.a", 82.047, "cm", "Table 1 (p. 337), SE 1.938", "read"),
            Published("shoot_length.b", 0.009, "1/(°C·d)", "Table 1 (p. 337), SE 0.001", "read"),
            Published("shoot_length.d_a", 300.560, "°C·d", "Table 1 (p. 337), SE 9.244", "read"),
            Published("leaves.a", 11.953, "leaves", "Table 1 (p. 337), SE 0.254", "read"),
            Published("leaves.b", 0.011, "1/(°C·d)", "Table 1 (p. 337), SE 0.001", "read"),
            Published("leaves.d_a", 253.320, "°C·d", "Table 1 (p. 337), SE 7.894", "read"),
            Published("vegetative_mass.a", 47.146, "g", "Table 1 (p. 337), SE 1.298", "read"),
            Published("vegetative_mass.b", 0.011, "1/(°C·d)", "Table 1 (p. 337), SE 0.001", "read"),
            Published(
                "vegetative_mass.d_a", 330.306, "°C·d", "Table 1 (p. 337), SE 10.398", "read"
            ),
            Published("fruit_mass.a", 72.285, "g", "Table 1 (p. 337), SE 3.232", "read"),
            Published("fruit_mass.b", 0.013, "1/(°C·d)", "Table 1 (p. 337), SE 0.001", "read"),
            Published("fruit_mass.d_a", 599.100, "°C·d", "Table 1 (p. 337), SE 14.695", "read"),
            Published("mass_from_length.slope", 0.678, "g/cm", "p. 336, R² 0.87", "read"),
            Published("mass_from_length.intercept", -7.250, "g", "p. 336", "read"),
            Published("t_base", 10.0, "°C", "p. 335, from 1 January, no upper threshold", "read"),
        ),
        flags=(
            "Concord is Vitis labruscana under deficit irrigation at Prosser: shoot length"
            " saturates at 82 cm and 12 leaves, numbers no vinifera vineyard would share; the"
            " form and the time scale (half the final length at 300 °C·d) are what transfer.",
            "No leaf area, canopy height or susceptibility; the only dates are degree-day marks"
            " (shoot length within 5 % of its maximum at 635 °C·d, 8-13 July).",
        ),
    ),
    "ruml2020.monthly_regression": Formulation(
        "Budburst and flowering of 20 cultivars as the average cultivar's line on the period's"
        " mean temperature plus a cultivar offset in days",
        (
            "Ruml & Korać 2020, Agro-knowledge Journal 21(2): 81-88, Eqs 2-3 (p. 84) and Table 1"
            " (p. 83)"
        ),
        year=2020,
        authors=("Ruml, Mirjana", "Korać, Nada"),
        authors_complete=True,
        authors_from="read",
        checked="mirjana_2020.pdf (the 2026-10-14 drop)",
        doi="10.7251/AGREN2002081R",
        structures=("monthly-temperature-regression",),
        calibrated_on=("ruml2016.karlovci",),
        calibration_note=(
            "The average cultivar's lines of literature/ruml2016 restated: budburst day of year"
            " = -3.62 Tb + 133.0 with Tb the mean daily temperature from 1 March to the onset"
            " (R² 0.71), flowering = -3.13 Tf + 217.1 with Tf the mean daily maximum from 15"
            " April to the onset (R² 0.85); each cultivar adds its correction factor, the"
            " difference between its mean date and the average cultivar's over 1986-2007"
            " (Table 1). In-sample mean absolute error 4 d (budburst, 3-6 by cultivar) and 3 d"
            " (flowering, 2-4); no hold-out. Read 2026-10-14 in the page images"
            " (literature/ruml2020)."
        ),
        parameters=(
            Published("budburst.k", 133.0, "DOY", "Eq. 2 (p. 84)", "read"),
            Published("budburst.alpha", -3.62, "d/°C", "Eq. 2 (p. 84)", "read"),
            Published("flowering.k", 217.1, "DOY", "Eq. 3 (p. 84)", "read"),
            Published("flowering.alpha", -3.13, "d/°C", "Eq. 3 (p. 84)", "read"),
            Published("budburst.pinot_noir.offset", -1, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.pinot_noir.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.cabernet_sauvignon.offset", 7, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.cabernet_sauvignon.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.gamay.offset", -3, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.gamay.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.merlot.offset", 3, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.merlot.offset", 0, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.probus.offset", 5, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.probus.offset", 4, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.limberger.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.limberger.offset", -1, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.prokupac.offset", -1, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.prokupac.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.chardonnay.offset", -4, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.chardonnay.offset", -3, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.bouvier.offset", -4, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.bouvier.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.ezerjo.offset", -3, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.ezerjo.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.petra.offset", -4, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.petra.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.pinot_blanc.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.pinot_blanc.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.neoplanta.offset", 0, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.neoplanta.offset", 2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.kreaca.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.kreaca.offset", 2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.muscat_ottonel.offset", 0, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.muscat_ottonel.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.riesling_239_20_gm.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.riesling_239_20_gm.offset", 0, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.pinot_gris.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.pinot_gris.offset", -2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.beli_medenac.offset", 2, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.beli_medenac.offset", 2, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.bagrina.offset", 3, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.bagrina.offset", 4, "d", "Table 1 (p. 83), CF", "read"),
            Published("budburst.riesling_italico.offset", 2, "d", "Table 1 (p. 83), CF", "read"),
            Published("flowering.riesling_italico.offset", 1, "d", "Table 1 (p. 83), CF", "read"),
        ),
        flags=(
            "The windows end at the onset itself, so as printed the lines cannot forecast; the"
            " paper does not say how it would be used before the stage. A simulator that knows"
            " its season can read them retrospectively.",
            "Slopes of -3.62 and -3.13 here against the 2016 table's -3.6 and -3.1 (rounding);"
            " the cultivar lines of 2016's Table 8 are replaced by offsets to the pooled line.",
        ),
    ),
    "buttaro2015.leaf_area": Formulation(
        "A grapevine leaf's area from its length times width, one line for eight table-grape"
        " genotypes",
        "Buttaro, Rouphael, Rivera, Colla & Gonnella 2015, Photosynthetica 53(3): 342-348,"
        " Table 3 (p. 346)",
        year=2015,
        authors=("Buttaro, D.", "Rouphael, Y.", "Rivera, C. M.", "Colla, G.", "Gonnella, M."),
        authors_complete=True,
        authors_from="read",
        checked="donato_2015.pdf (the 2026-10-14 drop)",
        doi="10.1007/s11099-015-0117-2",
        structures=("allometry",),
        calibration_note=(
            "LA = a + b (L x W) in cm2 fitted to 1,630 leaves of eight genotypes at Rutigliano"
            " (Bari), 2010, pooled after per-genotype lines proved alike (not shown); r² 0.986;"
            " validated on about 200 leaves of Italia in 2011 with a 0.8 % overestimate. Leaves"
            " 10-540 cm², length 3.1-25 cm. Twelve earlier single-cultivar models are listed"
            " (Table 1), Tsialtas et al. 2008's Cabernet line among them. Table 3 read 2026-10-14"
            " in the page image (literature/buttaro2015)."
        ),
        parameters=(
            Published("lw.a", -0.465, "cm²", "Table 3 (p. 346), SE 0.718", "read"),
            Published("lw.b", 0.914, "1", "Table 3 (p. 346), SE 0.004", "read"),
            Published("l.a", -88.599, "cm²", "Table 3 (p. 346), r² 0.884", "read"),
            Published("l.b", 20.758, "cm", "Table 3 (p. 346)", "read"),
            Published("w.a", -112.92, "cm²", "Table 3 (p. 346), r² 0.754", "read"),
            Published("w.b", 20.075, "cm", "Table 3 (p. 346)", "read"),
        ),
        flags=(
            "Table grapes in Apulia; a per-leaf relation, so leaf area per shoot or vine needs"
            " leaf counts and sizes from elsewhere. Table 3's rows 4 and 5 print identical"
            " constants for L² and W².",
        ),
    ),
    "sanchezdemiguel2011.shoot_leaf_area": Formulation(
        "Leaf area per shoot from leaves per shoot and the largest and smallest leaf, five"
        " cultivars at Madrid and Toledo",
        "Sanchez-de-Miguel, Junquera, de la Fuente, Jimenez, Linares, Baeza & Lissarrague 2011,"
        " Spanish Journal of Agricultural Research 9(1): 202-212, Eqs 6-7 (p. 206), Eqs 1-5"
        " (p. 205), Table 7 (p. 208)",
        year=2011,
        authors=(
            "Sanchez-de-Miguel, P.",
            "Junquera, P.",
            "de la Fuente, M.",
            "Jimenez, L.",
            "Linares, R.",
            "Baeza, P.",
            "Lissarrague, J. R.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="patricia_2011.pdf (the 2026-10-14 drop)",
        doi="10.5424/sjar/20110901-354-10",
        structures=("allometry",),
        calibrated_on=("sanchezdemiguel2011.madrid_toledo",),
        calibration_note=(
            "Lopes & Pinto 2005's form refitted: log10 of leaf area per shoot on log10 of"
            " leaves per shoot times the mean of the largest and smallest leaf (MLA), primary"
            " and lateral shoots apart, on the Syrah Toledo matrix (n 1,229) and applied to all"
            " six cultivar-sites; the reference areas are sums of one leaf in three through the"
            " paper's own main-vein lines (Eqs 1-5, 25 leaves a cultivar). Validation slopes"
            " 0.89-1.08, MAPE 6.3-11.3 %. The page prints the equations as 10 x [...]; read as"
            " a power of ten (literature/sanchezdemiguel2011). Pages 205-208 read 2026-10-14"
            " in the page images."
        ),
        parameters=(
            Published("primary.a", 0.012, "log10 cm²", "Eq. 6 (p. 206), R² 0.98", "read"),
            Published("primary.b", 0.996, "1", "Eq. 6 (p. 206)", "read"),
            Published("lateral.a", 0.036, "log10 cm²", "Eq. 7 (p. 206), R² 0.99", "read"),
            Published("lateral.b", 0.982, "1", "Eq. 7 (p. 206)", "read"),
            Published("cabernet_franc.leaf.k", 1.9077, "cm² cm^-1.803", "Eq. 1 (p. 205)", "read"),
            Published("cabernet_franc.leaf.p", 1.803, "1", "Eq. 1 (p. 205), R² 0.93", "read"),
            Published("cabernet_sauvignon.leaf.a", 0.38, "cm²", "Eq. 2 (p. 205)", "read"),
            Published("cabernet_sauvignon.leaf.b", 1.21, "1", "Eq. 2 (p. 205), R² 0.93", "read"),
            Published("merlot.leaf.a", -58.452, "cm²", "Eq. 3 (p. 205)", "read"),
            Published("merlot.leaf.b", 18.291, "cm", "Eq. 3 (p. 205), R² 0.86", "read"),
            Published("syrah.leaf.a", -75.409, "cm²", "Eq. 4 (p. 205)", "read"),
            Published("syrah.leaf.b", 21.41, "cm", "Eq. 4 (p. 205), R² 0.94", "read"),
            Published("tempranillo.leaf.a", -69.302, "cm²", "Eq. 5 (p. 205)", "read"),
            Published("tempranillo.leaf.b", 20.306, "cm", "Eq. 5 (p. 205), R² 0.93", "read"),
            Published(
                "flowering.cabernet_sauvignon.leaf_area", 96, "cm²", "Table 7 (p. 208)", "read"
            ),
            Published("flowering.cabernet_sauvignon.leaves", 20, "1", "Table 7 (p. 208)", "read"),
            Published("flowering.merlot.leaf_area", 118, "cm²", "Table 7 (p. 208)", "read"),
            Published("flowering.merlot.leaves", 17, "1", "Table 7 (p. 208)", "read"),
            Published("flowering.syrah.leaf_area", 183, "cm²", "Table 7 (p. 208)", "read"),
            Published("flowering.syrah.leaves", 12, "1", "Table 7 (p. 208)", "read"),
            Published("flowering.tempranillo.leaf_area", 141, "cm²", "Table 7 (p. 208)", "read"),
            Published("flowering.tempranillo.leaves", 12, "1", "Table 7 (p. 208)", "read"),
        ),
        flags=(
            "Needs a leaf count and two leaf sizes per shoot: no time or temperature term."
            " Cabernet Sauvignon's leaf line is quadratic in the main vein, Cabernet franc's a"
            " power; the others are lines. Table 7's flowering and ripening means (primary"
            " leaves, cm² and leaves a shoot) are the only seasonal numbers printed.",
        ),
    ),
    "su2022.lai_curve": Formulation(
        "Relative leaf area index of Thompson Seedless as a curve of degree-days above 10 °C,"
        " with the maximum LAI a line on seasonal water use",
        "Su, Tao, Sun, Shan & Wang 2022, Agronomy 12(5): 988, Table 3 (p. 9), Table 4 and"
        " Eq. 15 (pp. 10-14)",
        year=2022,
        authors=("Su, L.", "Tao, W.", "Sun, Y.", "Shan, Y.", "Wang, Q."),
        authors_complete=True,
        authors_from="read",
        checked="lijun_2022.pdf (the 2026-10-14 drop)",
        doi="10.3390/agronomy12050988",
        structures=("growth-on-thermal-time", "degree-day-phenology"),
        calibrated_on=("su2022.turpan",),
        calibration_note=(
            "RLAI = LAI / LAIm against degree-days (daily mean of maximum and minimum, each"
            " capped at 38 °C, above 10 °C; start date not printed), fitted by a genetic"
            " algorithm to the mean of six drip treatments on 15 sampling days of one season"
            " (2009). Five forms printed; the modified logistic (R² 0.9837, relative error"
            " 7.45 %) and the log-normal (0.9805, 8.16 %) are recorded, the paper preferring"
            " the three-parameter log-normal. Table 3 read 2026-10-14 in the page image"
            " (literature/su2022)."
        ),
        parameters=(
            Published("logistic.max", 1.4, "1", "Table 3 (p. 9)", "read"),
            Published("logistic.a", 3.7437, "1", "Table 3 (p. 9)", "read"),
            Published("logistic.b", -4.8303e-3, "1/°Cd", "Table 3 (p. 9)", "read"),
            Published("logistic.c", 1.2340e-6, "1/°Cd²", "Table 3 (p. 9)", "read"),
            Published("lognormal.max", 0.9771, "1", "Table 3 (p. 9)", "read"),
            Published("lognormal.gdd0", 2274.5, "°Cd", "Table 3 (p. 9)", "read"),
            Published("lognormal.alpha", 0.9142, "1", "Table 3 (p. 9)", "read"),
            Published("t_base", 10, "°C", "p. 5", "read"),
            Published("t_upper", 38, "°C", "p. 5", "read"),
            Published("laim.slope", 0.0056, "1/mm", "Eq. 15 (p. 10), R² 0.9654", "read"),
            Published("laim.intercept", -0.7418, "1", "Eq. 15 (p. 10)", "read"),
            Published("laim.x1", 5.84, "1", "Table 4 (p. 14), 1,215 mm", "read"),
            Published("laim.x6", 2.73, "1", "Table 4 (p. 14), 637.5 mm", "read"),
        ),
        flags=(
            "The engine's form: a growth measure as a function of a degree-day sum alone."
            " One season, one table-grape cultivar, a desert climate with two prunings. The"
            " fitted peaks (1,960-2,275 °Cd) sit after the measured one (about 1,690 °Cd). The"
            " modified logistic's fitted ceiling is 1.4 for a relative index whose maximum"
            " is 1; it peaks at 1.02 near 1,960 °Cd and passes half of that near 840 °Cd (own"
            " calculation, not printed).",
        ),
    ),
    "schumacher2024.cluster_resistance": Formulation(
        "Downy mildew severity of Pinot Noir clusters and leaf discs at seven growth stages",
        "Schumacher, Mertes, Kaltenbach, Bleyer & Fuchs 2024, Scientific Reports 14: 915,"
        " Results (p. 4)",
        year=2024,
        authors=(
            "Schumacher, S.",
            "Mertes, C.",
            "Kaltenbach, T.",
            "Bleyer, G.",
            "Fuchs, R.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="schumacher_2024.pdf (q191.pdf of the 2026-10-09 drop)",
        doi="10.1038/s41598-023-50666-4",
        structures=("age-resistance", "bunch-susceptibility-window"),
        calibrated_on=("schumacher2024.freiburg",),
        calibration_note=(
            "No curve is fitted: mean severity by BBCH stage, as the text prints it"
            " (literature/schumacher2024). Clusters, Pinot Noir: about 100 % to BBCH 75"
            " (92 % at 75), 55 % at 77-79, 2 % at 81-83. Souvignier Gris: nearly 100 % to"
            " 75, 64-65 % at 75, 41 % at 77-79, none at 81-83. Cabernet Cortis: 77, 86, 54,"
            " 20, 2 % at 53-55, 57-59, 65-68, 71-73, 75, none after. Solaris: 44-73 % to"
            " 65-68, 9 % at 71-73, none after. Leaf discs, Pinot Noir: 77, 73, 50, 16 % at"
            " 53-55, 57-59, 65-68, 71-73, 3 % at 81-83; Cabernet Cortis 13 and 6 %, Solaris"
            " 6 and under 1 % at the first two stages, below 1 % later; Souvignier Gris"
            " about 2 % throughout."
        ),
        parameters=(
            Published(
                "pinot_noir.cluster.bbch53_75",
                100,
                "%",
                "p. 4 text, 'almost 100%' up to and including BBCH 75",
                "read",
            ),
            Published("pinot_noir.cluster.bbch75", 92, "%", "p. 4 text, later paragraph", "read"),
            Published("pinot_noir.cluster.bbch77_79", 55, "%", "p. 4 text", "read"),
            Published("pinot_noir.cluster.bbch81_83", 2, "%", "p. 4 text", "read"),
            Published("pinot_noir.leaf_disc.bbch53_55", 77, "%", "p. 4 text", "read"),
            Published("pinot_noir.leaf_disc.bbch57_59", 73, "%", "p. 4 text", "read"),
            Published("pinot_noir.leaf_disc.bbch65_68", 50, "%", "p. 4 text", "read"),
            Published("pinot_noir.leaf_disc.bbch71_73", 16, "%", "p. 4 text", "read"),
            Published("pinot_noir.leaf_disc.bbch81_83", 3, "%", "p. 4 text", "read"),
        ),
        flags=(
            "Potted vines in an open greenhouse at Freiburg, 42 a cultivar, 2020-2023,"
            " inoculated in a chamber at 40,000 sporangia/ml and rated 4 weeks after; leaf"
            " discs are leaves matched to the cluster's stage, scored 7 days after, so they"
            " show a leaf of a given stage, not a given leaf's age in days. No calendar"
            " dates, no fitted curve, means read from the text, SDs only in the figures. The"
            " 2021 field trial gave Pinot Noir over 90 %.",
        ),
    ),
    "zhu2021.apsim_grapevine": Formulation(
        "Whole-vine model of Sauvignon blanc in APSIM Next Generation: chilling-forcing"
        " budburst, development-day growth, radiation-use biomass",
        "Zhu et al. 2021, in silico Plants 3(2): diab021, Table 2 (pp. 11-12) and text",
        year=2021,
        authors=(
            "Zhu, J.",
            "Parker, A.",
            "Gou, F.",
            "Agnew, R.",
            "Yang, L.",
            "Greven, M.",
            "Raw, V.",
            "Neal, S.",
            "Martin, D.",
            "Trought, M. C. T.",
            "Huth, N.",
            "Brown, H. E.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="junqi_2021.pdf (the 2026-10-14 drop)",
        doi="10.1093/insilicoplants/diab021",
        structures=(
            "rate-temperature-response",
            "growth-on-thermal-time",
            "degree-day-phenology",
            "chilling-dormancy",
            "radiation-use-efficiency",
        ),
        calibrated_on=("zhu2021.marlborough",),
        calibration_note=(
            "Sauvignon blanc, four Marlborough long-term sites, data sets 1-4 (2001-2020),"
            " fitted with DEoptim. RMSE budburst 4.1, flowering 3.1, veraison 6.8 d in"
            " calibration; 4.9, 4.2, 5.3 d in validation; 6.5, 4.85, 6.5 d for four other"
            " varieties. Table 2 read in the page images 2026-10-14 (literature/zhu2021)."
        ),
        parameters=(
            Published("chill.c", 12.42, "1", "Table 2 (p. 11)", "read"),
            Published("chill.d", -3.865, "1", "Table 2 (p. 11)", "read"),
            Published("forcing.t_base", 0.008, "°C", "Table 2 (p. 11)", "read"),
            Published("wang_engel.t_min", 3.9, "°C", "Table 2 (p. 11)", "read"),
            Published("wang_engel.t_opt", 29, "°C", "Table 2 (p. 11)", "read"),
            Published("wang_engel.t_max", 37.9, "°C", "Table 2 (p. 11)", "read"),
            Published("wang_engel.t_ref", 25, "°C", "Table 2 (p. 11)", "read"),
            Published("phyllochron.first", 1.64, "Ds", "text, l. 295 (first five leaves)", "read"),
            Published("phyllochron.later", 1.82, "Ds", "text, l. 295 (from the 10th leaf)", "read"),
            Published("leaf.max_area", 12000, "mm²", "Table 2 (p. 11)", "read"),
            Published("leaf.growth_duration", 14, "Ds", "Table 2 (p. 11)", "read"),
            Published("leaf.lag_duration", 40, "Ds", "Table 2 (p. 11)", "read"),
            Published("leaf.senescence_duration", 5, "Ds", "Table 2 (p. 11)", "read"),
            Published("sla.max", 20000, "mm²/g", "Table 2 (p. 11)", "read"),
            Published("sla.min", 15000, "mm²/g", "Table 2 (p. 11)", "read"),
            Published("rue.before_flowering", 0.8, "g/MJ", "Table 2 (p. 11)", "read"),
            Published("rue.after_flowering", 0.9, "g/MJ", "Table 2 (p. 11)", "read"),
            Published("extinction", 0.6, "1", "Table 2 (p. 11)", "read"),
            Published("shoot.t_m", 43, "Ds from budburst", "Table 2 (p. 12)", "read"),
            Published("shoot.t_e", 79.2, "Ds from budburst", "Table 2 (p. 12)", "read"),
            Published("nsc.k_max", 0.03, "g/g", "Table 2 (p. 11)", "read"),
            Published("nsc.t_m", 34.4, "Ds", "Table 2 (p. 11)", "read"),
            Published("nsc.t_e", 54, "Ds", "Table 2 (p. 11)", "read"),
            Published("berry.dw_max", 0.6, "g", "Table 2 (p. 12)", "read"),
            Published("berry.t_m", 47.8, "Ds from flowering", "Table 2 (p. 12)", "read"),
            Published("berry.t_e", 70, "Ds from flowering", "Table 2 (p. 12)", "read"),
            Published("ta.min", 7.8, "g/L", "Table 2 (p. 12)", "read"),
            Published("ta.max", 30.3, "g/L", "Table 2 (p. 12)", "read"),
            Published("ta.r", 0.0923, "1/Ds", "Table 2 (p. 12)", "read"),
            Published(
                "photoperiod.critical",
                13.1,
                "h",
                "text, l. 167 (cited to Camargo-Alvarez et al. 2020)",
                "read",
            ),
        ),
        flags=(
            "The engine's form twice over: a chilling sum then a forcing heat sum to a"
            " threshold for budburst (Chuine 2000's form), and growth as beta functions of"
            " development days (Wang & Engel 1998's rate integrated: thermal time). The"
            " forcing base 0.008 °C is printed as is and not explained. StructuralDMmax has"
            " no printed value. Eq. 10's TA at t = 0 (38.1 g/L) disagrees with the text"
            " (30.3 g/L at veraison). Needs APSIM Next Generation to run as published.",
        ),
    ),
    "schmidt2019.virtual_riesling": Formulation(
        "Virtual Riesling: a functional-structural model of the canopy of a Riesling vine, with"
        " phytomer, internode and leaf growth on thermal time and budburst by a degree-day sum",
        "Schmidt, Bahr, Friedel & Kahlen 2019, Agronomy 9(8): 426, Eqs 1-10 and text",
        year=2019,
        authors=(
            "Schmidt, D.",
            "Bahr, C.",
            "Friedel, M.",
            "Kahlen, K.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="dominik_2019.pdf (the 2026-10-14 drop)",
        doi="10.3390/agronomy9080426",
        structures=("growth-on-thermal-time", "degree-day-phenology", "allometry"),
        calibrated_on=("schmidt2019.geisenheim",),
        calibration_note=(
            "Phytomer rate, internode, leaf-vein and lateral budburst curves fitted to three"
            " Riesling vines digitised at Geisenheim in 2018 (E-L 12, 15, 26); leaf area form"
            " (Eq. 10) fitted to 302 leaves of Doring et al. 2013 after Beslic et al. 2010;"
            " budburst in other years is Nendel 2010's degree-day model with its parameters,"
            " borrowed, not fitted here. Read 2026-10-14 (literature/schmidt2019)."
        ),
        parameters=(
            Published("phyllochron.mu", 0.0453, "phytomers/°Cd", "text, l. 376", "read"),
            Published("phyllochron", 22.0892, "°Cd per phytomer", "text, l. 377", "read"),
            Published("t_base", 10, "°C", "Eq. 1, l. 343 (after Schultz 1992)", "read"),
            Published("internode.k", -3.1812, "1", "Eq. 3 (p. 7)", "read"),
            Published("il1max.a1", -0.5562, "cm per rank", "Eq. 4 (p. 7), as printed", "read"),
            Published("il1max.b1", 1.5729, "cm", "Eq. 4 (p. 7), as printed", "read"),
            Published("il1max.a2", 0.7212, "cm per rank", "Eq. 4 (p. 7)", "read"),
            Published("il1max.b2", 9.0909, "cm", "Eq. 4 (p. 7)", "read"),
            Published("lateral_internode.k", -3.9706, "1", "text, l. 459", "read"),
            Published("lateral_budburst.q0", 337.0334, "°Cd", "Eq. 8, l. 598", "read"),
            Published("lateral_budburst.q1", -18.5344, "°Cd per rank", "Eq. 8, l. 598", "read"),
            Published("lateral_budburst.min", 66.2676, "°Cd", "Eq. 9, l. 601", "read"),
            Published(
                "leaf.s_la",
                0.6869294,
                "sqrt(cm²) per cm of second-order vein",
                "Eq. 10, l. 649 (fitted to 302 leaves of Doring et al. 2013)",
                "read",
            ),
            Published(
                "nendel.t0",
                5.9,
                "°C",
                "text, l. 364 (borrowed from Nendel 2010)",
                "read",
            ),
            Published(
                "nendel.d_bb",
                186.1,
                "°Cd from 1 March",
                "text, l. 363-366 (borrowed from Nendel 2010; SD 24.7 °Cd)",
                "read",
            ),
            Published(
                "canopy.stop_height",
                2.3,
                "m",
                "text, l. 749-750 (run ends when 90 % of shoots reach it)",
                "read",
            ),
        ),
        flags=(
            "Eq. 4 as printed (a1 -0.5562, b1 1.5729) gives negative maxima for ranks 3-7,"
            " while Figure 4 shows 1.0 at rank 1 and 10.4 at rank 7, which a1 1.5729 and b1"
            " -0.5562 reproduce. The values are recorded as printed; the swap is a reading,"
            " confirmed on the page image 2026-10-14. Budburst is Nendel 2010's degree-day"
            " threshold, borrowed. The model needs its own code (GroIMP or similar, as the paper"
            " says) to run. Three vines of one cultivar in one year. Mean leaf area per shoot of"
            " 0.5-1.3 m² (l. 1512) and a cited LAI of about 3.8 (l. 1572) are outputs, not"
            " fits. Kin to the engine's degree-day pieces by form: growth on thermal time.",
        ),
    ),
    "vrignonbrenas2022.leaf_area_ramp": Formulation(
        "Leaf area per plant as a piecewise-linear ramp of thermal time after budburst, with"
        " a plateau, its slope and plateau time shifted by leaf nitrogen (SPAD) and storage",
        "Vrignon-Brenas et al. 2022, J. Exp. Bot. 73(5): 1385-1401, Table 4 (p. 10), Table 2",
        year=2022,
        authors=(
            "Vrignon-Brenas, S.",
            "Fontez, B.",
            "Bisson, A.",
            "Rolland, G.",
            "Chopard, J.",
            "Fumey, D.",
            "Metay, A.",
            "Pellegrino, A.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="sylvain_2021.pdf (the 2026-10-14 drop)",
        doi="10.1093/jxb/erab469",
        structures=("growth-on-thermal-time", "degree-day-phenology", "radiation-use-efficiency"),
        calibrated_on=("vrignonbrenas2022.montpellier_pots",),
        calibration_note=(
            "Own model, Bayesian fit to leaf area of potted Sauvignon blanc, five experiments"
            " on three batches, 2017-2019. Priors from earlier studies: plateau 1400 °Cd"
            " (Valdes-Gomez et al. 2009; Zufferey et al. 2012), onset 150 °Cd (Munitz et al."
            " 2016); no model shaped the data. Read 2026-10-14 (literature/vrignonbrenas2022)."
        ),
        parameters=(
            Published("slope.mu", 53.44, "cm²/°Cd", "Table 4 (p. 10); SD 3.21", "read"),
            Published(
                "slope.spad", 1.86, "cm²/°Cd per SPAD unit", "Table 4 (p. 10); SD 0.27", "read"
            ),
            Published("slope.storage", -7.49, "cm²/°Cd per g", "Table 4 (p. 10); SD 1.45", "read"),
            Published("tt_max.mu", 1335.35, "°Cd", "Table 4 (p. 10); SD 20.49", "read"),
            Published(
                "tt_max.spad", 12.47, "°Cd per SPAD unit", "Table 4 (p. 10); SD 4.65", "read"
            ),
            Published("tt_max.storage", -34.88, "°Cd per g", "Table 4 (p. 10); SD 3.72", "read"),
            Published(
                "tt_onset", 150, "°Cd after budburst", "text, l. 596-597 (fixed, a prior)", "read"
            ),
            Published("dm_per_mj.intercept", -6.35e-3, "g/MJ", "Eq. 4 fit, l. 871", "read"),
            Published("dm_per_mj.spad", 6.21e-4, "g/MJ per SPAD unit", "l. 871", "read"),
            Published("dm_per_mj.leaf_area", 5.29e-2, "g/MJ per m²", "l. 871 (R² 0.88)", "read"),
            Published("tt.budburst_to_flowering.2017", 326, "°Cd", "Table 2, l. 345", "read"),
            Published("tt.budburst_to_flowering.2018", 336, "°Cd", "Table 2, l. 348", "read"),
            Published("tt.budburst_to_flowering.2019", 272, "°Cd", "Table 2, l. 351", "read"),
            Published("tt.flowering_to_veraison.2017", 728, "°Cd", "Table 2, l. 346", "read"),
            Published("tt.flowering_to_veraison.2018", 779, "°Cd", "Table 2, l. 349", "read"),
            Published("tt.flowering_to_veraison.2019", 811, "°Cd", "Table 2, l. 352", "read"),
        ),
        flags=(
            "Potted Sauvignon blanc on SO4 outdoors, five experiments on three batches"
            " 2017-2019. The thermal-time base and formula are not printed. Eq. 1's leaf"
            " allometry has an unprinted sign. Leaf area per plant at the plateau is"
            " 0.17-1.68 m² (l. 797-798). The ramp is in thermal time after budburst, the"
            " engine's form (growth on thermal time), so kin by form. The text gives 12.45"
            " °Cd per SPAD unit (l. 781) where Table 4 prints 12.47.",
        ),
    ),
    "tsialtas2008.leaf_area": Formulation(
        "Leaf area of a Cabernet Sauvignon leaf from its length (own line) or from length and"
        " width (the best of eleven published lines)",
        "Tsialtas, Koundouras & Zioziou 2008, Photosynthetica 46(3): 452-456, text and Table 4",
        year=2008,
        authors=(
            "Tsialtas, J. T.",
            "Koundouras, S.",
            "Zioziou, E.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="j__2008.pdf (the 2026-10-14 drop)",
        structures=("allometry",),
        calibrated_on=("tsialtas2008.thessaly",),
        calibration_note=(
            "Own line fitted to 18 means of rootstock x irrigation x sampling, not to the 324"
            " leaves. The 0.587 line is Montero et al. 2000's, chosen as the best of eleven"
            " published lines by r² and mean squared difference. Read 2026-10-14"
            " (literature/tsialtas2008)."
        ),
        parameters=(
            Published("l.a", -151.41, "cm²", "text, l. 121 (r² 0.97, n 18 means)", "read"),
            Published("l.b", 18.379, "cm", "text, l. 121 (LA = a + b L)", "read"),
            Published(
                "best_published.lw",
                0.587,
                "1",
                "text, l. 100, 215-218 (LA = 0.587 L x W, cited to Montero et al. 2000)",
                "read",
            ),
        ),
        flags=(
            "Fitted to 18 treatment-stage means, not to the 324 leaves. Buttaro et al. 2015"
            " found the 0.587 line biased by 18 % on table grapes (literature/buttaro2015)."
            " No leaf counts per shoot. Independent of the engine.",
        ),
    ),
    "pallas2008.shoot_development": Formulation(
        "Shoot development of potted Syrah and Grenache N on thermal time: leaf emergence on the"
        " primary axis, the lag and end of secondary axes, and leaf area from leaf length and"
        " from leaf number",
        "Pallas, Louarn, Christophe, Lebon & Lecoeur 2008, Physiologia Plantarum 134: 49-63,"
        " read as Manuscript 1 of Pallas 2009 (PhD thesis, Ecole Centrale Paris), printed pp."
        " 50-63",
        year=2008,
        authors=(
            "Pallas, B.",
            "Louarn, G.",
            "Christophe, A.",
            "Lebon, E.",
            "Lecoeur, J.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="beno_t_2009.pdf (the 2026-10-14 drop; the thesis reprints the paper)",
        doi="10.1111/j.1399-3054.2008.01100.x",
        structures=("growth-on-thermal-time", "degree-day-phenology", "allometry"),
        calibrated_on=("pallas2008.montpellier_pots",),
        calibration_note=(
            "Potted Syrah and Grenache N at Montpellier, 2003, 2004 and 2006, 12 plants a"
            " cluster-load treatment, leaves counted and measured through 1200 °Cd above 10 °C;"
            " the thermal time is Lebon et al. 2004's, the secondary-axis structure (lag,"
            " linear production, end) is Louarn et al. 2007's, the leaf-length form follows"
            " Schultz 1992; neither Annals of Botany paper nor Schultz could be obtained"
            " (literature/unread/2026-10-14-truth-phenology-closed.md). Read in the thesis"
            " 2026-10-14 (literature/pallas2009); Eqs 6-8 on printed p. 53 read in the page image."
        ),
        parameters=(
            Published("t_base", 10, "°C", "l. 2329 (after Lebon et al. 2004)", "read"),
            Published(
                "phyllochron.rate", 0.044, "leaves/°Cd", "l. 2518, 2686 (both cultivars)", "read"
            ),
            Published("syrah.leaves_intercept", 2.75, "leaves", "l. 2686, R² 0.991, n 481", "read"),
            Published(
                "grenache.leaves_intercept", 3.50, "leaves", "l. 2686, R² 0.987, n 441", "read"
            ),
            Published("secondary.lag", 126, "°Cd", "l. 2603 (SD 32 °Cd)", "read"),
            Published(
                "secondary.end_gap",
                200,
                "°Cd without a new phytomer",
                "printed p. 53 (after Louarn et al. 2007)",
                "read",
            ),
            Published(
                "syrah.leaf.a", 0.011, "cm²/mm²", "Eq. 6, printed p. 53, n 182, r² 0.97", "read"
            ),
            Published("syrah.leaf.b", 0.1494, "cm²/mm", "Eq. 6, printed p. 53", "read"),
            Published(
                "grenache.leaf.a", 0.0091, "cm²/mm²", "Eq. 7, printed p. 53, n 135, r² 0.95", "read"
            ),
            Published("grenache.leaf.b", 0.2547, "cm²/mm", "Eq. 7, printed p. 53", "read"),
            Published(
                "syrah.axis.a", 0.93, "cm² per leaf²", "Eq. 8, printed p. 53, n 42, r² 0.97", "read"
            ),
            Published("syrah.axis.b", 56.63, "cm² per leaf", "Eq. 8, printed p. 53", "read"),
            Published(
                "grenache.axis.a",
                1.03,
                "cm² per leaf²",
                "Eq. 8, printed p. 53, n 37, r² 0.98",
                "read",
            ),
            Published("grenache.axis.b", 52.68, "cm² per leaf", "Eq. 8, printed p. 53", "read"),
            Published("experiment_end", 1200, "°Cd", "l. 2313", "read"),
        ),
        flags=(
            "Potted vines with cluster-load treatments, not a vineyard. Growth on thermal time is"
            " the engine's own form, so the record is kin to it by form. Manuscript 3's water"
            " effect (growth cycle of 23 °Cd lengthened by a sigmoid in FTSW, Eq. 21; the"
            " probability of leaf production, Eq. 22) has its parameters unprinted in the"
            " thesis, so it is in the note, not here; the RUE water factor in Manuscript 3 is"
            " Lebon et al. 2006's, cited."
        ),
    ),
    "mcartney1998.shoot_leaf_area": Formulation(
        "Leaf area per shoot as a logistic in days after bud break, Seyval and DeChaunac, shaded"
        " and unshaded",
        (
            "McArtney 1998, PhD dissertation, The Ohio State University, Fig. 4.4 (p. 47), Ch. 4"
            " text (pp. 44-45), Fig. 9.1 (p. 143)"
        ),
        year=1998,
        authors=("McArtney, S. J.",),
        authors_complete=True,
        authors_from="read",
        checked="steven_1998.pdf (the 2026-10-14 drop)",
        structures=("growth-on-days", "allometry"),
        calibrated_on=("mcartney1998.ohio",),
        calibration_note=(
            "area = a / (1 + exp(b - c t)), t in days after bud break, a in cm² a shoot. The"
            " 'DeChaunac' and 'Seyval' vines (French-American hybrids) had been under 80 % shade"
            " cloth from flowering in the previous season, or unshaded (Fig. 4.4 and Table 4.1"
            " say the previous year), in Ohio; shoot leaf area was sampled through the"
            " season and fitted by a sigmoid in SAS (Fig. 4.4, read in the page image). Single"
            " leaf area is k x length x width; in Ch. 9 field Seyval (45 shoots) leaf area is a"
            " line in shoot length. No model shaped the data; no dependence recorded. Days to"
            " half the final area, b/c, are 20.0 to 26.9 and the time scale 1/c 4.0 to 6.3 days,"
            " my own calculation, not printed."
        ),
        parameters=(
            Published(
                "seyval.a", 299, "cm² a shoot", "Fig. 4.4 (p. 47), read in the page image", "read"
            ),
            Published("seyval.b", 4.0, "1", "Fig. 4.4 (p. 47), read in the page image", "read"),
            Published("seyval.c", 0.17, "1/d", "Fig. 4.4 (p. 47), read in the page image", "read"),
            Published(
                "seyval_shaded.a",
                197,
                "cm² a shoot",
                "Fig. 4.4 (p. 47), read in the page image",
                "read",
            ),
            Published(
                "seyval_shaded.b", 4.8, "1", "Fig. 4.4 (p. 47), read in the page image", "read"
            ),
            Published(
                "seyval_shaded.c", 0.22, "1/d", "Fig. 4.4 (p. 47), read in the page image", "read"
            ),
            Published(
                "dechaunac.a",
                619,
                "cm² a shoot",
                "Fig. 4.4 (p. 47), read in the page image",
                "read",
            ),
            Published("dechaunac.b", 4.3, "1", "Fig. 4.4 (p. 47), read in the page image", "read"),
            Published(
                "dechaunac.c", 0.16, "1/d", "Fig. 4.4 (p. 47), read in the page image", "read"
            ),
            Published(
                "dechaunac_shaded.a",
                252,
                "cm² a shoot",
                "Fig. 4.4 (p. 47), read in the page image",
                "read",
            ),
            Published(
                "dechaunac_shaded.b", 5.0, "1", "Fig. 4.4 (p. 47), read in the page image", "read"
            ),
            Published(
                "dechaunac_shaded.c",
                0.25,
                "1/d",
                "Fig. 4.4 (p. 47), read in the page image",
                "read",
            ),
            Published(
                "leaf.k.dechaunac",
                0.83,
                "1",
                "l. 2442, area = k length x width, R² 0.98, P < 0.0001",
                "read",
            ),
            Published(
                "leaf.k.seyval",
                0.86,
                "1",
                "l. 2444, area = k length x width, R² 0.99, P < 0.0001",
                "read",
            ),
            Published(
                "shoot.area_intercept",
                -5.73,
                "cm²",
                "Fig. 9.1 B (p. 143), read in the page image, R² 0.84, n 45 Seyval shoots",
                "read",
            ),
            Published(
                "shoot.area_slope",
                10.9,
                "cm²/cm",
                "Fig. 9.1 B (p. 143), per cm of shoot length, read in the page image",
                "read",
            ),
            Published(
                "shoot.diameter_intercept",
                -351,
                "cm²",
                "Fig. 9.1 A (p. 143), read in the page image by the main session, R² 0.71",
                "read",
            ),
            Published(
                "shoot.diameter_slope",
                124.8,
                "cm²/mm",
                "Fig. 9.1 A (p. 143), per mm of basal shoot diameter, read in the page image",
                "read",
            ),
            Published(
                "shoot.leaves_intercept",
                -242,
                "cm²",
                "Fig. 9.1 C (p. 143), read in the page image by the main session, R² 0.71",
                "read",
            ),
            Published(
                "shoot.leaves_slope",
                69.8,
                "cm² per leaf",
                "Fig. 9.1 C (p. 143), per leaf on the shoot, read in the page image",
                "read",
            ),
            Published(
                "elongation.budbreak_to_bloom",
                13.98,
                "mm/d",
                "Ch. 9 table (l. 6481), bud break to bloom; OCR, unchecked",
                "read",
            ),
            Published(
                "elongation.bloom_to_2wab",
                17.34,
                "mm/d",
                "Ch. 9 table (l. 6481), bloom to 2 weeks after bloom; OCR, unchecked",
                "read",
            ),
            Published(
                "elongation.2_to_6wab",
                5.61,
                "mm/d",
                "Ch. 9 table (l. 6481), 2 to 6 weeks after bloom; OCR, unchecked",
                "read",
            ),
        ),
        flags=(
            "Hybrids in Ohio, not Vitis vinifera in a Mediterranean vineyard; the curve is for a"
            " shoot, not a vine.",
            "The logistic is in calendar days after bud break with no temperature, the form the"
            " truth now uses; its midpoint b/c (20 to 27 days) and time scale 1/c (4 to 6 days)"
            " are the comparable numbers.",
            "The exponents were read from a scanned figure; the Ch. 9 elongation values are OCR"
            " and unchecked on the image; the Ch. 9 year is not confirmed in the lines read.",
        ),
    ),
    "cola2014.barbera_canopy": Formulation(
        "Leaf area per shoot by vegetative BBCH stage and shoot count, canopy porosity on width,"
        " and the canopy ramp of Cola et al.'s Barbera model",
        "Cola, Mariani, Salinari, Civardi, Bernizzoni, Gatti & Poni 2014, Agricultural and Forest"
        " Meteorology 184: 117-136, Eqs 12-13 and 7-11 (p. 122), Eq. 15 (p. 123), Table 1 (p. 119)",
        year=2014,
        authors=(
            "Cola, G.",
            "Mariani, L.",
            "Salinari, F.",
            "Civardi, S.",
            "Bernizzoni, F.",
            "Gatti, M.",
            "Poni, S.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="1-s2.0-S0168192313002633-main.pdf (the 2026-10-15 drop)",
        doi="10.1016/j.agrformet.2013.09.008",
        structures=(
            "degree-day-phenology",
            "allometry",
            "carbon-balance",
            "water-limited-growth",
            "rate-temperature-response",
        ),
        calibrated_on=("cola2014.piacenza",),
        calibration_note=(
            "Barbera AT 84 on 420A, planted 1999, Piacenza, 2011-2012, low density cane-pruned"
            " Guyot and high density spur cordon; BBCH scored every 3-4 days; five shoots sampled"
            " destructively on 12 dates in 2011; porosity from 3,480 line-bar readings a date."
            " Validation 2003-2007 on other vines of the same vineyard for final leaf area (R²"
            " 0.92 HD, 0.63 LD) and yield (R² 0.96 LD; the abstract says 0.94 HD and Table 9"
            " 0.96). Pages 119-123 read 2026-10-14, p. 122 in the page image"
            " (literature/cola2014)."
        ),
        parameters=(
            Published("la1.bbch2", 3.51e-4, "m² shoot^-1", "Eq. 12 (p. 122), R² 0.99", "read"),
            Published("la1.bbch_n", -1.798e-6, "m² shoot^-1", "Eq. 12 (p. 122)", "read"),
            Published("la1.n2", -9.3745e-6, "m² shoot^-1", "Eq. 12 (p. 122)", "read"),
            Published("la1.bbch", -6.848e-2, "m² shoot^-1", "Eq. 12 (p. 122)", "read"),
            Published("la1.n", 8.66e-4, "m² shoot^-1", "Eq. 12 (p. 122)", "read"),
            Published(
                "la1.c",
                3.3268,
                "m² shoot^-1",
                "Eq. 12 (p. 122); BBCHveg 101-127, Nshoots clamped 10-65",
                "read",
            ),
            Published("la2.bbch2", 7.7521e-5, "m² shoot^-1", "Eq. 13 (p. 122), R² 0.98", "read"),
            Published("la2.bbch_n", -1.594e-4, "m² shoot^-1", "Eq. 13 (p. 122)", "read"),
            Published("la2.n2", 6.88e-5, "m² shoot^-1", "Eq. 13 (p. 122)", "read"),
            Published("la2.bbch", 3.028e-2, "m² shoot^-1", "Eq. 13 (p. 122)", "read"),
            Published("la2.n", 1.263e-2, "m² shoot^-1", "Eq. 13 (p. 122)", "read"),
            Published("la2.c", -2.3443, "m² shoot^-1", "Eq. 13 (p. 122)", "read"),
            Published("cp.a", 0.6417, "1", "Eq. 15 (p. 123), porosity on width, R² 0.82", "read"),
            Published("cp.b", -0.33, "m^-1", "Eq. 15 (p. 123), width Wx in m", "read"),
            Published("phdel.max", 1.55, "1", "Eq. 11 (p. 122), for more than 65 shoots", "read"),
            Published("phdel.base", 0.08, "1", "Eq. 8 (p. 122), read in the page image", "read"),
            Published("canopy.wx_min", 0.3, "m", "Table 1 (p. 119), low density 2011", "read"),
            Published("canopy.wx_max", 0.8, "m", "Table 1 (p. 119), low density 2011", "read"),
            Published("canopy.h_min", 0.2, "m", "Table 1 (p. 119), low density 2011", "read"),
            Published("canopy.h_max", 1.2, "m", "Table 1 (p. 119), low density 2011", "read"),
            Published("canopy.hd.wx_min", 0.2, "m", "Table 1 (p. 119), high density", "read"),
            Published("canopy.hd.wx_max", 0.6, "m", "Table 1 (p. 119), high density", "read"),
            Published("canopy.hd.h_min", 0.2, "m", "Table 1 (p. 119), high density", "read"),
            Published("canopy.hd.h_max", 1.0, "m", "Table 1 (p. 119), high density", "read"),
            Published(
                "canopy.ramp_start",
                101,
                "BBCH",
                "text, l. 400-408 (ramp to BBCH 77, then held)",
                "read",
            ),
            Published("canopy.ramp_end", 77, "BBCH", "text, l. 400-408", "read"),
            Published("leaf_weight.la1.a", 43.34, "cm² g^-1", "Eq. 2 (l. 206), R² 0.95", "read"),
            Published("leaf_weight.la1.b", -50.99, "cm²", "Eq. 2 (l. 206)", "read"),
            Published("leaf_weight.la2.a", 44.12, "cm² g^-1", "Eq. 3 (l. 209), R² 0.95", "read"),
            Published("leaf_weight.la2.b", 70.34, "cm²", "Eq. 3 (l. 209)", "read"),
            Published(
                "flowering.leaf_area.hd",
                4.8,
                "m² vine^-1",
                "text, l. 637-638 (BBCH 65, 2011)",
                "read",
            ),
            Published(
                "flowering.leaf_area.ld",
                1.2,
                "m² vine^-1",
                "text, l. 637-638 (BBCH 65, 2011)",
                "read",
            ),
        ),
        flags=(
            "The phenology is a heat sum (cumulated normal heat hours to stage thresholds, Fig. 4"
            " curves only, read by eye; thresholds shifted from Iphen's Cabernet Sauvignon"
            " reference, Mariani et al. 2013), the engine's form. Eqs 12-13 take BBCHveg as"
            " input, so in the paper's own run the clock is the heat sum.",
            "Eq. 39 (thermal limitation) as printed is negative at every temperature from 7 to"
            " 40 °C and cannot be used; Eq. 32's water factor is printed as a product in mm, not"
            " a ratio; Eqs 20-21 print 2 pi x 365 where 2 pi/365 would give a yearly cycle.",
            "The NHH cardinal temperatures (7, 25.5, 35 °C, cited to Mariani et al. 2012) and base"
            " are not printed as the NHH's own numbers; the light-interception equations are"
            " Oyarzun et al. 2007's, not printed; Table 1 spacing (2.2 x 1.8 m) disagrees with"
            " the text (2.5 x 1.2 m).",
        ),
    ),
    "lebon2004.leaf_development": Formulation(
        "Leaves on a grapevine main stem as lines in degree-days above 10 °C, the leaf appearance"
        " rate on mean temperature, and a leaf-area allometry, Grenache N",
        "Lebon, Pellegrino, Tardieu & Lecoeur 2004, Annals of Botany 93(3): 263-274, Eqs 5-8"
        " (p. 268), Eqs 1-3 and the lamina allometry (p. 266), Table 3",
        year=2004,
        authors=("Lebon, E.", "Pellegrino, A.", "Tardieu, F.", "Lecoeur, J."),
        authors_complete=True,
        authors_from="read",
        checked="mch038.pdf (the 2026-10-15 drop)",
        doi="10.1093/aob/mch038",
        structures=(
            "rate-temperature-response",
            "growth-on-thermal-time",
            "degree-day-phenology",
            "allometry",
        ),
        calibrated_on=("lebon2004.montpellier",),
        calibration_note=(
            "Grenache N, four experiments at Montpellier with no water deficit: two in pots"
            " (clone 226 on Fercal; 1999 and 2000 in the text, 2000 and 2001 in the tables) and"
            " two in a vineyard (clone 70 on 110 Richter, planted 1987; 1999 and 2000). Leaves"
            " counted on six to twelve shoots every 3-4 days or weekly; the leaf appearance rate"
            " fitted over periods of 9-15 days at 13.0-23.8 °C across all four experiments, one"
            " line for all (F 1.22); thermal time by daily integration above the base (CDD,"
            " after Bonhomme 2000). The framework is Rickman & Klepper 1995's, the leaf-area"
            " form Schultz 1992's. Pallas 2008 and Louarn 2007 borrow this paper's base and"
            " rate: pallas2008.shoot_development and louarn2007.shoot_architecture compute the"
            " same leaf-appearance rule. Read 2026-10-15 (literature/lebon2004); Eqs 1-3, the"
            " 93-leaf allometry and Eqs 5-8 on printed pp. 266 and 268 read in the page images."
        ),
        parameters=(
            Published(
                "lar.a", 0.0430, "leaves/day/°C", "Eq. 5, p. 268, r² 0.837, n 376 (l. 545)", "read"
            ),
            Published("lar.b", -0.3946, "leaves/day", "Eq. 5, p. 268 (l. 545)", "read"),
            Published(
                "t_base.fitted",
                9.2,
                "°C",
                "p. 268 (l. 547), -b/a, +/- 0.5 (SD or SE not said)",
                "read",
            ),
            Published("t_base.used", 10, "°C", "pp. 266 and 268 (l. 421, 552)", "read"),
            Published("initiated.a", 0.050, "leaves/°Cd", "Eq. 6, l. 548, r² 0.993", "read"),
            Published("initiated.b", 7.85, "leaves", "Eq. 6, l. 548", "read"),
            Published("unfolded.a", 0.046, "leaves/°Cd", "Eq. 7, l. 550, r² 0.986, n 186", "read"),
            Published("unfolded.b", 0.36, "leaves", "Eq. 7, l. 550", "read"),
            Published("expanded.a", 0.038, "leaves/°Cd", "Eq. 8, l. 551, r² 0.991", "read"),
            Published("expanded.b", -5.27, "leaves", "Eq. 8, l. 551", "read"),
            Published(
                "leaf.a", 0.0075, "area/length² (units not printed)", "p. 266, l. 394, n 93", "read"
            ),
            Published(
                "leaf.b",
                0.07505,
                "area/length (units not printed)",
                "p. 266, l. 394, r² 0.901",
                "read",
            ),
            Published("leaf.c", -29.151, "area (units not printed)", "p. 266, l. 394", "read"),
            Published("expansion.duration.phytomer10", 366, "°Cd", "l. 579", "read"),
            Published("expansion.duration.phytomer20", 425, "°Cd", "l. 579", "read"),
            Published("expansion.increment.to10", 25, "°Cd per phytomer", "l. 598", "read"),
            Published("expansion.increment.after10", 5, "°Cd per phytomer", "l. 599", "read"),
            Published("internode.plateau", 100, "mm", "from phytomer 12, l. 587", "read"),
        ),
        flags=(
            "Growth on thermal time is the engine's own form, so the record is kin to it by form."
            " The per-leaf logistic (Eq. 1) has no printed parameters, only Fig. 5. No branch"
            " relation is fitted: branch rates were not linear in thermal time, about 15 % of"
            " branches stopped, up to 25 % of R0 and 50 % of R1 and R2 in the vineyard. The pot"
            " years conflict (text 1999-2000, tables 2000-2001). No stage dates. The leaf-area"
            " allometry prints no units."
        ),
    ),
    "louarn2007.shoot_architecture": Formulation(
        "Main-stem phyllochron, branch leaf-appearance rates and durations by zone, and"
        " leaf-area allometries for Syrah and Grenache N in pots",
        "Louarn, Guedon, Lecoeur & Lebon 2007, Annals of Botany 99(3): 425-437, Table 1 (p. 430),"
        " Table 5 (p. 434), text p. 433 and 437",
        year=2007,
        authors=("Louarn, G.", "Guedon, Y.", "Lecoeur, J.", "Lebon, E."),
        authors_complete=True,
        authors_from="read",
        checked="mcl276.pdf (the 2026-10-15 drop)",
        doi="10.1093/aob/mcl276",
        structures=("growth-on-thermal-time", "degree-day-phenology", "allometry"),
        calibrated_on=("louarn2007.montpellier_pots",),
        calibration_note=(
            "Grenache N and Syrah in 0.050 m3 pots outdoors at Montpellier, four experiments"
            " 2002-2005, 60 shoots a genotype; thermal time above 10 °C after Lebon et al. 2004"
            " (this record computes the same leaf-appearance rule as"
            " lebon2004.leaf_development); the leaf-area form is Schultz 1992's. Zones come from"
            " a hidden semi-Markov model fitted to the branching sequences. Table 1 lines are"
            " from independent leaves. Read 2026-10-15 (literature/louarn2007); Table 1's minus"
            " signs, lost in the text layer, restored from the layout."
        ),
        parameters=(
            Published("t_base", 10, "°C", "l. 180 (after Lebon et al. 2004)", "read"),
            Published(
                "phyllochron.rate",
                0.044,
                "leaves/°Cd",
                "l. 812, +/- 0.002 (SD or SE not said), three years pooled",
                "read",
            ),
            Published(
                "syrah.leaf.a", 0.0111, "cm²/mm²", "Table 1, expts 3-4, n 182, r² 0.953", "read"
            ),
            Published("syrah.leaf.b", 0.1494, "cm²/mm", "Table 1, expts 3-4", "read"),
            Published(
                "grenache.leaf.a", 0.0091, "cm²/mm²", "Table 1, expts 3-4, n 135, r² 0.972", "read"
            ),
            Published("grenache.leaf.b", 0.2547, "cm²/mm", "Table 1, expts 3-4", "read"),
            Published(
                "syrah.leaf2.a", 0.0134, "cm²/mm²", "Table 1, expt 2, n 248, r² 0.971", "read"
            ),
            Published("syrah.leaf2.b", -0.0762, "cm²/mm", "Table 1, expt 2", "read"),
            Published(
                "grenache.leaf2.a", 0.0100, "cm²/mm²", "Table 1, expt 2, n 233, r² 0.956", "read"
            ),
            Published("grenache.leaf2.b", 0.1620, "cm²/mm", "Table 1, expt 2", "read"),
            Published("internode.a4.syrah", 1.315, "1", "Table 1, Eq. 4, n 160, r² 0.95", "read"),
            Published("internode.a4.grenache", 1.510, "1", "Table 1, Eq. 4, n 75, r² 0.98", "read"),
            Published("grenache.r0", 0.0334, "leaves/°Cd", "Table 5, zone B, R0 (l. 827)", "read"),
            Published("grenache.r1", 0.0235, "leaves/°Cd", "Table 5, zone B, R1 (l. 827)", "read"),
            Published("grenache.r2", 0.0260, "leaves/°Cd", "Table 5, zone B, R2 (l. 827)", "read"),
            Published("syrah.r0", 0.0341, "leaves/°Cd", "Table 5, zone B, R0 (l. 827)", "read"),
            Published("syrah.r1", 0.0337, "leaves/°Cd", "Table 5, zone B, R1 (l. 827)", "read"),
            Published("syrah.r2", 0.0297, "leaves/°Cd", "Table 5, zone B, R2 (l. 827)", "read"),
            Published("grenache.d0", 967, "°Cd", "Table 5, zone B, R0 duration (l. 832)", "read"),
            Published("grenache.d1", 631, "°Cd", "Table 5, zone B, R1 duration (l. 832)", "read"),
            Published("grenache.d2", 650, "°Cd", "Table 5, zone B, R2 duration (l. 832)", "read"),
            Published("syrah.d0", 912, "°Cd", "Table 5, zone B, R0 duration (l. 832)", "read"),
            Published("syrah.d1", 930, "°Cd", "Table 5, zone B, R1 duration (l. 832)", "read"),
            Published("syrah.d2", 720, "°Cd", "Table 5, zone B, R2 duration (l. 832)", "read"),
            Published(
                "zone_a.phytomers.grenache", 4.0, "phytomers", "l. 488-490, SD 0.8, n 58", "read"
            ),
            Published(
                "zone_a.phytomers.syrah", 2.7, "phytomers", "l. 488-490, SD 0.6, n 56", "read"
            ),
            Published(
                "state_1200.primary_phytomers.grenache",
                50.8,
                "phytomers",
                "Table 2, expt 3, l. 439",
                "read",
            ),
            Published(
                "state_1200.primary_phytomers.syrah",
                52.9,
                "phytomers",
                "Table 2, expt 3, l. 439",
                "read",
            ),
            Published(
                "state_1200.secondary_leaf_area.grenache",
                2.00,
                "m²",
                "Table 2, expt 3, l. 443",
                "read",
            ),
            Published(
                "state_1200.secondary_leaf_area.syrah",
                2.58,
                "m²",
                "Table 2, expt 3, l. 443",
                "read",
            ),
        ),
        flags=(
            "Potted vines, not a vineyard. Growth on thermal time is the engine's own form, so the"
            " record is kin to it by form. Table 5's Grenache R1 zone C proximal rate prints"
            " 0.288, an order above its neighbours, probably 0.0288; not corrected and not in the"
            " record. Table 1's minus signs are lost in the text layer and restored from the"
            " layout. The leaf area by rank logistics (Eq. 6, eight sets, r² 0.56-0.84) are in"
            " the note, not here. The +/- 0.002 on the phyllochron is not labelled SD or SE."
        ),
    ),
    "forster2016.melodist": Formulation(
        "MELODIST v0.1.1: hourly temperature, humidity, wind, radiation and precipitation from"
        " daily values, one variable at a time at one site (methods T1, H1-H4, W1-W3, R1-R3,"
        " P1-P2)",
        "Foerster et al. 2016, Geosci. Model Dev. 9:2315-2333, Table 2 and Sect. 3-4",
        year=2016,
        authors=(
            "Foerster, Kristian",
            "Hanzer, Florian",
            "Winter, Benjamin",
            "Marke, Thomas",
            "Strasser, Ulrich",
        ),
        authors_complete=True,
        authors_from="read",
        checked="kristian_2016.pdf (the 2026-10-18 drop)",
        doi="10.5194/gmd-9-2315-2016",
        structures=("disaggregation",),
        calibrated_on=("forster2016.five_sites",),
        calibration_note=(
            "Methods named in Table 2: temperature T1 (cosine between Tmin and Tmax); humidity"
            " H1 (dew point = Tmin), H2 (dew point = a Tmin + b, fitted per site), H3 (dew"
            " point linear between days with a sine term) and H4 (daily Hmin and Hmax); wind"
            " W1-W3; radiation R1-R3; precipitation P1-P2. H2, H3 and R2 are fitted on each"
            " site's calibration period, H1 and H4 are not. Fitted a and b are not printed."
            " Five sites, calibration and validation periods in forster2016.five_sites."
        ),
        parameters=(
            Published("h1.a", 1, "1", "text, l. 319 (H1: a = 1, b = 0)", "read"),
            Published("h1.b", 0, "°C", "text, l. 319 (H1: a = 1, b = 0)", "read"),
            Published(
                "h3.kr_high_radiation", 6, "1", "Eq. 8 text, l. 409 (above 100 W m-2)", "read"
            ),
            Published("h3.kr_low_radiation", 12, "1", "Eq. 8 text, l. 409 (otherwise)", "read"),
            Published("t1.tmax_after_noon", 2, "h", "text, l. 193 (rule of thumb)", "read"),
            Published("r2.angstrom_a", 0.25, "1", "text, l. 471 (default)", "read"),
            Published("r2.angstrom_b", 0.75, "1", "text, l. 471 (default)", "read"),
        ),
        flags=(
            "Not validated on humidity near saturation or on wet hours: Table 4 gives only"
            " whole-series mean, RMSE, r and NSE for H3 relative humidity (RMSE 10.39 to 18.52 %,"
            " r 0.02 at Ny-Alesund, 0.51 to 0.72 elsewhere); the text says RMSE 20 %, which"
            " Table 4 does not show. H1, H2 and H4 results are not printed in the tables read.",
            "Humidity from H1-H3 is es(Tdew) / es(T) of the disaggregated temperature; nothing"
            " printed says whether it is capped at 100 %. H1 holds the dew point at Tmin all day.",
            "Each variable is disaggregated alone, with no co-variation: wind speed has no link to"
            " rain or humidity, and there is no wind direction.",
            "Code is open: GPL-3, Python, GitHub kristianfoerster/melodist and Zenodo"
            " 10.5281/zenodo.54676, so it can run. It is a disaggregation tool, not a generator:"
            " the daily series come from elsewhere.",
        ),
        role="process",
    ),
    "pidoto2023.hourly_generator": Formulation(
        "Semi-parametric hourly weather generator: space-time rainfall (alternating renewal,"
        " copulas), k-NN resampling of daily temperature, humidity and radiation, hourly"
        " values by MELODIST's deterministic forms",
        "Pidoto & Haberlandt 2023, Hydrol. Earth Syst. Sci. 27:3957-3975, Sect. 2.1-2.4, Eqs 19-23",
        year=2023,
        authors=("Pidoto, Ross", "Haberlandt, Uwe"),
        authors_complete=True,
        authors_from="read",
        checked="ross_2023.pdf (the 2026-10-18 drop)",
        doi="10.5194/hess-27-3957-2023",
        borrows=("forster2016.melodist",),
        structures=("weather-generator", "disaggregation"),
        calibrated_on=("pidoto2023.germany",),
        calibration_note=(
            "Rainfall fitted to 699 DWD sub-daily stations in two seasons (April-September,"
            " October-March); the k-NN resamples HYRAS daily data conditioned on the"
            " catchment rainfall state. The hourly step applies MELODIST (Foerster et al."
            " 2016) with forms that need no hourly observations: temperature by the cosine"
            " (Eq. 20), relative humidity from Eq. 21 with the dew point equal to the daily"
            " minimum temperature through the day (Tdew = Tmin, a rule, no diurnal profile),"
            " radiation by Eq. 23. Fitted rainfall parameters are not printed."
        ),
        parameters=(
            Published("t1.tmax_after_noon", 2, "h", "p. 3964, text under Eq. 20", "read"),
            Published("magnus.pos.a", 6.1078, "not stated", "Eq. 22, p. 3964 (T >= 0 °C)", "read"),
            Published("magnus.pos.b", 17.08085, "1", "Eq. 22, p. 3964 (T >= 0 °C)", "read"),
            Published("magnus.pos.c", 234.175, "°C", "Eq. 22, p. 3964 (T >= 0 °C)", "read"),
            Published("magnus.neg.a", 6.1071, "not stated", "Eq. 22, p. 3964 (T < 0 °C)", "read"),
            Published("magnus.neg.b", 22.4429, "1", "Eq. 22, p. 3964 (T < 0 °C)", "read"),
            Published("magnus.neg.c", 272.44, "°C", "Eq. 22, p. 3964 (T < 0 °C)", "read"),
            Published("solar_constant", 1370, "W m-2", "Eq. 23, p. 3964", "read"),
            Published("hyetograph.alpha", 1 / 3, "1", "text, l. 233 (Callau Poduje 2017)", "read"),
        ),
        flags=(
            "Not validated on humidity near saturation or on wet hours: humidity is checked as"
            " monthly means and hourly means (bias rarely above 5 % daily; relative humidity has"
            " the greatest spread, April to July; hourly means deviate in winter, l. 786-818);"
            " the correlation with daily rainfall is shown, with no wet-hour statistic.",
            "Co-variation: humidity, temperature and radiation are resampled together as one"
            " daily day, conditioned on the rainfall state; hourly humidity follows only from"
            " the hourly temperature, with the dew point fixed at Tmin all day, so a rainy hour"
            " carries no extra humidity. Eq. 21 prints no cap at 100 %.",
            "No wind variable, so no wind direction with rain.",
            "Code: R and Python, 'on request from the author' (l. 905); no repository or"
            " licence printed, so it cannot be run from the paper. The input data (DWD, HYRAS)"
            " are open.",
        ),
        role="process",
    ),
    "gorner2021.edm": Formulation(
        "Euclidean distance model: hourly temperature, precipitation, sunshine, humidity and"
        " wind speed by resampling the most similar observed day",
        "Goerner et al. 2021, Theor. Appl. Climatol. 143:241-265, Sect. 3, Eqs 1-6",
        year=2021,
        authors=(
            "Goerner, Christina",
            "Franke, Johannes",
            "Kronenberg, Rico",
            "Hellmuth, Olaf",
            "Bernhofer, Christian",
        ),
        authors_complete=True,
        authors_from="read",
        checked="c__2020.pdf (the 2026-10-18 drop)",
        doi="10.1007/s00704-020-03426-7",
        structures=("disaggregation",),
        calibrated_on=("gorner2021.saxony_debilt",),
        calibration_note=(
            "An analogue method with no fitted parameter: the day to disaggregate is matched to"
            " the observed day of least Euclidean distance on standardised daily values, equal"
            " weights (Eq. 3), and that day's hourly course is scaled by the ratio of daily"
            " values (Eqs 4-6; temperature shifted). Selection S1 narrows windows of local"
            " observation time; S2 adds DWD objective weather patterns. Rescaled relative"
            " humidity above 100 % is set to 100 %."
        ),
        parameters=(
            Published("window.s1_first", 120, "min", "text, l. 350 (LOD +/- 2 h)", "read"),
            Published("window.s1_second", 60, "min", "text, l. 350 (+/- 1 h)", "read"),
            Published("window.s1_third", 30, "min", "text, l. 350 (+/- 30 min)", "read"),
            Published("window.s1_fourth", 15, "min", "text, l. 350 (+/- 15 min)", "read"),
            Published("rh.cap", 100, "%", "text, l. 393", "read"),
            Published("sunshine.cap", 60, "min", "text, l. 393", "read"),
        ),
        flags=(
            "Humidity near saturation is only partly checked: the observed and the generated"
            " 95th percentile are both 100 % (Tables 2-3), the Fichtelberg median is 90.2 %"
            " against 93.0 % observed, and 3780 (S1) and 2844 (S2) generated hourly values at"
            " Dresden were cut to 100 %. Nothing is checked on wet hours.",
            "Co-variation comes from the observed day: temperature, rain, sunshine, humidity"
            " and wind speed move together as they did in the chosen day. Wind direction is not"
            " handled. Fichtelberg wind speed can come out with an inverse diurnal cycle"
            " (l. 1171).",
            "Needs at least 10 years of hourly observations at or near the site (l. 1547); only"
            " as many days as were observed, so rare events have a small pool.",
            "No code or licence statement in the paper: it cannot be run from the paper.",
        ),
        role="process",
    ),
    "brunetto2018.leaf_litter_decay": Formulation(
        "Mass of fallen grapevine leaves left in a vineyard, as percent remaining falling"
        " exponentially with days after deposition, in the row and between rows",
        "Brunetto et al. 2018, Rev. Cienc. Agrar. 61:1-10, Table 4 (p. 7), as X = X0 exp(-k t)",
        year=2018,
        authors=(
            "Brunetto, Gustavo",
            "Garlete, Luana",
            "Ceretta, Carlos Alberto",
            "Melo, George Wellington Bastos de",
            "Hammerschmitt, Rodrigo Knevitz",
            "Couto, Rafael da Rosa",
        ),
        authors_complete=True,
        authors_from="read",
        checked="gustavo_2018.pdf (the 2026-10-18 drop)",
        doi="10.22491/rca.2018.2624",
        structures=("litter-decay",),
        calibrated_on=("brunetto2018.santana",),
        calibration_note=(
            "Leaves in litter bags, Cabernet Sauvignon, Santana do Livramento (Brazil), bags laid"
            " 16 April 2009 and collected from 0 to 210 days (the paper says May to November"
            " 2009, southern autumn to spring). The form is borrowed (cite as the paper does):"
            " Boer et al. 2007 for the exponential, Paul & Clark 1989 for the half-life"
            " 0.693 / k. t is in days after deposition; X is percent of dry mass remaining."
        ),
        parameters=(
            Published(
                "mass.in_row.x0", 96.17, "%", "Table 4, p. 7 (leaves, mass, in the row)", "read"
            ),
            Published("mass.in_row.k", 0.003, "1/d", "Table 4, p. 7 (printed 'g g-1')", "read"),
            Published("mass.in_row.half_life", 231, "d", "Table 4, p. 7", "read"),
            Published("mass.in_row.r2", 0.90, "1", "Table 4, p. 7", "read"),
            Published("mass.between_rows.x0", 94.43, "%", "Table 4, p. 7", "read"),
            Published(
                "mass.between_rows.k", 0.003, "1/d", "Table 4, p. 7 (printed 'g g-1')", "read"
            ),
            Published("mass.between_rows.half_life", 231, "d", "Table 4, p. 7", "read"),
            Published("mass.between_rows.r2", 0.92, "1", "Table 4, p. 7", "read"),
            Published("n15.in_row.k", 0.05, "1/d", "Table 4, p. 7 (15N excess in leaves)", "read"),
            Published("n15.in_row.half_life", 13.86, "d", "Table 4, p. 7", "read"),
        ),
        flags=(
            "One site and one winter, in a subtropical climate (Cfa, 18.4 °C mean): the rate is"
            " not for a temperate winter. It is the mass of the leaf, not the survival of any"
            " pathogen on it.",
            "k is printed to one significant figure and in 'g g-1'; per day is implied by the"
            " half-lives (0.693 / 0.003 = 231 d).",
            "Table 5 (stems) was not used. The reader reported its P row as k 0.002 against a"
            " half-life of 231 d, which would be inconsistent; the main session read k 0.002"
            " with 346.5 d, which is consistent.",
            "Soil temperature and moisture were not measured; the authors infer they are similar"
            " in the row and between rows.",
        ),
        role="process",
    ),
    "penaquinones2020.canopy_station": Formulation(
        "Daily maximum and minimum canopy air temperature at 0.5 m and 1.2 m as straight lines"
        " in a standard station's daily maximum and minimum at 1.7 m",
        "Pena Quinones et al. 2020, PLOS ONE 15(6):e0234436, Fig. 5 (p. 11)",
        year=2020,
        authors=(
            "Pena Quinones, Andres Javier",
            "Hoogenboom, Gerrit",
            "Salazar Gutierrez, Melba Ruth",
            "Stockle, Claudio",
            "Keller, Markus",
        ),
        authors_complete=True,
        authors_from="read",
        checked="andr_s_2020.pdf (the 2026-10-18 drop)",
        doi="10.1371/journal.pone.0234436",
        structures=("station-to-canopy",),
        calibrated_on=("penaquinones2020.prosser",),
        calibration_note=(
            "Each line is canopy temperature (°C) = a + b x station temperature (°C), fitted to"
            " the daily series of one Chardonnay vineyard at Prosser, Washington. Maximum at"
            " 0.5 m: R2 0.994, n 437; at 1.2 m: R2 0.991; minimum at 0.5 m: R2 0.987, n 436; at"
            " 1.2 m: R2 0.987. Standard errors are not printed. Read from the page image."
        ),
        parameters=(
            Published("max_05.a", -0.155, "°C", "Fig. 5, p. 11 (maximum, 0.5 m)", "read"),
            Published("max_05.b", 1.071, "1", "Fig. 5, p. 11 (maximum, 0.5 m)", "read"),
            Published("max_12.a", -0.384, "°C", "Fig. 5, p. 11 (maximum, 1.2 m)", "read"),
            Published("max_12.b", 1.082, "1", "Fig. 5, p. 11 (maximum, 1.2 m)", "read"),
            Published("min_05.a", -0.728, "°C", "Fig. 5, p. 11 (minimum, 0.5 m)", "read"),
            Published("min_05.b", 0.965, "1", "Fig. 5, p. 11 (minimum, 0.5 m)", "read"),
            Published("min_12.a", -0.414, "°C", "Fig. 5, p. 11 (minimum, 1.2 m)", "read"),
            Published("min_12.b", 0.942, "1", "Fig. 5, p. 11 (minimum, 1.2 m)", "read"),
        ),
        flags=(
            "One Chardonnay vineyard at Prosser, Washington (a dry climate), with the station"
            " about 410-415 m away (the abstract says 410 m, the text 415 m), from December 2015"
            " to 30 June 2017; the daily regressions use 436-437 of the 478 days compared.",
            "The offsets change with the season (a summer minimum 1.1-1.3 °C below the station's,"
            " a summer maximum 1.7-2.2 °C above it, near zero in winter), which one line per"
            " extreme does not show.",
            "The abstract's berry-cluster maxima (1.5 and 4.0 °C above the station, east and"
            " west) disagree with Table 2b (1.67 and 6.14 °C); the abstract's 2.0 °C summer"
            " canopy maximum is not a printed value either (Table 2a: 1.67 and 2.16 °C).",
            "No humidity, wetness or wind was measured in the canopy; it says nothing about"
            " relative humidity or leaf wetness hours.",
        ),
        role="process",
    ),
    "paulescu2023.minute_separation": Formulation(
        "Diffuse fraction of global horizontal irradiance at 1-minute steps from the clearness"
        " index and its hourly and daily values (M2); an eight-predictor version (M1)",
        "Paulescu & Paulescu 2023, Appl. Sci. 13:6558, Eqs 5 and 6 (p. 5)",
        year=2023,
        authors=("Paulescu, Eugenia", "Paulescu, Marius"),
        authors_complete=True,
        authors_from="read",
        checked="eugenia_2023.pdf (the 2026-10-18 drop)",
        doi="10.3390/app13116558",
        structures=("clearness-index-partition",),
        calibrated_on=("paulescu2023.payerne",),
        calibration_note=(
            "M2 (Eq. 6): kd = (1 + a1 kt + a2 kt^2 + a3 (kt khour)^2) / (1 + b1 kt + b2 kt^2 +"
            " b3 (kt kday)^2), kt the 1-minute clearness index and khour, kday the hourly and"
            " daily ones, all from global irradiance; R2 0.917, nMBE 0.007. M1 (Eq. 5) has eight"
            " predictors (kt, dKtc, kde, kday, khour, a persistence term psi, the clear-sky"
            " irradiance Gcs in MJ/(h m2), Kcsi), R2 0.929, nMBE 0.011, whose definitions are in"
            " the paper: numerator 1 + 7.217 Kcsi kt dKtc^2 - 0.656 Kcsi^0.5 kt^2 + 7.947 kde +"
            " 0.187 Gcs - 2.747 kt^2 khour^3 - 15.379 kt psi dKtc^3; denominator 1 + 1.655 Kcsi"
            " dKtc^3 + 14.008 (kday kt)^3 + 17.477 kde + 0.16 Gcs. Fitted on Payerne 2020"
            " (1-minute, elevation above 5 degrees) and tested on 36 BSRN stations with no"
            " overlap in time. M1 gathers predictors of earlier models (a predictor borrowing,"
            " not an equation); no model is said to have shaped the data."
        ),
        parameters=(
            Published("m2.a1", -2.525, "1", "Eq. 6, p. 5 (numerator, kt)", "read"),
            Published("m2.a2", 1.834, "1", "Eq. 6, p. 5 (numerator, kt^2)", "read"),
            Published("m2.a3", -0.204, "1", "Eq. 6, p. 5 (numerator, (kt khour)^2)", "read"),
            Published("m2.b1", -2.578, "1", "Eq. 6, p. 5 (denominator, kt)", "read"),
            Published("m2.b2", 1.902, "1", "Eq. 6, p. 5 (denominator, kt^2)", "read"),
            Published("m2.b3", 1.054, "1", "Eq. 6, p. 5 (denominator, (kt kday)^2)", "read"),
        ),
        flags=(
            "Erbs 1982 is not among the models compared (the reference models are PB, E2, S1, S3"
            " and Y4), so its error at these stations is not given.",
            "Fitted on one station-year at Payerne; the weakest results are at arid stations"
            " (Tamanrasset, DHI nRMSE 52.9 % for M2). The fit statistics do not name their"
            " dataset. Per-station errors are in Fig. 4, which was not extracted.",
            "A 1-minute model: the sweep's hourly weather does not have the inputs.",
        ),
        role="process",
    ),
    "laiti2018.brl_bolzano": Formulation(
        "Hourly diffuse fraction as a logistic function of the clearness index, solar time,"
        " elevation, the daily clearness index and a persistence index (BRL), with the"
        " coefficients refitted to an Alpine valley station",
        "Laiti et al. 2018, Atmosphere 9:117, Eq. 7 and Table 5 (l. 498-508)",
        year=2018,
        authors=(
            "Laiti, Lavinia",
            "Giovannini, Lorenzo",
            "Zardi, Dino",
            "Belluardo, Giorgio",
            "Moser, David",
        ),
        authors_complete=True,
        authors_from="read",
        checked="lavinia_2018.pdf (the 2026-10-18 drop)",
        doi="10.3390/atmos9040117",
        structures=("clearness-index-partition",),
        calibrated_on=("laiti2018.bolzano",),
        calibration_note=(
            "kd = 1 / (1 + exp(a0 + a1 kt + a2 t + a3 h + a4 Kt + a5 psi)), t apparent solar"
            " time, h solar elevation, Kt the daily clearness index, psi the mean of the"
            " clearness index in the hours before and after. The form and the original"
            " coefficients (brl.*) are Lauret et al. 2013's, borrowed and cited by the paper;"
            " the local ones (brl_local.*) are fitted to the Bolzano hours by robust least"
            " squares with a null mean bias, on the same 10,310 hours that validate them."
        ),
        parameters=(
            Published("brl.a0", -5.32, "1", "Table 5, l. 498-508 (original)", "read"),
            Published("brl.a1", 7.28, "1", "Table 5, l. 498-508 (original)", "read"),
            Published("brl.a2", -0.03, "not stated", "Table 5, l. 498-508 (original)", "read"),
            Published("brl.a3", -0.0047, "not stated", "Table 5, l. 498-508 (original)", "read"),
            Published("brl.a4", 1.72, "1", "Table 5, l. 498-508 (original)", "read"),
            Published("brl.a5", 1.08, "1", "Table 5, l. 498-508 (original)", "read"),
            Published("brl_local.a0", -6.67, "1", "Table 5, l. 498-508 (Bolzano)", "read"),
            Published("brl_local.a1", 6.72, "1", "Table 5, l. 498-508 (Bolzano)", "read"),
            Published("brl_local.a2", 0.06, "not stated", "Table 5, l. 498-508 (Bolzano)", "read"),
            Published(
                "brl_local.a3", -0.0072, "not stated", "Table 5, l. 498-508 (Bolzano)", "read"
            ),
            Published("brl_local.a4", 2.01, "1", "Table 5, l. 498-508 (Bolzano)", "read"),
            Published("brl_local.a5", 2.47, "1", "Table 5, l. 498-508 (Bolzano)", "read"),
        ),
        flags=(
            "The local fit is in-sample: the same 10,310 hours fit and validate it, and no split"
            " is stated. Its diffuse rMBE of 0.00 % is imposed by the fit.",
            "In the same valley Erbs 1982 has a diffuse rRMSE of 37.23 % and rMBE 7.35 % (Table 3,"
            " l. 430), and direct rRMSE 21.20 % (Table 4); the paper does not print the Erbs"
            " equation.",
            "Orographically shadowed hours (2,098 of 10,310) raise the mean diffuse bias of the 13"
            " models to 27 % against 7 % unshadowed; the sky view factor is 0.788.",
            "Units of t and h are not stated in the equation's text; the validation excludes solar"
            " elevations below 7 degrees.",
        ),
        role="process",
    ),
    "sanderson2022.taf": Formulation(
        "Topographic amplification factor TAF = W H / A of a valley cross-section from a 90 m"
        " DEM, and its down-valley gradient, to map where cold air pools",
        "Sanderson et al. 2022, J. Appl. Meteorol. Climatol. 61:1893-1904, Sect. 2 and 3"
        " (l. 260-270)",
        year=2022,
        authors=(
            "Sanderson, Michael G.",
            "Teixeira, Marta",
            "Graca, Antonio",
        ),
        authors_complete=True,
        authors_from="read",
        checked="michael_2022_2.pdf (the 2026-10-18 drop)",
        doi="10.1175/JAMC-D-21-0263.1",
        structures=("cold-air-pool",),
        structures_note=(
            "TAF is a terrain index of how much more a valley cools than an open column of air"
            " of the same width (Whiteman 1990; Lundquist et al. 2008, which this paper follows);"
            " it is a map of where cold air is likely to collect, not a temperature."
        ),
        calibration_note=(
            "Nothing is fitted. TAF is computed from the SRTM v4.1 90 m DEM alone: for each"
            " valley-floor pixel a transect gives W (valley width, from the edge coordinates),"
            " H (height from the transect low point to the lower of the two local maxima, the"
            " valley top) and A (cross-sectional area, by the trapezium rule); TAF = W H / A,"
            " the text layer's '5' being '=' in the page image. The down-valley gradient is a"
            " least-squares line over 5 contiguous pixels, tested at 5 %. Cold pools were then"
            " identified separately from 15-min data at the Leda pair of stations"
            " (sanderson2022.stations); no TAF value is compared with those events in the text"
            " read, so the station data are not a calibration of TAF."
        ),
        parameters=(
            Published(
                "transect.tributary_radius", 10, "pixel", "text, l. 231 (about 900 m)", "read"
            ),
            Published("transect.main_radius", 20, "pixel", "text, l. 233 (about 1800 m)", "read"),
            Published("dem.resolution", 90, "m", "text, l. 165 (SRTM v4.1, 3 arc s)", "read"),
        ),
        flags=(
            "Printed TAF results are ranges only: most values along the main Douro channel 1.4"
            " to 2.0, a few reaches 2.0 to 2.8 on convex sides (l. 266-270); no threshold of TAF"
            " for pooling and no units for the gradient are printed.",
            "Cold-pool events are counted at one pair of stations (Leda 2, 318 m, and Leda 3,"
            " 163 m, 155 m apart): inversion of at least 1 °C between sunset and sunrise,"
            " strong above 4 °C (l. 259-261, 317-318). Pools shallower than about 30 m are not"
            " recorded (l. 174, 598). These thresholds and the event counts are dataset facts,"
            " not parameters of TAF.",
            "The event total is 834 (32 % of nights, l. 368), but Table 2's rows sum to 796"
            " (182+240+79+0+6+11+0+53+225, checked in the page image); the 28 % marginal share"
            " fits 796. The abstract says seven categories and Table 2 has nine rows, two of"
            " them zero. Categories were assigned by eye.",
            "Humidity and leaf-wetting sensors exist at each station (l. 162-164) but no"
            " humidity, dew point or wetness result is printed: nothing here says how wet the"
            " air in a pool is.",
            "Station data are 15 min, not hourly, and are not open (commercial sensitivity,"
            " l. 628); daily values of the nine stations are in ECA&D (l. 122, 551).",
        ),
        role="process",
    ),
    "kuwagata2024.canopy_dew": Formulation(
        "One-layer energy-balance model of dew on a plant canopy: condensation rate from"
        " effective radiation, air temperature, relative humidity and an exchange velocity kL;"
        " the critical relative humidity for dew; potential and reference dew amounts",
        "Kuwagata et al. 2024, Agric. For. Meteorol. 354:109911, Sect. 2 and 3, Eqs 1-28",
        year=2024,
        authors=(
            "Kuwagata, Tsuneo",
            "Maruyama, Atsushi",
            "Kondo, Junsei",
            "Watanabe, Tsutomu",
        ),
        authors_complete=True,
        authors_from="read",
        checked="tsuneo_2024.pdf (the 2026-10-18 drop; the manuscript's author line)",
        doi="10.1016/j.agrformet.2024.109911",
        structures=("dew-energy-balance",),
        structures_note=(
            "Dew is a result of the canopy energy balance (Eq 1; bulk fluxes Eqs 4-5; Eq 7,"
            " dW/dt = -E_L / rho_w); the model has no relative-humidity threshold, and the"
            " critical relative humidity (Eq 8, approximated by Eq 24) is an output."
        ),
        calibrated_on=("kuwagata2024.kumamoto",),
        calibration_note=(
            "Not fitted. Checked against rice-canopy dew at Kumamoto, 18-27 August and"
            " 24 September-3 October 2003 (measured on four nights), the same observations as"
            " Maruyama et al. 2023 (literature/maruyama2023), by the reference dew amount W0"
            " (Eq 25) and the potential dew amount Wp (Eq 26). A multilayer reference (MLC, a"
            " MINCER derivative, Watanabe et al. 2004, 2005) is run on the same data and was"
            " itself checked against them, so W0 and Wp against MLC is not independent. The"
            " canopy length scale DL = 0.1 m was chosen 'for comparison with the measured"
            " data' (l. 629); how is not said. No error statistic is printed: measured against"
            " MLC 'fairly consistent', W0 'roughly consistent', Wp 'slightly larger'"
            " (l. 1213-1223)."
            " The structure is Kondo (1996)'s one-layer model (l. 411; not in the catalogue)"
            " and the maximum rate of Eq 10 is Monteith's (1961); neither is a record here."
        ),
        parameters=(
            Published("stefan_boltzmann", 5.67e-8, "W m-2 K-4", "text, l. 307", "read"),
            Published("emissivity", 1.0, "1", "text, l. 309 and 403 (assumed, black body)", "read"),
            Published("beta", 1.0, "1", "text, l. 403 (assumed: all leaves wet)", "read"),
            Published("water_density", 1000, "kg m-3", "text, l. 401 (10^3 in the paper)", "read"),
            Published("surface_pressure", 1013, "hPa", "text, l. 409", "read"),
            Published("time_step", 1800, "s", "text, l. 613", "read"),
            Published("wind_minimum", 0.05, "m s-1", "text, l. 613", "read"),
            Published(
                "min_evaporation_coefficient", 0.05, "1", "text, l. 615 (chL, Eq 27b)", "read"
            ),
            Published("albedo_daytime", 0.3, "1", "text, l. 617 (paddy rice)", "read"),
            Published("transmittance_daytime", 0.2, "1", "text, l. 617 (paddy rice)", "read"),
            Published("canopy_length_scale", 0.1, "m", "text, l. 629 (rice, DL)", "read"),
            Published(
                "wet_dew_threshold", 0.01, "mm", "text, l. 1374 (leaf wetness duration)", "read"
            ),
        ),
        flags=(
            "Dew forms below the engine's wetness rule: the paper derives a critical relative"
            " humidity that falls with strong radiative cooling and low air temperature, and"
            " states that for an effective radiation below -100 W m-2 condensation can occur at"
            " relative humidity under 0.4 (l. 1576-1578). Fig. 4 (not rendered by the reading;"
            " its axis runs to -150 W m-2) plots it, near 1.0 at zero effective radiation. At"
            " -100 W m-2 and 20 °C the maximum rate is 1.42 mm per day at 0.9, 0.37 mm per day"
            " at 0.6 (26 %) and 0.058 mm per day at 0.4 (4 %) (l. 1582-1589). The engine's"
            " RH >= 90 % stand-in is therefore not this model's rule; the paper itself notes"
            " empirical rules near 0.9 (l. 1566).",
            "A rice paddy, not a vineyard; one site, four measured nights, warm temperate"
            " humid subtropical climate (l. 643-653). Leaf wetness is the time dew exceeds"
            " 0.01 mm, afternoon to 07:30 local time (l. 1374).",
            "Needs effective radiation (measured downward longwave here), air temperature,"
            " humidity, wind (corrected from 2 m to canopy top) and canopy properties; the exchange"
            " velocity kL is from an empirical equation (Watanabe and Mizutani 1996). Eqs 1-7 and"
            " 21-24 were checked in page images, Eqs 8-20, 22-23, 27b and 28 from the text layer.",
            "Data: DOI 10.17632/fmvr43csy3.3 (Mendeley Data); licence not printed.",
        ),
        role="process",
    ),
    "nakamura2005.radiative_error": Formulation(
        "Radiative error of a naturally ventilated shield's air temperature, RE = C0 + C1 X,"
        " X = Rad / (rho Cp T U), from shortwave radiation by day and net radiation by night"
        " and the wind speed",
        "Nakamura & Mahrt 2005, J. Atmos. Oceanic Technol. 22:1046-1058, Eqs 11-12 (p. 1054) and"
        " Table 3 (p. 1055)",
        year=2005,
        authors=("Nakamura, Reina", "Mahrt, L."),
        authors_complete=True,
        authors_from="read",
        checked="reina_2005.pdf (the 2026-10-18 drop)",
        structures=("shield-radiative-error",),
        calibrated_on=("nakamura2005.corvallis",),
        calibration_note=(
            "Fitted to bin averages of the 30-min error of an Onset HOBO Pro thermistor in a"
            " naturally ventilated Davis 7714 multiplate shield against an aspirated RTD (RM"
            " Young 43408), both at 1 m over flat grassland at the Hyslop Experimental Station,"
            " Corvallis, Oregon, 14 March to 30 August 2002 (R2 0.98 day, 0.94 night). Tested"
            " with the 2002 coefficients on a second dataset at the same site, 15 July to"
            " 30 August 2003: daytime RMSE 0.29 to 0.13 °C, night 0.05 to 0.04 °C (Table 5)."
            " Rad is the shortwave outside the shield by day and the net radiation by night"
            " (W m-2), T_HB the sensor's air temperature in kelvin, U the 30-min wind speed"
            " (m s-1). The aspirated reference's own radiative error is assumed small."
        ),
        parameters=(
            Published("day.c0", 0.13, "°C", "Table 3, p. 1055 (day, shortwave)", "read"),
            Published(
                "day.c1", 373.40, "°C per unit X", "Table 3, p. 1055 (day, shortwave)", "read"
            ),
            Published("night.c0", 0.047, "°C", "Table 3, p. 1055 (night, net radiation)", "read"),
            Published(
                "night.c1",
                355.84,
                "°C per unit X",
                "Table 3, p. 1055 (night, net radiation)",
                "read",
            ),
            Published("air_density", 1.2, "kg m-3", "text under Eq. 11, p. 1054", "read"),
            Published("specific_heat", 1004, "J K-1 kg-1", "text under Eq. 11, p. 1054", "read"),
        ),
        flags=(
            "One shield (Davis 7714 multiplate) and one sensor (HOBO Pro thermistor), over grass at"
            " one Oregon site in spring and summer; the coefficients may not hold for a surface of"
            " another albedo (l. 568) or for another shield.",
            "The error it describes is large by day: a mean of 0.39 °C, above 0.5 °C in 22.9 % of"
            " daytime periods and above 1.0 °C in 2.6 % (l. 508-509); at night the mean is"
            " -0.002 °C and the error is below -0.5 °C in 4.6 % of periods (l. 513-514).",
            "Higher-order terms in X were not significant by an F test (l. 553); the daytime fit"
            " breaks down below X = 1.0e-4 and the correction is neglected there (3.1 % of"
            " daytime data, l. 581-584).",
        ),
        role="observation",
    ),
    "magarey2006.sweb": Formulation(
        "Canopy wetness from a water budget and an energy balance (SWEB): storage C = LAI x Cl,"
        " rain intercepted as 1 - exp(-0.5 LAI), a wet-area index (S/C)^0.67 scaled by Wmax,"
        " evaporation by the Tanner-Fuchs combination equation, night dew from half the canopy"
        " net radiation; the canopy is wet when the index exceeds 0.1",
        "Magarey, Russo & Seem 2006, Agric. For. Meteorol. 139:373-381, Eqs 1-15 (pp. 375-377)",
        year=2006,
        authors=("Magarey, R. D.", "Russo, J. M.", "Seem, R. C."),
        authors_complete=True,
        authors_from="read",
        checked="1-s2.0-S0168192306002371-main.pdf (the 2026-10-19 drop; the author line)",
        doi="10.1016/j.agrformet.2006.08.016",
        structures=("canopy-water-balance", "dew-energy-balance"),
        structures_note=(
            "A water store filled by rain (Eq 8) and dew (Eq 12) and emptied by evaporation"
            " (Eq 11), with wetness read from the wet-area index Wind = (S/C)^0.67 (Eq 3), not"
            " from a humidity. The dew term and the evaporation come from one Tanner-Fuchs"
            " energy balance on a big leaf at mean canopy height."
        ),
        calibrated_on=("magarey2006.geneva_adelaide",),
        calibration_note=(
            "Not fitted to those data: they are what it was validated against (visual wetness"
            " at Geneva NY in 1997 and 1998 and at Adelaide in 1998; mean absolute error 1.5,"
            " 0.8 and 0.7 h, Table 3; literature/magarey2006b). The transfer-coefficient"
            " constants cd 8.7 and cf 2.0 were fitted in controlled laboratory tests of"
            " drying drops and films on an artificial leaf (Magarey et al. 2005a,"
            " literature/magarey2005b; this paper prints none of those data). The energy"
            " balance is Tanner & Fuchs 1968's combination formula (l. 110), the transfer"
            " coefficient the generic form of Bird et al. 1960 (l. 111), the interception"
            " Norman & Campbell 1983's (Eq 8), the canopy storage Noilhan & Planton 1989's"
            " (l. 187); none is a record here, and each is credited, not read. Daytime net"
            " radiation is ignored because the first sunlit leaf layer absorbs 94 % of the"
            " solar radiation (Smart & Robinson 1991, l. 122); net radiation enters only for"
            " night condensation. Roughness length is Z/10 and zero-plane displacement 2/3 Zc"
            " (Eq 15), assumed. Code on request from the first author; no licence printed."
        ),
        parameters=(
            Published(
                "canopy_storage_per_leaf_area",
                0.02,
                "cm",
                "p. 376, l. 187 (Cl, 'a commonly accepted value', credited to Noilhan & Planton"
                " 1989); 0.2 mm per unit LAI",
                "read",
            ),
            Published(
                "w_max",
                0.5,
                "1",
                "p. 376, l. 229 (grapes; from the authors' lab tests), and 'Wmax, was assumed as"
                " 0.5' in the validation (magarey2006b, p. 365); used directly, not built from"
                " Wd, Wf and p (Eq 5)",
                "read",
            ),
            Published(
                "w_th", 0.1, "1", "p. 375, l. 152 (threshold on the wet-area index Wind)", "read"
            ),
            Published("wind_exponent", 0.67, "1", "p. 375, Eq 3, Wind = (S/C)^0.67", "read"),
            Published(
                "interception_k",
                0.5,
                "per unit LAI",
                "p. 376, Eq 8, I = (1 - exp(-0.5 LAI)) P, after Norman & Campbell 1983",
                "read",
            ),
            Published(
                "dew_radiation_share",
                0.5,
                "1",
                "p. 377, Eq 12 (night dew from 0.5 of the canopy net radiation)",
                "read",
            ),
            Published(
                "c_d",
                8.7,
                "cm^0.5 min^-0.5",
                "p. 377, l. 284 (drops; from Magarey et al. 2005a)",
                "read",
            ),
            Published(
                "c_f",
                2.0,
                "cm^0.5 min^-0.5",
                "p. 377, l. 284 (films; from Magarey et al. 2005a)",
                "read",
            ),
            Published("alpha", 1.3, "1", "p. 377, Eq 15 (wind profile shape, assumed)", "read"),
        ),
        flags=(
            "Wetness is the wet-area index above 0.1 (a fraction of leaves, l. 148-153), not a"
            " humidity and not an amount of water, and no comparison with a relative-humidity"
            " rule is printed. Turned into stored water, S/C > 0.1^(1/0.67) = 0.032, which is"
            " 0.0064 mm at LAI 1.0 and 0.013 mm at LAI 2.0 with Cl = 0.2 mm per unit LAI (own"
            " calculation, not printed); Agrarium's micro.wet_threshold_mm (0.02 mm, range"
            " 0.005-0.05) is the same order.",
            "In Agrarium's units Cl = 0.2 mm per unit LAI, against micro.storage_mm_per_lai 0.25"
            " (range 0.1-0.5). Interception 1 - exp(-0.5 LAI) is 0.39 at LAI 1, 0.63 at 2 and"
            " 0.78 at 3 (own calculation), against micro.interception 0.6 (0.3-0.9): equal near"
            " LAI 1.8. Storage and interception carry all of SWEB's LAI effect (wetness 130 to"
            " 650 min for LAI 1 to 4, l. 335, a text range; Fig. 1A reads about 150 to 640);"
            " there is no separate density term, so micro.density_drying_slowdown has no"
            " counterpart (own reading).",
            "Dew is a night term only, from half the canopy net radiation, so it is capped by"
            " the radiative loss: at a canopy net radiation of -100 W m-2 (an assumed value, not"
            " printed) and Delta/(Delta + gamma) near 0.7, about 0.05 mm per hour (own"
            " calculation). There is no leaf-cooling or dew-point input as in"
            " micro.leaf_cooling_c and micro.dew_rate_mm_h_per_c.",
            "The paper and its companion (magarey2006b) credit Cl differently: here 0.02 cm to"
            " Noilhan & Planton 1989, with 0.018 for grapes from Hoppmann & Wittich 1997 and"
            " 0.02 from the authors' unpublished lab tests (p. 378); there 0.02 to Hoppmann &"
            " Wittich 1997 and lab values of 0.022 (Concord) and 0.016 (Chancellor). Wmax 0.5"
            " is from lab tests on young (wettable) and mature (non-wettable) grape leaves,"
            " not tabulated. The 2005 review chapter by the same authors (magarey2005chapter,"
            " Table 10-2, p. 219) gives water storage 0.20 cm for a standard sensor, credited"
            " to the same Noilhan & Planton 1989: tenfold the 0.02 cm here; both are recorded.",
            "Wd, Wf and p (Eq 5) are printed nowhere found: not in this paper, its validation"
            " (magarey2006b), the drop-and-film paper (magarey2005b), the 2005 review chapter"
            " (magarey2005chapter), the uses by Dalla Marta et al. 2006 (dallamarta2006), Kim et"
            " al. 2005 (kim2005), Gil et al. 2015 (gil2015), Kudinha 2014 or Amir 2016. The"
            " authors and every user ran SWEB with Wmax = 0.5 set directly, so Eq 5 is not needed"
            " to run it. Amir 2016 reads Wmax 0.5 as a canopy of half mature and half immature"
            " leaves and credits that to Magarey 2006, which does not say it.",
            "Units of Eqs 9-10, checked at two sources: the 2005 chapter (Eq 3, p. 206, page"
            " image) prints the same combination equation with the same unit for every symbol"
            " as Table 2 here (Delta and delta mb per C, lambda J/g, Rn J/(min cm2), rho g/cm3,"
            " Cp J/(g C), h cm/min, vapour pressures mb). Worked through, the right side is"
            " g/(cm2 min), which is cm/min of water at 1 g/cm3; the printed units are"
            " consistent, and only the water density is implicit. Ep is named a 'latent heat"
            " flux density' but carries cm/min. Eq 13, h = c Uc^0.5 with c in cm^0.5 min^-0.5"
            " and Uc in cm/min, also gives cm/min. An earlier version of this record called"
            " Eqs 9-10 inconsistent; that was wrong.",
            "Time step, as printed: 'The model was run in 10 min time steps' in the sensitivity"
            " runs (p. 378); the"
            " validation scored SWEB at 1-h intervals at all three sites and at 10-min"
            " intervals at LO98 and AA98 (magarey2006b, p. 364-365), from weather logged every"
            " 60 s with hourly summaries, without saying at which step the model itself ran."
            " The 2005 chapter says wetness models are 'usually run using hourly weather data'"
            " (p. 207). Every later use ran it hourly: Gil et al. 2015 ('the model ran on an"
            " hourly basis', from 10-min data averaged per hour), Kudinha 2014, Amir 2016,"
            " Kim et al. 2005.",
            "Table 3 and the text disagree: the text gives MAE 1.5-1.8 h at the humid site and"
            " 0.9 h at Adelaide (l. 366-368), the table 1.5 and 0.8 h at Geneva and 0.7 h at"
            " Adelaide. The sign of the mean error is not printed (visual minus SWEB, from"
            " the means). The symbol whose value depends on crop type (l. 311) is missing in"
            " the text and the page image.",
            "Can it run: yes, with stated choices. Every equation is printed and the units"
            " close (above). A tool must set: Wmax 0.5 directly (as the authors did); a time"
            " step of 10 min (the authors' sensitivity runs) or 1 h (their validation scoring"
            " and every later use); Cl 0.02 cm (the 2006 papers) rather than 0.20 cm (the 2005"
            " chapter's sensor); canopy net radiation at night, which SWEB takes as an input"
            " and the paper measured, so a tool without it must estimate it; and the standard"
            " constants (lambda, delta, rho, Cp, Delta(T)) at its own choice, since none is"
            " printed. Not printed anywhere found: Wd, Wf, p; the symbol at l. 311."
            " Pages 375-378 here, p. 206 and 219 of the chapter and p. 364-365 of the"
            " validation were read on the page images (2026-10-19).",
        ),
        role="process",
    ),
    "reuveni1998.leaf_age": Formulation(
        "Downy mildew severity and sporulation of grape leaf discs by leaf position on the"
        " shoot (young top leaves, middle, old bottom leaves)",
        "Reuveni 1998, J. Phytopathol. 146:525-530, Table 1 (p. 528) and Figs 1-3",
        year=1998,
        authors=("Reuveni, M.",),
        authors_complete=True,
        authors_from="read",
        checked="the Wiley copy of the 2026-10-19 drop (single author, initial only)",
        structures=("age-resistance",),
        calibrated_on=("reuveni1998.golan",),
        calibration_note=(
            "No curve is fitted: three leaf positions measured. Leaf discs (12 mm, 10 per"
            " leaf) of field Cabernet Sauvignon, positions counted from the shoot tip: top"
            " leaves 3 + 4, middle 15 + 16, bottom 29 + 30 (l. 151-152); in the peroxidase"
            " experiment 2, 14 + 15 and 28 + 29 (l. 270-271). Each disc got one 5 ul drop of 2e4"
            " sporangia per ml; severity 0-4 (0 none; 4 over 50 % of the disc infected and"
            " sporulating); sporangia were counted per cm2 of disc. Field symptoms were not seen"
            " on leaves from number 12 down in 1993 and from 27 down in 1995 (Figs 1-2,"
            " p. 527-528; values only in the plots). Spray inoculation of attached greenhouse"
            " plants (2e4 sporangia per ml, rated 10 days later) gave severity near 3.5-4 for"
            " leaves 1-6 falling to near 0 by leaf 18 (Fig. 3, read from the figure,"
            " approximate). Leaf age in days was not measured; position stands for age"
            " (l. 156)."
        ),
        parameters=(
            Published("disc_sev_d4.top", 0.4, "scale 0-4", "Table 1, p. 528 (4 days)", "read"),
            Published("disc_sev_d4.middle", 0.1, "scale 0-4", "Table 1, p. 528 (4 days)", "read"),
            Published("disc_sev_d4.bottom", 0.03, "scale 0-4", "Table 1, p. 528 (4 days)", "read"),
            Published("disc_sev_d5.top", 1.2, "scale 0-4", "Table 1, p. 528 (5 days)", "read"),
            Published("disc_sev_d5.middle", 1.0, "scale 0-4", "Table 1, p. 528 (5 days)", "read"),
            Published("disc_sev_d5.bottom", 0.3, "scale 0-4", "Table 1, p. 528 (5 days)", "read"),
            Published("disc_sev_d7.top", 2.4, "scale 0-4", "Table 1, p. 528 (7 days)", "read"),
            Published("disc_sev_d7.middle", 2.3, "scale 0-4", "Table 1, p. 528 (7 days)", "read"),
            Published("disc_sev_d7.bottom", 1.0, "scale 0-4", "Table 1, p. 528 (7 days)", "read"),
            Published("sporangia.top", 13874, "per cm2 of disc", "Table 1, p. 528", "read"),
            Published("sporangia.middle", 8547, "per cm2 of disc", "Table 1, p. 528", "read"),
            Published("sporangia.bottom", 4870, "per cm2 of disc", "Table 1, p. 528", "read"),
        ),
        flags=(
            "Leaf position, not leaf age in days, and one cultivar (Cabernet Sauvignon) in the"
            " disc test; the middle leaves do not differ from the top at 5 and 7 days (the"
            " letters as printed, the test not checked), so the fall is between middle and"
            " bottom. Discs in dishes at 19 then 24 °C are not a field canopy.",
            "Golan Research Institute, Israel, as printed; field weather and site are not given."
            " The field ratings (1993 Cabernet Sauvignon, Chardonnay and Sauvignon Blanc; 1995"
            " Cabernet Sauvignon) are in the figures only, and the 1993 methods and the Fig. 1"
            " caption disagree on the plots and shoots (l. 281, 338).",
            "The paper is an OCR of a scan; Table 1 was read in the page image. Table 3's unit"
            " header (umol glucose per g per 10 min) and its footnote (milliunits per g)"
            " disagree (l. 528, 535); the enzyme tables are not recorded here.",
        ),
        role="process",
    ),
    "dhakar2025.leaf_wetness": Formulation(
        "Leaf wetness of a flat sensor plate (M1) from dew by energy balance, rain"
        " interception capped at 0.6 mm per event and evaporation by the SWEB combination"
        " equation; M2 adds a dew-point-depression gate on dew",
        "Dhakar, Amogi, Kothawade & Khot 2025, Agric. For. Meteorol. 363:110399, Eqs 2-11 and"
        " Table 2",
        year=2025,
        authors=(
            "Dhakar, Rajkumar",
            "Amogi, Basavaraj R.",
            "Kothawade, Gajanan S.",
            "Khot, Lav R.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="1-s2.0-S016819232500019X-main.pdf (the 2026-10-19 drop; the author line)",
        doi="10.1016/j.agrformet.2025.110399",
        borrows=("magarey2006.sweb",),
        structures=("dew-energy-balance", "canopy-water-balance"),
        structures_note=(
            "A wetness store (LW = Df + Ri - E, Eq 2) filled by dew from an energy balance on"
            " a plate (Eqs 3-6) and by rain, emptied by evaporation (Eqs 7-10). Wetness is"
            " the store above 0 mm. Evaporation and the weighting c = Wmax Cf + (1 - Wmax) Cd"
            " are SWEB's (l. 238-245, 265)."
        ),
        calibrated_on=("dhakar2025.awn",),
        calibration_note=(
            "Cd, Cf, alpha, DPDc, Wmax, Wf, N, Dp and Lp were fitted by Bayesian optimisation"
            " (maximising the F1 score of 15-min wet or dry) to the leaf wetness sensor of one"
            " station, Havillah (l. 315-326); Table 2 prints the values and the Morris bounds."
            " Havillah is also one of the ten validation stations, so that validation is not"
            " independent. The M3 and M4 thresholds (2.2 °C; RH 95 %) were chosen against the"
            " same sensor data. Evaporation and the c weighting are computed from SWEB"
            " (magarey2006.sweb); the DPDc of 2.2 °C is Sentelhas et al. 2008's (a value, not"
            " an equation computed); the 0.6 mm interception cap is Sentelhas et al. 2006's."
            " The fitted Cd and Cf replace SWEB's 8.7 and 2.0, which came from laboratory"
            " drying tests."
        ),
        parameters=(
            Published("alpha", 1.41, "1", "Table 2 (Bayesian value; bounds 0.5-2.0)", "read"),
            Published(
                "c_d",
                4.23,
                "cm^0.5 min^-0.5",
                "Table 2 (Bayesian value; printed bounds 5-10, so outside them)",
                "read",
            ),
            Published(
                "c_f", 1.78, "cm^0.5 min^-0.5", "Table 2 (Bayesian value; bounds 1-3)", "read"
            ),
            Published(
                "dpdc.table2", 1.85, "°C", "Table 2 (Bayesian value; bounds 1.5-5.0)", "read"
            ),
            Published("dpdc.text", 2.2, "°C", "text, l. 302 (from Sentelhas et al. 2008)", "read"),
            Published(
                "w_max",
                0.718,
                "1",
                "Table 2 (max fraction of the sensor's surface wet, not of a canopy)",
                "read",
            ),
            Published("w_f", 0.368, "1", "Table 2 (wettable fraction)", "read"),
            Published("stomata_n", 25e7, "m-2", "Table 2 (bounds 15e7-30e7)", "read"),
            Published("pore_diameter", 6.23, "um", "Table 2 (bounds 6-7)", "read"),
            Published("pore_length", 2.5, "um", "Table 2 (bounds 1-3)", "read"),
            Published("z_ref", 0.2, "m", "Table 2 (fixed)", "read"),
            Published("z_c", 0.15, "m", "Table 2 (fixed)", "read"),
            Published("plate_length", 0.12, "m", "Table 2 (D, fixed)", "read"),
            Published("plate_width", 0.07, "m", "Table 2 (Wl, fixed)", "read"),
            Published("rain_cap", 0.6, "mm", "text, l. 233-234 (per event)", "read"),
        ),
        flags=(
            "Table 2 prints Cd = 4.23, outside its own bounds of 5-10, and DPDc = 1.85 °C where"
            " the text sets 2.2 °C for M2 (l. 302); the paper does not say which value M2"
            " used. The text says the fitted values are in Table 1 (l. 326); they are in"
            " Table 2.",
            "The abstract gives M3 and M4 mean absolute errors of 10.16 and 7.03 h; the results"
            " give MAE 2.0-7.03 h and RMSE 4.53-10.16 h (l. 439-441), so the abstract's"
            " figures look like RMSE maxima. M2 daily: R2 0.84, RMSE 1.13 h and MAE 0.34 h"
            " (abstract); by station RMSE 0.76-1.95 h and MAE 0.2-0.81 h. M1 RMSE 0.76-2.14 h.",
            "It models the sensor, not a canopy: a flat plate 0.12 by 0.07 m at 0.15 m, with"
            " no leaf area index; Wmax is the sensor's wet fraction, and W = Wf x Wmax where"
            " SWEB has Wind x Wmax. Wetness is the store above 0 mm; the truth it is scored"
            " against is the sensor's normalised output above 0.4 (701 counts). Ten"
            " Washington AgWeatherNet stations, 15-min data, January 2019 to February 2023;"
            " no crop is named.",
            "M4, the relative humidity rule, is RH > 95 %, chosen from 85, 90 and 95 % against"
            " the sensor; the 90 % result is not printed, so the paper gives no verdict on the"
            " engine's RH >= 90 %. M4 accuracy 75-80 %, M3 60-75 % (l. 388).",
            "Data on request; no code or licence printed. Eq 5, the stomatal resistance, cites"
            " no source; the text cites Eq 9 where Eq 8 is meant (l. 485-487).",
        ),
        role="process",
    ),
    "molitor2014.shoots": Formulation(
        "Four leaves unfolded by the heat sum observed at that stage",
        "Molitor et al. 2014, doi:10.5344/ajev.2013.13066",
        year=2014,
        authors=(
            "Molitor, Daniel",
            "Junk, Jürgen",
            "Evers, Danièle",
            "Hoffmann, Lucien",
            "Beyer, Marco",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2014-molitor-10-5344-ajev-2013-13066.pdf",
        structures=("degree-day-phenology",),
        calibrated_on=("molitor2014.mt60",),
    ),
    "cooptera.shoots_derived": Formulation(
        "Shoots at 10 cm as 100 degree-days above 10 °C (derived here; the policy's until v0.8)",
        "derived in this repository (SOURCES.md §8), from the thesis's 25 °C·days a leaf",
        made_by="cooptera",
        structures=("degree-day-phenology",),
    ),
    "amerine1944.winkler_index": Formulation(
        "The Winkler index: degree-days above 10 °C from 1 April",
        "Amerine & Winkler 1944, as Wikipedia summarises it (SOURCES.md)",
        year=1944,
        authors=("Amerine, M.A.", "Winkler, A.J."),
        authors_from="trail",
        checked="Molitor et al. 2014's reference list (held)",
        structures=("degree-day-climate-index",),
        role="reference",
    ),
    "ferguson2014.cold_hardiness": Formulation(
        "Bud cold hardiness and budbreak, 23 cultivars",
        "Ferguson et al. 2014, doi:10.5344/ajev.2013.13098, Table 4",
        year=2014,
        authors=(
            "Ferguson, John C.",
            "Moyer, Michelle M.",
            "Mills, Lynn J.",
            "Hoogenboom, Gerrit",
            "Keller, Markus",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2014-ferguson-10-5344-ajev-2013-13098.pdf",
        borrows=("ferguson2011.hardiness",),
        structures=("cold-hardiness",),
        calibrated_on=("ferguson2014.prosser",),
    ),
    "ferguson2011.hardiness": Formulation(
        "The hardiness model's equations 1-6",
        "Ferguson et al. 2011, Annals of Botany 107: 389-396, read on PubMed Central; not held",
        year=2011,
        authors=("Ferguson", "Tarara", "Mills", "Grove", "Keller"),
        authors_from="trail",
        checked="cold_hardiness.py's docstring",
        structures=("cold-hardiness",),
    ),
    "vitimeteo.oospores": Formulation(
        "Oospore maturity at 140 degree-days above 8 °C",
        "VitiMeteo's rule, Siegfried et al. 2004, as Leoni et al. 2026 describe it; not held",
        year=2004,
        authors=("Siegfried, W.", "Viret, O.", "Bloesch, B.", "Bleyer, G.", "Kassemeyer, H.H."),
        authors_from="trail",
        checked=(
            "Leoni et al. 2026's reference list (held) for the 2004 authors; the rule in"
            " dubuis2012_vitimeteo.pdf, page images (literature/dubuis2012)"
        ),
        structures=("thermal-time-oospore-threshold",),
        added_authors=(
            Added(
                (
                    "Breuer, M.",
                    "Krause, R.",
                    "Naef, A.",
                    "Huber, M.",
                    "Huber, B.",
                    "Steinmetz, V.",
                ),
                "snippet",
                "VitiMeteo's project members, as a search summary lists them",
            ),
        ),
        calibration_note=(
            "Not recorded. Cooptera's origins.py places the rule's fit at Changins; Siegfried"
            " et al. 2004 is not held, and Leoni et al. 2026 do not say where the 140 °C-day"
            " threshold was fitted (read 2026-10-08). Dubuis et al. 2019 (read 2026-10-08):"
            " VitiMeteo's parameters 'were adjusted according to' observations in an external"
            " laboratory and in fields, oospore maturation being the example, with no place or"
            " years named. Bleyer et al. 2008 (read 2026-10-08) prints no oospore rule."
            " Dubuis et al. 2012, Revue suisse Vitic. Arboric. Hortic. 44(3):192-198, p. 196"
            " (read 2026-10-12, literature/dubuis2012), is where the rule is printed: 140 °C"
            " at the 8 °C threshold from 1 January, Fig. 1 (p. 194) 140-160 after Gehmann 1987."
            " Dubuis et al. 2012: since 2003 the oospore maturity in an"
            " outdoor test, first infections and the untreated plot's epidemic at Changins"
            " 'serve to validate' the model, whose parameters experts adjust; in six of nine"
            " years (2003-2011) the end of incubation met the first oil spots, in 2005 and 2007"
            " the model was more than two weeks early. Calibration on those observations is"
            " inferred, not stated"
        ),
        flags=(
            "Hoppmann & Wittich 1997 (Z. PflKrankh. PflSchutz 104:533-544, p. 536; read"
            " 2026-10-09) print the same form for the Geisenheim (DWD) model with 170"
            " degree-days above a daily mean of 8 °C 'during spring', not 140. Gessler et al."
            " 2011 (Phytopathol. Mediterr. 50:3-44, p. 7; read 2026-10-09) give Gehmann et"
            " al. 1987's German rule as 160 °C·days above 8 °C from 1 January, at 2 m.",
            "The threshold varies by source (read 2026-10-10): VitiMeteo's Luxembourg user guide"
            " calls it an adjustable setting, 'normalerweise 160 Gradtage' (literature/"
            "institutvitivinicole2015); Pertot et al.'s SafeCrop booklet credits Gehmann 1987 with"
            " 170 above 8 °C from 1 January (literature/pertot2007), where Gessler et al. 2011 give"
            " Gehmann's as 160; Puelles et al. 2024 use 140-160. The engine's 140 is Leoni et al."
            " 2026's reading of Siegfried et al. 2004.",
            "Read 2026-10-12 at VitiMeteo sources: Viret et al. 2007 (Revue suisse 39(1):57-59,"
            " Fig. 3, page image) print the germination date as the sum above 8 °C reaching 160;"
            " Dubuis et al. 2012 print 140 from 1 January in the text and 140-160 in Fig. 1."
            " So the model ran 160 in 2006 and 140 in 2012 at Changins, and the value is a"
            " regional setting, not a constant (literature/viret2007, literature/dubuis2012).",
        ),
    ),
    "leoni2026.oospores": Formulation(
        "Oospore maturity by a germination model (GLM)",
        "Leoni et al. 2026, OENO One, doi:10.20870/oeno-one.2026.60.3.9963",
        year=2026,
        authors=(
            "Leoni, Sara",
            "Ruzzante, Livio",
            "Fabre, Anne-Lise",
            "Kasparian, Jérôme",
            "Wolf, Jean-Pierre",
            "Dubuis, Pierre-Henri",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2026-leoni-10-20870-oeno-one-2026-60-3-9963.pdf",
        structures=("oospore-glm",),
        calibrated_on=("leoni2026.changins",),
        parameters=(
            Published("intercept", 2.36, "log d", "Table 1", "read"),
            Published("precip_since_jan1", 0.00076, "log d per unit", "Table 1", "read"),
            Published("rainy_days_since_jan1", -0.034, "log d/d", "Table 1", "read"),
            Published("tdd8_since_jan1", -0.0046, "log d/(°C·d)", "Table 1", "read"),
            Published("mature_mtg_d", 1.5, "d", "maturity when MTG < 1.5 d", "read"),
        ),
        flags=(
            "Read 2026-10-09 (literature/leoni2026): a Poisson GLM, log link, of the mean time"
            " to germination (MTG) before BBCH 13, n = 96; the precipitation term's unit is not"
            " printed and its p is 0.53. Predictors, the BBCH 13 split and the MTG < 1.5 d"
            " threshold were chosen on the same Changins data, with no hold-out.",
        ),
    ),
    "broome1995.botrytis": Formulation(
        "Botrytis infection index per wet period",
        (
            "Broome et al. 1995, Phytopathology 85: 97-102, doi:10.1094/Phyto-85-97 (the combined"
            " data's coefficients; the dry-period rules as UC IPM states them)"
        ),
        year=1995,
        authors=(
            "Broome, J. C.",
            "English, J. T.",
            "Marois, J. J.",
            "Latorre, B. A.",
            "Aviles, J. C.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="1995-broome-10-1094-phyto-85-97.pdf",
        structures=("wetness-temperature-infection-index",),
        flags=(
            "The paper is held in Chris's drop and read since 2026-10-08 (literature/"
            "broome1995): its byline is J. C. Broome, J. T. English, J. J. Marois, B. A."
            " Latorre and J. C. Aviles. The combined fit's b2 is garbled in the text copy, so"
            " 0.061601 needs the page image. Cooptera's list takes the byline from the paper"
            " since cooptera@2ae3182.",
            "Monteiro et al. 2015 (Embrapa Boletim 38, p. 10, read in the scan 2026-10-09;"
            " literature/monteiro2015bol) print the combined fit as -2.647866 - 0.374927W +"
            " 0.061601WT - 0.001511WT² (R² 0.75): the engine's coefficients, b2 included."
            " Rodrigues et al. 2019 print the intercept as +2.6479, a misprint.",
        ),
    ),
    "gubler1999.powdery_index": Formulation(
        "Powdery mildew risk index (UC Davis)",
        "the UC Davis risk index; the code says Gubler and Thomas; not held",
        year=1999,
        authors=("Gubler, W. D.", "Rademacher, M. R.", "Vasquez, S. J.", "Thomas"),
        authors_from="trail",
        checked=(
            "Bleyer et al. 2023's reference list (held) gives the first three; the "
            "literature survey (02-other-diseases-and-pests.md, row 24, from a snippet) "
            "adds Thomas"
        ),
        structures=("temperature-hours-mildew-index",),
        added_authors=(
            Added(
                ("Leavitt",),
                "snippet",
                "a search summary's author list",
            ),
        ),
        flags=(
            "Casanova-Gascón et al. 2019 (Agronomy 9:738, Somontano, read 2026-10-10;"
            " literature/casanovagascon2019): 'Thomas and Gubler's model was found to be very"
            " accurate' there, within a week of observed powdery mildew, 2016-2018. No numbers"
            " are printed.",
        ),
    ),
    "thiessen2018.ascospores": Formulation(
        "Powdery mildew ascospore release days",
        "Thiessen, Neill & Mahaffee 2018, Plant Disease 102: 1500-1508; not held",
        year=2018,
        authors=("Thiessen", "Neill", "Mahaffee"),
        authors_from="trail",
        checked="models/powdery_mildew.py",
        structures=("ascospore-release-rule",),
        flags=(
            "The paper is held in Chris's drop and read since 2026-10-08 (literature/"
            "thiessen2018): L. D. Thiessen, T. M. Neill and W. F. Mahaffee. Its Oregon rule:"
            " release when, within 24 h, wetness lasts over 6 h above 4 °C, rain exceeds"
            " 2.5 mm and RH exceeds 80% (66% accurate in its test). Cooptera's list, which"
            " this record must match, still gives the trail.",
        ),
    ),
    "sentelhas2008.wetness": Formulation(
        "Leaf wetness from humidity or dew-point depression thresholds",
        "Sentelhas et al. 2008, doi:10.1016/j.agrformet.2007.09.011",
        year=2008,
        authors=(
            "Sentelhas, Paulo C.",
            "Dalla Marta, Anna",
            "Orlandini, Simone",
            "Santos, Eduardo A.",
            "Gillespie, Terry J.",
            "Gleason, Mark L.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="2008-sentelhas-10-1016-j-agrformet-2007-09-011.pdf",
        borrows=("alduchov1996.magnus",),
        structures=("rh-threshold-wetness",),
    ),
    "cooptera.rh90_wetness": Formulation(
        "Leaf wetness where there is no sensor: RH of 90% or rain",
        "chosen here on the stations' sensors (STATUS.md, Step 5)",
        made_by="cooptera",
        structures=("rh-threshold-wetness",),
    ),
    "cooptera.logistic_wetness": Formulation(
        "Leaf wetness by a logistic model fitted on the stations",
        "fitted here; not adopted (STATUS.md)",
        made_by="cooptera",
        structures=("fitted-logistic-wetness",),
    ),
    "alduchov1996.magnus": Formulation(
        "Dew point and humidity by the Magnus formula",
        "Alduchov & Eskridge 1996; not held",
        year=1996,
        authors=("Alduchov, O. A.", "Eskridge, R. E."),
        authors_from="trail",
        checked="Daly et al. 2015's reference list (held)",
        structures=("magnus-humidity",),
        role="reference",
    ),
    "noaa.solar_position": Formulation(
        "The sun's elevation (night hours for sporulation)",
        "NOAA's general solar position formulas; no author is named",
        checked="models/sun.py, SOURCES.md",
        structures=("solar-position",),
        equations="solar",
        flags=(
            "NOAA's General Solar Position Calculations (gml.noaa.gov/grad/solcalc/"
            "solareqns.PDF, read 2026-10-07). It divides by 366 in a leap year; both tools'"
            " copies used 365 until 2026-10-07, up to 0.30 degrees of elevation wrong in 2028.",
            "NOAA's azimuth formula as printed puts the noon sun in the north if taken"
            " literally. The equations module uses pvlib's analytical form.",
        ),
        role="reference",
    ),
    "fao56.eq47": Formulation(
        "Wind speed at 2 m from another height",
        "FAO-56, equation 47; no author is named",
        checked="wetness_model.py, SOURCES.md",
        structures=("log-wind-profile",),
        role="reference",
    ),
    # -- Candidates: published, independent of the incubation lineage, run by neither tool ----
    "zachos1959.incubation": Formulation(
        "Incubation by Zachos's shortest durations to the oil spot",
        (
            "Zachos 1959, Ann. Inst. Phytopathol. Benaki N.S. 2(4): 193-355, chapter II, Figs"
            " 3-4 (Vello and Patras); the policy's second incubation since decision 21"
        ),
        year=1959,
        authors=("Zachos, D. G.",),
        authors_complete=True,
        authors_from="read",
        checked="1959-zachos-url-zachos-1959-benaki.pdf",
        calibrated_on=("zachos1959",),
        structures=("daily-incubation-table",),
        structures_note="days by mean temperature, used as daily fractions: Goidanich's form",
        parameters=(
            Published("vello.days_at_14c", 8.0, "d", "ch. II text and Fig. 3 (Vello)", "read"),
            Published("vello.days_16c_to_20c", 3.0, "d", "ch. II text and Fig. 3 (Vello)", "read"),
            Published(
                "vello.days_above_20c_to_25c", 2.5, "d", "ch. II text and Fig. 3 (Vello)", "read"
            ),
            Published("vello.days_at_28c", 6.0, "d", "ch. II text and Fig. 3 (Vello)", "read"),
            Published("patras.days_at_14c", 9.0, "d", "ch. II text and Fig. 4 (Patras)", "read"),
            Published("patras.days_at_17c", 4.0, "d", "ch. II text and Fig. 4 (Patras)", "read"),
            Published(
                "patras.days_21c_to_24c", 2.5, "d", "ch. II text and Fig. 4 (Patras)", "read"
            ),
            Published("patras.days_at_27c", 5.0, "d", "ch. II text and Fig. 4 (Patras)", "read"),
        ),
        flags=(
            "Shortest durations, on the 4th leaf, in spring and summer; in autumn they are"
            " longer at equal temperature (Table XII), and Corinth adds 1-2 days. Conidiophores"
            " follow the oil spots by at least 2 days. A degree-day sum was tried and rejected.",
            "In Cooptera's policy since its decision 21 (cooptera@df14b71, 2026-10-08): points"
            " read from Figs 3-4, the shorter curve at each temperature, joined by straight"
            " lines, a day adding 1/days from the day after the rain. Its Vello point at 28 °C"
            " is 6.1 d from the figure; the summary (p. 347) says 6.",
            "Magarey et al. 1991's incubation cubic was fitted partly to these data. Cooptera's"
            " magarey2010.rules computes no incubation curve, only the fact sheet's 5-day lower"
            " bound (Cooptera, 2026-10-08); where the sheet's 5-17 days came from is unknown.",
        ),
    ),
    "zachos1959.sporangia_survival": Formulation(
        "Survival of detached conidia (sporangia): days of rapid germination, by temperature,"
        " humidity and sun",
        (
            "Zachos 1959, Ann. Inst. Phytopathol. Benaki N.S. 2(4):193-355, chapter III,"
            " pp. 254-261, Tables XVI-XVIII and the conclusions (p. 260)"
        ),
        year=1959,
        authors=("Zachos, D. G.",),
        authors_complete=True,
        authors_from="read",
        calibrated_on=("zachos1959.conidia",),
        structures=("survival-days-table",),
        structures_note="days of viability read from experiments, no fitted curve",
        parameters=(
            Published("shade.saturated_23c_days", 8.0, "d", "Table XVIII, p. 259", "read"),
            Published("shade.ambient_23c_68rh_days", 1.0, "d", "Table XVIII, p. 259", "read"),
            Published("shade.saturated_25c_days", 2.0, "d", "Table XVIII, p. 260", "read"),
            Published("shade.ambient_25c_65rh_days", 1.0, "d", "Table XVIII, p. 259", "read"),
            Published("screen.ambient_mild_days", 4.0, "d", "Table XVII, 20 May, p. 257", "read"),
            Published("screen.saturated_mild_days", 6.0, "d", "Table XVII, 20 May, p. 257", "read"),
            Published("screen.hot_days", 1.0, "d", "Table XVII, 28 May, p. 257", "read"),
            Published("sun.most_lost_min", 15.0, "min", "Table XVI, p. 255", "read"),
            Published("sun.lethal_h", 1.0, "h", "Table XVI and p. 256", "read"),
        ),
        flags=(
            "The endpoint is rapid germination, within 2 h of wetting; germination after 24 h"
            " lasts longer (Tables XVII-XVIII). Durations are whole days. 'Mild': means"
            " 17.5-22.3 °C, RH 63-88 %, extremes 15-26 °C; 'hot': means 25-28.5 °C, maxima"
            " 31-33 °C. His conclusions (p. 260): about 4 days in shade if the mean is under"
            " 22 °C and the maximum at most 26 °C; 1-2 days at means of 22-25 °C; 6-8 days"
            " only in saturated air at means up to 23 °C, otherwise at most 2 days.",
            "Brischetto et al. 2020 cite this as sporangia 'on sporulating lesions' viable 4-8"
            " days in shade when maxima 'did not exceed 22°C': the experiments were on detached"
            " conidia on slides, and 6-8 days needed saturated air. Against Brischetto's eq. 2"
            " (Agrarium scripts/diagnostics/sporangia_survival.py, 2026-10-09): mild shade agrees;"
            " saturated air at 25 °C (2 d) and ambient air at 23-25 °C (1 d) do not, since the"
            " eq. 2 index T (1 - RH/100) is 0 in saturated air at any temperature; and eq. 2"
            " has no sun.",
        ),
    ),
    "kennelly2007.lesion_decline": Formulation(
        "Sporangia per lesion falling with each successive sporulation event",
        "Kennelly et al. 2007, Phytopathology 97:512-522, equation 1 and Figs 3-4",
        year=2007,
        authors=(
            "Kennelly, Megan M.",
            "Gadoury, David M.",
            "Wilcox, Wayne F.",
            "Magarey, Peter A.",
            "Seem, Robert C.",
        ),
        authors_complete=True,
        authors_from="read",
        doi="10.1094/PHYTO-97-4-0512",
        calibrated_on=("kennelly2007.loxton",),
        structures=("sporulation-decline-by-event",),
        structures_note="log relative sporulation linear in the event's number",
        parameters=(
            Published("intercept", 4.757, "ln(% + 1)", "eq. 1", "read"),
            Published("slope_per_event", -0.496, "ln(% + 1) per event", "eq. 1", "read"),
        ),
        flags=(
            "Y = ln(relative sporulation % + 1), X = the event's number; R² 0.77. Relative"
            " to each lesion's own maximum, so it says nothing of absolute yield. Lesion age"
            " alone did not reduce yield; an eighth sporulation gave under a fifth of a"
            " first's sporangia per mm² (Fig. 4A). Loxton, South Australia, 2003.",
            "It shares its paper and authors with the engine's kennelly2007.trigger, a flag:"
            " the trigger rests on Gadoury's historical Geneva data, this on Loxton lesions.",
        ),
    ),
    "rafaila1968.incubation": Formulation(
        "Incubation, infection to fructification, by temperature, detached leaves at 100% RH",
        (
            "Rafaila, Sevcenco & David 1968, Contributions to the biology of Plasmopara"
            " viticola, Phytopathol. Z. 63:328-336, Table 4"
        ),
        year=1968,
        authors=("Rafaila, C.", "Sevcenco, Victoria", "David, Zita"),
        authors_complete=True,
        authors_from="read",
        doi="10.1111/j.1439-0434.1968.tb02397.x",
        calibrated_on=("rafaila1968",),
        structures=("daily-incubation-table",),
        structures_note="days by temperature, used as daily fractions: Goidanich's form",
        parameters=(
            Published("days_at_10c", 18.0, "d", "Table 4 and text", "read"),
            Published("days_at_11c", 14.0, "d", "Table 4 and text", "read"),
            Published("days_at_12c", 12.0, "d", "Table 4 and text", "read"),
            Published(
                "days_at_14c",
                8.0,
                "d",
                "Table 4, columns matched in order (the text omits it)",
                "read",
            ),
            Published(
                "days_at_16c",
                7.0,
                "d",
                "Table 4, columns matched in order (the text omits it)",
                "read",
            ),
            Published(
                "days_at_17c",
                5.0,
                "d",
                "Table 4, columns matched in order (the text omits it)",
                "read",
            ),
            Published("days_19c_to_26c", 4.0, "d", "Table 4 and text", "read"),
            Published("days_at_27c", 5.0, "d", "Table 4 and text", "read"),
            Published("days_at_28c", 6.0, "d", "Table 4 and text", "read"),
            Published("days_at_29c", 7.0, "d", "Table 4 and text", "read"),
        ),
        flags=(
            "None at 30 °C. Below 10 °C no spores appeared, but infections stayed latent:"
            " leaves moved to 22 °C sporulated within 2-4 days. Older leaves incubate 1-4 days"
            " longer (Table 3).",
            "Magarey et al. 1991's incubation cubic was fitted partly to these data. Cooptera's"
            " magarey2010.rules computes no incubation curve, only the fact sheet's 5-day lower"
            " bound (Cooptera, 2026-10-08); where the sheet's 5-17 days came from is unknown.",
        ),
    ),
    # -- PLASMO, the Florence model (read 2026-10-09; literature/rosa1993, orlandini1993) --
    "orlandini1993.plasmo": Formulation(
        "PLASMO, the Florence model: primary trigger, infection, incubation and survival",
        (
            "Orlandini, Gozzini, Rosa, Egger, Storchi, Maracchi & Miglietta 1993, Bulletin"
            " OEPP/EPPO Bulletin 23:619-626; first published as Rosa et al. 1993, Comput."
            " Electron. Agric. 9:205-215, from Rosa 1988 (thesis, Firenze, not held)"
        ),
        year=1993,
        authors=(
            "Orlandini, S.",
            "Gozzini, B.",
            "Rosa, M.",
            "Egger, E.",
            "Storchi, P.",
            "Maracchi, G.",
            "Miglietta, F.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="EPPO Bulletin - December 1993 - ORLANDINI - PLASMO (10-9 drop), page images",
        structures=(
            "rain-temperature-trigger",
            "wet-degree-hours-infection",
            "daily-incubation-table",
            "survival-hours-temperature-humidity",
        ),
        structures_note="the union of its pieces' tags",
        flags=(
            "No sporulation step (sporangia emerge when incubation reaches 100 %) and no"
            " oospores (the trigger stands in). Rosa et al. 1993 add Genesio, R. to the authors;"
            " the later fuzzy-logic version (Orlandini et al. 2003, EPPO Bull. 33:415-420)"
            " prints no equations.",
        ),
    ),
    "rosa1993.incubation": Formulation(
        "Incubation progress per hour: a Gaussian in temperature fitted to Goidanich's table",
        (
            "Rosa, Genesio, Gozzini, Maracchi & Orlandini 1993, PLASMO: a computer program for "
            "grapevine downy mildew development forecasting, Comput. Electron. Agric. "
            "9:205-215, p. 208"
        ),
        year=1993,
        authors=("Rosa, M.", "Genesio, R.", "Gozzini, B.", "Maracchi, G.", "Orlandini, S."),
        authors_complete=True,
        authors_from="read",
        checked="1-s2.0-0168169993900394-main.pdf (10-9 drop), equations read in the page image",
        part_of=("orlandini1993.plasmo",),
        calibrated_on=("goidanich1957",),
        calibration_note=(
            "read: 'The development of incubation is described by a function deduced from the"
            " Goidanich table (Goidanich et al., 1958). The latter has been translated into an"
            " x-y graphic of points so as to find a curve passing sufficiently close to them'"
            " (p. 208). Goidanich, Cesarini [sic] & Foschi 1958, I nemici della vite, is taken"
            " to print the same table as the 1957 article (inferred: same authors, same table)"
        ),
        structures=("daily-incubation-table",),
        structures_note=(
            "an hourly rate curve fitted to Goidanich's table and summed to 100 %: the table's"
            " rate-summation form, tagged strictly"
        ),
        parameters=(
            Published("f1.t_peak_c", 23.5, "°C", "f1, p. 208", "read"),
            Published("f1.width_c", 11.2, "°C", "f1, p. 208", "read"),
            Published("f2.coefficient", 0.00577, "1/°C2", "f2, p. 208", "read"),
            Published("f2.t_mid_c", 16.7, "°C", "f2, p. 208", "read"),
            Published("f2.offset", 0.737, "1", "f2, p. 208", "read"),
            Published("f3.coefficient", 0.15, "1", "f3 = 0.15·sqrt(RH - 30), p. 208", "read"),
            Published("f3.rh_min_pct", 30.0, "%", "f3, p. 208", "read"),
        ),
        flags=(
            "As printed: f4 = f1·f2·f3; f1 = exp(-[(T - 23.5)/11.2]²); f2 = 1 for T <= 10 or"
            " T >= 23.5 °C, 0.00577(T - 16.7)² + 0.737 for 10-16.7 °C, 1 - 0.00577(T - 23.5)² for"
            " 16.7-23.5 °C; f3 = 0.15·sqrt(RH - 30). The units of f4 (% an hour) are not stated.",
        ),
    ),
    "orlandini1993.incubation": Formulation(
        "Incubation progress per hour: a parabola in temperature times a line in humidity",
        (
            "Orlandini, Gozzini, Rosa, Egger, Storchi, Maracchi & Miglietta 1993, PLASMO: a "
            "simulation model for control of Plasmopara viticola on grapevine, Bulletin "
            "OEPP/EPPO Bulletin 23:619-626, pp. 620-621"
        ),
        year=1993,
        authors=(
            "Orlandini, S.",
            "Gozzini, B.",
            "Rosa, M.",
            "Egger, E.",
            "Storchi, P.",
            "Maracchi, G.",
            "Miglietta, F.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="EPPO Bulletin - December 1993 - ORLANDINI - PLASMO (10-9 drop), page images",
        part_of=("orlandini1993.plasmo",),
        calibrated_on=("goidanich1957", "orlandini1993.emergences"),
        calibration_note=(
            "read: Tmin about 10 °C, Topt about 22 °C and Tmax about 34 °C 'were observed'"
            " in Goidanich 1959 (Manuale di Patologia Vegetale; Tmin also Magarey et al. 1991);"
            " m was 'chosen when the difference in time between observed and calculated"
            " sporangia emergences reached a minimum' (p. 621). That Goidanich's manual draws"
            " on the 1957 table's data is inferred, so the goidanich1957 link is the strict"
            " reading"
        ),
        structures=("daily-incubation-table",),
        structures_note="an hourly rate summed to 100 %: the table's rate-summation form, strictly",
        parameters=(
            Published("t_min_c", 10.0, "°C", "p. 621, 'about 10 °C'", "read"),
            Published("t_opt_c", 22.0, "°C", "p. 621, 'about 22 °C'", "read"),
            Published("t_max_c", 34.0, "°C", "p. 621, 'about 34 °C'", "read"),
            Published("rh_min_pct", 30.0, "%", "p. 620, null increments below RH 30 %", "read"),
            Published("m", 0.097, "%/h per % RH", "p. 621", "read"),
        ),
        flags=(
            "As printed (p. 621): d = f3(T)·f4(RH), f3 = 4(T - Tmin)(Tmax - T)/(Tmax - Tmin)²,"
            " f4 = m(RH - RHmin), summed hourly to 100 %. With m = 0.097, d is 6.8 % an hour at"
            " 22 °C and 100 % RH, which ends incubation in under 15 h against the 4-25 days the"
            " paper states: m or its unit is misprinted, or d is not % an hour. No RHmax is"
            " printed.",
            "Franche 2012 prints incubRate = 2.616·(T - Tmin)(Tmax - T)·(RH - RHmin)/(RHmax -"
            " RHmin)/(Tmax - Tmin)², 0.65 at the optimum. 2.616 is in none of Rosa 1993,"
            " Orlandini 1993, Orlandini 2003, Rosa 1995 (m = 0.082 on √(RH - 30)) or Orlandini"
            " 2008 (fm not printed; read 2026-10-09). Orlandini 2008 gives the bounds: 10-34 °C,"
            " 30-100 % RH. Orlandini et al. 2003a,b remain unfound.",
        ),
    ),
    "orlandini1993.infection": Formulation(
        "Infection when the wet hours reach n/T: a constant wet degree-hour sum",
        (
            "Orlandini, Gozzini, Rosa, Egger, Storchi, Maracchi & Miglietta 1993, PLASMO: a "
            "simulation model for control of Plasmopara viticola on grapevine, Bulletin "
            "OEPP/EPPO Bulletin 23:619-626, p. 620; Rosa et al. 1993, Comput. Electron. Agric."
            " 9:205-215, p. 208"
        ),
        year=1993,
        authors=(
            "Orlandini, S.",
            "Gozzini, B.",
            "Rosa, M.",
            "Egger, E.",
            "Storchi, P.",
            "Maracchi, G.",
            "Miglietta, F.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="EPPO Bulletin - December 1993 - ORLANDINI - PLASMO (10-9 drop), page images",
        part_of=("orlandini1993.plasmo",),
        calibrated_on=("blaeser1979", "orlandini1993.emergences"),
        calibration_note=(
            "read: 'This function has been derived on the basis of data from Blaeser & Weltzien"
            " (1979) ... The hyperbolic function most representative of Blaeser & Weltzien's"
            " data was found by the least squares method' (p. 620); n = 75.69 then chosen with m"
            " against observed sporangia emergences (p. 621). Rosa et al. 1993 fit the 'Blaeser"
            " table' and print n = 52.7"
        ),
        structures=("wet-degree-hours-infection",),
        parameters=(
            Published("n_degree_hours", 75.69, "°C·h", "p. 621", "read"),
            Published(
                "n_degree_hours_rosa1993", 52.7, "°C·h", "Rosa et al. 1993, f5, p. 208", "read"
            ),
            Published("t_low_c", 6.0, "°C", "p. 620", "read"),
            Published("t_high_c", 26.0, "°C", "p. 620", "read"),
        ),
        flags=(
            "As printed: f1(T) = n/T for 6 <= T <= 26 °C, otherwise 0, the wet hours needed;"
            " progress 100/f1 % per wet hour (p. 620). Blaeser & Weltzien's own fit is hours ="
            " -0.67 + 60.0/T.",
        ),
    ),
    "orlandini1993.survival": Formulation(
        "Survival of sporangia in hours, piecewise linear in temperature and scaled by humidity",
        (
            "Orlandini, Gozzini, Rosa, Egger, Storchi, Maracchi & Miglietta 1993, PLASMO: a "
            "simulation model for control of Plasmopara viticola on grapevine, Bulletin "
            "OEPP/EPPO Bulletin 23:619-626, p. 621; the same in Rosa et al. 1993, p. 209"
        ),
        year=1993,
        authors=(
            "Orlandini, S.",
            "Gozzini, B.",
            "Rosa, M.",
            "Egger, E.",
            "Storchi, P.",
            "Maracchi, G.",
            "Miglietta, F.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="EPPO Bulletin - December 1993 - ORLANDINI - PLASMO (10-9 drop), page images",
        part_of=("orlandini1993.plasmo",),
        calibrated_on=("blaeser1978.survival",),
        calibration_note=(
            "inferred: credited to Blaeser & Weltzien 1979, who print no function of this form;"
            " taken to be PLASMO's own fit of their survival data, which come from the 1978 tests"
        ),
        structures=("survival-hours-temperature-humidity",),
        parameters=(
            Published("below_10c_h", 235.8, "h", "f8, p. 621", "read"),
            Published("slope_10_15c_h_per_c", 1.8, "h/°C", "f8, p. 621", "read"),
            Published("intercept_10_15c_h", 217.8, "h", "f8, p. 621", "read"),
            Published("slope_15_30c_h_per_c", 15.52, "h/°C", "f8, p. 621, as printed", "read"),
            Published("intercept_15_30c_h", 12.0, "h", "f8, p. 621, as printed", "read"),
            Published("above_30c_h", 12.0, "h", "f8, p. 621", "read"),
        ),
        flags=(
            "As printed in both 1993 papers: hours = (f8(T) - 12)·RH/100 + 12; f8 = 235.8 (T <"
            " 10 °C), 1.8T + 217.8 (10-15 °C), 15.52T + 12 (15-30 °C), 12 (T > 30 °C); progress"
            " 100/hours % an hour. The 15-30 °C piece rises to 477.6 h at 30 °C and then drops to"
            " 12: probably a misprinted sign, since 15.52(30 - T) + 12 meets both neighbours"
            " (244.8 h at 15 °C, 12 h at 30 °C). Not corrected here.",
            "Orlandini et al. 2008 replaced it with orlandini2008.survival (read 2026-10-09),"
            " which prints no parameters, as Brischetto et al. 2020 say.",
        ),
    ),
    "orlandini1993.trigger": Formulation(
        "Primary infection: 8 mm of rain in 24 h once the minimum temperature stays above 10 °C",
        (
            "Orlandini, Gozzini, Rosa, Egger, Storchi, Maracchi & Miglietta 1993, PLASMO: a "
            "simulation model for control of Plasmopara viticola on grapevine, Bulletin "
            "OEPP/EPPO Bulletin 23:619-626, p. 620; Rosa et al. 1993, p. 208"
        ),
        year=1993,
        authors=(
            "Orlandini, S.",
            "Gozzini, B.",
            "Rosa, M.",
            "Egger, E.",
            "Storchi, P.",
            "Maracchi, G.",
            "Miglietta, F.",
        ),
        authors_complete=True,
        authors_from="read",
        checked="EPPO Bulletin - December 1993 - ORLANDINI - PLASMO (10-9 drop), page images",
        part_of=("orlandini1993.plasmo",),
        borrows=(),
        structures=("rain-temperature-trigger",),
        structures_note="credited to Goidanich 1959; shoots must be 100 mm long",
        parameters=(
            Published("rain_mm", 8.0, "mm", "p. 620 ('>= 8 mm within any 24-h period')", "read"),
            Published("t_min_c", 10.0, "°C", "p. 620", "read"),
            Published("shoot_mm", 100.0, "mm", "p. 620", "read"),
        ),
    ),
    "rosa1995.incubation": Formulation(
        "Incubation progress per hour: a parabola in temperature times a square root of humidity",
        (
            "Rosa, Gozzini, Orlandini & Seghi 1995, A computer program to improve the control of"
            " grapevine downy mildew, Comput. Electron. Agric. 12:311-322, p. 313"
        ),
        year=1995,
        authors=("Rosa, M.", "Gozzini, B.", "Orlandini, S.", "Seghi, L."),
        authors_complete=True,
        authors_from="read",
        checked="04_Rosa_Gozzini_Orlandini_Seghi_1995.pdf (supplied by Chris), page images",
        doi="10.1016/0168-1699(95)00007-Q",
        part_of=("orlandini1993.plasmo",),
        calibrated_on=("goidanich1957", "zachos1959", "orlandini1993.emergences"),
        calibration_note=(
            "read 2026-10-09: Tmin and Tmax 'are identifiable from literature (Tmin = 10°C; Tmax"
            " = 34°C) (Goidanich, 1959; Zachos, 1959; Magarey et al., 1991)'; m 'has been"
            " derived by comparing several infections and durations of incubation periods, with"
            " the results of simulations' (p. 313), from 'various field trials ... when the"
            " difference in time between observed and calculated sporangia emergencies reached a"
            " minimum value' (p. 317). Goidanich's manual and Zachos's monograph are taken as"
            " their incubation data, and the trials as Orlandini et al. 1993's: the strict"
            " reading, inferred"
        ),
        structures=("daily-incubation-table",),
        structures_note="an hourly rate summed to 100 %: the table's rate-summation form, strictly",
        parameters=(
            Published("t_min_c", 10.0, "°C", "p. 313", "read"),
            Published("t_max_c", 34.0, "°C", "p. 313", "read"),
            Published("rh_min_pct", 30.0, "%", "p. 313, RH in [30, 100]", "read"),
            Published("m", 0.082, "%/h per %^0.5", "p. 313, 'its mean value'", "read"),
        ),
        flags=(
            "As printed (p. 313): f1(t+1) = f1(t) + d(T, RH); d = d1(T)·d2(RH); d1 = 4(T -"
            " Tmin)(Tmax - T)/(Tmax - Tmin)²; d2 = m·(RH - 30)^(1/2); hourly, T in [Tmin, Tmax],"
            " RH in [30, 100]. At 22 °C and 100 % RH, d = 0.082·√70 = 0.69 % an hour, about 6 days"
            " to 100 %: unlike the 1993 version's m(RH - 30), the rate is plausible. 'New"
            " equations ... because of deficiencies shown by the previous model' (p. 313).",
            "Not Franche 2012's 2.616·(RH - RHmin)/(RHmax - RHmin): that form is linear in RH."
            " PLASMO 2.11, tested in 1992-1993 at Paretaio, Pulizzano and Sassuolo (Chianti).",
        ),
    ),
    "orlandini2008.plasmo": Formulation(
        (
            "PLASMO as an epidemic: leaf area, lesion and sporangia survival, sporulation,"
            " inoculation and incubation, tuned on two seasons' severity"
        ),
        (
            "Orlandini, Massetti & Dalla Marta 2008, An agrometeorological approach for the"
            " simulation of Plasmopara viticola, Comput. Electron. Agric. 64:149-161, eqs 1-6"
        ),
        year=2008,
        authors=("Orlandini, S.", "Massetti, L.", "Dalla Marta, A."),
        authors_complete=True,
        authors_from="read",
        checked="03_Orlandini_Massetti_DallaMarta_2008.pdf (supplied by Chris), page images",
        doi="10.1016/j.compag.2008.04.004",
        # The 'three ten' rule is one of two ways to start the epidemic (p. 154).
        borrows=("rule_3_10",),
        calibrated_on=(
            "orlandini2008.mondeggi",
            "blaeser1978.survival",
            "lalancette1988a",
            "goidanich1957",
        ),
        calibration_note=(
            "read 2026-10-09: C (sporangia per cm²) and D (sporangia survival, days) were tuned"
            " from 2 to 40 on the 1995-1996 severity at Mondeggi-Lappeggi, C22 D18 chosen (pp."
            " 158-160). Inferred: each function is credited to a source and its coefficients are"
            " not printed; the fits are taken to be to those sources' data. Survival (eqs 2, 4)"
            " to Blaeser & Weltzien 1978; sporulation (eq. 3) to Lalancette et al. 1988a, the"
            " sporulation paper (78:1316); inoculation (eq. 5) to Lalancette et al. 1988b, the"
            " infection paper (78:794, datasets.lalancette1988a); incubation (eq. 6) to Goidanich"
            " et al. 1958 and Magarey et al. 1991"
        ),
        structures=(
            "rain-temperature-trigger",
            "survival-hours-temperature-humidity",
            "dark-moist-hours-sporulation",
            "sporulation-temperature-bounds",
            "wetness-temperature-infection-index",
            "daily-incubation-table",
        ),
        structures_note=(
            "the union of its pieces, strictly: sporulation needs 7-12 night hours at RH >= 90 %"
            " within 10-30 °C; inoculation is a cubic in temperature times a term in 2-9 wet"
            " hours; incubation an hourly rate summed to 100 %"
        ),
        parameters=(
            Published("c_tuned", 22.0, "1", "p. 160, C22 D18", "read"),
            Published("d_tuned", 18.0, "d", "p. 160, C22 D18", "read"),
            Published("incubation_t_min_c", 10.0, "°C", "eq. 6, p. 159", "read"),
            Published("incubation_t_max_c", 34.0, "°C", "eq. 6, p. 159", "read"),
            Published("incubation_rh_min_pct", 30.0, "%", "eq. 6, p. 159", "read"),
            Published("incubation_rh_max_pct", 100.0, "%", "eq. 6, p. 159", "read"),
        ),
        flags=(
            "Prints the forms and bounds but none of the coefficients (a0-a2, b0-b3, c0-c2,"
            " cs,max, d0-d3, e0-e3, fm, B, F): it cannot be run from the paper.",
            "Sporulation (eq. 3) as printed: (c2T² + c1T + c0)/cs,max·(e^-((H-7)/2) - e^-((H-6)/2))"
            " for H = 7-12 consecutive night hours at RH >= 90 % and T = 10-30 °C. Inoculation"
            " (eq. 5): (e3T³ + e2T² + e1T + e0)·(e^-((H-2)/2) - e^-((H-1)/2)) for H = 2-9 wet"
            " hours (wetness or rain) and T = 5-30 °C. Summed hour by hour, the H terms"
            " telescope to 1 - e^-((H-6)/2) and 1 - e^-((H-1)/2) (arithmetic, not stated).",
            "Incubation (eq. 6) as typeset: fm·(T - Tmin)(Tmax - T)/[(Tmax - Tmin)²·√(RH - RHmin"
            "/RHmax - RHmin)], humidity under the root in the denominator, yet Fig. 7 rises with"
            " humidity: probably a typesetting error. Fig. 7 peaks near 8.5 % at 22 °C and 99 %;"
            " its time unit is not stated.",
            "Validation 1998-2003: risk class right in 4 of 6 years, 'Low' simulated as 'No"
            " risk' in the other two (Table 4); RMSE 0.74-5.55 (Table 3).",
        ),
    ),
    "orlandini2008.survival": Formulation(
        (
            "Survival of sporulating lesions and of sporangia: a Gaussian in humidity times the"
            " distance below 30 °C, with a 1/6 floor"
        ),
        (
            "Orlandini, Massetti & Dalla Marta 2008, Comput. Electron. Agric. 64:149-161, eqs 2"
            " and 4, Figs 3 and 5, pp. 154-157"
        ),
        year=2008,
        authors=("Orlandini, S.", "Massetti, L.", "Dalla Marta, A."),
        authors_complete=True,
        authors_from="read",
        checked="03_Orlandini_Massetti_DallaMarta_2008.pdf (supplied by Chris), page images",
        doi="10.1016/j.compag.2008.04.004",
        part_of=("orlandini2008.plasmo",),
        calibration_note=(
            "credited '(Blaeser and Weltzien, 1978)' for both (pp. 154, 156); b0-b3 and d0-d3 are"
            " not printed, nor is a fit described: the link to blaeser1978.survival is inferred"
        ),
        structures=("survival-hours-temperature-humidity",),
        structures_note=(
            "temperature and relative humidity, not a vapour pressure deficit, and not"
            " Blaeser & Weltzien's polynomial"
        ),
        parameters=(
            Published("t_max_c", 30.0, "°C", "eqs 2 and 4", "read"),
            Published("rh_min_pct", 30.0, "%", "eqs 2 and 4", "read"),
            Published("floor", 6.0, "1", "eqs 2 and 4, '+ 6', unit not stated", "read"),
        ),
        flags=(
            "As printed: O(t+1) = O(t)·(1 - B·f1), f1 = 1/6 for T > 30 °C, else 1/[(b0 + b1·e^-"
            "((RH - b2)/b3)²)·(T - 30) + 6] for RH 30-100 %; sporangia the same with D and"
            " d0-d3 (eq. 4). Figs 3 and 5 (days) reach about 13-14 at 5 °C near saturation, about"
            " 3-4 at 5 °C in dry air, and near 0 at 30 °C, falling linearly with temperature;"
            " that fits a floor of 6 hours, not days (inferred).",
            "Confirms Brischetto et al. 2020 and 2021: PLASMO's survival takes temperature and"
            " humidity after Blaeser & Weltzien 1978 and prints no parameters. It is not their"
            " equation.",
        ),
    ),
    "keil2007.sporulation": Formulation(
        "Sporangia per cm² of lesion from the temperature of the sporulating night: a quadratic",
        (
            "Keil 2007, Epidemiologische Aspekte der Falschen Mehltauinfektion durch Plasmopara"
            " viticola an Vitis, dissertation, Univ. Hohenheim, p. 53 and Fig. 19"
        ),
        year=2007,
        authors=("Keil, Sven Benjamin",),
        authors_complete=True,
        authors_from="read",
        checked="keil2008_epidemiologie.pdf (deep-research drop), title page",
        calibrated_on=("keil2007.freiburg",),
        calibration_note=(
            "read 2026-10-09: a trend line through Keil's own means at 15, 20, 25, 28 and 30 °C"
            " (R² 0.8955); compared with Lalancette 1988 and Blaeser 1978, not fitted to them"
        ),
        structures=("sporulation-temperature-bounds",),
        structures_note=(
            "positive only between about 13.5 and 31 °C (arithmetic): a temperature band read"
            " strictly, with a shape inside it"
        ),
        parameters=(
            Published("a", -747.5, "sporangia/cm² per °C²", "p. 53", "read"),
            Published("b", 33397.0, "sporangia/cm² per °C", "p. 53", "read"),
            Published("c", -330581.0, "sporangia/cm²", "p. 53", "read"),
        ),
        flags=(
            "As printed (p. 53): sporangia/cm² = -747.5 T² + 33397 T - 330581. Its vertex is"
            " 22.3 °C against the text's 'ca. 23 °C', and it is negative at 30 °C (about -1,400)"
            " where the text says almost no sporulation (arithmetic). Sporulation was seen down"
            " to 8 °C, below the fitted range.",
        ),
    ),
    "keil2007.sun_mortality": Formulation(
        "Extra deaths of sporangia in direct sun, against shaded controls: 3 points an hour",
        "Keil 2007, dissertation, Univ. Hohenheim, p. 63",
        year=2007,
        authors=("Keil, Sven Benjamin",),
        authors_complete=True,
        authors_from="read",
        checked="keil2008_epidemiologie.pdf (deep-research drop), title page",
        calibrated_on=("keil2007.freiburg",),
        calibration_note="read 2026-10-09: sporangia on glass in sun and in shade, summer 2005",
        structures=("sun-exposure-mortality",),
        parameters=(
            Published("slope", 3.0, "percentage points per hour", "p. 63", "read"),
            Published("intercept", -1.4, "percentage points", "p. 63", "read"),
            Published("irradiance", 0.65, "kWh/m² (mean)", "p. 63", "read"),
        ),
        flags=(
            "As printed (p. 63): Absterberate = 3 x Expositionsdauer - 1.4 (R² 0.85): the excess"
            " of dead sporangia over shaded controls; little difference in the first 2 h, about"
            " 10 % after 3-5 h, 17.5 % after 6 h, 23 % after 7 h. Light alone kills far fewer"
            " than Kennelly et al. 2007 found dead after 6-8 h of hot, dry days.",
            "Vitality also falls with the temperature sporangia formed at: 72.7 % at 15 °C, 40.5 %"
            " at 27.5 °C (Table 8).",
        ),
    ),
    "epi1983.corrected": Formulation(
        (
            "EPI, the potential infection state: winter potential energy from monthly rain and"
            " temperature against normals, then a daily kinetic phase from humidity"
        ),
        (
            "Strizyk's EPI, 'Modèle 83 corrigé', as printed in Ronzon (Tran Manh Sung) 1987,"
            " Modélisation du comportement épidémique du mildiou de la vigne, thesis, Univ."
            " Bordeaux II, pp. 49 and 51"
        ),
        year=1983,
        authors=("Strizyk, S.",),
        authors_from="trail",
        checked=(
            "Ronzon 1987 (deep-research drop, HAL tel-02856849), pp. 49-51, page images; the"
            " model's own report (Strizyk 1983, ACTA) is not held"
        ),
        calibration_note=(
            "not stated: run on 1975-1982 a posteriori and 1983-1986 in real time against the"
            " Plant Protection Service's attack classes (ronzon1987.bordeaux); no fit described"
        ),
        structures=("potential-energy-index",),
        parameters=(
            Published("pe.factor", 2.0, "1", "p. 49, PE = 2 ct (√H - √Hc)", "read"),
            Published("ep.factor", 0.2, "1", "p. 49, EP = 0.2 ct (√H√T - √Hc√Tc)", "read"),
            Published("en.threshold", 135.0, "per NJM", "p. 49, k >= 135/NJM", "read"),
            Published("kinetic.factor", 0.012, "1", "p. 51", "read"),
            Published("um.low_sigma", 0.16, "sd", "p. 51, UM - 0.16 sd < Um", "read"),
            Published("um.high_sigma", 0.7, "sd", "p. 51, Um < UM + 0.7 sd", "read"),
        ),
        flags=(
            "As printed (pp. 49, 51, checked in the page images): PE = 2 ct (√H - √Hc); EP = 0.2"
            " ct (√H √T - √Hc √Tc); EN_i = a log(K_i) when k >= 135/NJM, a = NJM x 1.5/18; EN ="
            " the sum over three decades; EPI = EPI0 + (PE + EP - EN), monthly October-March."
            " Kinetic phase: Um = ((U1 + U2 + U3) + 5 UN)/8, bounded by UM - 0.16 sd and UM +"
            " 0.7 sd (sd: the standard deviation of UM over at least 20 years); EPI = 0.012"
            " [(Um² √T - UM² √TM)/100] + EPI0. ct is a monthly constant (1.2, 1, 0.8 in the"
            " original version).",
            "Needs 20 years of monthly normals. An EPI in [-10, 0] at the end of March is a"
            " critical zone (p. 51). Maddalena et al. 2023 and Sanna et al. 2014 run EPI in"
            " Epicure; their version's thresholds are not printed.",
            "Kontogiannis et al. 2024 (Computers 13:63, p. 3, read in the page image 2026-10-10;"
            " literature/kontogiannis2024) print another version, cited to Stryzik: daily Ri and"
            " Ti against 0.95 of the monthly normal, k on the first term only, and EN = (1.5"
            " RDm/18) log10(Rd/RDd); a kinetic term 0.012 [1/4 (5 RHnight + 3 RH10-18h)^2 sqrt(Ti)"
            " - RH10-18h^2 sqrt(Tm)]/100, where Ronzon has Um = (3 day + 5 night)/8 against the"
            " normal UM; first infection when EPI > -10. Take the model from Ronzon's printing.",
        ),
    ),
    "rouzet2003.cold_days": Formulation(
        (
            "A correlation window, not a maturation start: days with Tmax over 10 °C counted"
            " after 60 cold days (7 °C <= Tmax <= 15 °C), against the date oospores mature"
        ),
        (
            "Rouzet & Jacquin 2003, Development of overwintering oospores of Plasmopara"
            " viticola and severity of primary foci in relation to climate, Bulletin OEPP/EPPO"
            " Bulletin 33:437-442, p. 440 and Table 7; the rule as Franche 2012 states it"
            " (§2-1-1, Tableau 1) is his reading of this window"
        ),
        year=2003,
        authors=("Rouzet, J.", "Jacquin, D."),
        authors_complete=True,
        authors_from="read",
        checked="EPPO Bulletin - 2004 - Rouzet - Development of overwintering oospores (10-9 drop)",
        doi="10.1111/j.1365-2338.2003.00670.x",
        calibrated_on=("rouzet2003.balma",),
        calibration_note=(
            "read 2026-10-09: correlated, by 30-day windows, with the dates oospores stored 2 cm"
            " under sand at Balma first germinated within 24 h, 23 years from 1969 to 1998"
        ),
        structures=("cold-day-oospore-start",),
        structures_note=(
            "the tag is Franche's use of the window; the paper fits no model with it, only"
            " correlations (r up to -0.87, Table 7)"
        ),
        parameters=(
            Published("cold_days", 60.0, "d", "p. 440", "read"),
            Published("tmax_low_c", 7.0, "°C", "p. 440 and Table 7 (its list prints 4)", "read"),
            Published("tmax_high_c", 15.0, "°C", "p. 440 and Table 7", "read"),
            Published("warm_tmax_c", 10.0, "°C", "p. 440 and Table 7 ('Md Tm >= 10')", "read"),
        ),
        flags=(
            "Read 2026-10-09 (literature/rouzet2003). The paper states: 'Finally, we worked on"
            " maximum temperature >= 10 °C. For this last condition, the calculation was started"
            " when 60 'cold' days had passed (with maximum temperature between 7 and 15 °C) and"
            " then cumulated days when maximum temperature was over 10 °C' (p. 440). It is the"
            " start of a statistical window whose count correlates with how far a year's"
            " maturity date falls from the mean; no date of maturation is predicted from it.",
            "Not printed: when the 60-day count starts (leaves were collected at the end of"
            " October; the windows are centred from 29 September), and whether the days must be"
            " consecutive. The criteria list (p. 440) prints the cold band as 4-15 °C, Table 7"
            " as 7-15 °C.",
            "The authors' conclusion: 'there is little prospect that oospore maturation can be"
            " modelled in the near future'; their maturation models gave only the divergence"
            " from the average date. Franche's dates for Aquitaine (21 January 2002, 24 January"
            " 2003, 31 December 2004) are his model's, not observations. Do not run this as a"
            " start of maturation.",
        ),
    ),
    # -- Agrarium's truth: formulations the engine does not list ------------------------------
    "rossi2008.oospores": Formulation(
        "oospore dormancy and germination",
        (
            "Rossi, Caffi, Giosuè & Bugiani 2008, Ecol. Model. 212:480-491, with the hydro-"
            "thermal time of Rossi, Caffi, Bugiani, Spanna & Della Valle 2008, Plant Pathol. "
            "57:216-226"
        ),
        year=2008,
        authors=("Rossi", "Caffi", "Giosuè", "Bugiani", "Spanna", "Della Valle"),
        authors_complete=True,
        authors_from="trail",
        part_of=("rossi2008.primary", "rossi2008pp.dormancy"),
        structures=("hydro-thermal-oospore-cohorts",),
    ),
    "rossi2008.incubation": Formulation(
        "incubation window",
        "Rossi et al. 2008, eqs 8-9",
        year=2008,
        authors=("Rossi", "Caffi", "Giosuè", "Bugiani"),
        authors_complete=True,
        authors_from="trail",
        part_of=("rossi2008.primary",),
        structures=("incubation-window",),
    ),
    "rossi2002.onset": Formulation(
        (
            "The period of probable primary infection, in pentads from 1 January, from March's"
            " rain days and April's longest dry spell"
        ),
        (
            "Rossi, Giosuè, Girometta & Bugiani 2002, Influenza delle condizioni meteorologiche"
            " sulle infezioni primarie di Plasmopara viticola in Emilia-Romagna, Atti Giornate"
            " Fitopatologiche 2002, 2:263-270, eq. 1 and Tab. 3, p. 268"
        ),
        year=2002,
        authors=("Rossi, V.", "Giosuè, S.", "Girometta, B.", "Bugiani, R."),
        authors_complete=True,
        authors_from="read",
        checked="rossi2002.pdf (the conference archive's scan), first page",
        calibrated_on=("rossi2002.emilia",),
        # Its targets were back-calculated from the oil-spot dates with eqs 8-9's regressions.
        calibrated_with=("rossi2008.incubation",),
        calibration_note=(
            "read 2026-10-09: a stepwise regression (F = 4 to enter and leave) fitted to the"
            " probable infection periods of the plain's three zones, 1993-2000, found by"
            " counting the incubation regressions back from each zone's mean oil-spot date"
            " (pp. 264-265, Fig. 2). The regressions are Rossi 2008's eqs 8-9"
        ),
        structures=("oospore-glm",),
        structures_note=(
            "a regression on monthly weather for the season's first infection date: tagged"
            " strictly as oospore-glm, since its target is the date maturity allows the first"
            " infection, not maturity itself"
        ),
        parameters=(
            Published("intercept_pentads", 28.34, "pentad", "Tab. 3", "read"),
            Published("rain_days_march", -0.77, "pentad/d", "Tab. 3", "read"),
            Published("dry_spell_april", 0.33, "pentad/d", "Tab. 3", "read"),
        ),
        flags=(
            "R² 0.77 (adjusted 0.75), standard error 1.37 pentads, largest error 2.3 pentads,"
            " on the plain's zones only (Tab. 3, p. 268). The authors say it explains the data"
            " that generated it and must be checked in other years and places (pp. 269-270).",
            "Not run by any tool. Recorded because it was fitted with the engine's incubation"
            " regressions, and as a pattern of first-infection timing in Emilia-Romagna.",
        ),
    ),
    "fedele2025.dose": Formulation(
        "primary lesions from oospore dose",
        (
            "Fedele, Maddalena, Furiosi, Rossi, Toffolatti & Caffi 2025, Front. Plant Sci. "
            "16:1524959"
        ),
        year=2025,
        authors=(
            "Fedele, Giorgia",
            "Maddalena, Giuliana",
            "Furiosi, Margherita",
            "Rossi, Vittorio",
            "Toffolatti, Silvia Laura",
            "Caffi, Tito",
        ),
        authors_complete=True,
        authors_from="read",
        doi="10.3389/fpls.2025.1524959",
        # Section 2.5: leaves were observed until the end of the primary inoculum season,
        # "estimated using the epidemiological weather-driven model previously proposed by
        # Rossi et al. (2008b)"; section 3.4's dose regression fits those counts.
        calibrated_with=("rossi2008.primary",),
        calibration_note=(
            "read 2026-10-08 in the paper (Frontiers, open access), sections 2.5 and 3.4"
        ),
        structures=("oospore-dose-response",),
    ),
    "kernel.mixture": Formulation(
        "dispersal: splash plus an anisotropic exponential-power wind kernel",
        "assumed; scale bounded by Gobbin et al. 2005 (abstract only)",
        made_by="agrarium",
        structures=("dispersal-kernel",),
    ),
    "bucket.canopy-water": Formulation(
        "leaf wetness as water on the canopy (rain, dew, evaporation)",
        (
            "assumed (SWEB, the energy balance it once pointed to, shares an author with"
            " magarey2005.generic: a flag since D27, not kinship)"
        ),
        made_by="agrarium",
        structures=("canopy-water-balance",),
    ),
    "drawn.stage-dates": Formulation(
        "phenology: stage dates drawn around an average, later in hollows",
        "assumed",
        made_by="agrarium",
        structures=("drawn-stage-dates",),
    ),
    "erbs1982.partition": Formulation(
        "direct and diffuse light from the clearness index",
        "Erbs, Klein & Duffie 1982, Solar Energy 28(4):293-302, eq. 1, as pvlib writes it",
        year=1982,
        authors=("Erbs, D. G.", "Klein, S. A.", "Duffie, J. A."),
        authors_complete=True,
        authors_from="read",
        structures=("clearness-index-partition",),
    ),
    "winstral.shelter": Formulation(
        "wind shelter from the maximum upwind slope Sx",
        "Winstral & Marks 2002; Winstral et al. 2009, as SMRF implements it",
        year=2002,
        authors=("Winstral", "Marks"),
        authors_from="read",
        structures=("upwind-slope-shelter",),
    ),
    "winstral.shelter.decoupled": Formulation(
        "wind shelter, except on calm, clear nights, when valley air decouples",
        (
            "Winstral's shelter by day and on windy or cloudy nights; on calm, clear nights the "
            "regional wind, unsheltered, as decoupled air drains (Daly, Conklin & Unsworth 2010, "
            "Int. J. Climatol. 30:1857-1864, search summary); its thresholds are assumed"
        ),
        year=2010,
        authors=("Winstral", "Marks", "Daly", "Conklin", "Unsworth"),
        authors_from="snippet",
        made_by="agrarium",
        borrows=("winstral.shelter",),
        structures=("upwind-slope-shelter",),
    ),
    # -- Candidates read in the re-ingestion of 2026-10-08 (literature/), run by neither tool --
    "lalancette1988.infection": Formulation(
        "Infection efficiency of P. viticola by temperature and wetness duration",
        (
            "Lalancette, Ellis & Madden 1988, Development of an infection efficiency model for"
            " Plasmopara viticola on American grape based on temperature and duration of leaf"
            " wetness, Phytopathology 78:794-800, eq. 5"
        ),
        year=1988,
        authors=("Lalancette, N.", "Ellis, M. A.", "Madden, L. V."),
        authors_complete=True,
        authors_from="read",
        checked="Phyto78n06_794.pdf (Chris's drop), read 2026-10-08",
        calibrated_on=("lalancette1988a",),
        calibration_note=(
            "its own chamber data, read 2026-10-08 (literature/lalancette1988infection)"
        ),
        structures=("richards-wetness-infection",),
        structures_note=(
            "a tag of its own (2026-10-08): not Magarey's cardinal-temperature response, nor"
            " the generalized Analytis form"
        ),
        parameters=(
            Published("k.b0", -0.071, "lesions/zoospore", "eq. 5", "read"),
            Published("k.b1", 0.018, "lesions/zoospore/°C", "eq. 5", "read"),
            Published("k.b2", -0.0005, "lesions/zoospore/°C²", "eq. 5", "read"),
            Published("k.offset", 0.01, "lesions/zoospore", "eq. 5", "read"),
            Published("rho.b1", -0.24, "1/h", "eq. 5; W is wet hours minus 1", "read"),
            Published("rho.b2", 0.070, "1/(h·°C)", "eq. 5", "read"),
            Published("rho.b3", -0.0021, "1/(h·°C²)", "eq. 5", "read"),
            Published("m", 1.2, "dimensionless", "eq. 5 and text", "read"),
        ),
        flags=(
            "Fitted on V. labrusca 'Catawba' in growth chambers at 5-30 °C; the authors warn"
            " against use outside that range.",
            "Magarey et al. 2005's P. viticola row was fitted to the same data (lalancette1988a);"
            " the engine runs Magarey's model with other parameters, so this shares no data with"
            " the engine. Ellis and Madden are authors of the engine's Lalancette bound: a flag.",
            "Brazilian copies differ from eq. 5 (read 2026-10-09): Hamada et al. 2008 print the"
            " intercept -0.71; Reis et al. 2013 the exponent 1/(-1.2); Monteiro et al. 2012 and"
            " 2015 and Embrapa's Boletim 38 an intercept of -0.061, no +0.01 and e^(+rho);"
            " Rodrigues et al. 2019 and Alves et al. 2015 that, with T² for T and no WT² term."
            " Take the equation from eq. 5, not a copy (literature/hamada2008, reis2013,"
            " monteiro2012, monteiro2015, monteiro2015bol, rodrigues2019, alves2015).",
        ),
    ),
    "tranmanhsung1990.pom": Formulation(
        "POM: the date oospores mature, from a rain index since 21 September",
        (
            "Tran Manh Sung, Strizyk & Clerjeau 1990, Simulation of the date of maturity of"
            " Plasmopara viticola oospores to predict the severity of primary infections in"
            " grapevine, Plant Disease 74:120-124"
        ),
        year=1990,
        authors=("Tran Manh Sung, C.", "Strizyk, S.", "Clerjeau, M."),
        authors_complete=True,
        authors_from="read",
        checked="PlantDisease74n02_120.PDF (Chris's drop), read 2026-10-08",
        calibrated_on=("tranmanhsung1990.bordeaux",),
        calibration_note="read 2026-10-08 (literature/tranmanhsung1990)",
        structures=("oospore-glm",),
        structures_note=(
            "a regression of the maturity date on a rain index is 'a fitted statistical model"
            " of weather' as the vocabulary reads; Agrarium recommends a tag of its own (its"
            " PLAN 15), which would clear it of Leoni 2026's"
        ),
        parameters=(
            Published("a", -0.21, "d per index unit", "Results, T = A*IJ + B", "read"),
            Published("b", 117.9, "d from 1 January", "Results, T = A*IJ + B", "read"),
            Published("severity.intercept", 1.7, "class", "Results, S = 1.7 + 0.012 IJ", "read"),
            Published("severity.slope", 0.012, "class per index unit", "Results", "read"),
        ),
        flags=(
            "Fitted to three maturity dates; validated on the twelve years it was fitted to"
            " (a posteriori, as the paper says). It gives one date, not a cohort curve.",
            "DMCast (Park et al. 1997) computes POM's index (read in Caffi et al. 2007).",
            "The 1987 thesis version (Ronzon 1987, literature/ronzon1987) fits its coefficients"
            " to 1985 and 1986 alone, with 1984 as a check (17 April calculated, 16 April"
            " observed), and gives severity classes, not a regression (six exact and four off by"
            " one, 1977-1986).",
        ),
    ),
    "sentelhas2004.penman_monteith": Formulation(
        "Leaf wetness of a sensor by Penman-Monteith latent heat, with a water store",
        (
            "Sentelhas 2004, Duração do período de molhamento foliar..., livre-docência thesis,"
            " ESALQ/USP, Piracicaba, chapter 7 (after Rao et al. 1998 and Pedro & Gillespie"
            " 1982)"
        ),
        year=2004,
        authors=("Sentelhas, Paulo Cesar",),
        authors_complete=True,
        authors_from="read",
        checked="related-sentelhas-2004-thesis.pdf (Chris's drop), read 2026-10-08",
        structures=("canopy-water-balance",),
        structures_note=(
            "a store filled by dew and rain and emptied by latent heat: the bucket's form"
        ),
        calibration_note=(
            "none: its parameters are taken from the literature, not fitted (read 2026-10-08,"
            " literature/sentelhas2004)"
        ),
        parameters=(
            Published("gamma_star.dew", 0.64, "kPa/°C", "ch. 7, eq. 3", "read"),
            Published("gamma_star.rain", 1.28, "kPa/°C", "ch. 7, eq. 3", "read"),
            Published("store.dew_mm", 0.8, "mm", "ch. 7", "read"),
            Published("store.rain_max_mm", 0.6, "mm", "ch. 7", "read"),
            Published("sensor_size_m", 0.07, "m", "ch. 7, eq. 4", "read"),
        ),
        flags=(
            "Its author wrote the engine's sentelhas2008.wetness, a humidity threshold of"
            " another form: a flag (D27). Mean absolute error 1.05-1.50 h a day across turf,"
            " three sites and crop tops including grape.",
        ),
    ),
    "kim2007.bacchus": Formulation(
        "Botrytis infection risk (Bacchus): an hourly rate by temperature, summed over wet hours",
        (
            "Kim, Beresford & Henshall 2007, N. Z. Plant Prot. 60:128-132, in the corrected form"
            " Hill, Beresford & Evans 2019 print (Phytopathology 109:84-95, eq. 1 and Fig. 3)"
        ),
        year=2007,
        authors=("Kim, K. S.", "Beresford, R. M.", "Henshall, W. R."),
        authors_complete=True,
        authors_from="read",
        checked=(
            "Hill et al. 2019's eq. 1 (10-1094-phyto-10-17-0357-r.pdf, read 2026-10-08, the"
            " page image checked 2026-10-10); Kim et al. 2007 itself, p. 129, read in the page"
            " image 2026-10-10 (literature/kim2007nzpp)"
        ),
        structures=("wetness-temperature-infection-index",),
        structures_note=(
            "Broome's tag as the vocabulary reads today; Agrarium's PLAN 15 (D34) recommends a"
            " tag of its own, an hourly rate summed over wet hours"
        ),
        calibration_note=(
            "not recorded: Kim et al. 2007 credit the model to Rengasamy & Edwards (unpublished"
            " data) and print no fit; Hill et al. 2019 do not refit it"
        ),
        parameters=(
            Published("a", 84.37, "h", "Hill et al. 2019, eq. 1 and Fig. 3 caption", "read"),
            Published("b", 7.238, "h/°C", "Hill et al. 2019, eq. 1 and Fig. 3 caption", "read"),
            Published("c", 0.156, "h/°C²", "Hill et al. 2019, eq. 1 and Fig. 3 caption", "read"),
            Published("c_kim2007", 0.1856, "h/°C²", "Kim et al. 2007, p. 129", "read"),
        ),
        flags=(
            "Per wet hour (sensor response above 50%), x = 1/(a - b·T + c·T²): about 2.42 at its"
            " peak near 23.2 °C (derived). Hill et al. call it a correction to Kim et al. 2007"
            " without saying what changed; Beresford is an author of both.",
            "In 101 site-years it predicted bunch rot no better than simple humidity hours"
            " (AUC 0.647 against 0.729; Hill et al. 2019).",
            "Kim et al. 2007 (p. 129, page image, 2026-10-10) print I = 84.37 - 7.238T +"
            " 0.1856T² as the risk for each wet hour, summed over the wet period: no reciprocal,"
            " c = 0.1856. Hill et al.'s 'correction' changes both. At one point: Kim's I is"
            " lowest (13.8) at 19.5 °C and highest at 0 °C, so it reads as wet hours needed, near"
            " Broome's 10.5 h at 20 °C; with Hill's c, the reciprocal reaches 2.42 per wet hour"
            " at 23.2 °C, an infection in 0.41 wet hours. Which one Bacchus is, is not settled.",
        ),
    ),
    "gonzalezdominguez2015.botrytis": Formulation(
        "Botrytis bunch rot of grapevine, daily: conidia on inoculum sources from mycelial growth"
        " and sporulation (temperature, moist hours, humidity), infection of inflorescences and"
        " young clusters (stages 53-73) and of ripening berries by conidia and berry to berry"
        " (stages 79-89), each scaled by a growth-stage susceptibility, summed into three"
        " severity indices",
        "González-Domínguez et al. 2015, PLoS ONE 10(10):e0140444, Eqs 1-12 (pp. 4-7) and Table 1",
        year=2015,
        authors=(
            "González-Domínguez, Elisa",
            "Caffi, Tito",
            "Ciliberti, Nicola",
            "Rossi, Vittorio",
        ),
        authors_complete=True,
        authors_from="read",
        checked=(
            "gonzalez2015_botrytis_plosone.pdf (literature/gonzalezdominguez2015); Eqs 1-12 read"
            " in the page images 2026-10-20"
        ),
        doi="10.1371/journal.pone.0140444",
        structures=("age-resistance",),
        structures_note=(
            "SUS1 (Eq 5), the inflorescences' and young clusters' susceptibility, is a cubic in"
            " the growth stage that peaks near stage 65 and falls by stage 73: age resistance."
            " SUS2 and SUS3 (Eqs 8, 11) rise with the stage as berries ripen. INF1 and INF2"
            " (Eqs 4, 7) are a beta function of temperature times a function of wetness"
            " duration (logistic; Gompertz), Ciliberti's form: the form of Agrarium's open"
            " decision D33 (Magarey's structure), left untagged until it is decided, as"
            " literature/ciliberti2015flowers leaves it. INF3 (Eq 10) is a beta in temperature"
            " over a logistic in relative humidity; sporulation (Eq 3) a beta in temperature"
            " times a quadratic in relative humidity. No rain or temperature threshold"
            " triggers infection: the model assumes conidia disperse and land every day"
            " (DISR = DEPR = 1, p. 4)."
        ),
        calibrated_on=(),
        calibration_note=(
            "Not fitted here. Eqs 2 and 4 are Ciliberti et al. 2015 (Phytopathology 105:325-333,"
            " literature/ciliberti2015flowers), Eqs 7 and 10 Ciliberti et al. 2015"
            " (Phytopathology 105:1090-1096, literature/ciliberti2015berries), Eq 3 Ciliberti et"
            " al. 2015 (Aust. J. Grape Wine Res., 'accepted', not held), Eq 8 from"
            " Deytieux-Belleau et al. 2009's data (Eur. J. Plant Pathol. 125:551-563, not held),"
            " Eqs 5 and 11 from Ciliberti's data (S1 Appendix, not held): laboratory"
            " inoculations, none dated by a model. None of these sources is a record here."
            " Evaluated, not fitted, on 21 untreated epidemics in 12 vineyards, 2009-2014"
            " (gonzalezdominguez2015.epidemics) by discriminant analysis of SEV1-SEV3 against"
            " severity groups: 17 of 21 right, 15 of 21 cross-validated (literature/"
            "gonzalezdominguez2015). The authors say the equations 'were not validated"
            " against independent data'."
        ),
        parameters=(
            Published("time_step", 1, "d", "p. 4", "read"),
            Published("sporulation_window", 7, "d", "Eq 1 (the sum over i-6 to i, over 7)", "read"),
            Published("mygr_a", 3.78, "1", "Eq 2", "read"),
            Published("mygr_b", 0.9, "1", "Eq 2", "read"),
            Published("mygr_c", 0.475, "1", "Eq 2", "read"),
            Published("mygr_tmin", 0.0, "°C", "p. 4, under Eq 3", "read"),
            Published("mygr_tmax", 40.0, "°C", "p. 4, under Eq 3", "read"),
            Published("spor_a", 3.7, "1", "Eq 3", "read"),
            Published("spor_b", 0.9, "1", "Eq 3", "read"),
            Published("spor_c", 10.49, "1", "Eq 3", "read"),
            Published("spor_rh0", -3.595, "1", "Eq 3", "read"),
            Published("spor_rh1", 0.097, "1/%", "Eq 3", "read"),
            Published("spor_rh2", -0.0005, "1/%2", "Eq 3", "read"),
            Published("spor_tmax", 35.0, "°C", "p. 4, under Eq 3", "read"),
            Published(
                "moist_hour_rain", 0.2, "mm", "p. 4 (R >= 0.2 mm makes a moist hour)", "read"
            ),
            Published("moist_hour_wetness", 30, "min", "p. 4 (WD >= 30 min)", "read"),
            Published("moist_hour_rh", 90, "%", "p. 4 (daily average RH >= 90 %)", "read"),
            Published("inf1_a", 3.56, "1", "Eq 4", "read"),
            Published("inf1_b", 0.99, "1", "Eq 4", "read"),
            Published("inf1_c", 0.71, "1", "Eq 4", "read"),
            Published("inf1_d", 1.85, "1", "Eq 4", "read"),
            Published("inf1_e", 0.19, "1/h", "Eq 4", "read"),
            Published("inf1_tmax", 35.0, "°C", "p. 6, under Eq 4", "read"),
            Published("sus1_c3", -379.09, "1", "Eq 5, on GS/100", "read"),
            Published("sus1_c2", 671.25, "1", "Eq 5", "read"),
            Published("sus1_c1", -390.33, "1", "Eq 5", "read"),
            Published("sus1_c0", 75.209, "1", "Eq 5", "read"),
            Published("inf2_a", 6.416, "1", "Eq 7", "read"),
            Published("inf2_b", 1.292, "1", "Eq 7", "read"),
            Published("inf2_c", 0.469, "1", "Eq 7", "read"),
            Published("inf2_gompertz_b", 2.3, "1", "Eq 7", "read"),
            Published("inf2_gompertz_k", 0.048, "1/h", "Eq 7", "read"),
            Published("inf2_tmax", 35.0, "°C", "p. 7, under Eq 7", "read"),
            Published("sus2_a", 5e-17, "1", "Eq 8", "read"),
            Published("sus2_b", 0.4219, "1", "Eq 8, per growth stage", "read"),
            Published("inf3_a", 7.75, "1", "Eq 10", "read"),
            Published("inf3_b", 2.14, "1", "Eq 10", "read"),
            Published("inf3_c", 0.469, "1", "Eq 10", "read"),
            Published("inf3_d", 35.36, "1", "Eq 10", "read"),
            Published("inf3_e", 40.26, "1", "Eq 10, on RH/100", "read"),
            Published("inf3_tmax", 30.0, "°C", "p. 7, under Eq 10", "read"),
            Published("sus3_slope", 0.0546, "1", "Eq 11, per growth stage", "read"),
            Published("sus3_intercept", -3.87, "1", "Eq 11 (capped at 1)", "read"),
        ),
        flags=(
            "Can it run: yes, from daily mean temperature, mean relative humidity, rain, wetness"
            " hours and the BBCH-like stage (Lorenz et al.); every coefficient is printed. Teq ="
            " (T - Tmin)/(Tmax - Tmin), Tmin 0 °C throughout. Evaluated at one point each"
            " (derived 2026-10-20): MYGR peaks at 1.01 near 19 °C, SPOR's temperature term at"
            " 0.94 near 16.6 °C and its humidity term at 1.11 near 97 % (0.43 at 60 %); INF1"
            " at 0.93 near 17.4 °C before the wetness term; INF2's temperature term reaches"
            " 1.15 near 19.7 °C, above 1, and its wetness term is 0.10 at 0 h, 0.48 at 24 h;"
            " INF3's humidity term is 0.52 at 88 % and 0.04 at 80 %; SUS1 is 0.45 at stage 53,"
            " 1.0 at 65 and 0.5 at 73; SUS2 0.015 at 79 and 1.0 at 89; SUS3 0.44 at 79.",
            "Latent infection and incubation are not modelled ('insufficient quantitative"
            " information', p. 5); outputs are severity indices, not diseased area.",
            "Rossi and Caffi are authors of engine models (Rossi 2008, Caffi 2013): a flag.",
        ),
        role="process",
    ),
    "spotts1977.black_rot_wetness": Formulation(
        "Black rot (Guignardia bidwellii) leaf infection: the minimum leaf wetness for light"
        " infection at each of nine constant temperatures, 10-32 °C",
        "Spotts 1977, Phytopathology 67:1378-1381, Table 1 (p. 1379)",
        year=1977,
        authors=("Spotts, Robert A.",),
        authors_complete=True,
        authors_from="read",
        checked=(
            "spotts1977_phytopathology.pdf (literature/spotts1977); Table 1 read in the page"
            " image 2026-10-10 and again 2026-10-20"
        ),
        structures=("minimum-wetness-table",),
        structures_note=(
            "A table of the minimum wetness for infection at each temperature: infection when"
            " wetness exceeds a temperature-dependent minimum, the assumption Magarey's response"
            " fits a curve to. That is the question of Agrarium's open decision D33, so it gets"
            " a tag of its own, not Magarey's, until D33 is decided. No rain trigger."
        ),
        calibrated_on=("spotts1977.ohio",),
        calibration_note=(
            "Its own chamber inoculations: a compilation of several experiments on Concord,"
            " Catawba, Aurore and Baco Noir, five replicates a cultivar an experiment (Table 1,"
            " footnote a), conidia at constant temperature in a moisture chamber. No model"
            " produced or dated the data. The dataset record also holds the vineyard studies at"
            " Chesterville, Ohio, 1975-1976, which Table 1 was not made from."
        ),
        parameters=(
            Published("min_wetness_10_0c", 24, "h", "Table 1 (p. 1379), 10.0 °C", "read"),
            Published("min_wetness_13_0c", 12, "h", "Table 1 (p. 1379), 13.0 °C", "read"),
            Published("min_wetness_15_5c", 9, "h", "Table 1 (p. 1379), 15.5 °C", "read"),
            Published("min_wetness_18_5c", 8, "h", "Table 1 (p. 1379), 18.5 °C", "read"),
            Published("min_wetness_21_0c", 7, "h", "Table 1 (p. 1379), 21.0 °C", "read"),
            Published("min_wetness_24_0c", 7, "h", "Table 1 (p. 1379), 24.0 °C", "read"),
            Published("min_wetness_26_5c", 6, "h", "Table 1 (p. 1379), 26.5 °C", "read"),
            Published("min_wetness_29_0c", 9, "h", "Table 1 (p. 1379), 29.0 °C", "read"),
            Published("min_wetness_32_0c", 12, "h", "Table 1 (p. 1379), 32.0 °C", "read"),
            Published(
                "no_infection_temperature", 7.0, "°C", "p. 1379, Results (none after 48 h)", "read"
            ),
        ),
        flags=(
            "Can it run: as a lookup, from hourly temperature and leaf wetness; between the"
            " printed temperatures the table must be interpolated, which the paper does not"
            " do. Above 32 °C nothing was tested; at 7 °C no infection after 48 h of wetness."
            " Minimum near 26.5 °C (6 h), rising to 24 h at 10 °C and 12 h at 32 °C.",
            "Light infection only; no severity response is printed. Plants under variable"
            " temperature were infected significantly less than at constant temperature"
            " (Table 2), and a 1-day dry period after inoculation reduced severity (Table 3).",
            "The source of VitiMeteo black rot's thresholds, via Ellis et al. 1986"
            " (literature/molitor2016); the reprint in literature/vazquezabal2019 is shifted one"
            " row. The engine runs no black rot model.",
        ),
        role="process",
    ),
    "calonnec2018.leaf_susceptibility": Formulation(
        "Grapevine powdery mildew on leaves of known age: infection efficiency falling"
        " exponentially with leaf age, colony diameter a logistic step down with age, and the"
        " probability that a leaf is still susceptible (sporulating) a logistic in age",
        "Calonnec et al. 2018, Front. Plant Sci. 9:1808, Tables 4 and 5 (p. 8) and Results (p. 9)",
        year=2018,
        authors=(
            "Calonnec, Agnes",
            "Jolivet, Jerome",
            "Vivin, Philippe",
            "Schnee, Sylvain",
        ),
        authors_complete=True,
        authors_from="read",
        checked=(
            "q186.pdf (literature/calonnec2018; the byline read in the text 2026-10-20); Tables"
            " 4-5 and p. 9 read in the page images 2026-10-20"
        ),
        doi="10.3389/fpls.2018.01808",
        structures=("age-resistance",),
        structures_note=(
            "Susceptibility of leaves falling with their age in days since tagging at 3 cm:"
            " infection efficiency I0 exp(-k age), and a logistic probability of sporulating."
        ),
        calibrated_on=("calonnec2018.bordeaux",),
        calibration_note=(
            "Its own leaf-disc inoculations (22 mm discs, 22 °C, 12:12 h; literature/"
            "calonnec2018) on leaves from two Bordeaux vineyards, Cabernet Sauvignon (2005) and"
            " Merlot (2009-2010), sprayed 6-20 days before sampling. No model produced or dated"
            " the data."
        ),
        parameters=(
            Published("inf_i0_cabernet", 0.606, "1", "Table 4, Inf, model M1, exp. 2-3", "read"),
            Published("inf_k_cabernet", 0.086, "1/d", "Table 4, Inf, M1 (R² 0.57)", "read"),
            Published("inf_i0_merlot_exp4", 0.63, "1", "Table 5, Inf, M1, exp. 4", "read"),
            Published(
                "inf_k_merlot_exp4", 0.095, "1/d", "Table 5, Inf, M1, exp. 4 (R² 0.74)", "read"
            ),
            Published("inf_i0_merlot_exp5", 0.38, "1", "Table 5, Inf, M1, exp. 5", "read"),
            Published(
                "inf_k_merlot_exp5", 0.067, "1/d", "Table 5, Inf, M1, exp. 5 (R² 0.54)", "read"
            ),
            Published("diam_m_cabernet", 4.64, "mm", "Table 4, Diam, model M2", "read"),
            Published("diam_big_m_cabernet", 6.86, "mm", "Table 4, Diam, M2", "read"),
            Published("diam_a50_cabernet", 8.35, "d", "Table 4, Diam, M2 (R² 0.41)", "read"),
            Published("logit_b0", 4.12, "1", "p. 9, logistic regression, beta0", "read"),
            Published("logit_b1", -0.20, "1/d", "p. 9, logistic regression, beta1", "read"),
        ),
        flags=(
            "Can it run: yes, for infection efficiency and the probability of sporulation, from"
            " a leaf's age in days since it reached 3 cm; the age clock must come from a growth"
            " model (the paper: about one leaf per 21 degree-days above 10 °C). At one point"
            " (derived 2026-10-20): Cabernet's efficiency is 0.61 at age 0 and 0.18 at 14 days;"
            " the logit gives P = 0.8 at 13.7 days and 0.5 at 20.6 days, against the printed"
            " 13.3 [11.4; 14.9] and 20 [18.7; 21.4] (coefficients rounded in print).",
            "Merlot exp. 6 is printed with I0 = 2243 and k = 0.615 (Table 5), impossible for a"
            " proportion: not taken. Sporulation per colony (models M3, M4) is printed too,"
            " with four-parameter fits per experiment; not taken here.",
            "Leaves were sprayed 6-20 days before sampling, so not untreated. Laboratory discs"
            " at one temperature; no weather in the equations.",
        ),
        role="process",
    ),
    "savary2009.cluster_transfer": Formulation(
        "Cluster disease driven by foliage disease: dx_C/dt = tc x_L (1 - x_C) between crop"
        " stages 2 and 5 (BBCH 55-57 to 77-78), with leaf severity x_L a logistic curve in days;"
        " fitted for downy and powdery mildew in Bordeaux",
        "Savary et al. 2009, Phytopathology 99:930-942, Eqs 1-2 (p. 932) and Tables 4-5 (p. 937)",
        year=2009,
        authors=(
            "Savary, Serge",
            "Delbac, Lionel",
            "Rochas, Amélie",
            "Taisant, Guillaume",
            "Willocquet, Laetitia",
        ),
        authors_complete=True,
        authors_from="read",
        checked=(
            "savary2009_phyto.pdf (literature/savary2009); Eqs 1-2 and Tables 4-5 read in the"
            " page images 2026-10-20"
        ),
        doi="10.1094/PHYTO-99-8-0930",
        structures=("bunch-susceptibility-window",),
        structures_note=(
            "tc is set to zero before crop stage 2 and after crop stage 5, 'due to decreasing"
            " susceptibility of maturing clusters in both DM (21) and PM (6,8-10)' (p. 932), and"
            " reference 21 is Kennelly et al. 2005, the source of the engine's bunch window;"
            " the stage scale is Kennelly et al.'s too (Table 1). A fixed window of cluster"
            " susceptibility is the engine's form, cited, not computed: kin by structure, not a"
            " borrowed equation. Eq 1, a logistic in days, and Eq 2 have no weather in them."
        ),
        calibrated_on=("savary2009.bordeaux",),
        calibration_note=(
            "Fitted to the plot means of its own trials (savary2009.bordeaux), x_L from Eq 1's"
            " fit to each site-year-management case (Table 4), then tc by nonlinear least"
            " squares on the cluster severities (Table 5). Sprays in the limited and continuous"
            " plots were at fixed crop stages, not timed by a model (literature/savary2009)."
        ),
        parameters=(
            Published("tc_dm_couhins_2006_unprot", 0.029, "1/d", "Table 5", "read"),
            Published("tc_dm_couhins_2006_limited", 0.007, "1/d", "Table 5", "read"),
            Published("tc_dm_couhins_2007_unprot", 0.227, "1/d", "Table 5", "read"),
            Published("tc_dm_couhins_2007_limited", 0.280, "1/d", "Table 5", "read"),
            Published("tc_dm_latresne_2006_unprot", 0.008, "1/d", "Table 5", "read"),
            Published("tc_dm_latresne_2007_unprot", 0.374, "1/d", "Table 5", "read"),
            Published("tc_dm_latresne_2007_limited", 0.189, "1/d", "Table 5", "read"),
            Published("tc_pm_couhins_2006_unprot", 0.538, "1/d", "Table 5", "read"),
            Published("tc_pm_couhins_2006_limited", 0.039, "1/d", "Table 5", "read"),
            Published("tc_pm_couhins_2007_unprot", 1.269, "1/d", "Table 5", "read"),
            Published("tc_pm_couhins_2007_limited", 0.518, "1/d", "Table 5", "read"),
            Published("tc_pm_latresne_2006_unprot", 0.050, "1/d", "Table 5", "read"),
            Published("tc_pm_latresne_2007_unprot", 0.361, "1/d", "Table 5", "read"),
            Published("tc_pm_latresne_2007_limited", 0.191, "1/d", "Table 5", "read"),
            Published("r_dm_couhins_2006_unprot", 0.052, "1/d", "Table 4", "read"),
            Published("r_dm_couhins_2007_unprot", 0.029, "1/d", "Table 4", "read"),
            Published("r_dm_latresne_2006_unprot", 0.062, "1/d", "Table 4", "read"),
            Published("r_dm_latresne_2007_unprot", 0.028, "1/d", "Table 4", "read"),
            Published("r_pm_couhins_2006_unprot", 0.068, "1/d", "Table 4", "read"),
            Published("r_pm_couhins_2007_unprot", 0.109, "1/d", "Table 4", "read"),
            Published("r_pm_latresne_2006_unprot", 0.025, "1/d", "Table 4", "read"),
            Published("r_pm_latresne_2007_unprot", 0.070, "1/d", "Table 4", "read"),
        ),
        flags=(
            "Can it run: as a coupling, given a leaf-severity series from any model and the"
            " dates of crop stages 2 (BBCH 55-57) and 5 (77-78); tc is per day per unit of leaf"
            " severity, severities as proportions. It varies tenfold between years (downy"
            " mildew at Couhins 0.029 in 2006, 0.227 in 2007), so it is a site-year parameter,"
            " not a constant. Latresne 2006 limited did not converge (NC).",
            "Not a weather model: the logistic leaf curve (Eq 1) and the transfer (Eq 2) are"
            " fitted per case. The 70 logistic regressions of cluster thresholds on leaf"
            " severity (Eq 3) are in literature/savary2009, not recorded here.",
        ),
        role="process",
    ),
    "kast2010.oidiag": Formulation(
        "OiDiag-2.2, Weinsberg's powdery mildew index: a daily index, an ontogenic term in days"
        " since the three-leaf stage times a climatic term from daily mean temperature, hours"
        " of humidity above 65 and 80 %, rain and leaf wetness, as a 7-day sliding mean that"
        " sets the next spray interval by fungicide class",
        "Kast & Bleyer 2010, Proc. 6th Int. Workshop on Grapevine Downy and Powdery Mildew,"
        " Bordeaux, pp. 151-152 of the proceedings (Table 1 and the index equations)",
        year=2010,
        authors=("Kast, W. K.", "Bleyer, K."),
        authors_complete=True,
        authors_from="read",
        checked=(
            "gdpm2010_proceedings_6th_bordeaux.pdf (literature/kast2010); p. 152 read in the page"
            " image 2026-10-20"
        ),
        structures=("daily-weather-risk-index", "age-resistance"),
        structures_note=(
            "Id = CL x ON, a 7-day mean in %. CL from T = ((0.11 TM - 0.0025 TM^2) - 0.6) x"
            " 1.63, H = (H80 + 0.7 H65)/24 and a rain-and-wetness term R that counts against"
            " the epidemic, bounded to 0-1.1. ON, a function of days since the three-leaf"
            " stage that peaks about three weeks later and then falls: age resistance. Not the"
            " UC Davis index's form (hours in a temperature band)."
        ),
        calibration_note=(
            "Not recorded as datasets. T is 'a function developed that best fitted to the data"
            " of Delp (1954) and Fessler and Kassemeyer (1995)' by multiple regression; ON"
            " follows Stark-Urnau and Kast (1999) for Württemberg and Baden; H is OiDiag 1.0's"
            " (Kast 1997). None of these is a record here; no model dated those data, as far as"
            " the paper says."
        ),
        parameters=(
            Published("t_a", 0.11, "1/°C", "p. 152, temperature index", "read"),
            Published("t_b", -0.0025, "1/°C2", "p. 152, temperature index", "read"),
            Published("t_c", -0.6, "1", "p. 152, temperature index", "read"),
            Published("t_scale", 1.63, "1", "p. 152, temperature index", "read"),
            Published("h_weight_65_80", 0.7, "1", "p. 152, H = (H80 + H65 x 0.7)/24", "read"),
            Published("h_weight_80", 1.0, "1", "p. 152", "read"),
            Published("r_rain_min", 2.5, "mm/d", "p. 152, rain below it neglected", "read"),
            Published("r_rain_heavy", 10.0, "mm/d", "p. 152, LWET x 3 above it", "read"),
            Published("r_weight", 1.5, "1/h", "p. 152, R1 = LWET x 1.5", "read"),
            Published("r_weight_heavy", 3.0, "1/h", "p. 152, R = LWET x 3", "read"),
            Published("cl_max", 1.1, "1", "p. 152, climatic index bounded to 0-1.1", "read"),
            Published("on_d3", 0.0002, "1", "p. 152, ON's D^3 term", "read"),
            Published("on_sqrt", 176.6, "1", "p. 152, ON's SQRT(D) term", "read"),
            Published("on_ln", -114.9, "1", "p. 152, ON's LN(D) term (printed '114,9*')", "read"),
            Published("on_d", -14.0, "1", "p. 152, ON's D term", "read"),
            Published("on_c", -66.0, "1", "p. 152, ON's constant; all over 100", "read"),
            Published("sliding_window", 7, "d", "p. 152, sliding mean", "read"),
        ),
        flags=(
            "Cannot run as printed: how T, H and R combine into the climatic index CL is not"
            " stated (p. 152 gives the three terms and the 0-1.1 bound only). ON is printed"
            " with unbalanced parentheses and '114,9*'; read as (0.0002 D^3 + 176.6 sqrt(D) -"
            " 114.9 ln(D) - 14.0 D - 66.0)/100 it gives 0.97 at day 1, 0.74 at day 5, 1.01 at"
            " day 20, 0.58 at day 50 and turns negative after about day 76 (derived"
            " 2026-10-20). T peaks at 0.99 near 22 °C and is negative below about 6 °C.",
            "Table 1 maps the index (0-20, 21-40, 41-60, 61-80, >80 %) to the days until the next"
            " spray for four fungicide classes, e.g. wettable sulfur 14, 12, 8, 7, 6 days and the"
            " class-4 products 23, 18, 15, 12, 11 days.",
            "The first-spray rule from 53 years of Weinsberg records (three-leaf date + (1.3T -"
            " 5D + 12) days) gives -26 days for the paper's own example (literature/kast2010).",
        ),
        role="process",
    ),
}
