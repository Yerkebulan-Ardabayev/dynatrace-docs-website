---
title: Многомерный анализ для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis
scraped: 2026-05-12T11:31:25.796328
---

# Многомерный анализ для веб-приложений

# Многомерный анализ для веб-приложений

* How-to guide
* 8-min read
* Published Jun 28, 2019

Dynatrace Real User Monitoring позволяет детально анализировать [пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") по множеству измерений. Страницы многомерного **User action analysis** доступны из множества точек входа в Dynatrace. В зависимости от начальной точки анализа могут быть применены предварительно выбранные фильтры, которые сохраняются при дальнейшем анализе.

Ниже представлены основные сценарии входа для использования представлений многомерного **User action analysis**.

Сценарий 1: Анализ по типу пользовательского действия

Dynatrace различает **Load actions**, **XHR actions** и **Custom actions** (см. ниже), что позволяет применять оптимальные метрики производительности для каждого типа действия. Это обеспечивает сфокусированный, контекстуальный анализ каждого типа пользовательских действий.

Чтобы перейти к многомерному анализу по типу пользовательского действия:

1. Перейдите в **Web**.
2. Выберите приложение для анализа.
3. В разделе **Impact of user actions on performance** выберите **Analyze Performance** для открытия представления **User action analysis**.

   ![Multidimensional analysis](https://dt-cdn.net/images/application-overview-screen-key-performance-filter1-1066-39375d615b.png)

   Multidimensional analysis

   Верхняя часть страницы многомерного **User action analysis** содержит основные параметры фильтрации для фокусировки анализа на конкретных типах пользовательских действий.
4. Из списков фильтров в верхней части страницы выберите нужные значения для фильтрации по **Action type**, **User type**, **Performance metric** и **Contribution** (см. изображение ниже).
5. Из раскрывающегося списка **Analyze user actions during the past…** выберите длительность временного диапазона для анализа.
6. Выберите на графике временной шкалы диапазон для анализа. В нижней части представления отображается более детальное многомерное аналитическое представление пользовательских действий с применёнными основными фильтрами.

![Multi-dimensional analysis](https://dt-cdn.net/images/multi-dimensional-primary-grouping-filter-and-metric-selsection-1600-15378e6362.png)

Multi-dimensional analysis

7. Необязательно: выберите **Filtered by** для добавления дополнительных фильтров. Доступны фильтры по продолжительности действия, Apdex, ошибкам JavaScript, типу пользователя, браузеру, расположению и другим параметрам. Ниже отображается список всех **Key user actions**, соответствующих критериям фильтра, и **Top 100 user actions** (этот список изначально отсортирован по общему затраченному времени, но можно также сортировать по ошибкам JavaScript, количеству действий или продолжительности).

![Multi-dimensional analysis](https://dt-cdn.net/images/multi-dimensional-analytics-screen-analytics-section1-870-aac5976141.png)

Multi-dimensional analysis

8. Выберите пользовательское действие для более детального анализа. Это открывает представление **User actions view** для выбранного пользовательского действия. Как видно, заданные фильтры и временной диапазон анализа применяются к анализу на этой странице.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/specific-user-action-with-filters-applied-from-multi-dimensional-user-action-analytics1-1600-e9ba1dc253.png)

   Multi-dimensional analysis

   Применённые фильтры и временной диапазон анализа переносятся даже в [представление **Waterfall analysis**](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") (см. ниже).

   ![Multi-dimensional analysis](https://dt-cdn.net/images/specific-waterfall-for-user-action-with-filters-applied-from-multi-dimensional-user-action-analytics-screen3-1600-bc8c0f6bd6.png)

   Multi-dimensional analysis

Сценарий 2: Анализ по типу браузера

Иногда необходимо выяснить, сталкиваются ли пользователи одного типа браузера с одинаковыми проблемами производительности.

Чтобы перейти к многомерному анализу по типу браузера:

1. Перейдите в **Web**.
2. Выберите приложение для анализа.
3. В инфографике **Performance analysis** выберите плитку **Top browser** в верхнем левом углу для отображения раздела **Browser breakdown**.
4. Выберите **Analyze performance** в нижней части раздела.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/1-application-overview-with-top-browser-insights-break-down-1600-f554e6b3c2.png)

   Multi-dimensional analysis

   Открывается представление **Multidimensional analysis**, в котором режим анализа установлен на **Browsers** (см. ниже).
5. Из списков фильтров в верхней части страницы выберите нужные значения для фильтрации по **Action type**, **User / browser type**, **Performance metric** и **Contribution**.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/browser-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-5e523dfa54.png)

   Multi-dimensional analysis
6. Выберите длительность из раскрывающегося списка временного диапазона анализа.
7. Выберите на графике временной шкалы диапазон для анализа. Здесь можно точно определить и проанализировать только те пользовательские действия, которые актуальны для анализа.

Сценарий 3: Анализ по типу пользователя

Иногда необходимо узнать больше о ботах, сканирующих сайт, — например, при работе над оптимизацией для поисковых систем (SEO), или просто посмотреть на «чистый» запрос, выполненный через Synthetic Monitoring.

Чтобы перейти к многомерному анализу по типу пользователя:

1. Перейдите в **Web**.
2. Выберите приложение для анализа.
3. В инфографике **Performance analysis** выберите плитку **Top user type** в верхнем левом углу для отображения раздела типов пользователей.
4. Выберите **Analyze performance** в нижней части раздела.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/0-application-overview-with-user-type-break-down-1600-652da6c2f1.png)

   Multi-dimensional analysis

   Открывается многомерное представление **User action analysis**, в котором выделены различные типы пользователей, выполнявших анализируемые пользовательские действия. Список **Analyze by** в разделе **Multidimensional analysis** предварительно настроен на **Browsers**.
5. Из списков фильтров в верхней части страницы выберите нужные значения для фильтрации по **Action type**, **Performance metric** и **Contribution**.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/user-type-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-f2e40b76ae.png)

   Multi-dimensional analysis
6. Выберите длительность из раскрывающегося списка временного диапазона анализа.
7. Выберите на графике временной шкалы диапазон для анализа. Здесь можно точно определить и проанализировать только интересующие пользовательские действия.

Сценарий 4: Анализ по геолокации

В этом сценарии основное внимание уделяется поиску пользовательских действий из конкретного географического региона. Например, если добавлена CDN для определённого региона и нужно понять, насколько хорошо она работает.

Чтобы перейти к многомерному анализу по геолокации:

1. Перейдите в **Web**.
2. Выберите приложение для анализа.
3. В инфографике **Performance analysis** выберите плитку **View geolocation breakdown** в нижнем левом углу для отображения раздела **Geolocation breakdown**.
4. Выберите **Analyze performance** в нижней части раздела.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/2-application-overview-with-geo-location-break-down-1600-945b822f7e.png)

   Multi-dimensional analysis

   Открывается многомерное представление **User action analysis** с топ-геолокациями, откуда поступают пользовательские действия.
