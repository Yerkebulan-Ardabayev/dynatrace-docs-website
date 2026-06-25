---
title: Источник данных Prometheus
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions
scraped: 2026-05-12T11:50:01.246339
---

# Источник данных Prometheus

# Источник данных Prometheus

* Справочник
* Чтение: 2 мин
* Обновлено 4 мая 2026 г.

Dynatrace предоставляет платформу для расширения наблюдаемости приложений и сервисов за счёт данных, получаемых непосредственно из Prometheus. Платформа расширений Dynatrace извлекает метрики Prometheus из эндпоинта `/metrics`, эндпоинта Prometheus API или экспортёра данных (Prometheus target).

Обратите внимание, что Dynatrace обеспечивает встроенную поддержку приёма метрик из [экспортёров Prometheus в Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Приём метрик из эндпоинтов Prometheus в Kubernetes, оповещения о метриках и потребление мониторинга.").

Расширения Prometheus можно запускать прямо на хосте Prometheus, где установлен OneAgent: в этом случае метрики автоматически обогащаются измерениями, специфичными для хоста. Если установить OneAgent на хосте Prometheus невозможно, расширения запускаются удалённо и выполняются на выбранной группе ActiveGate.

Предполагается следующее:

* Наличие достаточной экспертизы по [Prometheus](https://prometheus.io/) для создания расширения.
* Знакомство с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать YAML-файл расширения с помощью платформы Extensions.").

Обязательно ознакомьтесь со всеми предварительными требованиями и ограничениями.

## Поддерживаемые версии Dynatrace

* Dynatrace версии 1.225+
* ActiveGate окружения версии 1.225+
* OneAgent версии 1.225+ (локальные расширения)

## Ограничения

Сведения об ограничениях, применяемых к расширению, см. в разделе [Ограничения расширений](/managed/ingest-from/extensions/extension-limits "Узнайте об ограничениях расширений."), а также следующие ограничения, специфичные для Prometheus:

* Не более 1000 определений `metrics`
* Не более 50 измерений на метрику

Волатильные измерения

Большое количество измерений может превысить ограничения и негативно сказаться на производительности окружения Dynatrace. Учитывайте следующее:

* Метки Prometheus автоматически становятся измерениями Dynatrace.
* Некоторые метрики могут быть привязаны к измерениям с постоянно растущим набором значений, каждое из которых становится новым измерением.

Сведения о структуре YAML-файла расширения Prometheus и формате конфигурации мониторинга см. в [справочнике по источнику данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference "Узнайте о расширениях Prometheus в платформе Extensions.").

## Связанные темы

* [Сбор метрик Prometheus с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Настройте OpenTelemetry Collector для сбора данных Prometheus.")