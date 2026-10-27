# Sensors by tier, for Agrarium D60 (part 3 of inputs-d60.md)

Answer to part 3 of `inputs-d60.md` (this folder), 2026-10-27, by an `ingest` session. A strand
agent (claude-sonnet-5-5) read network station lists, field tests, reviews and makers' sheets;
every quote it cites was found at its line by `scripts/verify_quotes.py`. Kept here rather than as
`literature/sensors-d60.md` because note ids carry no hyphens; the papers read have notes.

How each claim was checked: **read** (the page or paper, quoted), **trail** (a held note:
`research_notes/placement-methods` section 7, "PM7"), **snippet** (a search summary or a page not
read as a document). Most network lists beyond AgroClim and Agrometeo are snippets.

## Tiers

- **Common** (typical farm stations and agricultural networks): air temperature and humidity at
  2 m; rain (tipping bucket); wind speed and direction (cup and vane, 2 m to 10 m); global
  radiation (pyranometer). Soil temperature is common; soil moisture on US networks.
  **Leaf wetness** is on disease-warning and research networks (AgroClim, every station, Cimel
  HU1871, `furushopercot2025`, read; Agrometeo, in minutes, `dubuis2020`, read; AgWeatherNet,
  Enviroweather and NEWA where fitted, snippet) and a Davis add-on, but not in Spain's SIAR base kit
  (snippet). Whether Meteocat's XEMA stations measure it is unconfirmed: its public station page
  lists no variables (no Meteocat API was called).
- **Cheap and emerging** (a grower could add them now): in-canopy T/RH nodes (RH error 2.7-7.4 %RH,
  nothing split above 90 %; PM7, trail); capacitive soil probes (RMSE 2.36-2.88 % VWC after
  soil-specific calibration, `adla2020`, read); Sentinel-2 NDVI (free, 10 m; R² 0.84-0.87 against
  drone NDVI, not significant on blocks under 0.5 ha, `sozzi2020`, read); drone point-cloud LAI
  (R² 0.82 against manual, 704 vines, `comba2020`, read); silicon-cell radiation (leads, unread).
- **Research only:** automated spore detection: rotating-arm traps with qPCR or LAMP (detection
  limit 0.3 sporangia m⁻³, sampled three times a week; `douillet2023`, held) and the real-time
  SwisensPoleno counter (r up to 0.94 against Hirst counts, but only late in the season;
  `cattani2026`, held); satellite LAI in clumped vines (unfitted products RMSE 0.97-1.27,
  `kang2022`, read); net radiometers (on no network list found); hyperspectral LAI.

## Leaf-wetness sensors, which matter most to D60

- **Type matters.** A painted resistance grid behaves like a leaf; an unpainted one missed dew
  onset 15.4 % of the time at 30° and 30.8 % at 45° (`lau2000`, held). Dielectric plates (PHYTOS 31,
  Campbell LWS, Onset S-LWA): no accuracy printed by the makers; Onset ±10 % between sensors;
  duration depends on mounting angle (`onofre2020`, an extension guide, read).
- **No placement standard exists** (Gleason 2008, held): NEWA says north-facing at 45°; UF/IFAS 30 cm
  and 30-45°; Campbell cites 60°. A measured-wetness variable should carry its sensor type and
  placement.
- **Sensor against canopy:** positions inside a canopy differ by under 1.5 h a day (PM6, trail); a
  station off the canopy by 2-4 h (`kleb2022`, `kleb2026thesis`).

## Not found

Swisens Poleno's price; makers' accuracy for dielectric wetness plates; XEMA's variable list.
Unread leads: Martinez et al. 2009 (Sensors 9:4615) and Gómez-Moreno et al. 2016 (Energies 9:926)
on silicon-cell pyranometers; Lieberherr et al. 2021 (AMT 14:7693) on real-time bioaerosol
counters; Buters et al. 2022; Vélez et al. 2021 (OENO One); Placidi et al. 2020; Paciolla et al. 2021.
The strand's full table, with lines: `/srv/papers/drop/2026-10-27-inputs-d60/reading/sensors/LEADS.md`
on `agents`.
