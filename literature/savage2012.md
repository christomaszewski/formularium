---
id: savage2012
citation: Savage, M.J. 2012. Estimation of leaf wetness duration for a short-grass surface. South African Journal of Plant and Soil 29(3-4):183-189
doi: 10.1080/02571862.2012.750017
read: 2026-10-27, in full (the first page is the publisher's cover sheet); Tables 2 and 3 read in the text, figures not read; by a reading agent and note writer (claude-sonnet-5-5); 14 of 14 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: [short grass]
regions: [South Africa, KwaZulu-Natal]
processes: [leaf wetness, leaf wetness duration, dielectric sensor, RH threshold, dew point depression, infrared thermometer, grass temperature]
records: []
datasets: []
files: [dr1027_savage2012.pdf (the 2026-10-27 inputs-d60 drop, from Chris)]
---

# Savage 2012: five ways to get daily leaf wetness over short grass, two RH rules among them

Dielectric sensors at 0.1 m are compared with two RH rules and two surface-temperature-against-dew-point rules over one winter month at Pietermaritzburg.

**Read this first.** One station, one month of comparison (31 days, 2011-08-20 to 2011-09-20), grass, winter. The sensors are not the reference in Table 3: the other methods are regressed on the infrared thermometer. The RH methods are compared with the sensors only through the Table 2 totals. The text mentions Penman-Monteith but prints no energy balance equation or coefficient. The paper is publisher copyright (All rights reserved), so no data or code is released.

## What it holds

- **Site and period:** Pietermaritzburg, KwaZulu-Natal, 684 m, 29.628 S 30.403 E, short grass; winters of 2011 and 2012, 2011-04-19 to 2012-06-15 (l. 143-145). Daily comparison covers 2011-08-20 to 2011-09-20 (Table 2).
- **Reference sensors:** three Decagon dielectric leaf wetness sensors (LWS), co-located at 45 degrees to the horizontal with their centres 100 mm above the soil (l. 138-139); Table 1 places the LWS, RH and air temperature at 0.1 m (l. 161). Wet at 284 mV or more, dry below 274 mV (l. 146-148); 2-min averages of ten 12-s readings (l. 144-145). No field calibration was needed.
- **Other sensors:** RH and air temperature at 2 m; grass thermocouple 25-50 mm above the canopy; infrared thermometer at 45 degrees facing south, 2.5 m up in the text and 2.6 m in Table 1, target 1.9 m across (l. 125-126, l. 162); net radiometer at 3 m (Table 1).
- **RH methods:** constant RH, wet above 87 %; extended, 70-87 % counts as wet if RH rose by more than 3 % in 30 min (l. 63-65), after Wichink Kruit et al. 2004. Dew point depression methods compare IRT or grass temperature with the dew point at 0.1 or 2 m. No printed coefficients beyond these thresholds.
- **Result in words:** the two RH methods gave the largest LWD of the five methods (l. 450); IRT and grass methods agreed reasonably without rain days but not with the sensors (l. 67-68).
- **Table 2, daily totals over 31 days (h):** sensors 165.1, 175.9, 193.0 (mean 178.0); IRT 143.6; grass 81.3; RH 258.9; RH extended 305.2 (l. 512). Without the rain days: sensors mean 142.1; IRT 139.9; grass 78.0; RH 193.3; RH extended 231.3 (l. 513). So the 87 % rule is 45 % above the sensor mean with rain days and 36 % above without; the extended rule is 71 % and 63 % above (arithmetic, not printed).
- **Table 3 (rain days excluded):** regressed on the IRT result, daily LWD RMSE against IRT is 3.406 h for the sensors, 1.761 h for grass temperature, 3.674 h for RH and 3.672 h for extended RH (l. 537).
- **Cited from Sentelhas et al. 2004:** sensors 300 mm above turfgrass at 15-45 degrees gave much better crop LWD than screen-height exposure (l. 97). Penman-Monteith is named as a reference index (Sentelhas et al. 2006, l. 82).

## Dependence

- RH methods are Wichink Kruit et al. 2004 and Sentelhas et al. 2008 (sentelhas2008); same extended RH rule as in gillespie2021. Sensor exposure follows Sentelhas et al. 2004 (sentelhas2004).
- Shares the RH-threshold form with sentelhas2008.wetness and cooptera.rh90_wetness. The dew point depression rules use measured surface or grass temperature, not a station input.

## Bearing (2026-10-27)

- **RH threshold error:** over short grass in a South African winter, a constant RH > 87 % rule gave 259 h of wetness in 31 days against 178 h from the sensors (45 % over); excluding rain days, 193 h against 142 h (36 % over). Kind of result: a measurement at one site over one month with three sensors that agree; no re-fit and no error in hours per day is given.
- **Sensor placement:** the sensors are at 0.1 m over grass, at 45 degrees; the paper's point is that wetness is a surface effect and screen-height RH overestimates it. This is not a vine canopy.
- **Not shown:** vines, summer, a fitted model, or any Penman-Monteith result.
