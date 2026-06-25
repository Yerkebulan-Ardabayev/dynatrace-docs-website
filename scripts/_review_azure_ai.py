#!/usr/bin/env python3
"""Automated QA for the monitor-azure-ai-* RU batch.

Checks per file: line-parity, em-dash, frontmatter source/scraped byte-equal,
URL set identical (EN vs RU), mojibake ellipsis preserved, and leftover EN
phrases that would indicate a missed translation. UI labels / dimensions /
metric names / image alts are legitimately EN and are NOT flagged.
"""

import re
from pathlib import Path

EN_DIR = Path(
    "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
)
RU_DIR = Path(
    "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
)

MOJIBAKE = b"\xc3\xa2\xc2\x80\xc2\xa6"  # double-encoded ellipsis
URL_RE = re.compile(r"\]\((/[^ )]+|https?://[^ )]+)")

# EN phrases that must NOT survive in RU (a leftover = missed replacement).
LEFTOVER = [
    "How-to guide",
    "min read",
    "* Published",
    "## Prerequisites",
    "## Enable monitoring",
    "## View service metrics",
    "## Available metrics",
    "### View metrics on",
    "To access the custom device",
    "Filter by service name",
    "Once you select",
    "lists all instances",
    "If the service has a preset",
    "For existing monitored services",
    "you can clone and edit",
    "Hiding a dashboard",
    "ingests metrics from",
    "You can view",
    "open the browse menu",
    "Dynatrace version",
    "ActiveGate version ",
    "Number of calls",
    "Total number of",
    "Size of incoming",
    "Size of outgoing",
    "Latency in milliseconds",
    "successful calls",
    "Number of errors",
    "Number of server",
    "Number of generated",
    "Processed ",
    " monitoring\n",
    "To learn how to enable",
    "Enable Azure monitoring",
]


def fm(text):
    out = {}
    for line in text.splitlines():
        if line.startswith("source:"):
            out["source"] = line
        elif line.startswith("scraped:"):
            out["scraped"] = line
        if line.strip() == "---" and len(out) >= 1 and "scraped" in out:
            break
    return out


def main():
    files = sorted(p.name for p in EN_DIR.glob("monitor-azure-ai-*.md"))
    total_fail = 0
    for f in files:
        en_b = (EN_DIR / f).read_bytes()
        ru_b = (RU_DIR / f).read_bytes()
        en, ru = en_b.decode("utf-8"), ru_b.decode("utf-8")
        fails = []

        # 1 line parity
        if en.count("\n") != ru.count("\n"):
            fails.append(f"line-parity {en.count(chr(10))}!={ru.count(chr(10))}")
        # 2 em-dash
        if "—" in ru:
            fails.append(f"em-dash x{ru.count(chr(0x2014))}")
        # 3 frontmatter source/scraped byte-equal
        if fm(en) != fm(ru):
            fails.append("frontmatter source/scraped differs")
        # 4 URL set identical (order-sensitive)
        if URL_RE.findall(en) != URL_RE.findall(ru):
            fails.append("URL list differs")
        # 5 mojibake preserved
        if en_b.count(MOJIBAKE) != ru_b.count(MOJIBAKE):
            fails.append(f"mojibake {en_b.count(MOJIBAKE)}!={ru_b.count(MOJIBAKE)}")
        # 6 leftover EN phrases (skip frontmatter title line which is EN-derived)
        body = ru
        for p in LEFTOVER:
            if p in body:
                fails.append(f"leftover EN: {p!r}")

        if fails:
            total_fail += 1
            print(f"FAIL  {f}")
            for x in fails:
                print(f"        - {x}")
        else:
            print(f"OK    {f}")
    print(f"\n{len(files) - total_fail}/{len(files)} clean")


if __name__ == "__main__":
    main()
