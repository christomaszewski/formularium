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
        "Rossi, Caffi, Giosuè & Bugiani 2008, Ecological Modelling 212: 480-491",
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
        checked="2008-rossi-10-1111-j-1365-3059-2007-01738-x.pdf",
        structures=("hydro-thermal-oospore-cohorts",),
        calibrated_on=("rossi2008pp.discs",),
    ),
    "blaeser1979.survival": Formulation(
        "Survival of sporangia, and 60 °C·h of wetness to infect",
        (
            "Blaeser & Weltzien 1979, credited for these equations by Rossi et al. 2008 and "
            "Brischetto et al. 2020 (both read); not held"
        ),
        year=1979,
        authors=("Blaeser", "Weltzien"),
        authors_from="trail",
        checked=(
            "2008-rossi-10-1016-j-ecolmodel-2007-10-046.pdf; "
            "2020-brischetto-10-3389-fpls-2020-01187.pdf"
        ),
        structures=("vpd-survival", "wet-degree-hours-infection"),
        structures_note=(
            "read 2026-10-09 (literature/blaeser1979): survival as a quadratic in the saturation"
            " deficit, infection as a constant temperature sum over the wet period"
        ),
        calibrated_on=("blaeser1978.survival", "blaeser1979"),
        calibration_note=(
            "Read 2026-10-09 in the paper (Z. PflKrankh. PflSchutz 86:489-498, by Marlene"
            " Blaeser and H. C. Weltzien; Cooptera's list keeps its trail record): the survival"
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
        checked="2013-caffi-10-1094-phyto-04-12-0082-r.pdf",
        structures=("dark-moist-hours-sporulation",),
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
        "Brischetto et al. 2020, doi:10.3389/fpls.2020.01187, equations 1 and 2",
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
            "Magarey 2010, Managing Downy Mildew (GWRDC fact sheet), the page's default disease "
            "layer; not held"
        ),
        year=2010,
        authors=("Magarey, P. A.",),
        authors_from="trail",
        checked="models/downy_mildew.py's docstring",
        borrows=("noaa.solar_position",),
        structures=("rain-temperature-trigger",),
    ),
    "puelles2024.ur": Formulation(
        "UR mildiu rules (La Rioja)",
        "Puelles et al. 2024, Crop Protection, doi:10.1016/j.cropro.2023.106450",
        year=2024,
        authors=("Puelles, M.", "Arbizu-Milagro, J.", "Castillo-Ruiz, F.J.", "Peña, J.M."),
        authors_complete=True,
        authors_from="read",
        checked="2024-puelles-10-1016-j-cropro-2023-106450.pdf",
        borrows=("goidanich.incubation",),
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
            " 1987, the 50 °C·h to Dubuis et al. 2012"
        ),
        flags=(
            "The paper's UR model also computes the 3-10 conditions (T >= 10 °C, shoots >= 10 cm,"
            " 10 mm in 24-48 h, 'the same algorithm as the Goidanich model'), which Cooptera's"
            " list does not name among its borrowings (asked 2026-10-09). It adds germination"
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
        checked="Leoni et al. 2026's reference list (held)",
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
            " years named. Bleyer et al. 2008 (read 2026-10-08) prints no oospore rule"
        ),
        flags=(
            "Hoppmann & Wittich 1997 (Z. PflKrankh. PflSchutz 104:533-544, p. 536; read"
            " 2026-10-09) print the same form for the Geisenheim (DWD) model with 170"
            " degree-days above a daily mean of 8 °C 'during spring', not 140. Gessler et al."
            " 2011 (Phytopathol. Mediterr. 50:3-44, p. 7; read 2026-10-09) give Gehmann et"
            " al. 1987's German rule as 160 °C·days above 8 °C from 1 January, at 2 m.",
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
        "Broome et al. 1995, Phytopathology 85: 97-102, as UC IPM states the rules; not held",
        year=1995,
        authors=("Broome, J.", "English, J.", "Marois, J.", "Latorre, B. A.", "Aviles, J."),
        authors_from="trail",
        checked="UC IPM's page; González-Domínguez et al. 2015's reference list (held)",
        structures=("wetness-temperature-infection-index",),
        flags=(
            "The paper is held in Chris's drop and read since 2026-10-08 (literature/"
            "broome1995): its byline is J. C. Broome, J. T. English, J. J. Marois, B. A."
            " Latorre and J. C. Aviles. The combined fit's b2 is garbled in the text copy, so"
            " 0.061601 needs the page image. Cooptera's list, which this record must match,"
            " still gives the trail.",
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
            " Rodrigues et al. 2019 that, with T² for T and no WT² term. Take the equation from"
            " eq. 5, not a copy (literature/hamada2008, reis2013, monteiro2012, monteiro2015,"
            " monteiro2015bol, rodrigues2019).",
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
}
