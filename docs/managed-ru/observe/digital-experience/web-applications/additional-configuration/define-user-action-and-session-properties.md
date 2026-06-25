---
title: Определение свойств пользовательских действий и сессий для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties
scraped: 2026-05-12T11:28:01.030159
---

# Определение свойств пользовательских действий и сессий для веб-приложений

# Определение свойств пользовательских действий и сессий для веб-приложений

* How-to guide
* 8-min read
* Updated on Mar 05, 2026

Dynatrace собирает обширную информацию о производительности веб-приложения. Эту информацию можно обогатить ценными метаданными и преобразовать их в свойства пользовательских действий и сессий.

Свойства действий и сессий представляют собой пары «ключ — значение», по которым можно фильтровать данные в нескольких аналитических представлениях Dynatrace. Эти свойства удобны для создания мощных запросов, сегментаций и агрегаций по зафиксированным метаданным. Свойства действий и сессий можно использовать для создания вычисляемых метрик приложений. Они также отображаются в представлении многомерного анализа, на странице **User sessions** и странице **User sessions query**. Для более глубокого понимания работы с этими свойствами посетите раздел [Использование свойств пользовательских действий и сессий для веб-приложений](/managed/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.").

Ниже приведена информация о настройке подобных свойств и соответствующие примеры конфигурации. Для работы со свойствами действий и сессий сначала необходимо [добавить свойства в веб-интерфейсе Dynatrace](#add-properties), а затем приступить к передаче необходимых метаданных в Dynatrace.

## Добавление пользовательского свойства

Используйте пользовательские свойства для настройки строковых, числовых и датовых свойств для отслеживаемых [пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") и [пользовательских сессий](/managed/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."). Dynatrace затем фиксирует значения свойств как часть пути каждого пользователя. Значения свойств позволяют получить несравнимую видимость всех деталей взаимодействия пользователей с приложением. Можно определять пользовательские свойства действий и сессий, специфичные для каждого приложения.

### Типы выражений

Dynatrace может фиксировать метаданные из следующих источников (**типов выражений**):

* CSS selector
* Переменная JavaScript
* JavaScript API
* Функция JavaScript
* Meta tag
* Значение cookie

  Требования к значению cookie

  Если в качестве источника данных нужно использовать `Cookie value`, убедитесь, что cookie не имеют атрибута `HttpOnly`. В противном случае RUM JavaScript не сможет читать значения cookie, поскольку cookie с атрибутом `HttpOnly` недоступны для JavaScript.
* Query string
* Атрибут запроса на стороне сервера
* Заголовок ответа XHR/fetch (доступен начиная с RUM JavaScript версии 1.253 для XHR/fetch и с версии 1.257 для Angular)

  Требования к заголовку ответа XHR/fetch

  Для использования `XHR/fetch response header` в качестве источника данных убедитесь в следующем:

  + В настройках приложения включите параметры **Capture fetch() requests**, **Capture XmlHttpRequest (XHR)** или **Angular**. Подробные инструкции см. в разделах [Активация поддержки общих JavaScript-фреймворков](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-generic-js-frameworks "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.") и [Активация поддержки Angular](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-specific-js-frameworks "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

    Захват метаданных из заголовков ответов XHR/fetch не поддерживается для AngularJS.
  + Для CORS и XHR-запросов Dynatrace может захватывать метаданные только из [безопасных для CORS заголовков ответов](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_response_header). Для извлечения данных из других заголовков используйте заголовок [`Access-Control-Expose-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers).

    - `Access-Control-Expose-Headers: Content-Encoding, Destination, Basket-value` — открыть доступ к указанным заголовкам
    - `Access-Control-Expose-Headers: *` — открыть доступ ко всем заголовкам, кроме `Authorization`, для запросов без учётных данных
    - `Access-Control-Expose-Headers: *, Authorization` — открыть доступ ко всем заголовкам для запросов без учётных данных

### Типы данных

Dynatrace может сохранять захваченные метаданные в одном из следующих типов данных:

| Тип данных | Примечание |
| --- | --- |
| `String` | Свойства действий и сессий типа `String` ограничены 1000 символами до применения правила очистки. |
| Number | `Double` или `Long` |
| `Date` | Доступен только для [типа выражения](#expression-types) `JavaScript API` — метаданные должны захватываться через [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API."). |

### Типы хранения

Метаданные можно сохранять на разных «уровнях хранения».

* **User action property**: данные хранятся в заданном свойстве на уровне пользовательского действия для каждого действия, из которого RUM JavaScript может извлечь метаданные.
* **User session property**: самое последнее захваченное значение хранится в заданном свойстве на уровне сессии.
* **Оба варианта**: данные хранятся в заданном свойстве как на уровне пользовательского действия, так и на уровне сессии.

### Определение пользовательского свойства

Чтобы определить пользовательское свойство:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Session and action properties**.
5. Выберите **Add property** > **Custom-defined property**.
6. Настройте свойство:

   * Выберите [**Expression type**](#expression-types). При необходимости также укажите [**Data type**](#data-types) и **String length**.
   * Введите обозначение выбранного типа выражения, например атрибут CSS-селектора или имя мета-тега. Для типа **Server-side request attribute** выберите [имя атрибута запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").
   * Необязательно: задайте **Display name** — имя свойства, используемое в веб-интерфейсе Dynatrace, например на странице сведений о сессии или пользовательском действии.
   * Укажите **Key** — имя свойства, используемое для его идентификации и поиска в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") и на странице **User sessions**.

     Ранее использованный **Key** нельзя повторно использовать [до тех пор, пока данные хранятся](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") в среде. Это связано с тем, что захваченные данные по-прежнему ссылаются на старую конфигурацию свойства.
   * Необязательно: отключите **Comply with "Do Not Track" browser settings** только если свойство не содержит персонально идентифицирующей информации.

     Этот параметр доступен только для определённых типов выражений и при условии, что в разделе конфиденциальности данных настроек приложения включён параметр **[Comply with "Do Not Track" browser settings](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")**.
   * Выберите хотя бы один [тип хранения](#storage-levels): свойство пользовательского действия, свойство сессии или оба. Для типа хранения свойства сессии выберите один из типов агрегации.
   * Необязательно: чтобы ограничить захватываемые значения, включите **Apply cleanup rule** и укажите [регулярное выражение](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

     Регулярное выражение применяется к захваченному значению: если захватываемая строка имеет, например, 1000 символов, захватываются только первые 100 символов, к которым и применяется regex.

## Добавление набора свойств

Используйте наборы свойств для связывания аналитических данных с информацией о производительности. Это можно реализовать, интегрировав в Dynatrace такие инструменты, как веб-аналитика и мониторинг производительности. Доступен широкий выбор наборов свойств, например Adobe, Google, Intercom и Tealeaf.

Чтобы добавить свойство из набора:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Session and action properties**.
5. Выберите **Add property** > **Property packs**, затем в раскрывающемся списке выберите нужный набор свойств.
6. В столбце **Configure properties** выберите **Add** для нужных свойств и нажмите **Next**.
7. Для каждого добавленного свойства выберите хотя бы один [тип хранения](#storage-levels): свойство пользовательского действия, свойство сессии или оба.
8. Выберите **Create property**.

## Примеры свойств действий и сессий

Ниже приведены примеры определений, работающих для тестового приложения easyTravel.

* В данном примере свойство `member_status` фиксирует статус членства в программе лояльности.

  ![Свойства пользовательских действий и сессий — пример CSS-селектора 1](https://dt-cdn.net/images/example1-2220-a488e55380.png)

  Свойства пользовательских действий и сессий — пример CSS-селектора 1
* `averagepersonprice` фиксирует среднюю стоимость путешествия на одного человека, забронированного через портал easyTravel.

  ![Свойства пользовательских действий и сессий — пример CSS-селектора 1](https://dt-cdn.net/images/example2-2195-bfc15d8a6d.png)

  Свойства пользовательских действий и сессий — пример CSS-селектора 1
* Свойство `author` фиксирует имя разработчика приложения easyTravel из мета-тега.

  ![Свойства пользовательских действий и сессий — пример мета-тега](https://dt-cdn.net/images/example3-2246-bef8792b1a.png)

  Свойства пользовательских действий и сессий — пример мета-тега
* В следующем примере строковая переменная JavaScript фиксирует `appversion` пользователя в течение сессии.

  ![Свойства пользовательских действий и сессий — пример переменной JavaScript](https://dt-cdn.net/images/javascript-variable-1488-c376427e90.png)

  Свойства пользовательских действий и сессий — пример переменной JavaScript
* Начиная с RUM JavaScript версии 1.295 возможно извлечение данных из JSON.
  В следующем примере строковая переменная JavaScript фиксирует свойство `userid` объекта JSON, хранящегося в виде строки в `sessionStorage`.

  ![Developer Tools](https://dt-cdn.net/images/userid-devtools-2544-09723cd81f.png)

  Developer Tools

  Для указания того, что строка должна быть разобрана как JSON, используйте символ `$` перед именем свойства (если имя свойства начинается с `$`, добавьте ещё один `$` в начало).
  В данном примере строка, хранящаяся в `sessionStorage.user`, будет извлечена, и символ `$` указывает на необходимость разбора строки как JSON, после чего будет захвачен `userid`.

  ![Свойство Userid](https://dt-cdn.net/images/userid-1732-1c6b552622.png)

  Свойство Userid

## Пример использования

Можно интегрировать Adobe Analytics с Dynatrace для улучшения взаимодействия между разными командами в вашем бизнесе. Подробнее см. [Tightening the communication within BizDevOps with Adobe Analytics & Dynatrace](https://www.dynatrace.com/news/blog/tightening-the-communication-within-bizdevops-with-adobe-analytics-dynatrace/) и [Actionable insights with our Adobe Analytics integration and new web properties](https://www.dynatrace.com/news/blog/actionable-insights-with-our-adobe-analytics-integration-and-new-web-properties/).

## Ограничения

* Максимальное количество свойств на приложение — 200.
* Максимальное количество свойств действий на приложение — 20.
* Свойства действий и сессий типа `String` ограничены 1000 символами до применения правила очистки.
* До 20 свойств на приложение предоставляются бесплатно. Дополнительные свойства потребляют DEM units.
  Подробнее см. разделы [DEM units](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#dem-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") (обратите внимание на записи **Session property** и **Action property** в таблице) и [Бесплатный уровень свойств действий и сессий](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#free-action-and-session-properties "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").

## Примечания

* Dynatrace начинает фиксировать свойства действий и сессий только после того, как они [определены в настройках приложения](#add-properties).
* Свойства сессий недоступны для активных сессий. Они становятся доступными только после завершения сессии.
* Метаданные фиксируются в конце пользовательского действия.
  Если необходимо захватывать метаданные в начале пользовательского действия, выберите **JavaScript API** в качестве [типа выражения](#expression-types) при [добавлении пользовательского свойства](#add-properties), а затем используйте [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") для передачи необходимых значений, а именно методы [addActionProperties](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#addactionproperties) и [sendSessionProperties](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#sendsessionproperties).
* Можно проверить, сколько свойств уже используется и сколько ещё можно добавить.

  1. Перейдите в **Web**.
  2. Выберите приложение, которое нужно настроить.
  3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
  4. В настройках приложения выберите **Capturing** > **Session and action properties**.
  5. Прокрутите страницу вниз до раздела **Property usage quotas**.

## Связанные темы

* [Использование свойств пользовательских действий и сессий для веб-приложений](/managed/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Mastering session and user action properties for enhanced analytics](https://www.youtube.com/watch?v=b8Vj0EoaDeM)