# -*- coding: utf-8 -*-
"""L4-IF.73 — apply the independent-review findings that were verified against
EN source + corpus norm (item 14). File-scoped exact replacements (idempotent).

Each fix below was confirmed real; reviewer false-positives were rejected:
  REJECTED (kept as-is): otel-dotnet "## ASP.NET core integration" heading (2
  inbound #anchor refs + shipped dotnet.md keeps ### Setup/### Add tracing EN);
  vmss "site extension" (EN source literally says it — faithful per CLAUDE.md §3);
  L182 "мониторятся" (corpus-accepted, 18x).

Run from repo root:  python scripts/_apply_review_fixes_azure.py
"""

import os

RU = os.path.join(os.path.dirname(__file__), "..", "docs", "managed-ru")
AZ = "ingest-from/microsoft-azure-services"

FIXES = {
    AZ + "/azure-platform/azure-native-integration.md": [
        # mistranslation: EN "selected Virtual Machine" (x2), not App Service
        (
            "для выбранного App Service отобразится",
            "для выбранной виртуальной машины отобразится",
        ),
        # doc-type: EN "Explanation" -> "Пояснение" (corpus norm), not "Концепция"
        ("* Концепция", "* Пояснение"),
        # zeugma: создавать/использовать need accusative, управлять instrumental
        (
            "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.",
            "Узнайте, как создавать Dynatrace Dashboards Classic, управлять ими и использовать их.",
        ),
        # UI-icon tooltip norm: corpus keeps EN (Edit 16:2, Expand row 19:6)
        ('"Редактировать")', '"Edit")'),
        ("![Развернуть строку](", "![Expand row]("),
        ('"Развернуть строку")', '"Expand row")'),
        # register: "20 entries" -> записей, not colloquial "штук"
        ("составляет по 20 штук.", "составляет по 20 записей."),
    ],
    AZ
    + "/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet.md": [
        # EN compound noun order: "baggage propagator", not inverted
        ("Также включается propagator baggage", "Также включается baggage propagator"),
    ],
    AZ
    + "/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service.md": [
        # gender agreement: пример (m) -> приведённый
        (
            "приведённая ниже пример конфигурации является",
            "приведённый ниже пример конфигурации является",
        ),
    ],
    AZ + "/azure-integrations/azure-monitoring-guide.md": [
        # zeugma: создавать/активировать accusative, управлять instrumental
        (
            "Можно создавать, активировать и управлять несколькими подключениями мониторинга.",
            "Можно создавать и активировать несколько подключений мониторинга, а также управлять ими.",
        ),
        # glossary: keep "log forwarding" EN (batch norm) + logs->журналов
        (
            "Используйте пересылку логов Azure для приёма логов Azure.",
            "Используйте Azure log forwarding для приёма журналов Azure.",
        ),
        # idiom: рекомендации ПО настройке (not О настройке)
        (
            "рекомендациями о [настройке Azure service principal",
            "рекомендациями по [настройке Azure service principal",
        ),
    ],
    AZ + "/azure-integrations/set-up-log-forwarder-azure.md": [
        # calque "Вы ... выполнили" -> impersonal passive
        (
            "Вы тщательно выполнили шаги по [настройке параметров диагностики]",
            "Тщательно выполнены шаги по [настройке параметров диагностики]",
        ),
    ],
}


def main():
    total = 0
    for rel, pairs in FIXES.items():
        p = os.path.join(RU, rel)
        with open(p, encoding="utf-8", newline="") as f:
            t = f.read().replace("\r\n", "\n").replace("\r", "\n")
        n = 0
        for old, new in pairs:
            c = t.count(old)
            if c == 0 and new not in t:
                print("  WARN no match: %s :: %r" % (rel.split("/")[-1], old[:50]))
            t = t.replace(old, new)
            n += c
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
        print("  %3d  %s" % (n, rel.split("/")[-1]))
        total += n
    print("\nTOTAL: %d replacements" % total)


if __name__ == "__main__":
    main()
