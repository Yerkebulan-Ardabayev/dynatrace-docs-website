# -*- coding: utf-8 -*-
"""L4-IF.73 terminology post-pass (deterministic, idempotent).

Folds in the cross-file fixes the critical review found that structural QA is blind
to. Every fix was verified against corpus norm BEFORE inclusion (item 14):

* TOOLTIPS (#9): azure-monitoring-guide.md left ~17 EN link tooltips untranslated
  (line has Cyrillic link-text -> leftover scan blind). Two sources:
  - URL-matched: for each `](url "EN tooltip")` whose URL already has a canonical
    Cyrillic tooltip elsewhere in the shipped corpus, reuse that canonical RU.
  - NO_MATCH: 5 tooltips whose URL has no corpus RU yet -> explicit RU below,
    grounded on corpus phrasing ("Настройка и конфигурирование мониторинга ...").
* TITLE (#16): azure-arc-enabled-servers.md kept `Microsoft Azure Arc-enabled
  servers` EN; the hub links it as "Серверы Microsoft Azure с поддержкой Azure
  Arc" (blindspot #13: link-text == target title) -> translate title: + # H1.
  NB: azure-native-integration "Azure Native Dynatrace Service" stays EN (product
  /offering name, inbound link-text EN, "Azure Native" kept EN 23x) -> NOT here.
* MISC (#11): one ": это" over-correction in web-app-for-containers.md.

Kept EN after verification (NOT touched): img alt (corpus 189:3 EN), "Step N"
(corpus split ~50/50), "Expand row" (41x EN), dimension cells "Name of the node",
bold UI labels incl. "custom device overview page" (bold-UI-label rule).

Re-runnable: only replaces exact EN strings. Run from repo root:
    python scripts/_apply_l10n_azure.py
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
RU_ROOT = os.path.join(BASE, "managed-ru")
AZ_REL = "ingest-from/microsoft-azure-services"
AZ = os.path.join(RU_ROOT, AZ_REL)

CYR = re.compile(r"[А-Яа-яЁё]")
LINK = re.compile(r'\]\(([^)\s]+)\s+"([^"]+)"\)')  # ](url "tooltip")

# 32 batch files (relative to managed-ru) — only these are touched.
BATCH = set()
for _r, _d, _fs in os.walk(AZ):
    for _fn in _fs:
        if _fn.endswith(".md"):
            BATCH.add(os.path.join(_r, _fn))

# --- explicit RU for the 5 tooltips whose URL has no corpus RU yet -------------
NO_MATCH = {
    "Set and configure your Dynatrace SaaS environment using Azure Marketplace.": "Настройте и сконфигурируйте среду Dynatrace SaaS через Azure Marketplace.",
    "Set up and configure Azure monitoring in Dynatrace.": "Настройка и конфигурирование мониторинга Azure в Dynatrace.",
    "Set up and configure metric events for alerting.": "Настройка и конфигурирование метрических событий для оповещений.",
    "Guide how to limit Azure API calls to avoid throttling limits": "Руководство по ограничению вызовов Azure API во избежание лимитов троттлинга",
    "Integration with Azure Monitor alerts and supported Azure Monitor alerts types": "Интеграция с оповещениями Azure Monitor и поддерживаемые типы оповещений Azure Monitor",
}

# --- page title (#16) applied to `title: X` and `# X` ------------------------
TITLES = {
    "Microsoft Azure Arc-enabled servers": "Серверы Microsoft Azure с поддержкой Azure Arc",
}

# --- targeted MISC fixes -----------------------------------------------------
MISC = {
    "что и команда запуска: это команда, выполняющая скрипт": "что и команда запуска, то есть команда, выполняющая скрипт",
}


def build_url2ru():
    """Canonical Cyrillic tooltip per URL, from the whole shipped corpus."""
    url2ru = {}
    for r, _, fs in os.walk(RU_ROOT):
        for fn in fs:
            if not fn.endswith(".md"):
                continue
            txt = open(os.path.join(r, fn), encoding="utf-8").read()
            for url, tip in LINK.findall(txt):
                if CYR.search(tip):
                    url2ru.setdefault(url, {}).setdefault(tip, 0)
                    url2ru[url][tip] += 1
    return {u: max(d.items(), key=lambda x: x[1])[0] for u, d in url2ru.items()}


def patch_text(t, url2ru):
    n = 0

    # 1) tooltips by URL canonical (only EN tooltips, >=3 words, prose)
    def repl(m):
        nonlocal n
        url, tip = m.group(1), m.group(2)
        if CYR.search(tip):
            return m.group(0)
        if tip in NO_MATCH:
            n += 1
            return '](%s "%s")' % (url, NO_MATCH[tip])
        if url in url2ru and len(tip.split()) >= 3:
            n += 1
            return '](%s "%s")' % (url, url2ru[url])
        return m.group(0)

    t = LINK.sub(repl, t)

    # 2) titles (#16) on `title:`/`# ` lines only
    lines = t.split("\n")
    for i, l in enumerate(lines):
        s = l.strip()
        for en, ru in TITLES.items():
            if s == "title: " + en:
                lines[i] = "title: " + ru
                n += 1
            elif s == "# " + en:
                lines[i] = "# " + ru
                n += 1
    t = "\n".join(lines)

    # 3) misc targeted
    for en, ru in MISC.items():
        if en in t:
            n += t.count(en)
            t = t.replace(en, ru)
    return t, n


def main():
    url2ru = build_url2ru()
    total = touched = 0
    for p in sorted(BATCH):
        with open(p, encoding="utf-8", newline="") as f:
            t = f.read().replace("\r\n", "\n").replace("\r", "\n")
        nt, n = patch_text(t, url2ru)
        if n:
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(nt)
            rel = os.path.relpath(p, AZ).replace("\\", "/")
            print("  %3d  %s" % (n, rel))
            total += n
            touched += 1
    print("\nTOTAL: %d replacements across %d files" % (total, touched))


if __name__ == "__main__":
    main()
