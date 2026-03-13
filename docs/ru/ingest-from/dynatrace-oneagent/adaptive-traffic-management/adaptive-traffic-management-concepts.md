---
title: Adaptive Traffic Management concepts
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-concepts
scraped: 2026-03-06T21:34:53.354074
---

# Концепции Adaptive Traffic Management

# Концепции Adaptive Traffic Management

* Latest Dynatrace
* Explanation
* 2-min read
* Published Jan 26, 2026

На этой странице описаны различные термины, связанные с Adaptive Traffic Management.

## Adaptive Traffic Management (ATM)

ATM for Dynatrace Platform Subscription ATM for Dynatrace classic license

**Adaptive Traffic Management (ATM)** — это интеллектуальный механизм выборки трассировок Dynatrace для Full-Stack Monitoring.

OneAgent автоматически управляет объёмом принимаемых данных трассировки посредством Adaptive Traffic Management. Он непрерывно корректирует [адаптивную частоту выборки трассировок](#adaptive-trace-sampling-rate), чтобы поддерживать объём принимаемых данных трассировки примерно в пределах вашего [включённого объёма трассировок Full-Stack](#full-stack-included-trace-volume) или вашего [общего лицензированного объёма трассировок Full-Stack](#total-licensed-full-stack-trace-volume) (только для Dynatrace Platform Subscription). Это достигается путём мониторинга объёма принимаемых данных трассировки от хостов и приложений, отслеживаемых в режиме Full-Stack. Если объём принимаемых данных трассировки превышает выделенный объём, Adaptive Traffic Management снижает адаптивную частоту выборки трассировок на OneAgent, уменьшая скорость захвата трассировок и объём принимаемых данных трассировки. OneAgent использует выборку на основе заголовка (head-based sampling), при которой решение о выборке для каждой трассировки принимается в момент её начала.

## Адаптивная частота выборки трассировок

ATM for Dynatrace Platform Subscription ATM for Dynatrace classic license

**Адаптивная частота выборки трассировок** — это частота, с которой Dynatrace OneAgents или другие участвующие агенты трассировки запускают распределённые трассировки, как правило применяя адаптивную выборку.

Adaptive Traffic Management инструктирует агентов инициировать трассировки с определённой частотой, например 1000 в минуту. Эта частота непрерывно корректируется, чтобы объём принимаемых данных трассировки не превышал заданного предела. Агенты, сообщающие о 100% захвате трассировок, могут запускать меньше трассировок, чем эта частота, в зависимости от числа транзакций приложения. Агенты, сообщающие о частоте захвата трассировок ниже 100%, ведут выборку именно с этой частотой.

В рамках Dynatrace Platform Subscription вы можете настроить [адаптивную частоту выборки трассировок](adaptive-traffic-management-saas-dps.md#adjust-adaptive-trace-sampling-rate "Learn how Adaptive Traffic Management works with Dynatrace Platform Subscription (DPS) and how it manages trace sampling for Full-Stack monitored hosts and applications.") на уровне области видимости (scope), что позволяет лучше контролировать использование включённого объёма трассировок Full-Stack Monitoring.

## Расширенный приём трассировок

ATM for Dynatrace Platform Subscription

**Расширенный приём трассировок (Extended trace ingest)** — платная опция, позволяющая увеличить объём принимаемых трассировок сверх объёма, уже включённого в Full-Stack Monitoring.

Подробнее см. раздел [Расширенный приём трассировок для Full-Stack Monitoring](../../../license/capabilities/app-infra-observability/full-stack-monitoring.md#extend-trace-ingest "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").

## Включённый объём трассировок Full-Stack

ATM for Dynatrace Platform Subscription ATM for Dynatrace classic license

**Включённый объём трассировок Full-Stack** — это объём [данных трассировки](../../../license/capabilities/app-infra-observability/full-stack-monitoring.md#full-stack-traces "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged."), включённый в [Full-Stack Monitoring](../../../license/capabilities/app-infra-observability/full-stack-monitoring.md "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").

Adaptive Traffic Management обеспечивает, чтобы хосты и приложения, отслеживаемые в режиме Full-Stack, оставались в пределах этого лицензированного объёма трассировок.

В рамках Dynatrace Platform Subscription вы можете [расширить приём трассировок](#extended-trace-ingest) сверх **включённого объёма трассировок Full-Stack**. В этом случае Adaptive Traffic Management обеспечивает, чтобы хосты и приложения, отслеживаемые в режиме Full-Stack, оставались в пределах [общего лицензированного объёма трассировок Full-Stack](#total-licensed-full-stack-trace-volume).

## Общий лицензированный объём трассировок Full-Stack

ATM for Dynatrace Platform Subscription

**Общий лицензированный объём трассировок Full-Stack** — это сумма объёма трассировок, включённого в Full-Stack Monitoring (называемого [включённым объёмом трассировок Full-Stack](#full-stack-included-trace-volume)), и объёма трассировок, добавленного через [расширенный приём трассировок](#extended-trace-ingest).

Adaptive Traffic Management обеспечивает, чтобы хосты и приложения, отслеживаемые в режиме Full-Stack, оставались в пределах общего лицензированного объёма трассировок Full-Stack.

## Используемый адаптивный объём трассировок

ATM for Dynatrace Platform Subscription

**Используемый адаптивный объём трассировок (Usable adaptive trace volume)** — это та часть вашего [общего лицензированного объёма трассировок Full-Stack](#total-licensed-full-stack-trace-volume), которую вы выделяете для Adaptive Traffic Management.

Чтобы контролировать, какая часть вашего [включённого объёма трассировок Full-Stack](#full-stack-included-trace-volume) распределяется через Adaptive Traffic Management, вы можете [уменьшить используемый адаптивный объём трассировок](adaptive-traffic-management-saas-dps.md#reduce-usable-adaptive-trace-volume "Learn how Adaptive Traffic Management works with Dynatrace Platform Subscription (DPS) and how it manages trace sampling for Full-Stack monitored hosts and applications."). Эта возможность самообслуживания также позволяет выделить часть включённого объёма трассировок Full-Stack для спанов с фиксированной частотой выборки из OpenTelemetry или OneAgent. Таким образом, вы можете более эффективно управлять избыточным объёмом принимаемых трассировок.
