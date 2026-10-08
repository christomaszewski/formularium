---
id: moral2012infection
citation: Moral, Juan, Jurado-Bello, José, Sánchez, M. Isabel, de Oliveira, Rodrígues & Trapero, Antonio. 2012. Effect of temperature, wetness duration, and planting density on olive anthracnose caused by Colletotrichum spp. Phytopathology 102:974-981
doi: 10.1094/PHYTO-12-11-0343
read: 2026-10-08, in full, by a reading agent (claude-sonnet-5-5); 30 quotes checked by scripts/verify_quotes.py, dependence by the main session
status: read
diseases: [olive anthracnose]
crops: [olive]
regions: [Andalusia]
processes: [infection, latent period]
records: [magarey2005.generic]
datasets: []
files: [10-1094-phyto-12-11-0343.pdf]
---

# Moral et al. 2012: olive anthracnose by temperature, wetness and planting density

From the Universidad de Córdoba (with the Universidade Agostinho Neto, Huambo). Olive, not grape; read for its infection forms.

## What it holds

- Lab and field study of olive anthracnose (Colletotrichum acutatum, C. simmondsii) in Cordoba, Spain. Not grape.
- Own data: detached fruit at 5 to 35 deg C (l. 76); plants and cuttings at 0 to 48 h wetness (l. 141); field fruit counts at four planting densities, 2003-2004 (l. 189). No model dated any of it.
- Temperature fits use the Analytis beta model, Y = k t^a (1-t)^b, Table 1; fitted Topt 15.6 to 24.1 deg C. Tmin and Tmax are not printed there.
- Builds an infection model by Magarey et al. 2005 (l. 185): W(T) = Wmin / f(T) up to Wmax (Eq. 3, l. 194). Eq. 4 for f(T) is lost in the extraction. The f(T) property is cited to Yin et al. 1995.
- Parameters: Tmin 10, Topt 20.4, Tmax 25 deg C (l. 285). Wmin 1.0 h at 5% affected fruit and 12.2 h at 20% (l. 288).
- Tmin and Tmax follow the range where fruit were infected (10 to 25 deg C, l. 247). Topt equals one Analytis fit.
- Methods print the thresholds as 10 and 20% (l. 213); elsewhere 5 and 20%.
- Field support is only 'preliminary data' (l. 390).

## Dependence

- **It computes Magarey et al. 2005's infection model** (its eq. 3, W(T) = Wmin/f(T) up to Wmax, l. 185-194): a borrowed equation, kin to the engine's Magarey and Brischetto pieces. Its own parameters (Tmin 10, Topt 20.4, Tmax 25 °C; Wmin 1.0 h at 5% and 12.2 h at 20%; l. 285-288) were fitted to its own fruit data.
- Its temperature fits use the Analytis beta (Hau & Kranz 1990), the form Agrarium's D33 asks about.
- Its fourth author's name prints as "Rodrígues de Oliveira"; the split of given name and surname is a guess.

## Bearing (2026-10-08)

- **Kin by a borrowed equation** (Magarey's), for another host. A worked example of Magarey's model refitted to new data; nothing for the grape truth.
