---
title: Использование свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile
---

# Использование свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic

# Использование свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 27 января 2022 г.

Свойства пользовательского действия и свойства пользовательской сессии дают мощный и гибкий способ добавления информации к каждому пользовательскому действию и пользовательской сессии. Эти свойства можно использовать для более глубокой видимости всех деталей взаимодействия пользователей с приложением.

Свойства действия и сессии, это пары "ключ, значение" с метаданными, полученными из захваченных данных. Эти метаданные "продвигаются" из значений, отправленных SDK, или атрибутов запроса. Свойства действия и сессии пригодятся, когда нужно создавать мощные запросы, сегментации или агрегации по захваченным метаданным. Эти свойства также можно использовать на страницах **User sessions** и **User sessions query**.

Разделы ниже помогут узнать, где найти значения, захваченные как свойства пользовательского действия и сессии, и как полностью использовать эти свойства.

Перед тем как использовать свойства пользовательского действия и сессии, их нужно определить в настройках приложения. Подробности см. в разделе [Определение свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправка метаданных в Dynatrace и определение свойств действия и сессии для отслеживаемых мобильных приложений.").

## Анализ пользовательской сессии

Страница **[User sessions](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Информация о сегментации пользовательских сессий и атрибутах фильтрации.")** предлагает возможность фильтровать пользовательские сессии по свойствам действия и сессии. Например, если ведётся программа лояльности, можно добавить свойство `loyalty_status`, чтобы узнать, является ли пользователь в отслеживаемой пользовательской сессии участником уровня `Silver`, `Gold` или `Platinum`. Затем на странице **User sessions** можно отфильтровать клиентов `Platinum` или `Gold`.

1. Перейти в **Session Segmentation**.
2. В **Filter by** выбрать один из типов свойств, например, **Session date properties** или **User action string properties**, а затем выбрать нужное свойство.
3. Выбрать значение или значения свойства согласно потребностям.
4. Выбрать сессию, чтобы просмотреть её детали и доступные свойства сессии.
5. Со страницы деталей пользовательской сессии можно углубиться в пользовательские действия. Развернуть пользовательское действие и выбрать **Perform waterfall analysis**. На этой странице можно проверить доступные свойства действия, а также все отправленные значения.

   ![Анализ пользовательского действия](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)

   Анализ пользовательского действия
6. В правом верхнем углу выбрать **Analyze user action**, чтобы углубиться ещё сильнее. В разделе **User action properties** выбрать свойство действия для дальнейшего анализа.

## Дополнительные данные с помощью USQL

Свойства пользовательского действия и сессии могут значительно расширить возможности аналитики при использовании [Dynatrace User Sessions Query Language (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Информация о доступе к данным пользовательских сессий и их запросах по ключевым словам, синтаксису, функциям и не только.") для аналитики, требующей расширенной фильтрации или постоянной фильтрации между представлениями анализа. Кроме того, когда нужно отслеживать денежные значения и цели конверсии, ключевые для успеха бизнеса, можно строить запросы на основе уникальных значений отдельных свойств пользовательского действия или сессии, определённых для окружения.

Чтобы использовать свойства действия и сессии в USQL

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

В примере ниже показано, сколько ошибок запросов встретили клиенты уровней Silver, Gold и Platinum.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Получение дополнительных данных с помощью USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

Получение дополнительных данных с помощью USQL

## Интеграция через User session API

[User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Информация о том, что предлагает Dynatrace User Sessions Query language API.") в сочетании с [User Sessions Query Language (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Информация о доступе к данным пользовательских сессий и их запросах по ключевым словам, синтаксису, функциям и не только.") позволяет получить доступ ко всем данным пользовательских действий и сессий, включая свойства и значения.

Продолжая пример с программой лояльности выше, можно использовать информацию о проблеме и информацию о статусе лояльности через User session API, запросив пользовательские сессии, затронутые проблемой, после её закрытия. Это позволяет использовать данную информацию, например, для настройки персонализированных маркетинговых кампаний.

Вот несколько примеров запросов, которые могут пригодиться:

* Пользовательские сессии участников уровня Gold в приложении за определённый промежуток времени, это можно использовать для проблем, затрагивающих всё приложение.

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Пользователи уровня Platinum в конкретном приложении, посетившие определённую страницу за определённый промежуток времени, это можно использовать для проблем, затрагивающих конкретную страницу.

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и пользовательских приложений можно [создать запрос](#usql) со свойствами действия и сессии, а затем закрепить полученный график на одном из дашбордов.

Для веб-приложений дополнительно можно создавать вычисляемые метрики на основе пользовательских свойств, использовать эти метрики для создания графика, а затем закреплять этот график на дашбордах. Это можно сделать в [Data Explorer](/managed/analyze-explore-automate/explorer "Запросы метрик и преобразование результатов для получения нужных данных.").

Общий **Web property pack** используется в следующем примере для отслеживания маркетинговых кампаний на [Dynatrace.com​](https://www.dynatrace.com/), чтобы просмотреть следующее:

* Общий трафик по континентам
* Топ кампаний по континентам
* Самый медленный опыт загрузки посадочной страницы по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

Web property pack

## Экспорт свойств сессии

Захваченные свойства пользовательской сессии можно экспортировать вместе со всеми остальными данными пользовательской сессии в потоках экспорта пользовательских сессий.

Подробнее см. в разделе [Экспорт пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/export-session-data "Настройка Dynatrace для экспорта данных пользовательских сессий на указанную конечную точку webhook.").

## Похожие темы

* [Определение свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправка метаданных в Dynatrace и определение свойств действия и сессии для отслеживаемых мобильных приложений.")
* [Mastering session and user action properties for enhanced analytics​](https://www.youtube.com/watch?v=b8Vj0EoaDeM)