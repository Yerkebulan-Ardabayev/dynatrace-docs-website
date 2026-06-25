"""Screen all RU translations against EN sources for quality risks.

Output: TRANSLATION_REWORK.md with at-risk files sorted by severity.
Criteria: RU/EN ratio<0.7, different code-block count, or >15% link count diff.
"""

import re
from pathlib import Path

en_dir = Path("docs/managed")
ru_dir = Path("docs/managed-ru")
risky = []
total = 0
for ru_file in ru_dir.rglob("*.md"):
    rel = ru_file.relative_to(ru_dir)
    en_file = en_dir / rel
    if not en_file.exists():
        continue
    total += 1
    en_text = en_file.read_text(encoding="utf-8")
    ru_text = ru_file.read_text(encoding="utf-8")
    en_lines = en_text.count("\n")
    ru_lines = ru_text.count("\n")
    if en_lines < 30:
        continue
    ratio = ru_lines / en_lines if en_lines else 0
    en_code = en_text.count("```")
    ru_code = ru_text.count("```")
    en_links = len(re.findall(r"\]\([^)]+\)", en_text))
    ru_links = len(re.findall(r"\]\([^)]+\)", ru_text))
    flags = []
    if ratio < 0.7:
        flags.append(f"ratio={ratio:.2f}")
    if en_code != ru_code:
        flags.append(f"code:{en_code}vs{ru_code}")
    if en_links and abs(en_links - ru_links) > max(2, en_links * 0.15):
        flags.append(f"links:{en_links}vs{ru_links}")
    if flags:
        risky.append(
            (ratio, en_lines, ru_lines, "/".join(flags), str(rel).replace("\\", "/"))
        )

risky.sort()

with open("TRANSLATION_REWORK.md", "w", encoding="utf-8") as f:
    f.write("# Под-риск файлы для пере-перевода или ревизии\n\n")
    f.write("Дата screening: 2026-05-14\n")
    f.write(
        f"Всего переведено: {total}. Под-риск: {len(risky)} ({len(risky) / total * 100:.1f}%).\n\n"
    )
    f.write(
        "Критерии: RU/EN ratio<0.7 ИЛИ разное число code-блоков ИЛИ разница ссылок >15%.\n\n"
    )
    f.write("Сортировка: по возрастанию ratio (худшие первыми).\n\n")
    f.write("| # | EN | RU | Flags | Path |\n")
    f.write("|---|---|---|---|---|\n")
    for i, (r, en, ru, fl, p) in enumerate(risky, 1):
        f.write(f"| {i} | {en} | {ru} | {fl} | {p} |\n")

print(f"Total translated: {total}")
print(f"At-risk: {len(risky)}")
print()
sev = {
    "critical (<0.30)": 0,
    "major (0.30-0.50)": 0,
    "minor (0.50-0.70)": 0,
    "code/links only": 0,
}
for r, en, ru, fl, p in risky:
    if "ratio" not in fl:
        sev["code/links only"] += 1
    elif r < 0.30:
        sev["critical (<0.30)"] += 1
    elif r < 0.50:
        sev["major (0.30-0.50)"] += 1
    else:
        sev["minor (0.50-0.70)"] += 1
for k, v in sev.items():
    print(f"  {k}: {v}")
