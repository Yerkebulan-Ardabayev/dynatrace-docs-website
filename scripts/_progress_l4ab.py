# -*- coding: utf-8 -*-
"""One-shot: record L4-AB in TRANSLATION_PROGRESS.md (giant-line safe).
Prepends L4-AB canon to the header line, demotes L4-AA to ИСТОРИЯ,
updates corpus counts, inserts the Status-table row. Idempotent-guarded."""

import io

P = "TRANSLATION_PROGRESS.md"
L = io.open(P, encoding="utf-8").read().split("\n")

if "**L4-AB configuration-api/service-api/ остаток" in L[3]:
    print("already recorded; abort")
    raise SystemExit(0)

L4AB = (
    "**L4-AB configuration-api/service-api/ остаток = 49ф "
    "(service-api.md parent + custom-services-api/ 7 + detection-rules/ 26 "
    "[parent + models.md 1756 + 4 rule-type families ×6: full-web-request/"
    "full-web-service/opaque-web-request/opaque-web-service] + "
    "failure-detection/ 15 [parent + json-models.md 1318 + detection-rules ×7 "
    "+ parameter-set ×6]) ЗАКРЫТ → **service-api/ subsection 100% ЦЕЛИКОМ** "
    "(L4-AA 14 + L4-AB 49 = 63ф). ~15.2K EN-строк. **АКТИВНЫЙ API** L89/L90 "
    "(без `* Deprecated`, `* Reference`/`* Published <date>`/title/H1×2 "
    "EN-verbatim, line-parity EXACT EN==RU). anchor = L4-AA service-api "
    "R-table reused verbatim (~90% shared: ВСЕ `#### The X object`-headings, "
    "*ComparisonInfo/*Dto, Condition/Placeholder/PropagationSource/"
    "UniversalTag/TagInfo/Error*/ErrorEnvelope/ConstraintViolation/StubList/"
    "EntityShortRep/ConfigMeta, L99 phrases, ## Authentication/Parameters/"
    "Response headings, response-code cells, table headers, k8s/config "
    "L4M/L4U). **4 rule-type families ~85% twin** (84 diff-строк после "
    "rule-type-token нормализации) → twin-splice IMPLICIT через общую "
    "R-table (identical EN→identical RU, L4Z/L4W метод в 2.3× масштабе "
    "49ф/4-family). **L101 MIXED period в ОДНОМ subsection**: `Failed. The "
    "input is invalid` БЕЗ точки (5×) И С точкой (39×) → substring "
    '`("Failed. The input is invalid","Сбой. Невалидный ввод")` сохраняет '
    "точку источника per-cell АВТО (L4X#3 4-й раз — грепать EN-ячейку, "
    "mixed OK). json-models structure L3G (`### TYPE`-headings/`Parameters`/"
    "`JSON model` tab-labels EN) + `Возможные значения:` двоеточие L4O/L99 "
    "(НЕ «Элемент может принимать»). **Link-text 3 правила**: (a) "
    "descriptive nav-bullet (service-api.md/detection-rules.md "
    "`[Полные веб-запросы]`/`[Создание вычисляемой метрики сервиса]`) "
    "ПЕРЕВЕДЕНО L4Y#4; (b) doc-ref cross-ref `[Service detection API - "
    "JSON models]`/`[Failure detection API - JSON models]`(`dt-url.net`) "
    "EN-verbatim (target не RU, canon-d/L4Y#5, surrounding-prose переведена, "
    "3-char BOM `ï»¿` strip L4M); (c) `[запрос на изменение порядка]` "
    "reorder-embedding link-text ПЕРЕВЁДЕН L4Y#4, title-attr RU. Anomalous "
    "endpoint `## PUT a custom service rule` H2 (custom-services-api/"
    "put-rule.md) EN-verbatim (L99/L4T endpoint-name-as-heading; corpus 0 "
    "`## VERB`-headings — source-quirk зеркалить L93). Splice "
    "`scripts/_build_serviceapi_ab.py` (L4-AA R reused + **86 new entries**: "
    "TIER-0d FD-embedding-intros/8 service-detection-body-cells/card-descr/"
    "attribute-cell-prefixes/12 json-models-condition-forms + 44 nav-bullet "
    "link-text bracket-anchored) + критич.ревью "
    "`scripts/_review_serviceapi_ab.py` (копия `_review_serviceapi.py` + "
    "**NEW [LATIN-RUN] defect-класс ПОРТИРОВАН из `scripts/_latinscan_ab.py`"
    "** — generic stripped-Latin-run net hard-gated В harness: "
    "L4Y#3 структурно закреплён). **Критический ревью (orchestrator "
    "mandatory)**: build-pass-1 review 0 структурных деф НО независимый "
    "orchestrator generic-LATIN-RUN net поймал **СИСТЕМНЫЙ leftover-EN "
    "класс на 18ф** (ВСЕ 4 rule-type families + failure-detection + "
    "custom-services + models.md + service-api.md 40+ nav-link-text): "
    "inherited L4-AA SUSPECT покрывал только request-attributes/naming "
    "vocab, detection-rules cell-vocab НЕ покрыт "
    "(**structural-green≠semantic 6-й раз**: L4N/L4P/L4T/L4W/L4Y/L4-AB). "
    "Fix WHOLE class (grep-audit все family/verb twins НЕ только flagged): "
    "86 R-entries + LATIN-RUN портирован в review. 3 build/review-iter "
    "этого раунда (36→11→1→0 деф). Финал independently re-verified: review "
    "[OK] 0 деф (incl LATIN-RUN=0), `_latinscan_ab.py` 94 flags ВСЕ EN-lock "
    "(orchestrator triaged: doc-ref link-text 42 + object/enum/type-names "
    "51 + endpoint-H2 1, 0 leftover-prose; `Service detection API - JSON "
    "models` подтверждён genuine markdown cross-ref `[X](dt-url.net)` с "
    "переведённой surrounding-prose, corpus-precedent L4-AA "
    "`[Service metrics API - JSON models]` идентичен), line-parity EXACT "
    "49/49, em-dash global 0 (63ф), Orphan RU 0, diff +49 (1650→1699, "
    "pending 1005→956, dynatrace-api 687→736/419→370). **Lesson L4-AB:** "
    "(1) **reused-curated-SUSPECT под NEW vocab-domain под-покрывает → "
    "generic LATIN-RUN net ОБЯЗАН быть В review-harness, НЕ optional "
    "orchestrator-step (L4Y#3 эскалирован: портировать [LATIN-RUN] в "
    "`_review_*`, structural-gate каждый batch с новым доменом)**; "
    "(2) systematic leftover-class охватывает ВСЕ family/verb twins не "
    "только flagged-file → fix WHOLE class через grep-audit; "
    "(3) doc-ref cross-ref link-text `[<API> - JSON models]` EN-verbatim "
    "где target не RU, surrounding-prose переведена (canon-d/L4Y#5 "
    "подтверждён); (4) descriptive nav-bullet link-text ПЕРЕВОД ≠ "
    "doc-ref/Related cross-ref EN — 2 правила L4Y#4; (5) anomalous "
    "endpoint `## VERB` H2 = EN-verbatim L99/L4T (corpus 0 `## VERB` — "
    "source-quirk зеркалить L93); (6) L101 mixed-period в ОДНОМ subsection "
    "OK — substring сохраняет точку источника per-cell (L4X#3 4-й раз); "
    "(7) twin-splice масштаб 49ф/4-family ~85% (L4Z в 2.3×, implicit "
    "R-table). ИСТОРИЯ L4-AA ниже:** "
)

