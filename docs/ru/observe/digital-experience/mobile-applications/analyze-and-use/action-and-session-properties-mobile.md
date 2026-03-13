---
title: Leverage user action and user session properties for mobile applications
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile
scraped: 2026-03-06T21:25:38.421195
---

# Использование свойств действий пользователя и сеансов пользователя для мобильных приложений

# Использование свойств действий пользователя и сеансов пользователя для мобильных приложений

* Classic
* How-to guide
* 1-min read
* Published Jan 27, 2022

Свойства действий пользователя и свойства сеансов пользователя предоставляют мощное и гибкое средство добавления информации к каждому действию и сеансу пользователя. Вы можете использовать эти свойства для более глубокого понимания всех деталей взаимодействия пользователей с вашим приложением.

Свойства действий и сеансов представляют собой пары метаданных "ключ-значение", которые формируются на основе захваченных данных. Эти метаданные "продвигаются" из значений, переданных через SDK, или из атрибутов запросов. Свойства действий и сеансов удобны, когда вам нужно создавать мощные запросы, сегментации или агрегации на основе захваченных метаданных. Вы также можете использовать эти свойства на страницах **User sessions** и **User sessions query**.

Ознакомьтесь с разделами ниже, чтобы узнать, где можно найти значения, захваченные в качестве свойств действий пользователя и сеансов, и как полностью использовать эти свойства.

Прежде чем использовать свойства действий и сеансов пользователя, необходимо определить эти свойства в настройках вашего приложения. Подробнее см. [Define user action and user session properties for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

## Анализ сеансов пользователей

Страница **[User sessions](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")** предоставляет возможность фильтрации сеансов пользователей по свойствам действий и сеансов. Например, если вы используете программу лояльности, вы можете добавить свойство `loyalty_status`, чтобы определить, является ли пользователь в отслеживаемом сеансе участником уровня `Silver`, `Gold` или `Platinum`. Затем вы можете фильтровать клиентов уровня `Platinum` или `Gold` на странице **User sessions**.

1. Перейдите в ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. В поле **Filter by** выберите один из типов свойств, например **Session date properties** или **User action string properties**, а затем выберите нужное свойство.
3. Выберите значение или значения свойства в соответствии с вашими потребностями.
4. Выберите сеанс, чтобы просмотреть его детали и доступные свойства сеанса.
5. Со страницы деталей сеанса пользователя вы можете углубиться в действия пользователя. Разверните действие пользователя и выберите **Perform waterfall analysis**. На этой странице вы можете проверить доступные свойства действий, а также все переданные значения.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)
6. В правом верхнем углу выберите **Analyze user action**, чтобы углубиться ещё дальше. В разделе **User action properties** выберите свойство действия для дальнейшего анализа.

## Дополнительные возможности с USQL

Свойства действий и сеансов пользователя могут значительно улучшить ваши аналитические возможности при использовании [Dynatrace User Sessions Query Language (USQL)](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") для аналитики, требующей расширенной фильтрации или постоянной фильтрации между представлениями анализа. Кроме того, когда вам нужно отслеживать денежные показатели и цели конверсии, ключевые для успеха вашего бизнеса, вы можете строить запросы на основе уникальных значений индивидуальных свойств действий или сеансов пользователя, определённых для вашей среды.

Использование свойств действий и сеансов в USQL

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

[User sessions API](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.") в сочетании с [User Sessions Query Language (USQL)](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") позволяет получить доступ ко всем данным действий и сеансов пользователя, включая свойства и значения.

Расширяя приведённый выше пример программы лояльности, вы можете использовать информацию о проблемах и статусе лояльности через User session API, запрашивая сеансы пользователей, затронутые проблемой, после её закрытия. Это позволяет использовать полученную информацию, например, для настройки персонализированных маркетинговых кампаний.

Вот несколько примеров запросов, которые могут быть полезны:

* Сеансы пользователей уровня Gold в приложении за определённый период времени — это можно использовать для проблем, затрагивающих всё приложение.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum в конкретном приложении, посещающие определённую страницу в заданный период времени — это можно использовать для проблем, затрагивающих конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и пользовательских приложений вы можете [создать запрос](#usql) со свойствами действий и сеансов, а затем закрепить полученный график на одном из ваших дашбордов.

Для веб-приложений вы можете дополнительно создавать вычисляемые метрики на основе пользовательских свойств, использовать эти метрики для построения графиков и закреплять графики на дашбордах. Это можно сделать в [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

В следующем примере используется универсальный **Web property pack** для отслеживания маркетинговых кампаний на [Dynatrace.com](https://www.dynatrace.com/) и отображения следующей информации:

* Общий трафик по континентам
* Топ кампаний по континентам
* Самый медленный опыт landing-страницы по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

## Экспорт свойств сеансов

Вы можете экспортировать захваченные свойства сеансов пользователя вместе со всеми другими данными сеанса в потоках экспорта сеансов пользователя.

Подробнее см. [Export user sessions](/docs/observe/digital-experience/session-segmentation/export-session-data "Set up Dynatrace to export user session data to a provided webhook endpoint.").

## Связанные темы

* [Define user action and user session properties for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)
