---
title: Leverage user action and user session properties for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties
scraped: 2026-03-06T21:28:12.602325
---

# Использование свойств действий пользователя и сеансов для веб-приложений

# Использование свойств действий пользователя и сеансов для веб-приложений

* Classic
* How-to guide
* 3-min read
* Published Jan 27, 2022

Свойства действий пользователя и свойства сеансов пользователя предоставляют мощный и гибкий способ добавления информации к каждому действию и сеансу пользователя. Вы можете использовать эти свойства для более глубокого понимания всех деталей взаимодействия пользователей с вашим приложением.

Свойства действий и сеансов представляют собой метаданные в виде пар ключ-значение, которые извлекаются из захваченных данных. Эти метаданные «продвигаются» из атрибутов запросов, атрибутов CSS-селекторов, мета-тегов и других источников. Свойства действий и сеансов полезны, когда вам нужно создавать мощные запросы, сегментации или агрегации на основе захваченных метаданных. Вы можете использовать свойства действий и сеансов для создания вычисляемых метрик приложения. Эти свойства также доступны на странице многомерного анализа, странице **User sessions** и странице **User sessions query**.

Ознакомьтесь с разделами ниже, чтобы узнать, где можно найти значения, захваченные как пользовательские свойства действий и сеансов, и как можно максимально эффективно использовать эти свойства.

Прежде чем использовать свойства действий и сеансов пользователя, необходимо определить эти свойства в настройках приложения. Подробнее см. [Define user action and user session properties for web applications](../additional-configuration/define-user-action-and-session-properties.md "Define custom string, numeric, and date properties for your monitored web applications.").

## Анализ сеансов пользователей

Страница **[User sessions](../../session-segmentation/new-user-sessions.md "Learn about user session segmentation and filtering attributes.")** позволяет фильтровать сеансы пользователей по свойствам действий и сеансов. Например, если вы проводите программу лояльности, вы можете добавить свойство `loyalty_status`, чтобы узнать, является ли пользователь в отслеживаемом сеансе участником уровня `Silver`, `Gold` или `Platinum`. Затем вы можете отфильтровать клиентов `Platinum` или `Gold` на странице **User sessions**.

1. Перейдите в ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. В разделе **Filter by** выберите один из типов свойств, например **Session date properties** или **User action string properties**, а затем выберите нужное свойство.
3. Выберите значение или значения свойства в соответствии с вашими потребностями.
4. Выберите сеанс, чтобы просмотреть его детали и доступные свойства сеанса.
5. Со страницы деталей сеанса пользователя вы можете углубиться в действия пользователя. Разверните действие пользователя, а затем выберите **Perform waterfall analysis**. На этой странице вы можете проверить доступные свойства действий, а также все зафиксированные значения.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)
6. В правом верхнем углу выберите **Analyze user action** для ещё более глубокого анализа. В разделе **User action properties** выберите свойство действия для дальнейшего анализа.

## Дополнительные аналитические возможности с USQL

Свойства действий и сеансов пользователя могут значительно расширить ваши аналитические возможности при использовании [Dynatrace User Sessions Query Language (USQL)](../../session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data.md "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") для аналитики, требующей расширенной фильтрации или постоянной фильтрации в различных представлениях анализа. Кроме того, если вы хотите отслеживать денежные значения и цели конверсии, ключевые для успеха вашего бизнеса, вы можете создавать запросы на основе уникальных значений отдельных свойств действий пользователя или сеансов, определённых для вашей среды.

Чтобы использовать свойства действий и сеансов в USQL

