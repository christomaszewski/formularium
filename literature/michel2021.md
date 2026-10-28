---
id: michel2021
citation: Michel, A., Sharma, V., Lehning, M. & Huwald, H. 2021. Climate change scenarios at hourly time-step over Switzerland from an enhanced temporal downscaling approach. International Journal of Climatology 41:3503-3522
doi: 10.1002/joc.7032
read: 2026-10-27, lightly: abstract, introduction, data description, the delta-change definition, the verification design and the discussion of limits (searched for humidity); the results sections and the snow case study skimmed, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 5 of 5 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Switzerland]
processes: [delta-change, temporal downscaling, hourly disaggregation, climate change scenario, quantile mapping, relative humidity, weather generator, harmonic smoothing]
records: []
datasets: []
files: [syn1027_michel2021.pdf (the 2026-10-27 drop)]
---

# Michel et al. 2021: hourly climate-change scenarios for Switzerland by delta-change on observed hourly series

Applies daily climate-change signals (CH2018) to historical hourly station series to give 68 scenarios at 188 stations. No record: a method and a data product, not a stochastic generator; the humidity structure is the observed one, rescaled.

**Read this first.** Only the data description, method definition, verification design and limits were read, not the results sections. The humid-hour count is not scored in what was read. Relative humidity (RH) is scaled multiplicatively, so it can exceed 100 % (l. 224-226, 1618).

## What it holds

- **Method** (l. 29, 216-226): daily scenarios (CH2018, EURO-CORDEX chains, quantile-mapped to stations) are applied to historical hourly series by a delta: additive for temperature, multiplicative for the other variables, smoothed by harmonic fitting (seven harmonics found best, l. 47). The authors note that multiplicative delta "might lead to unrealistically high values".
- **Product** (l. 52, 238-240): 68 climate-change scenarios at hourly resolution for 188 stations (MeteoSwiss and IMIS networks), five variables including RH. The paper says the source code and the data product are open access (repository and licence not read). 
- **Verification design** (l. 566-584): the 30-year period is split into ten blocks of 3 years; nine are used to fit the harmonics and the tenth is the check, repeated ten times, with RMSE of seasonal means. The checks read are on seasonal means (RMSE) and on the choice of harmonics; the parts read give no check of hourly distributions.
- **Stated limits** (l. 1618, 1629): scaled RH "can be superior to 1" and users "must apply appropriate filtering and correction... especially regarding upper bound values"; the sub-daily cycle is climate-change agnostic, being the historical one, which "should be considered as an additional source of uncertainty".
- **Generator test** (l. 1635-1683): for stationary series, 500 realisations of the AWE-GEN generator for Florence, Italy, 1980-2010, were smoothed over 10 and 30 years and seasonal means compared. This tests the smoothing, not the generator's humidity.
- **Humidity statistics checked:** seasonal means of RH only (in the verification design); no hours at or above 90 %, no dew point, no daily cycle.

## Dependence

- CH2018 scenarios (MeteoSwiss et al. 2018), EURO-CORDEX, MeteoSwiss and IMIS station data, the spatial transfer of Rajczak et al. 2016, and AWE-GEN (Fatichi et al. 2011) for the stationarity test. No shared-author flag with the other weather notes.

## Bearing (2026-10-27)

- **D45:** not a check on humid hours. It keeps observed hourly RH shapes, so humid hours are as real as the station series, but it cannot change their frequency except through the scaling, which can push RH past 100 %.
- **D60:** a delta-change on a real hourly record is the cheapest way to make a perturbed scenario that keeps humid-hour structure (compare the resampling of `hirschi2012`); it needs real hourly RH, so it does not fill a missing input. The upper-bound problem (RH above 100 %) applies to any multiplicative correction of hourly RH.
- **Not shown:** that scaled hourly RH keeps the right number of hours at or above 90 %; any disease model run on the product.
