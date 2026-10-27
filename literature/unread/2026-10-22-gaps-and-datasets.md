# Gaps and datasets (2026-10-22): leads not obtained or not read

The night pass of 2026-10-21/22 searched for Agrarium's and Cooptera's open gaps and for open
datasets. Two literature strands ran, the downy mildew cycle (34 OpenAlex calls) and the
Penedès host (43 calls), and a retry strand took the leads earlier passes could not fetch.
Nothing below was read. Titles and DOIs are from the strands' reference lists or Crossref,
unchecked unless said.

- **How they were tried:** the publisher's page; every OpenAlex location
  (`fetch_locations.py`); Europe PMC; the Wayback Machine (online again on 2026-10-22);
  institutional repositories.
- **Refusals:** Wiley, Elsevier, APS and ACS refuse this VM. digital.csic.es serves
  "accesoRestringido" for the Boso papers. TDX returned 403. incavi.gencat.cat returned a
  block page.

## Downy mildew cycle

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 1989 | G. K. Hill | Effect of temperature on sporulation efficiency of oilspots caused by *Plasmopara viticola* in vineyards. Wein-Wissenschaft 44:86-90 | none | lesion decline over 2-3 months; `dm.sporulating_days` | not online |
| 2014 | C. E. L. Delmas | J. Microbiol. Methods (zoospores per sporangium) | 10.1016/j.mimet.2014.10.012 | the zoospore-to-sporangium conversion | Elsevier |
| 2002 | F. J. Rodríguez-Rajo | Ourense aerobiology, *Plasmopara* peak at 11-12 h (cited by `albelda2005`) | not identified | release hour | reference not identified |
| 1998 | M. R. Díaz | Seasonal variation of airborne fungal spore concentrations in a vineyard of North-West Spain. Aerobiologia 14:221-227 | 10.1007/bf02694210 (Crossref, match unconfirmed) | release hour | not fetched |
| 1998 | Paredes | Jornadas de Viticultura y Enología, Tierra de Barros, 91-96 | none | release hour | not online |
| 2008 | Cursano | cited by Rossi et al. 2009 for 5 % of soil splashes reaching leaves | not identified | splash | not identified |

## Penedès host

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2014 | S. Boso | Susceptibility to downy mildew of different *Vitis* varieties. Crop Protection 63 | 10.1016/j.cropro.2014.04.018 | the same | Elsevier; green copy restricted |
| 2015 | M. C. Ramos | Spatial and temporal variability of cv. Tempranillo phenology and grape quality within the Ribera del Duero DO. Int. J. Biometeorol. 59:1849-1860 | 10.1007/s00484-015-0992-z (Crossref) | elevation delay in days | not tried |
| 2022 | A. Cameron | The effect of temperature on grapevine phenological intervals: sensitivity of budburst to flowering. Agric. For. Meteorol. 315:108841 | not found | budburst-to-flowering interval against temperature | Elsevier, not tried |
| 2019 | A. Hall & J. Blackman | Modelling within-region spatiotemporal variability in grapevine phenology. OENO One 53(2) | 10.20870/oeno-one.2019.53.2.2450 | spread of budburst between vineyards | oeno-one.eu timed out |
| 2004 | M. A. Pozo-Bayón | Effect of vineyard yield on the composition of sparkling wines produced from Parellada. Food Chem. 86:413-419 | 10.1016/j.foodchem.2003.09.016 | Parellada yield per vine | Elsevier |
| - | M. C. Ramos (Univ. Lleida) | the 1996-2009 stage dates behind `ramos2010`, `ramos2008`, `ramos2017` | - | yearly budbreak including Xarel·lo | unpublished: ask the author |
| - | INCAVI, DO Penedès, Servei de Sanitat Vegetal | campaign reports; weekly phenology and warning bulletins | - | budbreak by year; first oil spots since 1961 | incavi.gencat.cat block page |

## Retry strand

Leads from earlier passes, retried on 2026-10-22 (the strand's log of every place tried is in
the drop's `reading/g7_retry/search.md`). Obtained and read: Pérez-Rodríguez 2013, Ebeling
2018, Batzer 2008, Leroy 2013, Pelosi 2023, Calonnec 2004 and 2008, Legler 2013, Ridley
2010 (in-press proof), Dhakar 2025's Appendix A, Gindro 2022, Boso 2011; Gobbin 2005 and 2007
filed (their notes were read in 2026-10-09). A headless browser that opens Wiley's home page
first gets `pdfdirect` PDFs of articles Wiley serves free.

| Year | First author | Title / venue | DOI | Settles | Tried |
|---|---|---|---|---|---|
| 2001 | P. Cabras | rain wash-off of fungicides from grape leaves | 10.1081/PFC-100106189 | E6 wash-off per mm | T&F refuses; no repository copy |
| 2005 | S. Dalla Marta | SWEB on grapevine | 10.1016/j.agrformet.2005.07.003 | SWEB's canopy terms | Florence repository copy restricted (request-a-copy form) |
| 1971 | J. J. Landsberg & G. B. James | J. Appl. Ecol. (wind in plant canopies) | 10.2307/2402680 | SWEB Eq 15's source | JSTOR |
| 1996 | T. Watanabe & K. Mizutani | Agric. For. Meteorol. | 10.1016/0168-1923(95)02301-1 | Kuwagata's k_L | Elsevier |
| 2013 | P. Lauret | Renewable Energy | 10.1016/j.renene.2012.01.049 | the BRL's units | Elsevier; Wayback captures are of the HTML page |
| 2023 | Yang | Plant Pathology (latent qPCR in commercial vineyards) | 10.1111/ppa.13808 | qPCR detection lead time | Wiley, not free |
| 2016 | C. Malings & M. Pozzi | Reliab. Eng. Syst. Saf. | 10.1016/j.ress.2016.05.010 | spatial value-of-information placement | Elsevier |
| 2025 | Mendes | SSRN 10.2139/ssrn.5429516 (spring rain, downy mildew and yield in France) | 10.2139/ssrn.5429516 | yield loss | SSRN refuses; no journal version found |
| 2021 | Asadi & Tian | Agric. For. Meteorol. | 10.1016/j.agrformet.2021.108548 | wet hours from reanalysis | Elsevier |
| 1993 | Nair & Allen | Mycol. Res. | 10.1016/s0953-7562(09)80871-x | Botrytis infection by time and temperature | Elsevier |
| 1999 | R. D. Magarey | PhD thesis, Cornell | none | SWEB's Wd, Wf, p | eCommons and ProQuest: not found open |
| 1997 | E. Giralt | Míldiu: 1960-1995: la primera xarxa d'avisos antimíldiu de l'Estat espanyol (ICEA) | none | Penedès first oil spots, 1961-1995 | printed volume only |
| 1967 | J. Ticó | Un servicio de avisos contra el mildiu de la viña | none | the Penedès network's first years | not online |

