---
id: magarey2010
citation: Magarey, Peter A. 2010. Managing Downy Mildew (Winning the war!). Grape and Wine Research and Development Corporation, Innovators Network fact sheet, module INO904, March 2010, 6 pp.
doi: 
read: 2026-10-10, a light read (methods, results and conclusions), by a reading agent (claude-haiku-5-5); 23 of 23 quotes found at their lines by scripts/verify_quotes.py
status: read
diseases: [downy mildew, powdery mildew]
crops: [grapevine]
regions: [Australia, Hunter Valley, inland regions of Australia]
processes: [primary infection, secondary infection, infection, incubation, sporulation, oospores, leaf wetness, spray timing, season severity, dispersal]
records: [magarey2010.rules]
datasets: []
files: [B11-magarey2010-gwrdc.pdf]
---

# Magarey 2010: managing downy mildew, an Australian grower fact sheet

A light read (the deep-research B list).

## What it holds

- A GWRDC fact sheet by Peter A. Magarey, March 2010, on managing downy mildew (l. 1-11, 22).
- Severe disease once in 9-10 years in inland regions; more often in the Hunter Valley (l. 33-35).
- Primary infection rule of thumb 10:10:24: at least 10 mm rain and at least 10 °C over 24 h (l. 120-122); oospores need 16 h of wetting at 8 °C or more (l. 126-127).
- Sporulation at RH 98 % or more and 13 °C or more for 4 h of darkness; infection after 45 °C-h of leaf wetness (l. 133-137).
- Incubation 5-17 days, temperature-controlled, with no formula (l. 101).
- Post-infection sprays work within 5 days of infection (l. 219).

## Dependence

- Yes, the sheet is the source of an engine formulation. The Formularium catalogue record for Cooptera's magarey2010.rules (the engine's 'downy mildew rules of thumb') describes it as 'Magarey 2010, Managing Downy Mildew (GWRDC fact sheet)', with the rules 10:10:24, sporulation and infection; this sheet prints those rules (l. 120-123 for 10:10:24; l. 133-137 for sporulation and the 45 °C-h leaf-wetness infection rule). So it shares the rules' form and numbers with an engine model: it computes nothing itself, but the engine's rules are its rules. The 5-day lower bound the engine takes for incubation is the lower end of this sheet's 5-17 days (l. 101), which the sheet does not source. The 45 °C-h threshold is not the 60 °C·h wetness rule of Blaeser & Weltzien 1979 (an engine-list model), and the 13 °C sporulation bound is not checked against Lalancette 1988 or Caffi 2013 here. Magarey is the author: a flag only.

## Bearing (2026-10-10)

- The source of the engine's magarey2010.rules (10:10:24, sporulation, infection), so a truth that holds those rules out must not use this sheet's numbers, and its threshold values are unsourced and need the Lalancette, Caffi and Blaeser & Weltzien checks before any use.
