"""Translation diff: какие managed/*.md ещё не переведены в managed-ru/.

Usage:
    python scripts/translation_diff.py              # _pending.txt + summary
    python scripts/translation_diff.py --by-section # + _pending_by_section.txt

Сравнивает по относительному пути:
    docs/managed/managed-cluster/operation/migrate-a-cluster.md
    docs/managed-ru/managed-cluster/operation/migrate-a-cluster.md

Если RU-файл существует — считается переведённым (содержимое НЕ проверяется,
если нужна проверка пустоты — добавить позже).
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN_DIR = ROOT / "docs" / "managed"
RU_DIR = ROOT / "docs" / "managed-ru"
PENDING_TXT = ROOT / "_pending.txt"
PENDING_BY_SECTION_TXT = ROOT / "_pending_by_section.txt"


def collect(base: Path) -> set[str]:
    return {p.relative_to(base).as_posix() for p in base.rglob("*.md")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--by-section",
        action="store_true",
        help="Также вывести группировку по верхнеуровневым разделам",
    )
    args = parser.parse_args()

    if not EN_DIR.exists():
        print(f"ERROR: {EN_DIR} не существует", file=sys.stderr)
        return 1

    en = collect(EN_DIR)
    ru = collect(RU_DIR) if RU_DIR.exists() else set()

    pending = sorted(en - ru)
    extra_ru = sorted(ru - en)  # переведено, но оригинала нет (нужно перепроверить)

    PENDING_TXT.write_text("\n".join(pending) + "\n", encoding="utf-8")

    print(f"EN total:        {len(en):>5}")
    print(f"RU total:        {len(ru):>5}")
    print(f"Translated:      {len(en & ru):>5}")
    print(f"Pending:         {len(pending):>5}  -> {PENDING_TXT.name}")
    if extra_ru:
        print(f"RU без EN:       {len(extra_ru):>5}  (внимание: устаревший RU?)")
        for p in extra_ru[:10]:
            print(f"  - {p}")

    if args.by_section:
        sections: Counter[str] = Counter()
        for p in pending:
            sections[p.split("/", 1)[0]] += 1
        lines = []
        for section, count in sections.most_common():
            lines.append(f"## {section}  ({count})")
            for p in pending:
                if p.split("/", 1)[0] == section:
                    lines.append(f"- [ ] {p}")
            lines.append("")
        PENDING_BY_SECTION_TXT.write_text("\n".join(lines), encoding="utf-8")
        print(f"By-section:      {PENDING_BY_SECTION_TXT.name}")
        print()
        print("Pending by top-level section:")
        for section, count in sections.most_common():
            print(f"  {section:<30} {count:>5}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
