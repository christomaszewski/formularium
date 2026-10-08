---
id: moral2012inoculum
citation: Moral, Juan & Trapero, Antonio. 2012. Mummified Fruit as a Source of Inoculum and Disease Dynamics of Olive Anthracnose Caused by Colletotrichum spp. Phytopathology 102(10):982-989
doi: 10.1094/PHYTO-12-11-0344
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 28 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [olive anthracnose]
crops: [olive]
regions: [Andalusia]
processes: [sporulation, epidemic progress]
records: [magarey2005.generic]
datasets: []
files: [10-1094-phyto-12-11-0344.pdf]
---

# Moral & Trapero 2012: mummified olives as inoculum, and anthracnose epidemics

From the Universidad de Córdoba. Olive, not grape; read for its use of Yin's temperature function.

## What it holds

- Laboratory and field study of olive anthracnose sporulation and epidemics in Cordoba, Spain. Not grape.
- Temperature trial: mummified fruit at 5 to 35 deg C, 72 h; peak near 20 deg C (l. 200). Wetness trial: 0 to 168 h at 23 deg C (l. 108). Own data, none dated by a model.
- Conidial production Y(T) = f(T) x CPmax (Eq. 1, l. 84), the structure of Magarey et al. 2005 (l. 81) used for sporulation.
- f(T) is Yin's function (l. 86): f(T) = (2.6923 - T/13) (T/22)^1.6923 (Eq. 5, l. 208), with Tmin 0, Topt 22, Tmax 35 deg C (l. 205).
- Cardinal temperatures come from these data and from mycelial growth in culture (a thesis and a 1960 paper), set not fitted; R2 0.866 (l. 212).
- Wetness: linear, Y = 2.1592 + 0.0859 X, 0 to 96 h (l. 223).
- Washing: Y = 10.1751 - 3.2098 x 0.5923^X (l. 214), journal page 985.
- Field epidemics: Weibull Y = A(1 - exp{-[B(t - C)]^D}) on 18 trees over 2005-08 (l. 161); descriptive, parameters in Table 1.

## Dependence

- **It computes Yin's temperature function** (eq. 5, l. 208; ref 34, l. 86), the f(T) inside Magarey et al. 2005's model, in Magarey's structure Y = f(T)·maximum (l. 81), applied to sporulation. Its cardinal temperatures (0, 22, 35 °C) were set from its own data and mycelial growth in culture, not fitted.
- The engine computes the same f(T) inside `magarey2005.generic`, so the candidate records a borrowed equation (Agrarium's candidates), though only the temperature function is shared.

## Bearing (2026-10-08)

- **Kin through the temperature function it shares with Magarey's model**; another host either way. Its Weibull epidemic fits (18 trees, 2005-2008) are descriptive.
