---
id: hirschi2012
citation: Hirschi, M., Stoeckli, S., Dubrovsky, M., Spirig, C., Calanca, P., Rotach, M. W., Fischer, A. M., Duffy, B. & Samietz, J. 2012. Downscaling climate change scenarios for apple pest and disease modeling in Switzerland. Earth System Dynamics 3:33-47
doi: 10.5194/esd-3-33-2012
read: 2026-10-27, lightly: abstract, sections 2.1-2.4 (downscaling, fire blight and leaf wetness, validation design), 3 (direct and indirect validation of fire blight) and the discussion of the humidity threshold; the codling moth parts not read, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 18 of 18 quotes found at their lines by scripts/verify_quotes.py; the text is two-column and interleaved
status: read
diseases: [fire blight]
crops: [apple]
regions: [Switzerland]
processes: [weather generator, k-nearest-neighbour resampling, hourly disaggregation, climate change scenario, ENSEMBLES, indirect validation, leaf wetness RH threshold, infection-day model]
records: []
datasets: []
files: [syn1027_hirschi2012.pdf (the 2026-10-27 drop)]
---

# Hirschi et al. 2012: a daily weather generator plus resampled observed hourly days, tested through a fire blight infection-day model

A stochastic daily generator (M&Rfi) combined with k-nearest-neighbour resampling of observed hourly days makes 100 years of synthetic hourly weather per Swiss station and period, to run apple pest and disease models under ENSEMBLES climate-change signals. No record: a method; the dataset is MeteoSwiss station data, not published here.

**Read this first.** The one end-to-end check in this strand of a disease model on synthetic weather against the same model on observed weather, but with caveats that limit it: one station, a rare-event count (about 60 % of years have zero infection days, l. 350), a leaf-wetness rule that is an RH threshold of 77 % and not 90 % (l. 320), and hourly RH that is copied from an observed day (l. 249), not generated. The reading agent did not name the model; the text names it as Maryblyt (l. 273).

## What it holds

- **Generator** (l. 36, 205-253): step 1, M&Rfi, a Richardson-type generator (Markov chain for rain occurrence, gamma amounts, an autoregressive model for the rest), makes daily precipitation, solar radiation and temperature (mean and range) only (l. 218): no daily humidity. Calibrated per station on daily observations, 1981-2009 (l. 229-231). Step 2 resamples: for each synthetic day, the 10 most similar observed days within +/-10 days (Mahalanobis distance on precipitation, temperature, range and radiation) are found and one is drawn at random (l. 228-235); precipitation and radiation are then rescaled and temperature shifted to match the generated day.
- **Humidity** (l. 249): "relative humidity from the same chosen observation day was added to the hourly output". So the diurnal RH shape is observed, chosen by similarity in the four daily variables; RH is not generated and no humidity statistic is fitted.
- **Scenarios** (l. 155-163, 1190-1198): ENSEMBLES RCM signals change temperature and precipitation (frequency, intensity, dry-to-wet transition) only; RH and radiation changes were left out as too uncertain, which the authors call a "conservative assumption". Ten stations (l. 206); 100 years of synthetic weather per case (l. 222); periods 1980-2009 and 2045-2074 (l. 36-38).
- **Fire blight model** (l. 273-285): the infection-day rule of Maryblyt: open blossoms; 110 cumulative degree-hours above 18.3 degC within the last 44.4 cumulative degree-days above 4.4 degC; daily mean temperature above 15.6 degC; a day with leaf wetness over 2 h or rain over 0.25 mm; and an assumed inoculum. Leaf wetness is hours with RH above 77 % (l. 316-321), an intermediate value from the literature. Bloom is a temperature-sum model for 'Golden Delicious'.
- **Direct validation** (l. 316-325): at Waedenswil, 29 years of observations (1981-2009) against 100 years of synthetic weather; seasonal and daily cycles of temperature, precipitation and solar radiation, split by dry and wet days. "Good agreement"; other stations similar. Humidity is not in that list.
- **Indirect validation, the end-to-end check** (l. 339-360): the disease model is driven by synthetic weather and its output compared with the output of the same model driven by observed weather, at Waedenswil. About 60 % of years have no infection days and the rest 1 to 7 (l. 350). Wilcoxon-Mann-Whitney, Kolmogorov-Smirnov and binomial tests find no significant difference between the two (l. 353). RH thresholds from 71 % to 87 % changed the agreement little (l. 359). The authors say this test also checks the generator on precipitation and humidity (l. 359-360).
- **Humidity statistics checked:** none directly. Indirectly, the count of infection days per year, which depends on hours with RH above 77 % but not at or above 90 %. No hours-per-year count, dew point, daily RH cycle or monthly mean is reported.
- **Authors' own caution** (l. 37, 1183): the projected change in infection days is "less certain" because of the leaf-wetness approximation and the bloom simulation.
- **Power of the test** (arithmetic, not printed): with 29 observed years (l. 317) and about 40 % of them having infection days (l. 350), only about a dozen observed years carry information, so a non-significant test is weak evidence of agreement.

## Dependence

- Builds on the Maryblyt model (Steiner 1990; Steiner and Lightner 1996; Duffy et al. 2008), the generator M&Rfi (Dubrovsky et al. 2004) with the resampling tool HOWGH (Dubrovsky et al. 2011, not seen), ENSEMBLES RCM output, and RH-threshold leaf wetness after Van Jaarsveld 2004 and Wichink Kruit et al. 2008 (as cited). The codling moth model SOPRA is not used here. Shared author Dubrovsky is the generator's author (a flag).

## Bearing (2026-10-27)

- **D45:** the nearest thing to a check on humid hours through a disease model, but not one: threshold 77 %, one station, a rare-event count, RH taken from observed days so that the humid-hour statistics are not generated. It supports "no generator checked at or above 90 % RH", with this as a near miss.
- **D60:** the design is the one to copy: run the disease engine on the generator's output and on observed weather and compare infection counts. Resampling observed hourly days keeps real RH shapes but can only reproduce what the station has seen; a generator calibrated from reanalysis cannot copy RH from station days.
- **Not shown:** that the daily RH or the wet-spell lengths of the synthetic weather are right; any test at 90 %; any vineyard disease.
