---
title: Custom Metrics Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/custom-metrics-classic
scraped: 2026-05-12T11:24:20.554609
---

# Custom Metrics Classic (DPS)

# Custom Metrics Classic (DPS)

* 16-min read
* Updated on Jan 12, 2026

На этой странице описано, как потребляется и тарифицируется DPS-возможность Custom Metrics Classic.
Обзор возможности и основных функций см. в [Custom Metrics Classic](/managed/license/capabilities/platform-extensions#metrics "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: точки данных метрик

Единица измерения для расчёта пользовательских метрик — точка данных метрики.
Точка данных метрики — единичное измерение пользовательской метрики.
Каждая точка данных метрики, относящаяся к пользовательской метрике, потребляет дополнительную точку данных при каждом расчёте метрики.

## Расчёт вашего потребления

1. В **Hub** найдите облачный сервис или расширение, которое вы хотите использовать (например, Amazon S3, Azure Storage Account, Oracle Database, F5).
2. Определите, сколько пользовательских метрик Dynatrace принимает для данного сервиса или расширения.
3. Определите количество точек данных метрик на пользовательскую метрику.
4. Используйте приведённый пример в качестве руководства.

Если у вас одна пользовательская метрика, записываемая раз в минуту, годовое потребление составит 525,6 тыс. точек данных:

`1 точка данных × 60 мин × 24 ч × 365 дней = 525,6 тыс. точек данных/год`

Обратите внимание, что одна пользовательская метрика может иметь несколько измерений.
Например, если у вас одна и та же пользовательская метрика для 2 экземпляров облачного сервиса, вы потребляете 2 точки данных:

1. `cloud.aws.dynamo.requests.latency, dt.entity.dynamo\_db\_table=DYNAMO\_DB\_TABLE-41043ED33F90F271 21.78`
2. `cloud.aws.dynamo.requests.latency, dt.entity.dynamo\_db\_table=DYNAMO\_DB\_TABLE-707BF9DD5C975159 4.47`

`2 экземпляра × 1 точка данных × 60 мин × 24 ч × 365 дней = 1 051,2 тыс. точек данных/год`

Точки данных метрик тарифицируются не по количеству измерений, а по увеличенному числу точек данных метрик.
Если измерения добавляются, но количество точек данных метрик остаётся прежним, тарифицируемое потребление не меняется:

1. `cloud.aws.dynamo.requests.latency, dt.entity.dynamo\_db\_table=DYNAMO\_DB\_TABLE-41043ED33F90F271, Operation='DeleteItem' 21.78`
2. `cloud.aws.dynamo.requests.latency, dt.entity.dynamo\_db\_table=DYNAMO\_DB\_TABLE- 707BF9DD5C975159, Operation='DeleteItem' 4.47`

В данном случае потребляется то же количество точек данных, что и в примере выше.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Custom Metrics Classic в вашей организации.
Для использования в Data Explorer введите DPS в поле **Search**.
Эти метрики также доступны через Environment API и связаны в Account Management (**Usage summary** > **Custom Metrics Classic** > **Actions** > **View details**).
В таблице ниже перечислены метрики для мониторинга потребления Custom Metrics Classic в вашей организации.

(DPS) Recorded metric data points per metric key
:   Ключ: `builtin:billing.custom_metrics_classic.raw.usage_by_metric_key`

    Измерение: `metric_key\[STRING]`

    Разрешение: 1 мин

    Описание: Количество потреблённых точек данных метрик с разбивкой по ключу метрики.

(DPS) Total billable metric data points
:   Ключ: `builtin:billing.custom_metrics_classic.usage`

    Измерение: count

    Разрешение: 15 мин

    Описание: Общее количество точек данных метрик после вычета включённых точек данных.

(DPS) Total billable metric data points by other entities
:   Ключ: `builtin:billing.custom_metrics_classic.usage.other`

    Измерение: count

    Разрешение: 15 мин

    Описание: Количество тарифицируемых точек данных метрик, не включённых в мониторинг хостов.

(DPS) Billable metric data points reported and split by other entities
:   Ключ: `builtin:billing.custom_metrics_classic.usage.other_by_entity`

    Измерение: `dt.entity.monitored_entity\[ME:MONITORED_ENTITY]`

    Разрешение: 15 мин

    Описание: Количество тарифицируемых точек данных метрик с разбивкой по сущностям, не привязанным к хосту.

(DPS) Total metric data points billable for Full-Stack monitored hosts
:   Ключ: `builtin:billing.custom_metrics_classic.usage.fullstack_hosts`

    Измерение: count

    Разрешение: 15 мин

    Описание: Количество тарифицируемых точек данных метрик для хостов с Full-Stack мониторингом.

(DPS) Total metric data points billable for Infrastructure hosts
:   Ключ: `builtin:billing.custom_metrics_classic.usage.infrastructure_hosts`

    Измерение: count

    Разрешение: 15 мин

    Описание: Количество тарифицируемых точек данных метрик для хостов с Infrastructure мониторингом.

Суммарное количество тарифицируемых точек данных метрик за различные интервалы (15 мин, час, день или неделя) в любом выбранном периоде можно отслеживать с помощью метрики «(DPS) Total billed metric data points».
В примере ниже показано потребление, агрегированное в 1-часовых интервалах.

![Custom Metrics Classic (DPS)](https://dt-cdn.net/images/image048-720-a365c019d1.png)

Custom Metrics Classic (DPS)

Суммарное количество тарифицируемых точек данных метрик можно детализировать для просмотра потребления по хостам с Full-Stack мониторингом, хостам с Infrastructure мониторингом и прочим сущностям.
Для этого используются метрики: «(DPS) Total metric data points billed for Full-Stack hosts», «(DPS) Total metric data points billed for Infrastructure hosts» и «(DPS) Total metric data points billed by other entities».

В примере ниже показано количество тарифицируемых точек данных метрик, потреблённых всеми хостами Full-Stack, хостами Infrastructure и прочими сущностями.

![Custom Metrics Classic (DPS)](https://dt-cdn.net/images/image044-709-5de5ca2fb6.png)

Custom Metrics Classic (DPS)

Потребление точек данных метрик по любой отфильтрованной сущности можно отслеживать с помощью метрики «(DPS) Billed metric data points reported and split by other entities».
В примере ниже показано количество тарифицируемых точек данных метрик из Azure Storage Account.

![Custom Metrics Classic (DPS)](https://dt-cdn.net/images/image046-720-81567cdfe3.png)

Custom Metrics Classic (DPS)

Потребление точек данных метрик по ключу метрики можно отслеживать с помощью метрики «(DPS) Recorded metric data points per metric key».
В примере ниже перечислены топовые ключи метрик для Azure Storage Account в порядке убывания потребления.

![Custom Metrics Classic (DPS)](https://dt-cdn.net/images/image048-720-a365c019d1.png)

Custom Metrics Classic (DPS)

Вы можете легко управлять тарифицируемыми точками данных метрик для облачных сервисов — определять, какие точки данных наиболее ценны, и отключать менее ценные.
Например, узнайте, как это сделать для [Azure Storage Account](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account#configure-service-metrics "Monitor Azure Storage Account and view available metrics.").

## Связанные темы

* [Обзор расширений платформы (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)