5. Из списков фильтров в верхней части страницы выберите нужные значения для фильтрации по **Action type**, **User type**, **Performance metric** и **Contribution**.

![Multi-dimensional analysis](https://dt-cdn.net/images/geo-location-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-7d2031e084.png)

Multi-dimensional analysis

6. Выберите длительность из раскрывающегося списка временного диапазона анализа.
7. Выберите на графике временной шкалы диапазон для анализа. Здесь можно точно определить и проанализировать только пользовательские действия, актуальные для анализа.

Сценарий 5: Анализ по типу ошибки

![Multidimensional analysis](https://dt-cdn.net/images/multidimensional-analysis-5007-e664cf92d9.png)

Multidimensional analysis

Для веб-приложений Dynatrace классифицирует [ошибки](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") как **Request**, **Custom** и **JavaScript**, что позволяет применять фильтры и анализировать их по категориям. Это обеспечивает сфокусированный контекстуальный анализ каждого типа ошибок, обнаруженных в выбранном временном диапазоне.

Чтобы перейти к многомерному анализу по ошибкам:

1. Перейдите в **Web**.
2. Выберите приложение для анализа.
3. В инфографике **Performance analysis** выберите плитку **Errors by type** в нижнем левом углу для просмотра топ ошибок **Request**, **Custom** и **JavaScript**.
4. Выберите **Analyze errors** для перехода на страницу **Multidimensional analysis: Errors**.
5. Примените фильтры для просмотра конкретных ошибок в выбранном временном диапазоне, выбрав значения из следующих списков:

   * **Error type**: `Request`, `Custom` и `JavaScript`
   * **Context**: `Errors during user actions` и `Errors between user actions`
   * **Origin**: `1st party errors`, `3rd party errors` и `CDN errors`
6. Выберите **Show your errors** по `Type`, `Context` или `Origin`.
7. Выберите длительность из раскрывающегося списка диапазона анализа.
8. Выберите на графике временной шкалы диапазон для анализа. Здесь можно сузить анализ до актуальных ошибок.
9. Необязательно: выберите соответствующий тип ошибки в легенде для скрытия или отображения на графике.

![Error analysis](https://dt-cdn.net/images/error-analysis-2757-13832acb4e.png)

Error analysis

После использования **Overview** для выявления накопления ошибок можно также использовать карточку **Detail analysis** для выбранного временного диапазона для дальнейшего анализа.

1. Выберите одно из следующих измерений для анализа временного диапазона:

   * **Performance over time**
   * **Distribution**
   * **Browsers**
   * **Geolocation**
   * **Errors**
2. Выберите вариант группировки ошибок по `Type`, `Context` или `Origin`.
3. Необязательно: примените фильтр, выбрав поле ввода и нужный фильтр. Нажмите **Enter** и введите соответствующее значение фильтра.

![Analysis by error type](https://dt-cdn.net/images/error-analysis-1873-78a0287859.png)

Analysis by error type

В этом примере обнаружена ошибка `HTTP 500` в API бронирования. При выборе ошибки на странице сведений об ошибке отображается базовая информация:

* Как часто возникала ошибка
* Количество затронутых сессий и пользователей
* Элементы, такие как пользовательские действия, ОС, типы браузеров и расположения, участвовавшие в ошибке

В карточке сведений об ошибке можно найти дополнительную информацию — например, была ли ошибка обнаружена RUM JavaScript или OneAgent. При выборе **Edit detection rules for this error pattern** открывается страница редактирования шаблона ошибки веб-запроса. Кроме того, можно выбрать **Create detection rule based on this error pattern** для создания явного правила ошибки веб-запроса.

![Error details](https://dt-cdn.net/images/error-details-5093-27df9761b5.png)

Error details

Для дальнейшего расследования ошибки можно провести детальный анализ сессии одной из затронутых сессий, перечисленных в разделе **User sessions affected by the error**, чтобы узнать больше о том, где и как произошла ошибка. Такие функции, как [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers."), упрощают поиск и передачу информации об ошибках пользователей в организации.

![User details page](https://dt-cdn.net/images/user-sessions-to-user-details-page-1637-f01f4b8bf0.png)

User details page

![Session replay](https://dt-cdn.net/images/session-replay-1917-70e8439a06.png)

Session replay

Другой способ дальнейшего расследования ошибки — рассмотреть её с точки зрения пользовательского действия. Используйте фильтр по конкретной ошибке в карточке **Detail analysis** для выбранного временного диапазона, чтобы сузить интересующие ошибки, затем прокрутите страницу до **Key user actions** или **Top 100 user actions** для поиска связанных пользовательских действий. Выберите интересующее пользовательское действие для его анализа.

![Analyze errors by user action](https://dt-cdn.net/images/analyze-errors-by-user-action-2880-b1252314fe.png)

Analyze errors by user action

В качестве примера: на следующей странице показано, что ошибки могут быть интегрированы в анализ водопада в виде полосы или маркера в момент возникновения ошибки.

![Waterfall analysis](https://dt-cdn.net/images/waterfall-1863-b48855309b.png)

Waterfall analysis