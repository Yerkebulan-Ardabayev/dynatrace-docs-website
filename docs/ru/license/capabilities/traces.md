---
title: Обзор Traces на базе Grail (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/traces
scraped: 2026-03-06T21:13:53.688477
---

# Обзор Traces powered by Grail (DPS)


Возможность Traces powered by Grail DPS предоставляет клиентам доступ к:

* Приёму распределённых трассировок для OpenTelemetry через OTLP API.
* Приёму распределённых трассировок для бессерверных функций.
* Расширенному приёму трассировок для [Full-Stack Monitoring](app-infra-observability.md "Узнайте о различных вариантах Application & Infrastructure Observability, доступных с лицензией Dynatrace Platform Subscription (DPS).") сверх [включённого объёма данных трассировки](app-infra-observability/full-stack-monitoring.md#full-stack-traces "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.").
* Расширенному хранению данных трассировки до 10 лет.
* Расширенной аналитике трассировки в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** и через API.

На этой странице описаны различные возможности трассировки и функции, которые они предоставляют в рамках подписки DPS.

Информацию о том, как использование конкретной возможности переводится в потребление вашего обязательства по лицензии DPS, см. в

* [Traces - Ingest & Process](traces/dps-traces-ingest.md "Узнайте, как рассчитывается потребление возможности Traces - Ingest & Process DPS.")
* [Traces - Retain](traces/dps-traces-retain.md "Узнайте, как рассчитывается потребление возможности Traces - Retain DPS.")
* [Traces - Query](traces/dps-traces-query.md "Узнайте, как рассчитывается потребление возможности Traces - Query DPS.")

## Обзор функции Traces - Ingest

Ingest & Process заменяет расширения платформы [Custom Traces Classic](platform-extensions/custom-traces-classic.md "Узнайте, как рассчитывается потребление возможности Dynatrace Custom Traces Classic DPS.") и [Serverless Functions Classic](platform-extensions/serverless-functions-classic.md "Узнайте, как рассчитывается потребление возможности Dynatrace Serverless Functions Classic DPS.").
Их нельзя использовать одновременно.

Потребление Ingest & Process возникает, когда:

| Концепция | Описание |
| --- | --- |
| Приём данных | Данные распределённых трассировок, поступающие из следующих источников, тарифицируются как [Ingest & Process](#trace-ingest-usage):  - Через OpenTelemetry [OTLP Trace Ingest API](../../ingest-from/opentelemetry/otlp-api.md "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") из источников, не относящихся к Full-Stack. - Через [бессерверные функции](../../discover-dynatrace/get-started/serverless-monitoring.md "Наблюдаемость бессерверных функций с Dynatrace"). - Расширенный приём трассировок для [Full-Stack Monitoring](app-infra-observability/full-stack-monitoring.md "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.") (если клиент [явно запрашивает расширенный приём трассировок](app-infra-observability/full-stack-monitoring.md#extend-trace-ingest "Узнайте, как рассчитывается потребление возможности Dynatrace Full-Stack Monitoring DPS.")).  Обогащение спанов дополнительными метаданными на источнике, например [метаданными Kubernetes](../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Руководства по обогащению телеметрии в Kubernetes"), увеличивает размер принятых данных, тарифицируемых как [Ingest & Process](#trace-ingest-usage). |
| Обработка данных через OpenPipeline | - Обработка данных через OpenPipeline включена в [Traces - Ingest & Process](#trace-ingest-usage). Однако она увеличивает размер данных спанов, тарифицируемых как [Traces - Retain](#trace-retain-usage). - Обогащение топологии на основе сущностей Dynatrace (типы сущностей `dt.entity.*`) не увеличивает тарифицируемый размер спана или потребление [Traces - Ingest & Process](#trace-ingest-usage). - Пользовательские метрики создаются из данных спанов и тарифицируются как [Metrics - Ingest & Process](metrics/dps-metrics-ingest.md "Узнайте, как рассчитывается потребление возможности Metrics - Ingest & Process DPS."). Это ключи метрик Grail, поэтому они доступны только в последней версии Dynatrace. |

Dynatrace оставляет за собой право работать с клиентами для настройки или отключения правил парсинга, процессоров или конвейеров, которые испытывают деградацию сервиса.

## Обзор функции Traces - Retain

Потребление Retain возникает, когда:

| Концепция | Описание |
| --- | --- |
| Доступность данных | Сохранённые данные доступны для анализа и запросов до конца периода хранения (с ограничениями, описанными в примечании ниже этой таблицы). |
| Период хранения | Выберите желаемый период хранения. Для данных трассировки доступный [период хранения](../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md "Проверьте сроки хранения для различных типов данных.") составляет от 10 дней до 10 лет. Хранение трассировок определяется на уровне бакета, что позволяет настраивать периоды хранения для конкретных трассировок. Расчёт хранения не зависит от источника приёма трассировки, будь то Full-Stack, Mainframe или Ingest & Process. Первые 10 дней хранения всегда включены. |
| Обогащение топологии | Спаны обогащаются и обрабатываются в OpenPipeline. Обогащённые данные (включая обогащение топологии и обработку данных, как описано в [Ingest & Process](#trace-ingest-usage)) являются основой для потребления Retain для данных, которые хранятся более 10 включённых дней. |
| Обработка данных | Сервисы, эндпоинты и сбои обнаруживаются на основе данных спанов. |
| Управление хранением данных | Спаны фильтруются или исключаются на основе содержимого, топологии или метаданных. Они маршрутизируются в выделенный бакет. |

Для Traces - Retain доступность данных в определённых приложениях ограничена:

* ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** предоставляет доступ только к первым 10 дням сохранённых данных.
  Это приложение заменяется на ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
* ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** предоставляет доступ только к первым 10 дням сохранённых данных.
  Это приложение будет заменено на ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
* ![Multidimensional Analysis](https://dt-cdn.net/images/multidimensional-analysis-512-3aed148cfe.png "Multidimensional Analysis") **Multidimensional Analysis** предоставляет доступ только к первым 35 дням сохранённых данных.
  Это приложение будет заменено на ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

## Обзор функции Traces - Query

Потребление Query возникает, когда:

| Концепция | Описание |
| --- | --- |
| Выполнение DQL-запросов | [DQL-запрос](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.") сканирует и получает данные, хранящиеся в Grail. Спаны могут объединяться и анализироваться в контексте с другими сигналами платформы Dynatrace, такими как логи, события или метрики. |
| Использование приложений | DQL-запросы могут выполняться:  - Приложениями, такими как Notebooks **Notebooks**, Dashboards **Dashboards**, Workflows **Workflows** и Anomaly Detection **Anomaly Detection**. (Примечание: Distributed Tracing **Distributed Tracing** и Services **Services** не генерируют потребление Query.) - Плитки дашборда, основанные на данных спанов, запускают выполнение DQL-запросов при обновлении - Пользовательские приложения - Dynatrace API |

Использование ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** и ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** включено в Dynatrace.
Эти приложения не генерируют потребление запросов.

Когда в запросе также считываются другие типы данных, это может привести к потреблению соответствующей возможности, например [Log - Query](log-analytics/dps-log-query.md "Узнайте, как рассчитывается потребление возможности Log Management & Analytics - Query DPS.").

## Связанные темы

* [Distributed Tracing](../../observe/application-observability/distributed-tracing.md "Трассировка и анализ в реальном времени высокораспределённых систем с Grail.")
* [Traces](../../semantic-dictionary/model/trace.md "Познакомьтесь с моделями Semantic Dictionary, связанными с трассировками.")
* [Лицензирование Dynatrace](../../license.md "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace.")
* [Цены Dynatrace](https://www.dynatrace.com/pricing/)
