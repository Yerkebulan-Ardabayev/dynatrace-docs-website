---
title: Calculate your consumption of Log Management & Analytics - Query (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/log-analytics/dps-log-query
scraped: 2026-02-06T16:21:01.498046
---

# Рассчитайте потребление Log Management & Analytics — Query (DPS)

# Рассчитайте потребление Log Management & Analytics — Query (DPS)

* Последняя версия Dynatrace
* Объяснение
* 6-минутное чтение
* Обновлено 4 ноября 2025 г.

Журнал — обзор функции запроса

На этой странице описывается, как используется и выставляется счет за возможность управления журналами и аналитикой — Query DPS.
Обзор этой возможности, включая ее основные функции, см. в разделе [Аналитика журналов (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

Использование ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Распределенной трассировки** и ![Услуги](https://dt-cdn.net/hub/logos/services.png "Services") **Сервисов** включено в состав Dynatrace.
Эти приложения не производят никакого потребления.

## Как рассчитывается потребление: сканируется ГиБ

Запрошенные данные — это объем данных, считанных во время выполнения запроса DQL.
Он рассчитывается на каждый отсканированный гибибайт (отсканированный ГиБ).

Примените следующий расчет, чтобы определить потребление для измерения использования данных по запросу:

`consumption = (number of GiB of uncompressed data read during query execution) Ã (GiB scanned price as per your rate card)`

Потребление запросов основано на ГиБ данных, сканированных для возврата результата.
Наивысшая потенциальная стоимость запроса равна объему журналов в диапазоне поиска запроса, умноженному на цену в вашем прейскуранте.

Grail применяет различные оптимизации для улучшения времени отклика и снижения затрат.
В некоторых случаях эти оптимизации позволяют выявить части данных, которые не имеют отношения к результату запроса — цена за сканирование этих данных снижается на 98 %.

Влияние оптимизации сканирования Grail зависит от атрибутов данных и запросов.
Он может развиваться по мере того, как Dynatrace продолжает совершенствовать интеллект запросов Grail.

## Отслеживайте свое потребление

В этом разделе описаны различные инструменты Dynatrace, которые можно использовать для отслеживания потребления и затрат.

### Отслеживайте свое потребление с помощью показателей

Dynatrace предоставляет встроенную метрику использования, которая поможет вам понять и проанализировать использование вашей организацией Log Management & Analytics — Query.
Чтобы использовать эту метрику, в обозревателе данных введите `DPS` в поле **Поиск**.

Управление журналами и аналитика — запрос
: Ключ: `builtin:billing.log.query.usage`

Размерность: байт

Разрешение: 1 час

Описание: количество байтов, прочитанных во время выполнения запроса DQL, включая выборочные данные.

Пример использования метрики: отслеживание общего количества байтов, сканируемых с ежечасными интервалами.

Вы можете отслеживать общее количество сканированных байт для [Запрос](#query) с часовыми интервалами для любого выбранного периода времени, используя метрику `builtin:billing.log.query.usage`.

В приведенном ниже примере показано использование, агрегированное за 1-часовые интервалы между 04.09.2023 и 11.09.2023 (за последние 7 дней).

![Управление журналами и аналитика — запрос](https://dt-cdn.net/images/image034-806-25e7da895d.png)

### Отслеживайте свое потребление с помощью запросов DQL

Пример использования метрики: отслеживание общего количества просканированных гибибайтов.

Следующий запрос DQL предоставляет обзор общего использования [Запрос](#query) в отсканированных гибибайтах:

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| filter event.type == "Log Management & Analytics - Query"



| dedup event.id



| summarize {



data_read_bytes = sum(billed_bytes)



}, by: {



startHour = bin(timestamp, 1d)



}
```

В приведенном ниже примере показано ежедневное использование запросов, визуализированное в виде линейной диаграммы за последние 30 дней:

![Сохранение с включенными запросами (LMA)](https://dt-cdn.net/images/image-5-screenshot-2024-10-17-at-15-19-09-1243-832a39ebb6.png)

### Отслеживайте свое потребление и расходы в Управлении учетной записью

Вы также можете просмотреть показатели использования в разделе «Управление учетной записью».
Перейдите в раздел [**Управление аккаунтом**ï»¿](https://myaccount.dynatrace.com/) > **Подписка** > **Обзор** > **Сведения о стоимости и использовании** > **Сводка использования** и выберите возможность **Управление журналами и аналитика — Запрос**.

### Отслеживайте потребление и расходы через API

Вы можете запросить метрики через [API среды — API метрик v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Похожие темы

* [Аналитика журналов (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")
* [Что такое Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [Язык запросов Dynatrace](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Лицензия Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), модель лицензирования для всех возможностей Dynatrace.")
* [Цены на Dynatrace»¿](https://www.dynatrace.com/pricing/)