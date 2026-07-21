---
title: Использование свойств пользовательских действий и пользовательских сессий для настраиваемых приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/action-and-session-properties-custom
---

# Использование свойств пользовательских действий и пользовательских сессий для настраиваемых приложений в RUM Classic

# Использование свойств пользовательских действий и пользовательских сессий для настраиваемых приложений в RUM Classic

* Практическое руководство
* Чтение 1 минута
* Опубликовано 30 января 2023 г.

Свойства пользовательских действий и свойства пользовательских сессий предоставляют мощный и гибкий способ добавления информации к каждому пользовательскому действию и пользовательской сессии. Их можно использовать для более глубокой видимости всех деталей взаимодействия пользователей с приложением.

Свойства действий и сессий, это пары "ключ-значение" метаданных, полученных из захваченных данных. Эти метаданные "продвигаются" из значений, переданных через SDK, или из атрибутов запросов. Свойства действий и сессий пригодятся, когда нужно строить мощные запросы, сегментации или агрегации по захваченным метаданным. Эти свойства также можно использовать на страницах **User sessions** и **User sessions query**.

В разделах ниже описано, где найти значения, захватываемые как свойства пользовательских действий и сессий, и как использовать эти свойства по максимуму.

Прежде чем использовать свойства пользовательских действий и сессий, нужно определить эти свойства в настройках приложения. Подробнее см. [Определение свойств пользовательских действий и пользовательских сессий для настраиваемых приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.").

## Анализ пользовательских сессий

Страница **[User sessions](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.")** предлагает возможность фильтровать пользовательские сессии по свойствам действий и сессий. Например, при работе программы лояльности можно добавить свойство `loyalty_status`, чтобы узнать, является ли пользователь в отслеживаемой пользовательской сессии участником уровня `Silver`, `Gold` или `Platinum`. Затем на странице **User sessions** можно отфильтровать клиентов уровня `Platinum` или `Gold`.

1. Перейти в **Session Segmentation**.
2. В поле **Filter by** выбрать один из типов свойств, например **Session date properties** или **User action string properties**, а затем выбрать нужное свойство.
3. Выбрать значение или значения свойства в соответствии с потребностями.
4. Выбрать сессию, чтобы просмотреть её детали и доступные свойства сессии.
5. На странице деталей пользовательской сессии можно углубиться в пользовательские действия. Развернуть пользовательское действие, а затем выбрать **Perform waterfall analysis**. На этой странице можно проверить доступные свойства действия, а также все переданные значения.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)

   User action analysis
6. В правом верхнем углу выбрать **Analyze user action**, чтобы копнуть ещё глубже. В разделе **User action properties** выбрать свойство действия для дальнейшего анализа.

## Дополнительные данные с помощью USQL

Свойства пользовательских действий и сессий могут значительно расширить возможности аналитики при использовании [Dynatrace User Sessions Query Language (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") для аналитики, требующей расширенной фильтрации или постоянной фильтрации между разными представлениями анализа. Кроме того, когда нужно отслеживать денежные значения и цели конверсии, ключевые для успеха бизнеса, можно строить запросы на основе уникальных значений отдельных свойств пользовательских действий или сессий, определённых для среды.

Использование свойств действий и сессий в USQL

1. Перейти в **Query User Sessions**.
2. Ввести нужный запрос. Доступны следующие настраиваемые свойства:

   | Настраиваемое свойство | Таблица | Свойство действия | Свойство сессии |
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

[User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers."), в сочетании с [User Sessions Query Language (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."), позволяет получить доступ ко всем данным пользовательских действий и сессий, включая свойства и значения.

Расширяя приведённый выше пример с программой лояльности, можно использовать информацию о проблеме и информацию о статусе лояльности через User session API, запрашивая пользовательские сессии, затронутые проблемой, после её закрытия. Это позволяет использовать эту информацию, например, для настройки персонализированных маркетинговых кампаний.

Вот несколько примеров запросов, которые могут пригодиться:

* Пользовательские сессии участников уровня Gold в приложении за определённый период времени, это можно использовать для проблем, затрагивающих всё приложение целиком.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum в конкретном приложении, посетившие определённую страницу за определённый период времени, это можно использовать для проблем, затрагивающих конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и настраиваемых приложений можно [создать запрос](#usql) со свойствами действий и сессий, а затем закрепить полученную диаграмму на одном из дашбордов.

Для веб-приложений дополнительно можно создавать вычисляемые метрики на основе настраиваемых свойств, использовать эти метрики для построения диаграммы, а затем закрепить эту диаграмму на дашбордах. Это можно сделать в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

В следующем примере общий **Web property pack** используется для отслеживания маркетинговых кампаний на [Dynatrace.com﻿](https://www.dynatrace.com/), чтобы просмотреть следующее:

* Общий трафик по континентам
* Топ кампаний по континентам
* Самый медленный опыт посадочной страницы по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

Web property pack

## Экспорт свойств сессии

Захваченные свойства пользовательских сессий можно экспортировать вместе со всеми остальными данными пользовательских сессий в потоках экспорта пользовательских сессий.

Подробнее см. [Экспорт пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/export-session-data "Set up Dynatrace to export user session data to a provided webhook endpoint.").

## Связанные темы

* [Определение свойств пользовательских действий и пользовательских сессий для настраиваемых приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.")
* [Mastering session and user action properties for enhanced analytics﻿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)