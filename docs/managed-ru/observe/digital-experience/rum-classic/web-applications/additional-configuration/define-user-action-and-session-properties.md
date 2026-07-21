---
title: Определение свойств пользовательских действий и сессий для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties
---

# Определение свойств пользовательских действий и сессий для веб-приложений в RUM Classic

# Определение свойств пользовательских действий и сессий для веб-приложений в RUM Classic

* Практическое руководство
* 8 минут чтения
* Обновлено 05 марта 2026 г.

Dynatrace собирает много информации о производительности вашего веб-приложения. Эту информацию можно обогатить ценными метаданными и превратить эти метаданные в свойства пользовательских действий и сессий.

Свойства действий и сессий представляют собой пары "ключ-значение", которые можно фильтровать в нескольких представлениях анализа Dynatrace. Эти свойства пригодятся при создании мощных запросов, сегментаций и агрегаций по собранным метаданным. Свойства действий и сессий можно использовать для создания вычисляемых метрик приложения. Их также можно увидеть в многомерном представлении анализа, на странице **User sessions** и странице **User sessions query**. Чтобы глубже разобраться в использовании этих свойств, посетите раздел [Использование свойств пользовательских действий и сессий для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/action-and-session-properties "Свойства пользовательских действий и сессий, представляющие собой пары ключ-значение метаданных, обеспечивают дополнительную видимость и более глубокий анализ опыта ваших конечных пользователей. Используя эти свойства для веб-приложений, можно фильтровать пользовательские сессии, добавлять вычисляемые метрики, создавать диаграммы и многое другое.").

