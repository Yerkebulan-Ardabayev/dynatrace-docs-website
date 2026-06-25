#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splice-builder for batch L4W: configuration-api/rum/web-application-
configuration-api/ DEFER-completion = default-application/ (2: get/put-
configuration) + web-application/ (5: del / get-all / get / post / put) = 7
files. Closes web-application-configuration-api/ entirely (L4V did parent +
data-privacy/5 + error-rules/2 + key-user-actions/3).

ACTIVE API, no deprecated banner (L89/L90; `* Reference` / `* Published Sep 03,
2019` / `* Updated on Aug 18, 2025` for post — no `* Deprecated`). EN -> RU
exact-string replacement only (no newline added/removed) => line-parity
automatic, code-fence byte-identical (L98/L100). EN is CRLF for del-web-
application => normalize LF first (L4M), strip leading BOM.

Twin structure (L85/L86): the `WebApplicationConfig` object + ~40 sub-objects +
JSON model (~lines 47-1392) is byte-identical across get-web-application /
default-application/get-configuration (GET-twins) and post-web-application /
put-web-application / default-application/put-configuration (POST/PUT-twins) =>
translate the giant object ONCE in COMMON, splice into all 5.

Canon anchor = FRESHEST same-subsection twin = L4V web-application-
configuration-api RU (error-rules/get-configuration, key-user-actions/del-
configuration, parent combined-block card) + L4U mobile-custom-app shared-
object canon (Error/ErrorEnvelope/ConstraintViolation/EntityShortRepresentation
/StubList verbatim). L103 case (b): env-api/rum has NO web-application twin.

Domain corpus-dominance (verified against managed-ru/):
  "web application"   -> "веб-приложение" (73+44x, parent RU confirms)
  "user action"       -> "пользовательское действие" (L4U 619x)
  "user session"      -> "пользовательская сессия" (L4U)
  "conversion goal"   -> "цель конверсии" (corpus "целей конверсии")
  "Real user monitoring settings." -> "Настройки мониторинга реальных
                          пользователей." (L4T rum-overview H1 anchor)
  "Session Replay"    -> EN (51x dominant; lowercase "session replay" prose
                          -> "Session Replay" too, L4U lock)
  "Apdex" / "Davis AI" -> EN (CLAUDE.md tech-term; error-rules L4V RU)
  "beacon" / "CORS"   -> EN-lock (L4S/L4U)
  "JavaScript"        -> "JavaScript" EN, agent -> "JavaScript-агент"
  "regular expression"-> "регулярное выражение" (10x, L4U)
  "request attribute" -> "атрибут запроса" (L4U 54x)
  "IP address"        -> "IP-адрес" (95x)
  "placeholder"       -> "плейсхолдер" (9x vs 0; field/code stays EN)
  "X enabled/disabled."-> "X включён/отключён." (gender-agree by subject;
                          corpus boolean canon "включён (`true`)" 61x)
  `**field**` bold spans + enum values in backticks = EN-lock (style-guide
  UI + L99, L4S SUSPECT exclusion). title + H1x2 + `* Reference` /
  `* Published` / `* Updated on` = EN-verbatim (L99).
