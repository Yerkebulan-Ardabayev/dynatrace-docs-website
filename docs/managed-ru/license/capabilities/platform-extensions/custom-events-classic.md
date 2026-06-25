---
title: Custom Events Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/custom-events-classic
scraped: 2026-05-12T12:13:09.459125
---

# Custom Events Classic (DPS)

# Custom Events Classic (DPS)

* 16-min read
* Updated on Jan 12, 2026

На этой странице описано, как потребляется и тарифицируется DPS-возможность Custom Events Classic.
Обзор возможности и основных функций см. в [Custom Events Classic](/managed/license/capabilities/platform-extensions#events "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: пользовательские события

Единица измерения для расчёта потребления пользовательских событий в вашей среде — пользовательское событие.

Хотя встроенные типы событий через OneAgent или облачные интеграции не влекут дополнительных затрат, подобные пользовательские настройки событий приводят к дополнительному потреблению, поскольку требуют значительно большей вычислительной и аналитической мощности, чем встроенный приём событий через OneAgent или облачные интеграции.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Custom Events Classic в вашей организации.

Для использования в Data Explorer введите DPS в поле **Search**.
Эти метрики также доступны через Environment API и связаны в Account Management (**Usage summary** > **Custom Events Classic** > **Actions** > **View details**).
В таблице ниже перечислены метрики для мониторинга потребления Custom Events Classic в вашей организации.

(DPS) Total Custom Events Classic billing usage
:   Ключ: `builtin:billing.custom_events_classic.usage`

    Измерение: count

    Разрешение: 1 мин

    Описание: Количество тарифицируемых принятых событий, агрегированных по всем мониторируемым сущностям.

(DPS) Custom Events Classic billing usage by event info
:   Ключ: `builtin:billing.custom_events_classic.usage_by_event_info`

    Измерение: count

    Разрешение: 1 мин

    Описание: Количество тарифицируемых принятых событий с разбивкой по типу сущности.

(DPS) Custom Events Classic billing usage by monitored entity
:   Ключ: `builtin:billing.custom_events_classic.usage_by_entity`

    Измерение: count

    Разрешение: 1 мин

    Описание: Количество тарифицируемых принятых событий с разбивкой по мониторируемой сущности.

Суммарное количество тарифицируемых классических событий, принятых за различные интервалы в любом выбранном периоде, можно отслеживать с помощью метрики «(DPS) Total Custom Events Classic billing usage».
В примере ниже показано потребление, агрегированное в 1-часовых интервалах.
С 11:00 до 14:00 каждый час принималось около 1 600 пользовательских классических событий.

![Custom Events Classic (DPS)](https://dt-cdn.net/images/image061-828-61035cf7a2.png)

Custom Events Classic (DPS)

## Связанные темы

* [Обзор расширений платформы (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)