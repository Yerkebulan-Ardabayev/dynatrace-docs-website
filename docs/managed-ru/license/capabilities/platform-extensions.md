---
title: Обзор расширений платформы (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions
scraped: 2026-05-12T12:04:51.279123
---

# Обзор расширений платформы (DPS)

# Обзор расширений платформы (DPS)

* Overview
* 16-min read
* Updated on Jan 12, 2026

На этой странице описаны различные расширения платформы и функции, предоставляемые с подпиской DPS.

Информацию о том, как использование конкретной возможности переводится в потребление лицензионного лимита DPS, см. на страницах:

* [Custom Events Classic](/managed/license/capabilities/platform-extensions/custom-events-classic "Learn how your consumption of the Dynatrace Custom Events Classic DPS capability is billed and charged.")
* [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.")
* [Custom Traces Classic](/managed/license/capabilities/platform-extensions/custom-traces-classic "Learn how your consumption of the Dynatrace Custom Traces Classic DPS capability is billed and charged.")
* [Log Monitoring Classic](/managed/license/capabilities/platform-extensions/log-monitoring-classic "Learn how your consumption of the Dynatrace Log Monitoring Classic DPS capability is billed and charged.")
* [Serverless Functions Classic](/managed/license/capabilities/platform-extensions/serverless-functions-classic "Learn how your consumption of the Dynatrace Serverless Functions Classic DPS capability is billed and charged.")

Узнайте, как рассчитывается потребление расширений платформы Dynatrace по модели Dynatrace Platform Subscription.

## Обзор возможности Custom Metrics Classic

Вы можете расширить ценность Dynatrace, определяя, включая или принимая пользовательские метрики.
Dynatrace позволяет интегрировать сторонние источники данных, принимать пользовательские метрики через API, использовать расширения, облачные интеграции и многое другое.

Ниже приведён неполный список типов пользовательских метрик:

* Метрики, принятые из Amazon CloudWatch, Azure Monitor или Google Cloud Operations Cloud для мониторинга облачных сервисов
* Метрики, принятые из удалённых расширений для мониторинга баз данных, сетевых устройств, очередей и другого
* Все метрики, принятые через API
* Расчётные метрики сервисов, пользовательские метрики DEM и метрики логов

## Обзор возможности Log Monitoring Classic

Dynatrace может принимать записи логов.
Запись лога распознаётся одним из следующих способов:

* Временная метка (timestamp)
* JSON-объект

## Обзор возможности Custom Traces Classic

Вы можете [принимать трассировки](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") в Dynatrace с помощью [экспортёров OpenTelemetry](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") для приложений, запущенных на хостах без установленного OneAgent.
Эти распределённые трассировки отправляются через [Trace Ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

## Обзор возможности Custom Events Classic

У вас есть возможность настраивать пользовательские события и/или каналы приёма событий.

Пользовательские создаваемые/принимаемые или подписанные события, которые могут быть настроены для окружения, включают:

* Любые пользовательские события, отправленные в Dynatrace через [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").
* Любые пользовательские события (например, события Kubernetes), созданные из сообщений лога с помощью [правила обработки логов](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

## Обзор возможности Serverless Functions Classic

Dynatrace обеспечивает сквозную наблюдаемость бессерверных облачных функций на основе данных мониторинга из трассировок, метрик и логов.

Dynatrace также позволяет принимать логи из ваших бессерверных облачных функций.

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)