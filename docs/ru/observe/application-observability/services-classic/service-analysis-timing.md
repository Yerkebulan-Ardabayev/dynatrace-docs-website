---
title: Service analysis timings
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-timing
scraped: 2026-03-06T21:12:16.263242
---

# Тайминги анализа сервисов

# Тайминги анализа сервисов

* Classic
* Reference
* 5-min read
* Updated on Jul 24, 2023

Анализ сервисов работает с множеством различных таймингов, описывающих поведение сервиса. В таблице ниже представлен обзор таких таймингов. Тайминги варьируются в зависимости от типа анализа:

* DT: [Распределённые трассировки](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#pp-code-level-tab "Повысьте производительность распределённой системы, сегментируя запросы с медленным временем отклика через Service flow и анализируя их распределённые трассировки.").
* RT: [Время отклика](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Определите действия, потребляющие наибольшее время отклика для каждого сервиса.").
* SF: [Service flow](/docs/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает отслеживать последовательность вызовов сервисов, инициируемых каждым запросом к сервису в вашей среде.").
* MH: [Горячие точки методов](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Определите действия, потребляющие наибольшее время отклика для каждого сервиса.").

Независимо от того, какой анализ вы выполняете, не гарантируется, что вы увидите все перечисленные здесь тайминги. Фактически отображаемые тайминги полностью зависят от того, как запущены ваши сервисы. Например, если распределённая трассировка полностью выполняется на одном хосте без какого-либо сетевого взаимодействия, сетевые тайминги отображаться не будут.

## Связанные темы

* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Получите наблюдаемость в высокораспределённых, облачно-нативных архитектурах для эффективной трассировки и анализа транзакций в реальном времени.")
* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает отслеживать последовательность вызовов сервисов, инициируемых каждым запросом к сервису в вашей среде.")
* [Многомерный анализ](/docs/observe/application-observability/multidimensional-analysis "Настройте представление многомерного анализа и сохраните его как вычисляемую метрику.")
