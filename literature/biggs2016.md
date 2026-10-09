---
id: biggs2016
citation: Biggs, Trent W., Petropoulos, George P., Velpuri, Naga Manohar, Marshall, Michael, Glenn, Edward P., Nagler, Pamela & Messina, Alex. 2016. Remote sensing of actual evapotranspiration from croplands. In Thenkabail, P. S. (ed.), Remote Sensing Handbook, vol. III: Remote Sensing of Water Resources, Disasters, and Urban Studies, chapter 3, pp. 59 ff. CRC Press (© 2016; version date 2015-05-13)
doi:
read: 2026-10-08, the chapter in full, the citation from the volume's contents and copyright page, by a reading agent (claude-sonnet-5-5); 31 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: []
crops: []
regions: [global]
processes: [evapotranspiration]
records: []
datasets: []
files: []
---

# Biggs et al. 2016: remote sensing of actual evapotranspiration from croplands (handbook chapter)

Chapter 3 of the Remote Sensing Handbook's volume III. The only part of the three-volume handbook ingested: the rest is paused (Chris, 2026-10-08), so this note names no file, and `coverage.py` still lists the handbook as unnoted.

## What it holds

- Review chapter of satellite ET methods for croplands (Biggs and six co-authors, Remote Sensing Handbook vol. III, ed. Thenkabail, CRC Press; book p. 59). It reports no new data; error figures are quoted from other papers.
- Three families: vegetation-index, radiometric-temperature, and scatterplot (l. 150).
- Quoted errors against towers: empirical crop-coefficient methods 10-30% RMSD (l. 185); PT-JPL 13% annual (l. 845); MOD16 RMSE about 20% (l. 206) but 72-76% at two irrigated sites (l. 919); SEBAL/METRIC 15-20% daily, about 5% seasonal (l. 217); ALEXI MAD 10% daily (l. 239); SSEB under 30% (l. 243); scatterplot methods about 30% (l. 259).
- Overall 10-30% monthly, 5-10% seasonal (l. 2000). Eddy-covariance references carry 15-30% error (l. 2018).
- Wet canopy appears only as model terms: PT-JPL f_wet = RH^4 and lE_I (l. 800, l. 487); MOD16 F_wet = 0 below RH 70% (l. 854). Dew is mentioned once (l. 1309). There is no wetness validation.
- Vineyards: only Campos et al. 2010, NDVI regression in Spanish grapes, no error given (l. 775).
- Many equations are cited, not derived. Alpha_PT is 1.26 (l. 677).

## Dependence

- A review: every error figure is quoted from other papers. Its ALEXI figures rest on the same Iowa SMEX02 data as [anderson2007](anderson2007.md).
- No author of an engine model.

## Bearing (2026-10-08)

- Clear, and of indirect use: the error ranges of satellite ET by family (10-30% monthly, 5-10% seasonal) for a satellite ET operator. Nothing on leaf wetness beyond model terms, and one vineyard study cited without an error.
