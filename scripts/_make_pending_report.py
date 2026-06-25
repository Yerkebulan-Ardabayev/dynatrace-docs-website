#!/usr/bin/env python3
"""Write changes_report.json listing every pending RU translation (EN without RU).

Feeds translate_managed.py (--report changes_report.json), which translates each
via local `claude -p` (no external API). Resumable with --skip-existing.
"""

import json
from pathlib import Path

en = Path("docs/managed")
ru = Path("docs/managed-ru")
en_files = {p.relative_to(en) for p in en.rglob("*.md")}
ru_files = {p.relative_to(ru) for p in ru.rglob("*.md")}
pending = sorted(str(p).replace("\\", "/") for p in (en_files - ru_files))

# smallest-first so quick wins land early and a test sample is cheap
pending.sort(key=lambda r: (en / r).stat().st_size)

report = {"new_articles": [{"path": p} for p in pending], "updated_articles": []}
json.dump(
    report,
    open("changes_report.json", "w", encoding="utf-8"),
    indent=2,
    ensure_ascii=False,
)
print(f"wrote changes_report.json with {len(pending)} pending files")
print("first 5:", pending[:5])
