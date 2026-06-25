---
title: DDU для пользовательских трассировок (Trace API)
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces
scraped: 2026-05-12T12:10:14.914661
---

# DDU для пользовательских трассировок (Trace API)

# DDU для пользовательских трассировок (Trace API)

* 2-min read
* Published Mar 30, 2021

Хотя интеграция данных спанов OpenTracing и OpenTelemetry в Dynatrace через OneAgent не влечёт дополнительных затрат, у вас есть возможность настроить Dynatrace Trace API для приёма спанов OpenTelemetry и OpenTracing — так называемых «пользовательских трассировок». Этот подход полезен для seamless-интеграции данных трассировок OpenTelemetry, поступающих от сторонних сервисов. Приём спанов через конечную точку Trace API потребляет [единицы Davis data units](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."), поскольку требует большей вычислительной и аналитической мощности, чем приём через OneAgent.

Подробнее о приёме спанов OpenTelemetry и OpenTracing через OneAgent (без потребления DDU) см. в [OneAgent OpenTracing and OpenTelemetry support](/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace.").

## Потребление DDU при приёме пользовательских трассировок

Хотя трассировка может содержать спаны, захваченные OneAgent и Dynatrace Trace API, DDU потребляют только спаны, принятые через Dynatrace Trace API. Для API-сервиса, инструментированного OpenTelemetry, где спаны захватываются через OneAgent, DDU не потребляются. Пользовательские трассировки, принятые через Dynatrace Trace API, лицензируются на основе числа принятых спанов (каждый спан соответствует единственной операции в трассировке).

### Пример потребления DDU

Для расчёта потребления DDU для пользовательских трассировок умножьте общее число вызовов на общее число спанов, умноженное на вес DDU, за измеряемый период. Рассмотрим API-сервис, инструментированный OpenTelemetry, принимающий в среднем 10 спанов на API-вызов через Dynatrace Trace API. При среднем числе API-вызовов 1 миллион в месяц ежемесячное потребление DDU составит 7 000 DDU (`1 000 000 вызовов × 10 спанов × 0,0007 DDU = 7 000 DDU`), а годовой эквивалент — 84 000 DDU (`7 000 DDU × 12 месяцев = 84 000 DDU`).

Пулы Davis data units

[Пулы Davis data units для трассировок](/managed/license/monitoring-consumption-classic/davis-data-units#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") позволяют задавать жёсткие лимиты потребления DDU для трассировок. Перейдите в **Settings** > **Consumption** > **Davis data units pools** и включите **Enable limit** в разделе **Traces** для установки ежегодного или ежемесячного лимита.

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Расширение Dynatrace (единицы Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDU для метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")