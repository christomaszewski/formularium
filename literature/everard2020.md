---
id: everard2020
citation: Everard, K.A., Oldroyd, H.J. & Christen, A. 2020. Turbulent heat and momentum exchange in nocturnal drainage flow through a sloped vineyard. Boundary-Layer Meteorology 175:1-23
doi: 10.1007/s10546-019-00491-y
read: "2026-10-25, lightly: site, profile results and discussion; Fig. 4b read off the page image, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 7 of 7 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [grapevine]
regions: [Canada, British Columbia, Okanagan]
processes: [canopy flow, wind, nocturnal drainage flow, momentum flux, wind profile, canopy turbulence]
records: []
datasets: []
files: [dr1025_everard2020.pdf (the 2026-10-25 drop)]
---

# Everard et al. 2020: night-time wind in a sloped Okanagan vineyard is nearly constant inside the leaf layer

Five sonic anemometers on one mast in a row-gap trellised vineyard, during drainage flow on 211 summer nights.

**Read this first.** The wind ratios below are read by eye from a box plot (Fig. 4b), so they are approximate, not printed. They hold only for nocturnal drainage flow on a 7 degree slope, where a jet maximum lies near the top of the profile, and the row direction against the flow is not stated in the lines read.

## What it holds

- **Site:** the Black Sage-Osoyoos vineyard in the southern Okanagan, on a 7 degree slope; canopy height h_c 2.3 m, with leaf area from 0.9 m up to 2.3 m (l. 259); rows 3 m apart, drip irrigated (l. 261).
- **Instruments and sample:** five CSAT3 sonic anemometers at 0.45, 0.9, 1.49, 2.34 and 4.73 m on one mast (l. 264), 4 to 22 July 2016; 211 five-minute night cases of drainage flow, about 17% of the nocturnal conditions (l. 21; l. 727).
- **Profile:** wind speed increases with height, with a weak inflection point near the canopy top and a jet maximum between z/h_c = 1.02 and 2.34 (l. 701-702).
- **No attenuation in the leaf layer:** there is no significant vertical gradient in wind speed between z/h_c = 0.39 and 0.65 (l. 705). This is not an exponential decay into the canopy.
- **Fig. 4b (approximate, from a box plot):** median wind speed divided by that at canopy top is about 0.55 at z/h_c 0.2, 0.7 at 0.39 and 0.65, 1.0 at 1.02 and 1.25 at 2.06 (l. 728). So mid-canopy wind is about 0.7 of the canopy-top wind, and about 0.56 of the wind at 2.06 h_c (arithmetic, not printed: 0.7 / 1.25).
- **Cited from Miller et al. 2017:** a row-gap trellised canopy behaves as dense or sparse depending on the approaching wind angle relative to the rows (l. 141).

## Dependence

None recorded. The dense-or-sparse statement is cited from `miller2017`.

## Bearing (2026-10-25)

- **Mid-canopy to open wind and SWEB Eq 15:** at night, in a 2.3 m canopy, mid-canopy wind is about 0.7 of canopy top and about 0.56 of the wind at twice the canopy height. That is higher than the 0.3 U_Z found by trial for SWEB. The reference heights differ (2.06 h_c here; SWEB's Z over a 150 cm canopy) and the wind at 2.06 h_c sits near a jet maximum, so the 0.56 is not a daytime vineyard value. Night values matter most for dew.
- One site, three weeks, drainage flow only; figure-read ratios. Kind of result: measurement (read off a figure).
- **dm.row_barrier:** only the cited Miller et al. statement; no direction-split result of its own.
