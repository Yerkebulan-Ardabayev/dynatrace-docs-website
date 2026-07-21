---
title: Создание вычисляемых метрик для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-calculated-metrics-web
---

# Создание вычисляемых метрик для веб-приложений в RUM Classic

# Создание вычисляемых метрик для веб-приложений в RUM Classic

* Практическое руководство
* Чтение 2 мин.
* Обновлено 10 мая 2024 г.

В Dynatrace можно создавать вычисляемые метрики, чтобы сделать текущий анализ доступным для [построения графиков](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [использования через API](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). Вычисляемые метрики также можно использовать для добавления пользовательских оповещений.

После выбора нужного приложения можно воспользоваться **Multidimensional Analysis**, чтобы выбрать аспекты пользовательских действий и создать вычисляемую метрику. Можно разбить выбранные метрики производительности по другому измерению, например по геолокации, браузеру и типу ошибки, либо использовать только отдельные измерения, такие как [свойства пользовательского действия](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

![Dashboard with custom charts based on calculated metrics](https://dt-cdn.net/images/image-19-1916-a1098d2ab4.png)

Дашборд с пользовательскими графиками на основе вычисляемых метрик

## Создание метрики

Чтобы создать вычисляемую метрику на основе приложения

1. Перейти в **Web** и выбрать приложение, для которого нужно создать метрику.
2. Прокрутить вниз до **Impact of user actions on performance** и выбрать **Analyze performance**.
3. На странице **User action analysis** выбрать нужный период времени, параметры и фильтры.
4. Выбрать один из вариантов **Analyze by** и метрику производительности, для которой нужно создать метрику.
5. Опционально: с помощью панели фильтров добавить фильтры по геолокациям, версиям браузера, свойствам пользовательского действия и другим параметрам, чтобы сфокусировать итоговую метрику на нужных данных.
6. Выбрать **Create metric**.

   ![Creating a metric on the Multidimensional analysis page](https://dt-cdn.net/images/createmetric-1896-0987193fdb.png)

   Создание метрики на странице Multidimensional analysis
7. Опционально: изменить имя и ключ метрики и включить **Split by <dimension name>**.
8. Опционально: выбрать **Advanced options**, если нужно дополнительно указать или изменить следующие параметры.

   * Metric
   * Metric name
   * Metric key для использования через API
   * Filters
   * Split-by parameters
9. Выбрать **Create metric**.

Метрику можно использовать для создания пользовательского графика или оповещения.

В вычисляемые метрики записываются только новые данные, ретроспективные данные не включаются.

В каждой среде можно иметь до 500 включённых вычисляемых метрик по всем приложениям и до 100 включённых вычисляемых метрик на одно приложение.

### Пример

В этом примере проанализируем `Price`, это [свойство пользовательского действия](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties#custom-properties "Define custom string, numeric, and date properties for your monitored web applications."), и отфильтруем его по `Loyalty status`, ещё одному свойству пользовательского действия.

На странице **Multidimensional analysis** выбирается период анализа. Чтобы отфильтровать цены, оплаченные только клиентами уровня platinum, в списке **Analyze by** выбирается `Price`, после чего устанавливаются дополнительные фильтры путём выбора `String property`, `Loyalty status` и `Platinum`.

![Example - Revenue by platinum customers](https://dt-cdn.net/images/loyalty-status-example-1385-0549af2191.png)

Пример: выручка по клиентам уровня platinum

Также можно создать метрику и построить на её основе пользовательский график.

![Example - Create a metric](https://dt-cdn.net/images/example-create-metric-320-b73577057f.png)

Пример: создание метрики

## Создание пользовательских графиков на основе вычисляемых метрик

Создание графиков помогает анализировать комбинации метрик приложения прямо на дашборде. Доступные сущности можно разбивать и фильтровать, чтобы точно настроить измерения метрики, отображаемые на графиках, и отфильтровать сущности, релевантные именно вам.

Подробнее о создании графиков и закреплении их на дашбордах см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

## Управление метриками

После создания вычисляемой метрики можно просматривать её свойства, удалять её, временно отключать, а также создавать для неё график или событие метрики.

После создания метрики изменить её свойства нельзя.

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Metrics**.
5. Выбрать метрику, которой нужно управлять, и проверить её свойства либо выполнить одно из следующих действий.

   * **Enable or disable** ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") метрику
   * **Copy** URL API для метрики
   * **Create a chart** с помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
   * **Create alert** для создания [события метрики](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
   * **Analyze**, чтобы открыть представление [многомерного анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions.") для метрики
   * **Delete metric**

## Похожие темы

* [Метрики веб-приложений API](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")