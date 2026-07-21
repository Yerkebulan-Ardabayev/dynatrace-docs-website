---
title: Использование свойств пользовательских действий и сессий для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/action-and-session-properties
---

# Использование свойств пользовательских действий и сессий для веб-приложений в RUM Classic

# Использование свойств пользовательских действий и сессий для веб-приложений в RUM Classic

* Практическое руководство
* 3 мин на чтение
* Опубликовано 27 янв. 2022 г.

Свойства пользовательских действий и свойства пользовательских сессий, это мощное и гибкое средство добавления информации к каждому пользовательскому действию и пользовательской сессии. Эти свойства можно использовать для более глубокой видимости всех деталей взаимодействия пользователей с приложением.

Свойства действий и сессий, это пары ключ-значение метаданных, полученные из захваченных данных. Эти метаданные "продвигаются" из атрибутов запроса, атрибутов CSS-селекторов, мета-тегов и других источников. Свойства действий и сессий пригодятся, когда нужно создавать мощные запросы, сегментации или агрегации по захваченным метаданным. С помощью свойств действий и сессий можно создавать вычисляемые метрики приложения. Также эти свойства можно просматривать на странице многомерного анализа, странице **User sessions** и странице **User sessions query**.

В разделах ниже описано, где найти значения, захваченные как пользовательские свойства действий и сессий, и как полностью использовать возможности этих свойств.

