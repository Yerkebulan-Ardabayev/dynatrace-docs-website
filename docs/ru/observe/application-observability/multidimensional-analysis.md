---
title: Multidimensional analysis
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis
scraped: 2026-03-06T21:17:27.365659
---

# Многомерный анализ

# Многомерный анализ

* Classic
* How-to guide
* 4-min read
* Updated on Sep 13, 2022

Представление **Multidimensional analysis** позволяет анализировать веб-запросы ваших сервисов с детальной фильтрацией, что даёт возможность сосредоточить анализ на наиболее важных измерениях. Это представление легко настраивается и служит удобной отправной точкой для углублённого анализа ваших сервисов.

С помощью многомерного анализа вы можете исследовать пользовательские представления: **Top web requests**, **Database statements** и **Exception analysis**.

Чтобы перейти на страницу **Multidimensional analysis**

1. Перейдите в **Multidimensional Analysis**.
2. Выберите один из вариантов анализа для исследования или **Create analysis view**.

## Предопределённые представления

[### Top web requests

Анализ наиболее частых и наиболее ресурсоёмких веб-запросов.](multidimensional-analysis/top-web-requests.md "Learn how to analyze all web requests across all of your services using Dynatrace.")[### Top database statements

Анализ наиболее частых и наиболее ресурсоёмких запросов к базам данных.](multidimensional-analysis/top-database-statements.md "Understand the database activity across your environment with Dynatrace.")[### Exception analysis

Анализ и понимание всех исключений на уровне кода.](multidimensional-analysis/exception-analysis.md "Learn how Dynatrace can help you see which exceptions occurred in your environment during a selected analysis timeframe.")

## Источник данных

