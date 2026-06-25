---
title: Анализ отдельных пользовательских действий
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions
scraped: 2026-05-12T11:34:59.369496
---

# Анализ отдельных пользовательских действий

# Анализ отдельных пользовательских действий

* How-to guide
* 3-min read
* Published Jul 19, 2017

Страницы сведений о пользовательских действиях предоставляют быстрый доступ ко всем соответствующим данным, что позволяет получить всю необходимую информацию о факторах, влияющих на производительность каждого пользовательского действия.

Чтобы перейти на страницу сведений о пользовательском действии:

1. Перейдите в **Web**.
2. Выберите приложение.
3. Прокрутите страницу вниз до раздела **Top user actions** и выберите **View full details**.
4. Выберите действие из списка **Key user actions** или **Top 100 user actions**.

В зависимости от того, какое пользовательское действие нужно проанализировать, можно также напрямую выбрать одно из действий в разделе **Top user actions**.

На странице сведений о пользовательском действии выберите области инфографики в верхней части страницы для перехода к соответствующему разделу для каждой сводной метрики, или введите строку в поле **Filter user types** для просмотра данных, специфичных для реальных пользователей или синтетического мониторинга.

![Action details 1](https://dt-cdn.net/images/32-actiondetails-1-1423-b88f87bd5b.png)

Action details 1

![Action details 2](https://dt-cdn.net/images/33-actiondetails-2-1423-f9e6a23325.png)

Action details 2

## Производительность

В разделе **Performance** можно просматривать влияние активности пользователей на производительность, изучать различные [факторы производительности](/managed/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") и видеть распределение для выбранной метрики производительности.

![Performance](https://dt-cdn.net/images/performance-2285-289d4f850e.png)

Performance

## График разбивки по факторам и анализ водопада

При анализе пользовательских действий один из основных вопросов — на каком уровне расходуется наибольшее время ответа? Было ли больше времени потрачено на фронтенд (преимущественно в браузере), сеть или сервер? График **Contributor breakdown** даёт быстрый обзор времени, затраченного на фронтенд, сеть и сервер. Для полного [анализа водопада](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") отдельных пользовательских действий выберите **View analysis in waterfall chart**, чтобы увидеть, какие ресурсы влияют на продолжительность действия.

![User actions](https://dt-cdn.net/images/actions-2285-9af9ca267d.png)

User actions

## Рейтинг Apdex

Dynatrace использует [рейтинги Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для оценки удовлетворённости пользователей. Выбрав **Apdex rating**, можно просмотреть удовлетворённость пользователей в указанном временном диапазоне для конкретного пользовательского действия.

![Apdex](https://dt-cdn.net/images/apdex-actions-2291-8bcf39ab96.png)

Apdex

## Загруженные ресурсы

Раздел **Loaded resources** содержит обзор категорий загруженных ресурсов и их влияния на продолжительность действия.

![Loaded resources](https://dt-cdn.net/images/loaded-resources-2251-3786b5042a.png)

Loaded resources

## Свойства пользовательских действий

В этом разделе перечислены свойства пользовательских действий, [определённые для конкретного пользовательского действия](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). Выбрав одно свойство, можно просмотреть данные, захваченные через это свойство.

![User action properties](https://dt-cdn.net/images/properties-2284-38c4617813.png)

User action properties

## Проблемы

Раздел [**Problems**](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.") отображает проблемы, автоматически обнаруженные Davis — движком Dynatrace на основе ИИ для определения первопричин. Выберите проблему для просмотра подробностей.

![Problems](https://dt-cdn.net/images/problems-actions-2259-a04f530ffa.png)

Problems

## Ошибки

Выберите **Errors** для просмотра анализа [ошибок](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") по двум измерениям: тип ошибки ([JavaScript](/managed/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors."), запросы и пользовательские ошибки) и происхождение (собственные, сторонние или CDN).

Также можно просматривать наиболее часто встречающиеся ошибки JavaScript в данном пользовательском действии за указанный [временной диапазон](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings."). Выберите **Analyze errors** для перехода на [страницу многомерного анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."), где можно выполнить многомерный анализ с точки зрения ошибок в сочетании с измерениями типа, контекста или происхождения. На этой странице при выборе конкретной ошибки из списка **Error** открывается [страница сведений об ошибке](/managed/observe/digital-experience/session-segmentation/new-user-sessions#error-details-page "Learn about user session segmentation and filtering attributes.").

![User action details page - Errors](https://dt-cdn.net/images/user-action-page-error-2283-670dd35d85.png)

User action details page - Errors

## Топ сегментов

В этом разделе представлена разбивка по **Browsers**, **Users** и **Geolocations** с метриками по этим измерениям для конкретного пользовательского действия.

![Segments](https://dt-cdn.net/images/segments-2249-32b57f8e1b.png)

Segments

## Топ-3 факторов веб-запросов

В этом разделе показаны **Top 3 web request contributors** — три серверных сервиса с наибольшим суммарным временем обработки. Выберите **View full details** для просмотра полного списка факторов веб-запросов.

![User action contributors](https://dt-cdn.net/images/contributors-2261-af12bd0f24.png)

User action contributors

## Сравнение ошибок JavaScript с пользовательскими действиями

В этом разделе показан процент пользовательских действий, затронутых ошибками JavaScript за указанный [временной диапазон](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

![Javascript errors vs actions](https://dt-cdn.net/images/js-errors-2253-a4fad35c29.png)

Javascript errors vs actions