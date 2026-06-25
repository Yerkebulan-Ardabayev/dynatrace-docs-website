#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splice-builder for batch L4U: configuration-api/rum/mobile-custom-app-
configuration/ parent + apps/ (5) + key-user-actions/ (3) + user-action-and-
session-properties/ (5) = 14 files.

ACTIVE API, no deprecated banner (L89/L90; `* Reference` / `* Published Nov 05,
2020`, no `* Deprecated` bullet). Continues the rum/ subsection L4S/L4T. EN ->
RU exact-string replacement only (no newline added/removed) => line-parity
automatic, code-fence byte-identical (L98/L100). EN is CRLF => normalize LF
first (L4M), strip leading BOM.

Canon anchor = FRESHEST same-subsection twin = L4T application-detection-
configuration RU + L4S content-resources RU (L4T lesson #1: freshest same-
subsection twin, NOT old pre-L99 canon). L103 case (b): env-api/rum/ has NO
mobile-custom-app twin (only geographic-regions / rum-js-code / rum-manual-
insertion-tags / user-sessions / rum-cookie-names) => anchor = config-api L99
+ shared objects from L4T appdetect RU verbatim.

Domain corpus-dominance (verified against managed-ru/):
  "custom application" -> "пользовательское приложение" (40x, 0 кастомн*)
  "user action" -> "пользовательское действие" (619x vs 80 "действие польз.")
  "Instrumentation Wizard" -> "мастер инструментирования" (L4K corpus
       "в мастере инструментирования", mobile-symbolication sibling)
  "endpoint" -> "эндпоинт" (rum/plugins corpus 42x)
  "request attribute" -> "атрибут запроса" (54x vs 15 EN)
  "Session Replay" -> EN (348x corpus + style-guide product-name lock)
  "beacon" -> EN-lock (L4S beacon domains/origins/cors all EN)
  "Apdex" -> EN (CLAUDE.md technical-term rule)
  `**tolerable**` / `**frustrated**` / `**origin**` / `**beaconEndpointType**`
       bold spans = EN-lock (style-guide UI + L99, L4S SUSPECT exclusion)
