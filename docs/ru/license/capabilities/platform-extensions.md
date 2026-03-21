---
title: Обзор Platform extensions (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/platform-extensions
scraped: 2026-03-06T21:36:49.590243
---

# Обзор расширений платформы (DPS)


С 12 января 2026 года расширения платформы SaaS больше не включаются в тарифную карту для новых подписок DPS, заключённых начиная с этой даты.
Существующие клиенты DPS сохраняют доступ к возможностям расширений платформы SaaS.

На этой странице описаны различные расширения платформы и возможности, которые они предоставляют в рамках подписки DPS.

Информация о том, как использование конкретной возможности переводится в потребление лицензионного коммита DPS, приведена в разделах:

* [Custom Events Classic](platform-extensions/custom-events-classic.md "Узнайте, как рассчитывается и тарифицируется потребление возможности Dynatrace Custom Events Classic DPS.")
* [Custom Metrics Classic](platform-extensions/custom-metrics-classic.md "Узнайте, как рассчитывается и тарифицируется потребление возможности Dynatrace Custom Metrics Classic DPS.")
* [Custom Traces Classic](platform-extensions/custom-traces-classic.md "Узнайте, как рассчитывается и тарифицируется потребление возможности Dynatrace Custom Traces Classic DPS.")
* [Log Monitoring Classic](platform-extensions/log-monitoring-classic.md "Узнайте, как рассчитывается и тарифицируется потребление возможности Dynatrace Log Monitoring Classic DPS.")
* [Serverless Functions Classic](platform-extensions/serverless-functions-classic.md "Узнайте, как рассчитывается и тарифицируется потребление возможности Dynatrace Serverless Functions Classic DPS.")

Узнайте, как рассчитывается потребление расширений платформы Dynatrace в рамках модели Dynatrace Platform Subscription.

## Обзор возможностей Custom Metrics Classic

Вы можете расширить возможности Dynatrace, определяя, включая или принимая пользовательские метрики.
Dynatrace позволяет интегрировать сторонние источники данных, принимать пользовательские метрики через API, использовать расширения, облачные интеграции и многое другое.

Ниже приведён неполный список типов пользовательских метрик:

* Метрики, принятые из Amazon CloudWatch, Azure Monitor или Google Cloud Operations Cloud для мониторинга облачных сервисов
* Метрики, принятые из удалённых расширений для мониторинга баз данных, сетевых устройств, очередей и других компонентов
* Все метрики, принятые через API
* Рассчитанные метрики сервисов, пользовательские DEM-метрики и метрики журналов

## Обзор возможностей Log Monitoring Classic

Dynatrace может принимать записи журналов.
Запись журнала распознаётся одним из следующих способов:

* Временная метка
* JSON-объект

## Обзор возможностей Custom Traces Classic

Вы можете [принимать трассировки](../../ingest-from/opentelemetry/otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") в Dynatrace с помощью [экспортёров OpenTelemetry](../../ingest-from/opentelemetry.md "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и журналы) в Dynatrace.") для приложений, работающих на хостах без установленного OneAgent.
Эти распределённые трассировки отправляются через [Trace Ingest API](../../ingest-from/opentelemetry/otlp-api.md "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

## Обзор возможностей Custom Events Classic

У вас есть возможность настроить пользовательские события и/или каналы приёма событий.

Пользовательские созданные/принятые или подписочные события, которые можно настроить для среды, включают:

* Любое пользовательское событие, отправленное в Dynatrace с помощью [Events API v2](../../dynatrace-api/environment-api/events-v2.md "Узнайте, что можно сделать с помощью Dynatrace Events API v2.").
* Любое пользовательское событие (например, событие Kubernetes), созданное из сообщений журнала с помощью [правила обработки журналов](../../analyze-explore-automate/logs/lma-classic-log-processing.md#lmc-log-processing-rules "Используйте правила обработки журналов для преобразования входящих данных журналов с целью улучшения понимания, анализа или дальнейшего преобразования.").

## Обзор возможностей Serverless Functions Classic

Dynatrace обеспечивает сквозную наблюдаемость бессерверных облачных функций на основе данных мониторинга, поступающих из трассировок, метрик и журналов.

Dynatrace также позволяет принимать журналы из ваших бессерверных облачных функций.

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