Многомерный анализ использует данные трассировок и запросов в качестве источника данных, включая информацию о [распределённых трассировках](../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md#traces-grail "Check retention times for various data types.") и [запросах](../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md#request-attributes "Check retention times for various data types.").

* Для временных интервалов менее двух часов используется более высокое разрешение (менее 1 минуты).
* Для больших объёмов данных, особенно для длительных временных интервалов или нефильтрованного анализа, применяется выборка (сэмплирование): используется только часть данных трассировок и запросов.
* Для просмотра информации о данных, используемых для анализа, и рекомендаций по повышению точности наведите курсор на **Refine**.
* Чтобы включить больше данных в анализ, выберите **Refine**.

Многомерный анализ и диаграммы

В отличие от [Data Explorer](../../analyze-explore-automate/explorer.md#limitations "Query for metrics and transform results to gain desired insights."), многомерный анализ использует данные трассировок и запросов, а не данные метрик, поэтому значения на диаграммах многомерного анализа могут отличаться от значений на пользовательских диаграммах.

## Настройка представления

В разделе **Configure view** вы можете настроить множество возможностей фильтрации. Представление автоматически обновляется при изменении параметров.

Вы можете экспортировать табличные данные в файл формата CSV (значения, разделённые запятыми).

1. В правом нижнем углу страницы выберите **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

   ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
2. Выберите **Export visible data** или **Export table data**.

## Представление

![Top database statements page](https://dt-cdn.net/images/top-database-statements-3564-3bd08ea1b1.png)

На диаграмме отображаются 15 основных измерений (все остальные измерения агрегируются в одно), а таблица ниже содержит до 85 дополнительных измерений, что в сумме составляет до 100 отображаемых измерений. Представление мгновенно адаптируется к изменениям, которые вы вносите в панели **Configure view**.

В столбце **Actions** таблицы вы можете выбрать:

* **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") для фильтрации представления по указанному измерению.
* **More** (**...**) для доступа к дополнительным вариантам анализа из [меню **Analyze**](services-classic/context-specific-drill-down.md#analyze-menu "Learn about easy navigation and filtering for services analysis.").

Для временных интервалов, содержащих данные старше 10 дней, вы можете включить **Show data retention**, чтобы лучше понять, какие данные доступны за какой период, непосредственно на диаграмме.

### Сохранение представления

После настройки представления вы можете сохранить его для быстрого доступа в будущем. Просто выберите **Save** и укажите имя.

Dynatrace предоставляет несколько предустановленных представлений:

* [Exception analysis](multidimensional-analysis/exception-analysis.md "Learn how Dynatrace can help you see which exceptions occurred in your environment during a selected analysis timeframe.")
* [Top database statements](multidimensional-analysis/top-database-statements.md "Understand the database activity across your environment with Dynatrace.")
* [Top web requests](multidimensional-analysis/top-web-requests.md "Learn how to analyze all web requests across all of your services using Dynatrace.")

## Вычисляемая метрика сервиса

Вы можете сохранить настроенное представление как вычисляемую метрику сервиса, которую можно использовать так же, как любую другую метрику Dynatrace, например, для [построения диаграмм](../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") или [экспорта данных через API](../../dynatrace-api/environment-api/metric-v2/get-data-points.md "Read data points of one or multiple metrics via Metrics v2 API.").

В вычисляемые метрики записываются только новые данные; ретроспективные данные не включаются.

Ограничения

* В вычисляемые метрики записываются только новые данные; ретроспективные данные не включаются.
* Вы можете иметь до 500 включённых вычисляемых метрик на окружение и до 100 включённых вычисляемых метрик на сервис.
* Классические вычисляемые метрики поддерживают не более 100 значений измерений. Это называется правилом «top X», поскольку в зависимости от конфигурации можно выбрать меньше. Однако, какие бы 100 значений измерений вы ни выбрали, оставшиеся измерения агрегируются в один временной ряд, и значение измерения доступно через специальное измерение `remainder`. Условие фильтрации [remainder](../../dynatrace-api/environment-api/metric-v2/metric-selector.md#remainder "Configure the metric selector for the Metric v2 API.") позволяет фильтровать по этому измерению `remainder`.

* Вычисляемые метрики сервиса Grail с кардинальностью выше 2000 в любом 5-минутном окне за последние 2 недели или с момента последнего изменения метрики автоматически отключаются в Grail. Включение таких метрик в Grail не допускается. Если метрика уже включена в Grail, вы будете уведомлены об отклонении метрики через готовый дашборд [**Metric & Dimensions Usage + Rejections**](../../dynatrace-api/environment-api/metric-v2/best-practices.md#identify-high-cardinality-situations "Best practices for metrics."). Чтобы включить классическую метрику в Grail и продолжить сбор входящих данных в Grail, убедитесь, что кардинальность остаётся ниже лимита.

Чтобы создать вычисляемую метрику сервиса из представления многомерного анализа

1. Перейдите в **Multidimensional Analysis**.
2. Выберите **Create analysis view**.
3. Необязательно: выберите зону управления. Новая метрика будет ограничена данными из этой зоны.
4. Настройте представление. Описание доступных параметров приведено в разделе [**Configure view**](#configure) выше.
5. В панели **View** выберите **Create metric**.

   ![Create calculated metric](https://dt-cdn.net/images/service-calculated-metric-create-328-e5859c1ea9.png)
6. Укажите имя для метрики. Имя автоматически добавляется к ключу метрики.
7. Необязательно: при необходимости измените ключ метрики.

   После создания метрики её ключ изменить нельзя.
8. Необязательно: если вы хотите более точно настроить метрику, выберите **Advanced options** для настройки дополнительных параметров метрики. Подробности см. в разделе [Вычисляемые метрики для сервисов](services/calculated-service-metric.md "Learn how to create a calculated metric based on web requests.").
9. Выберите **Create metric**.

## Связанные темы

* [API метрик сервиса](../../dynatrace-api/configuration-api/calculated-metrics/service-metrics.md "Manage calculated service metrics via the Dynatrace configuration API.")
* [Вычисляемые метрики для сервисов](services/calculated-service-metric.md "Learn how to create a calculated metric based on web requests.")