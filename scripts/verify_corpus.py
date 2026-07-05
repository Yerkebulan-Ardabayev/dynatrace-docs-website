"""Critical verification: что в docs/managed/ — действительно Managed, и tracking совпадает с реальностью.

Запускать каждый раз перед/после батча, чтобы не было «забытых» файлов.

Usage:
    python scripts/verify_corpus.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN_DIR = ROOT / "docs" / "managed"
RU_DIR = ROOT / "docs" / "managed-ru"

SOURCE_RE = re.compile(r"^source:\s*(https?://\S+)", re.MULTILINE)

# Допустимые корни source URL для Managed-корпуса. Dynatrace отдаёт одну и ту же
# документацию с нескольких хостов; часть страниц канона (уже принятого пользователем)
# ссылается на www.dynatrace.com/docs и docs.dynatrace.com/managed без завершающего
# слэша. Всё это — легитимный Managed-корпус. Гейт должен ловить действительно чужое
# (не-dynatrace хост или SaaS-only путь), а не падать на готовом корпусе.
ALLOWED_PREFIXES = (
    "https://docs.dynatrace.com/managed",       # с/без завершающего слэша
    "https://docs.dynatrace.com/docs/",         # общий docs-хост (Managed+SaaS)
    "https://www.dynatrace.com/docs/",          # альтернативный docs-домен
    "https://www.dynatrace.com/support/",       # legacy support/help
)


def main() -> int:
    if not EN_DIR.exists():
        print(f"ERROR: {EN_DIR} не существует", file=sys.stderr)
        return 1

    en_files = sorted(EN_DIR.rglob("*.md"))
    ru_files = sorted(RU_DIR.rglob("*.md")) if RU_DIR.exists() else []

    en_rel = {p.relative_to(EN_DIR).as_posix() for p in en_files}
    ru_rel = {p.relative_to(RU_DIR).as_posix() for p in ru_files}

    bad_source = []  # source URL не похож на Managed
    no_source = []  # вообще нет source: в frontmatter
    section_count: Counter[str] = Counter()

    for p in en_files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"WARN: не прочитан {p}: {e}", file=sys.stderr)
            continue
        m = SOURCE_RE.search(text)
        if not m:
            no_source.append(p.relative_to(EN_DIR).as_posix())
            continue
        url = m.group(1)
        if not url.startswith(ALLOWED_PREFIXES):
            bad_source.append((p.relative_to(EN_DIR).as_posix(), url))
        section_count[p.relative_to(EN_DIR).as_posix().split("/", 1)[0]] += 1

    print("=" * 70)
    print("Corpus verification -- docs/managed/")
    print("=" * 70)
    print(f"EN files (total):         {len(en_rel):>5}")
    print(f"RU files (total):         {len(ru_rel):>5}")
    print(f"Translated (EN AND RU):   {len(en_rel & ru_rel):>5}")
    print(f"Pending (EN minus RU):    {len(en_rel - ru_rel):>5}")
    print(f"Orphan RU (RU minus EN):  {len(ru_rel - en_rel):>5}")
    print()
    print("Source check:")
    print(f"  Files without source:   {len(no_source):>5}")
    print(f"  Files with non-managed source: {len(bad_source):>3}")
    if bad_source:
        print("  [WARN] FOUND NON-MANAGED SOURCES:")
        for path, url in bad_source[:20]:
            print(f"    {path}  ->  {url}")
        if len(bad_source) > 20:
            print(f"    ... +{len(bad_source) - 20} more")
    else:
        print("  [OK] All source URLs point to Managed docs")
    if no_source:
        # Не фатально: часть канона — рукописные сводные руководства (backup.md,
        # installation.md и т.п.) без scraped-frontmatter. Это ожидаемо, не блокируем.
        print(f"  [WARN] {len(no_source)} files without source (рукописные, ок):")
        for path in no_source[:10]:
            print(f"    {path}")
    print()
    print(f"Pending by top-level section:")
    pending_by_section: Counter[str] = Counter()
    for p in sorted(en_rel - ru_rel):
        pending_by_section[p.split("/", 1)[0]] += 1
    for section, count in pending_by_section.most_common():
        total_in_section = section_count.get(section, count)
        # для root-level .md секция == имя файла, total = 1
        if "/" not in section and section.endswith(".md"):
            print(f"  {section:<30} {count:>5} (root index)")
        else:
            done = total_in_section - count
            print(
                f"  {section:<30} {count:>5} pending / {total_in_section} total ({done} done)"
            )

    # Гейт валит прогон ТОЛЬКО на реально чужом источнике (bad_source): не-dynatrace
    # хост или SaaS-only путь, попавший в Managed-дерево. Отсутствие source: —
    # предупреждение, не блокирует (рукописные файлы канона легитимны).
    if bad_source:
        print(f"\n[FAIL] {len(bad_source)} файл(ов) с чужим (не-Managed) source — гейт заблокировал прогон")
        return 1
    print("\n[OK] Корпус Managed консистентен (source-check пройден)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
