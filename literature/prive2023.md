---
id: prive2023
citation: Privé, N.C., McGrath-Spangler, E.L., Carvalho, D., Karpowicz, B.M. & Moradi, I. 2023. Robustness of observing system simulation experiments. Tellus A 75(1):309-333
doi: 10.16993/tellusa.3254
read: 2026-10-27, lightly: abstract, the introduction (twin discussion), the validation sections 3.1 to 3.3 and the discussion of model error and impacts; the individual instrument impact maps skimmed, by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 21 of 21 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: []
processes: [OSSE, fraternal twin, OSSE validation, forecast sensitivity to observations, model error, nature run, data assimilation]
records: []
datasets: []
files: [syn1027_prive2023.pdf (the 2026-10-27 drop)]
---

# Privé et al. 2023: two versions of NASA's OSSE compared with the real system, and what a less-alike forecast model changes

Compares a 2015-era and a 2020-era version of the NASA GMAO OSSE, differing mainly in the forecast model's physics and dynamics, against the same data-assimilation system run on real observations, and shows how the predicted value of three proposed instruments changes. No record: a method with measured validation numbers.

**Read this first.** Atmosphere and weather forecasting, not plants. The numbers below are validation statistics of one OSSE family over July to September; Privé, Errico and McCarty 2021 and Privé and Errico 2013b, which this paper leans on, were not obtained. The paper's own data are too large to archive.

## What it holds

- **Insufficient model error** (l. 28, 836): a common problem is OSSEs having "insufficient model error compared to NWP in the real world"; it "affects every aspect of the OSSE, from the calibration of the simulated observations to the observation impacts" at medium range. Reduced OSSE impacts were deduced to come from insufficient error growth, which gives observations less work to do (l. 543).
- **Cited on twins** (l. 65-69, 70-73): Yu et al. 2019 found that the identical twin led to "overestimates of the impact of some" observations and "underestimates of other" impacts, and that a realistic model error growth rate "was not sufficient to yield accurate" impacts. Privé and Errico 2013b (cited) found forecast errors considerably lower in the identical twin but error growth rates "somewhat similar" in identical and fraternal twins.
- **The change tested** (l. 826): the updated OSSE "can still be considered a 'fraternal twin'", with convection, radiation and boundary-layer physics changed to reduce twinning; its forecasts should be worse than the previous OSSE's because the forecast model is less like the nature run (l. 881-886).
- **Analysis increments** (l. 825, 869-871): 20 % smaller than in the real system in the updated OSSE against 30 % smaller in the previous; the earlier ECMWF-nature-run OSSE had 5-20 % smaller (cited from Errico et al. 2013).
- **Bulk observation impact** (l. 890-893, forecast sensitivity to observation impact summed over all observations): about 60 % of the real system's in the previous OSSE, more than 70 % in the updated. Net impacts are closer to real, though some data types are still substantially lower (l. 548).
- **One instrument's impact flips sign** (l. 886): for the geostationary infrared sounder, southern-extratropical impact poleward of 35 degrees S reversed from detrimental in the previous OSSE to beneficial in the updated one.
- **Another changes by a fifth** (l. 928): MISTiC AMV analysis-error improvement 10-12 % in the updated OSSE against 8-10 % in the previous, with no change in how those observations were handled.
- **Season-specific calibration** (l. 856-857): October "showed considerably worse validation" than July to September, so another season would need recalibration of cloud contamination, AMV locations and simulated observation errors.
- **Conclusion** (l. 931-942): the effects are "modest" and the overall distribution and magnitude of impacts are similar in systems with different degrees of twinning; "a range of fraternal twin OSSEs should give robust experimental results, as long as the degree of twinning is well-understood".

## What TRUTH-METHOD says of it

Not cited in TRUTH-METHOD. It bears on part 3 (the gap should be about the size of the gap to reality). Verdict: **not in TRUTH-METHOD; new, and it adds measured limits.**
- Matching error growth is not enough (l. 67-73, cited): an identical twin had considerably lower errors but similar growth.
- A move to a less-alike model shifted bulk impact from about 60 % to more than 70 % of the real system's (l. 892-893) and flipped one instrument's regional impact (l. 886); the authors still call the overall result robust (l. 931-942).
- The direction is usually under-statement here (OSSE impact below the real system's), field by field.

## Dependence

- G5NR nature run (Gelaro et al. 2014), the GEOS/GSI assimilation system, Privé and Errico 2013a,b, Errico et al. 2013 and Privé et al. 2021 (all cited, none read except as slides in `errico2015ntrs`). Privé is an author of `errico2015ntrs`: a shared-author flag.

## Bearing (2026-10-27)

- **TRUTH-METHOD, part 3:** one matched quantity (error growth) did not make an OSSE accurate; the gap calibration should compare several outputs, and the report should show how an output changes when the truth family is swapped (here: increments, bulk impact, regional sign).
- **D60:** a synthetic outcome's value for a given instrument or input can change sign between two simulator versions (l. 886); treat a synthetic-only impact as a robustness test, never as establishing a feature.
- **Not shown:** an OSSE prediction later verified by the real instrument; any plant or disease case.
