---
title: Использование свойств пользовательских действий и сессий в веб-приложениях
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties
scraped: 2026-05-12T11:34:37.087353
---

# Использование свойств пользовательских действий и сессий в веб-приложениях

# Использование свойств пользовательских действий и сессий в веб-приложениях

* How-to guide
* 3-min read
* Published Jan 27, 2022

Свойства пользовательских действий и сессий предоставляют мощный и гибкий механизм добавления информации к каждому пользовательскому действию и сессии. Их можно использовать для более детального анализа взаимодействия пользователей с приложением.

Свойства действий и сессий — это пары «ключ–значение» в виде метаданных, получаемых из захваченных данных. Эти метаданные «продвигаются» из атрибутов запросов, атрибутов CSS-селекторов, мета-тегов и других источников. Свойства действий и сессий полезны при создании сложных запросов, сегментаций или агрегаций по захваченным метаданным. Их можно использовать для создания вычисляемых метрик приложения. Также эти свойства можно просматривать на странице многомерного анализа, странице **User sessions** и странице **User sessions query**.

Ниже описано, где можно найти значения, захватываемые как пользовательские свойства действий и сессий, и как полностью использовать эти свойства.

Перед использованием свойств пользовательских действий и сессий необходимо определить их в настройках приложения. Подробнее см. в разделе [Определение свойств пользовательских действий и сессий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

## Анализ пользовательских сессий

На странице **[User sessions](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")** доступна возможность фильтровать пользовательские сессии по свойствам действий и сессий. Например, при запуске программы лояльности можно добавить свойство `loyalty_status`, чтобы узнать, является ли пользователь в отслеживаемой сессии участником уровня `Silver`, `Gold` или `Platinum`. Затем на странице **User sessions** можно фильтровать клиентов уровня `Platinum` или `Gold`.

1. Перейдите в **Session Segmentation**.
2. В поле **Filter by** выберите один из типов свойств, например **Session date properties** или **User action string properties**, и выберите нужное свойство.
3. Выберите одно или несколько значений свойства.
4. Выберите сессию для просмотра деталей и доступных свойств сессии.
5. На странице сведений о пользовательской сессии можно детализировать пользовательские действия. Разверните пользовательское действие и выберите **Perform waterfall analysis**. На этой странице можно проверить доступные свойства действия и все зафиксированные значения.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)

   User action analysis
6. В правом верхнем углу выберите **Analyze user action** для более детального анализа. В разделе **User action properties** выберите свойство действия для дальнейшего анализа.

## Дополнительная аналитика с USQL

Свойства пользовательских действий и сессий значительно расширяют аналитические возможности при использовании [Dynatrace User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") для анализа, требующего расширенной фильтрации. Кроме того, для отслеживания денежных значений и целей конверсии, ключевых для бизнеса, можно создавать запросы на основе уникальных значений отдельных свойств действий или сессий.

Чтобы использовать свойства действий и сессий в USQL:

1. Перейдите в **Query User Sessions**.
2. Введите нужный запрос. Доступны следующие пользовательские свойства:

   | Пользовательское свойство | Таблица | Свойство действия | Свойство сессии |
   | --- | --- | --- | --- |
   | `<dataType>Properties.<propertyKey>` | `useraction` | Применимо |  |
   | `<dataType>Properties.<propertyKey>` | `usersession` |  | Применимо |
   | `useraction.<dataType>Properties.<propertyKey>` | `useraction` | Применимо |  |
   | `useraction.<dataType>Properties.<propertyKey>` | `usersession` | Применимо |  |
   | `usersession.<dataType>Properties.<propertyKey>` | `useraction` |  | Применимо |
   | `usersession.<dataType>Properties.<propertyKey>)` | `usersession` |  | Применимо |

   Часть `<dataType>` может принимать следующие значения:

   * `string`
   * `long`
   * `double`
   * `date`
3. Выберите **Run query**.

В приведённом ниже примере показано, сколько ошибок запросов встретили клиенты уровней Silver, Gold и Platinum.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Gain additional insights with USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

Gain additional insights with USQL

## Интеграция через User session API

[User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.") в сочетании с [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") позволяет получать доступ ко всем данным пользовательских действий и сессий, включая свойства и значения.

Продолжая пример с программой лояльности, можно использовать информацию о проблемах и статусе лояльности через User session API, запрашивая пользовательские сессии, затронутые проблемой после её закрытия. Это позволяет, например, настроить персонализированные маркетинговые кампании.

Примеры полезных запросов:

* Сессии пользователей уровня Gold для приложения в определённом временном диапазоне — полезно для проблем, затрагивающих всё приложение.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum, посещающие конкретную страницу приложения в определённом временном диапазоне — полезно для проблем, затрагивающих конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и пользовательских приложений можно [создавать запросы](#usql) со свойствами действий и сессий, а затем закреплять полученные графики на дашбордах.

Для веб-приложений дополнительно доступно создание вычисляемых метрик на основе пользовательских свойств, использование этих метрик для построения графиков и их закрепление на дашбордах. Всё это можно сделать в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

В следующем примере пакет **Web property pack** используется для отслеживания маркетинговых кампаний и просмотра следующих данных:

* Общий трафик по континентам
* Топ-кампании по континентам
* Самый медленный опыт целевой страницы по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

Web property pack

## Экспорт свойств сессий

Захваченные свойства пользовательских сессий можно экспортировать вместе со всеми остальными данными пользовательских сессий в потоках экспорта.

Подробнее см. в разделе [Экспорт пользовательских сессий](/managed/observe/digital-experience/session-segmentation/export-session-data "Set up Dynatrace to export user session data to a provided webhook endpoint.").

## Многомерный анализ

Пользовательские свойства также можно использовать в [многомерном анализе](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."). Например, можно анализировать пользовательские действия на основе пользовательских свойств или фильтровать данные по значениям свойств.

Чтобы использовать пользовательские свойства на странице **Multidimensional analysis**:

1. Перейдите в **Web** и выберите приложение.
2. В разделе **Impact of user actions on performance** выберите **Analyze performance**.
3. Прокрутите страницу вниз до раздела **Detail analysis for selected timeframe** и выберите нужное пользовательское свойство в поле **Analyze by**.

   ![Using custom properties on the Multidimensional analysis page](https://dt-cdn.net/images/use-properties-mda-2-2134-eb53554356.png)

   Using custom properties on the Multidimensional analysis page
4. Необязательно: в поле **Filter by** задайте нужные фильтры. Например, можно фильтровать по свойствам пользовательских действий.

   ![Filtering by property on the Multidimensional analysis page](https://dt-cdn.net/images/mda-filter-by-properties-2132-bc8eab93c3.png)

   Filtering by property on the Multidimensional analysis page
5. Прокрутите страницу вниз для просмотра дополнительных деталей. Дополнительные значения свойств позволяют получить дополнительные сведения о производительности и состоянии приложения.

## Вычисляемые метрики, графики и оповещения

Для расширения возможностей создайте [вычисляемую метрику](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") на основе свойств пользовательских действий. Метрику можно создать со [страницы **Multidimensional analysis**](#mda) или из настроек приложения. После добавления метрики её можно использовать для создания пользовательских графиков и оповещений.

Чтобы создать метрику со страницы **Multidimensional analysis**:

1. На странице **Multidimensional analysis** прокрутите страницу вниз до раздела **Detail analysis for selected timeframe** и задайте нужные параметры в полях **Analyze by** и, при необходимости, **Filter by**.
2. Выберите **Create metric**.
3. Необязательно: измените имя и ключ метрики.

   ![Creating a calculated metric with data filtered by action property](https://dt-cdn.net/images/creating-calculated-metric-with-data-filtered-by-action-property-2134-e9027de910.png)

   Creating a calculated metric with data filtered by action property
4. Выберите **Create metric** для сохранения метрики.
5. Необязательно: выберите **Create a chart** или **Create alert**. Подробнее см. в разделах [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

Чтобы создать метрику из настроек веб-приложения:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Metrics**, а затем **Add metric**.
5. Выберите нужную метрику и укажите **Metric name** и **Metric key for API usage**.
6. Необязательно: в поле **Filter by** задайте нужные фильтры. Например, можно фильтровать по свойствам пользовательских действий.
7. Выберите **Create metric**.
8. Необязательно: в списке метрик разверните созданную метрику и выберите **Create a chart** или **Create alert**. Подробнее см. в разделах [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Связанные темы

* [Определение свойств пользовательских действий и сессий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)