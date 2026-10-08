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
        calibration_note=(
            "Not recorded. Kennelly et al. 2007 say the criterion 'was developed (7,8)' by"
            " Gadoury et al. 1998 and 2000 'using the reported data', naming none, and evaluated"
            " it in four Finger Lakes Chancellor vineyards, 2001-2003 (read 2026-10-08)"
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
        calibrated_on=("goidanich1957",),
        calibration_note=(
            "Inferred, trail (2026-10-08): eqs 8-9 are Rossi et al. 2002's regressions, which"
            " Rossi et al. 2005 describe as relating temperature to incubation at two humidity"
            " levels after Goidanich et al. 1957. Rossi et al. 2002 is not held"
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
        structures_note="from its title alone; the paper is not held",
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
            "Shared data, which kinship cannot see (it compares authors and borrowed"
            " equations). Table 2's P. viticola row was fitted to Lalancette, Ellis & Madden"
            " 1988 (its ref. 43, 5-28 °C, 2-24 h wet, 20% incidence), the Ohio infection data;"
            " its grape Botrytis rows to Nair & Allen 1993 (ref. 56: berries 12-30 °C, flowers"
            " 5-30 °C, 20% incidence). Its Botrytis Tmax of 35 °C is the paper's default where"
            " none was measured.",
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
        structures=("wet-degree-hours-infection",),
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
            " threshold was fitted (read 2026-10-08)"
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
    ),
    "broome1995.botrytis": Formulation(
        "Botrytis infection index per wet period",
        "Broome et al. 1995, Phytopathology 85: 97-102, as UC IPM states the rules; not held",
        year=1995,
        authors=("Broome, J.", "English, J.", "Marois, J.", "Latorre, B. A.", "Aviles, J."),
        authors_from="trail",
        checked="UC IPM's page; González-Domínguez et al. 2015's reference list (held)",
        structures=("wetness-temperature-infection-index",),
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
    ),
    "thiessen2018.ascospores": Formulation(
        "Powdery mildew ascospore release days",
        "Thiessen, Neill & Mahaffee 2018, Plant Disease 102: 1500-1508; not held",
        year=2018,
        authors=("Thiessen", "Neill", "Mahaffee"),
        authors_from="trail",
        checked="models/powdery_mildew.py",
        structures=("ascospore-release-rule",),
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
        "Shortest incubation, infection to oil spots, by mean temperature: Vello and Patras",
        (
            "Zachos 1959, Recherches sur la biologie et l'épidémiologie du mildiou de la vigne"
            " en Grèce. Bases de prévisions et d'avertissements, Ann. Inst. Phytopathol. Benaki"
            " N.S. 2(4):193-355, chapter II, Figs 3-4 and Table XIII"
        ),
        year=1959,
        authors=("Zachos, D. G.",),
        authors_complete=True,
        authors_from="read",
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
            "Magarey et al. 1991's incubation cubic was fitted partly to these data. Cooptera's"
            " magarey2010.rules computes no incubation curve, only the fact sheet's 5-day lower"
            " bound (Cooptera, 2026-10-08); where the sheet's 5-17 days came from is unknown.",
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
        "assumed (SWEB, the energy balance it once pointed to, is kin through Magarey)",
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
}