# 1) header line: counts + prepend L4-AB, demote L4-AA
L[3] = L[3].replace(
    "(Opus +14 = **1650/2655 = 62.15%**, pending 1005, Orphan RU 0, "
    "dynatrace-api 687 done/419 pending;",
    "(Opus +49 = **1699/2655 = 64.00%**, pending 956, Orphan RU 0, "
    "dynatrace-api 736 done/370 pending;",
)
L[3] = L[3].replace(
    "**L4-AA configuration-api/service-api/ partial = 14ф",
    L4AB + "**L4-AA configuration-api/service-api/ partial = 14ф",
    1,
)

# 2) corpus count lines
L[5] = (
    L[5]
    .replace("1650 RU files", "1699 RU files")
    .replace("(после L4-AA;", "(после L4-AB;")
)
L[6] = "Translated: **1699 файлов** (EN AND RU), **64.00%**"
L[7] = "Remaining: **956 файлов**"

# 3) Status-table row after the L4-AA row
ROW = (
    "| L4-AB | configuration-api/service-api/ остаток "
    "(service-api.md + custom-services-api/ 7 + detection-rules/ 26 + "
    "failure-detection/ 15) ЗАКРЫТ → service-api/ subsection 100% ЦЕЛИКОМ "
    "(L4-AA 14 + L4-AB 49 = 63ф); АКТИВНЫЙ; twin-splice 4 rule-type "
    "families; критич.ревью поймал системный leftover-EN на 18ф (fixed, "
    "86 R-entries); [LATIN-RUN] net портирован в review-harness | "
    "49 | 49 | ✅ done |"
)
for i, ln in enumerate(L):
    if ln.startswith("| L4-AA | configuration-api/service-api/ partial"):
        L.insert(i + 1, ROW)
        break

io.open(P, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print("L4-AB recorded in TRANSLATION_PROGRESS.md")
