---
id: maddalena2022
citation: Maddalena, G., Lecchi, B., Serina, F., Torcoli, S., S.L. Toffolatti (printed 'Maddalena1, 2, *, G., Lecchi1, B., Serina3, F., Torcoli3, S. & Toffolatti1'), S.L. 2022. Oospore germination dynamics and disease forecasting model: an integrated approach for downy mildew management. BIO Web of Conferences (GDPM 2022) 50:04002 (article number, 4 pages)
doi: 10.1051/bioconf/20225004002
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 27 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Lombardy]
processes: [oospore germination, primary infection, season onset]
records: []
datasets: [maddalena2022.franciacorta]
files: [10-1051-bioconf-20225004002.pdf]
---

# Maddalena et al. 2022: oospore germination and EPI in Franciacorta

From the University of Milan and the Franciacorta consortium.

## What it holds

- Maddalena et al. combine oospore germination assays with the EPI model in Franciacorta, 2021 (l. 120).
- Ten vineyards, 8 of them Chardonnay (l. 103); untreated plots of about 75 plants assessed weekly (l. 124).
- Germination: oospore-rich leaves from three vineyards, collected mid-October 2020 (l. 115). Assays once or twice a week from late March to end of June 2021 (l. 118), at 20 C (l. 123), checked daily for 1 to 16 days (l. 125). t is the minimum days to germinate (l. 128).
- Germination was seen until 21 June (l. 172). t fell to 2-5 days when EPI showed risk (l. 162). No table of t.
- EPI (Strizyk; Sesma version in Epicure) gives an FTA risk index; no formula is printed (l. 65, 160). It predicted medium-high risk from end of April to early June (l. 154, 155).
- First symptoms were seen 6-21 May (l. 157), from infections dated 28 April-11 May (l. 158).
- The paper says the incubation period was "calculated (Goidanich et al., 1957)" to find the most probable infection date (l. 176). It does not name the 28 April-11 May dates as its output, but infection is not observed in the field, so they probably carry Goidanich's assumption (inference).
- At bunch closure I%D was 66 and 68, I%I 18 and 31, for leaves and bunches (l. 195).
- One season only (l. 220); no statistic for the "high accuracy" (l. 200).

## Dependence

- **Its infection dates were placed by Goidanich et al. 1957's incubation:** "the length of incubation period was calculated (Goidanich et al., 1957), to ... ascertain the most probable date of disease infection occurrence" (l. 175-177). The paper names the method, not each date's source; infections are not seen in the field, so the reported dates (28 April-11 May, l. 158) are that method's. The engine runs Goidanich's table, so anything fitted or scored on those dates is calibrated with `goidanich.incubation` (Formularium dataset `maddalena2022.franciacorta`).
- It runs EPI (Strizyk's, the Sesma version in Epicure) without printing it.
- Maddalena and Toffolatti co-wrote Fedele 2025 with Rossi and Caffi: flags.

## Bearing (2026-10-08)

- **Kin by calibration, not by its authors** (Agrarium's candidates; D27 as amended). Its germination assays (t falling to 2-5 days as risk rose, l. 162; germination until 21 June, l. 172) are clear data; its infection dates are Goidanich's.
