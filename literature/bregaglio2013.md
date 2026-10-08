---
id: bregaglio2013
citation: Bregaglio, Simone, Donatelli, Marcello & Confalonieri, Roberto. 2013. Fungal infections of rice, wheat, and grape in Europe in 2030–2050. Agronomy for Sustainable Development 33(4):767-776
doi: 10.1007/s13593-013-0149-6
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 26 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [downy mildew, Botrytis bunch rot, rice blast, wheat rusts]
crops: [grapevine, rice, wheat]
regions: [Europe]
processes: [infection]
records: [magarey2005.generic]
datasets: []
files: [10-1007-s13593-013-0149-6.pdf]
---

# Bregaglio, Donatelli & Confalonieri 2013: fungal infections in Europe, 2030-2050

From the University of Milan and CRA Bologna. A climate-impact study that runs Magarey et al. 2005's generic infection model for six pathogens, grape downy mildew and Botrytis among them.

## What it holds

- Runs Magarey et al. 2005's generic infection model on a European grid for six pathogens (l. 164).
- The temperature response is the Yan and Hunt 1999 function (l. 173), hourly (l. 170).
- Infection needs a wet period between WDmin and WDmax, scaled by f(T); two wet periods merge if the dry gap is under D50 (l. 200).
- P. viticola, Table 1: Tmin 1, Topt 20, Tmax 30 deg C; WDmin 2 h, WDmax 14 h, D50 6 h (l. 304). Its only source is Magarey et al. (2005) (l. 305).
- No calibration; averages of literature values where several exist (l. 220).
- Data collected: none. Weather is bias-corrected ENSEMBLES, A1B, baseline 1993-2007 (l. 164); leaf wetness is estimated with Kim et al. 2002 (l. 198).
- A climate-impact study with no validation against disease observations.
- Dependence: computes Magarey 2005 and Yan-Hunt; its P. viticola numbers are Magarey's, so it adds no independent evidence for them.

## Dependence

- **It computes Magarey et al. 2005's model** (a borrowed equation) with Magarey's own P. viticola and Botrytis rows (its Table 1), so it also shares those rows' data: Lalancette, Ellis & Madden 1988 and Nair & Allen 1993 (Formularium datasets `lalancette1988a`, `nair1993`).
- Wetness from Kim et al. 2002 (CART); no data of its own.

## Bearing (2026-10-08)

- **Kin by a borrowed equation**, as before, and now for that reason rather than its authors (Agrarium's candidates). Its P. viticola numbers are Magarey's, so it adds no independent evidence for them.
