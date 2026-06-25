# -*- coding: utf-8 -*-
"""Generate PENDING_TRANSLATION.md — a human-readable, always-current tracker of
which docs/managed (EN) files still lack a docs/managed-ru (RU) translation.

Run from repo root (works identically on Windows and Mac):
    python scripts/_gen_pending_md.py

It diffs docs/managed vs docs/managed-ru (same logic as _pending_inventory.py)
and writes PENDING_TRANSLATION.md with a per-area checklist of what's left.
"""

import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "docs", "managed")
RU = os.path.join(ROOT, "docs", "managed-ru")


def rels(base):
    out = set()
    for r, _, fs in os.walk(base):
        for fn in fs:
            if fn.endswith(".md"):
                out.add(os.path.relpath(os.path.join(r, fn), base).replace("\\", "/"))
    return out


def main():
    en, ru = rels(EN), rels(RU)
    pending = sorted(en - ru)
    done = len(en) - len(pending)
    pct = (done / len(en) * 100) if en else 0.0

    groups = defaultdict(list)
    for p in pending:
        parts = p.split("/")
        key = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
        groups[key].append(p)

    lines = []
    lines.append("# Что ещё нужно перевести (EN -> RU)")
    lines.append("")
    lines.append(
        f"**Готово: {done} / {len(en)} ({pct:.2f}%). Осталось: {len(pending)} файлов.**"
    )
    lines.append("")
    lines.append(
        "> Этот файл генерируется автоматически. Пересоздать актуальную версию:"
    )
    lines.append(
        "> `python scripts/_gen_pending_md.py`  (или `python scripts/_pending_inventory.py` для сводки в консоль)."
    )
    lines.append(">")
    lines.append("> Как доперевести: открыть Claude Code в этой папке и сказать,")
    lines.append(
        "> например: «продолжай перевод раздела amazon-web-services по тому же пайплайну»."
    )
    lines.append(
        "> EN-исходник: `docs/managed/<путь>` -> RU-результат: `docs/managed-ru/<путь>`."
    )
    lines.append(
        "> Движок и глоссарии: `scripts/` (_zos_canon_l4if71.py, _GLOSSARY_*.md, _build_*.py)."
    )
    lines.append("")
    if not pending:
        lines.append("Все файлы переведены. ✅")
    else:
        for key in sorted(groups, key=lambda k: -len(groups[k])):
            lines.append(f"## {key}  ({len(groups[key])})")
            lines.append("")
            for p in groups[key]:
                lines.append(f"- [ ] `{p}`")
            lines.append("")

    out = os.path.join(ROOT, "PENDING_TRANSLATION.md")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(
        f"wrote {out}: {len(pending)} pending across {len(groups)} groups ({pct:.2f}% done)"
    )


if __name__ == "__main__":
    main()