title + H1x2 + `* Reference` + `* Published` = EN-verbatim (L99).
L101: all 400 `Failed. The input is invalid` source = WITH period =>
substring match (period stays outside span, preserved). validate-204 EN
"Success. The submitted configuration is valid." -> "Успех."-prefix (NOT
"Validated.", by EN cell, L4S/L4T). 404 `Failed. The specified entity doesn't
exist` substring (period by source = all WITH period).
Related-topics link-text = target RU H1 verbatim (L4O/L4L, all 3 targets
translated: delete-application-mobile/custom + rum-concepts/user-actions);
title-attr translated by corpus pattern. BOM 3-char `\xef\xbb\xbf` (L4M)
stripped from `[regular expression]` link-text in cleanupRule cell.
Source-quirk L93 verbatim-by-meaning: "Get parameters of a session property
its ID." (missing "by").
"""

import os, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
SUB = r"docs\managed\dynatrace-api\configuration-api\rum"
SUBR = r"docs\managed-ru\dynatrace-api\configuration-api\rum"
EN = os.path.join(ROOT, SUB)
RU = os.path.join(ROOT, SUBR)

FILES = [
    "mobile-custom-app-configuration.md",
    "mobile-custom-app-configuration/apps/get-all.md",
    "mobile-custom-app-configuration/apps/get-app.md",
    "mobile-custom-app-configuration/apps/post-app.md",
    "mobile-custom-app-configuration/apps/put-app.md",
    "mobile-custom-app-configuration/apps/delete-app.md",
    "mobile-custom-app-configuration/key-user-actions/get-configuration.md",
    "mobile-custom-app-configuration/key-user-actions/post-configuration.md",
    "mobile-custom-app-configuration/key-user-actions/del-configuration.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/get-all.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/get-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/post-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/put-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/delete-property.md",
]

# ---------------------------------------------------------------- COMMON
# Applied AFTER per-file. Ordered longest/most-specific first to avoid
# substring-collision RU+EN hybrids (L4N/L4P/L4T lesson).
COMMON = [
    # --- structural headers (newline-anchored; `## Validate payload` /
    #     `#### Curl` stay EN per L99 ALLOWED_EN, L4S) ---
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
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    ("| Code | Description |", "| Код | Описание |"),
    # --- object headers (`#### The \`X\` object` -> `#### Объект \`X\``) ---
    (
        "#### The `NewMobileCustomAppConfig` object",
        "#### Объект `NewMobileCustomAppConfig`",
    ),
    (
        "#### The `MobileCustomAppConfig` object",
        "#### Объект `MobileCustomAppConfig`",
    ),
    ("#### The `MobileCustomApdex` object", "#### Объект `MobileCustomApdex`"),
    (
        "#### The `KeyUserActionMobileList` object",
        "#### Объект `KeyUserActionMobileList`",
    ),
    ("#### The `KeyUserActionMobile` object", "#### Объект `KeyUserActionMobile`"),
    (
        "#### The `MobileSessionUserActionPropertyList` object",
        "#### Объект `MobileSessionUserActionPropertyList`",
    ),
    (
        "#### The `MobileSessionUserActionPropertyShort` object",
        "#### Объект `MobileSessionUserActionPropertyShort`",
    ),
    (
        "#### The `MobileSessionUserActionPropertyUpd` object",
        "#### Объект `MobileSessionUserActionPropertyUpd`",
    ),
    (
        "#### The `MobileSessionUserActionProperty` object",
        "#### Объект `MobileSessionUserActionProperty`",
    ),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    # --- shared boilerplate prose ---
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
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.",
    ),
    # --- shared param cell (delete/get/put-app + key-user x3 + props x4) ---
    (
        "| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |",
        "| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |",
    ),
    (
        "| id | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |",
        "| id | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |",
    ),
    (
        "| key | string | The key of the required mobile session or user action property. | path | Required |",
        "| key | string | Ключ нужного свойства мобильной сессии или пользовательского действия. | path | Required |",
    ),
    # --- shared EntityShortRepresentation / Error / ConstraintViolation
    #     canon (verbatim from L4T appdetect RU) ---
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
    # --- SHARED app-config field descriptions (get-app/post-app/put-app
    #     MobileCustomAppConfig + NewMobileCustomAppConfig identical) ---
    # longest-first: cell variant (double-space "  A duration") BEFORE the
    # standalone object-intro line "Apdex configuration ..." (substring)
    (
        "Apdex configuration of a mobile or custom application.  A duration less than the **tolerable** threshold is considered satisfied.",
        "Конфигурация Apdex для мобильного или пользовательского приложения.  Длительность меньше порога **tolerable** считается удовлетворительной.",
    ),
    (
        "A duration less than the **tolerable** threshold is considered satisfied.",
        "Длительность меньше порога **tolerable** считается удовлетворительной.",
    ),
    (
        "Apdex configuration of a mobile or custom application.",
        "Конфигурация Apdex для мобильного или пользовательского приложения.",
    ),
    (
        "Configuration of an existing mobile or custom application.",
        "Конфигурация существующего мобильного или пользовательского приложения.",
    ),
    (
        "Configuration of a mobile or custom application to be created.",
        "Конфигурация создаваемого мобильного или пользовательского приложения.",
    ),
    (
        "The UUID of the application.  It is used only by OneAgent to send data to Dynatrace.",
        "UUID приложения.  Используется только OneAgent для отправки данных в Dynatrace.",
    ),
    ("The type of the application.", "Тип приложения."),
    (
        "The URL of the beacon endpoint.  Only applicable when the **beaconEndpointType** is set to `ENVIRONMENT_ACTIVE_GATE` or `INSTRUMENTED_WEB_SERVER`.",
        "URL beacon-эндпоинта.  Применимо только когда **beaconEndpointType** установлен в `ENVIRONMENT_ACTIVE_GATE` или `INSTRUMENTED_WEB_SERVER`.",
    ),
    ("The type of the beacon endpoint.", "Тип beacon-эндпоинта."),
    (
        "The percentage of user sessions to be analyzed.",
        "Процент пользовательских сессий для анализа.",
    ),
    (
        "Custom application icon.  Mobile apps always use the mobile device icon, so this icon can only be set for custom apps.",
        "Иконка пользовательского приложения.  Мобильные приложения всегда используют иконку мобильного устройства, поэтому эту иконку можно задать только для пользовательских приложений.",
    ),
    (
        "The Dynatrace entity ID of the application.",
        "ID сущности Dynatrace для приложения.",
    ),
    ("The name of the application.", "Имя приложения."),
    (
        "The opt-in mode is enabled (`true`) or disabled (`false`).  This value is only applicable to mobile and not to custom apps.",
        "Режим opt-in включён (`true`) или отключён (`false`).  Это значение применимо только к мобильным, а не к пользовательским приложениям.",
    ),
    (
        "The session replay is enabled (`true`) or disabled (`false`). This value is only applicable to mobile and not to custom apps.",
        "Session Replay включён (`true`) или отключён (`false`). Это значение применимо только к мобильным, а не к пользовательским приложениям.",
    ),
    (
        "**Deprecated**. Please use `sessionReplayEnabled` to enable or disable session replay for mobile apps.",
        "**Устарело**. Используйте `sessionReplayEnabled` для включения или отключения Session Replay для мобильных приложений.",
    ),
    (
        "Apdex error condition: if `true` the user session is considered frustrated when an error is reported.",
        "Условие ошибки Apdex: если `true`, пользовательская сессия считается frustrated при сообщении об ошибке.",
    ),
    (
        "Apdex **frustrated** threshold, in milliseconds: a duration greater than or equal to this value is considered frustrated.",
        "Порог Apdex **frustrated**, в миллисекундах: длительность больше или равная этому значению считается frustrated.",
    ),
    (
        "Apdex **tolerable** threshold, in milliseconds: a duration greater than or equal to this value is considered tolerable.",
        "Порог Apdex **tolerable**, в миллисекундах: длительность больше или равная этому значению считается tolerable.",
    ),
    # --- SHARED property field descriptions (get/post/put-property
    #     MobileSessionUserActionProperty + ...Upd identical) ---
    (
        "Configuration of the mobile session or user action property.",
        "Конфигурация свойства мобильной сессии или пользовательского действия.",
    ),
    (
        "An update of a mobile session or user action property.",
        "Обновление свойства мобильной сессии или пользовательского действия.",
    ),
    (
        "A short representation of mobile session or user action property.",
        "Краткое представление свойства мобильной сессии или пользовательского действия.",
    ),
    (
        "The aggregation type of the property.  It defines how multiple values of the property are aggregated.",
        "Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства.",
    ),
    (
        "The cleanup rule of the property.  Defines how to extract the data you need from a string value. Specify the [regular expression\xef\xbb\xbf](https://dt-url.net/k9e0iaq) for the data you need there.",
        "Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение](https://dt-url.net/k9e0iaq) для нужных вам данных.",
    ),
    (
        "The display name of the session or user action property.",
        "Отображаемое имя свойства сессии или пользовательского действия.",
    ),
    ("The display name of the property.", "Отображаемое имя свойства."),
    (
        "The unique key of the mobile session or user action property.",
        "Уникальный ключ свойства мобильной сессии или пользовательского действия.",
    ),
    (
        "The key of the session or user action property.",
        "Ключ свойства сессии или пользовательского действия.",
    ),
    (
        "The name of the reported value.  Only applicable when the **origin** is set to `API`.",
        "Имя передаваемого значения.  Применимо только когда **origin** установлен в `API`.",
    ),
    ("The origin of the property", "Источник свойства"),
    (
        "The ID of the request attribute.  Only applicable when the **origin** is set to `SERVER_SIDE_REQUEST_ATTRIBUTE`.",
        "ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`.",
    ),
    (
        "If `true`, the property is stored as a session property",
        "Если `true`, свойство хранится как свойство сессии",
    ),
    (
        "If `true`, the property is stored as a user action property",
        "Если `true`, свойство хранится как свойство пользовательского действия",
    ),
    ("The data type of the property.", "Тип данных свойства."),
    # --- SHARED key-user-action descriptions ---
    (
        "A list of key actions in an application.",
        "Список ключевых действий в приложении.",
    ),
    ("A key user action.", "Ключевое пользовательское действие."),
    (
        "The name of the key user action.",
        "Имя ключевого пользовательского действия.",
    ),
    # --- SHARED session-prop-list descriptions ---
    (
        "Contains lists of short representations of mobile session properties and mobile user action properties.",
        "Содержит списки кратких представлений свойств мобильных сессий и свойств мобильных пользовательских действий.",
    ),
    (
        "A list of short representations of mobile session properties.",
        "Список кратких представлений свойств мобильных сессий.",
    ),
    (
        "A list of short representations of mobile user action properties.",
        "Список кратких представлений свойств мобильных пользовательских действий.",
    ),
    # --- response-code cells (L101: period stays outside the matched span
    #     for the recurrent ones; full-cell for the unique ones) ---
    (
        "Success. The submitted configuration is valid. Response doesn't have a body.",
        "Успех. Переданная конфигурация валидна. Ответ без тела.",
    ),
    (
        "Success. The application has been deleted. The response doesn't have a body.",
        "Успех. Приложение удалено. Ответ без тела.",
    ),
    (
        "Success. The application has been created. The response contains the identifier and name of the new application.",
        "Успех. Приложение создано. Ответ содержит идентификатор и имя нового приложения.",
    ),
    (
        "Success. The application has been updated. Response doesn't have a body.",
        "Успех. Приложение обновлено. Ответ без тела.",
    ),
    (
        "Success. The action has been marked as a key user action. The response contains its name.",
        "Успех. Действие отмечено как ключевое пользовательское действие. Ответ содержит его имя.",
    ),
    (
        "Success. The user action has been removed from the list of key user actions. The response doesn't have a body.",
        "Успех. Пользовательское действие удалено из списка ключевых пользовательских действий. Ответ без тела.",
    ),
    (
        "Success. The property has been created. The response contains the ID of the new property.",
        "Успех. Свойство создано. Ответ содержит ID нового свойства.",
    ),
    (
        "Success. The property has been updated. The response doesn't have a body.",
        "Успех. Свойство обновлено. Ответ без тела.",
    ),
    (
        "Success. The property has been deleted. The response doesn't have a body.",
        "Успех. Свойство удалено. Ответ без тела.",
    ),
    (
        "Failed. The applicationId is already used by another application.",
        "Сбой. applicationId уже используется другим приложением.",
    ),
    (
        "Failed. The max number of key user actions has been reached for the application.",
        "Сбой. Достигнуто максимальное число ключевых пользовательских действий для приложения.",
    ),
    # substring (period by source — all 404/400 in this batch = WITH period)
    (
        "Failed. The specified entity doesn't exist",
        "Сбой. Указанная сущность не существует",
    ),
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    ("| Success |", "| Успех |"),
    # --- "The element can hold these values" -> "Возможные значения:" WITH
    #     colon (L99; also handles leading-dash `-The element ...`) ---
    ("The element can hold these values", "Возможные значения:"),
]

# ---------------------------------------------------------------- PER-FILE
P = {}

# ---- parent (combined-block card canon L4T) ----
P["mobile-custom-app-configuration.md"] = [
    (
        'Get an overview of all mobile and custom apps.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-all "List all mobile and custom apps applications via the Dynatrace API.")[### View an app',
        'Обзор всех мобильных и пользовательских приложений.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-all "Список всех мобильных и пользовательских приложений через Dynatrace API.")[### Просмотр приложения',
    ),
    (
        'Get parameters of an app by its ID.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-app "View parameters of a mobile or custom app via the Dynatrace API.")',
        'Получить параметры приложения по его ID.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-app "Просмотр параметров мобильного или пользовательского приложения через Dynatrace API.")',
    ),
    (
        'Create a new mobile or custom app with the exact parameters you need.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/post-app "Create a mobile or custom app via the Dynatrace API.")[### Edit an app',
        'Создать новое мобильное или пользовательское приложение с точно нужными параметрами.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/post-app "Создание мобильного или пользовательского приложения через Dynatrace API.")[### Редактирование приложения',
    ),
    (
        'Update an existing mobile or custom application or create a new app with the specified ID.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/put-app "Update parameters of a mobile or custom app via the Dynatrace API.")[### Delete an app',
        'Обновить существующее мобильное или пользовательское приложение или создать новое приложение с указанным ID.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/put-app "Обновление параметров мобильного или пользовательского приложения через Dynatrace API.")[### Удаление приложения',
    ),
    (
        'Delete an app you don\'t need anymore.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/delete-app "Delete a mobile or custom app via the Dynatrace API.")',
        'Удалить ненужное приложение.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/delete-app "Удаление мобильного или пользовательского приложения через Dynatrace API.")',
    ),
    (
        'Get the list of key user actions in the specified application.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/get-configuration "View key user actions of a mobile or custom app via the Dynatrace API.")[### Edit key user actions list',
        'Получить список ключевых пользовательских действий в указанном приложении.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/get-configuration "Просмотр ключевых пользовательских действий мобильного или пользовательского приложения через Dynatrace API.")[### Редактирование списка ключевых пользовательских действий',
    ),
    (
        'Mark a user action as the key action in the specified application.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/post-configuration "Add a key user action to a mobile or custom app via the Dynatrace API.")[### Delete a key user action',
        'Отметить пользовательское действие как ключевое в указанном приложении.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/post-configuration "Добавление ключевого пользовательского действия в мобильное или пользовательское приложение через Dynatrace API.")[### Удаление ключевого пользовательского действия',
    ),
    (
        'Remove a user action from the list of key actions in the specified application.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/del-configuration "Remove a key user action from a mobile or custom app via the Dynatrace API.")',
        'Удалить пользовательское действие из списка ключевых действий в указанном приложении.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/del-configuration "Удаление ключевого пользовательского действия из мобильного или пользовательского приложения через Dynatrace API.")',
    ),
    (
        'Get an overview of all session properties of an app.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-all "View all user session properties a mobile or custom app via the Dynatrace API.")[### View a user session property',
        'Обзор всех свойств сессий приложения.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-all "Просмотр всех свойств пользовательских сессий мобильного или пользовательского приложения через Dynatrace API.")[### Просмотр свойства пользовательской сессии',
    ),
    (
        'Get parameters of a session property its ID.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-property "View user session property a mobile or custom app via the Dynatrace API.")',
        'Получить параметры свойства сессии по его ID.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-property "Просмотр свойства пользовательской сессии мобильного или пользовательского приложения через Dynatrace API.")',
    ),
    (
        'Create a new user session property for your mobile or custom app.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/post-property "Create user session property a mobile or custom app via the Dynatrace API.")[### Edit a user session property',
        'Создать новое свойство пользовательской сессии для вашего мобильного или пользовательского приложения.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/post-property "Создание свойства пользовательской сессии мобильного или пользовательского приложения через Dynatrace API.")[### Редактирование свойства пользовательской сессии',
    ),
    (
        'Update an existing user session property for your mobile or custom app.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/put-property "Update user session property a mobile or custom app via the Dynatrace API.")[### Delete a user session property',
        'Обновить существующее свойство пользовательской сессии для вашего мобильного или пользовательского приложения.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/put-property "Обновление свойства пользовательской сессии мобильного или пользовательского приложения через Dynatrace API.")[### Удаление свойства пользовательской сессии',
    ),
    (
        'Delete a user session property you don\'t need anymore.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/delete-property "Delete user session property a mobile or custom app via the Dynatrace API.")',
        'Удалить ненужное свойство пользовательской сессии.](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/delete-property "Удаление свойства пользовательской сессии мобильного или пользовательского приложения через Dynatrace API.")',
    ),
    # heading-only lines (longest-first to avoid `[### List all` collision)
    (
        "[### List all user session properties",
        "[### Список всех свойств пользовательских сессий",
    ),
    ("[### List all apps", "[### Список всех приложений"),
    ("[### View key user actions", "[### Просмотр ключевых пользовательских действий"),
    (
        "[### Create a user session property",
        "[### Создание свойства пользовательской сессии",
    ),
    ("[### Create an app", "[### Создание приложения"),
]

# ---- apps/get-all ----
P["mobile-custom-app-configuration/apps/get-all.md"] = [
    (
        "Lists all mobile and custom apps configured in your Dynatrace environment.",
        "Перечисляет все мобильные и пользовательские приложения, настроенные в вашем окружении Dynatrace.",
    ),
]

# ---- apps/get-app ----
P["mobile-custom-app-configuration/apps/get-app.md"] = [
    (
        "Gets parameters of the specified mobile or custom app.",
        "Возвращает параметры указанного мобильного или пользовательского приложения.",
    ),
]

# ---- apps/post-app ----
P["mobile-custom-app-configuration/apps/post-app.md"] = [
    (
        "Creates a new mobile or custom app.",
        "Создаёт новое мобильное или пользовательское приложение.",
    ),
    (
        "| body | [NewMobileCustomAppConfig](#openapi-definition-NewMobileCustomAppConfig) | The JSON body of the request. Contains the parameters of the new mobile or custom application. | body | Optional |",
        "| body | [NewMobileCustomAppConfig](#openapi-definition-NewMobileCustomAppConfig) | JSON-тело запроса. Содержит параметры нового мобильного или пользовательского приложения. | body | Optional |",
    ),
]

# ---- apps/put-app ----
P["mobile-custom-app-configuration/apps/put-app.md"] = [
    (
        "Updates the specified mobile or custom app.",
        "Обновляет указанное мобильное или пользовательское приложение.",
    ),
    (
        "| body | [MobileCustomAppConfig](#openapi-definition-MobileCustomAppConfig) | The JSON body of the request. Contains updated configuration of the mobile or custom application.  Do not set the identifier in the body. | body | Optional |",
        "| body | [MobileCustomAppConfig](#openapi-definition-MobileCustomAppConfig) | JSON-тело запроса. Содержит обновлённую конфигурацию мобильного или пользовательского приложения.  Не указывайте identifier в теле. | body | Optional |",
    ),
]

# ---- apps/delete-app ----
P["mobile-custom-app-configuration/apps/delete-app.md"] = [
    (
        "Deletes the specified mobile or custom app.",
        "Удаляет указанное мобильное или пользовательское приложение.",
    ),
    (
        '* [Delete a mobile application](/managed/observe/digital-experience/mobile-applications/additional-configuration/delete-application-mobile "Delete your mobile applications via the Dynatrace web UI or API.")',
        '* [Удаление мобильного приложения](/managed/observe/digital-experience/mobile-applications/additional-configuration/delete-application-mobile "Удаление мобильных приложений через веб-интерфейс Dynatrace или API.")',
    ),
    (
        '* [Delete a custom application](/managed/observe/digital-experience/custom-applications/additional-configuration/delete-application-custom "Delete your custom applications via the Dynatrace web UI or API.")',
        '* [Удаление пользовательского приложения](/managed/observe/digital-experience/custom-applications/additional-configuration/delete-application-custom "Удаление пользовательских приложений через веб-интерфейс Dynatrace или API.")',
    ),
]

# ---- key-user-actions/get-configuration ----
P["mobile-custom-app-configuration/key-user-actions/get-configuration.md"] = [
    (
        "Gets the list of the key user actions in the specified app.",
        "Возвращает список ключевых пользовательских действий в указанном приложении.",
    ),
    (
        '* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")',
        '* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")',
    ),
]

# ---- key-user-actions/post-configuration ----
P["mobile-custom-app-configuration/key-user-actions/post-configuration.md"] = [
    (
        "Adds a user action to the list of key user actions in the specified app.",
        "Добавляет пользовательское действие в список ключевых пользовательских действий в указанном приложении.",
    ),
    (
        "| actionName | string | The name of the user action to be marked as a key user action. | path | Required |",
        "| actionName | string | Имя пользовательского действия, отмечаемого как ключевое пользовательское действие. | path | Required |",
    ),
    (
        '* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")',
        '* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")',
    ),
]

# ---- key-user-actions/del-configuration ----
P["mobile-custom-app-configuration/key-user-actions/del-configuration.md"] = [
    (
        "Removes a user action from the list of key user actions in the specified app.",
        "Удаляет пользовательское действие из списка ключевых пользовательских действий в указанном приложении.",
    ),
    (
        "| actionName | string | The ID of the user action to be removed from the key user actions list. | path | Required |",
        "| actionName | string | ID пользовательского действия, удаляемого из списка ключевых пользовательских действий. | path | Required |",
    ),
    (
        '* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")',
        '* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")',
    ),
]

# ---- user-action-and-session-properties/get-all ----
P["mobile-custom-app-configuration/user-action-and-session-properties/get-all.md"] = [
    (
        "Lists all user session and user action properties from the specified mobile or custom app.",
        "Перечисляет все свойства пользовательских сессий и пользовательских действий из указанного мобильного или пользовательского приложения.",
    ),
]

# ---- user-action-and-session-properties/get-property ----
P[
    "mobile-custom-app-configuration/user-action-and-session-properties/get-property.md"
] = [
    (
        "Gets the parameters of the specified user session property of an app.",
        "Возвращает параметры указанного свойства пользовательской сессии приложения.",
    ),
]

# ---- user-action-and-session-properties/post-property ----
P[
    "mobile-custom-app-configuration/user-action-and-session-properties/post-property.md"
] = [
    (
        "Creates a new user session property in the specified application.",
        "Создаёт новое свойство пользовательской сессии в указанном приложении.",
    ),
    (
        "| body | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | The JSON body of the request. Contains the configuration of the property. | body | Optional |",
        "| body | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | JSON-тело запроса. Содержит конфигурацию свойства. | body | Optional |",
    ),
]

# ---- user-action-and-session-properties/put-property ----
P[
    "mobile-custom-app-configuration/user-action-and-session-properties/put-property.md"
] = [
    (
        "Updates the specified user session property in an application.",
        "Обновляет указанное свойство пользовательской сессии в приложении.",
    ),
    (
        "If the session property with the specified ID does not exist, a new session property is created.",
        "Если свойство сессии с указанным ID не существует, создаётся новое свойство сессии.",
    ),
    (
        "| body | [MobileSessionUserActionPropertyUpd](#openapi-definition-MobileSessionUserActionPropertyUpd) | The JSON body of the request. Contains the configuration of the property. | body | Optional |",
        "| body | [MobileSessionUserActionPropertyUpd](#openapi-definition-MobileSessionUserActionPropertyUpd) | JSON-тело запроса. Содержит конфигурацию свойства. | body | Optional |",
    ),
]

# ---- user-action-and-session-properties/delete-property ----
P[
    "mobile-custom-app-configuration/user-action-and-session-properties/delete-property.md"
] = [
    (
        "Deletes the specified user session property from an app.",
        "Удаляет указанное свойство пользовательской сессии из приложения.",
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
