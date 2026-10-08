"""Find a paper's DOI and metadata on Crossref, from a free-text citation.

    python scripts/crossref_lookup.py "Rafaila Sevcenco David 1968 biology Plasmopara viticola"

Prints the best matches: DOI, title, authors, journal, volume, pages and year.

Crossref's metadata is a lead, not a reading. Use it to find the paper, to fix a citation's
volume or pages, and to see the author list a publisher deposited. Record an author list
as `read` only after reading it in the paper itself. Standard library only; calls
api.crossref.org, so it needs the network, and no test runs it.
"""

from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request

API = "https://api.crossref.org/works"
FIELDS = "DOI,title,author,issued,container-title,volume,issue,page"


def lookup(citation: str, rows: int = 5) -> list[dict]:
    query = urllib.parse.urlencode(
        {"query.bibliographic": citation, "rows": rows, "select": FIELDS}
    )
    with urllib.request.urlopen(f"{API}?{query}", timeout=30) as response:
        return json.load(response)["message"]["items"]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    for item in lookup(" ".join(sys.argv[1:])):
        authors = "; ".join(
            f"{a.get('family', '')}, {a.get('given', '')}".strip(", ")
            for a in item.get("author", [])
        )
        year = (item.get("issued", {}).get("date-parts") or [[None]])[0][0]
        print(f"{item.get('DOI')}  ({year})")
        print(f"    {(item.get('title') or [''])[0]}")
        print(f"    {authors or '(no authors deposited)'}")
        journal = (item.get("container-title") or [""])[0]
        volume, issue, page = (item.get(k, "") for k in ("volume", "issue", "page"))
        print(f"    {journal} {volume}({issue}) {page}")
    print("\nA lead, not a reading: read the author list in the paper before recording it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
