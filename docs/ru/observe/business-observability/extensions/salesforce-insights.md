---
title: Salesforce Insights
source: https://www.dynatrace.com/docs/observe/business-observability/extensions/salesforce-insights
scraped: 2026-03-06T21:14:39.366787
---

# Salesforce Insights

# Salesforce Insights

* Последняя версия Dynatrace
* Расширение
* 12 мин чтения
* Обновлено 06 окт. 2025 г.

Salesforce Insights позволяет администраторам Salesforce и командам ИТ-операций отслеживать свою среду Salesforce.

## Настройка

Узнайте, как настроить Salesforce Insights и какие данные оно может захватывать.

Убедитесь, что выполнены следующие требования для использования расширения.

### Учётная запись Salesforce

Расширение Salesforce может захватывать четыре типа данных Salesforce. Выберите каждую конфигурацию для получения подробной информации.

* Конфигурация [Event Streaming](#event-streaming) позволяет отслеживать использование вашей учётной записи Salesforce CRM.
* Конфигурация [EventLogFile](#eventlog) позволяет загружать файлы логов из Salesforce в Dynatrace.
* Конфигурация [API Queries](#soql) позволяет загружать данные Salesforce Object Query Language (SOQL) в Dynatrace. Данные загружаются в Dynatrace как события логов или бизнес-события.
* Конфигурация [Platform Events](#platform-events) позволяет подписываться на пользовательские события платформы Salesforce и загружать их в Dynatrace как бизнес-события.

### Аутентификация

Выберите один из трёх методов аутентификации, наиболее подходящий для ваших нужд.

Подключённое приложение

Пользователь и пароль

Client ID

В этом режиме расширение подключается как [подключённое приложение](https://dt-url.net/pv2c01v5). Это рекомендуемый механизм аутентификации.
Технически приложение реализует [поток OAuth 2.0 JWT Bearer](https://dt-url.net/yzs3qlb).

Dynatrace запросит:

* **Consumer Key** подключённого приложения.
* **Private Key** подключённого приложения.
* **Subject** JWT-токена — это имя пользователя, входящего в профиль подключённого приложения.

#### Требования

* `openssl` — для генерации сертификата, не нужен, если у вас уже есть сертификат и закрытый ключ

  Примечание: в Windows, если у вас установлен `git`, у вас также должна быть копия `openssl`.
  Вы найдёте его в каталоге, например `C:\Program Files\Git\mingw64\bin`, в зависимости от вашей установки.

#### Сертификат

У подключённого приложения должен быть сертификат, с помощью которого мы впоследствии аутентифицируемся в Salesforce, используя закрытый ключ этого сертификата.

Эта команда генерирует сертификат и закрытый ключ:

```
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out cert.pem
```

* Файл `cert.pem` будет добавлен в подключённое приложение.
* Файл `key.pem` будет использоваться Dynatrace для аутентификации в Salesforce.

#### Создание подключённого приложения

В Salesforce Lightning

1. В разделе **Setup** > **Apps** > **External Client Apps** > **Settings** убедитесь, что `Allow creation of connected apps` **включено**.
2. Выберите **New Connected App**.

Назовите приложение и добавьте контактный адрес электронной почты. В разделе **API (Enable OAuth Settings)**:

1. Установите флажок **Enable OAuth Settings**
2. Если Callback URL не используется, можно указать `http://localhost`
3. Установите флажок **Use digital signatures**
4. Загрузите сгенерированный файл `cert.pem` в разделе `Use digital signatures`.
5. В **Selected OAuth Scopes** добавьте следующие области:

   * **Manage use data via APIs (API)**
   * **Perform requests at any time (refresh\_token, offline\_access)**
6. Оставьте все остальные настройки по умолчанию и выберите **Save**.

#### Политика OAuth

1. Настройте разрешённых пользователей в **OAuth Policy**.
2. В разделе **Apps** > **App Manager** найдите подключённое приложение и выберите **Manage**.
3. Нажмите кнопку **Edit Policies**.
4. В разделе **OAuth Policies** выберите **Admin approved users are pre-authorized**.
5. Выберите **Save**.

#### Утверждённые пользователи

Определите пользователей, которые могут использовать приложение. Это можно сделать, добавив профили в список **Application Profile Assignment**.

1. На странице подключённого приложения перейдите в **Profiles** > **Manage Profiles**.
2. Добавьте профили, которые могут использовать подключённое приложение.
   Примечание: впоследствии любое имя пользователя из этих профилей можно использовать в качестве **Subject** при настройке расширения.

Профили требуют следующих разрешений для потоковой передачи событий:

* Общие разрешения пользователя

  + `View Real-Time Event Monitoring Data`
* Административные разрешения

  + `Customize Application`
  + `View All Data`

Для ознакомления с необходимой документацией по разрешениям см. [как включить доступ к мониторингу событий в реальном времени](https://dt-url.net/5343qhf).

1. Обычный пользователь Salesforce с разрешениями для нужной конфигурации (Event Streaming, Event Log File или SOQL).
2. Пароль пользователя.
3. [Токен безопасности](https://dt-url.net/oz23qoo) для пользователя.

Обратите внимание, что этот вариант не рекомендуется, так как пользовательские пароли и токены безопасности могут меняться; обычно он используется только для тестирования расширения.

Для [аутентификации Client ID](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_client_credentials_flow.htm&type=5) выберите **Enable Client Credentials Flow** в настройках Connected App или External Client App и укажите **Consumer Key** и **Consumer Secret**.

Вам также потребуется выбрать пользователя, от имени которого будет запускаться приложение. Это можно сделать в **App Manager** > **Manage** > **Edit Policies** > **Client Credentials Flow** > **Run As**.

Обратите внимание, что это менее безопасно, чем Connected App с сертификатом.

### Включение расширения

Для включения расширения Salesforce у вас должен быть Environment ActiveGate.

1. Найдите расширение в Hub и активируйте его.
2. Выберите **Add monitoring configuration** на странице конфигурации.
3. Выберите группу ActiveGate.

   * Один из этих серверов должен иметь доступ к Salesforce API, который общедоступен.
   * URL входа: `https://login.salesforce.com` или `https://test.salesforce.com`
   * Конечные точки Pub/Sub: `api.pubsub.salesforce.com:7443` или `api.deu.pubsub.salesforce.com:7443`
   * При необходимости можно настроить прокси.

Параметры конфигурации мониторинга

| Параметр | Описание |
| --- | --- |
| **Endpoint name** | Выберите понятное имя для идентификации конечной точки |
| **Login URL** | Выберите [Production](https://dt-url.net/lui3q3b) или [Sandbox](https://dt-url.net/okk3qle) |
| **Pub/Sub URL** | Выберите **Global Endpoint** или **Europe (Frankfurt) Endpoint** |
| **Reporting Mode** | **Business Events**, **Logs**, **OpenKit (RUM)** |
| **Custom Application ID** | Идентификатор пользовательского приложения Dynatrace для созданного приложения (необходим только при использовании управляемой среды и OpenKit в качестве режима отчётности.) |
| **Authentication type** | Выберите [имя пользователя и пароль](#user-password-authentication) или [подключённое приложение](#connected-app-authentication) |
| **Events filtering** | Выберите, какие события реального времени вы хотите отправлять в Dynatrace; по умолчанию все включены |
| **Usernames Blocklist** | Необязательный список имён пользователей для игнорирования; используйте его для блокировки пользователей автоматизации/API от отчётности |
| **Proxy** | Необязательный прокси; если ActiveGate не может подключиться к URL Salesforce |

OpenKit

Если вы используете OpenKit, рекомендуется начать с настройки пользовательского приложения.

## Приём данных Salesforce

Выберите один из трёх методов приёма данных в зависимости от ваших потребностей мониторинга.

Event Streaming

EventLogFile

API Queries (SOQL)

Platform Events

Захватывайте [события реального времени](https://dt-url.net/fj03qyl) из Salesforce и отправляйте их как [бизнес-события](/docs/observe/business-observability/bo-basic-concepts "Основные концепции Dynatrace Business Observability.") в Dynatrace.

[Приём RUM](/docs/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.") следует использовать только в управляемых средах.

1. Включите **Real-time event Streaming**.
2. В **Setup** > **Event Manager** включите **Streaming Data** для событий, которые вы хотите захватывать.
3. Получите учётные данные, необходимые расширению для подключения к Salesforce.

Включите такие варианты использования, как:

* Отслеживание перехвата сессий, атак с заполнением учётных данных и аномалий
* Отслеживание важных наборов разрешений и изменений
* Каковы самые медленные времена отклика страниц Lightning или Classic?
* Какие файлы загружаются, скачиваются и каким пользователем?
* Какие отчёты используются чаще всего, кто их запускает, какие запросы используются?
* Каковы самые популярные запросы API?
* Какие браузеры используют пользователи?
* Откуда осуществляется доступ к Salesforce?
* Сколько пользователей используют платформу в данный момент, каков их пользовательский опыт?

Расширение использует [Salesforce Pub/Sub API](https://dt-url.net/3843qs9) для прослушивания событий потоковой передачи. Эти события захватываются и отправляются как бизнес-события, или в случае OpenKit как **Действия пользователя** со всеми соответствующими свойствами, отправленными как **Свойства действий**.

Для подробного описания каждого события и его свойств см. [документацию Salesforce](https://dt-url.net/g1034yh).

### Текущие захватываемые события

| События | Описание |
| --- | --- |
| [ApiAnomalyEvent](https://dt-url.net/ax63qn2) | Отслеживание аномалий в том, как пользователи выполняют вызовы API. |
| [ApiEventStream](https://dt-url.net/1m83q6q) | Отслеживание запросов API пользователей в вашей организации. |
| [BulkApiResultEvent](https://dt-url.net/ioc3q4t) | Отслеживание, когда пользователь скачивает результаты запроса Bulk API. |
| [ConcurLongRunApexErrEvent](https://dt-url.net/19e3q2i) | Отслеживание возникновения ошибки Concurrent Long Running Apex. |
| [CredentialStuffingEvent](https://dt-url.net/avg3q25) | Отслеживание, когда пользователь успешно входит в Salesforce во время выявленной атаки с заполнением учётных данных. |
| [FileEvent](https://dt-url.net/sui3q40) | Отслеживание файловой активности. Например, отслеживание, когда пользователь скачивает или просматривает файл. |
| [LightningUriEventStream](https://dt-url.net/bbk3quc) | Отслеживание, когда пользователь создаёт, получает доступ, обновляет или удаляет запись в Salesforce Lightning. |
| [ListViewEventStream](https://dt-url.net/7a03qz2) | Отслеживание, когда пользователь получает доступ к данным с помощью представлений списков. |
| [LoginAsEventStream](https://dt-url.net/o423qb0) | Отслеживание, когда администратор входит в вашу организацию под именем другого пользователя. |
| [LoginEventStream](https://dt-url.net/un43qqg) | Отслеживание, когда пользователь входит в вашу организацию. |
| [LogoutEventStream](https://dt-url.net/7i63qh5) | Отслеживание, когда пользователь выходит из интерфейса Salesforce. |
| [PermissionSetEvent](https://dt-url.net/ay83qje) | Отслеживание, когда пользователям назначается разрешение Modify All Data или View All Data через набор разрешений. |
| [ReportAnomalyEvent](https://dt-url.net/0ga3qkk) | Отслеживание аномалий в том, как пользователи запускают или экспортируют отчёты. |
| [ReportEventStream](https://dt-url.net/9vc3q8c) | Отслеживание, когда пользователь получает доступ к данным или экспортирует их с помощью отчётов. |
| [SessionHijackingEvent](https://dt-url.net/1fe3q8b) | Отслеживание, когда несанкционированный пользователь получает контроль над сессией пользователя Salesforce с помощью украденного идентификатора сессии. |
| [UriEventStream](https://dt-url.net/fig3qk1) | Отслеживание, когда пользователь создаёт, получает доступ, обновляет или удаляет запись в Salesforce Classic. |

Расширение ограничено событиями, которые Salesforce генерирует как **события реального времени**.

Выберите режим отчётности для данных Event Streaming:

### Бизнес-события

Для бизнес-событий все данные принимаются с использованием API бизнес-событий.

Их можно запрашивать с помощью DQL:

```
fetch bizevents



| filter event.type == "salesforce.ApiEventStream"
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/query-event-streaming-1-1523-1e42763655.png)

Каждое из событий типа `salesforce.NameOfTheEvent` будет содержать все свойства, задокументированные Salesforce.
Например, см. [свойства для ApiEventStream](https://dt-url.net/1m83q6q).

Таким образом, можно создавать визуализации, используя все эти свойства.

```
fetch bizevents



| filter event.type == "salesforce.ApiEventStream"



| summarize count(), by: {SourceIp}
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-event-streaming-visualization-1054-0ead02b872.png)

Вы можете получить список всех типов событий с помощью DQL:

```
fetch bizevents



| filter event.provider == "https://dynatrace--staging.sandbox.my.salesforce.com"



| summarize count(), by: {event.type}
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-event-streaming-event-types-1047-67bd7752e5.png)

#### Пример: получение входов пользователей с течением времени

```
fetch bizevents



| filter event.type == "salesforce.LoginEventStream"



| makeTimeseries logins=count(), by:{Username}, interval: 5m



| sort logins desc
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-eventstreaming-users-1151-e4c2abe6c6.png)

### OpenKit

Чтобы создать пользовательское приложение для получения данных:

1. В Hub перейдите в раздел **Digital Experience Monitoring**. Затем выберите **Generic front end** > **Set up**.
2. Создайте ваше пользовательское приложение — назовите его и выберите значок.
3. Выберите **Monitor custom application**.

![custom-app-01](https://dt-cdn.net/images/custom-app-01-1251-cec1d8931d.png)

4. В **Custom application settings** перейдите в **Instrumentation wizard** и сохраните `Application ID` для дальнейшего использования.

![custom-app-02](https://dt-cdn.net/images/custom-app-02-937-2cdaf63646.png)

5. Теперь вы можете включить расширение. Подробности см. в разделе <#enable-extension>.

Данные отправляются в созданное вами приложение Frontend, поэтому вы можете получить доступ к:

* **Sessions Details**
* Отдельным свойствам, выбрав **User Action** > **Perform waterfall analysis**

Для использования этих свойств в [User Sessions Query Language](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как получать доступ и выполнять запросы к данным пользовательских сессий на основе ключевых слов, синтаксиса, функций и многого другого."):

1. В настройках приложения перейдите в **Session and user action properties**.
2. Создайте свойство.
   Примечание: имя должно точно совпадать с именем свойства, см. [события Salesforce](https://dt-url.net/bbk3quc).

Пример: захват количества строк

![salesforce-data-04](https://dt-cdn.net/images/data-04-822-d25b8f5d10.png)

Запрос свойства:

```
SELECT useraction.name, SUM(longProperties.rowsprocessed) FROM useraction WHERE useraction.name STARTSWITH "Report" GROUP BY useraction.name
```

![salesforce-data-05](https://dt-cdn.net/images/data-05-1232-2127c34f50.png)

## EventLogFile

Захватывайте [файлы логов событий](https://dt-url.net/0a03q0q) из Salesforce и принимайте их как [логи](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Передавайте данные логов в Dynatrace через API и позвольте Dynatrace преобразовать их в значимые сообщения логов.") в Dynatrace.

* EventLogFile необходимо включить в [Salesforce](https://dt-url.net/27u3qmr).
* У пользователя должны быть установлены разрешения для чтения файлов логов событий.

#### Детали

1. Создайте новую конфигурацию EventLogFile, выбрав **Configure EventLogFile**.
   Обратите внимание, что в разделе **Events to capture** все различные файлы логов по умолчанию будут отключены.
2. Выберите, какие файлы логов вы хотите принимать.

Не ожидайте данных в реальном времени из этой конфигурации. Данные логов событий [задерживаются на несколько часов](https://dt-url.net/aqm3qh5) в Salesforce.

#### Визуализация

События отправляются в Dynatrace как события логов и могут быть запрошены с помощью DQL:

```
fetch logs



| filter query.type == "EventLogFile"
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-eventlogfile-1-1058-92cd80e16c.png)

Все свойства определённого файла логов событий будут доступны.
Для получения сведений о полях см. [поддерживаемые типы событий EventLogFile](https://dt-url.net/0a03q0q).

#### Пример

Получение деталей событий `ApexExecution`:

```
fetch logs



| filter EVENT_TYPE == "ApexExecution"



| fields TIMESTAMP_DERIVED, ENTRY_POINT, EXEC_TIME, CPU_TIME, DB_TOTAL_TIME, NUMBER_SOQL_QUERIES
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-eventlogfile-2-1144-a972a14519.png)

## API Queries (SOQL)

Выполняйте [запросы SOQL](https://dt-url.net/ox23q6n) к Salesforce и принимайте данные как [логи](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Передавайте данные логов в Dynatrace через API и позвольте Dynatrace преобразовать их в значимые сообщения логов.") или бизнес-события.
У пользователя должны быть разрешения для запроса Salesforce API и чтения запрашиваемых **объектов**.

#### Детали

Для загрузки данных Salesforce Object Query Language (SOQL) в Dynatrace:

1. Выберите **Configure API queries**.
2. Добавьте до 100 SOQL-запросов для выполнения с указанным интервалом.
   Каждый запрос имеет следующие параметры:

   * **Query Name** — имя запроса, которое поможет вам найти эти данные запроса позже в Dynatrace Logs.
   * **Query** — выполняемый SOQL-запрос.

     + Запрос **должен** содержать хотя бы одно поле datetime.
     + Заполнитель `{last_execution_timestamp}` **должен** использоваться для фильтрации результатов запроса и дедупликации данных.
     + Пример: `SELECT Id, CreatedDate, Field, NewValue, OldValue FROM OpportunityFieldHistory WHERE CreatedDate > {last_execution_timestamp}`
   * **Frequency**

     + Частота может быть типа **Interval** или **Cron**.
     + **Interval** — запрос будет выполняться каждые X минут.
     + **Cron** — запрос будет выполняться на основе предоставленного выражения cron; вы можете использовать [crontab guru](https://dt-url.net/j0o3qxt) для генерации выражения cron.

#### Визуализация

Рассмотрим следующую конфигурацию запроса:

```
Query Name: Logins



Query: SELECT UserId, COUNT(Id) from LoginHistory WHERE LoginTime > {last_execution_timestamp} GROUP BY UserId
```

![img.png](https://dt-cdn.net/images/query-logins-607-41fe169e79.png)

Результаты можно получить с помощью DQL:

```
fetch logs



| filter query.name == "Logins"
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-api-query-1577-d62b4ba57b.png)

Диаграмму можно создать с помощью:

```
fetch logs



| filter query.name == "Logins"



| makeTimeseries sum(toDouble(expr0)), by: {UserId}, interval: 5m
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-api-query-chart-1139-89bb9c3aa6.png)

Вы также можете получить все запросы и их тексты, настроенные для данного экземпляра Salesforce:

```
fetch logs



| filter event.provider == "https://dynatrace--staging.sandbox.my.salesforce.com"



| summarize count(), by: {query.name}
```

Визуализация результата запроса

![img.png](https://dt-cdn.net/images/dql-all-queries-1140-350b2a1991.png)

## Platform Events

Подписывайтесь на пользовательские [Salesforce Platform Events](https://developer.salesforce.com/docs/atlas.en-us.250.0.platform_events.meta/platform_events/platform_events_intro.htm) и принимайте их как [бизнес-события](/docs/observe/business-observability/bo-basic-concepts "Основные концепции Dynatrace Business Observability.") в Dynatrace.

Platform Events предоставляют мощный способ отправки и получения пользовательских уведомлений о событиях внутри Salesforce и во внешние системы. Эта конфигурация позволяет захватывать данные о событиях в реальном времени из пользовательских платформенных событий, стандартных платформенных событий и событий захвата изменений данных.

#### Детали

Для приёма Salesforce Platform Events в Dynatrace:

1. Выберите **Configure Platform Events**.
2. Добавьте темы, на которые вы хотите подписаться. Темы имеют следующие форматы:

   * **Custom Platform Events**: `/event/YourCustomEvent__e`
   * **Standard Platform Events**: `/event/LoginEventStream`, `/event/LogoutEventStream`
   * **Change Data Capture**: `/data/ChangeEvents`, `/data/AccountChangeEvent`
3. Настройте аутентификацию с помощью одного из поддерживаемых методов (Connected App, User and Password или Client ID).

#### Варианты использования

Включите такие варианты использования, как:

* Мониторинг пользовательских бизнес-процессов и рабочих процессов
* Отслеживание изменений критически важных объектов Salesforce с помощью Change Data Capture
* Интеграция с внешними системами с использованием пользовательских Platform Events
* Создание дашбордов и оповещений в реальном времени на основе событий Salesforce
* Корреляция событий Salesforce с другими данными наблюдаемости

#### Визуализация

Platform Events отправляются в Dynatrace как бизнес-события и могут быть запрошены с помощью DQL:

```
fetch bizevents



| filter event.type == "salesforce.YourCustomEvent__e"
```

Пример: запрос всех Platform Events из экземпляра Salesforce

```
fetch bizevents



| filter event.provider == "https://yourinstance.my.salesforce.com"



| summarize count(), by: {event.type}
```

Каждое Platform Event будет включать все пользовательские поля, определённые для события, что делает их доступными для фильтрации, группировки и визуализации.

## Расширение периода хранения данных Salesforce Insights

По умолчанию принятые данные хранятся 30 дней. Вы можете изменить время хранения, создав пользовательский [бакет](/docs/observe/business-observability/bo-event-processing/bo-bucket-assignment "Назначьте период хранения данным бизнес-событий в Dynatrace через классический конвейер.").

Чтобы создать пользовательский бакет для события Salesforce

1. В Dynatrace перейдите в **Settings** > **Business Observability** > **Bucket assignment**.
2. На странице **Business event bucket assignment** выберите **Add rule** и назовите ваше правило.
3. В поле **Bucket** выберите период хранения.
4. Добавьте **Matcher** к вашему правилу, введя или вставив ваш [специфичный для матчера DQL-запрос](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "Это DQL-матчер в событиях классического конвейера."). События, соответствующие вашему правилу, будут назначены в выбранный вами бакет. Если ни одно правило не совпадает, события будут назначены в бакет по умолчанию. Чтобы назначить все ваши события Salesforce в ваш бакет, необходимо использовать матчер, содержащий функцию `matchesValue` и URL Salesforce, как в примере ниже.

   ```
   matchesValue(event.provider, "https://environment.my.salesforce.com")
   ```
5. Выберите **Save changes**.

## Устранение неполадок

Журналы ошибок можно получить через Dynatrace, перейдя на страницу расширения и выбрав **Status** для каждой конфигурации мониторинга.

Подробные журналы можно получить, создав [диагностику ActiveGate](/docs/ingest-from/dynatrace-activegate/activegate-diagnostics "Узнайте, как запустить диагностику ActiveGate").