Перед тем как использовать свойства пользовательских действий и сессий, нужно определить эти свойства в настройках приложения. Подробнее см. [Определение свойств пользовательских действий и сессий для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

## Анализ пользовательских сессий

Страница **[User sessions](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.")** предлагает возможность фильтровать пользовательские сессии по свойствам действий и сессий. Например, при работе программы лояльности можно добавить свойство `loyalty_status`, чтобы узнать, является ли пользователь в отслеживаемой пользовательской сессии участником уровня `Silver`, `Gold` или `Platinum`. После этого можно отфильтровать клиентов уровня `Platinum` или `Gold` на странице **User sessions**.

1. Перейти в **Session Segmentation**.
2. В **Filter by** выбрать один из типов свойств, например, **Session date properties** или **User action string properties**, и затем выбрать нужное свойство.
3. Выбрать значение или значения свойства в соответствии со своими потребностями.
4. Выбрать сессию для просмотра её деталей и доступных свойств сессии.
5. На странице деталей пользовательской сессии можно углубиться в пользовательские действия. Развернуть пользовательское действие и выбрать **Perform waterfall analysis**. На этой странице можно проверить доступные свойства действия, а также все сообщённые значения.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)

   User action analysis
6. В верхнем правом углу выбрать **Analyze user action** для ещё более глубокого анализа. В разделе **User action properties** выбрать свойство действия для дальнейшего анализа.

## Дополнительные сведения с помощью USQL

Свойства пользовательских действий и сессий могут значительно расширить возможности аналитики при использовании [Dynatrace User Sessions Query Language (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") для аналитики, которая требует расширенной фильтрации или постоянной фильтрации между разными представлениями анализа. Кроме того, если нужно отслеживать денежные значения и цели конверсии, ключевые для успеха бизнеса, можно строить запросы на основе уникальных значений отдельных свойств пользовательских действий или сессий, определённых для среды.

Использование свойств действий и сессий в USQL

1. Перейти в **Query User Sessions**.
2. Ввести нужный запрос. Доступны следующие пользовательские свойства:

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
3. Выбрать **Run query**.

В примере ниже показано, сколько ошибок запросов возникло у клиентов уровня Silver, Gold и Platinum.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Gain additional insights with USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

Gain additional insights with USQL

## Интеграция через User session API

[User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers."), в сочетании с [User Sessions Query Language (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), даёт доступ ко всем данным пользовательских действий и сессий, включая свойства и значения.

Расширяя приведённый выше пример программы лояльности, можно использовать сведения о проблеме и информацию о статусе лояльности через User session API, запрашивая пользовательские сессии, которые были затронуты проблемой, после её закрытия. Это позволяет использовать эту информацию, например, для настройки персонализированных маркетинговых кампаний.

Вот несколько примеров запросов, которые могут пригодиться:

* Пользовательские сессии участников уровня Gold в приложении за определённый период времени, это можно использовать для проблем, затрагивающих всё приложение.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum в конкретном приложении, перешедшие на конкретную страницу за определённый период времени, это можно использовать для проблем, затрагивающих конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и пользовательских приложений можно [создать запрос](#usql) со свойствами действий и сессий, а затем закрепить полученную диаграмму на одном из дашбордов.

Для веб-приложений дополнительно можно создавать вычисляемые метрики на основе пользовательских свойств, использовать эти метрики для создания диаграммы, а затем закрепить эту диаграмму на дашбордах. Это делается в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

В следующем примере обычный **Web property pack** используется для отслеживания маркетинговых кампаний на [Dynatrace.com﻿](https://www.dynatrace.com/), чтобы просмотреть следующее:

* Общий трафик по континентам
* Топ кампаний по континентам
* Самый медленный опыт посадочной страницы по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

Web property pack

## Экспорт свойств сессии

Захваченные свойства пользовательских сессий можно экспортировать вместе со всеми остальными данными пользовательских сессий в потоках экспорта пользовательских сессий.

Подробнее см. [Экспорт пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/export-session-data "Set up Dynatrace to export user session data to a provided webhook endpoint.").

## Многомерный анализ

Также можно использовать пользовательские свойства на странице [Многомерный анализ](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions."). Например, можно анализировать действия пользователей на основе пользовательских свойств или фильтровать данные по значениям свойств.

Использование пользовательских свойств на странице **Multidimensional analysis**

1. Перейти в **Web** и выбрать приложение.
2. В разделе **Impact of user actions on performance** выбрать **Analyze performance**.
3. Прокрутить вниз до **Detail analysis for selected timeframe** и выбрать нужное пользовательское свойство в **Analyze by**.

   ![Using custom properties on the Multidimensional analysis page](https://dt-cdn.net/images/use-properties-mda-2-2134-eb53554356.png)

   Использование пользовательских свойств на странице Multidimensional analysis
4. Необязательно В **Filter by** задать нужные фильтры. Например, можно фильтровать по свойствам действий пользователя.

   ![Filtering by property on the Multidimensional analysis page](https://dt-cdn.net/images/mda-filter-by-properties-2132-bc8eab93c3.png)

   Фильтрация по свойству на странице Multidimensional analysis
5. Прокрутить вниз, чтобы увидеть больше деталей. Дополнительные значения свойств можно использовать для более глубокого анализа производительности и успешности приложения.

## Вычисляемые метрики, графики и оповещения

Чтобы расширить полезность, нужно создать [вычисляемую метрику](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") на основе свойств действий пользователя. Создать метрику можно либо со [страницы **Multidimensional analysis**](#mda), либо из настроек приложения. После добавления метрики её можно использовать для создания пользовательских графиков и оповещений.

Создание метрики со страницы **Multidimensional analysis**

1. На странице **Multidimensional analysis** прокрутить вниз до **Detail analysis for selected timeframe** и задать нужные параметры в **Analyze by** и, при необходимости, в **Filter by**.
2. Выбрать **Create metric**.
3. Необязательно Изменить имя метрики и ключ метрики.

   ![Creating a calculated metric with data filtered by action property](https://dt-cdn.net/images/creating-calculated-metric-with-data-filtered-by-action-property-2134-e9027de910.png)

   Создание вычисляемой метрики с данными, отфильтрованными по свойству действия
4. Выбрать **Create metric**, чтобы сохранить метрику.
5. Необязательно Выбрать **Create a chart** или **Create alert**. Подробнее см. [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

Создание метрики из настроек веб-приложения

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Metrics**, затем **Add metric**.
5. Выбрать нужную метрику и указать **Metric name** и **Metric key for API usage**.
6. Необязательно В **Filter by** задать нужные фильтры. Например, можно фильтровать по свойствам действий пользователя.
7. Выбрать **Create metric**.
8. Необязательно В списке метрик развернуть созданную метрику и выбрать **Create a chart** или **Create alert**. Подробнее см. [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Похожие темы

* [Define user action and user session properties for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.")
* [Mastering session and user action properties for enhanced analytics﻿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)