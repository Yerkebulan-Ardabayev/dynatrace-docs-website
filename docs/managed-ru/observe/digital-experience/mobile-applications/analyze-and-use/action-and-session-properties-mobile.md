---
title: Использование свойств пользовательских действий и сессий для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile
scraped: 2026-05-12T11:27:58.023840
---

# Использование свойств пользовательских действий и сессий для мобильных приложений

# Использование свойств пользовательских действий и сессий для мобильных приложений

* How-to guide
* 1-min read
* Published Jan 27, 2022

Свойства пользовательских действий и сессий предоставляют мощный и гибкий способ добавления информации к каждому пользовательскому действию и сессии. Вы можете использовать эти свойства для более глубокого анализа деталей взаимодействия пользователей с вашим приложением.

Свойства действий и сессий — это пары ключ-значение метаданных, извлекаемые из захваченных данных. Эти метаданные «продвигаются» из значений, переданных через SDK, или атрибутов запросов. Свойства действий и сессий удобны, когда требуется создавать мощные запросы, сегментации или агрегации захваченных метаданных. Эти свойства также можно использовать на страницах **User sessions** и **User sessions query**.

Ознакомьтесь с разделами ниже, чтобы узнать, где можно найти значения, захваченные как свойства пользовательских действий и сессий, и как максимально использовать эти свойства.

Прежде чем использовать свойства пользовательских действий и сессий, необходимо определить их в настройках приложения. Подробнее см. в разделе [Определение свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для отслеживаемых мобильных приложений.").

## Анализ пользовательских сессий

Страница **[User sessions](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.")** предлагает возможность фильтрации пользовательских сессий по свойствам действий и сессий. Например, если вы запускаете программу лояльности, вы можете добавить свойство `loyalty_status`, чтобы узнать, является ли пользователь в отслеживаемой сессии участником уровня `Silver`, `Gold` или `Platinum`. Затем вы можете фильтровать клиентов уровня `Platinum` или `Gold` на странице **User sessions**.

1. Перейдите в **Session Segmentation**.
2. В **Filter by** выберите один из типов свойств, например **Session date properties** или **User action string properties**, а затем выберите нужное свойство.
3. Выберите одно или несколько значений свойства в соответствии с вашими потребностями.
4. Выберите сессию для просмотра её деталей и доступных свойств.
5. Со страницы сведений о пользовательской сессии вы можете перейти к пользовательским действиям. Разверните пользовательское действие и нажмите **Perform waterfall analysis**. На этой странице вы можете проверить доступные свойства действия и все переданные значения.

   ![User action analysis](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)

   User action analysis
6. В правом верхнем углу нажмите **Analyze user action** для более глубокого анализа. В разделе **User action properties** выберите свойство действия для дальнейшего анализа.

## Дополнительные аналитические возможности с USQL

Свойства пользовательских действий и сессий значительно расширяют аналитические возможности при использовании [Dynatrace User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их.") для аналитики с расширенной фильтрацией. Когда вам нужно отслеживать денежные значения и целевые показатели конверсии, важные для успеха бизнеса, вы можете строить запросы на основе уникальных значений отдельных свойств действий или сессий, определённых для вашего окружения.

Чтобы использовать свойства действий и сессий в USQL:

1. Перейдите в **Query User Sessions**.
2. Введите необходимый запрос. Доступны следующие пользовательские свойства:

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
3. Нажмите **Run query**.

В приведённом ниже примере показано, сколько ошибок запросов столкнулись клиенты Silver, Gold и Platinum.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Gain additional insights with USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

Gain additional insights with USQL

## Интеграция через User session API

[User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает API User Sessions Query Language Dynatrace.") в сочетании с [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным пользовательских сессий и запрашивать их.") позволяет вам получать доступ ко всем данным пользовательских действий и сессий, включая свойства и значения.

Продолжая пример с программой лояльности, вы можете использовать информацию о проблемах и статусе лояльности через User session API, запрашивая пользовательские сессии, затронутые проблемой после её закрытия. Это позволяет использовать информацию, например, для настройки персонализированных маркетинговых кампаний.

Вот несколько примеров запросов, которые могут быть полезны:

* Пользовательские сессии участников Gold в приложении за определённый временной диапазон — используйте для проблем, затрагивающих всё приложение.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum в конкретном приложении, переходившие на определённую страницу за определённый период — используйте для проблем, затрагивающих конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Панели мониторинга

Для веб-, мобильных и пользовательских приложений вы можете [создать запрос](#usql) со свойствами действий и сессий, а затем закрепить результирующий график на одной из ваших панелей мониторинга.

Для веб-приложений вы также можете создавать вычисленные метрики на основе пользовательских свойств, использовать их для создания графиков и закреплять эти графики на панелях мониторинга через [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.").

В следующем примере используется общий **Web property pack** для отслеживания маркетинговых кампаний на [Dynatrace.com](https://www.dynatrace.com/) с отображением следующей информации:

* Общий трафик по континентам
* Ведущие кампании по континентам
* Наиболее медленный посадочный опыт по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

Web property pack

## Экспорт свойств сессий

Вы можете экспортировать захваченные свойства пользовательских сессий вместе со всеми другими данными в потоках экспорта пользовательских сессий.

Подробнее см. в разделе [Экспорт пользовательских сессий](/managed/observe/digital-experience/session-segmentation/export-session-data "Настройте Dynatrace для экспорта данных пользовательских сессий на указанный webhook-эндпоинт.").

## Связанные темы

* [Определение свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для отслеживаемых мобильных приложений.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)