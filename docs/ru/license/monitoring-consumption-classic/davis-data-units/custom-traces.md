---
title: DDUs for custom traces (Trace API)
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces
scraped: 2026-03-06T21:37:37.198226
---

# DDU для пользовательских трассировок (Trace API)

# DDU для пользовательских трассировок (Trace API)

* Classic
* 2-min read
* Published Mar 30, 2021

Хотя интеграция данных спанов OpenTracing и OpenTelemetry в Dynatrace через OneAgent не влечёт дополнительных затрат и лицензирования, у вас есть возможность настроить Dynatrace Trace API для приёма спанов OpenTelemetry и OpenTracing; они называются «пользовательскими трассировками». Такой подход полезен для бесшовной интеграции данных трассировок OpenTelemetry, генерируемых сторонними сервисами. Приём спанов через конечную точку Trace API потребляет [единицы данных Davis](../davis-data-units.md "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."), поскольку этот подход требует большей вычислительной мощности и аналитических ресурсов, чем приём через OneAgent.

Для получения подробной информации о приёме спанов OpenTelemetry и OpenTracing на основе OneAgent, при котором DDU не потребляются, см. [поддержку OpenTracing и OpenTelemetry в OneAgent](../../../ingest-from/extend-dynatrace/extend-tracing/opentracing.md "Learn how to integrate OpenTracing with Dynatrace.").

## Потребление DDU при приёме пользовательских трассировок

Хотя трассировка может содержать спаны, захваченные как с помощью OneAgent, так и через Dynatrace Trace API, DDU потребляют только спаны, принятые через Dynatrace Trace API. Для API-сервиса, инструментированного с помощью OpenTelemetry, где спаны захватываются через OneAgent, DDU не потребляются. Пользовательские трассировки, принятые через Dynatrace Trace API, лицензируются на основе приёма спанов (каждый спан соответствует одной операции внутри трассировки).

### Пример потребления DDU

Для расчёта потребления DDU для пользовательских трассировок умножьте общее количество вызовов на общее количество спанов и на вес DDU за измеряемый период времени. Рассмотрим API-сервис, инструментированный с помощью OpenTelemetry, который в среднем принимает 10 спанов на API-вызов через Dynatrace Trace API. Если среднее количество API-вызовов в месяц составляет 1 миллион, то ежемесячное потребление DDU составит 7 000 DDU (`1 000 000 вызовов × 10 спанов × 0,0007 DDU = 7 000 DDU`), а в годовом эквиваленте — 84 000 DDU (`7 000 DDU × 12 месяцев = 84 000 DDU`).

Пулы единиц данных Davis

[Пулы единиц данных Davis для трассировок](../davis-data-units.md#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") позволяют устанавливать жёсткие ограничения на потребление DDU для трассировок. Перейдите в **Settings** > **Consumption** > **Davis data units pools** и включите **Enable limit** в разделе **Traces**, чтобы задать годовой или ежемесячный лимит.

## Связанные темы

* [Цены на Dynatrace](https://www.dynatrace.com/pricing/)
* [Лицензирование Dynatrace](../../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Расширение Dynatrace (единицы данных Davis)](../davis-data-units.md "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDU для метрик](metric-cost-calculation.md "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Расширение наблюдаемости метрик](../../../ingest-from/extend-dynatrace/extend-metrics.md "Learn how to extend metric observability in Dynatrace.")
