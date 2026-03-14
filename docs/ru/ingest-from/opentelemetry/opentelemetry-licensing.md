---
title: Лицензирование OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/opentelemetry-licensing
scraped: 2026-03-06T21:23:28.479475
---

# Лицензирование OpenTelemetry


* Последняя версия Dynatrace
* Обзор
* Чтение: 2 минуты
* Опубликовано 25 августа 2025 г.

Последняя версия Dynatrace

Узнайте, как рассчитывается приём данных OpenTelemetry в модели лицензирования Dynatrace Platform Subscription (DPS).

## Обзор

Dynatrace обеспечивает бесшовную поддержку приёма и обработки данных OpenTelemetry.
Это позволяет использовать возможности наблюдаемости в ваших распределённых системах.

Лицензирование данных OpenTelemetry полностью интегрировано в модель Dynatrace Platform Subscription, обеспечивая прозрачную и последовательную тарификацию всех типов телеметрии (трассировки и спаны, метрики и логи).

С Dynatrace данные OpenTelemetry обрабатываются так же, как и любые другие принятые данные.
Гибкое ценообразование основано на объёме принятых, сохранённых и запрошенных данных.
Расчёт цен использует те же [позиции тарифной карты](https://www.dynatrace.com/pricing/), что и для всех телеметрических данных, поступающих на платформу.

## Traces powered by Grail (DPS)

Dynatrace позволяет бесшовно принимать и анализировать данные трассировки OpenTelemetry.

Полную информацию см. в разделе [Обзор Traces powered by Grail (DPS)](../../license/capabilities/traces.md "Узнайте, как рассчитывается потребление Dynatrace Traces powered by Grail в модели Dynatrace Platform Subscription (DPS).").

### Приём

Данные трассировки OpenTelemetry тарифицируются по объёму принятых данных.
Они тарифицируются как [Traces - Ingest & Process](../../license/capabilities/traces/dps-traces-ingest.md "Узнайте, как рассчитывается потребление возможности Traces - Ingest & Process DPS.").

Full-Stack Monitoring включает [определённый объём данных трассировки](../../license/capabilities/app-infra-observability/full-stack-monitoring.md#full-stack-traces "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.") для трассировок, отправленных через OneAgent Trace API или с хоста, отслеживаемого в режиме Full-Stack.
Вам тарифицируются только данные трассировки (из этих источников), превышающие включённый объём.

### Хранение

Хранение данных трассировки OpenTelemetry тарифицируется по объёму сохранённых данных трассировки.
Оно измеряется в гибибайтах в день (ГиБ-день) и тарифицируется как [Traces - Retain](../../license/capabilities/traces/dps-traces-retain.md "Узнайте, как рассчитывается потребление возможности Traces - Retain DPS.").

[Период хранения данных трассировки по умолчанию -- 10 дней](../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md#purepath "Проверьте сроки хранения для различных типов данных.") -- включён.
Любые данные трассировки, сохранённые дольше 10 дней, тарифицируются по гибибайтам как [Traces - Retain](../../license/capabilities/traces.md#trace-retain-usage "Узнайте, как рассчитывается потребление Dynatrace Traces powered by Grail в модели Dynatrace Platform Subscription (DPS).").

### Запросы

Запросы трассировок OpenTelemetry тарифицируются по количеству отсканированных гибибайтов (ГиБ-сканировано) и тарифицируются как [Traces - Query](../../license/capabilities/traces/dps-traces-query.md "Узнайте, как рассчитывается потребление возможности Traces - Query DPS.").

Использование [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](../../observe/application-observability/distributed-tracing.md "Трассировка и анализ в реальном времени высокораспределённых систем с Grail.") и [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](../../observe/application-observability/services/services-app.md "Централизованное управление состоянием, производительностью и ресурсами сервисов с помощью приложения Services.") включено в Dynatrace.
Эти приложения не генерируют потребление запросов.

## Metrics powered by Grail (DPS)

Dynatrace поддерживает метрики OpenTelemetry, позволяя бесшовно принимать и анализировать данные OpenTelemetry наряду с метриками из сред, отслеживаемых Dynatrace.
Метрики OpenTelemetry тарифицируются как Metrics powered by Grail, так же как и другие принятые метрики.

Полную информацию см. в разделе [Обзор Metrics powered by Grail (DPS)](../../license/capabilities/metrics.md "Узнайте, как рассчитывается потребление Dynatrace Metrics powered by Grail в модели Dynatrace Platform Subscription.").

### Приём

Метрики OpenTelemetry тарифицируются по количеству принятых точек данных метрик, измеряемых группами по 100 000 точек данных.
Этот приём тарифицируется как [Metrics - Ingest & Process](../../license/capabilities/metrics/dps-metrics-ingest.md "Узнайте, как рассчитывается потребление возможности Metrics - Ingest & Process DPS.").

Метрики, поступающие с хостов или контейнеров, отслеживаемых в режиме Full-Stack, [включают определённое количество точек данных метрик](../../license/capabilities/app-infra-observability/full-stack-monitoring.md#dps-included-metrics "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.").
Каждый гибибайт памяти хоста или приложения добавляет 900 точек данных в каждом 15-минутном интервале.

В среде с Full-Stack Monitoring вам тарифицируются только точки данных метрик, превышающие этот лимит.

### Хранение

Хранение метрик OpenTelemetry тарифицируется по объёму сохранённых данных метрик.
Оно измеряется в гибибайтах в день (ГиБ-день) и тарифицируется как [Metrics - Retain](../../license/capabilities/metrics/dps-metrics-retain.md "Узнайте, как рассчитывается потребление возможности Metrics - Retain DPS.").

Metrics powered by Grail включает [15 месяцев (462 дня) хранения с минутной гранулярностью](../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md "Проверьте сроки хранения для различных типов данных.").
Метрики, которые вы решите хранить дольше этого периода, тарифицируются.

### Запросы

Запросы данных метрик включены в [Metrics - Ingest & Process](../../license/capabilities/metrics/dps-metrics-ingest.md "Узнайте, как рассчитывается потребление возможности Metrics - Ingest & Process DPS.").

## Logs powered by Grail (DPS)

Dynatrace обеспечивает полную поддержку логов OpenTelemetry.
Это позволяет централизовать данные логов из источников OpenTelemetry наряду с логами из сред, отслеживаемых Dynatrace. Логи OpenTelemetry тарифицируются как Logs powered by Grail.

Полную информацию см. в разделе [Log Analytics (DPS)](../../license/capabilities/log-analytics.md "Узнайте, как рассчитывается потребление Dynatrace Log Analytics в модели Dynatrace Platform Subscription.").

### Приём

Данные логов OpenTelemetry тарифицируются по принятому объёму.
Он измеряется в гибибайтах (ГиБ) и тарифицируется как [Log Management & Analytics - Ingest & Process](../../license/capabilities/log-analytics/dps-log-ingest.md "Узнайте, как рассчитывается потребление возможности Log Management & Analytics - Ingest & Process DPS.").

### Хранение

Хранение данных логов тарифицируется по объёму сохранённых данных логов.
Оно измеряется в гибибайтах в день (ГиБ-день) и тарифицируется как [Log Management & Analytics - Retain](../../license/capabilities/log-analytics/dps-log-retain.md "Узнайте, как рассчитывается потребление возможности Log Management & Analytics - Retain DPS.").

### Запросы

Запросы данных логов тарифицируются по объёму запрошенных данных логов.
Он измеряется в гибибайтах сканированных (ГиБ-сканировано) и тарифицируется как [Log Management & Analytics - Query](../../license/capabilities/log-analytics/dps-log-query.md "Узнайте, как рассчитывается потребление возможности Log Management & Analytics - Query DPS.").

## Отслеживание потребления

Dynatrace предоставляет различные способы отслеживания приёма данных OpenTelemetry.
Они описаны на соответствующей странице возможности DPS:

* [Готовые ноутбуки для отслеживания приёма трассировок](../../license/capabilities/traces/dps-traces-ingest.md#consumption-trace-ingest "Узнайте, как рассчитывается потребление возможности Traces - Ingest & Process DPS.")
* [Встроенные метрики для отслеживания приёма логов](../../license/capabilities/log-analytics/dps-log-ingest.md#track-your-consumption "Узнайте, как рассчитывается потребление возможности Log Management & Analytics - Ingest & Process DPS.")
* [Расчёты для отслеживания приёма метрик](../../license/capabilities/metrics/dps-metrics-ingest.md#calculate-your-consumption "Узнайте, как рассчитывается потребление возможности Metrics - Ingest & Process DPS.")

## Связанные темы

* [OpenTelemetry и Dynatrace](../opentelemetry.md "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.")
* [Log Analytics (DPS)](../../license/capabilities/log-analytics.md "Узнайте, как рассчитывается потребление Dynatrace Log Analytics в модели Dynatrace Platform Subscription.")
* [Обзор Traces powered by Grail (DPS)](../../license/capabilities/traces.md "Узнайте, как рассчитывается потребление Dynatrace Traces powered by Grail в модели Dynatrace Platform Subscription (DPS).")
* [Обзор Metrics powered by Grail (DPS)](../../license/capabilities/metrics.md "Узнайте, как рассчитывается потребление Dynatrace Metrics powered by Grail в модели Dynatrace Platform Subscription.")