1. Перейдите в ![Query user sessions](https://dt-cdn.net/images/query-user-sessions-512-77c5a8da9f.png "Query user sessions") **Query User Sessions**.
2. Введите необходимый запрос. Доступны следующие пользовательские свойства:

   | Пользовательское свойство | Таблица | Свойство действия | Свойство сеанса |
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

В приведённом ниже примере вы можете увидеть, сколько ошибок запросов возникло у клиентов уровней Silver, Gold и Platinum.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Gain additional insights with USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

## Интеграция через User session API

[User sessions API](../../../../dynatrace-api/environment-api/rum/user-sessions.md "Learn what the Dynatrace User Sessions Query language API offers.") в сочетании с [User Sessions Query Language (USQL)](../../session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data.md "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") позволяет получить доступ ко всем данным действий и сеансов пользователя, включая свойства и значения.

Расширяя приведённый выше пример с программой лояльности, вы можете использовать информацию о проблемах и статусе лояльности через User session API, запрашивая сеансы пользователей, на которые повлияла проблема после её закрытия. Это позволяет использовать полученную информацию, например, для настройки персонализированных маркетинговых кампаний.

Вот несколько примеров запросов, которые вы можете использовать:

* Сеансы пользователей уровня Gold в приложении за определённый период времени — это можно использовать для проблем, влияющих на всё приложение.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum в определённом приложении, посещающие конкретную страницу в заданном временном диапазоне — это можно использовать для проблем, влияющих на конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и пользовательских приложений вы можете [создать запрос](#usql) со свойствами действий и сеансов, а затем закрепить полученную диаграмму на одном из ваших дашбордов.

Для веб-приложений вы можете дополнительно создать вычисляемые метрики на основе пользовательских свойств, использовать эти метрики для создания диаграммы, а затем закрепить её на дашборде. Это можно сделать в [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.").

В следующем примере используется универсальный **Web property pack** для отслеживания маркетинговых кампаний на [Dynatrace.com](https://www.dynatrace.com/) и просмотра следующей информации:

* Общий трафик по континентам
* Лучшие кампании по континентам
* Самый медленный опыт загрузки по маркетинговым кампаниям

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

## Экспорт свойств сеансов

Вы можете экспортировать захваченные свойства сеансов пользователя вместе со всеми остальными данными сеансов в потоках экспорта сеансов пользователя.

Подробнее см. [Export user sessions](../../session-segmentation/export-session-data.md "Set up Dynatrace to export user session data to a provided webhook endpoint.").

## Многомерный анализ

Вы также можете использовать пользовательские свойства в [Multidimensional analysis](multi-dimensional-analysis.md "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."). Например, вы можете анализировать действия пользователей на основе ваших пользовательских свойств или фильтровать данные по значениям свойств.

Чтобы использовать пользовательские свойства на странице **Multidimensional analysis**

1. Перейдите в **Web** и выберите ваше приложение.
2. В разделе **Impact of user actions on performance** выберите **Analyze performance**.
3. Прокрутите вниз до **Detail analysis for selected timeframe** и выберите нужное пользовательское свойство в **Analyze by**.

   ![Using custom properties on the Multidimensional analysis page](https://dt-cdn.net/images/use-properties-mda-2-2134-eb53554356.png)
4. Необязательно: в **Filter by** установите необходимые фильтры. Например, можно фильтровать по свойствам действий пользователя.

   ![Filtering by property on the Multidimensional analysis page](https://dt-cdn.net/images/mda-filter-by-properties-2132-bc8eab93c3.png)
5. Прокрутите вниз, чтобы увидеть больше деталей. Вы можете использовать дополнительные значения свойств для дальнейшего анализа производительности и успешности вашего приложения.

## Вычисляемые метрики, диаграммы и оповещения

Для расширения возможностей создайте [вычисляемую метрику](../additional-configuration/rum-calculated-metrics-web.md "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") с вашими свойствами действий пользователя. Вы можете создать метрику либо со страницы [**Multidimensional analysis**](#mda), либо из настроек приложения. После добавления метрики вы можете использовать её для создания пользовательских диаграмм и оповещений.

Чтобы создать метрику со страницы **Multidimensional analysis**

1. На странице **Multidimensional analysis** прокрутите вниз до **Detail analysis for selected timeframe** и настройте необходимые параметры в **Analyze by** и, при необходимости, в **Filter by**.
2. Выберите **Create metric**.
3. Необязательно: измените имя метрики и ключ метрики.

   ![Creating a calculated metric with data filtered by action property](https://dt-cdn.net/images/creating-calculated-metric-with-data-filtered-by-action-property-2134-e9027de910.png)
4. Выберите **Create metric** для сохранения метрики.
5. Необязательно: выберите **Create a chart** или **Create alert**. Подробнее см. [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и [Metric events](../../../../dynatrace-intelligence/anomaly-detection/metric-events.md "Learn about metric events in Dynatrace").

Чтобы создать метрику из настроек веб-приложения

1. Перейдите в **Web**.
2. Выберите приложение, которое хотите настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**...**) > **Edit**.
4. В настройках приложения выберите **Metrics**, затем выберите **Add metric**.
5. Выберите нужную метрику и укажите **Metric name** и **Metric key for API usage**.
6. Необязательно: в **Filter by** установите необходимые фильтры. Например, можно фильтровать по свойствам действий пользователя.
7. Выберите **Create metric**.
8. Необязательно: из списка метрик разверните созданную метрику и выберите **Create a chart** или **Create alert**. Подробнее см. [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и [Metric events](../../../../dynatrace-intelligence/anomaly-detection/metric-events.md "Learn about metric events in Dynatrace").

## Связанные темы

* [Define user action and user session properties for web applications](../additional-configuration/define-user-action-and-session-properties.md "Define custom string, numeric, and date properties for your monitored web applications.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)
