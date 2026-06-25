# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../data-sources/prometheus-extensions.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources"

TRANS = {
    "* Reference": "* Справочник",
    "* 2-min read": "* Чтение: 2 мин",
    "* Updated on May 04, 2026": "* Обновлено 4 мая 2026 г.",
    "Dynatrace provides you with a framework that you can use to extend your application and services observability into data acquired directly from Prometheus. The Dynatrace extensions framework can pull Prometheus metrics from the `/metrics` endpoint, a Prometheus API endpoint, or a data exporter (Prometheus target).": "Dynatrace предоставляет платформу для расширения наблюдаемости приложений и сервисов за счёт данных, получаемых непосредственно из Prometheus. Платформа расширений Dynatrace извлекает метрики Prometheus из эндпоинта `/metrics`, эндпоинта Prometheus API или экспортёра данных (Prometheus target).",
    'Note that Dynatrace provides out-of-the-box support for ingesting metrics from [Prometheus exporters in Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").': 'Обратите внимание, что Dynatrace обеспечивает встроенную поддержку приёма метрик из [экспортёров Prometheus в Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Приём метрик из эндпоинтов Prometheus в Kubernetes, оповещения о метриках и потребление мониторинга.").',
    "You can run Prometheus extensions right on the Prometheus host where you installed OneAgent, so your metrics are automatically enriched with host-specific dimensions. If, however, you can't install OneAgent on the Prometheus host, you can run extensions remotely and execute them on an ActiveGate group of your choice.": "Расширения Prometheus можно запускать прямо на хосте Prometheus, где установлен OneAgent: в этом случае метрики автоматически обогащаются измерениями, специфичными для хоста. Если установить OneAgent на хосте Prometheus невозможно, расширения запускаются удалённо и выполняются на выбранной группе ActiveGate.",
    "We assume the following:": "Предполагается следующее:",
    "* You possess sufficient [Prometheus](https://prometheus.io/) subject matter expertise to create an extension.": "* Наличие достаточной экспертизы по [Prometheus](https://prometheus.io/) для создания расширения.",
    '* You\'re familiar with [Extensions basic concepts](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").': '* Знакомство с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать YAML-файл расширения с помощью платформы Extensions.").',
    "Be sure to review all prerequisites and limits.": "Обязательно ознакомьтесь со всеми предварительными требованиями и ограничениями.",
    "## Supported Dynatrace versions": "## Поддерживаемые версии Dynatrace",
    "* Dynatrace version 1.225+": "* Dynatrace версии 1.225+",
    "* Environment ActiveGate version 1.225+": "* ActiveGate окружения версии 1.225+",
    "* OneAgent version 1.225+ (local extensions)": "* OneAgent версии 1.225+ (локальные расширения)",
    "## Limits": "## Ограничения",
    'For limits applying to your extension, see [Extensions limits](/managed/ingest-from/extensions/extension-limits "Learn about extensions limits.") and the following Prometheus-specific limits:': 'Сведения об ограничениях, применяемых к расширению, см. в разделе [Ограничения расширений](/managed/ingest-from/extensions/extension-limits "Узнайте об ограничениях расширений."), а также следующие ограничения, специфичные для Prometheus:',
    "* Maximum 1,000 `metrics` definitions": "* Не более 1000 определений `metrics`",
    "* Maximum 50 dimensions per metric": "* Не более 50 измерений на метрику",
    "Volatile dimensions": "Волатильные измерения",
    "Note that a large number of dimensions can exceed the limits and impact your Dynatrace environment performance beyond its capacity. Consider that:": "Большое количество измерений может превысить ограничения и негативно сказаться на производительности окружения Dynatrace. Учитывайте следующее:",
    "* Prometheus labels automatically become Dynatrace dimensions.": "* Метки Prometheus автоматически становятся измерениями Dynatrace.",
    "* Certain metrics can be assigned to dimensions with a constantly increasing set of values, each of them becoming a new dimension.": "* Некоторые метрики могут быть привязаны к измерениям с постоянно растущим набором значений, каждое из которых становится новым измерением.",
    'See [Prometheus data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference "Learn about Prometheus extensions in the Extensions framework.") to learn about the structure of the Prometheus extension YAML file and monitoring configuration format.': 'Сведения о структуре YAML-файла расширения Prometheus и формате конфигурации мониторинга см. в [справочнике по источнику данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference "Узнайте о расширениях Prometheus в платформе Extensions.").',
    "## Related topics": "## Связанные темы",
    '* [Scrape Prometheus metrics with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.")': '* [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора данных Prometheus.")',
}

PASS = {
    "title: Prometheus data source",
    "# Prometheus data source",
}

if __name__ == "__main__":
    build_one(REL, "prometheus-extensions.md", TRANS, PASS)
    qa_one(REL, "prometheus-extensions.md")
