---
title: Settings API - Security notifications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-notification-integration
scraped: 2026-05-12T11:43:50.526365
---

# Settings API - Security notifications schema table

# Settings API - Security notifications schema table

* Опубликовано 5 декабря 2023 г.

### Security notifications (`builtin:appsec.notification-integration)`

Интегрируйте security notifications с существующей системой incident-management или с командным каналом совместной работы. Внутри security integrations используйте alerting profiles для vulnerability и attack, чтобы отфильтровать общий поток alerts до тех, что релевантны вашей команде.

Подробнее см. [Security notifications](https://dt-url.net/ly039s4).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:appsec.notification-integration` | * `group:integration` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-integration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.notification-integration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-integration` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Тип security alert `trigger` | enum | Возможные значения: * `SECURITY_PROBLEM` * `ATTACK_CANDIDATE` | Required |
| Тип notification `type` | enum | Возможные значения: * `WEBHOOK` * `JIRA` * `EMAIL` | Required |
| Отображаемое имя `displayName` | text | - | Required |
| `webhookConfiguration` | [WebhookConfiguration](#WebhookConfiguration) | - | Required |
| `securityProblemBasedWebhookPayload` | [SecurityProblemBasedWebhookPayload](#SecurityProblemBasedWebhookPayload) | - | Required |
| `attackCandidateBasedWebhookPayload` | [AttackCandidateBasedWebhookPayload](#AttackCandidateBasedWebhookPayload) | - | Required |
| `jiraConfiguration` | [JiraConfiguration](#JiraConfiguration) | - | Required |
| `securityProblemBasedJiraPayload` | [SecurityProblemBasedJiraPayload](#SecurityProblemBasedJiraPayload) | - | Required |
| `attackCandidateBasedJiraPayload` | [AttackCandidateBasedJiraPayload](#AttackCandidateBasedJiraPayload) | - | Required |
| `emailConfiguration` | [EmailConfiguration](#EmailConfiguration) | - | Required |
| `securityProblemBasedEmailPayload` | [SecurityProblemBasedEmailPayload](#SecurityProblemBasedEmailPayload) | - | Required |
| `attackCandidateBasedEmailPayload` | [AttackCandidateBasedEmailPayload](#AttackCandidateBasedEmailPayload) | - | Required |
| Alerting profile `securityProblemBasedAlertingProfile` | setting | Выберите alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-alerting-profile`), чтобы управлять доставкой security notifications, связанных с этой integration. | Required |
| Alerting profile `attackCandidateBasedAlertingProfile` | setting | Выберите alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-attack-alerting-profile`), чтобы управлять доставкой security notifications, связанных с этой integration. | Required |

##### Объект `WebhookConfiguration`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL webhook endpoint `url` | text | - | Required |
| Принимать любой SSL-сертификат (включая self-signed и невалидные) `acceptAnyCertificate` | boolean | - | Required |
| Дополнительные HTTP-заголовки `headers` | Set<[WebhookConfigurationHeader](#WebhookConfigurationHeader)> | Используйте дополнительные HTTP-заголовки для передачи любой дополнительной информации: configuration, authorization, metadata. JSON-based webhook endpoints требуют заголовка **Content-Type: application/json** для escaping специальных символов и предотвращения malformed JSON-контента. | Required |

##### Объект `SecurityProblemBasedWebhookPayload`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Custom payload `payload` | text | Содержимое сообщения уведомления при его просмотре пользователями.  Если значение security problem не задано, placeholder заменяется пустой строкой.  **Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в custom payload может привести к утечке информации к недоверенным сторонам.  Доступные placeholders:  **{SecurityProblemId}**: уникальный идентификатор, назначаемый Dynatrace, например, "S-1234".  **{Title}**: краткое описание типа найденной vulnerability, например, "Remote Code Execution".  **{Description}**: более детальное описание vulnerability.  **{CvssScore}**: CVSS score найденной vulnerability, например, "10.0". Может быть пустым. **{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/), это улучшенный risk-calculation score на основе CVSS, например, "10.0".  **{Severity}**: severity security problem, например, "Critical" или "Medium".  **{SecurityProblemUrl}**: URL security problem в Dynatrace.  **{AffectedEntities}**: данные об entities, затронутых security problem, в виде json-массива.  **{ManagementZones}**: разделённый запятыми список всех management zones, затронутых vulnerability на момент обнаружения.  **{Tags}**: разделённый запятыми список tags, заданных для entities, затронутых vulnerability. Например: "PROD, owner:John". Укажите ключ tag в квадратных скобках: **{Tags[key]}**, чтобы получить все связанные значения. Например: "{Tags[owner]}" будет преобразовано в "John". Tags без значения преобразуются в пустую строку.  **{Exposed}**: описывает, открыт ли один или несколько затронутых процессов в публичный Интернет. Может быть "true" или "false".  **{DataAssetsReachable}**: описывает, может ли один или несколько затронутых процессов достичь data assets. Может быть "true" или "false".  **{ExploitAvailable}**: описывает, существует ли exploit для этой vulnerability. Может быть "true" или "false". | Required |

##### Объект `AttackCandidateBasedWebhookPayload`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Custom payload `payload` | text | Содержимое сообщения уведомления при его просмотре пользователями.  Если значение attack не задано, placeholder заменяется пустой строкой.  **Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в custom payload может привести к утечке информации к недоверенным сторонам.  Доступные placeholders:  **{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например: "A-1234".  **{Title}**: место расположения attack, например: "com.dynatrace.Class.method():120"  **{Type}**: тип attack, например: "SQL Injection".  **{AttackUrl}**: URL attack в Dynatrace.  **{ProcessGroupId}**: данные об атакованной process group.  **{EntryPoint}**: entry point attack в процесс, например: "/login". Может быть пустым.  **{Status}**: статус attack, например: "Exploited"  **{Timestamp}**: время, когда произошла attack.  **{VulnerabilityName}**: имя связанной code-level vulnerability, например: "InMemoryDatabaseCaller.getAccountInfo():51". Может быть пустым. | Required |

##### Объект `JiraConfiguration`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL Jira endpoint `url` | text | URL endpoint Jira API. | Required |
| Имя пользователя `username` | text | Имя пользователя Jira profile. | Required |
| API token `apiToken` | secret | API token для Jira profile. Password-аутентификация [была deprecated в Jira](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-basic-auth-and-cookie-based-auth/) | Required |
| Project key `projectKey` | text | Project key Jira issue, создаваемого этим уведомлением. | Required |
| Тип issue `issueType` | text | Тип Jira issue, создаваемого этим уведомлением. Чтобы найти все доступные типы issue или создать свой, в Jira перейдите в Project settings > Issue types. | Required |

##### Объект `SecurityProblemBasedJiraPayload`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Summary `summary` | text | Summary Jira issue, создаваемого этим уведомлением.  **Note:** поле Jira summary должно содержать менее 255 символов. Любой контент сверх этого лимита после раскрытия placeholders отбрасывается.  Доступные placeholders:  **{SecurityProblemId}**: уникальный идентификатор, назначаемый Dynatrace, например, "S-1234".  **{Title}**: краткое описание типа найденной vulnerability, например, "Remote Code Execution".  **{CvssScore}**: CVSS score найденной vulnerability, например, "10.0". Может быть пустым. **{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/), это улучшенный risk-calculation score на основе CVSS, например, "10.0".  **{Severity}**: severity security problem, например, "Critical" или "Medium".  **{SecurityProblemUrl}**: URL security problem в Dynatrace.  **{Exposed}**: описывает, открыт ли один или несколько затронутых процессов в публичный Интернет. Может быть "true" или "false".  **{DataAssetsReachable}**: описывает, может ли один или несколько затронутых процессов достичь data assets. Может быть "true" или "false".  **{ExploitAvailable}**: описывает, существует ли exploit для этой vulnerability. Может быть "true" или "false". | Required |
| Описание issue `description` | text | Description Jira issue, создаваемого этим уведомлением.  Если значение security problem не задано, placeholder заменяется пустой строкой.  **Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в description может привести к утечке информации к недоверенным сторонам.  Доступные placeholders:  **{SecurityProblemId}**: уникальный идентификатор, назначаемый Dynatrace, например, "S-1234".  **{Title}**: краткое описание типа найденной vulnerability, например, "Remote Code Execution".  **{Description}**: более детальное описание vulnerability.  **{CvssScore}**: CVSS score найденной vulnerability, например, "10.0". Может быть пустым. **{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/), это улучшенный risk-calculation score на основе CVSS, например, "10.0".  **{Severity}**: severity security problem, например, "Critical" или "Medium".  **{SecurityProblemUrl}**: URL security problem в Dynatrace.  **{AffectedEntities}**: данные об entities, затронутых security problem, в виде json-массива.  **{ManagementZones}**: разделённый запятыми список всех management zones, затронутых vulnerability на момент обнаружения.  **{Tags}**: разделённый запятыми список tags, заданных для entities, затронутых vulnerability. Например: "PROD, owner:John". Укажите ключ tag в квадратных скобках: **{Tags[key]}**, чтобы получить все связанные значения. Например: "{Tags[owner]}" будет преобразовано в "John". Tags без значения преобразуются в пустую строку.  **{Exposed}**: описывает, открыт ли один или несколько затронутых процессов в публичный Интернет. Может быть "true" или "false".  **{DataAssetsReachable}**: описывает, может ли один или несколько затронутых процессов достичь data assets. Может быть "true" или "false".  **{ExploitAvailable}**: описывает, существует ли exploit для этой vulnerability. Может быть "true" или "false". | Required |

##### Объект `AttackCandidateBasedJiraPayload`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Summary `summary` | text | Summary Jira issue, создаваемого этим уведомлением.  **Note:** поле Jira summary должно содержать менее 255 символов. Любой контент сверх этого лимита после раскрытия placeholders отбрасывается.  Доступные placeholders:  **{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например, "A-1234".  **{Title}**: место расположения attack, например: "com.dynatrace.Class.method():120"  **{Type}**: тип attack, например: "SQL Injection".  **{AttackUrl}**: URL attack в Dynatrace.  **{ProcessGroupId}**: данные об атакованной process group.  **{EntryPoint}**: entry point attack в процесс, например: "/login". Может быть пустым.  **{Status}**: статус attack, например: "Exploited"  **{Timestamp}**: время, когда произошла attack.  **{VulnerabilityName}**: имя связанной code-level vulnerability, например: "InMemoryDatabaseCaller.getAccountInfo():51". Может быть пустым. | Required |
| Описание issue `description` | text | Description Jira issue, создаваемого этим уведомлением.  Если значение attack не задано, placeholder заменяется пустой строкой.  **Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в description может привести к утечке информации к недоверенным сторонам.  Доступные placeholders:  **{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например: "A-1234".  **{Title}**: место расположения attack, например: "com.dynatrace.Class.method():120"  **{Type}**: тип attack, например: "SQL Injection".  **{AttackUrl}**: URL attack в Dynatrace.  **{ProcessGroupId}**: данные об атакованной process group.  **{EntryPoint}**: entry point attack в процесс, например: "/login". Может быть пустым.  **{Status}**: статус attack, например: "Exploited"  **{Timestamp}**: время, когда произошла attack.  **{VulnerabilityName}**: имя связанной code-level vulnerability, например: "InMemoryDatabaseCaller.getAccountInfo():51". Может быть пустым. | Required |

##### Объект `EmailConfiguration`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Кому `recipients` | set | - | Required |
| CC `ccRecipients` | set | - | Required |
| BCC `bccRecipients` | set | - | Required |

##### Объект `SecurityProblemBasedEmailPayload`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тема `subject` | text | Тема email-уведомлений.  Доступные placeholders:  **{SecurityProblemId}**: уникальный идентификатор, назначаемый Dynatrace, например, "S-1234".  **{Title}**: краткое описание типа найденной vulnerability, например, "Remote Code Execution".  **{CvssScore}**: CVSS score найденной vulnerability, например, "10.0". Может быть пустым. **{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/), это улучшенный risk-calculation score на основе CVSS, например, "10.0".  **{Severity}**: severity security problem, например, "Critical" или "Medium".  **{SecurityProblemUrl}**: URL security problem в Dynatrace.  **{Exposed}**: описывает, открыт ли один или несколько затронутых процессов в публичный Интернет. Может быть "true" или "false".  **{DataAssetsReachable}**: описывает, может ли один или несколько затронутых процессов достичь data assets. Может быть "true" или "false".  **{ExploitAvailable}**: описывает, существует ли exploit для этой vulnerability. Может быть "true" или "false". | Required |
| Тело `body` | text | Шаблон email-уведомлений.  Если значение security problem не задано, placeholder заменяется пустой строкой.  **Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в description может привести к утечке информации к недоверенным сторонам.  Доступные placeholders:  **{SecurityProblemId}**: уникальный идентификатор, назначаемый Dynatrace, например, "S-1234".  **{Title}**: краткое описание типа найденной vulnerability, например, "Remote Code Execution".  **{Description}**: более детальное описание vulnerability.  **{CvssScore}**: CVSS score найденной vulnerability, например, "10.0". Может быть пустым. **{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/), это улучшенный risk-calculation score на основе CVSS, например, "10.0".  **{Severity}**: severity security problem, например, "Critical" или "Medium".  **{SecurityProblemUrl}**: URL security problem в Dynatrace.  **{AffectedEntities}**: данные об entities, затронутых security problem, в виде json-массива.  **{ManagementZones}**: разделённый запятыми список всех management zones, затронутых vulnerability на момент обнаружения.  **{Tags}**: разделённый запятыми список tags, заданных для entities, затронутых vulnerability. Например: "PROD, owner:John". Укажите ключ tag в квадратных скобках: **{Tags[key]}**, чтобы получить все связанные значения. Например: "{Tags[owner]}" будет преобразовано в "John". Tags без значения преобразуются в пустую строку.  **{Exposed}**: описывает, открыт ли один или несколько затронутых процессов в публичный Интернет. Может быть "true" или "false".  **{DataAssetsReachable}**: описывает, может ли один или несколько затронутых процессов достичь data assets. Может быть "true" или "false".  **{ExploitAvailable}**: описывает, существует ли exploit для этой vulnerability. Может быть "true" или "false". | Required |

##### Объект `AttackCandidateBasedEmailPayload`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тема `subject` | text | Тема email-уведомлений.  Доступные placeholders:  **{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например, "A-1234".  **{Title}**: место расположения attack, например: "com.dynatrace.Class.method():120"  **{Type}**: тип attack, например: "SQL Injection".  **{AttackUrl}**: URL attack в Dynatrace.  **{ProcessGroupId}**: данные об атакованной process group.  **{EntryPoint}**: entry point attack в процесс, например: "/login". Может быть пустым.  **{Status}**: статус attack, например: "Exploited"  **{Timestamp}**: время, когда произошла attack.  **{VulnerabilityName}**: имя связанной code-level vulnerability, например: "InMemoryDatabaseCaller.getAccountInfo():51". Может быть пустым. | Required |
| Тело `body` | text | Шаблон email-уведомлений.  Если значение security problem не задано, placeholder заменяется пустой строкой.  **Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в body может привести к утечке информации к недоверенным сторонам.  Доступные placeholders:  **{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например: "A-1234".  **{Title}**: место расположения attack, например: "com.dynatrace.Class.method():120"  **{Type}**: тип attack, например: "SQL Injection".  **{AttackUrl}**: URL attack в Dynatrace.  **{ProcessGroupId}**: данные об атакованной process group.  **{EntryPoint}**: entry point attack в процесс, например: "/login". Может быть пустым.  **{Status}**: статус attack, например: "Exploited"  **{Timestamp}**: время, когда произошла attack.  **{VulnerabilityName}**: имя связанной code-level vulnerability, например: "InMemoryDatabaseCaller.getAccountInfo():51". Может быть пустым. | Required |

##### Объект `WebhookConfigurationHeader`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Скрытое значение HTTP-заголовка `secret` | boolean | - | Required |
| Значение `value` | text | Значение HTTP-заголовка. Может быть пустым. | Required |
| Значение `secretValue` | secret | Секретное значение HTTP-заголовка. Может быть пустым. | Required |