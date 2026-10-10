---
id: holcman2014
citation: Holcman, Ester. 2014. Sistemas de alerta fitossanitário para o controle do míldio em vinhedos conduzidos sob coberturas plásticas no Noroeste Paulista [Plant-protection warning systems for downy mildew control in vineyards under plastic covers in Northwest São Paulo]. Tese de doutorado, Universidade de São Paulo (ESALQ), Piracicaba
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 25 of 25 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, anthracnose (mentioned), powdery mildew (mentioned)]
crops: [grapevine, table grape]
regions: [Northwest São Paulo, Jales (SP), Brazil, Ohio (infection-efficiency source)]
processes: [primary infection, sporulation, oospores, sporangia, leaf wetness, warning system, spray timing, infection efficiency, microclimate, plastic cover, incidence and severity, 3-10 rule]
records: [rule_3_10, lalancette1988.infection]
datasets: []
files: [br_alerta_coberturas_2014.pdf]
---

# Holcman 2014: downy mildew warnings under plastic covers, São Paulo

A light read (the deep-research B list).

## What it holds

- Two seasons (2012, 2013) at Embrapa Jales: table grape under plastic or 18 % shade net, five treatments, six replicates (l. 292-297).
- Treatments: the 3-10 rule (BA) and two infection-efficiency warnings, MA25 and MA75 (l. 300-301).
- 2012 under plastic: untreated incidence 86.48 %; calendar 0.35 % with 20 sprays; 3-10 rule 2.08 % with 8 (l. 7694-7696, Table 4.10).
- Spray cut against the calendar: 60 to 75 % in 2012, 65.5 to 82.6 % in 2013 (l. 9038).
- 2013: no disease in any treatment; the authors blame dry weather in susceptible stages (l. 9016-9018).
- Plastic cut light by 18.3 % over the seasons (l. 6003); its wetness claim conflicts: 34 % longer (l. 307) against similar in 2012 (l. 6019-6020).
- Madden et al. 2000 equation printed (l. 6831-6833); i0 needs an unprinted i_max.
- Primary-infection trigger cited from Kennelly 2007a: rain above 2.5 mm, air above 11 C (l. 1626).

## Dependence

- Computes the 3-10 rule (Baldacci 1947): run as the BA treatment in the field on hourly data (l.6802-6820) and described in the review (l.1751-1762). Computes the infection-efficiency model of Lalancette et al. 1988a, as used by Madden et al. 2000: the MA25 and MA75 treatments (l.6823-6859). Its equations are printed at l.6831-6833; the 1988a source is named at l.6826 and l.6840. Note that the engine list names Lalancette 1988 for sporulation bounds, not for infection efficiency. Cites, does not compute: Kennelly et al. 2007a primary trigger (rain above 2.5 mm and above 11 C, l.1625-1626); Kennelly 2007b sporangia death (l.1613); Rossi et al. 2008 oospore germination (l.1593-1596); Lalancette 1988a sporulation bounds 5-25 C (l.1637-1638); Blaeser and Weltzien 1979 cycles (l.1635-1636); Zachos 1959 sunlight (l.1655). Check of the Madden equation at T 20 C, DPM 12 h gives i of 0.080 but i_max is not printed, so i0 cannot be checked. Shared authors: Kennelly and Magarey are cited, not co-authors.

## Bearing (2026-10-10)

- Field evidence that a 3-10 rule and a Lalancette-type infection-efficiency warning can cut sprays by 60 to 80 percent against a calendar in a humid tropical vineyard under plastic, with the equations printed, which the truth may use as a comparator, not as a model input for the engine.
