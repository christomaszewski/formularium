"""Extract a paper's text for reading, and map where things are in it.

    python scripts/extract_paper.py PAPER.pdf [--out DIR]

Copies the PDF into its own new directory (a downloaded file is untrusted data), runs
poppler's `pdftotext -layout`, and prints:
- the page count, the PDF's own title, and characters per page: under about 500 a page
  usually means a scan without a text layer, which needs OCR before anyone can read it;
- the DOIs found in the text;
- the first lines, where the title and authors usually are;
- a map of headings, tables, figures, equations and the reference list, with line numbers.

The text lands in DIR/paper.txt (default: a new temporary directory). Read it there, cite
line numbers, and delete the directory when done: neither the PDF nor its text goes into a
repository. Standard library only; needs `pdftotext` and `pdfinfo` (Debian: poppler-utils).
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANDMARKS = re.compile(
    r"^\s*(abstract|summary|r[ée]sum[ée]|zusammenfassung|introduction|materials?|methods?|"
    r"m[ée]thodes?|results?|r[ée]sultats?|discussion|conclusions?|references|literature|"
    r"bibliograph\w*|acknowledg\w*|table|tableau|tabelle|fig\.?|figure|eq\.?|equation|"
    r"chapitre|chapter|annexe?|appendix)\b",
    re.IGNORECASE,
)
DOI = re.compile(r"\b10\.\d{4,9}/[^\s\"<>,;]+", re.IGNORECASE)


def _run(*args: str) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--out", type=Path, help="directory to create (default: a temp dir)")
    args = parser.parse_args()
    if not shutil.which("pdftotext"):
        print("pdftotext is missing: install poppler-utils", file=sys.stderr)
        return 2
    out = args.out or Path(tempfile.mkdtemp(prefix="paper-"))
    out.mkdir(parents=True, exist_ok=True)
    pdf = out / "paper.pdf"
    shutil.copyfile(args.pdf, pdf)
    txt = out / "paper.txt"
    _run("pdftotext", "-layout", str(pdf), str(txt))
    info = _run("pdfinfo", str(pdf))
    pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    title = re.search(r"^Title:\s+(.*)$", info, re.M)
    text = txt.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    per_page = len(text) / max(pages, 1)

    print(f"text:   {txt}")
    print(f"pages:  {pages}; characters per page: {per_page:.0f}")
    if per_page < 500:
        print("        few characters per page: probably a scan; OCR it before reading")
    print(f"title:  {title.group(1).strip() if title else '(none in the PDF)'}")
    dois = sorted({d.rstrip(".)") for d in DOI.findall(text)})
    print(f"DOIs:   {', '.join(dois[:8]) or '(none found)'}")
    print("\nfirst lines:")
    for line in [ln.strip() for ln in lines if ln.strip()][:12]:
        print(f"    {line[:110]}")
    print("\nlandmarks (line: text):")
    for number, line in enumerate(lines, start=1):
        if LANDMARKS.match(line):
            print(f"  {number:6d}: {line.strip()[:100]}")
    print(f"\nDelete {out} when done: the paper stays out of every repository.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
