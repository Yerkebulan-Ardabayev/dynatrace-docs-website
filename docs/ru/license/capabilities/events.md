---
title: Обзор Events на базе Grail (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/events
scraped: 2026-03-06T21:24:51.504563
---

# Обзор событий на базе Grail (DPS)


* 5 минут чтения

Эта страница описывает различные возможности, связанные с событиями, и функции, которые они предоставляют в рамках подписки DPS.

Для получения информации о том, как потребление конкретной возможности переводится в использование лицензионного коммита DPS, см.:

* Events - Ingest & Process
* Events - Retain
* Events - Query

Dynatrace обеспечивает мониторинг и отчётность по:

* Встроенным типам событий через OneAgent или облачные интеграции.
* Пользовательским событиям и/или каналам приёма событий.
  К ним относятся:

  + Любое пользовательское событие, отправленное в Dynatrace через Events API v2 или [OneAgent API](../../ingest-from/extend-dynatrace/extend-events.md#oneagent "Learn how to extend event observability in Dynatrace.").
  + Любое пользовательское событие (например, событие Kubernetes), созданное из сообщений журнала с помощью [правила обработки журнала](../../analyze-explore-automate/logs/lma-classic-log-processing.md#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
  + Любое пользовательское событие, созданное на шаге обработки в OpenPipeline.

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

* Log events
* Metric events
* Events API v2
* What is Dynatrace Grail?
* License Dynatrace, the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricing](https://www.dynatrace.com/pricing/)
