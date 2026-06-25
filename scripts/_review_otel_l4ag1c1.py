# -*- coding: utf-8 -*-
"""L4-AG.1c.1 review: critical defect detector.

Проверяет (по канону L4-AG.1a.15a+b):
  1) line-parity EN ↔ RU (must be exact)
  2) em-dash в RU (CLAUDE.md #0 запрет на « — »)
  3) mojibake leftover (BOM/â/Â/triple-symbols)
  4) EN-leftover целые параграфы prose (после автозамены)
  5) signal-words («You can send», «See also», «Learn how», «Related topics»...)
  6) calque comma («X, Y, и Z» — лишняя запятая перед союзом)
"""

import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

EN = Path("docs/managed")
RU = Path("docs/managed-ru")

FILES = [
    "ingest-from/technology-support/application-software/rust.md",
    "ingest-from/technology-support/application-software/ruby.md",
    "ingest-from/technology-support/application-software/erlang-elixir.md",
    "ingest-from/technology-support/application-software/cpp.md",
    "ingest-from/opentelemetry/integrations.md",
    "ingest-from/technology-support/application-software.md",
    "ingest-from/opentelemetry/walkthroughs.md",
    "ingest-from/opentelemetry/walkthroughs/java.md",
    "ingest-from/opentelemetry/walkthroughs/php.md",
    "ingest-from/opentelemetry/walkthroughs/python.md",
]

# Phrases that should NOT survive in RU (after our translation pass).
# These are EN sentence-starters / connectives. Whitelisted: identifiers,
# code, URL paths, attribute-keys.
SIGNAL_WORDS = [
    "You can send",
    "See also",
    "Learn how to",
    "Learn about",
    "Read about",
    "Read an overview",
    "This page provides",
    "The following runtimes",
    "The following walk-throughs",
    "The following features",
    "These walkthroughs",
    "Related topics",
    "Published ",
    "Updated on ",
    "Reference\n",
    "Overview\n",
    "How-to guide\n",
    "min read",
    "for capturing traces",
    "for custom tracing",
    "Yes |",  # «| Automatic instrumentation | Yes |» should be «Да»
    "Supported |",
    "Feature |",
]

# Em-dash (real Unicode U+2014). Long en-dash «–» (U+2013) допустим в списках.
EMDASH = chr(0x2014)

# Mojibake suspect chars
SUSPECT = ["â", "Â", chr(0xC3), chr(0xC2), "ï»¿", "﻿"]


def review_file(rel: str) -> list[str]:
    en_p = EN / rel
    ru_p = RU / rel
    en_text = en_p.read_text(encoding="utf-8")
    ru_text = ru_p.read_text(encoding="utf-8")

    issues = []

    # 1) line-parity
    en_lines = en_text.count("\n")
    ru_lines = ru_text.count("\n")
    if en_lines != ru_lines:
        issues.append(f"line-parity DIFF: en={en_lines} ru={ru_lines}")

    # 2) em-dash in RU
    for ln_no, line in enumerate(ru_text.splitlines(), 1):
        if EMDASH in line:
            issues.append(f"em-dash at L{ln_no}: {line[:80]}")

    # 3) mojibake leftover (anywhere outside source/scraped frontmatter lines)
    for ln_no, line in enumerate(ru_text.splitlines(), 1):
        if line.startswith(("source:", "scraped:")):
            continue
        for ch in SUSPECT:
            if ch in line:
                issues.append(f"mojibake[{ch!r}] at L{ln_no}: {line[:80]}")
                break

    # 4) EN-leftover prose: lines that contain SIGNAL_WORDS
    for ln_no, line in enumerate(ru_text.splitlines(), 1):
        if line.startswith(("source:", "scraped:")):
            continue
        for kw in SIGNAL_WORDS:
            if kw in line:
                issues.append(f"signal[{kw!r}] at L{ln_no}: {line[:120]}")

    # 5) calque comma «, и » / «, или »
    for ln_no, line in enumerate(ru_text.splitlines(), 1):
        if ", и " in line and not line.strip().startswith(("|", "-", "*", "[")):
            # check if there are >=3 enumerated items (A, B, и C)
            # heuristic: at least 2 commas before « и »
            before = line.split(", и ", 1)[0]
            if before.count(",") >= 1:
                issues.append(f"calque[,и] at L{ln_no}: {line[:80]}")

    return issues


def main():
    total = 0
    for rel in FILES:
        issues = review_file(rel)
        if issues:
            print(f"\n{rel}: {len(issues)} issues")
            for it in issues:
                print(f"  - {it}")
            total += len(issues)
        else:
            print(f"OK  {rel}")
    print(f"\nTotal issues: {total}")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
