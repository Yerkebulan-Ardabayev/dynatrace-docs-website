#!/usr/bin/env python3
"""Back up + delete old pre-restructure RU files (scraped 2026-02 / 2026-03).

These were translated from the previous scrape of docs.dynatrace.com (old URL
structure www.dynatrace.com/docs/ without /managed/). They have a different
page structure and no line-parity with the current EN corpus (scraped 2026-05).
Backed up to _backup_old_scrape_2026-0203/ before deletion (most RU files are
NOT git-tracked, so this is the only recovery path).
"""

import shutil
from pathlib import Path

RU = Path("docs/managed-ru")
BACKUP = Path("_backup_old_scrape_2026-0203")

old = []
for p in sorted(RU.rglob("*.md")):
    head = p.read_text(encoding="utf-8", errors="replace")[:800]
    for line in head.splitlines():
        if line.startswith("scraped:"):
            if line.startswith("scraped: 2026-02") or line.startswith(
                "scraped: 2026-03"
            ):
                old.append(p)
            break

print(f"old pre-restructure RU files found: {len(old)}\n")
for p in old:
    rel = p.relative_to(RU)
    dst = BACKUP / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dst)
    p.unlink()
    print(f"  purged  {rel}")

print(f"\nbacked up to {BACKUP}/ and deleted {len(old)} files")
