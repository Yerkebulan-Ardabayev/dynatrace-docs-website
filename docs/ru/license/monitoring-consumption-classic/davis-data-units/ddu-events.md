---
title: DDU для пользовательских событий Davis
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events
scraped: 2026-03-06T21:32:03.536928
---

# DDUs for custom Davis events

# DDUs for custom Davis events

* Classic
* 2-min read
* Published Jul 09, 2021

Хотя мониторинг и отчётность по встроенным типам событий через OneAgent или облачные интеграции не требуют дополнительных затрат или лицензирования, у вас есть возможность настраивать пользовательские события и/или каналы приёма событий. Такие настройки, связанные с событиями, действительно приводят к потреблению [единиц данных Davis](../davis-data-units.md "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Приём пользовательских событий Davis потребляет DDU, поскольку требует значительно большей вычислительной и аналитической мощности по сравнению со встроенным приёмом событий через OneAgent или облачные интеграции.

## Типы пользовательских событий Davis, потребляющие DDU

Пользовательские созданные/принятые или подписанные события, которые вы можете настроить для своей среды и тем самым потреблять DDU, включают:

* Любое пользовательское событие, отправленное в Dynatrace через [Events API v2](../../../dynatrace-api/environment-api/events-v2.md "Find out what you can do with the Dynatrace Events API v2.") или [OneAgent API](../../../ingest-from/extend-dynatrace/extend-events.md#oneagent "Learn how to extend event observability in Dynatrace.")
* Любое пользовательское событие (например, событие Kubernetes), созданное из лог-сообщений с помощью правила извлечения [лог-события](../../../analyze-explore-automate/log-monitoring/analyze-log-data/log-events.md "Learn how to create and use Dynatrace log events to analyze log data.")

## Как рассчитывается потребление DDU для пользовательских событий Davis

Потребление DDU для пользовательских событий Davis эквивалентно [лицензированию по точкам данных пользовательских метрик](metric-cost-calculation.md#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). Каждое принятое пользовательское событие потребляет 0,001 DDU. Это также применяется к обновлениям уже отправленных пользовательских событий.

Пулы единиц данных Davis

[Пулы единиц данных Davis для событий](../davis-data-units.md#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") позволяют устанавливать жёсткие ограничения на потребление DDU для событий. Перейдите в **Settings** > **Consumption** > **Davis data units pools** и включите **Enable limit** в разделе **Events**, чтобы установить годовой или ежемесячный лимит.

## Часто задаваемые вопросы

### Что может вызвать потребление, отображаемое как объект «Not related to a monitored entity»

Потребление может быть вызвано Events v2 API, если не указан селектор сущности. См. [Events v2](../../../dynatrace-api/environment-api/events-v2.md "Find out what you can do with the Dynatrace Events API v2.").

## Связанные темы

* [Тарификация Dynatraceï»¿](https://www.dynatrace.com/pricing/)
