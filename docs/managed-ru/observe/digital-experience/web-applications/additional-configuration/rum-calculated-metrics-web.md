---
title: Создание вычисляемых метрик для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web
scraped: 2026-05-12T11:07:09.084282
---

# Создание вычисляемых метрик для веб-приложений

# Создание вычисляемых метрик для веб-приложений

* How-to guide
* 2-min read
* Updated on May 10, 2024

В Dynatrace можно создавать вычисляемые метрики для использования в [построении графиков](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [работе с API](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). Вычисляемые метрики также можно применять для настройки пользовательских оповещений.

Выбрав интересующее приложение, можно использовать **Multidimensional Analysis** для выбора аспектов пользовательских действий и создания вычисляемой метрики. Можно разделить выбранные метрики производительности по дополнительному измерению — например, по геолокации, браузеру или типу ошибки — или использовать только одно измерение, например [свойства пользовательских действий](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

![Dashboard with custom charts based on calculated metrics](https://dt-cdn.net/images/image-19-1916-a1098d2ab4.png)

Dashboard with custom charts based on calculated metrics

## Создание метрики

Чтобы создать вычисляемую метрику для приложения:

1. Перейдите в **Web** и выберите приложение, для которого нужно создать метрику.
2. Прокрутите страницу вниз до раздела **Impact of user actions on performance** и выберите **Analyze performance**.
3. На странице **User action analysis** выберите нужный временной диапазон, параметры и фильтры.
4. Выберите один из вариантов **Analyze by** и метрику производительности, для которой нужно создать вычисляемую метрику.
5. Необязательно: используйте панель фильтров, чтобы добавить фильтры по геолокации, версиям браузеров, свойствам пользовательских действий и т.д. для уточнения результирующей метрики.
6. Выберите **Create metric**.

   ![Creating a metric on the Multidimensional analysis page](https://dt-cdn.net/images/createmetric-1896-0987193fdb.png)

   Creating a metric on the Multidimensional analysis page
7. Необязательно: измените имя и ключ метрики и включите **Split by <dimension name>**.
8. Необязательно: выберите **Advanced options**, если нужно дополнительно указать или изменить следующие параметры.

   * Metric
   * Metric name
   * Metric key for API usage
   * Filters
   * Split-by parameters
9. Выберите **Create metric**.

Используйте метрику для создания пользовательского графика или оповещения.

В вычисляемые метрики записываются только новые данные; ретроспективные данные не включаются.

Можно создать до 500 включённых вычисляемых метрик на среду для всех приложений и до 100 включённых вычисляемых метрик на приложение.

### Пример

В этом примере рассмотрим анализ свойства `Price`, которое является [свойством пользовательского действия](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties#custom-properties "Define custom string, numeric, and date properties for your monitored web applications."), с фильтрацией по `Loyalty status` — другому свойству пользовательского действия.

На странице **Multidimensional analysis** выберите временной диапазон анализа. Чтобы отфильтровать цены, уплаченные только платиновыми клиентами, в списке **Analyze by** выберите `Price` и добавьте фильтры: `String property`, `Loyalty status` и `Platinum`.

![Example - Revenue by platinum customers](https://dt-cdn.net/images/loyalty-status-example-1385-0549af2191.png)

Example - Revenue by platinum customers

Также можно создать метрику и сгенерировать пользовательский график.

![Example - Create a metric](https://dt-cdn.net/images/example-create-metric-320-b73577057f.png)

Example - Create a metric

## Создание пользовательских графиков на основе вычисляемых метрик

Создание графиков помогает анализировать комбинации метрик приложения непосредственно на дашборде. Можно разделять и фильтровать доступные сущности для настройки измерений метрик на графиках.

Подробнее о создании графиков и их закреплении на дашбордах см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

## Управление метриками

После создания вычисляемой метрики можно просматривать её свойства, удалять её, временно отключать или создавать для неё график либо событие по метрике.

После создания метрики изменить её свойства нельзя.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Metrics**.
5. Выберите метрику, которой нужно управлять, и проверьте её свойства или выполните одно из следующих действий.

   * **Включить или отключить** ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") метрику
   * **Copy** — скопировать URL API для метрики
   * **Create a chart** — создать график с помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
   * **Create alert** — создать [событие по метрике](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
   * **Analyze** — открыть представление [многомерного анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.") для метрики
   * **Delete metric** — удалить метрику

## Связанные темы

* [Web application metrics API](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")