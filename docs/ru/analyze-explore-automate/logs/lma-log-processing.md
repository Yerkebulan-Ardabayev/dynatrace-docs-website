---
title: Log processing
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing
scraped: 2026-03-06T21:15:13.168025
---

# Обработка логов

# Обработка логов

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Dec 11, 2025

Dynatrace может преобразовывать входящие данные логов для лучшего понимания, анализа или дальнейшей трансформации.

Информация может записываться в самых разных форматах в зависимости от приложения, процесса, операционной системы и других факторов. Предварительная обработка и обработка логов с помощью OpenPipeline предоставляет централизованный и гибкий способ извлечения ценности из необработанных строк логов.

![Diagram - Steps of log processing](https://dt-cdn.net/images/lma-log-processing-with-openpipeline-v2-2500-0a3f3308e5.png)

Обработка логов включает следующие шаги.

### 1. Автоматическая обработка логов при приёме

Dynatrace обрабатывает логи при приёме, чтобы обеспечить готовность строк логов для автоматизации, устранения неполадок и анализа. Такой унифицированный подход позволяет переключаться между различными [стратегиями приёма логов](lma-log-ingestion.md "Stream log data to Dynatrace.") с нулевой или минимальной конфигурацией.

Автоматическая обработка логов при приёме включает извлечение временных меток, извлечение степени серьёзности и разбор полезной нагрузки лога.

Подробнее смотрите в разделе [Автоматическая обработка логов при приёме](lma-log-processing/lma-automatic-processing.md "Ingest and process logs automatically with OneAgent, Log Monitoring API v2, or Dynatrace OTLP API.").

### 2. Предварительная обработка с OpenPipeline

Dynatrace применяет предварительную обработку логов для обогащения, нормализации и подготовки данных логов к анализу. Благодаря такому структурированному подходу логи поддерживаемых технологий обогащаются без ручной настройки, имеют улучшенную структуру и метаданные и связаны со своими трассировками.

Предварительная обработка с OpenPipeline обеспечивает согласованную структуру логов, улучшенную возможность запросов и бесшовную интеграцию с функциями наблюдаемости Dynatrace.

Дополнительную информацию смотрите в разделе [Предварительная обработка логов с OpenPipeline с готовыми наборами](lma-log-processing/lma-pre-processing.md "Streamline log analysis by enriching and normalizing data using ready-made technology bundles for popular technologies before it enters OpenPipeline.").

### 3. Обработка логов с OpenPipeline

Обработка логов с OpenPipeline предполагает использование [решения OpenPipeline](../../platform/openpipeline.md "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") для обработки логов перед их сохранением в Grail. Этот шаг включает различные этапы, такие как обработка, извлечение метрик и данных, права доступа и хранение. Подробный обзор всех этапов смотрите в разделе [Обработка логов с OpenPipeline](lma-log-processing/lma-openpipeline.md "Process logs using Dynatrace OpenPipeline.").

Рекомендуется использовать обработку логов с OpenPipeline как масштабируемое и мощное решение для управления, обработки и анализа логов. Если у вас нет доступа к OpenPipeline, используйте [классический конвейер обработки логов](lma-classic-log-processing.md "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").

## Связанные темы

* [OpenPipeline](../../platform/openpipeline.md "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Поток данных в OpenPipeline](../../platform/openpipeline/concepts/data-flow.md "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Обработка в OpenPipeline](../../platform/openpipeline/concepts/processing.md "Learn the core concepts of Dynatrace OpenPipeline processing.")
