---
title: Расширение наблюдаемости метрик
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics
scraped: 2026-05-12T11:37:59.140301
---

# Расширение наблюдаемости метрик

# Расширение наблюдаемости метрик

* 3-min read
* Updated on Mar 16, 2023

Dynatrace предоставляет несколько методов для приёма пользовательских метрик и расширения наблюдаемости.

## Data Explorer

Для визуализации метрик перейдите в **Observe and explore > Metrics** и откройте Data Explorer. В режиме Advanced mode используйте Metrics Selector для построения запросов.

## Потребление DDU

Приём пользовательских метрик потребляет Davis Data Units (DDU). Подробнее об управлении потреблением DDU см. в разделе [лицензирования](/managed/license "Узнайте об управлении лицензией Dynatrace.").

## Измерения и кортежи метрик

Каждая метрика может содержать измерения (dimensions), которые представляют собой пары «ключ-значение» для фильтрации и агрегации данных.

## Ограничения на приём метрик

| Параметр | Ограничение |
| --- | --- |
| Максимальное количество метрик на токен | 1000 |
| Максимальное количество измерений на метрику | 50 |
| Максимальная длина имени метрики | 250 символов |

## Методы приёма метрик

* [JMX-расширения](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Узнайте, как расширить мониторинг Dynatrace с помощью JMX.")
* [Micrometer](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Узнайте, как отправлять метрики Micrometer в Dynatrace.")
* [OneAgent Metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик.")
* [Скриптовая интеграция](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнайте, как принимать метрики с помощью локальной скриптовой интеграции.")
* [Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Расширьте наблюдаемость с помощью метрик Prometheus.")
* [StatsD](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Принимайте метрики StatsD в Dynatrace.")

## Связанные темы

* [Метаданные пользовательских метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Узнайте о параметрах метаданных метрик.")
* [Протокол приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте о протоколе приёма метрик.")