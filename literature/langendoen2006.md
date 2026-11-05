---
id: langendoen2006
citation: Langendoen, K., Baggio, A. & Visser, O. 2006. Murphy loves potatoes: experiences from a pilot sensor network deployment in precision agriculture. 20th IEEE International Parallel and Distributed Processing Symposium (IPDPS), workshop WPDRTS, Rhodes
doi: 10.1109/IPDPS.2006.1639412
read: "2026-11-04, in full, searched for yield and failure, by a reading agent and a note writer; 5 of 5 quotes found at their lines by scripts/verify_quotes.py"
status: read
diseases: []
crops: [potato]
regions: [Netherlands]
processes: [wireless sensor network, data yield, node failure, packet loss, deployment]
records: []
datasets: []
files: [dr1104_langendoen2006.pdf (the 2026-11-04 drop)]
---

# Langendoen, Baggio & Visser 2006: a 100-node potato-field sensor network that returned 2 % of its messages

A Delft report on a failed pilot of about 100 Mica2 nodes in a Dutch potato field in 2005, written as lessons for sensor-network engineers.

**Read this first.**
- The 2 % yield came from software bugs in a prototype network, not from the usual failure rate of field loggers. It is a lower bound on what an untested design can lose, not a rate to use for commercial loggers.
- The DOI is unchecked (the reading agent's note). The text is two-column and the extracted lines interleave the columns, so quotes are left-column fragments.

## What it holds

- **Test run (l. 378, l. 379):** 97 nodes running for three weeks, each sending 1 message per 10 minutes; 5 874 messages received.
- **Yield (l. 380):** that "amounts to 2%" of the expected messages. The cause was a software bug, not a field failure rate.
- **Resets (l. 328):** nodes reset "at an alarming rate", once every 2 to 6 h (the reading agent's reading of the line).
- **Design assumptions (l. 389):** the design assumed 1 node failing per week of about 100 and packet error rates under 10 %; the pilot showed these to be wrong.
- **Setting:** prototype Mica2 network, potato field, the Netherlands, 2005; precision agriculture.

## Dependence

None recorded.

## Bearing (2026-11-04)

- **sense.logger_loss_per_day (Cooptera, Agrarium sensing):** a pilot network's data yield, 2 % over three weeks. It shows an upper limit of failure for an untested research network, not a rate for a vineyard logger. Kind of evidence: one pilot, 97 nodes, the authors' count, a software fault.
- Use with the single-station completeness in okan2026 (98.6 %) to bracket the range; do not average them.
