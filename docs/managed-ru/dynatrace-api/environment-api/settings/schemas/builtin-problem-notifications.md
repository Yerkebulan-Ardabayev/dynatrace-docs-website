---
title: Settings API - Problem notifications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-problem-notifications
scraped: 2026-05-12T11:40:53.824560
---

# Settings API - Problem notifications schema table

# Settings API - Problem notifications schema table

* Опубликовано 5 декабря 2023 г.

### Problem notifications (`builtin:problem.notifications)`

Интегрируйте problem notifications Dynatrace с существующей системой incident-management или с командным каналом совместной работы. Внутри problem integrations используются alerting profiles, чтобы отфильтровать общий поток alerts до подмножества, релевантного вашей команде.

Подробнее см. [Third-party integrations](https://dt-url.net/j803tgc).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:problem.notifications` | * `group:integration` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.notifications` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:problem.notifications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.notifications` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Тип notification `type` | enum | Возможные значения: * `EMAIL` * `SLACK` * `JIRA` * `ANSIBLETOWER` * `OPS_GENIE` * `PAGER_DUTY` * `VICTOROPS` * `WEBHOOK` * `XMATTERS` * `TRELLO` * `SERVICE_NOW` | Required |
| Отображаемое имя `displayName` | text | Имя notification configuration. | Required |
| `emailNotification` | [EmailNotification](#EmailNotification) | - | Required |
| `slackNotification` | [SlackNotification](#SlackNotification) | - | Required |
| `jiraNotification` | [JiraNotification](#JiraNotification) | - | Required |
| `ansibleTowerNotification` | [AnsibleTowerNotification](#AnsibleTowerNotification) | - | Required |
| `opsGenieNotification` | [OpsGenieNotification](#OpsGenieNotification) | - | Required |
| `pagerDutyNotification` | [PagerDutyNotification](#PagerDutyNotification) | - | Required |
| `victorOpsNotification` | [VictorOpsNotification](#VictorOpsNotification) | - | Required |
| `webHookNotification` | [WebHookNotification](#WebHookNotification) | - | Required |
| `xMattersNotification` | [XMattersNotification](#XMattersNotification) | - | Required |
| `trelloNotification` | [TrelloNotification](#TrelloNotification) | - | Required |
| `serviceNowNotification` | [ServiceNowNotification](#ServiceNowNotification) | - | Required |
| Alerting profile `alertingProfile` | setting | Выберите alerting profile (`<your-dynatrace-url>//ui/settings/builtin:alerting.profile`), чтобы управлять доставкой problem notifications, связанных с этой integration. | Required |

##### Объект `EmailNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Кому `recipients` | set | - | Required |
| CC `ccRecipients` | set | - | Required |
| BCC `bccRecipients` | set | - | Required |
| Тема `subject` | text | Тема email-уведомлений. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |
| Слать email при закрытии problem `notifyClosedProblems` | boolean | - | Required |
| Тело `body` | text | Шаблон email-уведомлений. Введите '{' для подсказок placeholder.  **{ImpactedEntities}**: данные об entities, на которые повлиял problem, в виде json-массива.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsHTML}**: все детали problem event, включая root cause, как HTML-форматированная строка.  **{ProblemDetailsJSONv2}**: problem как json-объект, следующий структуре [Dynatrace Problems V2 API](https://dt-url.net/7a03ti2). Опциональные поля evidenceDetails и impactAnalysis включены, recentComments не входит.  **{ProblemDetailsJSON}**: problem как json-объект, следующий структуре [Dynatrace Problems V1 API](https://dt-url.net/qn23tk2).  **{ProblemDetailsMarkdown}**: все детали problem event, включая root cause, как Markdown-форматированная строка.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `SlackNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL `url` | secret | Настройте incoming WebHook integration в вашем Slack account. Скопируйте и вставьте сгенерированный WebHook URL в поле выше. | Required |
| Канал `channel` | text | Канал (например, `#general`) или пользователь (например, `@john.smith`), которому отправляется сообщение. | Required |
| Сообщение `message` | text | Содержимое сообщения. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `JiraNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL Jira endpoint `url` | text | URL endpoint Jira API. | Required |
| Имя пользователя `username` | text | Имя пользователя Jira profile. | Required |
| API token `apiToken` | secret | API token для Jira profile. Password-аутентификация [была deprecated в Jira](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-basic-auth-and-cookie-based-auth/) | Required |
| Project key `projectKey` | text | Project key Jira issue, создаваемого этим уведомлением. | Required |
| Тип issue `issueType` | text | Тип Jira issue, создаваемого этим уведомлением. Чтобы найти все доступные типы issue или создать свой, в JIRA перейдите в Options > Issues. | Required |
| Summary `summary` | text | Summary Jira issue, создаваемого этим уведомлением. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |
| Описание issue `description` | text | Description Jira issue, создаваемого этим уведомлением. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `AnsibleTowerNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL job template `jobTemplateURL` | text | URL целевого job template. Например, https:///#/templates/job\_template/ **Note:** обязательно выберите опцию **Prompt on Launch** в секции Extra Variables конфигурации job template. | Required |
| Принимать любой SSL-сертификат (включая self-signed и невалидные) `acceptAnyCertificate` | boolean | - | Required |
| Имя пользователя `username` | text | Имя пользователя account. | Required |
| Пароль `password` | secret | Пароль account. | Required |
| Custom-сообщение (необязательно) `customMessage` | text | Это сообщение будет отображаться в поле Extra Variables **Message** вашего job template. Введите '{' для подсказок placeholder.  **{ImpactedEntities}**: данные об entities, на которые повлиял problem, в виде json-массива.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `OpsGenieNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| API-ключ OpsGenie `apiKey` | secret | API-ключ для доступа к OpsGenie. Перейдите в OpsGenie-Integrations и создайте новую Dynatrace integration. Скопируйте созданный API-ключ. | Required |
| Региональный домен OpsGenie `domain` | text | Региональный домен OpsGenie. Например, **api.opsgenie.com** для US или **api.eu.opsgenie.com** для EU. | Required |
| Сообщение `message` | text | Содержимое сообщения. Введите '{' для подсказок placeholder.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ImpactedEntityNames}**: entity, на которую повлиял problem (или несколько затронутых entities). | Required |

##### Объект `PagerDutyNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Account `account` | text | Имя PagerDuty account. | Required |
| Имя service `serviceName` | text | Имя service. | Required |
| Service key `serviceApiKey` | secret | Events API-ключ для доступа к PagerDuty. | Required |

##### Объект `VictorOpsNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| API-ключ `apiKey` | secret | API-ключ для целевого Splunk On-Call account. Получите API-ключ Splunk On-Call здесь: Settings -> Integrations -> Rest Endpoint -> Dynatrace. | Required |
| Routing key `routingKey` | text | Routing key, определяющий группу для уведомления. | Required |
| Сообщение `message` | text | Содержимое сообщения. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED. | Required |

##### Объект `WebHookNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Секретный webhook URL `urlContainsSecret` | boolean | - | Optional |
| Webhook URL `url` | text | URL endpoint webhook. | Required |
| Webhook URL `secretUrl` | secret | Секретный URL endpoint webhook. | Required |
| Принимать любой SSL-сертификат (включая self-signed и невалидные) `acceptAnyCertificate` | boolean | - | Required |
| Вызывать webhook при merge новых events в существующие problems `notifyEventMergesEnabled` | boolean | - | Required |
| Вызывать webhook при закрытии problem `notifyClosedProblems` | boolean | - | Required |
| Использовать OAuth 2.0 для аутентификации `useOAuth2` | boolean | - | Optional |
| OAuth 2.0 credentials `oAuth2Credentials` | [OAuth2Credentials](#OAuth2Credentials) | Для аутентификации integration используется OAuth 2.0 *Client Credentials* Flow (Grant Type). Подробнее см. [Client Credentials Flow](https://dt-url.net/ym22wsm)). Полученный Access Token передаётся в заголовке *Authorization* запроса, переносящего payload уведомления. | Required |
| Дополнительные HTTP-заголовки `headers` | Set<[WebHookNotificationHeader](#WebHookNotificationHeader)> | Список дополнительных HTTP-заголовков. | Required |
| Custom payload `payload` | text | Содержимое сообщения уведомления. Введите '{' для подсказок placeholder.  **{ImpactedEntities}**: данные об entities, на которые повлиял problem, в виде json-массива.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsHTML}**: все детали problem event, включая root cause, как HTML-форматированная строка.  **{ProblemDetailsJSONv2}**: problem как json-объект, следующий структуре [Dynatrace Problems V2 API](https://dt-url.net/7a03ti2). Опциональные поля evidenceDetails и impactAnalysis включены, recentComments не входит.  **{ProblemDetailsJSON}**: problem как json-объект, следующий структуре [Dynatrace Problems V1 API](https://dt-url.net/qn23tk2).  **{ProblemDetailsMarkdown}**: все детали problem event, включая root cause, как Markdown-форматированная строка.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `XMattersNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| xMatters URL `url` | text | URL webhook xMatters. | Required |
| Принимать любой SSL-сертификат (включая self-signed и невалидные) `acceptAnyCertificate` | boolean | - | Required |
| Дополнительные HTTP-заголовки `headers` | Set<[WebHookNotificationHeader](#WebHookNotificationHeader)> | Список дополнительных HTTP-заголовков. | Required |
| Custom payload `payload` | text | Содержимое сообщения уведомления. Введите '{' для подсказок placeholder.  **{ImpactedEntities}**: данные об entities, на которые повлиял problem, в виде json-массива.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsHTML}**: все детали problem event, включая root cause, как HTML-форматированная строка.  **{ProblemDetailsJSONv2}**: problem как json-объект, следующий структуре [Dynatrace Problems V2 API](https://dt-url.net/7a03ti2). Опциональные поля evidenceDetails и impactAnalysis включены, recentComments не входит.  **{ProblemDetailsJSON}**: problem как json-объект, следующий структуре [Dynatrace Problems V1 API](https://dt-url.net/qn23tk2).  **{ProblemDetailsMarkdown}**: все детали problem event, включая root cause, как Markdown-форматированная строка.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `TrelloNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Application key Trello `applicationKey` | text | Application key для Trello account. Вы должны быть залогинены в Trello, чтобы Trello автоматически сгенерировал application key. [Получить application key](https://trello.com/app-key) | Required |
| Authorization token Trello `authorizationToken` | secret | Authorization token для Trello account. | Required |
| ID доски Trello, к которой привязываются problem cards `boardId` | text | - | Required |
| ID списка Trello, к которому привязываются новые problem cards `listId` | text | - | Required |
| ID списка Trello, к которому привязываются resolved problem cards `resolvedListId` | text | - | Required |
| Текст карточки `text` | text | Текст карточки и placeholders problem, появляющиеся на новых problem cards. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |
| Описание карточки `description` | text | Description Trello card. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsMarkdown}**: все детали problem event, включая root cause, как Markdown-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{ProblemURL}**: URL problem в Dynatrace.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |

##### Объект `ServiceNowNotification`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Идентификатор инстанса ServiceNow `instanceName` | text | Идентификатор инстанса ServiceNow. Это первая часть вашего ServiceNow URL. Поле взаимоисключающее с полем **url**: допустимо использовать только одно из них. | Required |
| OnPremise URL `url` | text | URL on-premise ServiceNow installation. Поле взаимоисключающее с полем **instanceName**: допустимо использовать только одно из них. | Optional |
| Имя пользователя `username` | text | Имя пользователя ServiceNow account. Убедитесь, что у пользователя есть роли `web_service_admin` и `x_dynat_ruxit.Integration`. | Required |
| Пароль `password` | secret | Пароль ServiceNow account. | Required |
| Описание `message` | text | Содержимое ServiceNow description. Введите '{' для подсказок placeholder.  **{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).  **{ImpactedEntityNames}**: entity, на которую повлиял problem.  **{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.  **{PID}**: уникальный системный идентификатор зафиксированного problem.  **{ProblemDetailsHTML}**: все детали problem event, включая root cause, как HTML-форматированная строка.  **{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.  **{ProblemID}**: отображаемый номер зафиксированного problem.  **{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.  **{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION или CUSTOM\_ALERT.  **{ProblemTitle}**: краткое описание problem.  **{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.  **{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется. | Required |
| Слать incidents в ServiceNow ITSM. `sendIncidents` | boolean | - | Required |
| Слать events в ServiceNow ITOM. `sendEvents` | boolean | - | Required |
| Использовать text-формат для problem details вместо HTML. `formatProblemDetailsAsText` | boolean | - | Optional |

##### Объект `OAuth2Credentials`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL access token `accessTokenUrl` | text | - | Required |
| Client ID `clientId` | text | - | Required |
| Client secret `clientSecret` | secret | - | Required |
| Scope `scope` | text | Запрашиваемый scope доступа | Optional |
| Включить client credentials в HTTP-заголовок "Authorization" по схеме HTTP "Basic". `authenticateViaRequestHeader` | boolean | Если false, client credentials включаются в тело HTTP-запроса. | Optional |

##### Объект `WebHookNotificationHeader`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Имя HTTP-заголовка. | Required |
| Скрытое значение HTTP-заголовка `secret` | boolean | - | Required |
| Значение `value` | text | Значение HTTP-заголовка. Может быть пустым. | Required |
| Значение `secretValue` | secret | Секретное значение HTTP-заголовка. Может быть пустым. | Required |