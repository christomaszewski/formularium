---
id: murakami2024
citation: "Murakami, K., Nemoto, M. & Yamazaki, T. 2025. Should leaves be removed on the east or the west? Diurnal patterns of cluster-zone microclimate and leaf photosynthesis in hedgerow grapevines during an extraordinarily hot summer in Hokkaido in 2023. Journal of Agricultural Meteorology 81(1):2-11 (accepted 21 June 2024)"
doi: 10.2480/agrmet.D-24-00016
read: "2026-10-25, lightly: the Discussion on wind, read closely, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [Japan, Hokkaido]
processes: [canopy flow, wind, leaf removal, cluster-zone microclimate, cluster temperature, photosynthesis, hedgerow]
records: []
datasets: []
files: [dr1025_murakami2024.pdf (the 2026-10-25 drop)]
---

# Murakami et al. 2025: a Hokkaido leaf-removal study whose discussion quotes the wind ratios of two older papers

A cluster-zone microclimate and photosynthesis study in hedgerow grapevines; for this strand only its wind paragraph matters.

**Read this first.** The wind numbers (half, three to four times, one tenth) are the authors' summary of Hunter et al. 2016 and English et al. 1989, plus the authors' own inference. They were not measured here. Use `hunter2016` and `english1989` for the sources. The paper is dated 2025 (volume 81); the id keeps the year the key gave, 2024.

## What it holds

- **Cited from Hunter et al. 2016 (named at l. 381):** the wind at the middle of the vine canopy was approximately half that measured 1 m above the canopy (l. 382-383). The site and the row direction are not given in this paper.
- **Cited from English et al. 1989:** the wind near clusters rose three to four times with leaf removal on both sides of the canopy (l. 386). This matches `english1989` (checked at source in that note).
- **Authors' inference, not a measurement:** combining the two, the wind near clusters in a vine canopy without leaf removal should be about one tenth of that outside the canopy (l. 389). The working is not printed.
- **Their own observation:** at about 15:00 on 19 August (2023), wind above 4 m/s reduced the temperature differences between leaf-removal and control treatments (l. 377); lower wind on 23 August widened them.

## Dependence

The wind paragraph rests entirely on `hunter2016` (abstract only in this strand) and `english1989`.

## Bearing (2026-10-25)

- **Mid-canopy to open wind (SWEB Eq 15):** a second-hand 0.5 (mid-canopy against 1 m above the canopy, Shiraz on a vertical trellis) sits in the range of the measured ratios in this strand. The reference is 1 m above the canopy, not twice its height, so it does not compare directly with SWEB's U_Z. The one-tenth is a cluster-zone inference.
- **micro.evap_wind_per_ms:** nothing on drying. Only that strong wind (above 4 m/s) cuts cluster temperature differences, a heat-transfer statement.
- Kind of result: citation and inference in a discussion section.
