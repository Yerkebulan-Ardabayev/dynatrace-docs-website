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

    # Active mass-translation scope is docs/managed/ingest-from — ALL real
    # remaining work lives there. Other top-level pages (managed-cluster API
    # refs, installation.md, etc.) are legacy / CI-rescrape-managed and may
    # appear/disappear with the scheduled scrape; kept in a separate section so
    # the tracker reads correctly on any machine regardless of git/disk drift.
    active = [p for p in pending if p.startswith("ingest-from/")]
    legacy = [p for p in pending if not p.startswith("ingest-from/")]

    def group(items):
        g = defaultdict(list)
        for p in items:
            parts = p.split("/")
            key = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
            g[key].append(p)
        return g

    def emit(items):
        for key, lst in sorted(group(items).items(), key=lambda kv: -len(kv[1])):
            lines.append(f"### {key}  ({len(lst)})")
            lines.append("")
            for p in lst:
                lines.append(f"- [ ] `{p}`")
            lines.append("")

    lines = []
    lines.append("# Что ещё нужно перевести (EN -> RU)")
    lines.append("")
    lines.append(f"**Готово: {done} / {len(en)} ({pct:.2f}%).**")
    lines.append("")
    lines.append(
        f"- **Активный перевод (`ingest-from`): осталось {len(active)} файлов** — это реальная работа."
    )
    if legacy:
        lines.append(
            f"- Прочие/legacy страницы: {len(legacy)} (топ-левел / cluster-API, управляются CI-рескрейпом, низкий приоритет)."
        )
    lines.append("")
    lines.append("> Генерируется автоматически: `python scripts/_gen_pending_md.py`.")
    lines.append(
        "> Как доперевести: открыть Claude Code в этой папке и сказать, например:"
    )
    lines.append(
        "> «продолжай перевод раздела amazon-web-services по тому же пайплайну (движок `_zos_canon_l4if71`, глоссарий, субагенты, QA, крит.ревью)»."
    )
    lines.append(
        "> EN-исходник: `docs/managed/<путь>` -> RU-результат: `docs/managed-ru/<путь>`."
    )
    lines.append("")
    if not pending:
        lines.append("Все файлы переведены. ✅")
    else:
        lines.append("## Активный перевод — ingest-from")
        lines.append("")
        if not active:
            lines.append("Раздел ingest-from переведён полностью. ✅")
            lines.append("")
        else:
            emit(active)
        if legacy:
            lines.append("## Прочие / legacy (низкий приоритет, управляется CI)")
            lines.append("")
            emit(legacy)

    out = os.path.join(ROOT, "PENDING_TRANSLATION.md")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(
        f"wrote {out}: active(ingest-from)={len(active)}, legacy={len(legacy)}, total={len(pending)} ({pct:.2f}% done)"
    )


if __name__ == "__main__":
    main()
