---
title: OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline
scraped: 2026-03-06T21:10:24.659240
---

# OpenPipeline

# OpenPipeline

* Последняя версия Dynatrace
* Обзор
* Время чтения: 1 мин
* Обновлено 19 декабря 2025 г.

Dynatrace версии 1.295+

OpenPipeline --- это решение Dynatrace для обработки данных, обеспечивающее бесшовный прием и обработку данных из различных источников, любого масштаба и в любом формате в Dynatrace Platform.

## Сценарии использования

* Настройка приема и обработки данных для различных областей конфигурации, таких как логи и события, с помощью единого решения.
* Масштабирование управления данными между командами с контролем доступа и целевых технологий.
* Обеспечение безопасной и соответствующей требованиям обработки конфиденциальных данных.
* Обогащение и контекстуализация данных с помощью настраиваемой обработки.
* Оптимизация качества данных и контроль затрат.

## Концепции

[### Поток данных

[Узнайте, как данные проходят от приема до хранения через Dynatrace OpenPipeline.](openpipeline/concepts/data-flow.md "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")[### Обработка

[Изучите основные концепции обработки данных в Dynatrace OpenPipeline.](openpipeline/concepts/processing.md "Learn the core concepts of Dynatrace OpenPipeline processing.")

## Начало работы

[### Как принимать данные (события)

[Как настроить прием данных для области конфигурации в OpenPipeline.](openpipeline/getting-started/how-to-ingestion.md "How to ingest data for a configuration scope in OpenPipeline.")[### Настройка обработки

[Настройте источники приема, маршруты и обработку данных через OpenPipeline.](openpipeline/getting-started/tutorial-configure-processing.md "Configure ingest sources, routes, and processing for your data in OpenPipeline.")

### Примеры обработки

* [Снижение кардинальности на основе спанов и метрик](openpipeline/use-cases/reduce-span-metric-cardinality.md "Leverage three different views in the Services app to normalize span and metric data, ensuring aggregations and analysis remain reliable and usable.")
* [Примеры обработки в OpenPipeline](openpipeline/use-cases/processing-examples.md "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [Парсинг строк логов и извлечение метрик](openpipeline/use-cases/tutorial-log-processing-pipeline.md "Configure OpenPipeline processing for log lines.")
* [Извлечение метрик из спанов и распределенных трассировок](openpipeline/use-cases/tutorial-extract-metrics-from-spans.md "Extract metrics directly from your spans and distributed traces via OpenPipeline.")
* [Обработка логов с помощью парсеров технологических пакетов](openpipeline/use-cases/tutorial-technology-processor.md "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.")
* [Извлечение метрики для отслеживания системных событий](openpipeline/use-cases/tutorial-system-events.md "Learn how to extract a metric to track system events with OpenPipeline.")
* [Настройка управления приемом данных в мультиоблачной среде с помощью групп конвейеров](openpipeline/use-cases/pipeline-groups-multicloud.md "Configure pipeline groups via the Settings API to ensure consistent governance across multicloud deployments, restrict sensitive stages, and structure team responsibilities through mandatory and restricted pipelines.")
* [Извлечение метрики из пользовательских событий](../observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-events.md "Turn user events into actionable insights by extracting custom metrics for long-term analysis.")
* [Извлечение метрики из пользовательских сессий](../observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-sessions.md "Discover how to build custom metrics from user sessions, illustrated by a customer conversion metric.")

## Справочные материалы

[### API приема данных

[Справочные материалы по API приема данных для областей конфигурации, поддерживаемых OpenPipeline.](openpipeline/reference/api-ingestion-reference.md "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.")[### OpenPipeline API

[Справочные материалы по настройке через OpenPipeline API.](openpipeline/reference/openpipeline-api.md "Configure OpenPipeline capabilities of ingest source, routing, and processing via API.")[### Ограничения

[Справочные материалы по ограничениям OpenPipeline.](openpipeline/reference/limits.md "Reference limits of Dynatrace OpenPipeline.")
