---
title: Расчет потребления Log Management & Analytics - Query (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/log-analytics/dps-log-query
scraped: 2026-03-06T21:11:26.513950
---

# Расчёт потребления Log Management & Analytics — Query (DPS)


* Latest Dynatrace
* Explanation
* 6-min read

Обзор функции Log — Query

На этой странице описывается, как потребляется и тарифицируется возможность Log Management & Analytics — Query DPS.
Обзор возможности, включая её основные функции, см. в разделе [Log Analytics (DPS)](../log-analytics.md "Узнайте, как рассчитывается потребление Dynatrace Log Analytics с использованием модели подписки Dynatrace Platform Subscription.").

Использование ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** и ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** включено в состав Dynatrace.
Эти приложения не генерируют потребление.

## Как рассчитывается потребление: ГиБ просканировано

Запрашиваемые данные — это объём данных, прочитанных при выполнении DQL-запроса.
Рассчитывается в гибибайтах просканированных данных (ГиБ просканировано).

Для определения потребления по измерению использования данных Query применяйте следующий расчёт:

`потребление = (количество ГиБ несжатых данных, прочитанных при выполнении запроса) × (цена за ГиБ просканировано согласно вашей тарифной карте)`

Потребление при запросах основано на объёме ГиБ данных, просканированных для получения результата.
Максимально возможная стоимость запроса равна объёму журналов в диапазоне поиска запроса, умноженному на цену в вашей тарифной карте.

Grail применяет различные оптимизации для улучшения времени отклика и снижения стоимости.
В некоторых случаях эти оптимизации определяют части данных, не относящихся к результату запроса, — стоимость сканирования таких данных снижается на 98%.

Влияние оптимизаций сканирования Grail варьируется в зависимости от атрибутов данных и запросов.
Оно может изменяться по мере того, как Dynatrace продолжает совершенствовать интеллект запросов Grail.

## Отслеживание потребления

В этом разделе описываются различные инструменты Dynatrace, которые можно использовать для отслеживания потребления и расходов.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенную метрику использования, помогающую понять и анализировать потребление вашей организацией Log Management & Analytics — Query.
Для использования этой метрики введите `DPS` в поле **Search** в Data Explorer.

Log Management & Analytics — Query
:   Ключ: `builtin:billing.log.query.usage`

    Измерение: байт

    Разрешение: 1 час

    Описание: количество байт, прочитанных при выполнении DQL-запроса, включая дискретизированные данные.

Пример использования метрики: мониторинг общего количества просканированных байт в почасовых интервалах

Вы можете отслеживать общее количество просканированных байт для [Query](#query) в почасовых интервалах за любой выбранный период времени с помощью метрики `builtin:billing.log.query.usage`.

В приведённом ниже примере показано использование, агрегированное с интервалом 1 час, за период с 2023-09-04 по 2023-09-11 (последние 7 дней).

![Log Management & Analytics - Query](https://dt-cdn.net/images/image034-806-25e7da895d.png)

### Отслеживание потребления с помощью DQL-запросов

Пример использования метрики: мониторинг общего количества просканированных гибибайт

Следующий DQL-запрос предоставляет обзор общего использования [Query](#query) в просканированных гибибайтах:

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

В приведённом ниже примере показано ежедневное использование запросов, визуализированное в виде линейного графика за последние 30 дней:

![Retain with included Queries (LMA)](https://dt-cdn.net/images/image-5-screenshot-2024-10-17-at-15-19-09-1243-832a39ebb6.png)

### Отслеживание потребления и расходов в Account Management

Вы также можете просматривать метрики использования в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Log Management & Analytics — Query**.

### Отслеживание потребления и расходов через API

Вы можете запрашивать метрики через [Environment API — Metrics API v2](../../../dynatrace-api/environment-api/metric-v2.md "Получайте информацию о метриках через Metrics v2 API.").

## Связанные темы

* [Log Analytics (DPS)](../log-analytics.md "Узнайте, как рассчитывается потребление Dynatrace Log Analytics с использованием модели подписки Dynatrace Platform Subscription.")
* [Что такое Dynatrace Grail?](../../../platform/grail/dynatrace-grail.md "Grail — это хранилище данных Dynatrace, специально разработанное для данных наблюдаемости и безопасности и выступающее единым унифицированным хранилищем журналов, метрик, трассировок, событий и многого другого.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [Лицензирование Dynatrace](../../../license.md "О модели лицензирования Dynatrace Platform Subscription (DPS) для всех возможностей Dynatrace.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
