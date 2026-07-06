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

# Корни source URL настоящего Managed-корпуса. Только эти считаются каноничным
# Managed. Гейт валит прогон на реально чужом (не-dynatrace) источнике.
MANAGED_PREFIXES = (
    "https://docs.dynatrace.com/managed",       # с/без завершающего слэша
    "https://www.dynatrace.com/support/",       # legacy support/help
)

# SaaS/общий docs-хост Dynatrace: это НЕ Managed (air-gapped Managed таких фич не
# имеет). Не валим прогон, т.к. отдельные такие страницы уже попали в готовый корпус,
# но и НЕ выдаём их за Managed — помечаем предупреждением для ручной ревизии.
# Managed/SaaS-границу не размываем (принцип Managed-only).
SAAS_DOCS_RE = re.compile(r"^https?://(?:www|docs)\.dynatrace\.com/docs/")
DYNATRACE_HOST_RE = re.compile(r"^https?://(?:[a-z0-9-]+\.)?dynatrace\.com/")


def main() -> int:
    if not EN_DIR.exists():
        print(f"ERROR: {EN_DIR} не существует", file=sys.stderr)
        return 1

    en_files = sorted(EN_DIR.rglob("*.md"))
    ru_files = sorted(RU_DIR.rglob("*.md")) if RU_DIR.exists() else []

    en_rel = {p.relative_to(EN_DIR).as_posix() for p in en_files}
    ru_rel = {p.relative_to(RU_DIR).as_posix() for p in ru_files}

    bad_source = []  # source на реально чужом (не-dynatrace) хосте — валит прогон
    saas_source = []  # source на SaaS/общем docs-хосте Dynatrace — предупреждение
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
        rel = p.relative_to(EN_DIR).as_posix()
        if url.startswith(MANAGED_PREFIXES):
            pass  # каноничный Managed
        elif SAAS_DOCS_RE.match(url) or DYNATRACE_HOST_RE.match(url):
            saas_source.append((rel, url))  # dynatrace, но не Managed-путь -> warn
        else:
            bad_source.append((rel, url))  # реально чужой хост -> fail
        section_count[rel.split("/", 1)[0]] += 1

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
    print(f"  Files without source:      {len(no_source):>5}")
    print(f"  Files with SaaS-docs source: {len(saas_source):>3}")
    print(f"  Files with foreign source:   {len(bad_source):>3}")
    if bad_source:
        print("  [FAIL] FOUND FOREIGN (non-Dynatrace) SOURCES:")
        for path, url in bad_source[:20]:
            print(f"    {path}  ->  {url}")
        if len(bad_source) > 20:
            print(f"    ... +{len(bad_source) - 20} more")
    else:
        print("  [OK] No foreign source hosts")
    if saas_source:
        # SaaS/общий docs-хост Dynatrace в Managed-корпусе. Не Managed по сути
        # (Copilot, Grail-приложения и т.п. в air-gapped Managed недоступны).
        # Не валим прогон (уже в готовом корпусе), но помечаем для ручной ревизии,
        # НЕ выдаём за Managed. Managed/SaaS-границу держим явно.
        print(f"  [WARN] {len(saas_source)} файл(ов) ссылаются на SaaS-хост dynatrace.com/docs/ (не Managed, проверить):")
        for path, url in saas_source[:10]:
            print(f"    {path}  ->  {url}")
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

    # Гейт валит прогон ТОЛЬКО на реально чужом (не-dynatrace) источнике (bad_source).
    # SaaS-хост dynatrace.com/docs/ и отсутствие source: — предупреждения, не блокируют
    # (эти файлы уже в готовом каноне; SaaS помечен явно, за Managed не выдаётся).
    if bad_source:
        print(f"\n[FAIL] {len(bad_source)} файл(ов) с чужим (не-Dynatrace) source — гейт заблокировал прогон")
        return 1
    print("\n[OK] Managed source-check пройден", end="")
    if saas_source:
        print(f" (внимание: {len(saas_source)} файл(ов) с SaaS-source — см. WARN выше)", end="")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
