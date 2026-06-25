---
title: Оповещения на основе данных журналов
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/alert-log-data
scraped: 2026-05-12T11:13:31.804728
---

# Оповещения на основе данных журналов

# Оповещения на основе данных журналов

* Пояснение
* Чтение: 3 мин
* Опубликовано 12 июня 2025 г.

Log Monitoring Classic

Dynatrace Log Monitoring позволяет определять шаблоны, события и пользовательские метрики журналов для получения проактивных уведомлений.

## Метрики журналов

Можно создать метрику на основе отслеживаемых данных журналов. С такой метрикой Dynatrace непрерывно сканирует данные журналов и отображает её график на панели мониторинга, чтобы любые изменения шаблона в пользовательской метрике были чётко видны.

* Ознакомьтесь с разделом [Метрики журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных.") для получения общей информации.
* Ознакомьтесь с [Примером создания оповещения на основе метрики журнала](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics#log-monitoring-metric-alert-example "Узнайте, как создавать и использовать метрики журналов Dynatrace.").

## События журналов

Когда Dynatrace принимает данные журналов, он применяет запрос, указанный в определении события журнала. Каждое совпадение запускает событие журнала, которое можно настроить на создание отдельной проблемы для каждого события или объединение в одну проблему.

* Ознакомьтесь с разделом [События журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Узнайте, как создавать и использовать события журналов Dynatrace для анализа данных.") для получения общей информации.
* Ознакомьтесь с [Примером создания события журнала на основе принятых данных журналов](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events#log-monitoring-log-event-example "Узнайте, как создавать и использовать события журналов Dynatrace.").

## Связанные темы

* [Метрики журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных.")
* [События журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Узнайте, как создавать и использовать события журналов Dynatrace для анализа данных.")