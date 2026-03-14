---
title: Обзор Events на базе Grail (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/events
scraped: 2026-03-06T21:24:51.504563
---

# Обзор событий на базе Grail (DPS)

# Обзор событий на базе Grail (DPS)

* Последняя версия Dynatrace
* Обзор
* 5 минут чтения
* Обновлено 28 января 2026 г.

Эта страница описывает различные возможности, связанные с событиями, и функции, которые они предоставляют в рамках подписки DPS.

Для получения информации о том, как потребление конкретной возможности переводится в использование лицензионного коммита DPS, см.:

* [Events - Ingest & Process](events/dps-events-ingest.md "Learn how your consumption of the Events powered by Grail - Ingest & Process DPS capability is billed and charged.")
* [Events - Retain](events/dps-events-retain.md "Learn how your consumption of the Events powered by Grail - Retain DPS capability is billed and charged.")
* [Events - Query](events/dps-events-query.md "Learn how your consumption of the Events powered by Grail - Query DPS capability is billed and charged.")

Dynatrace обеспечивает мониторинг и отчётность по:

* Встроенным типам событий через OneAgent или облачные интеграции.
* Пользовательским событиям и/или каналам приёма событий.
  К ним относятся:

  + Любое пользовательское событие, отправленное в Dynatrace через [Events API v2](../../dynatrace-api/environment-api/events-v2.md "Find out what you can do with the Dynatrace Events API v2.") или [OneAgent API](../../ingest-from/extend-dynatrace/extend-events.md#oneagent "Learn how to extend event observability in Dynatrace.").
  + Любое пользовательское событие (например, событие Kubernetes), созданное из сообщений журнала с помощью [правила обработки журнала](../../analyze-explore-automate/logs/lma-classic-log-processing.md#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
  + Любое пользовательское событие, созданное на [шаге обработки](../../platform/openpipeline/concepts/processing.md "Learn the core concepts of Dynatrace OpenPipeline processing.") в OpenPipeline.

Потребление всех событий подлежит тарификации, за исключением определённых включённых событий, описанных в таблице «Включённые события» ниже.

Список тарифицируемых типов событий

Следующие события тарифицируются:

* Бизнес-события
* SDLC-события
* Пользовательские события, включая:

  + События безопасности
  + События Davis
  + Предупреждающие события Kubernetes
  + Общие пользовательские события
  + Пользовательские события, определённые клиентом

Включённые события

В таблице ниже описаны события, включённые в отдельный пакет тарифного плана.

1

Хранение сверх включённого периода тарифицируется как Events powered by Grail - Retain.

## Обзор функций Events - Ingest & Process

Вот что включено в измерение использования данных Ingest & Process:

## Обзор функций Events - Retain

Вот что включено в измерение использования данных Retain:

## Обзор функций Events - Query

Использование данных Query происходит при:

* Отправке пользовательских DQL-запросов в средстве просмотра журналов и событий в расширенном режиме.
* Использовании приложений Business Observability (Business Flow, Salesforce Insights и Carbon Impact).
* Выполнении DQL-запросов в Notebooks, Dashboards, Workflows, пользовательских приложениях и через API.

Вот что включено в измерение использования данных Query:

## Связанные темы

* [Log events](../../analyze-explore-automate/logs/lma-log-processing/lma-log-events.md "Create log events based on log data and use them in problem detection.")
* [Metric events](../../dynatrace-intelligence/anomaly-detection/metric-events.md "Learn about metric events in Dynatrace")
* [Events API v2](../../dynatrace-api/environment-api/events-v2.md "Find out what you can do with the Dynatrace Events API v2.")
* [What is Dynatrace Grail?](../../platform/grail/dynatrace-grail.md "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricing](https://www.dynatrace.com/pricing/)
