# -*- coding: utf-8 -*-
"""L4-AG.1a.15b builder: 2 builtin notification 20-31KB (финальный builtin батч).

Состав батча:
  - builtin-appsec-notification-integration.md (20.8KB, security notifications:
    Webhook/Jira/Email × SecurityProblemBased/AttackCandidateBased = 6 payload nested)
  - builtin-problem-notifications.md (30.8KB, 11 notification types:
    Email/Slack/Jira/AnsibleTower/OpsGenie/PagerDuty/VictorOps/WebHook/XMatters/
    Trello/ServiceNow + OAuth2 + WebHookNotificationHeader)

Канон L4-AG.1a.14c сохранён (chr() для triple-mojibake, _normalize чистит
mojibake-BOM, empty-label rows разрешены).

Mojibake-аудит EN:
  - mojibake-BOM `i.»¿` 7 (appsec) + 10 (problem-notifications) внутри
    hyperlink-текстов, чистится `_normalize`.
  - Иных типов нет (single 0, triple 0, double-B 0, double-decoded 0).

КАНОН L4-AG.1a.15b NEW: PLACEHOLDER_GLOSSARY — глобальная подстановка
повторяющихся placeholder-описаний (substring replace). 11 nested типов
problem-notifications + 6 payload типов appsec используют идентичные
placeholder-блоки (~30 уникальных placeholders), которые повторяются
~100 раз в общей сложности. Replace ИХ на RU-эквивалент через
substring-pass ДО построчного pass'а. Длинные cells получают
частичный перевод (placeholders + intro), prefix-описание остаётся
через PARAM_DESC или EN (если короткий и не критичен).

Lesson L4-AG.1a.7 lesson 2 сохранён: ключи без BOMJ (mojibake-BOM
съедается до пасса).
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-appsec-notification-integration.md",
    "builtin-problem-notifications.md",
]

DISPLAY_NAME = {
    "Security notifications": "Security notifications",
    "Problem notifications": "Problem notifications",
}

SCHEMA_DESC = {
    # appsec-notification-integration: 2 параграфа
    "Integrate security notifications with your existing incident-management system or team-collaboration channel. Within security integrations, use vulnerability and attack alerting profiles to filter the total number of alerts down to those relevant for your team.": "Интегрируйте security notifications с существующей системой incident-management или с командным каналом совместной работы. Внутри security integrations используйте alerting profiles для vulnerability и attack, чтобы отфильтровать общий поток alerts до тех, что релевантны вашей команде.",
    "To learn more, visit [Security notifications](https://dt-url.net/ly039s4).": "Подробнее см. [Security notifications](https://dt-url.net/ly039s4).",
    # problem-notifications: 2 параграфа
    "Integrate Dynatrace problem notifications with your organization's existing incident-management system or team-collaboration channel. Alerting profiles are used within problem integrations to filter the total number of alerts to a subset that is relevant for your team.": "Интегрируйте problem notifications Dynatrace с существующей системой incident-management или с командным каналом совместной работы. Внутри problem integrations используются alerting profiles, чтобы отфильтровать общий поток alerts до подмножества, релевантного вашей команде.",
    "For details see [Third-party integrations](https://dt-url.net/j803tgc).": "Подробнее см. [Third-party integrations](https://dt-url.net/j803tgc).",
}

# Глобальный pass: substring замены для intro-фраз и placeholder-блоков.
# Применяется ко всему тексту ДО построчного парсинга.
GLOBAL_PHRASES = [
    # Intro
    (
        "This is the content your notification message will include when users view it.",
        "Содержимое сообщения уведомления при его просмотре пользователями.",
    ),
    (
        "In case a value of a security problem is not set, the placeholder will be replaced by an empty string.",
        "Если значение security problem не задано, placeholder заменяется пустой строкой.",
    ),
    (
        "In case a value of an attack is not set, the placeholder will be replaced by an empty string.",
        "Если значение attack не задано, placeholder заменяется пустой строкой.",
    ),
    (
        "**Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the custom payload might leak information to untrusted parties.",
        "**Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в custom payload может привести к утечке информации к недоверенным сторонам.",
    ),
    (
        "**Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the description might leak information to untrusted parties.",
        "**Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в description может привести к утечке информации к недоверенным сторонам.",
    ),
    (
        "**Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the body might leak information to untrusted parties.",
        "**Note:** Security notifications содержат чувствительную информацию. Избыточное использование placeholders в body может привести к утечке информации к недоверенным сторонам.",
    ),
    ("Available placeholders:", "Доступные placeholders:"),
    ("Type '{' for placeholder suggestions.", "Введите '{' для подсказок placeholder."),
    ("The subject of the email notifications.", "Тема email-уведомлений."),
    ("The template of the email notifications.", "Шаблон email-уведомлений."),
    ("The content of the message.", "Содержимое сообщения."),
    ("The content of the notification message.", "Содержимое сообщения уведомления."),
    (
        "**Note:** The Jira summary field must contain less than 255 characters. Any content exceeding this limit after evaluating the placeholders will be discarded.",
        "**Note:** поле Jira summary должно содержать менее 255 символов. Любой контент сверх этого лимита после раскрытия placeholders отбрасывается.",
    ),
    (
        "The summary of the Jira issue to be created by this notification.",
        "Summary Jira issue, создаваемого этим уведомлением.",
    ),
    (
        "The description of the Jira issue to be created by this notification.",
        "Description Jira issue, создаваемого этим уведомлением.",
    ),
    # ServiceNow
    (
        "The content of the ServiceNow description.",
        "Содержимое ServiceNow description.",
    ),
    # AnsibleTower
    (
        "This message will be displayed in the Extra Variables **Message** field of your job template.",
        "Это сообщение будет отображаться в поле Extra Variables **Message** вашего job template.",
    ),
    # Trello
    (
        "The card text and problem placeholders to appear on new problem cards.",
        "Текст карточки и placeholders problem, появляющиеся на новых problem cards.",
    ),
    ("The description of the Trello card.", "Description Trello card."),
    # security placeholders
    (
        '**{SecurityProblemId}**: The unique identifier assigned by Dynatrace, for example, "S-1234".',
        '**{SecurityProblemId}**: уникальный идентификатор, назначаемый Dynatrace, например, "S-1234".',
    ),
    (
        '**{Title}**: A short summary of the type of vulnerability that was found, for example, "Remote Code Execution".',
        '**{Title}**: краткое описание типа найденной vulnerability, например, "Remote Code Execution".',
    ),
    (
        "**{Description}**: A more detailed description of the vulnerability.",
        "**{Description}**: более детальное описание vulnerability.",
    ),
    (
        '**{CvssScore}**: CVSS score of the identified vulnerability, for example, "10.0". Can be empty.',
        '**{CvssScore}**: CVSS score найденной vulnerability, например, "10.0". Может быть пустым.',
    ),
    (
        '**{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/) is an enhanced risk-calculation score based on the CVSS, for example, "10.0".',
        '**{DavisSecurityScore}**: [Davis Security Score](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/), это улучшенный risk-calculation score на основе CVSS, например, "10.0".',
    ),
    (
        '**{Severity}**: The security problem severity, for example, "Critical" or "Medium".',
        '**{Severity}**: severity security problem, например, "Critical" или "Medium".',
    ),
    (
        "**{SecurityProblemUrl}**: URL of the security problem in Dynatrace.",
        "**{SecurityProblemUrl}**: URL security problem в Dynatrace.",
    ),
    (
        "**{AffectedEntities}**: Details about the entities affected by the security problem in a json array.",
        "**{AffectedEntities}**: данные об entities, затронутых security problem, в виде json-массива.",
    ),
    (
        "**{ManagementZones}**: Comma-separated list of all management zones affected by the vulnerability at the time of detection.",
        "**{ManagementZones}**: разделённый запятыми список всех management zones, затронутых vulnerability на момент обнаружения.",
    ),
    (
        '**{Tags}**: Comma-separated list of tags that are defined for a vulnerability\'s affected entities. For example: "PROD, owner:John". Assign the tag\'s key in square brackets: **{Tags[key]}** to get all associated values. For example: "{Tags[owner]}" will be resolved as "John". Tags without an assigned value will be resolved as empty string.',
        '**{Tags}**: разделённый запятыми список tags, заданных для entities, затронутых vulnerability. Например: "PROD, owner:John". Укажите ключ tag в квадратных скобках: **{Tags[key]}**, чтобы получить все связанные значения. Например: "{Tags[owner]}" будет преобразовано в "John". Tags без значения преобразуются в пустую строку.',
    ),
    (
        '**{Exposed}**: Describes whether one or more affected process is exposed to the public Internet. Can be "true" or "false".',
        '**{Exposed}**: описывает, открыт ли один или несколько затронутых процессов в публичный Интернет. Может быть "true" или "false".',
    ),
    (
        '**{DataAssetsReachable}**: Describes whether one or more affected process can reach data assets. Can be "true" or "false".',
        '**{DataAssetsReachable}**: описывает, может ли один или несколько затронутых процессов достичь data assets. Может быть "true" или "false".',
    ),
    (
        '**{ExploitAvailable}**: Describes whether there\'s an exploit available for the vulnerability. Can be "true" or "false".',
        '**{ExploitAvailable}**: описывает, существует ли exploit для этой vulnerability. Может быть "true" или "false".',
    ),
    # attack placeholders
    (
        '**{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example: "A-1234".',
        '**{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например: "A-1234".',
    ),
    (
        '**{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example, "A-1234".',
        '**{AttackDisplayId}**: уникальный идентификатор, назначаемый Dynatrace, например, "A-1234".',
    ),
    (
        '**{Title}**: Location of the attack, for example: "com.dynatrace.Class.method():120"',
        '**{Title}**: место расположения attack, например: "com.dynatrace.Class.method():120"',
    ),
    (
        '**{Type}**: The type of attack, for example: "SQL Injection".',
        '**{Type}**: тип attack, например: "SQL Injection".',
    ),
    (
        "**{AttackUrl}**: URL of the attack in Dynatrace.",
        "**{AttackUrl}**: URL attack в Dynatrace.",
    ),
    (
        "**{ProcessGroupId}**: Details about the process group attacked.",
        "**{ProcessGroupId}**: данные об атакованной process group.",
    ),
    (
        '**{EntryPoint}**: The entry point of the attack into the process, for example: "/login". Can be empty.',
        '**{EntryPoint}**: entry point attack в процесс, например: "/login". Может быть пустым.',
    ),
    (
        '**{Status}**: The status of the attack, for example: "Exploited"',
        '**{Status}**: статус attack, например: "Exploited"',
    ),
    (
        "**{Timestamp}**: When the attack happened.",
        "**{Timestamp}**: время, когда произошла attack.",
    ),
    (
        '**{VulnerabilityName}**: Name of the associated code-level vulnerability, for example: "InMemoryDatabaseCaller.getAccountInfo():51". Can be empty.',
        '**{VulnerabilityName}**: имя связанной code-level vulnerability, например: "InMemoryDatabaseCaller.getAccountInfo():51". Может быть пустым.',
    ),
    # problem placeholders (problem-notifications)
    (
        "**{ImpactedEntities}**: Details about the entities impacted by the problem in form of a json array.",
        "**{ImpactedEntities}**: данные об entities, на которые повлиял problem, в виде json-массива.",
    ),
    (
        "**{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).",
        "**{ImpactedEntity}**: краткое описание problem и затронутой entity (или нескольких entities).",
    ),
    (
        "**{ImpactedEntityNames}**: The entity impacted by the problem.",
        "**{ImpactedEntityNames}**: entity, на которую повлиял problem.",
    ),
    (
        "**{ImpactedEntityNames}**: The entity impacted by the problem (or multiple impacted entities).",
        "**{ImpactedEntityNames}**: entity, на которую повлиял problem (или несколько затронутых entities).",
    ),
    (
        "**{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.",
        "**{NamesOfImpactedEntities}**: имена всех entities, на которые повлиял problem.",
    ),
    (
        "**{PID}**: Unique system identifier of the reported problem.",
        "**{PID}**: уникальный системный идентификатор зафиксированного problem.",
    ),
    (
        "**{ProblemDetailsHTML}**: All problem event details including root cause as an HTML-formatted string.",
        "**{ProblemDetailsHTML}**: все детали problem event, включая root cause, как HTML-форматированная строка.",
    ),
    (
        "**{ProblemDetailsJSONv2}**: Problem as json object following the structure from the [Dynatrace Problems V2 API](https://dt-url.net/7a03ti2). The optional fields evidenceDetails and impactAnalysis are included, but recentComments is not.",
        "**{ProblemDetailsJSONv2}**: problem как json-объект, следующий структуре [Dynatrace Problems V2 API](https://dt-url.net/7a03ti2). Опциональные поля evidenceDetails и impactAnalysis включены, recentComments не входит.",
    ),
    (
        "**{ProblemDetailsJSON}**: Problem as json object following the structure from the [Dynatrace Problems V1 API](https://dt-url.net/qn23tk2).",
        "**{ProblemDetailsJSON}**: problem как json-объект, следующий структуре [Dynatrace Problems V1 API](https://dt-url.net/qn23tk2).",
    ),
    (
        "**{ProblemDetailsMarkdown}**: All problem event details including root cause as a Markdown-formatted string.",
        "**{ProblemDetailsMarkdown}**: все детали problem event, включая root cause, как Markdown-форматированная строка.",
    ),
    (
        "**{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.",
        "**{ProblemDetailsText}**: все детали problem event, включая root cause, как текстово-форматированная строка.",
    ),
    (
        "**{ProblemID}**: Display number of the reported problem.",
        "**{ProblemID}**: отображаемый номер зафиксированного problem.",
    ),
    (
        "**{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.",
        "**{ProblemImpact}**: уровень impact problem. Возможные значения: APPLICATION, SERVICE или INFRASTRUCTURE.",
    ),
    (
        "**{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\\_CONTENTION, or CUSTOM\\_ALERT.",
        "**{ProblemSeverity}**: уровень severity problem. Возможные значения: AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\\_CONTENTION или CUSTOM\\_ALERT.",
    ),
    (
        "**{ProblemTitle}**: Short description of the problem.",
        "**{ProblemTitle}**: краткое описание problem.",
    ),
    (
        "**{ProblemURL}**: URL of the problem within Dynatrace.",
        "**{ProblemURL}**: URL problem в Dynatrace.",
    ),
    (
        "**{State}**: Problem state. Possible values are OPEN or RESOLVED.",
        "**{State}**: состояние problem. Возможные значения: OPEN или RESOLVED.",
    ),
    (
        "**{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist.",
        "**{Tags}**: разделённый запятыми список tags, заданных для всех затронутых entities. Чтобы обратиться к значению конкретного tag, укажите ключ tag в квадратных скобках: **{Tags[key]}**. Если у tag нет значения, placeholder заменяется пустой строкой. Если ключа tag не существует, placeholder не заменяется.",
    ),
]

PARAM_LABEL = {
    # common
    "Enabled": "Включено",
    "Display name": "Отображаемое имя",
    "Description": "Описание",
    "Name": "Имя",
    "Value": "Значение",
    "Username": "Имя пользователя",
    "Password": "Пароль",
    "URL": "URL",
    "Subject": "Тема",
    "Body": "Тело",
    "Summary": "Summary",
    "Message": "Сообщение",
    "Channel": "Канал",
    "Account": "Account",
    "Type": "Тип",
    "To": "Кому",
    "CC": "CC",
    "BCC": "BCC",
    # appsec
    "Security alert type": "Тип security alert",
    "Notification type": "Тип notification",
    "Webhook endpoint URL": "URL webhook endpoint",
    "Accept any SSL certificate (including self-signed and invalid certificates)": "Принимать любой SSL-сертификат (включая self-signed и невалидные)",
    "Additional HTTP headers": "Дополнительные HTTP-заголовки",
    "Custom payload": "Custom payload",
    "Jira endpoint URL": "URL Jira endpoint",
    "API token": "API token",
    "Project key": "Project key",
    "Issue type": "Тип issue",
    "Issue description": "Описание issue",
    "Secret HTTP header value": "Скрытое значение HTTP-заголовка",
    "Alerting profile": "Alerting profile",
    # problem-notifications specific
    "Send email if problem is closed": "Слать email при закрытии problem",
    "OpsGenie API key": "API-ключ OpsGenie",
    "OpsGenie region domain": "Региональный домен OpsGenie",
    "Service name": "Имя service",
    "Service key": "Service key",
    "API key": "API-ключ",
    "Routing key": "Routing key",
    "Secret webhook URL": "Секретный webhook URL",
    "Webhook URL": "Webhook URL",
    "Call webhook if new events merge into existing problems": "Вызывать webhook при merge новых events в существующие problems",
    "Call webhook if problem is closed": "Вызывать webhook при закрытии problem",
    "Use OAuth 2.0 for authentication": "Использовать OAuth 2.0 для аутентификации",
    "OAuth 2.0 credentials": "OAuth 2.0 credentials",
    "xMatters URL": "xMatters URL",
    "Trello application key": "Application key Trello",
    "Trello authorization token": "Authorization token Trello",
    "Trello board ID problem cards should be assigned to": "ID доски Trello, к которой привязываются problem cards",
    "Trello list ID new problem cards should be assigned to": "ID списка Trello, к которому привязываются новые problem cards",
    "Trello list ID resolved problem cards should be assigned to": "ID списка Trello, к которому привязываются resolved problem cards",
    "Card text": "Текст карточки",
    "Card description": "Описание карточки",
    "ServiceNow instance identifier": "Идентификатор инстанса ServiceNow",
    "OnPremise URL": "OnPremise URL",
    "Send incidents into ServiceNow ITSM.": "Слать incidents в ServiceNow ITSM.",
    "Send events into ServiceNow ITOM.": "Слать events в ServiceNow ITOM.",
    "Use text format for problem details instead of HTML.": "Использовать text-формат для problem details вместо HTML.",
    "Access token URL": "URL access token",
    "Client ID": "Client ID",
    "Client secret": "Client secret",
    "Scope": "Scope",
    'Include the client credentials in the HTTP "Authorization" request header field with the HTTP "Basic" authentication scheme.': 'Включить client credentials в HTTP-заголовок "Authorization" по схеме HTTP "Basic".',
    "Custom message (optional)": "Custom-сообщение (необязательно)",
    "Job template URL": "URL job template",
}

PARAM_DESC = {
    # appsec short
    "Select an alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-alerting-profile`) to control the delivery of security notifications related to this integration.": "Выберите alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-alerting-profile`), чтобы управлять доставкой security notifications, связанных с этой integration.",
    "Select an alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-attack-alerting-profile`) to control the delivery of security notifications related to this integration.": "Выберите alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-attack-alerting-profile`), чтобы управлять доставкой security notifications, связанных с этой integration.",
    "Use additional HTTP headers to attach any additional information, for example, configuration, authorization, or metadata.  Note that JSON-based webhook endpoints require the addition of the **Content-Type: application/json** header to enable escaping of special characters and to avoid malformed JSON content.": "Используйте дополнительные HTTP-заголовки для передачи любой дополнительной информации: configuration, authorization, metadata. JSON-based webhook endpoints требуют заголовка **Content-Type: application/json** для escaping специальных символов и предотвращения malformed JSON-контента.",
    "The URL of the Jira API endpoint.": "URL endpoint Jira API.",
    "The username of the Jira profile.": "Имя пользователя Jira profile.",
    "The API token for the Jira profile. Using password authentication [was deprecated by Jira](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-basic-auth-and-cookie-based-auth/)": "API token для Jira profile. Password-аутентификация [была deprecated в Jira](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-basic-auth-and-cookie-based-auth/)",
    "The project key of the Jira issue to be created by this notification.": "Project key Jira issue, создаваемого этим уведомлением.",
    "The type of the Jira issue to be created by this notification.  To find all available issue types or create your own, in Jira, go to Project settings > Issue types.": "Тип Jira issue, создаваемого этим уведомлением. Чтобы найти все доступные типы issue или создать свой, в Jira перейдите в Project settings > Issue types.",
    "The type of the Jira issue to be created by this notification.  To find all available issue types, or to create your own issue type, within JIRA go to Options > Issues.": "Тип Jira issue, создаваемого этим уведомлением. Чтобы найти все доступные типы issue или создать свой, в JIRA перейдите в Options > Issues.",
    "The value of the HTTP header.": "Значение HTTP-заголовка.",
    "The value of the HTTP header. May contain an empty value.": "Значение HTTP-заголовка. Может быть пустым.",
    "The secret value of the HTTP header. May contain an empty value.": "Секретное значение HTTP-заголовка. Может быть пустым.",
    # problem-notifications
    "The name of the notification configuration.": "Имя notification configuration.",
    "Select an alerting profile (`<your-dynatrace-url>//ui/settings/builtin:alerting.profile`) to control the delivery of problem notifications related to this integration.": "Выберите alerting profile (`<your-dynatrace-url>//ui/settings/builtin:alerting.profile`), чтобы управлять доставкой problem notifications, связанных с этой integration.",
    "Set up an incoming WebHook integration within your Slack account. Copy and paste the generated WebHook URL into the field above.": "Настройте incoming WebHook integration в вашем Slack account. Скопируйте и вставьте сгенерированный WebHook URL в поле выше.",
    "The channel (for example, `#general`) or the user (for example, `@john.smith`) to send the message to.": "Канал (например, `#general`) или пользователь (например, `@john.smith`), которому отправляется сообщение.",
    "The URL of the webhook endpoint.": "URL endpoint webhook.",
    "The secret URL of the webhook endpoint.": "Секретный URL endpoint webhook.",
    "The URL of the xMatters webhook.": "URL webhook xMatters.",
    "A list of the additional HTTP headers.": "Список дополнительных HTTP-заголовков.",
    "The name of the HTTP header.": "Имя HTTP-заголовка.",
    "The API key to access OpsGenie.  Go to OpsGenie-Integrations and create a new Dynatrace integration. Copy the newly created API key.": "API-ключ для доступа к OpsGenie. Перейдите в OpsGenie-Integrations и создайте новую Dynatrace integration. Скопируйте созданный API-ключ.",
    "The region domain of the OpsGenie.  For example, **api.opsgenie.com** for US or **api.eu.opsgenie.com** for EU.": "Региональный домен OpsGenie. Например, **api.opsgenie.com** для US или **api.eu.opsgenie.com** для EU.",
    "The name of the PagerDuty account.": "Имя PagerDuty account.",
    "The name of the service.": "Имя service.",
    "The Events API key to access PagerDuty.": "Events API-ключ для доступа к PagerDuty.",
    "The API key for the target Splunk On-Call account.  Receive your Splunk On-Call API key by navigating to: Settings -> Integrations -> Rest Endpoint -> Dynatrace.": "API-ключ для целевого Splunk On-Call account. Получите API-ключ Splunk On-Call здесь: Settings -> Integrations -> Rest Endpoint -> Dynatrace.",
    "The routing key, defining the group to be notified.": "Routing key, определяющий группу для уведомления.",
    "The application key for the Trello account.  You must be logged into Trello to have Trello automatically generate an application key for you. [Get application key](https://trello.com/app-key)": "Application key для Trello account. Вы должны быть залогинены в Trello, чтобы Trello автоматически сгенерировал application key. [Получить application key](https://trello.com/app-key)",
    "The authorization token for the Trello account.": "Authorization token для Trello account.",
    "The ServiceNow instance identifier. It refers to the first part of your own ServiceNow URL.  This field is mutually exclusive with the **url** field. You can only use one of them.": "Идентификатор инстанса ServiceNow. Это первая часть вашего ServiceNow URL. Поле взаимоисключающее с полем **url**: допустимо использовать только одно из них.",
    "The URL of the on-premise ServiceNow installation.  This field is mutually exclusive with the **instanceName** field. You can only use one of them.": "URL on-premise ServiceNow installation. Поле взаимоисключающее с полем **instanceName**: допустимо использовать только одно из них.",
    "The username of the ServiceNow account.  Make sure that your user account has the `web_service_admin` and `x_dynat_ruxit.Integration` roles.": "Имя пользователя ServiceNow account. Убедитесь, что у пользователя есть роли `web_service_admin` и `x_dynat_ruxit.Integration`.",
    "The password to the ServiceNow account.": "Пароль ServiceNow account.",
    "Account username.": "Имя пользователя account.",
    "Account password.": "Пароль account.",
    "The URL of the target job template.  For example, https:///#/templates/job\\_template/  **Note:** Be sure to select the **Prompt on Launch** option in the Extra Variables section of your job template configuration.": "URL целевого job template. Например, https:///#/templates/job\\_template/ **Note:** обязательно выберите опцию **Prompt on Launch** в секции Extra Variables конфигурации job template.",
    "The scope of access you are requesting": "Запрашиваемый scope доступа",
    "If false, the client credentials are included in the HTTP request body.": "Если false, client credentials включаются в тело HTTP-запроса.",
    "To authenticate your integration, the OAuth 2.0 *Client Credentials* Flow (Grant Type) is used. For details see [Client Credentials Flow](https://dt-url.net/ym22wsm)).  The obtained Access Token is subsequently provided in the *Authorization* header of the request carrying the notification payload.": "Для аутентификации integration используется OAuth 2.0 *Client Credentials* Flow (Grant Type). Подробнее см. [Client Credentials Flow](https://dt-url.net/ym22wsm)). Полученный Access Token передаётся в заголовке *Authorization* запроса, переносящего payload уведомления.",
}

STRUCT = [
    ("* Published Dec 05, 2023", "* Опубликовано 5 декабря 2023"),
    ("| Schema ID | Schema groups | Scope |", "| Schema ID | Группы схемы | Scope |"),
    ("Retrieve schema via Settings API", "Получить schema через Settings API"),
    ("## Authentication", "## Аутентификация"),
    ("## Parameters", "## Параметры"),
    (
        "To execute this request, you need an access token with **Read settings** "
        "(`settings.read`) scope. To learn how to obtain and use it, see "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Для выполнения запроса необходим access token со scope **Read settings** "
        "(`settings.read`). О том, как получить и использовать токен, см. "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "| Property | Type | Description | Required |",
        "| Свойство | Тип | Описание | Обязательный |",
    ),
]

ENUM_PHRASE = ("The element has these enums", "Возможные значения:")


def _normalize(t):
    t = t.replace("\r\n", "\n")
    t = t.replace(chr(0xFEFF), "")
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")
    return t


def _heading(line):
    marker = " (`builtin:"
    i = line.find(marker)
    if not line.startswith("### ") or i == -1:
        return None
    name = line[4:i]
    tail = line[i:]
    ru = DISPLAY_NAME.get(name)
    if ru is None:
        return None
    return "### " + ru + tail


def _param_row(line):
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 4:
        return None
    c0, ctype, cdesc, creq = cells
    if "`" not in c0:
        return None
    bt = c0.find("`")
    label = c0[:bt].rstrip()
    code = c0[bt:]
    sep = c0[len(label) : bt]
    if label and label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL.get(label, label)
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    marker_len = len(ENUM_PHRASE[0])
    if ei == -1:
        ei = d.find(ENUM_PHRASE[1])
        marker_len = len(ENUM_PHRASE[1])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + marker_len :]
        if head == "" or head == "-":
            new_desc = ENUM_PHRASE[1] + enum_tail
        else:
            head_ru = PARAM_DESC.get(head, head)
            new_desc = head_ru + " " + ENUM_PHRASE[1] + enum_tail
    else:
        new_desc = "-" if d == "-" else PARAM_DESC.get(d, d)
    return (
        "| "
        + new_label
        + sep
        + code
        + " | "
        + ctype
        + " | "
        + new_desc
        + " | "
        + creq
        + " |"
    )


NESTED_HEADING_RE = _re.compile(r"^##### The (`[^`]+`) object$")


def _nested_heading(line):
    m = NESTED_HEADING_RE.match(line)
    if not m:
        return None
    return "##### Объект " + m.group(1)


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    # GLOBAL substring replace pass (placeholders + intro phrases)
    for en, ru in GLOBAL_PHRASES:
        t = t.replace(en, ru)
    for en, ru in SCHEMA_DESC.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    t = t.replace(ENUM_PHRASE[0], ENUM_PHRASE[1])
    out = []
    for line in t.split("\n"):
        nl = _heading(line) or _nested_heading(line) or _param_row(line)
        out.append(nl if nl is not None else line)
    t = "\n".join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return src, dst


if __name__ == "__main__":
    bad = 0
    for rel in PILOT:
        src, dst = build(rel)
        en_n = (
            io.open(src, "r", encoding="utf-8", newline="")
            .read()
            .replace("\r\n", "\n")
            .count("\n")
        )
        ru_n = io.open(dst, "r", encoding="utf-8", newline="").read().count("\n")
        flag = "" if en_n == ru_n else "  <<< PARITY MISMATCH"
        if flag:
            bad += 1
        print("%-66s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY MISMATCH:", bad)
