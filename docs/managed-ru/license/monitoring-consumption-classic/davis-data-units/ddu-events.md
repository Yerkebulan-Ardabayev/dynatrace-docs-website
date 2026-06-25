---
title: DDU для пользовательских событий Davis
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units/ddu-events
scraped: 2026-05-12T12:00:20.069619
---

# DDU для пользовательских событий Davis

# DDU для пользовательских событий Davis

* 2-min read
* Published Jul 09, 2021

Хотя встроенные типы событий через OneAgent или облачные интеграции не влекут дополнительных затрат, у вас есть возможность настраивать пользовательские события и/или каналы приёма событий. Такие пользовательские настройки событий приводят к потреблению [единиц Davis data units](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Приём пользовательских событий Davis потребляет DDU, поскольку требует значительно большей вычислительной и аналитической мощности, чем встроенный приём событий через OneAgent или облачные интеграции.

## Типы пользовательских событий Davis, потребляющих DDU

Пользовательские создаваемые/принимаемые или подписанные события, которые вы можете настроить для своей среды и тем самым потреблять DDU, включают:

* Любые пользовательские события, отправленные в Dynatrace с помощью [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") или [OneAgent API](/managed/ingest-from/extend-dynatrace/extend-events#oneagent "Learn how to extend event observability in Dynatrace.")
* Любые пользовательские события (например, события Kubernetes), созданные из сообщений лога с помощью правила извлечения [лог-событий](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")

## Расчёт потребления DDU для пользовательских событий Davis

Потребление DDU для пользовательских событий Davis эквивалентно [лицензированию точек данных пользовательских метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). Каждое принятое пользовательское событие потребляет 0,001 DDU. Это также применяется к обновлениям уже отправленных пользовательских событий.

Пулы Davis data units

[Пулы Davis data units для событий](/managed/license/monitoring-consumption-classic/davis-data-units#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") позволяют задавать жёсткие лимиты потребления DDU для событий. Перейдите в **Settings** > **Consumption** > **Davis data units pools** и включите **Enable limit** в разделе **Events** для установки ежегодного или ежемесячного лимита.

## Часто задаваемые вопросы

### Что может быть причиной потребления, отображаемого как сущность «Not related to a monitored entity»?

Это потребление может быть вызвано Events v2 API при отсутствии селектора сущностей. См. [Events v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)