Ниже приведена информация о том, как настроить такие свойства, а также соответствующие примеры конфигурации. Чтобы использовать свойства действий и сессий, сначала нужно [добавить свойства в веб-интерфейсе Dynatrace](#add-properties), а затем начать передачу нужных метаданных в Dynatrace.

## Добавление пользовательского свойства

Используйте свойства с пользовательским определением для настройки строковых, числовых свойств и свойств даты для отслеживаемых [пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в вашем приложении.") и [пользовательских сессий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её длительность, и многое другое."). Затем Dynatrace собирает значения свойств как часть пути каждого пользователя. Значения свойств можно использовать для непревзойдённой видимости всех деталей взаимодействия пользователей с приложением. Можно определить пользовательские свойства действий и сессий, специфичные для каждого приложения.

### Типы выражений

Dynatrace может собирать метаданные из следующих источников (**типы выражений**):

* CSS-селектор
* Переменная JavaScript
* JavaScript API
* Функция JavaScript
* Метатег
* Значение cookie

  Требования для значения cookie

  Если вы хотите использовать `Cookie value` в качестве источника данных, убедитесь, что у cookie нет атрибута `HttpOnly`. В противном случае RUM JavaScript не сможет прочитать значения cookie, поскольку cookie с атрибутом `HttpOnly` недоступны для JavaScript.
* Строка запроса
* Атрибут запроса на стороне сервера
* Заголовок ответа XHR/fetch (доступно начиная с версии RUM JavaScript 1.253 для XHR/fetch и начиная с версии RUM JavaScript 1.257 для Angular)

  Требования для заголовка ответа XHR/fetch

  Если вы хотите использовать `XHR/fetch response header` в качестве источника данных, убедитесь в следующем:

  + В настройках приложения включите параметры **Capture fetch() requests**, **Capture XmlHttpRequest (XHR)** или **Angular**. Подробные инструкции см. в разделах [Активация поддержки универсальных JavaScript-фреймворков](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-generic-js-frameworks "Узнайте, зачем нужно активировать конкретные JavaScript-фреймворки для поддержки XHR-действий, и как настроить Real User Monitoring Classic для XHR-действий.") или [Активация поддержки Angular](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-specific-js-frameworks "Узнайте, зачем нужно активировать конкретные JavaScript-фреймворки для поддержки XHR-действий, и как настроить Real User Monitoring Classic для XHR-действий.").

    Сбор метаданных из заголовков ответа XHR/fetch не поддерживается для AngularJS.
  + Для CORS и XHR запросов Dynatrace может собирать метаданные только из [заголовков ответа, разрешённых CORS﻿](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_response_header). Если нужно извлекать данные из других заголовков, используйте заголовок [`Access-Control-Expose-Headers`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers).

    - `Access-Control-Expose-Headers: Content-Encoding, Destination, Basket-value` для раскрытия указанных заголовков
    - `Access-Control-Expose-Headers: *` для раскрытия всех заголовков, кроме заголовка `Authorization`, для запросов без учётных данных
    - `Access-Control-Expose-Headers: *, Authorization` для раскрытия всех заголовков для запросов без учётных данных

### Типы данных

Dynatrace может сохранять собранные метаданные в одном из следующих типов данных:

| Тип данных | Примечание |
| --- | --- |
| `String` | Свойства действий и сессий типа данных `String` ограничены 1000 символами до применения правила очистки. |
| Число | `Double` или `Long` |
| `Date` | Доступно только для [типа выражения](#expression-types) `JavaScript API`, метаданные должны собираться через [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Узнайте, как настроить Real User Monitoring Classic с помощью JavaScript API."). |

### Типы хранения

Метаданные можно сохранять на разных "уровнях хранения".

* **User action property**: данные сохраняются в определённом свойстве на уровне пользовательского действия для каждого действия, для которого RUM JavaScript может получить метаданные.
* **User session property**: последнее собранное значение сохраняется в определённом свойстве на уровне сессии.
* **Both options**: данные сохраняются в определённом свойстве как на уровне пользовательского действия, так и на уровне сессии.

### Определение пользовательского свойства

Чтобы определить пользовательское свойство

1. Перейдите в раздел **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Session and action properties**.
5. Выберите **Add property** > **Custom-defined property**.
6. Настройте свойство:

   * Выберите [**Expression type**](#expression-types). Если применимо, также выберите [**Data type**](#data-types) и **String length**.
   * Введите обозначение типа выражения, который нужно использовать, например, атрибут CSS-селектора или имя метатега. Для типа **Server-side request attribute** выберите [имя атрибута запроса](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и как использовать их на всех уровнях всех представлений анализа сервисов.").
   * Необязательно Определите **Display name**, то есть имя свойства, которое используется в веб-интерфейсе Dynatrace, например, на странице сведений о сессии или странице сведений о пользовательском действии.
   * Укажите **Key**, то есть имя свойства, которое используется для идентификации и последующего поиска свойства в [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ и выполнять запросы к данным пользовательских сессий на основе ключевых слов, синтаксиса, функций и многого другого.") и на странице **User sessions**.

     **Key**, который уже использовался ранее, нельзя использовать повторно, [пока данные сохраняются](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Ознакомьтесь со стандартными и настраиваемыми периодами хранения данных сервисов, RUM Classic, синтетических тестов, Log Monitoring, метрик, диагностики и данных безопасности в Dynatrace Managed.") в вашей среде. Это связано с тем, что собранные данные всё ещё ссылаются на старую конфигурацию свойства.
   * Необязательно Отключите **Comply with "Do Not Track" browser settings** только в том случае, если свойство не содержит персональных данных.

     Этот параметр доступен только для определённых типов выражений и если в разделе конфиденциальности данных настроек приложения включён параметр **[Comply with "Do Not Track" browser settings](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Узнайте о настройках конфиденциальности, которые предоставляет Dynatrace для обеспечения соответствия ваших веб-приложений нормам конфиденциальности данных вашего региона.")**.
   * Выберите хотя бы один [тип хранения](#storage-levels): свойство действия, свойство сессии или оба. Для типа хранения свойства сессии выберите один из типов агрегации.
   * Необязательно Чтобы ограничить собираемые значения, включите **Apply cleanup rule** и укажите [регулярное выражение](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Узнайте, как использовать регулярные выражения в контексте Dynatrace.").

     Регулярное выражение применяется к собранному значению: если попытаться собрать строку длиной, например, 1000 символов, будут собраны только первые 100 символов, и регулярное выражение будет применено именно к этим 100 символам.

## Добавление пакета свойств

Используй наборы свойств (property packs), чтобы связать данные аналитики с показателями производительности. Для этого можно интегрировать инструменты, такие как веб-аналитика и мониторинг производительности, в Dynatrace. Доступно множество наборов свойств, например Adobe, Google, Intercom и Tealeaf.

Чтобы добавить свойство из набора свойств

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Capturing** > **Session and action properties**.
5. Выбрать **Add property** > **Property packs**, а затем выбрать нужный набор свойств из выпадающего списка.
6. В столбце **Configure properties** выбрать **Add** для свойств, которые нужно добавить, а затем выбрать **Next**.
7. Выбрать минимум один [тип хранения](#storage-levels): user action property, session property или оба, для каждого из добавленных свойств.
8. Выбрать **Create property**.

## Примеры свойств действий и сессий

Ниже приведены примеры определений, которые работают для тестового приложения easyTravel.

* В этом примере свойство `member_status` фиксирует статус членства в программе лояльности.

  ![User action and session properties - CSS selector example 1](https://dt-cdn.net/images/example1-2220-a488e55380.png)

  User action and session properties - CSS selector example 1
* `averagepersonprice` фиксирует среднюю цену на человека за поездку, забронированную через портал easyTravel.

  ![User action and session properties - CSS selector example 1](https://dt-cdn.net/images/example2-2195-bfc15d8a6d.png)

  User action and session properties - CSS selector example 1
* Свойство `author` фиксирует имя разработчика приложения easyTravel из тега метаданных.

  ![User action and session properties - meta tag example](https://dt-cdn.net/images/example3-2246-bef8792b1a.png)

  User action and session properties - meta tag example
* В следующем примере строковая переменная JavaScript фиксирует `appversion` пользователя во время сессии.

  ![User action and session properties - JavaScript variable example](https://dt-cdn.net/images/javascript-variable-1488-c376427e90.png)

  User action and session properties - JavaScript variable example
* Начиная с версии RUM JavaScript 1.295 стало возможным извлекать данные из JSON.
  В следующем примере строковая переменная JavaScript фиксирует свойство `userid` JSON, хранящегося в виде строки в `sessionStorage`.

  ![Developer Tools](https://dt-cdn.net/images/userid-devtools-2544-09723cd81f.png)

  Developer Tools

  Чтобы указать, что строку нужно разобрать как JSON, нужно использовать символ `$` перед именем свойства (даже если имя свойства начинается с `$`, добавить перед ним ещё один `$`).
  В этом примере будет получена строка, хранящаяся в `sessionStorage.user`, а символ `$` указывает, что строку нужно разобрать как JSON, после чего будет зафиксировано `userid`.

  ![Userid property](https://dt-cdn.net/images/userid-1732-1c6b552622.png)

  Userid property

## Сценарий использования

Можно интегрировать Adobe Analytics с Dynatrace, чтобы упростить взаимодействие между разными командами в бизнесе. Подробнее о том, как это сделать, можно узнать здесь: [Tightening the communication within BizDevOps with Adobe Analytics & Dynatrace﻿](https://www.dynatrace.com/news/blog/tightening-the-communication-within-bizdevops-with-adobe-analytics-dynatrace/) и [Actionable insights with our Adobe Analytics integration and new web properties﻿](https://www.dynatrace.com/news/blog/actionable-insights-with-our-adobe-analytics-integration-and-new-web-properties/).

## Ограничения

* Можно определить максимум 200 свойств на приложение.
* Можно определить максимум 20 свойств действий на приложение.
* Свойства действий и сессий типа данных `String` ограничены 1000 символами до применения правила очистки.
* Можно использовать до 20 свойств на приложение бесплатно. Дополнительные свойства расходуют DEM units.
  Подробнее см. [DEM units](/managed/license/classic-licensing/digital-experience-monitoring-units#dem-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") (обратить внимание на строки **Session property** и **Action property** в таблице) и [Free tier of action and session properties](/managed/license/classic-licensing/digital-experience-monitoring-units#free-action-and-session-properties "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").

## Примечания

* Dynatrace начинает фиксировать свойства действий и сессий только после того, как эти свойства [определены в настройках приложения](#add-properties).
* Свойства сессии недоступны для текущих активных сессий. Свойства становятся доступны только после завершения сессии.
* Метаданные фиксируются в конце пользовательского действия.  
  Если нужно зафиксировать метаданные в начале пользовательского действия, нужно выбрать **JavaScript API** в качестве [типа выражения](#expression-types) при [добавлении пользовательского свойства](#add-properties), а затем использовать [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring Classic using the JavaScript API.") для передачи нужных значений, а именно методы [addActionProperties﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#addactionproperties) и [sendSessionProperties﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#sendsessionproperties).
* Можно проверить, сколько свойств уже используется и сколько ещё можно добавить.

  1. Перейти в **Web**.
  2. Выбрать приложение, которое нужно настроить.
  3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
  4. В настройках приложения выбрать **Capturing** > **Session and action properties**.
  5. Прокрутить вниз до **Property usage quotas**.

## Связанные темы

* [Leverage user action and user session properties for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Mastering session and user action properties for enhanced analytics﻿](https://www.youtube.com/watch?v=b8Vj0EoaDeM)