---
id: magarey2005
citation: Magarey, R. D., Sutton, T. B. & Thayer, C. L. 2005. A simple generic infection model for foliar fungal plant pathogens. Phytopathology 95:92-100
doi: 10.1094/PHYTO-95-0092
read: 2026-10-07, equations 1-2, the Wmax rule, Table 2's header and grape rows and refs 43 and 56, in place in the copy Cooptera holds (the Cooptera session read it; this session checked the same lines)
status: read
diseases: [many, downy mildew, botrytis]
crops: [many, grapevine]
regions: [general]
processes: [infection]
records: [magarey2005.generic]
datasets: [lalancette1988a, nair1993]
---

# Magarey, Sutton & Thayer 2005: a generic infection model

## What it holds

- **Eq. 1:** W(T) = Wmin / f(T) ≤ Wmax, the wetness an infection needs at mean temperature T.
- **Eq. 2:** f(T) = ((Tmax − T)/(Tmax − Topt))·((T − Tmin)/(Topt − Tmin))^((Topt − Tmin)/(Tmax − Topt))
  "if Tmin ≤ T ≤ Tmax and 0 otherwise": Yin et al.'s temperature response.
- **An unknown Wmax:** Wmax = 3.8 + 3.0·Wmin (r = 0.71, RMS 6.0 h, 64 studies).
- **Table 2, grape rows** (Tmin, Tmax, Topt °C; Wmin, Wmax h):
  - *P. viticola*: 1, 30, 20; 2, 14 (ref. 43, Lalancette, Ellis & Madden 1988);
  - *B. cinerea*, berries: 10, 35 (the paper's default where none was measured), 20; 4, 10
    (ref. 56, Nair & Allen 1993);
  - *B. cinerea*, flowers: 1, 34, 25; 1, 12 (ref. 56).
- The paper leaves open how the cap meets f(T) = 0.

## Dependence

- Cooptera runs this equation with Brischetto 2021's parameters, not Table 2's.
- Table 2's grape rows share data with Lalancette 1988 and Nair & Allen 1993: a truth fitted
  to those would share calibration data with nothing the engine runs, since the engine does
  not use Table 2.

## Bearing (2026-10-07)

- The source of Formularium's `equations.magarey2005`, now marked read.
- Supplies Nair & Allen 1993's Botrytis numbers, which the model survey had not seen: a
  Botrytis truth on them holds out only the engine's Magarey and Brischetto pieces, not
  Broome's index.
