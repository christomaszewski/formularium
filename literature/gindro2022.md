---
id: gindro2022
citation: Gindro, K., Schnee, S., Lecoultre, N., Michellod, E., Zufferey, V., Spring, J.-L., Viret, O. & Dubuis, P.-H. 2022. Development of downy mildew in grape bunches of susceptible and resistant cultivars: infection pathways and limited systemic spread. Australian Journal of Grape and Wine Research 28:572-580
doi: 10.1111/ajgw.12560
read: 2026-10-22, in full (all 9 journal pages; Table 1 and the inoculum line checked in the page image), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 90 of 90 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew]
crops: [grapevine]
regions: [Switzerland, Changins]
processes: [downy mildew, bunch infection, stomata, ontogenic resistance, inflorescence, rachis, pedicel, berry, histology, PCR]
records: []
datasets: []
files: [gd1021_gindro2022.pdf (the 2026-10-22 drop)]
---

# Gindro et al. 2022: downy mildew enters bunches through stomata and spreads only to adjacent tissue

Tunnel inoculations of Chasselas (susceptible) and Divico (resistant) bunches at four stages, followed by microscopy and PCR: where the pathogen enters, how far it spreads and when bunches stop being infected.

**Read this first.** Qualitative. The paper prints no infection percentages, no dose series, no leaf-against-bunch comparison and no per-sporangium probability, so it gives no value for `dm.bunch_efficiency` or `host.rachis_only_factor`, only stages, pathways and a window. One dose (10 mL of 4 x 10^5 sporangia per mL) was sprayed on each bunch (l. 114, 124). The text layer garbles the inoculum ("4  105"); the page image reads 4 x 10^5. Text and Table 1 disagree on when Divico BBCH 69 first showed symptoms: 19 dpi in the text (l. 212), 15 dpi in the table (l. 157). The date of the veraison (BBCH 81) inoculation is not tabulated.

## What it holds

- **Design:** Chasselas (susceptible Vitis vinifera) and Divico (Gamaret x Bronner, interspecific, resistant, with the RPV10 locus; l. 138, 486) in an experimental vineyard of Agroscope Changins under a transparent plastic roof and walls to keep out rain and natural infection (l. 71, 74). Ten bunches, two per plant, per cultivar at each of four stages: BBCH 55 (inflorescence swelling), 69 (end of flowering), 75 (pea size), 81 (veraison) (l. 20, 88, 94). Chasselas in 2014 (not shown) and 2016, Divico in 2016 (l. 144). Each bunch bagged 24 h after spraying (l. 128); detached Chasselas leaves got the same inoculum only to confirm it was infective (l. 134).
- **Dates** (Table 1, PDF p. 2, l. 149-157): Chasselas 2016 inoculated 17 May (BBCH 55), 27 June (BBCH 69) and 11 July (BBCH 75), so pea size is 14 days after the end of flowering; Divico 17 May, 20 June and 5 July, 15 days. First symptoms in Chasselas at 13 dpi (BBCH 55) and 14 dpi (BBCH 75), and at 8 dpi for BBCH 69 (l. 150-151).
- **Chasselas by stage:** BBCH 55, pathogen in the calyptra at 6 dpi (l. 221), shepherd's crook at 23 dpi, whole inflorescence colonised and necrotic at 39 dpi (l. 212); entire flower and rachis colonised at 23 dpi (l. 227). BBCH 69, slight symptoms (l. 215): small necrosis on the rachis tip and berries at 8 dpi (l. 217), infection through stomata of the calyx and receptacle and none on the berry itself at 8 dpi, whole berry colonised by 15 dpi (l. 231-233), branches desiccated by 43 dpi (l. 222) while other berries ripened normally (l. 22-23). BBCH 75, grey-green spots on sparse berries at 14 dpi, brown rot from 23 dpi, leather berries at 37 dpi (l. 224-226). BBCH 81, no symptoms or signs of infection (l. 24, 228, 249).
- **Window:** infection occurs from BBCH 55 until the onset of veraison, with symptoms weakening as the bunch develops (l. 312-314); natural field infection can be seen until shortly before veraison (l. 53, no source given). Earlier detached-bunch work (Gindro et al. 2012) found infection at BBCH 55 only (l. 48-50, cited); the attached-bunch result here differs.
- **Pathway:** an active stoma is needed (l. 25). Stomata are on the calyptra, calyx, receptacle, pedicel and rachis (l. 355); the grown berry has none that work, so it is colonised from the pedicel and receptacle (l. 412, 422); functional stomata become lenticels (Kennelly et al. 2005, cited; l. 408). Later stages show more non-functioning stomata on receptacle, pedicel and rachis (l. 379-380). The authors read the falling infection rate as fewer entry sites and/or lower tissue receptivity (l. 412-414).
- **Rachis and pedicel:** both strongly infected at BBCH 55 except the vascular tissue (l. 359) and colonised at BBCH 69 except the steles (l. 238-239). At BBCH 75 only berries are reported; at BBCH 81 berries, pedicels and rachis showed nothing under a loupe, so there was no microscopy and no separate rachis result (l. 250). No rachis-only rate is given.
- **Spread:** only into adjacent tissue (l. 28, 385). It never went from the rachis into several berries or from the inflorescence into the shoot (l. 391-392), never into vascular tissue (l. 398); after BBCH 69 it stayed in single branches and after BBCH 75 in single berries, never the whole bunch (l. 394-396).
- **Divico:** infections rare (l. 449). BBCH 55: a few stomata of the calyptra, pedicel and rachis penetrated, no haustoria (l. 311-315); BBCH 69: a few berries with necrotic spots turned brown and fell (l. 215, 320); BBCH 75 and 81: no symptoms or infection (l. 217, 295). It is not immune (l. 484); up to three sprays between BBCH 57 and 75 are advised (l. 500). PCR agreed with microscopy (l. 255-256).

## Dependence

- **Borrows** its inoculation and PCR methods from Gindro et al. 2003 and 2014; the BBCH scale from Lorenz et al. 1995. Contrasts with Gindro et al. 2012 (detached bunches). Ontogenic-resistance statements cite Kennelly et al. 2005 (held, `kennelly2005`) and Fröbel and Zyprian 2019 (held, `frobel2019`).
- **Data:** its own; no dataset is listed. Shared authors with Gindro et al. 2012 (same Agroscope group): a flag.

## Bearing (2026-10-22)

- **`dm.bunch_efficiency` and `host.rachis_only_factor`:** nothing numerical. What the paper supports is the mechanism: entry only through functioning stomata of the calyptra, calyx, receptacle, pedicel and rachis; berries reached from adjacent tissue; no spread from one rachis lesion to several berries. That argues against a rachis infection infecting the whole bunch, but gives no factor.
- **Window:** in Chasselas under a tunnel with one heavy dose, berries still took infection 14 to 15 days after the end of flowering (BBCH 75), on only a few berries, and not at veraison; pedicel and rachis were infected at BBCH 55 and 69, with no result for them at BBCH 75. The end of susceptibility therefore lies between about 14 days after flowering and veraison, which is not dated. `kennelly2005` is the quantitative source by days after flowering.
- **Not shown:** infection rates, a dose response, any open-field bunch result. Kind of result: histology and PCR on 10 bunches per stage, one susceptible and one resistant cultivar, no statistics.
