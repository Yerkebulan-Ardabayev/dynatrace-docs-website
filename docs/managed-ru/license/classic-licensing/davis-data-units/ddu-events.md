---
title: DDU для пользовательских событий Davis
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units/ddu-events
---

# DDU для пользовательских событий Davis

# DDU для пользовательских событий Davis

* Чтение: 2 мин
* Опубликовано 09 июля 2021 г.

Мониторинг и отображение встроенных типов событий по умолчанию через OneAgent или облачные интеграции не влечёт дополнительных затрат и лицензирования, но есть возможность настроить пользовательские события и/или каналы приёма событий. Такие пользовательские настройки, связанные с событиями, приводят к расходу [Davis data units](/managed/license/classic-licensing/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Приём пользовательских событий Davis расходует DDU, поскольку требует значительно больше вычислительных и аналитических ресурсов, чем приём встроенных событий через OneAgent или облачные интеграции.

## Типы пользовательских событий Davis, которые расходуют DDU

Пользовательские созданные/принятые или подписанные события, которые можно настроить для своей среды и которые тем самым расходуют DDU, включают:

* Любое пользовательское событие, отправленное в Dynatrace с помощью [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") или [OneAgent API](/managed/ingest-from/extend-dynatrace/extend-events#oneagent "Learn how to extend event observability in Dynatrace.")
* Любое пользовательское событие (например, событие Kubernetes), созданное из сообщений журнала правилом извлечения [log event](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")

## Как рассчитывается расход DDU для пользовательских событий Davis

Расход DDU для пользовательских событий Davis эквивалентен [лицензированию точек данных пользовательских метрик](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). Каждое принятое пользовательское событие расходует 0.001 DDU. Это также относится к обновлениям уже отправленных пользовательских событий.

Пулы Davis data units

[Пулы Davis data units для событий](/managed/license/classic-licensing/davis-data-units#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") позволяют устанавливать жёсткие ограничения на расход DDU для событий. Перейти в **Settings** > **Consumption** > **Davis data units pools** и включить **Enable limit** в разделе **Events**, чтобы задать годовой или месячный лимит.

## Часто задаваемые вопросы

### Что может вызывать расход, отображаемый для сущности «Not related to a monitored entity»

Такой расход может быть вызван API events v2, если не указан селектор сущности. См. [Events v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

## Похожие темы

* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)