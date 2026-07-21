---
title: DDU для пользовательских трасс (Trace API)
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units/custom-traces
---

# DDU для пользовательских трасс (Trace API)

# DDU для пользовательских трасс (Trace API)

* 2 минуты чтения
* Опубликовано 30 марта 2021 г.

Интеграция данных span из OpenTracing и OpenTelemetry в Dynatrace через OneAgent не влечёт дополнительных затрат и не требует лицензирования, но есть возможность настроить Dynatrace Trace API для приёма span'ов OpenTelemetry и OpenTracing: их называют «пользовательскими трассами» (custom traces). Такой подход удобен для бесшовной интеграции данных трасс OpenTelemetry, которые отправляют сторонние сервисы. Приём span'ов через эндпоинт Trace API расходует [Davis data units](/managed/license/classic-licensing/davis-data-units "Понять, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU)."), поскольку этот подход требует больше вычислительных и аналитических ресурсов, чем приём через OneAgent.

Подробнее о приёме span'ов OpenTelemetry и OpenTracing через OneAgent, который не расходует DDU, см. [Поддержка OpenTracing и OpenTelemetry в OneAgent](/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing "Узнать, как интегрировать OpenTracing с Dynatrace.").

## Потребление DDU при приёме пользовательских трасс

Трасса может содержать span'ы, захваченные как через OneAgent, так и через Dynatrace Trace API, но DDU расходуют только те span'ы, которые приняты через Dynatrace Trace API. Если сервис API инструментирован с помощью OpenTelemetry, а span'ы захватываются через OneAgent, DDU не расходуются. Пользовательские трассы, принятые через Dynatrace Trace API, лицензируются на основе приёма span'ов (каждый span соответствует одной операции внутри трассы).

### Пример расчёта потребления DDU

Чтобы рассчитать потребление DDU для пользовательских трасс, нужно умножить общее число вызовов на общее число span'ов и на вес DDU за измеряемый период времени. Рассмотрим сервис API, инструментированный с помощью OpenTelemetry, который в среднем принимает 10 span'ов на каждый вызов API через Dynatrace Trace API. Если среднее число вызовов API в месяц составляет 1 миллион, месячное потребление DDU равно 7000 DDU (`1 000 000 вызовов × 10 span'ов × 0,0007 DDU = 7000 DDU`), что в годовом эквиваленте составляет 84 000 DDU (`7000 DDU × 12 месяцев = 84 000 DDU`).

Пулы Davis data units

[Пулы Davis data units для трасс](/managed/license/classic-licensing/davis-data-units#ddu-pools "Понять, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU).") позволяют устанавливать жёсткие лимиты на потребление DDU для трасс. Перейти в **Settings** > **Consumption** > **Davis data units pools** и включить **Enable limit** в разделе **Traces**, чтобы задать годовой или месячный лимит.

## Связанные темы

* [Тарификация Dynatrace﻿](https://www.dynatrace.com/pricing/)
* [Классическое лицензирование Dynatrace](/managed/license/monitoring-consumption-classic "Понять, как рассчитывается классическое потребление мониторинга Dynatrace, включая host units, DDU, DEM units и Application Security units.")
* [Расширение Dynatrace (Davis data units)](/managed/license/classic-licensing/davis-data-units "Понять, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU).")
* [DDU для метрик](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Понять, как рассчитать потребление и стоимость Davis data units для отслеживаемых метрик.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнать, как расширить наблюдаемость метрик в Dynatrace.")