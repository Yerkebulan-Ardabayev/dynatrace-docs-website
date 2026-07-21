---
title: Анализ отдельных пользовательских действий в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/analyze-individual-user-actions
---

# Анализ отдельных пользовательских действий в RUM Classic

# Анализ отдельных пользовательских действий в RUM Classic

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 19 июля 2017 г.

Страницы с подробностями о пользовательском действии дают быстрый доступ ко всем релевантным данным о нём, предоставляя всю информацию, необходимую для понимания того, что влияет на производительность каждого из пользовательских действий.

Чтобы перейти к странице с подробностями о пользовательском действии

1. Перейти в **Web**.
2. Выбрать приложение.
3. Прокрутить вниз до раздела **Top user actions** и выбрать **View full details**.
4. Выбрать действие, указанное в **Key user actions** или **Top 100 user actions**.

В зависимости от того, какое пользовательское действие нужно проанализировать, можно также напрямую выбрать одно из действий, показанных в разделе **Top user actions**.

На странице с подробностями о пользовательском действии можно выбрать области инфографики в верхней части страницы, чтобы перейти к соответствующему разделу страницы, связанному с каждой сводной метрикой, или ввести строку в поле **Filter user types**, чтобы просмотреть данные, специфичные для реальных пользователей или синтетического мониторинга.

![Action details 1](https://dt-cdn.net/images/32-actiondetails-1-1423-b88f87bd5b.png)

Action details 1

![Action details 2](https://dt-cdn.net/images/33-actiondetails-2-1423-f9e6a23325.png)

Action details 2

## Performance

В разделе **Performance** можно просмотреть влияние активности пользователей на производительность, ознакомиться с различными [показателями, влияющими на производительность](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") и увидеть распределение для выбранной метрики производительности.

![Performance](https://dt-cdn.net/images/performance-2285-289d4f850e.png)

Performance

## Диаграмма разбивки по показателям, влияющим на производительность, и waterfall-анализ

При анализе пользовательских действий один из главных вопросов, требующих ответа: на каком уровне расходуется больше всего времени отклика? Было ли больше времени затрачено на фронтенде (в основном в браузере), в сети или на сервере? Диаграмма **Contributor breakdown** даёт быстрый обзор времени, затраченного на фронтенде, в сети и на сервере. Для полного [waterfall-анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") отдельных пользовательских действий нужно выбрать **View analysis in waterfall chart**, чтобы увидеть, какие ресурсы влияют на длительность действия.

![User actions](https://dt-cdn.net/images/actions-2285-9af9ca267d.png)

User actions

## Apdex rating

Dynatrace использует [оценки Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для расчёта удовлетворённости пользователей. Выбрав **Apdex rating**, можно просмотреть удовлетворённость пользователей за указанный период времени для конкретного пользовательского действия.

![Apdex](https://dt-cdn.net/images/apdex-actions-2291-8bcf39ab96.png)

Apdex

## Loaded resources

Раздел **Loaded resources** содержит обзор категорий загружаемых ресурсов и их влияния на длительность действия.

![Loaded resources](https://dt-cdn.net/images/loaded-resources-2251-3786b5042a.png)

Loaded resources

## User action properties

В этом разделе перечислены свойства пользовательского действия, [определённые для конкретного пользовательского действия](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). Выбрав одно свойство, можно просмотреть данные, зафиксированные с помощью этого свойства.

![User action properties](https://dt-cdn.net/images/properties-2284-38c4617813.png)

User action properties

## Problems

Раздел [**Problems**](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.") показывает проблемы, автоматически обнаруженные Davis, движком причинно-следственного анализа на основе ИИ от Dynatrace. Достаточно выбрать проблему, чтобы узнать подробности.

![Problems](https://dt-cdn.net/images/problems-actions-2259-a04f530ffa.png)

Problems

## Errors

Выбрать **Errors**, чтобы просмотреть анализ [ошибок](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") по двум разным измерениям: тип ошибки ([JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors."), request и пользовательские ошибки) и источник (первая сторона, третья сторона или CDN).

Также можно просмотреть наиболее часто встречающиеся ошибки JavaScript в этом пользовательском действии за указанный [период времени](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings."). Выбрать **Analyze errors**, чтобы перейти на [страницу многомерного анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions."), где можно выполнить многомерный анализ с точки зрения **Errors**, в сочетании с измерением типа, контекста или источника соответственно. На этой странице, выбрав конкретную ошибку из списка **Error**, можно перейти на [страницу с подробностями об ошибке](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#error-details-page "Learn about user session segmentation and filtering attributes.").

![User action details page - Errors](https://dt-cdn.net/images/user-action-page-error-2283-670dd35d85.png)

User action details page - Errors

## Top segments

Этот раздел содержит разбивку по **Browsers**, **Users** и **Geolocations** и показывает метрики по этим измерениям для конкретного пользовательского действия.

![Segments](https://dt-cdn.net/images/segments-2249-32b57f8e1b.png)

Segments

## Top 3 web request contributors

Этот раздел показывает **Top 3 web request contributors**, то есть три службы на стороне сервера, которые потребили больше всего суммарного времени. Выбрать **View full details**, чтобы просмотреть полный список факторов, влияющих на веб-запросы.

![User action contributors](https://dt-cdn.net/images/contributors-2261-af12bd0f24.png)

User action contributors

## Compare JavaScript errors with user actions

В этом разделе показан процент пользовательских действий, на которые повлияли ошибки JavaScript за указанный [период времени](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

![Javascript errors vs actions](https://dt-cdn.net/images/js-errors-2253-a4fad35c29.png)

Javascript errors vs actions