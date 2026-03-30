---
title: Лицензирование OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/opentelemetry-licensing
scraped: 2026-03-06T21:23:28.479475
---

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

Полную информацию см. в разделе Обзор Traces powered by Grail (DPS).").

### Приём

Данные трассировки OpenTelemetry тарифицируются по объёму принятых данных.
Они тарифицируются как Traces - Ingest & Process.

Full-Stack Monitoring включает [определённый объём данных трассировки](../../license/capabilities/app-infra-observability/full-stack-monitoring.md#full-stack-traces "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.") для трассировок, отправленных через OneAgent Trace API или с хоста, отслеживаемого в режиме Full-Stack.
Вам тарифицируются только данные трассировки (из этих источников), превышающие включённый объём.

### Хранение

Хранение данных трассировки OpenTelemetry тарифицируется по объёму сохранённых данных трассировки.
Оно измеряется в гибибайтах в день (ГиБ-день) и тарифицируется как Traces - Retain.

[Период хранения данных трассировки по умолчанию -- 10 дней](../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md#purepath "Проверьте сроки хранения для различных типов данных.") -- включён.
Любые данные трассировки, сохранённые дольше 10 дней, тарифицируются по гибибайтам как [Traces - Retain](../../license/capabilities/traces.md#trace-retain-usage "Узнайте, как рассчитывается потребление Dynatrace Traces powered by Grail в модели Dynatrace Platform Subscription (DPS).").

### Запросы

Запросы трассировок OpenTelemetry тарифицируются по количеству отсканированных гибибайтов (ГиБ-сканировано) и тарифицируются как Traces - Query.

Использование [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](../../observe/application-observability/distributed-tracing.md "Трассировка и анализ в реальном времени высокораспределённых систем с Grail.") и [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](../../observe/application-observability/services/services-app.md "Централизованное управление состоянием, производительностью и ресурсами сервисов с помощью приложения Services.") включено в Dynatrace.
Эти приложения не генерируют потребление запросов.

## Metrics powered by Grail (DPS)

Dynatrace поддерживает метрики OpenTelemetry, позволяя бесшовно принимать и анализировать данные OpenTelemetry наряду с метриками из сред, отслеживаемых Dynatrace.
Метрики OpenTelemetry тарифицируются как Metrics powered by Grail, так же как и другие принятые метрики.

Полную информацию см. в разделе Обзор Metrics powered by Grail (DPS).

### Приём

Метрики OpenTelemetry тарифицируются по количеству принятых точек данных метрик, измеряемых группами по 100 000 точек данных.
Этот приём тарифицируется как Metrics - Ingest & Process.

Метрики, поступающие с хостов или контейнеров, отслеживаемых в режиме Full-Stack, [включают определённое количество точек данных метрик](../../license/capabilities/app-infra-observability/full-stack-monitoring.md#dps-included-metrics "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.").
Каждый гибибайт памяти хоста или приложения добавляет 900 точек данных в каждом 15-минутном интервале.

В среде с Full-Stack Monitoring вам тарифицируются только точки данных метрик, превышающие этот лимит.

### Хранение

Хранение метрик OpenTelemetry тарифицируется по объёму сохранённых данных метрик.
Оно измеряется в гибибайтах в день (ГиБ-день) и тарифицируется как Metrics - Retain.

Metrics powered by Grail включает 15 месяцев (462 дня) хранения с минутной гранулярностью.
Метрики, которые вы решите хранить дольше этого периода, тарифицируются.

### Запросы

Запросы данных метрик включены в Metrics - Ingest & Process.

## Logs powered by Grail (DPS)

Dynatrace обеспечивает полную поддержку логов OpenTelemetry.
Это позволяет централизовать данные логов из источников OpenTelemetry наряду с логами из сред, отслеживаемых Dynatrace. Логи OpenTelemetry тарифицируются как Logs powered by Grail.

Полную информацию см. в разделе Log Analytics (DPS).

### Приём

Данные логов OpenTelemetry тарифицируются по принятому объёму.
Он измеряется в гибибайтах (ГиБ) и тарифицируется как Log Management & Analytics - Ingest & Process.

### Хранение

Хранение данных логов тарифицируется по объёму сохранённых данных логов.
Оно измеряется в гибибайтах в день (ГиБ-день) и тарифицируется как Log Management & Analytics - Retain.

### Запросы

Запросы данных логов тарифицируются по объёму запрошенных данных логов.
Он измеряется в гибибайтах сканированных (ГиБ-сканировано) и тарифицируется как Log Management & Analytics - Query.

## Отслеживание потребления

Dynatrace предоставляет различные способы отслеживания приёма данных OpenTelemetry.
Они описаны на соответствующей странице возможности DPS:

* Готовые ноутбуки для отслеживания приёма трассировок
* Встроенные метрики для отслеживания приёма логов
* Расчёты для отслеживания приёма метрик

## Связанные темы

* OpenTelemetry и Dynatrace в Dynatrace.")
* Log Analytics (DPS)
* Обзор Traces powered by Grail (DPS).")
* Обзор Metrics powered by Grail (DPS)
