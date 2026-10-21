---
id: kochendorfer2020
citation: Kochendorfer, J., Earle, M. E., Hodyss, D., Reverdin, A., Roulet, Y.-A., Nitu, R., Rasmussen, R., Landolt, S., Buisán, S. & Laine, T. 2020. Undercatch Adjustments for Tipping-Bucket Gauge Measurements of Solid Precipitation. Journal of Hydrometeorology 21:1193- (last page not verified)
doi: 10.1175/JHM-D-19-0256.1
read: 2026-10-21, lightly: abstract, Introduction (liquid and wind passages), Section 2 (gauges, reference, methods; Tables 1-2), Section 3 (adjustment, Eq. 2, Table 3), Section 4; solid-precipitation results read for wind only; by a reading agent (claude-haiku-5-5) and a note writer (claude-sonnet-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: []
crops: []
regions: [Canada, United States, Finland, Switzerland, Spain]
processes: [sensor error, tipping-bucket rain gauge, undercatch, wind, catch efficiency]
records: []
datasets: []
files: [kochendorfer2020.pdf (the 2026-10-21 drop)]
---

# Kochendorfer et al. 2020: wind undercatch of heated tipping-bucket gauges in solid and mixed precipitation

Catch efficiency of heated tipping-bucket gauges against a double-fence reference at five WMO-SPICE sites, with a wind-based adjustment. Liquid rain is excluded. No record.

**Read this first.** Two unchecked garbles in the text layer. Equation (2) (PDF page 5, l. 280) prints its exponent as "e2b(U)": the minus sign is lost and is read as CE = a exp(-bU). Table 3 (l. 634-648) is one scrambled block, so which of its numbers belong to the mixed and which to the solid fit is inferred; its coefficients are not copied here. Only winter solid and mixed precipitation were evaluated, so the function does not describe rain.

## What it holds

- **Sites and gauges** (l. 38, 148-149, 233, 260-268): five sites (CARE Canada, Marshall USA, Sodankyla Finland, Weissfluhjoch Switzerland, Formigal Spain), winters 2013/14 and 2014/15; heated tipping-bucket gauges CAE PMB25R (0.1 mm), Meteoservis MR3H-FC (0.1 mm) and Thies Precipitation Transmitter (0.1 or 0.2 mm), among others. A tip reports only after 0.1 to 0.2 mm has collected (l. 110).
- **Reference** (l. 210-214): double-fence automated reference with a Geonor T-200B3 weighing gauge.
- **Adjustment** (Eq. 1-2, PDF page 5; l. 280-294): catch efficiency CE = gauge / reference, fitted as an exponential decline with wind speed, separately for mixed and for solid precipitation, with a gauge-height wind and a 10 m wind form and a maximum valid wind (Table 3, unchecked). Zero-wind observations excluded (l. 227).
- **Liquid precipitation excluded** (l. 433-438): no rain undercatch result. Background only, cited: tipping-bucket gauges under-read liquid at high rates and in high wind (l. 115, Duchon et al. 2014; Buisan 2017).
- **Not printed:** prices; any RH or wet-surface test; a failure or data-loss rate beyond removing frozen-anemometer periods (l. 224-227).

## Dependence

- Builds on the transfer-function method of Kochendorfer et al. 2017a,b (l. 282-283) and the Spanish network work of Buisan et al. 2017; weighing-gauge functions of Wolff et al. 2015 and the high-rate correction of Lanza & Stagi 2012 are cited. The authors say the wind shield, not the gauge model, sets undercatch for weighing gauges (l. 344).

## Bearing (2026-10-21)

Sensor menu of D48 and its observation operators.

- **Error model supported:** the form of a wind-dependent rain-gauge undercatch (catch efficiency falling exponentially with wind) and the point that a tipping bucket has a 0.1 to 0.2 mm tip resolution. For a vineyard the numbers do not carry over: they are for winter snow and mixed precipitation under shields, and the sign and coefficients are unchecked.
- **Not measured:** liquid-rain undercatch, behaviour above 90 %RH or when wet, drift, data loss, packet delivery, price.
- **Kind of result:** a multi-site field comparison against a reference gauge, with a fitted adjustment; winter, high latitude and altitude sites.
