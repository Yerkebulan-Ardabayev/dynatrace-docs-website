---
title: Многомерный анализ веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis
---

# Многомерный анализ веб-приложений в RUM Classic

# Многомерный анализ веб-приложений в RUM Classic

* Практическое руководство
* Чтение: 8 мин
* Опубликовано 28 июня 2019 г.

Dynatrace Real User Monitoring Classic позволяет глубоко погружаться в анализ [пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") по множеству измерений. Многомерные страницы **User action analysis** доступны из множества точек входа во всём Dynatrace. В зависимости от того, откуда начинается анализ, применяются заранее выбранные фильтры, которые сохраняются по мере продвижения анализа.

Ниже перечислены основные сценарии входа для работы с новейшими многомерными представлениями **User action analysis**.

Сценарий 1: анализ по типу пользовательского действия

Dynatrace различает **Load actions**, **XHR actions** и **Custom actions** (см. ниже), что позволяет применять оптимальные метрики производительности для каждого типа действия. Это обеспечивает сфокусированный, контекстный анализ каждого типа пользовательского действия.

Доступ к многомерному анализу по типу пользовательского действия

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать.
3. В разделе **Impact of user actions on performance** страницы выбрать **Analyze Performance**, чтобы открыть представление **User action analysis**.

   ![Multidimensional analysis](https://dt-cdn.net/images/application-overview-screen-key-performance-filter1-1066-39375d615b.png)

   Многомерный анализ

   Верхняя часть многомерной страницы **User action analysis** содержит основные параметры фильтрации, которые можно использовать, чтобы сфокусировать анализ на конкретных типах пользовательских действий.
4. В списках фильтров вверху страницы выбрать нужные значения для фильтрации по **Action type**, **User type**, **Performance metric** и **Contribution** (см. изображение ниже).
5. Выбрать длительность для периода анализа в выпадающем списке **Analyze user actions during the past…**.
6. Выбрать участок временной шкалы, чтобы задать период, который нужно проанализировать. В нижней части представления отображается более детальное, многомерное представление аналитики пользовательских действий со всеми применёнными основными фильтрами.

![Multi-dimensional analysis](https://dt-cdn.net/images/multi-dimensional-primary-grouping-filter-and-metric-selsection-1600-15378e6362.png)

Многомерный анализ

7. Необязательно Выбрать **Filtered by**, чтобы добавить дополнительные фильтры. Доступны фильтры по длительности действия, Apdex, ошибкам JavaScript, типу пользователя, браузеру, местоположению и другим параметрам. Ниже отображается список всех **Key user actions**, соответствующих заданным критериям фильтрации, а также **Top 100 user actions** (этот список изначально строится по общему затраченному времени, но его также можно фильтровать по ошибкам JavaScript, количеству действий или длительности.

![Multi-dimensional analysis](https://dt-cdn.net/images/multi-dimensional-analytics-screen-analytics-section1-870-aac5976141.png)

Многомерный анализ

8. Выбрать пользовательское действие, которое нужно исследовать подробнее. Это откроет представление **User actions view** для выбранного пользовательского действия (загрузка страницы `/special-offers.jsp` в примере ниже). Как видно, заданные фильтры и период анализа применены к анализу на этой странице.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/specific-user-action-with-filters-applied-from-multi-dimensional-user-action-analytics1-1600-e9ba1dc253.png)

   Многомерный анализ

   Применённые фильтры и период анализа переносятся даже в [**Waterfall analysis view**](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") (см. ниже).

   ![Multi-dimensional analysis](https://dt-cdn.net/images/specific-waterfall-for-user-action-with-filters-applied-from-multi-dimensional-user-action-analytics-screen3-1600-bc8c0f6bd6.png)

   Многомерный анализ

Сценарий 2: анализ по типу браузера

Иногда нужно понять, сталкиваются ли пользователи с одним и тем же типом браузера с одинаковыми проблемами производительности.

Доступ к многомерному анализу по типу браузера

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать.
3. В инфографике **Performance analysis** выбрать плитку **Top browser** в верхнем левом углу, чтобы отобразить раздел **Browser breakdown**.
4. Выбрать **Analyze performance** внизу раздела.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/1-application-overview-with-top-browser-insights-break-down-1600-f554e6b3c2.png)

   Многомерный анализ

   Это открывает представление **Multidimensional analysis**, где режим анализа установлен на **Browsers** (см. ниже).
5. В списках фильтров вверху страницы выбрать нужные значения для фильтрации по **Action type**, **User / browser type**, **Performance metric** и **Contribution**.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/browser-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-5e523dfa54.png)

   Многомерный анализ
6. Выбрать длительность в выпадающем списке периода анализа.
7. Выбрать участок временной шкалы, чтобы задать период, который нужно проанализировать. Отсюда можно определить и проанализировать только те пользовательские действия, которые относятся к анализу.

Сценарий 3: анализ по типу пользователя

Иногда нужно узнать больше о ботах, которые сканируют сайт, например потому что компания работает над поисковой оптимизацией (SEO), или просто нужно посмотреть «clean room request», выполненный через Synthetic monitoring.

Доступ к многомерному анализу по типу пользователя

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать.
3. В инфографике **Performance analysis** выбрать плитку **Top user type** в верхнем левом углу, чтобы отобразить раздел User type.
4. Выбрать **Analyze performance** внизу раздела.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/0-application-overview-with-user-type-break-down-1600-652da6c2f1.png)

   Многомерный анализ

   Это открывает многомерное представление **User action analysis**, в котором выделяются разные типы пользователей, выполнившие анализируемые пользовательские действия. Список **Analyze by** в разделе **Multidimensional analysis** предустановлен на **Browsers**.
5. В списках фильтров вверху страницы выбрать нужные значения для фильтрации по **Action type**, **Performance metric** и **Contribution**.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/user-type-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-f2e40b76ae.png)

   Многомерный анализ
6. Выбрать длительность в выпадающем списке периода анализа.
7. Выбрать участок временной шкалы, чтобы задать период, который нужно проанализировать. Отсюда можно определить и проанализировать только те пользовательские действия, которые представляют наибольший интерес.

Сценарий 4: анализ по геолокации

В этом сценарии основное внимание уделяется поиску пользовательских действий из определённого географического региона. Допустим, для определённого региона была добавлена сеть доставки контента (Content Delivery Network, CDN), и нужно получить представление о том, насколько хорошо работает новая CDN.

Доступ к многомерному анализу по геолокации

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать.
3. В инфографике **Performance analysis** выбрать плитку **View geolocation breakdown** в нижнем левом углу, чтобы отобразить раздел **Geolocation breakdown**.
4. Выбрать **Analyze performance** внизу раздела.

   ![Multi-dimensional analysis](https://dt-cdn.net/images/2-application-overview-with-geo-location-break-down-1600-945b822f7e.png)

   Многомерный анализ

   Это открывает многомерное представление **User action analysis**, в котором теперь отображаются основные геолокации, откуда происходят пользовательские действия.
5. В списках фильтров вверху страницы выбрать нужные значения для фильтрации по **Action type**, **User type**, **Performance metric** и **Contribution**.

![Multi-dimensional analysis](https://dt-cdn.net/images/geo-location-breakdown-entry-to-multi-dimensional-user-analytics-screen-1599-7d2031e084.png)

Многомерный анализ

6. Выбрать длительность в выпадающем списке периода анализа.
7. Выбрать участок временной шкалы, чтобы задать период, который нужно проанализировать. Отсюда можно определить и проанализировать только те пользовательские действия, которые относятся к анализу.

Сценарий 5: анализ по типу ошибки

![Multidimensional analysis](https://dt-cdn.net/images/multidimensional-analysis-5007-e664cf92d9.png)

Многомерный анализ

Для веб-приложений Dynatrace классифицирует [ошибки](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") как ошибки **Request**, **Custom** и **JavaScript**, что позволяет применять фильтры и анализировать их по категориям. Таким образом можно проводить сфокусированный и контекстный анализ каждого типа ошибок, обнаруженных в выбранном периоде

Доступ к многомерному анализу по ошибкам

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать.
3. В инфографике **Performance analysis** выбрать плитку **Errors by type** в нижнем левом углу, чтобы просмотреть основные ошибки **Request**, **Custom** и **JavaScript**.
4. Выбрать **Analyze errors**, чтобы перейти на страницу **Multidimensional analysis: Errors**.
5. Применить фильтры, чтобы просмотреть конкретные ошибки в выбранном периоде, выбрав их из следующих списков:

* **Тип ошибки**: `Request`, `Custom` и `JavaScript`
   * **Context**: `Errors during user actions` и `Errors between user actions`
   * **Origin**: `1st party errors`, `3rd party errors` и `CDN errors`
6. Выбрать **Show your errors** по `Type`, `Context` или `Origin`.
7. Выбрать длительность периода из списка диапазонов анализа.
8. Выбрать диаграмму временной шкалы, чтобы задать нужный временной интервал, и сдвигать выделение по шкале, чтобы выбрать диапазон для анализа. Так можно сузить и анализировать только те ошибки, которые относятся к текущему анализу.
9. Необязательно Выбрать соответствующий тип ошибки в легенде, чтобы скрыть или показать этот тип ошибки на диаграмме.

![Error analysis](https://dt-cdn.net/images/error-analysis-2757-13832acb4e.png)

Error analysis

После того как с помощью **Overview** найдено скопление ошибок, для выбранного периода можно дополнительно проанализировать ошибки с помощью карточки **Detail analysis**.

1. Выбрать одно из следующих измерений, по которому нужно проанализировать период:

   * **Performance over time**
   * **Distribution**
   * **Browsers**
   * **Geolocation**
   * **Errors**
2. Выбрать опцию группировки ошибок по `Type`, `Context` или `Origin`.
3. Необязательно Применить фильтр, выбрав поле ввода и указав нужный фильтр. Использовать **Enter** и указать соответствующее значение фильтра.

![Analysis by error type](https://dt-cdn.net/images/error-analysis-1873-78a0287859.png)

Analysis by error type

В этом примере обнаружена ошибка `HTTP 500` в booking API, которую теперь нужно изучить подробнее. При выборе этой ошибки на странице деталей ошибки отображается основная информация о ней, например:

* Как часто возникала ошибка
* Количество сессий и пользователей, затронутых ошибкой
* Элементы, такие как пользовательские действия, ОС, типы браузеров и локации, связанные с ошибкой

В карточке деталей ошибки можно найти дополнительную информацию об ошибке, например была ли ошибка обнаружена с помощью RUM JavaScript или OneAgent. При выборе **Edit detection rules for this error pattern** происходит переход на страницу, где можно отредактировать шаблон ошибки веб-запроса, обнаруживший ошибку. Также можно выбрать **Create detection rule based on this error pattern**, чтобы создать явное правило ошибки веб-запроса для обнаруженной ошибки запроса.

![Error details](https://dt-cdn.net/images/error-details-5093-27df9761b5.png)

Error details

Чтобы изучить ошибку подробнее, можно провести углублённый анализ сессии по одной из затронутых сессий из списка **User sessions affected by the error** и выяснить, где и как именно возникла ошибка. Такие функции, как [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers."), позволяют легко находить ошибки этих пользователей и делиться информацией о них внутри организации.

![User details page](https://dt-cdn.net/images/user-sessions-to-user-details-page-1637-f01f4b8bf0.png)

User details page

![Session replay](https://dt-cdn.net/images/session-replay-1917-70e8439a06.png)

Session replay

Ещё один способ изучить ошибку подробнее, это посмотреть на неё с точки зрения пользовательского действия. Использовать фильтр по определённой ошибке, найденной в карточке **Detail analysis** для выбранного периода, чтобы сузить круг интересующих ошибок, а затем прокрутить вниз до **Key user actions** или **Top 100 user actions**, чтобы найти связанные пользовательские действия. Выбрать интересующее пользовательское действие и открыть его для анализа отдельных пользовательских действий.

![Analyze errors by user action](https://dt-cdn.net/images/analyze-errors-by-user-action-2880-b1252314fe.png)

Analyze errors by user action

Например, на следующей странице показано, что ошибки можно включить в waterfall-анализ в виде столбца или маркера в момент возникновения ошибки.

![Waterfall analysis](https://dt-cdn.net/images/waterfall-1863-b48855309b.png)

Waterfall analysis