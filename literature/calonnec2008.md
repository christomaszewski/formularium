---
id: calonnec2008
citation: Calonnec, A., Cartolaro, P., Naulin, J.-M., Bailey, D. & Langlais, M. 2008. A host-pathogen simulation model: powdery mildew of grapevine. Plant Pathology 57:493-508
doi: 10.1111/j.1365-3059.2007.01783.x
read: 2026-10-22, in full (two columns interleaved; Eqs 4 to 11 and Figure 1 checked in the page image of PDF p. 4), by a reading agent (claude-sonnet-5-5) and a note writer (claude-sonnet-5-5); 36 of 36 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [powdery mildew]
crops: [grapevine]
regions: [France, Bordeaux]
processes: [powdery mildew, epidemic simulation, infection, latent period, spore dispersal, ontogenic resistance, leaf growth]
records: []
datasets: []
files: [gd1021_calonnec2008.pdf (the 2026-10-22 drop)]
---

# Calonnec et al. 2008: a daily single-vine model of grapevine powdery mildew

A deterministic, daily simulation of Erysiphe necator on one Cabernet Sauvignon vine, with a parameter table (Table 1) that leaves the dispersal kernel's constants mostly unprinted.

**Read this first.** The dispersal kernel cannot be rebuilt from the paper: the decay constant cid = 0.04 is printed with no unit and no source, the cone angle theta has no value, and alpha and b of the spore-release Eq. 9 are credited to Willocquet et al. (1998) with no values (l. 412, 287, 408). Table 1's "range of value" column holds paired values joined by a dash (for example 1.055 to 0.338 is ng then mg; 874 to 0.314 is beta then delta; 18 to 2 is A then B). Decimal marks are middle dots. Fig. 3 (schematic) was not extracted. The model covers the leaf epidemic only: no damage function (l. 82, 737).

## What it holds

- **Scope:** one vine, one season, a daily step; spread restricted to the leaf population (l. 82). Leaves appear after a degree-day sum above 10 degC from 1 January (l. 184). Leaf susceptibility classes by age: s1 under 5 days (highly susceptible), s2 5 to 10 days, s3 10 to 20 days (low), s4 over 20 days (l. 354).
- **Temperature response** (Eq. 4, PDF p. 4, l. 254): F(Tn) = ((m+n)^(m+n) / (n^n m^m)) Tn^n (1 - Tn)^m, Tn = (T - Tmin) / (Tmax - Tmin), the Analytis form.
- **Infection** (Eq. 5, l. 264): I = I0 F(Tn) exp(-tau A), A the leaf age. Table 1 (PDF p. 7): I0 0.53 (l. 396); tau 0.147 (l. 397); infection shape ng, mg 1.055 and 0.338 (l. 398); cardinal temperatures Tmaxg 33 and Tming 5 degC, from Delp (1954) and Sall (1980) (l. 399). I0 F(Tn) is almost zero below 10 and above 30 degC, with a maximum near 22 degC (l. 269, cited). Units of I0 and tau are not printed.
- **Colony growth** (Eqs 6 and 7, l. 293): a logistic diameter step driven by F(Tn), with Kmax = (A - B) exp(-c age) + B. Table 1: n, m 1.24 and 0.27 (l. 400); Tmax 33 and Tmin 5 degC (l. 401); r 0.2 (l. 402); t* 13 day (l. 403); A 18 and B 2 mm (l. 404); c 0.08 (l. 405).
- **Latent period** (Eq. 8, l. 230): rho(T) = rho_min / F(Tn), complete when the sum of 1/rho over days reaches 1; rho_min 6 day (Blaise and Gessler 1992; Rumbolz 1999; l. 406).
- **Spore release and production:** Eq. 9 (page image): Qs = exp(alpha u + b) / (1 + exp(alpha u + b)), u the daily maximum wind speed in m per s, with its direction (l. 254); alpha and b unprinted (l. 408). Eq. 10: spores per colony Q = beta exp(delta s), beta 874 and delta 0.314 from detached-leaf inoculations, units of beta and of colony size s not printed (l. 409). Eq. 11: Qr = Qs [Q(t) + R(t-1)], R the spores left undispersed (l. 264). The simulation averages about 5,000 spores released per cm2 of sporulating tissue (l. 658). Infectious period DI 10 day, an input; reports run from 3 to 20 days (l. 271, 413).
- **Dispersal kernel:** spores released in a step are dispersed in a cone of angle theta about the wind direction (value not printed; l. 287); density falls exponentially with axial distance d from the source (decay cid) and then linearly with radial position r(theta) in the cone (l. 290); the deposit on a leaf is Qc = Qr S exp(-cid d), proportional to leaf area S, with d's unit (m or cm) not printed (l. 295). Table 1: cid 0.04, no unit, no source (l. 412). A plot-scale, long-distance model (normal distribution) is proposed as future work (l. 718).
- **Sources of parameters:** detached-leaf laboratory experiments at INRA Bordeaux 2001 to 2003 (infection, colony growth against temperature) and field vines (sporulation, leaf-age dependence); latent period and spore release from the literature (l. 334).
- **Validation and runs:** three-vine microplots of Cabernet Sauvignon inoculated on 4 May (day 124, 3 leaves) or 16 May (day 133, 5 leaves) 2001; simulations did not differ significantly from the data for incidence (P 0.81 and 0.91) and severity (P 0.74 and 0.35) (l. 348). Simulated: primary infection on day 115 gave 58 % of primary leaves diseased at flowering in late-budbreak 1998, against 19 % in early-budbreak 2003 (l. 595); ontogenic resistance limited the final infected leaf area to 36 % (1998) and 48 % (2003) of the total (l. 609).
- **Limits:** no ascospore or chasmothecia dynamics (primary infection is an input), no water stress, leaf epidemic only, no damage function for yield or quality (l. 737).

## Dependence

- **Borrows** the temperature response from Analytis (1977, 1980); the latent period from Blaise and Gessler (1992) and Rumbolz (1999); infection cardinal temperatures from Delp (1954) and Sall (1980); the wind release function from Willocquet et al. (1998). The ray model of dispersal and its decay constant are not sourced.
- **Fitted to** its own detached-leaf experiments (2001 to 2003) and 2002 Cabernet Sauvignon growth data at INRA Grande Ferrade. `leroy2013` (downy mildew) borrows this paper's latent-period method. Shared authors with `calonnec2004`: a flag.

## Bearing (2026-10-22)

- **What it answers:** a grapevine powdery mildew epidemic model with its parameters. Most values are in Table 1 (infection, colony growth, latency, spore production, infectious period). The dispersal kernel is an exponential decay along a wind cone with cid = 0.04, but with no unit, no cone angle and no calibration, so the kernel's form is usable and its constants are not.
- **For the engine's powdery mildew:** the infection cardinal temperatures (5 and 33 degC), the 6-day minimum latent period and the 10-day infectious period can be set against what the engine uses; its primary inoculum is an input here, not modelled.
- **Not shown:** a damage function; a dispersal calibration; validation beyond two inoculations in one year on a few vines, reported as non-significant differences, not as a skill score. Kind of result: a mechanistic simulation with laboratory-derived parameters.
