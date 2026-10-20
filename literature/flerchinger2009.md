---
id: flerchinger2009
citation: Flerchinger, G. N., Xaio, W., Marks, D., Sauer, T. J. & Yu, Q. 2009. Comparison of algorithms for incoming atmospheric long-wave radiation. Water Resources Research 45:W03423 (corrected 13 June 2017)
doi: 10.1029/2008WR007394
read: 2026-10-19, abstract, sections 2-5 and the erratum by the main session; Tables 1, 2, 9, 10 and 12 and the erratum read on the page images (170 dpi)
status: read
diseases: []
crops: []
regions: [North America, China, Idaho, Iowa, Yucheng, Tibetan Plateau]
processes: [downward longwave radiation, cloud correction, clear-sky emissivity, net radiation]
records: [flerchinger2009.dilley_unsworth]
datasets: [flerchinger2009.sites]
files: [flerchinger2009.pdf (open access, fetched 2026-10-19 for the pilot equations)]
---

# Flerchinger et al. 2009: thirteen clear-sky and ten cloud-corrected longwave algorithms at 21 sites

Read because the placement pilot's SWEB needs canopy net radiation at night and the truth's
weather has none: this is the multi-site validation of longwave estimates from air temperature,
humidity and cloud.

## What it holds

- **Algorithms** (Tables 1-3): 13 clear-sky forms (Ångström, Brunt, Brutsaert, Garratt, Idso &
  Jackson, Idso, Iziomon, Keding, Niemelä, Prata, Satterlund, Swinbank, Dilley & O'Brien), 10 cloud
  corrections (8 on cloud fraction c, 2 on a solar index), and Aubinet's four all-sky forms. Units:
  e_o in kPa, T_o in K, w in cm, fluxes W m⁻².
- **Data** (Table 4): measured downward longwave at 14 sites for fitting the clearness limits (nine
  AmeriFlux sites, Reynolds Mountain ID, Brooks field IA, Yucheng, Ganzi, Nagqu) and 7 independent
  AmeriFlux sites; mostly two years of 30-min data, 1982-2007; radiometers at least 2 m above the
  vegetation. Cloud is not observed: it comes from the clearness index, by Campbell's linear rule
  (c = 1 at k_cld, 0 at k_clr) or Kasten & Czeplak's S = S_clr(1 − 0.75c^3.4) inverted (Eq 5-6).
- **Clear sky** (Tables 5-6): Dilley, Prata and Ångström best, RMSD about 23 W m⁻² hourly; Dilley
  underestimates.
- **All sky** (Tables 7-12): Dilley with Kimball, Unsworth or Crawford best. Dilley-Unsworth with
  k_cld 0.15 and k_clr 0.80 (Table 9): RMSD 24.5 W m⁻² hourly and 14.9 W m⁻² daily over 14 sites
  (Table 10), 26.9 W m⁻² at the 7 independent sites (Table 12). Campbell's linear rule beat Kasten &
  Czeplak's (32.6 W m⁻² for the best pair with it).
- **Night** (Sect. 4.7): midnight RMSD 25.0-25.6 W m⁻² for the five best pairs against 19.3-20.6 W m⁻²
  at noon with a 4-hour solar window; night cloud comes from the 24 h of sunshine around the hour.
- **Erratum (2017, p. 14, page image):** Table 1's Dilley term is 96.96√(w/2.5), not √(w/25), and
  w = 465 e_o/T_o, not 4650; Ångström's exponent is −0.67 e_o, not −0.067 e_o; Brutsaert's 1982
  correction is (1 + 0.22c²). The two Dilley typos cancel (4650/25 = 465/2.5), so Table 1 as first
  printed gives the same L_clr; Prata's w does change.

## Dependence

- **Borrowed and cited, none a record:** Dilley & O'Brien 1998, Unsworth & Monteith 1975, Campbell
  1985, Kasten & Czeplak 1980 and the other algorithms' sources. The paper fits only the clearness
  limits (k_cld, k_clr), on the 14 sites (`flerchinger2009.sites`).
- **The engine** runs no radiation model; nothing here is shared with it.

## Bearing (2026-10-19)

- **The validated estimate for the pilot's night radiation:** Dilley's clear sky with Unsworth's
  cloud correction takes air temperature, vapour pressure and the cloud fraction, which the truth's
  weather draws directly. Recorded as `flerchinger2009.dilley_unsworth` with
  `formularium.equations.flerchinger2009`.
- **Two gaps between it and SWEB:** it gives the downward flux, so the canopy's net needs its own
  emission (Kuwagata 2024's effective radiation takes the canopy at air temperature); and its
  validation took cloud from the clearness index, not from a given cloud fraction.
- No vineyard, no Mediterranean lowland: the nearest climate is Reynolds Mountain, Idaho, semiarid
  rangeland "characterized by a Mediterranean climate" at 2,097 m.
