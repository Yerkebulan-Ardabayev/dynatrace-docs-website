# -*- coding: utf-8 -*-
"""One-shot: mark the 10 L4-IF.35 GCP files done in the pending trackers and
prepend an L4-IF.35 section to TRANSLATION_PROGRESS.md. Run once."""

import os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PATHS = [
    "ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring.md",
    "ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring.md",
    "ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring.md",
    "ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring.md",
    "ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring.md",
    "ingest-from/google-cloud-platform/gcp-integrations/gcp-functions.md",
    "ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md",
    "ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md",
    "ingest-from/google-cloud-platform/gcp-integrations/gcp-guide.md",
    "ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new.md",
]

# 1) _pending.txt: drop the 10 lines
pend = open("_pending.txt", encoding="utf-8").read().split("\n")
keep = [l for l in pend if l.strip() not in PATHS]
removed = len(pend) - len(keep)
open("_pending.txt", "w", encoding="utf-8", newline="\n").write("\n".join(keep))
print(
    f"_pending.txt: removed {removed} lines, now {len([l for l in keep if l.strip()])} entries"
)

# 2) _pending_by_section.txt: flip - [ ] -> - [x]
sec = open("_pending_by_section.txt", encoding="utf-8").read()
flipped = 0
for p in PATHS:
    a = f"- [ ] {p}"
    if a in sec:
        sec = sec.replace(a, f"- [x] {p}")
        flipped += 1
open("_pending_by_section.txt", "w", encoding="utf-8", newline="\n").write(sec)
print(f"_pending_by_section.txt: flipped {flipped} checkboxes")

# 3) TRANSLATION_PROGRESS.md: prepend L4-IF.35 (colon, not em-dash, per style rule)
SECTION = """## L4-IF.35 (2026-06-04, Opus 4.8): GCP per-service monitoring leaves + hubs +10

**Прогресс:** 2205 -> 2215/2655 = 83.43%, pending 450 -> 440. GCP остаток 30 -> 20 (gcp-guide subtree 10, OTel-on-GCF walkthroughs 6, cloudrun.md 1, legacy 3).

**Файлы (10):**
- 5 metric-leaf (build-script `_build_gcp_metrics_l4if35.py`, канон L4-IF.34): cloudrun/cloud-run-monitoring (51), gcp-functions/cloud-functions-monitoring (45), google-app-engine/app-engine-monitoring (80), google-compute-engine/compute-engine-monitoring (385), google-gke/google-kubernetes-engine-monitoring (156). 4-колоночные таблицы: header переведён, Name/identifier EN, Unit переведён.
- 5 hubs (build-script `_build_gcp_hubs_l4if35.py`, построчный dict): gcp-functions (35), google-compute-engine (26), google-app-engine (89), gcp-guide (56), gcp-supported-service-metrics-new (99; services-таблица 40 строк, link-text = title целевой страницы, yes/no -> да/нет).

**Каноны (durable):**
- UNIT map дополнен: NanoSecond -> Наносекунда, MebiByte -> Мебибайт (раньше отсутствовали).
- Title `X with Operations suite metrics monitoring` -> `Мониторинг X с метриками Operations suite` (спец-кейс; generic `X monitoring` -> `Мониторинг X` оставил бы EN-хвост в заголовке).
- Hub services-table: link-text каждой строки = RU-title целевой страницы (кросс-страничная консистентность); yes -> да / no -> нет; entity-id EN; footnote `[1](#fn-1-1-def)` byte-identical.

**QA авто 10/10 PASS** (`_qa_l4if35.py`): 0 FAIL / 0 WARN. line-parity, frontmatter byte-eq, em-dash=0, mojibake/BOM=0, URL-identity, code-fence, heading-parity, calque, EN-leftover + 4-col table-integrity (leaves).

**Critical review:** independent-review субагент 0 CRITICAL / 0 MAJOR / 1 MINOR (gcp-supported шаги: `необходимо` + императив -> `выполните следующие действия:`, исправлено). Мой скепт-проход: zeugma чисто (`без выделения серверов и управления ими`), em-dash=0. git status: EN не тронут, субагент не писал.

**Build-инфра урок:** сырой мойибейк (`U+00EF U+00BB U+00BF`, `U+00E2 U+0080 ..`) в Python-исходнике через Write-тул схлопывается (Windows). Фикс: `_MJ`/`MOJI` через `\\uXXXX`-escape, патчить файл Python-скриптом, не Write-тулом. RU-вывод писать `open(..., "wb")` (байты, LF, без trailing newline), markdown-форматтер тогда не трогает.

**Flag (вне scope батча):** `dynatrace-activegate/activegate-sfm-metrics.md` весь unit-столбец оставлен EN (Count/Byte/Millisecond/MebiByte), в отличие от GCP/Azure-канона (Unit переводится). Отдельное решение по этому файлу за пользователем.

"""
tp = open("TRANSLATION_PROGRESS.md", encoding="utf-8").read()
lines = tp.split("\n")
# insert after the first H1 title line (line 0) + its following blank
assert lines[0].startswith("# "), lines[0]
new = lines[0] + "\n\n" + SECTION + "\n".join(lines[1:]).lstrip("\n")
open("TRANSLATION_PROGRESS.md", "w", encoding="utf-8", newline="\n").write(new)
print("TRANSLATION_PROGRESS.md: prepended L4-IF.35 section")
print("em-dash in new section:", "—" in SECTION)
