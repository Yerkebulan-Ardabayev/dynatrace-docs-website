---
title: Использование свойств действий и сессий пользователей в пользовательских приложениях
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/analyze-and-use/action-and-session-properties-custom
scraped: 2026-05-12T11:27:59.520880
---

# Использование свойств действий и сессий пользователей в пользовательских приложениях

# Использование свойств действий и сессий пользователей в пользовательских приложениях

* How-to guide
* 1-min read
* Published Jan 30, 2023

Свойства действий и сессий пользователей — мощный и гибкий инструмент добавления информации к каждому действию и сессии. Вы можете использовать эти свойства для более глубокой видимости всех деталей взаимодействия пользователей с вашим приложением.

Свойства действий и сессий — это метаданные в формате «ключ-значение», извлечённые из захваченных данных. Эти метаданные «повышаются» из значений, переданных через SDK, или атрибутов запросов. Свойства действий и сессий удобны для создания сложных запросов, сегментаций или агрегаций на основе захваченных метаданных. Их также можно использовать на страницах **User sessions** и **User sessions query**.

В разделах ниже описано, где найти значения, захваченные в качестве свойств действий и сессий, и как максимально эффективно использовать эти свойства.

Перед использованием свойств действий и сессий необходимо определить их в настройках вашего приложения. Подробнее см. [Определение свойств действий и сессий пользователей в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/define-custom-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для ваших пользовательских приложений.").

## Анализ сессий пользователей

Страница **[User sessions](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте о сегментации и атрибутах фильтрации сессий пользователей.")** предоставляет возможность фильтрации сессий по свойствам действий и сессий. Например, если вы ведёте программу лояльности, добавьте свойство `loyalty_status`, чтобы определить, является ли пользователь в мониторируемой сессии участником уровня `Silver`, `Gold` или `Platinum`. Затем вы сможете фильтровать `Platinum` или `Gold` клиентов на странице **User sessions**.

1. Перейдите в **Session Segmentation**.
2. В поле **Filter by** выберите один из типов свойств, например **Session date properties** или **User action string properties**, и выберите нужное свойство.
3. Выберите одно или несколько значений свойства.
4. Выберите сессию для просмотра её деталей и доступных свойств.
5. На странице деталей сессии вы можете перейти к пользовательским действиям. Разверните пользовательское действие и нажмите **Perform waterfall analysis**. На этой странице доступны свойства действий и все переданные значения.

   ![Анализ пользовательского действия](https://dt-cdn.net/images/user-action-analysis-1639-89f7ffac81.png)

   Анализ пользовательского действия
6. В правом верхнем углу нажмите **Analyze user action** для более детального анализа. В разделе **User action properties** выберите свойство действия для дальнейшего анализа.

## Дополнительные аналитические возможности с USQL

Свойства действий и сессий значительно расширяют аналитические возможности при использовании [User Sessions Query Language (USQL) Dynatrace](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным сессий и выполнять запросы.") для анализа, требующего расширенной или постоянной фильтрации в нескольких аналитических представлениях. Кроме того, для отслеживания денежных значений и целей конверсии, критически важных для вашего бизнеса, можно строить запросы на основе уникальных значений отдельных свойств действий или сессий, определённых для вашей среды.

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
3. Нажмите **Run query**.

В примере ниже показано, сколько ошибок запросов встретили клиенты уровней Silver, Gold и Platinum.

```
SELECT stringProperties.loyalty_status AS "Loyalty status", COUNT(useraction.requestErrorCount) AS "HTTP error count" FROM usersession WHERE stringProperties.loyalty_status IS NOT NULL GROUP BY stringProperties.loyalty_status
```

![Дополнительные аналитические возможности с USQL](https://dt-cdn.net/images/use-properties-usql-1642-60372d3301.png)

Дополнительные аналитические возможности с USQL

## Интеграция через User session API

[User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает API Dynatrace User Sessions Query Language.") в сочетании с [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ к данным сессий и выполнять запросы.") обеспечивает доступ ко всем данным действий и сессий пользователей, включая свойства и значения.

Расширяя пример с программой лояльности, вы можете использовать информацию о проблемах и статусе лояльности через User session API, запрашивая сессии, затронутые проблемой после её закрытия. Это позволяет, например, настраивать персонализированные маркетинговые кампании.

Примеры запросов:

* Сессии Gold-участников в приложении за определённый период (подходит для проблем, затрагивающих всё приложение):

  ```
  SELECT userId, stringProperties.loyalty_status FROM usersession WHERE stringProperties.loyalty_status = "Gold" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287
  ```
* Platinum-участники в конкретном приложении, посещавшие определённую страницу за указанный период (подходит для проблем, затрагивающих конкретную страницу):

  ```
  SELECT userId, stringProperties.loyalty_status, useraction.targetUrl FROM usersession WHERE stringProperties.loyalty_status = "Platinum" AND userType = "REAL_USER" AND useraction.application = "easyTravel" AND startTime > 1531741985241 AND endTime < 1531932305287 AND useraction.targetUrl = "https://easytravel.perform-2018.dynalabs.io/special-offers.jsp"
  ```

## Дашборды

Для веб-, мобильных и пользовательских приложений вы можете [создать запрос](#usql) с использованием свойств действий и сессий, а затем закрепить полученную диаграмму на одном из дашбордов.

Для веб-приложений дополнительно доступно создание вычисляемых метрик на основе пользовательских свойств, построение диаграмм и их закрепление на дашбордах через [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.").

В качестве общего примера используется **Web property pack** для отслеживания маркетинговых кампаний на [Dynatrace.com](https://www.dynatrace.com/):

* Общий трафик по континентам
* Топ-кампании по континентам
* Самый медленный опыт посадочной страницы по маркетинговой кампании

![Web property pack](https://dt-cdn.net/images/dynatrace-com-marketing-campaigns-anonym-1600x951-1600-59971b5148.png)

Web property pack

## Экспорт свойств сессий

Захваченные свойства сессий пользователей можно экспортировать вместе со всеми другими данными сессий в рамках потоков экспорта сессий.

Подробнее см. [Экспорт данных сессий пользователей](/managed/observe/digital-experience/session-segmentation/export-session-data "Настройте Dynatrace для экспорта данных сессий пользователей на указанный webhook-эндпоинт.").

## Связанные темы

* [Определение свойств действий и сессий пользователей в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/define-custom-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для ваших пользовательских приложений.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)