L101: 400 `Failed. The input is invalid.` source = WITH period (post/put/
default-put validate) => substring `Failed. The input is invalid` (period
outside span, preserved, L4S). validate-204 EN "Validated. The submitted
configuration is valid. Response does not have a body." -> "Validated."-prefix
(EN-prefix L4I, by EN cell). Related-topics link-text = target RU H1 verbatim
(L4O/L4L: del-web-application -> "Удаление веб-приложения" target translated).
Source-quirks L93 verbatim-by-meaning: "Analize" (typo), "noting specified"
(typo), "applicationâs"/"serverâs" (mojibake apostrophe -> render meaning),
"MATCHES_REGULAR_ERPRESSION" (typo in operand2 prose).
BOM 3-char `\xef\xbb\xbf` (L4M) in `[regular expression]` cleanupRule cell
stripped.
"""

import os, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
SUB = r"docs\managed\dynatrace-api\configuration-api\rum\web-application-configuration-api"
SUBR = r"docs\managed-ru\dynatrace-api\configuration-api\rum\web-application-configuration-api"
EN = os.path.join(ROOT, SUB)
RU = os.path.join(ROOT, SUBR)

FILES = [
    "default-application/get-configuration.md",
    "default-application/put-configuration.md",
    "web-application/del-web-application.md",
    "web-application/get-all.md",
    "web-application/get-web-application.md",
    "web-application/post-web-application.md",
    "web-application/put-web-application.md",
]

# ---------------------------------------------------------------- COMMON
# Applied AFTER per-file. Ordered longest/most-specific first to avoid
# substring-collision RU+EN hybrids (L4N/L4P/L4T lesson).
COMMON = [
    # --- structural headers (`## Validate payload` / `#### Curl` stay EN
    #     per L99 ALLOWED_EN, L4S) ---
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n#### Response body objects\n", "\n#### Объекты тела ответа\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n#### Response body JSON models\n", "\n#### JSON-модели тела ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n#### Response codes\n", "\n#### Коды ответа\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response\n", "\n### Ответ\n"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # --- table headers ---
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    ("| Code | Description |", "| Код | Описание |"),
    # --- object headers (`#### The \`X\` object` -> `#### Объект \`X\``) ---
    (
        "#### The `WebApplicationConfigBrowserRestrictionSettings` object",
        "#### Объект `WebApplicationConfigBrowserRestrictionSettings`",
    ),
    (
        "#### The `WebApplicationConfigBrowserRestriction` object",
        "#### Объект `WebApplicationConfigBrowserRestriction`",
    ),
    (
        "#### The `WebApplicationConfigIpAddressRestrictionSettings` object",
        "#### Объект `WebApplicationConfigIpAddressRestrictionSettings`",
    ),
    (
        "#### The `UserActionNamingPlaceholderProcessingStep` object",
        "#### Объект `UserActionNamingPlaceholderProcessingStep`",
    ),
    (
        "#### The `UserActionNamingRuleCondition` object",
        "#### Объект `UserActionNamingRuleCondition`",
    ),
    (
        "#### The `UserActionNamingPlaceholder` object",
        "#### Объект `UserActionNamingPlaceholder`",
    ),
    (
        "#### The `UserActionAndSessionProperties` object",
        "#### Объект `UserActionAndSessionProperties`",
    ),
    (
        "#### The `UserActionNamingSettings` object",
        "#### Объект `UserActionNamingSettings`",
    ),
    (
        "#### The `UserActionNamingRule` object",
        "#### Объект `UserActionNamingRule`",
    ),
    (
        "#### The `AdvancedJavaScriptTagSettings` object",
        "#### Объект `AdvancedJavaScriptTagSettings`",
    ),
    (
        "#### The `GlobalEventCaptureSettings` object",
        "#### Объект `GlobalEventCaptureSettings`",
    ),
    (
        "#### The `JavaScriptFrameworkSupport` object",
        "#### Объект `JavaScriptFrameworkSupport`",
    ),
    (
        "#### The `JavaScriptInjectionRules` object",
        "#### Объект `JavaScriptInjectionRules`",
    ),
    (
        "#### The `AdditionalEventHandlers` object",
        "#### Объект `AdditionalEventHandlers`",
    ),
    (
        "#### The `VisuallyComplete2Settings` object",
        "#### Объект `VisuallyComplete2Settings`",
    ),
    (
        "#### The `ResourceTimingSettings` object",
        "#### Объект `ResourceTimingSettings`",
    ),
    (
        "#### The `EventWrapperSettings` object",
        "#### Объект `EventWrapperSettings`",
    ),
    (
        "#### The `SessionReplaySetting` object",
        "#### Объект `SessionReplaySetting`",
    ),
    (
        "#### The `ConfigurationMetadata` object",
        "#### Объект `ConfigurationMetadata`",
    ),
    (
        "#### The `VisitDurationDetails` object",
        "#### Объект `VisitDurationDetails`",
    ),
    (
        "#### The `VisitNumActionDetails` object",
        "#### Объект `VisitNumActionDetails`",
    ),
    (
        "#### The `DestinationDetails` object",
        "#### Объект `DestinationDetails`",
    ),
    (
        "#### The `UserActionDetails` object",
        "#### Объект `UserActionDetails`",
    ),
    (
        "#### The `MonitoringSettings` object",
        "#### Объект `MonitoringSettings`",
    ),
    (
        "#### The `MetaDataCapturing` object",
        "#### Объект `MetaDataCapturing`",
    ),
    ("#### The `WebApplicationConfig` object", "#### Объект `WebApplicationConfig`"),
    ("#### The `ContentCapture` object", "#### Объект `ContentCapture`"),
    ("#### The `TimeoutSettings` object", "#### Объект `TimeoutSettings`"),
    ("#### The `ConversionGoal` object", "#### Объект `ConversionGoal`"),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `IpAddressRange` object", "#### Объект `IpAddressRange`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    ("#### The `UserTag` object", "#### Объект `UserTag`"),
    ("#### The `Apdex` object", "#### Объект `Apdex`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    # --- shared boilerplate prose (L4U/L4V canon) ---
    (
        "To execute this request, you need an access token with `ReadConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `ReadConfig`.",
    ),
    (
        "To execute this request, you need an access token with `WriteConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `WriteConfig`.",
    ),
    (
        "To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "The request doesn't provide any configurable parameters.",
        "В запросе нет настраиваемых параметров.",
    ),
    (
        "The request consumes and produces an `application/json` payload.",
        "Запрос принимает и возвращает payload `application/json`.",
    ),
    (
        "The request consumes an `application/json` payload.",
        "Запрос принимает payload `application/json`.",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает payload `application/json`.",
    ),
    (
        'This API only supports web applications. For mobile and custom applications, see [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").',
        'Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений смотрите [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace mobile и custom app config API.").',
    ),
    (
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.",
    ),
    # --- shared Error / ErrorEnvelope / ConstraintViolation /
    #     EntityShortRepresentation / StubList canon (L4U/L4V verbatim) ---
    (
        "An ordered list of short representations of Dynatrace entities.",
        "Упорядоченный список кратких представлений сущностей Dynatrace.",
    ),
    (
        "The short representation of a Dynatrace entity.",
        "Краткое представление сущности Dynatrace.",
    ),
    (
        "| description | string | A short description of the Dynatrace entity. |",
        "| description | string | Краткое описание сущности Dynatrace. |",
    ),
    (
        "| id | string | The ID of the Dynatrace entity. |",
        "| id | string | ID сущности Dynatrace. |",
    ),
    (
        "| name | string | The name of the Dynatrace entity. |",
        "| name | string | Имя сущности Dynatrace. |",
    ),
    (
        "| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | An ordered list of short representations of Dynatrace entities. |",
        "| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Упорядоченный список кратких представлений сущностей Dynatrace. |",
    ),
    (
        "| code | integer | The HTTP status code |",
        "| code | integer | HTTP-код статуса |",
    ),
    (
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |",
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |",
    ),
    (
        "| message | string | The error message |",
        "| message | string | Сообщение об ошибке |",
    ),
    ("\nA list of constraint violations\n", "\nСписок нарушений ограничений\n"),
    # ============================================================
    #  WebApplicationConfig object + ~40 sub-objects (the giant
    #  shared block; translate once -> splices into all 5 big files)
    #  longest/most-specific FIRST.
    # ============================================================
    # --- object intros ---
    (
        "Configuration to capture meta data with the Javascript agent. The captured metadata can be referenced by its uniqueId in UserTags, UserActionAndSessionProperties or UserActionNamingPlaceholder",
        "Конфигурация захвата метаданных JavaScript-агентом. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder",
    ),
    (
        "Settings for restricting certain browser type, version, platform and, comparator. It also restricts the mode.",
        "Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивают режим.",
    ),
    (
        "Settings for restricting certain ip addresses and for introducing subnet mask. It also restricts the mode.",
        "Настройки для ограничения определённых IP-адресов и для ввода маски подсети. Также ограничивают режим.",
    ),
    (
        "In addition to the event handlers, events called using `addEventListener` or `attachEvent` can be captured. Be careful with this option! Event wrappers can conflict with the JavaScript code on a web page.",
        "Помимо обработчиков событий, можно захватывать события, вызываемые через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице.",
    ),
    (
        "These settings influence the monitoring data you receive for 3rd party, CDN, and 1st party resources.",
        "Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов.",
    ),
    (
        "Browser exclusion rules for the browsers that are to be excluded.",
        "Правила исключения для браузеров, которые нужно исключить.",
    ),
    (
        "Defines userAction and session custom defined properties settings of an application.",
        "Определяет настройки пользовательски заданных свойств пользовательских действий и сессий приложения.",
    ),
    (
        "The IP address or the IP address range to be mapped to the location.",
        "IP-адрес или диапазон IP-адресов, сопоставляемый с локацией.",
    ),
    ("Configuration of a web application.", "Конфигурация веб-приложения."),
    (
        "A conversion goal of the application.",
        "Цель конверсии приложения.",
    ),
    (
        "Configuration of a destination-based conversion goal.",
        "Конфигурация цели конверсии на основе назначения.",
    ),
    (
        "Configuration of a user action-based conversion goal.",
        "Конфигурация цели конверсии на основе пользовательского действия.",
    ),
    (
        "Configuration of a visit duration-based conversion goal.",
        "Конфигурация цели конверсии на основе длительности визита.",
    ),
    (
        "Configuration of a number of user actions-based conversion goal.",
        "Конфигурация цели конверсии на основе количества пользовательских действий.",
    ),
    (
        "Defines the Apdex settings of an application.",
        "Определяет настройки Apdex приложения.",
    ),
    ("Metadata useful for debugging", "Метаданные для отладки"),
    (
        "Real user monitoring settings.",
        "Настройки мониторинга реальных пользователей.",
    ),
    (
        "Advanced JavaScript tag settings.",
        "Расширенные настройки JavaScript-тега.",
    ),
    (
        "Additional event handlers and wrappers.",
        "Дополнительные обработчики и обёртки событий.",
    ),
    (
        "Global event capture settings.",
        "Настройки глобального захвата событий.",
    ),
    ("Settings for content capture.", "Настройки захвата контента."),
    (
        "Settings for resource timings capture.",
        "Настройки захвата таймингов ресурсов.",
    ),
    ("Settings for timed action capture.", "Настройки захвата отложенных действий."),
    ("Settings for VisuallyComplete2", "Настройки VisuallyComplete2"),
    (
        "Support of various JavaScript frameworks.",
        "Поддержка различных JavaScript-фреймворков.",
    ),
    ("Rules for javascript injection", "Правила внедрения JavaScript"),
    ("Session replay settings", "Настройки Session Replay"),
    (
        "The settings of user action naming.",
        "Настройки именования пользовательских действий.",
    ),
    ("The settings of naming rule.", "Настройки правила именования."),
    (
        "The settings of conditions for user action naming.",
        "Настройки условий именования пользовательских действий.",
    ),
    ("The placeholder settings.", "Настройки плейсхолдера."),
    ("The processing step settings.", "Настройки шага обработки."),
    (
        "Defines UserTags settings of an application.",
        "Определяет настройки UserTags приложения.",
    ),
    # --- WebApplicationConfig fields ---
    (
        "| conversionGoals | [ConversionGoal[]](#openapi-definition-ConversionGoal) | A list of conversion goals of the application. |",
        "| conversionGoals | [ConversionGoal[]](#openapi-definition-ConversionGoal) | Список целей конверсии приложения. |",
    ),
    (
        "| costControlUserSessionPercentage | number | Analize *X*% of user sessions. |",
        "| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. |",
    ),
    (
        "| identifier | string | Dynatrace entity ID of the web application. |",
        "| identifier | string | ID сущности Dynatrace для веб-приложения. |",
    ),
    (
        "| loadActionKeyPerformanceMetric | string | The key performance metric of load actions. The element can hold these values",
        "| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности действий загрузки. Возможные значения:",
    ),
    (
        "| metaDataCaptureSettings | [MetaDataCapturing[]](#openapi-definition-MetaDataCapturing) | Java script agent meta data capture settings. |",
        "| metaDataCaptureSettings | [MetaDataCapturing[]](#openapi-definition-MetaDataCapturing) | Настройки захвата метаданных JavaScript-агентом. |",
    ),
    (
        "| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Real user monitoring settings. |",
        "| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки мониторинга реальных пользователей. |",
    ),
    (
        "| name | string | The name of the web application, displayed in the UI. |",
        "| name | string | Имя веб-приложения, отображаемое в UI. |",
    ),
    (
        "| realUserMonitoringEnabled | boolean | Real user monitoring enabled/disabled. |",
        "| realUserMonitoringEnabled | boolean | Мониторинг реальных пользователей включён/отключён. |",
    ),
    (
        "| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Session replay settings |",
        "| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки Session Replay |",
    ),
    (
        "| type | string | The type of the web application. The element can hold these values",
        "| type | string | Тип веб-приложения. Возможные значения:",
    ),
    (
        "| urlInjectionPattern | string | Url injection pattern for manual web application. |",
        "| urlInjectionPattern | string | Шаблон внедрения URL для ручного веб-приложения. |",
    ),
    (
        "| userActionAndSessionProperties | [UserActionAndSessionProperties[]](#openapi-definition-UserActionAndSessionProperties) | User action and session properties settings. Empty List means no change |",
        "| userActionAndSessionProperties | [UserActionAndSessionProperties[]](#openapi-definition-UserActionAndSessionProperties) | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений |",
    ),
    (
        "| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | The settings of user action naming. |",
        "| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. |",
    ),
    (
        "| userTags | [UserTag[]](#openapi-definition-UserTag) | User tags settings. |",
        "| userTags | [UserTag[]](#openapi-definition-UserTag) | Настройки пользовательских тегов. |",
    ),
    (
        "| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | These settings influence the monitoring data you receive for 3rd party, CDN, and 1st party resources. |",
        "| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов. |",
    ),
    (
        "| xhrActionKeyPerformanceMetric | string | The key performance metric of XHR actions. The element can hold these values",
        "| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности XHR-действий. Возможные значения:",
    ),
    # shared "Defines the Apdex settings of an application." cells (3x in
    # WebApplicationConfig: customActionApdexSettings/loadActionApdexSettings/
    # xhrActionApdexSettings) — handled by object-intro replace above which
    # also matches the cell text "Defines the Apdex settings of an application."
    # --- ConversionGoal fields ---
    (
        "| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Configuration of a destination-based conversion goal. |",
        "| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. |",
    ),
    (
        "| id | string | The ID of conversion goal.  Omit it while creating a new conversion goal. |",
        "| id | string | ID цели конверсии.  Не указывайте его при создании новой цели конверсии. |",
    ),
    (
        "| name | string | The name of the conversion goal. |",
        "| name | string | Имя цели конверсии. |",
    ),
    (
        "| type | string | The type of the conversion goal. The element can hold these values",
        "| type | string | Тип цели конверсии. Возможные значения:",
    ),
    (
        "| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Configuration of a user action-based conversion goal. |",
        "| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. |",
    ),
    (
        "| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Configuration of a visit duration-based conversion goal. |",
        "| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. |",
    ),
    (
        "| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Configuration of a number of user actions-based conversion goal. |",
        "| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе количества пользовательских действий. |",
    ),
    # --- DestinationDetails / UserActionDetails fields ---
    (
        "| caseSensitive | boolean | The match is case-sensitive (`true`) or (`false`). |",
        "| caseSensitive | boolean | Сопоставление чувствительно к регистру (`true`) или нет (`false`). |",
    ),
    (
        "| matchType | string | The operator of the match. The element can hold these values",
        "| matchType | string | Оператор сопоставления. Возможные значения:",
    ),
    (
        "| urlOrPath | string | The path to be reached to hit the conversion goal. |",
        "| urlOrPath | string | Путь, который нужно достичь для выполнения цели конверсии. |",
    ),
    (
        "| actionType | string | Type of the action to which the rule applies. The element can hold these values",
        "| actionType | string | Тип действия, к которому применяется правило. Возможные значения:",
    ),
    (
        "| matchEntity | string | The type of the entity to which the rule applies. The element can hold these values",
        "| matchEntity | string | Тип сущности, к которой применяется правило. Возможные значения:",
    ),
    (
        "| value | string | The value to be matched to hit the conversion goal. |",
        "| value | string | Значение для сопоставления, чтобы выполнить цель конверсии. |",
    ),
    (
        "| durationInMillis | integer | The duration of session to hit the conversion goal, in milliseconds. |",
        "| durationInMillis | integer | Длительность сессии для выполнения цели конверсии, в миллисекундах. |",
    ),
    (
        "| numUserActions | integer | The number of user actions to hit the conversion goal. |",
        "| numUserActions | integer | Количество пользовательских действий для выполнения цели конверсии. |",
    ),
    # --- Apdex fields ---
    (
        "| frustratingFallbackThreshold | number | Fallback threshold of an XHR action, defining a tolerable user experience, when the configured KPM is not available. |",
        "| frustratingFallbackThreshold | number | Резервный порог XHR-действия, определяющий приемлемый пользовательский опыт, когда настроенная KPM недоступна. |",
    ),
    (
        "| frustratingThreshold | number | Maximal value of apdex, which is considered as tolerable user experience. |",
        "| frustratingThreshold | number | Максимальное значение Apdex, которое считается приемлемым пользовательским опытом. |",
    ),
    (
        "| toleratedFallbackThreshold | number | Fallback threshold of an XHR action, defining a satisfied user experience, when the configured KPM is not available. |",
        "| toleratedFallbackThreshold | number | Резервный порог XHR-действия, определяющий удовлетворительный пользовательский опыт, когда настроенная KPM недоступна. |",
    ),
    (
        "| toleratedThreshold | number | Maximal value of apdex, which is considered as satisfied user experience. |",
        "| toleratedThreshold | number | Максимальное значение Apdex, которое считается удовлетворительным пользовательским опытом. |",
    ),
    # --- MetaDataCapturing fields ---
    (
        "| capturingName | string | The name of the meta data to capture. |",
        "| capturingName | string | Имя захватываемых метаданных. |",
    ),
    (
        "| name | string | Name for displaying the captured values in Dynatrace. |",
        "| name | string | Имя для отображения захваченных значений в Dynatrace. |",
    ),
    (
        "| publicMetadata | boolean | True if this metadata should be captured regardless of the privacy settings |",
        "| publicMetadata | boolean | True, если эти метаданные нужно захватывать независимо от настроек конфиденциальности |",
    ),
    (
        "| type | string | The type of the meta data to capture. The element can hold these values",
        "| type | string | Тип захватываемых метаданных. Возможные значения:",
    ),
    (
        "| uniqueId | integer | The unique id of the meta data to capture. |",
        "| uniqueId | integer | Уникальный id захватываемых метаданных. |",
    ),
    (
        "| useLastValue | boolean | True if the last captured value should be used for this metadata. By default the first value will be used. |",
        "| useLastValue | boolean | True, если для этих метаданных нужно использовать последнее захваченное значение. По умолчанию используется первое значение. |",
    ),
    # --- ConfigurationMetadata fields (L4M canon) ---
    (
        "| clusterVersion | string | Dynatrace version. |",
        "| clusterVersion | string | Версия Dynatrace. |",
    ),
    (
        "| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |",
        "| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |",
    ),
    (
        "| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |",
        "| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |",
    ),
    # --- MonitoringSettings fields ---
    (
        "| addCrossOriginAnonymousAttribute | boolean | Add the cross origin = anonymous attribute to capture JavaScript error messages and W3C resource timings. |",
        "| addCrossOriginAnonymousAttribute | boolean | Добавить атрибут cross origin = anonymous для захвата сообщений об ошибках JavaScript и таймингов ресурсов W3C. |",
    ),
    (
        "| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Advanced JavaScript tag settings. |",
        "| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Расширенные настройки JavaScript-тега. |",
    ),
    (
        "| angularPackageName | string | The name of the angular package. |",
        "| angularPackageName | string | Имя пакета angular. |",
    ),
    (
        "| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Settings for restricting certain browser type, version, platform and, comparator. It also restricts the mode. |",
        "| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивают режим. |",
    ),
    (
        "| cacheControlHeaderOptimizations | boolean | Optimize the value of cache control headers for use with Dynatrace real user monitoring enabled/disabled. |",
        "| cacheControlHeaderOptimizations | boolean | Оптимизация значения заголовков cache control для использования с мониторингом реальных пользователей Dynatrace включена/отключена. |",
    ),
    (
        "| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Settings for content capture. |",
        "| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки захвата контента. |",
    ),
    (
        "| cookiePlacementDomain | string | Domain for cookie placement. |",
        "| cookiePlacementDomain | string | Домен для размещения cookie. |",
    ),
    (
        "| correlationHeaderInclusionRegex | string | To enable RUM for XHR calls to AWS Lambda, define a regular expression matching these calls, Dynatrace can then automatically add a custom header (x-dtc) to each such request to the respective endpoints in AWS.  Important: These endpoints must accept the x-dtc header, or the requests will fail. |",
        "| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, задайте регулярное выражение, соответствующее этим вызовам, после чего Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим эндпоинтам в AWS.  Важно: эти эндпоинты должны принимать заголовок x-dtc, иначе запросы будут завершаться ошибкой. |",
    ),
    (
        "| customConfigurationProperties | string | Additional JavaScript tag properties that are specific to your application. To do this, type key=value pairs separated using a (|) symbol. |",
        "| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для вашего приложения. Для этого введите пары key=value, разделённые символом (|). |",
    ),
    (
        "| excludeXhrRegex | string | You can exclude some actions from becoming XHR actions.  Put a regular expression, matching all the required URLs, here.  If noting specified the feature is disabled. |",
        "| excludeXhrRegex | string | Вы можете исключить некоторые действия из числа XHR-действий.  Укажите здесь регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. |",
    ),
    (
        "| fetchRequests | boolean | `fetch()` request capture enabled/disabled. |",
        "| fetchRequests | boolean | Захват запросов `fetch()` включён/отключён. |",
    ),
    (
        "| injectionMode | string | JavaScript injection mode. The element can hold these values",
        "| injectionMode | string | Режим внедрения JavaScript. Возможные значения:",
    ),
    (
        "| instrumentedWebServer | boolean | Instrumented web or app server. |",
        "| instrumentedWebServer | boolean | Инструментированный веб-сервер или сервер приложений. |",
    ),
    (
        "| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Settings for restricting certain ip addresses and for introducing subnet mask. It also restricts the mode. |",
        "| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки для ограничения определённых IP-адресов и для ввода маски подсети. Также ограничивают режим. |",
    ),
    (
        "| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Support of various JavaScript frameworks. |",
        "| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. |",
    ),
    (
        "| javaScriptInjectionRules | [JavaScriptInjectionRules[]](#openapi-definition-JavaScriptInjectionRules) | Java script injection rules. |",
        "| javaScriptInjectionRules | [JavaScriptInjectionRules[]](#openapi-definition-JavaScriptInjectionRules) | Правила внедрения JavaScript. |",
    ),
    (
        "| libraryFileFromCdn | boolean | Get the JavaScript library file from the CDN.  Not supported by agentless applications and assumed to be false for auto-injected applications if omitted. |",
        "| libraryFileFromCdn | boolean | Получать файл библиотеки JavaScript из CDN.  Не поддерживается безагентными приложениями и считается false для авто-внедряемых приложений, если опущено. |",
    ),
    (
        "| libraryFileLocation | string | The location of your application's custom JavaScript library file.  If nothing specified the root directory of your web server is used.  **Required** for auto-injected applications, not supported by agentless applications. |",
        "| libraryFileLocation | string | Расположение пользовательского файла библиотеки JavaScript вашего приложения.  Если ничего не указано, используется корневой каталог вашего веб-сервера.  **Required** для авто-внедряемых приложений, не поддерживается безагентными приложениями. |",
    ),
    (
        "| monitoringDataPath | string | The location to send monitoring data from the JavaScript tag.  Specify either a relative or an absolute URL. If you use an absolute URL, data will be sent using CORS.  **Required** for auto-injected applications, optional for agentless applications. |",
        "| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Укажите относительный или абсолютный URL. Если вы используете абсолютный URL, данные будут отправляться через CORS.  **Required** для авто-внедряемых приложений, опционально для безагентных приложений. |",
    ),
    (
        "| sameSiteCookieAttribute | string | Same site cookie attribute The element can hold these values",
        "| sameSiteCookieAttribute | string | Атрибут cookie SameSite Возможные значения:",
    ),
    (
        "| scriptTagCacheDurationInHours | integer | Time duration for the cache settings. |",
        "| scriptTagCacheDurationInHours | integer | Длительность для настроек кэша. |",
    ),
    (
        "| secureCookieAttribute | boolean | Secure attribute usage for Dynatrace cookies enabled/disabled. |",
        "| secureCookieAttribute | boolean | Использование атрибута secure для cookie Dynatrace включено/отключено. |",
    ),
    (
        "| serverRequestPathId | string | Path to identify the server's request ID. |",
        "| serverRequestPathId | string | Путь для идентификации ID запроса сервера. |",
    ),
    (
        "| useCors | boolean | Send beacon data via CORS. |",
        "| useCors | boolean | Отправлять данные beacon через CORS. |",
    ),
    (
        "| xmlHttpRequest | boolean | `XmlHttpRequest` support enabled/disabled. |",
        "| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest` включена/отключена. |",
    ),
    # --- AdvancedJavaScriptTagSettings fields ---
    (
        "| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Additional event handlers and wrappers. |",
        "| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики и обёртки событий. |",
    ),
    (
        "| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | In addition to the event handlers, events called using `addEventListener` or `attachEvent` can be captured. Be careful with this option! Event wrappers can conflict with the JavaScript code on a web page. |",
        "| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | Помимо обработчиков событий, можно захватывать события, вызываемые через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице. |",
    ),
    (
        "| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Global event capture settings. |",
        "| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. |",
    ),
    (
        "| instrumentUnsupportedAjaxFrameworks | boolean | Instrumentation of unsupported Ajax frameworks enabled/disabled. |",
        "| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков включено/отключено. |",
    ),
    (
        "| maxActionNameLength | integer | Maximum character length for action names. Valid values range from 5 to 10000. |",
        "| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения: от `5` до `10000`. |",
    ),
    (
        "| maxErrorsToCapture | integer | Maximum number of errors to be captured per page. Valid values range from 0 to 50. |",
        "| maxErrorsToCapture | integer | Максимальное число ошибок, захватываемых на страницу. Допустимые значения: от `0` до `50`. |",
    ),
    (
        "| proxyWrapperEnabled | boolean | Proxy wrapper enabled/disabled. |",
        "| proxyWrapperEnabled | boolean | Обёртка прокси включена/отключена. |",
    ),
    (
        "| specialCharactersToEscape | string | Additional special characters that are to be escaped using non-alphanumeric characters in HTML escape format. |",
        "| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать с использованием не-алфавитно-цифровых символов в формате HTML escape. |",
    ),
    (
        "| syncBeaconFirefox | boolean | Send the beacon signal as a synchronous XMLHttpRequest using Firefox enabled/disabled. |",
        "| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest через Firefox включена/отключена. |",
    ),
    (
        "| syncBeaconInternetExplorer | boolean | Send the beacon signal as a synchronous XMLHttpRequest using Internet Explorer enabled/disabled. |",
        "| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest через Internet Explorer включена/отключена. |",
    ),
    (
        "| userActionNameAttribute | string | User action name attribute. |",
        "| userActionNameAttribute | string | Атрибут имени пользовательского действия. |",
    ),
    # --- AdditionalEventHandlers fields ---
    (
        "| blurEventHandler | boolean | Blur event handler enabled/disabled. |",
        "| blurEventHandler | boolean | Обработчик события blur включён/отключён. |",
    ),
    (
        "| changeEventHandler | boolean | Change event handler enabled/disabled. |",
        "| changeEventHandler | boolean | Обработчик события change включён/отключён. |",
    ),
    (
        "| clickEventHandler | boolean | Click event handler enabled/disabled. |",
        "| clickEventHandler | boolean | Обработчик события click включён/отключён. |",
    ),
    (
        "| maxDomNodesToInstrument | integer | Max. number of DOM nodes to instrument. Valid values range from 0 to 100000. |",
        "| maxDomNodesToInstrument | integer | Макс. число DOM-узлов для инструментирования. Допустимые значения: от `0` до `100000`. |",
    ),
    (
        "| mouseupEventHandler | boolean | Mouseup event handler enabled/disabled. |",
        "| mouseupEventHandler | boolean | Обработчик события mouseup включён/отключён. |",
    ),
    (
        "| toStringMethod | boolean | toString method enabled/disabled. |",
        "| toStringMethod | boolean | Метод toString включён/отключён. |",
    ),
    (
        "| userMouseupEventForClicks | boolean | Use mouseup event for clicks enabled/disabled. |",
        "| userMouseupEventForClicks | boolean | Использование события mouseup для кликов включено/отключено. |",
    ),
    # --- EventWrapperSettings fields ---
    (
        "| blur | boolean | Blur enabled/disabled. |",
        "| blur | boolean | Blur включён/отключён. |",
    ),
    (
        "| change | boolean | Change enabled/disabled. |",
        "| change | boolean | Change включён/отключён. |",
    ),
    (
        "| click | boolean | Click enabled/disabled. |",
        "| click | boolean | Click включён/отключён. |",
    ),
    (
        "| mouseUp | boolean | MouseUp enabled/disabled. |",
        "| mouseUp | boolean | MouseUp включён/отключён. |",
    ),
    (
        "| touchEnd | boolean | TouchEnd enabled/disabled. |",
        "| touchEnd | boolean | TouchEnd включён/отключён. |",
    ),
    (
        "| touchStart | boolean | TouchStart enabled/disabled. |",
        "| touchStart | boolean | TouchStart включён/отключён. |",
    ),
    # --- GlobalEventCaptureSettings fields ---
    (
        "| additionalEventCapturedAsUserInput | string | Additional events to be captured globally as user input.  For example, DragStart or DragEnd. |",
        "| additionalEventCapturedAsUserInput | string | Дополнительные события, захватываемые глобально как пользовательский ввод.  Например, DragStart или DragEnd. |",
    ),
    (
        "| doubleClick | boolean | DoubleClick enabled/disabled. |",
        "| doubleClick | boolean | DoubleClick включён/отключён. |",
    ),
    (
        "| keyDown | boolean | KeyDown enabled/disabled. |",
        "| keyDown | boolean | KeyDown включён/отключён. |",
    ),
    (
        "| keyUp | boolean | KeyUp enabled/disabled. |",
        "| keyUp | boolean | KeyUp включён/отключён. |",
    ),
    (
        "| mouseDown | boolean | MouseDown enabled/disabled. |",
        "| mouseDown | boolean | MouseDown включён/отключён. |",
    ),
    (
        "| mouseUp | boolean | MouseUp enabled/disabled. |",
        "| mouseUp | boolean | MouseUp включён/отключён. |",
    ),
    (
        "| scroll | boolean | Scroll enabled/disabled. |",
        "| scroll | boolean | Scroll включён/отключён. |",
    ),
    # --- WebApplicationConfigBrowserRestrictionSettings / Restriction ---
    (
        "| browserRestrictions | [WebApplicationConfigBrowserRestriction[]](#openapi-definition-WebApplicationConfigBrowserRestriction) | A list of browser restrictions. |",
        "| browserRestrictions | [WebApplicationConfigBrowserRestriction[]](#openapi-definition-WebApplicationConfigBrowserRestriction) | Список ограничений браузеров. |",
    ),
    (
        "| mode | string | The mode of the list of browser restrictions. The element can hold these values",
        "| mode | string | Режим списка ограничений браузеров. Возможные значения:",
    ),
    (
        "| browserType | string | The type of the browser that is used. The element can hold these values",
        "| browserType | string | Тип используемого браузера. Возможные значения:",
    ),
    (
        "| browserVersion | string | The version of the browser that is used. |",
        "| browserVersion | string | Версия используемого браузера. |",
    ),
    (
        "| comparator | string | Compares different browsers together. The element can hold these values",
        "| comparator | string | Сравнивает разные браузеры между собой. Возможные значения:",
    ),
    (
        "| platform | string | The platform on which the browser is being used. The element can hold these values",
        "| platform | string | Платформа, на которой используется браузер. Возможные значения:",
    ),
    # --- ContentCapture fields ---
    (
        "| javaScriptErrors | boolean | JavaScript errors monitoring enabled/disabled. |",
        "| javaScriptErrors | boolean | Мониторинг ошибок JavaScript включён/отключён. |",
    ),
    (
        "| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Settings for resource timings capture. |",
        "| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки захвата таймингов ресурсов. |",
    ),
    (
        "| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Settings for timed action capture. |",
        "| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки захвата отложенных действий. |",
    ),
    (
        "| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Settings for VisuallyComplete2 |",
        "| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки VisuallyComplete2 |",
    ),
    (
        "| visuallyCompleteAndSpeedIndex | boolean | Visually complete and Speed index support enabled/disabled. |",
        "| visuallyCompleteAndSpeedIndex | boolean | Поддержка Visually complete и Speed index включена/отключена. |",
    ),
    # --- ResourceTimingSettings fields ---
    (
        "| nonW3cResourceTimings | boolean | Timing for JavaScript files and images on non-W3C supported browsers enabled/disabled. |",
        "| nonW3cResourceTimings | boolean | Тайминги для файлов JavaScript и изображений в браузерах без поддержки W3C включены/отключены. |",
    ),
    (
        "| nonW3cResourceTimingsInstrumentationDelay | integer | Instrumentation delay for monitoring resource and image resource impact in browsers that don't offer W3C resource timings.  Valid values range from 0 to 9999.  Only effective if **nonW3cResourceTimings** is enabled. |",
        "| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и ресурсов-изображений в браузерах, не предоставляющих тайминги ресурсов W3C.  Допустимые значения: от `0` до `9999`.  Действует только если **nonW3cResourceTimings** включён. |",
    ),
    (
        "| resourceTimingCaptureType | string | Defines how detailed resource timings are captured.  Only effective if **w3cResourceTimings** or **nonW3cResourceTimings** is enabled. The element can hold these values",
        "| resourceTimingCaptureType | string | Определяет, насколько детально захватываются тайминги ресурсов.  Действует только если включён **w3cResourceTimings** или **nonW3cResourceTimings**. Возможные значения:",
    ),
    (
        "| resourceTimingsDomainLimit | integer | Limits the number of domains for which W3C resource timings are captured.  Only effective if **resourceTimingCaptureType** is `CAPTURE_LIMITED_SUMMARIES`. |",
        "| resourceTimingsDomainLimit | integer | Ограничивает число доменов, для которых захватываются тайминги ресурсов W3C.  Действует только если **resourceTimingCaptureType** равен `CAPTURE_LIMITED_SUMMARIES`. |",
    ),
    (
        "| w3cResourceTimings | boolean | W3C resource timings for third party/CDN enabled/disabled. |",
        "| w3cResourceTimings | boolean | Тайминги ресурсов W3C для сторонних/CDN включены/отключены. |",
    ),
    # --- TimeoutSettings fields ---
    (
        "| temporaryActionLimit | integer | Defines how deep temporary actions may cascade. 0 disables temporary actions completely. Recommended value if enabled is 3. |",
        "| temporaryActionLimit | integer | Определяет, насколько глубоко могут каскадироваться временные действия. 0 полностью отключает временные действия. Рекомендуемое значение при включении равно 3. |",
    ),
    (
        "| temporaryActionTotalTimeout | integer | The total timeout of all cascaded timeouts that should still be able to create a temporary action |",
        "| temporaryActionTotalTimeout | integer | Суммарный таймаут всех каскадированных таймаутов, при котором ещё можно создать временное действие |",
    ),
    (
        "| timedActionSupport | boolean | Timed action support enabled/disabled.  Enable to detect actions that trigger sending of XHRs via *setTimout* methods. |",
        "| timedActionSupport | boolean | Поддержка отложенных действий включена/отключена.  Включите, чтобы обнаруживать действия, которые инициируют отправку XHR через методы *setTimout*. |",
    ),
    # --- VisuallyComplete2Settings fields ---
    (
        "| excludeUrlRegex | string | A RegularExpression used to exclude images and iframes from being detected by the VC module. |",
        "| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. |",
    ),
    (
        "| ignoredMutationsList | string | Query selector for mutation nodes to ignore in VC and SI calculation |",
        "| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при расчёте VC и SI |",
    ),
    (
        "| inactivityTimeout | integer | The time in ms the VC module waits for no mutations happening on the page after the load action. Defaults to 1000. |",
        "| inactivityTimeout | integer | Время в мс, которое модуль VC ожидает отсутствия мутаций на странице после действия загрузки. По умолчанию 1000. |",
    ),
    (
        "| mutationTimeout | integer | Determines the time in ms VC waits after an action closes to start calculation. Defaults to 50. |",
        "| mutationTimeout | integer | Определяет время в мс, которое VC ожидает после закрытия действия перед началом расчёта. По умолчанию 50. |",
    ),
    (
        "| threshold | integer | Minimum visible area in pixels of elements to be counted towards VC and SI. Defaults to 50. |",
        "| threshold | integer | Минимальная видимая площадь элементов в пикселях, учитываемая для VC и SI. По умолчанию 50. |",
    ),
    # --- WebApplicationConfigIpAddressRestrictionSettings / IpAddressRange ---
    (
        "| ipAddressRestrictions | [IpAddressRange[]](#openapi-definition-IpAddressRange) | - |",
        "| ipAddressRestrictions | [IpAddressRange[]](#openapi-definition-IpAddressRange) | - |",
    ),
    (
        "| mode | string | The mode of the list of ip address restrictions. The element can hold these values",
        "| mode | string | Режим списка ограничений IP-адресов. Возможные значения:",
    ),
    (
        "| address | string | The IP address to be mapped.  For an IP address range, this is the **from** address. |",
        "| address | string | Сопоставляемый IP-адрес.  Для диапазона IP-адресов это адрес **from**. |",
    ),
    (
        "| addressTo | string | The **to** address of the IP address range. |",
        "| addressTo | string | Адрес **to** диапазона IP-адресов. |",
    ),
    (
        "| subnetMask | integer | The subnet mask of the IP address range. |",
        "| subnetMask | integer | Маска подсети диапазона IP-адресов. |",
    ),
    # --- JavaScriptFrameworkSupport fields ---
    (
        "| activeXObject | boolean | ActiveXObject detection support enabled/disabled. |",
        "| activeXObject | boolean | Поддержка обнаружения ActiveXObject включена/отключена. |",
    ),
    (
        "| angular | boolean | AngularJS and Angular support enabled/disabled. |",
        "| angular | boolean | Поддержка AngularJS и Angular включена/отключена. |",
    ),
    (
        "| dojo | boolean | Dojo support enabled/disabled. |",
        "| dojo | boolean | Поддержка Dojo включена/отключена. |",
    ),
    (
        "| extJS | boolean | ExtJS, Sencha Touch support enabled/disabled. |",
        "| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/отключена. |",
    ),
    (
        "| icefaces | boolean | ICEfaces support enabled/disabled. |",
        "| icefaces | boolean | Поддержка ICEfaces включена/отключена. |",
    ),
    (
        "| jQuery | boolean | jQuery, Backbone.js support enabled/disabled. |",
        "| jQuery | boolean | Поддержка jQuery, Backbone.js включена/отключена. |",
    ),
    (
        "| mooTools | boolean | MooTools support enabled/disabled. |",
        "| mooTools | boolean | Поддержка MooTools включена/отключена. |",
    ),
    (
        "| prototype | boolean | Prototype support enabled/disabled. |",
        "| prototype | boolean | Поддержка Prototype включена/отключена. |",
    ),
    # --- JavaScriptInjectionRules fields ---
    (
        "| enabled | boolean | The enable or disable rule of the java script injection. |",
        "| enabled | boolean | Правило включения или отключения внедрения JavaScript. |",
    ),
    (
        "| htmlPattern | string | The html pattern of the java script injection. |",
        "| htmlPattern | string | HTML-шаблон внедрения JavaScript. |",
    ),
    (
        "| rule | string | The url rule of the java script injection. The element can hold these values",
        "| rule | string | Правило URL внедрения JavaScript. Возможные значения:",
    ),
    (
        "| target | string | The target against which the rule of the java script injection should be matched. The element can hold these values",
        "| target | string | Цель, по которой сопоставляется правило внедрения JavaScript. Возможные значения:",
    ),
    (
        "| urlOperator | string | The url operator of the java script injection. The element can hold these values",
        "| urlOperator | string | URL-оператор внедрения JavaScript. Возможные значения:",
    ),
    (
        "| urlPattern | string | The url pattern of the java script injection. |",
        "| urlPattern | string | URL-шаблон внедрения JavaScript. |",
    ),
    # --- SessionReplaySetting fields ---
    (
        "| costControlPercentage | integer | Session replay sampling rating in percentage. |",
        "| costControlPercentage | integer | Частота сэмплирования Session Replay в процентах. |",
    ),
    (
        "| cssResourceCapturingExclusionRules | string[] | A list of URLs to be excluded from CSS resource capturing. |",
        "| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата CSS-ресурсов. |",
    ),
    (
        "| enableCssResourceCapturing | boolean | Capture (`true`) or don't capture (`false`) CSS resources from the session. |",
        "| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) CSS-ресурсы из сессии. |",
    ),
    (
        "| enabled | boolean | SessionReplay Enabled. |",
        "| enabled | boolean | Session Replay включён. |",
    ),
    # --- UserActionAndSessionProperties fields ---
    (
        "| aggregation | string | The aggregation type of the property.  It defines how multiple values of the property are aggregated. The element can hold these values",
        "| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Возможные значения:",
    ),
    (
        "| cleanupRule | string | The cleanup rule of the property.  Defines how to extract the data you need from a string value. Specify the [regular expression\xef\xbb\xbf](https://dt-url.net/k9e0iaq) for the data you need there. |",
        "| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение](https://dt-url.net/k9e0iaq) для нужных вам данных. |",
    ),
    (
        "| displayName | string | The display name of the property. |",
        "| displayName | string | Отображаемое имя свойства. |",
    ),
    (
        "| ignoreCase | boolean | If true, the value of this property will always be stored in lower case. Defaults to false. |",
        "| ignoreCase | boolean | Если true, значение этого свойства всегда сохраняется в нижнем регистре. По умолчанию false. |",
    ),
    (
        "| key | string | Key of the property |",
        "| key | string | Ключ свойства |",
    ),
    (
        "| longStringLength | integer | If the type is LONG\\_STRING, the max length for this property. Must be a multiple of 100. Defaults to 200. |",
        "| longStringLength | integer | Если тип LONG\\_STRING, максимальная длина для этого свойства. Должна быть кратна 100. По умолчанию 200. |",
    ),
    (
        '| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig.Must be set if "origin" is of type META\\_DATA. |',
        '| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig.Должна быть задана, если "origin" имеет тип META\\_DATA. |',
    ),
    (
        "| origin | string | The origin of the property The element can hold these values",
        "| origin | string | Источник свойства Возможные значения:",
    ),
    (
        "| serverSideRequestAttribute | string | The ID of the request attribute.  Only applicable when the **origin** is set to `SERVER_SIDE_REQUEST_ATTRIBUTE`. |",
        "| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. |",
    ),
    (
        "| storeAsSessionProperty | boolean | If `true`, the property is stored as a session property |",
        "| storeAsSessionProperty | boolean | Если `true`, свойство хранится как свойство сессии |",
    ),
    (
        "| storeAsUserActionProperty | boolean | If `true`, the property is stored as a user action property |",
        "| storeAsUserActionProperty | boolean | Если `true`, свойство хранится как свойство пользовательского действия |",
    ),
    (
        "| type | string | The data type of the property. The element can hold these values",
        "| type | string | Тип данных свойства. Возможные значения:",
    ),
    (
        "| uniqueId | integer | Unique id among all userTags and properties of this application |",
        "| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения |",
    ),
    # --- UserActionNamingSettings fields ---
    (
        "| customActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | User action naming rules for custom actions. |",
        "| customActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для пользовательских действий. |",
    ),
    (
        "| ignoreCase | boolean | Case insensitive naming. |",
        "| ignoreCase | boolean | Именование без учёта регистра. |",
    ),
    (
        "| loadActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | User action naming rules for loading actions. |",
        "| loadActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для действий загрузки. |",
    ),
    (
        "| placeholders | [UserActionNamingPlaceholder[]](#openapi-definition-UserActionNamingPlaceholder) | User action placeholders. |",
        "| placeholders | [UserActionNamingPlaceholder[]](#openapi-definition-UserActionNamingPlaceholder) | Плейсхолдеры пользовательских действий. |",
    ),
    (
        "| queryParameterCleanups | string[] | List of parameters that should be removed from the query before using the query in the user action name. |",
        "| queryParameterCleanups | string[] | Список параметров, которые нужно удалить из запроса перед использованием запроса в имени пользовательского действия. |",
    ),
    (
        "| splitUserActionsByDomain | boolean | Deactivate this setting if different domains should not result in separate user actions. |",
        "| splitUserActionsByDomain | boolean | Отключите эту настройку, если разные домены не должны приводить к отдельным пользовательским действиям. |",
    ),
    (
        "| useFirstDetectedLoadAction | boolean | First load action found under an XHR action should be used when true. Else the deepest one under the xhr action is used |",
        "| useFirstDetectedLoadAction | boolean | Если true, используется первое действие загрузки, найденное под XHR-действием. Иначе используется самое глубокое под XHR-действием |",
    ),
    (
        "| xhrActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | User action naming rules for xhr actions. |",
        "| xhrActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для XHR-действий. |",
    ),
    # --- UserActionNamingRule fields ---
    (
        "| conditions | [UserActionNamingRuleCondition[]](#openapi-definition-UserActionNamingRuleCondition) | Defines the conditions when the naming rule should apply. |",
        "| conditions | [UserActionNamingRuleCondition[]](#openapi-definition-UserActionNamingRuleCondition) | Определяет условия, при которых должно применяться правило именования. |",
    ),
    (
        "| template | string | Naming pattern. Use Curly brackets `{}` to select placeholders. |",
        "| template | string | Шаблон именования. Используйте фигурные скобки `{}` для выбора плейсхолдеров. |",
    ),
    (
        "| useOrConditions | boolean | If set to `true` the conditions will be connected by logical OR instead of logical AND. |",
        "| useOrConditions | boolean | Если установлено `true`, условия соединяются логическим OR вместо логического AND. |",
    ),
    # --- UserActionNamingRuleCondition fields ---
    (
        "| operand1 | string | Must be a defined placeholder wrapped in curly braces |",
        "| operand1 | string | Должен быть определённым плейсхолдером в фигурных скобках |",
    ),
    (
        '| operand2 | string | Must be null if operator is "IS\\_EMPTY", a regex if operator is "MATCHES\\_REGULAR\\_ERPRESSION". In all other cases the value can be a freetext or a placeholder wrapped in curly braces |',
        '| operand2 | string | Должен быть null, если оператор "IS\\_EMPTY", регулярным выражением, если оператор "MATCHES\\_REGULAR\\_ERPRESSION". Во всех остальных случаях значение может быть произвольным текстом или плейсхолдером в фигурных скобках |',
    ),
    (
        "| operator | string | The operator of the condition The element can hold these values",
        "| operator | string | Оператор условия Возможные значения:",
    ),
    # --- UserActionNamingPlaceholder fields ---
    (
        "| input | string | Input. The element can hold these values",
        "| input | string | Ввод. Возможные значения:",
    ),
    (
        '| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig. Must be set if "Input" is of type METADATA. |',
        '| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если "Input" имеет тип METADATA. |',
    ),
    (
        "| name | string | Placeholder name. |",
        "| name | string | Имя плейсхолдера. |",
    ),
    (
        "| processingPart | string | Part. The element can hold these values",
        "| processingPart | string | Часть. Возможные значения:",
    ),
    (
        "| processingSteps | [UserActionNamingPlaceholderProcessingStep[]](#openapi-definition-UserActionNamingPlaceholderProcessingStep) | Processing actions. |",
        "| processingSteps | [UserActionNamingPlaceholderProcessingStep[]](#openapi-definition-UserActionNamingPlaceholderProcessingStep) | Действия обработки. |",
    ),
    (
        "| useGuessedElementIdentifier | boolean | Use the element identifier that was selected by Dynatrace. |",
        "| useGuessedElementIdentifier | boolean | Использовать идентификатор элемента, выбранный Dynatrace. |",
    ),
    # --- UserActionNamingPlaceholderProcessingStep fields ---
    (
        "| fallbackToInput | boolean | If set to true: Returns the input if **patternBefore** or **patternAfter** cannot be found and the **type** is `SUBSTRING`.  Returns the input if **regularExpression** doesn't match and **type** is `EXTRACT_BY_REGULAR_EXPRESSION`.  Otherwise null is returned. |",
        "| fallbackToInput | boolean | Если установлено true: возвращает ввод, если **patternBefore** или **patternAfter** не найдены и **type** равен `SUBSTRING`.  Возвращает ввод, если **regularExpression** не совпадает и **type** равен `EXTRACT_BY_REGULAR_EXPRESSION`.  Иначе возвращается null. |",
    ),
    (
        "| patternAfter | string | The pattern after the required value. It will be removed. |",
        "| patternAfter | string | Шаблон после нужного значения. Он будет удалён. |",
    ),
    (
        "| patternAfterSearchType | string | The required occurrence of **patternAfter**. The element can hold these values",
        "| patternAfterSearchType | string | Нужное вхождение **patternAfter**. Возможные значения:",
    ),
    (
        "| patternBefore | string | The pattern before the required value. It will be removed. |",
        "| patternBefore | string | Шаблон перед нужным значением. Он будет удалён. |",
    ),
    (
        "| patternBeforeSearchType | string | The required occurrence of **patternBefore**. The element can hold these values",
        "| patternBeforeSearchType | string | Нужное вхождение **patternBefore**. Возможные значения:",
    ),
    (
        "| patternToReplace | string | The pattern to be replaced.  Only applicable if the **type** is `REPLACE_WITH_PATTERN`. |",
        "| patternToReplace | string | Заменяемый шаблон.  Применимо только если **type** равен `REPLACE_WITH_PATTERN`. |",
    ),
    (
        "| regularExpression | string | A regular expression for the string to be extracted or replaced.  Only applicable if the **type** is `EXTRACT_BY_REGULAR_EXPRESSION` or `REPLACE_WITH_REGULAR_EXPRESSION`. |",
        "| regularExpression | string | Регулярное выражение для извлекаемой или заменяемой строки.  Применимо только если **type** равен `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. |",
    ),
    (
        "| replacement | string | Replacement for the original value. |",
        "| replacement | string | Замена для исходного значения. |",
    ),
    (
        "| type | string | An action to be taken by the processing:  * `SUBSTRING`: Extracts the string between **patternBefore** and **patternAfter**. * `REPLACEMENT`: Replaces the string between **patternBefore** and **patternAfter** with the specified **replacement**. * `REPLACE_WITH_PATTERN`: Replaces the **patternToReplace** with the specified **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: Extracts the part of the string that matches the **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: Replaces all occurrences that match **regularExpression** with the specified **replacement**. * `REPLACE_IDS`: Replaces all IDs and UUIDs with the specified **replacement**. The element can hold these values",
        "| type | string | Действие, выполняемое при обработке:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанную **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанную **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, соответствующую **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, соответствующие **regularExpression**, на указанную **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанную **replacement**. Возможные значения:",
    ),
    # --- UserTag fields ---
    (
        "| cleanupRule | string | Cleanup rule expression of the userTag |",
        "| cleanupRule | string | Выражение правила очистки userTag |",
    ),
    (
        "| ignoreCase | boolean | If true, the value of this tag will always be stored in lower case. Defaults to false. |",
        "| ignoreCase | boolean | Если true, значение этого тега всегда сохраняется в нижнем регистре. По умолчанию false. |",
    ),
    (
        "| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig. Must be set if the UserTag is based on metadata captured by the Javascript agent (e.g. a Javascript variable, CSS selector, etc.) |",
        "| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если UserTag основан на метаданных, захваченных JavaScript-агентом (например, переменная JavaScript, CSS-селектор и т. д.) |",
    ),
    (
        "| serverSideRequestAttribute | string | Serverside request attribute id of the userTag. Must be set if the UserTag is based on a serverside request attribute. |",
        "| serverSideRequestAttribute | string | ID серверного атрибута запроса userTag. Должен быть задан, если UserTag основан на серверном атрибуте запроса. |",
    ),
    (
        "| uniqueId | integer | uniqueId, unique among all userTags and properties of this application |",
        "| uniqueId | integer | uniqueId, уникальный среди всех userTags и свойств этого приложения |",
    ),
    # --- WaterfallSettings fields ---
    (
        "| resourceBrowserCachingThreshold | integer | Warn about resources with a lower browser cache rate above *X*%. |",
        "| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с более низкой частотой кэширования браузером выше *X*%. |",
    ),
    (
        "| resourcesThreshold | integer | Warn about resources larger than *X* bytes. |",
        "| resourcesThreshold | integer | Предупреждать о ресурсах больше *X* байт. |",
    ),
    (
        "| slowCdnResourcesThreshold | integer | Warn about slow CDN resources with a response time above *X* ms. |",
        "| slowCdnResourcesThreshold | integer | Предупреждать о медленных CDN-ресурсах со временем отклика выше *X* мс. |",
    ),
    (
        "| slowFirstPartyResourcesThreshold | integer | Warn about slow 1st party resources with a response time above *X* ms. |",
        "| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных собственных ресурсах со временем отклика выше *X* мс. |",
    ),
    (
        "| slowThirdPartyResourcesThreshold | integer | Warn about slow 3rd party resources with a response time above *X* ms. |",
        "| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных сторонних ресурсах со временем отклика выше *X* мс. |",
    ),
    (
        "| speedIndexVisuallyCompleteRatioThreshold | integer | Warn if Speed index exceeds *X* % of Visually complete. |",
        "| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X* % от Visually complete. |",
    ),
    (
        "| uncompressedResourcesThreshold | integer | Warn about uncompressed resources larger than *X* bytes. |",
        "| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах больше *X* байт. |",
    ),
    # --- response-code cells (L101: period stays outside the matched span) ---
    (
        "Success. The response body contains the ID and name of the new web application.",
        "Успех. Тело ответа содержит ID и имя нового веб-приложения.",
    ),
    (
        "Success. The new configuration has been created. The response body contains the ID and name of the new web application.",
        "Успех. Новая конфигурация создана. Тело ответа содержит ID и имя нового веб-приложения.",
    ),
    (
        "Success. Configuration has been updated. Response doesn't have a body.",
        "Успех. Конфигурация обновлена. Ответ без тела.",
    ),
    (
        "Success. The application has been deleted. The response does not have a body.",
        "Успех. Приложение удалено. Ответ без тела.",
    ),
    (
        "Validated. The submitted configuration is valid. Response does not have a body.",
        "Validated. Переданная конфигурация валидна. Ответ без тела.",
    ),
    # bare GET-200 cell (L4V canon: error-rules/key-user-actions/data-privacy
    # RU all render `| Success |` -> `| Успех |`)
    ("| Success |", "| Успех |"),
    # L101 substring (period by source — preserved outside span)
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    # --- "The element can hold these values" -> "Возможные значения:" WITH
    #     colon (L99; also handles leading-dash `-The element ...`) ---
    ("The element can hold these values", "Возможные значения:"),
]

# ---------------------------------------------------------------- PER-FILE
P = {}

# ---- default-application/get-configuration ----
P["default-application/get-configuration.md"] = [
    (
        "Gets parameters of the default web application of your Dynatrace environment.",
        "Возвращает параметры веб-приложения по умолчанию вашего окружения Dynatrace.",
    ),
]

# ---- default-application/put-configuration ----
P["default-application/put-configuration.md"] = [
    (
        "Updates the default web application of your Dynatrace environment.",
        "Обновляет веб-приложение по умолчанию вашего окружения Dynatrace.",
    ),
    (
        "| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON body of the request, containing the new parameters of the default web application. | body | Optional |",
        "| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON-тело запроса, содержащее новые параметры веб-приложения по умолчанию. | body | Optional |",
    ),
]

# ---- web-application/del-web-application ----
P["web-application/del-web-application.md"] = [
    (
        "Deletes the specified web application.",
        "Удаляет указанное веб-приложение.",
    ),
    (
        "| id | string | The ID of the web application to delete. | path | Required |",
        "| id | string | ID удаляемого веб-приложения. | path | Required |",
    ),
    (
        '* [Delete a web application](/managed/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.")',
        '* [Удаление веб-приложения](/managed/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Удаление веб-приложений через веб-интерфейс Dynatrace или API.")',
    ),
]

# ---- web-application/get-all ----
P["web-application/get-all.md"] = [
    (
        "Lists all web applications configured in your Dynatrace environment.",
        "Перечисляет все веб-приложения, настроенные в вашем окружении Dynatrace.",
    ),
]

# ---- web-application/get-web-application ----
P["web-application/get-web-application.md"] = [
    (
        "Gets parameters of the specified web application.",
        "Возвращает параметры указанного веб-приложения.",
    ),
    (
        "| id | string | The ID of the requested web application. | path | Required |",
        "| id | string | ID нужного веб-приложения. | path | Required |",
    ),
]

# ---- web-application/post-web-application ----
P["web-application/post-web-application.md"] = [
    (
        "Creates a new web application.",
        "Создаёт новое веб-приложение.",
    ),
    (
        "| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON body of the request, containing parameters of the new web application configuraiton. | body | Optional |",
        "| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON-тело запроса, содержащее параметры конфигурации нового веб-приложения. | body | Optional |",
    ),
]

# ---- web-application/put-web-application ----
P["web-application/put-web-application.md"] = [
    (
        "Updates the specified web application.",
        "Обновляет указанное веб-приложение.",
    ),
    (
        "| id | string | The ID of the web application to update.  If you set the ID in the body as well, it must match this ID. | path | Required |",
        "| id | string | ID обновляемого веб-приложения.  Если вы также укажете ID в теле, он должен совпадать с этим ID. | path | Required |",
    ),
    (
        "| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON body of the request, containing updated configuration of the web application. | body | Optional |",
        "| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON-тело запроса, содержащее обновлённую конфигурацию веб-приложения. | body | Optional |",
    ),
]


def build():
    written, miss = [], 0
    for rel in FILES:
        ep = os.path.join(EN, rel.replace("/", os.sep))
        rp = os.path.join(RU, rel.replace("/", os.sep))
        with open(ep, "r", encoding="utf-8") as f:
            txt = f.read()
        txt = txt.replace("\r\n", "\n")
        if txt.startswith("﻿"):
            txt = txt[1:]
        txt = txt.replace("â", "'").replace("â", "'")
        for en, ru in P.get(rel, []):
            if en not in txt:
                print(f"  !! MISS per-file in {rel}: {en[:70]!r}")
                miss += 1
            txt = txt.replace(en, ru)
        for en, ru in COMMON:
            txt = txt.replace(en, ru)
        os.makedirs(os.path.dirname(rp), exist_ok=True)
        with open(rp, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        written.append(rel)
    print(f"built {len(written)} files -> {RU}  (per-file MISS: {miss})")
    return written


if __name__ == "__main__":
    build()
    sys.exit(0)
