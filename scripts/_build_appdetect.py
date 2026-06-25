#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splice-builder for batch L4T: configuration-api/rum/application-detection-configuration/
parent + 8 endpoints (del-rule / get-all / get-host-detection-config / get-rule /
post-rule / put-host-detection-config / put-rule / reorder-rules) = 9 files.

ACTIVE API, no deprecated banner (L89/L90). Continues the rum/ subsection L4S
started. EN -> RU exact-string replacement only (no newline added/removed) =>
line-parity automatic, code-fence byte-identical (L98/L100). EN is CRLF =>
normalize to LF first (L4M lesson), strip leading BOM.

Canon anchor = FRESHEST same-subsection twin (L4S rum content-resources RU +
L4R aws-privatelink RU), NOT old conditional-naming L2R (pre-L99 canon
"Элемент может принимать"/"Ошибка. Входные данные некорректны" — L4S lesson:
anchor свежайший twin того же вида). Example-section canon from reports-api L4I /
alerting-profiles post-profile L4J (`## Пример`/`#### URL запроса`/`#### Тело
запроса`/`#### Тело ответа`/`#### Код ответа`/`#### Результат`; `#### Curl`/`##
Validate payload` EN; image alt+caption EN L4D). Shared Error/ErrorEnvelope/
ConstraintViolation/ConfigurationMetadata/EntityShortRepresentation/StubList
from plugins-api L4N / content-resources L4S RU verbatim. L101: period-by-source
via substring `Failed. The input is invalid` (period stays outside match — all
app-detect 400 = WITH period). validate-204: post/put-rule EN "Validated." ->
"Validated."-prefix kept (L4I); put-host-detection EN "Success." -> "Успех.".
Domain: "application detection rule" -> "правило обнаружения приложений"
(corpus-confirmed: target RU H1 "Проверка правил обнаружения приложений");
feature-name `**Applications detection rules**` EN-bold-lock (L4S). Related-
topics link-text = target RU H1 verbatim (L4O/L4L): rum-overview ->
"Мониторинг реальных пользователей", application-detection-rules -> "Проверка
правил обнаружения приложений", define-your-applications -> "Определение
приложений для Real User Monitoring"; title-attr reused from established corpus.
BOM `\xef\xbb\xbf` (3-char, L4M) stripped from `[create an application first]`.
Source-quirks L93 verbatim-by-meaning: "the the **pattern**" double-the,
"host detection headers configuration" double-noun.
"""

import os, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
SUB = r"docs\managed\dynatrace-api\configuration-api\rum"
SUBR = r"docs\managed-ru\dynatrace-api\configuration-api\rum"
EN = os.path.join(ROOT, SUB)
RU = os.path.join(ROOT, SUBR)

FILES = [
    "application-detection-configuration.md",
    "application-detection-configuration/del-rule.md",
    "application-detection-configuration/get-all.md",
    "application-detection-configuration/get-host-detection-config.md",
    "application-detection-configuration/get-rule.md",
    "application-detection-configuration/post-rule.md",
    "application-detection-configuration/put-host-detection-config.md",
    "application-detection-configuration/put-rule.md",
    "application-detection-configuration/reorder-rules.md",
]

# ---------------------------------------------------------------- COMMON
# Applied AFTER per-file. Each entry within-line (or newline-anchored full
# line) => line-parity preserved. Ordered longest/most-specific first.
COMMON = [
    # --- structural headers (newline-anchored) ---
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
    ("\n## Example\n", "\n## Пример\n"),
    ("\n#### Request URL\n", "\n#### URL запроса\n"),
    ("\n#### Request body\n", "\n#### Тело запроса\n"),
    ("\n#### Response body\n", "\n#### Тело ответа\n"),
    ("\n#### Response code\n", "\n#### Код ответа\n"),
    ("\n#### Result\n", "\n#### Результат\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # `## Validate payload` / `#### Curl` => EN-verbatim (L99 ALLOWED_EN, L4S)
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
    # --- object headers ---
    (
        "#### The `ApplicationDetectionRulesHostDetectionSettings` object",
        "#### Объект `ApplicationDetectionRulesHostDetectionSettings`",
    ),
    (
        "#### The `ApplicationDetectionRuleConfig` object",
        "#### Объект `ApplicationDetectionRuleConfig`",
    ),
    (
        "#### The `ConfigurationMetadataDtoImpl` object",
        "#### Объект `ConfigurationMetadataDtoImpl`",
    ),
    (
        "#### The `ConfigurationMetadata` object",
        "#### Объект `ConfigurationMetadata`",
    ),
    ("#### The `ApplicationFilter` object", "#### Объект `ApplicationFilter`"),
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
        "The request produces an `application/json` payload.",
        "Запрос возвращает payload `application/json`.",
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
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.",
    ),
    (
        "The API token is passed in the **Authorization** header.",
        "API-токен передаётся в заголовке **Authorization**.",
    ),
    (
        "The request body is truncated in the **Curl** section. See the **Request body** section for the full body. You can download or copy the example request body to try it out on your own. Be sure to use an application ID that is available in your environment.",
        "Тело запроса усечено в разделе **Curl**. Полное тело смотрите в разделе **Request body**. Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно используйте ID приложения, доступного в вашем окружении.",
    ),
    # --- shared applicationIdentifier cell (BOM-strip; identical get/post/put-rule)
    (
        "The Dynatrace entity ID of the application, for example `APPLICATION-4A3B43`.  You must use an existing ID. If you need to create a rule for an application that doesn't exist yet, [create an application first\xef\xbb\xbf](https://dt-url.net/vt03khh) and then configure detection rules for it.",
        "ID сущности Dynatrace для приложения, например `APPLICATION-4A3B43`.  Нужно использовать существующий ID. Если нужно создать правило для ещё не существующего приложения, [сначала создайте приложение](https://dt-url.net/vt03khh), а затем настройте для него правила обнаружения.",
    ),
    # --- shared object descriptions / cells ---
    (
        "An ordered list of host detection headers.  Headers are evaluated from top to bottom; the first matching header applies.",
        "Упорядоченный список заголовков определения хоста.  Заголовки оцениваются сверху вниз; применяется первый подходящий заголовок.",
    ),
    (
        "Configuration of host detection headers.",
        "Конфигурация заголовков определения хоста.",
    ),
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
    # longest-first: "The unique name of the Application detection rule."
    # MUST precede the standalone "Application detection rule." (L4N/L4P
    # substring-collision lesson — else RU+EN hybrid leftover)
    (
        "The unique name of the Application detection rule.",
        "Уникальное имя правила обнаружения приложений.",
    ),
    (
        "The condition of an application detection rule.",
        "Условие правила обнаружения приложений.",
    ),
    (
        "The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies.",
        "Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое подходящее правило.",
    ),
    ("Application detection rule.", "Правило обнаружения приложений."),
    ("| The ID of the rule. |", "| ID правила. |"),
    (
        "Where to look for the the **pattern** value.",
        "Где искать значение **pattern**.",
    ),
    ("The operator of the matching.", "Оператор сопоставления."),
    ("The value to look for.", "Значение для поиска."),
    # --- response-code cells (L101: period stays outside the matched span) ---
    (
        "Success. The configuration has been updated. Response doesn't have a body.",
        "Успех. Конфигурация обновлена. Ответ без тела.",
    ),
    (
        "Success. The submitted configuration is valid. Response doesn't have a body.",
        "Успех. Переданная конфигурация валидна. Ответ без тела.",
    ),
    (
        "Validated. The submitted configuration is valid. Response doesn't have a body.",
        "Validated. Переданная конфигурация валидна. Ответ без тела.",
    ),
    (
        "Success. The application detection rule has been created. Response contains the ID of the new rule.",
        "Успех. Правило обнаружения приложений создано. Ответ содержит ID нового правила.",
    ),
    (
        "Success. Application detection rule has been created. Response contains the ID of the new rule.",
        "Успех. Правило обнаружения приложений создано. Ответ содержит ID нового правила.",
    ),
    (
        "Success. Application detection rule has been updated. Response doesn't have a body.",
        "Успех. Правило обнаружения приложений обновлено. Ответ без тела.",
    ),
    (
        "Success. Application detection rules have been reordered. Response doesn't have a body.",
        "Успех. Порядок правил обнаружения приложений изменён. Ответ без тела.",
    ),
    ("Deleted. Response doesn't have a body.", "Удалено. Ответ без тела."),
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    ("| Success |", "| Успех |"),
    # --- "The element can hold these values" -> "Возможные значения:" WITH
    #     colon (L99; also handles leading-dash `-The element ...`) ---
    ("The element can hold these values", "Возможные значения:"),
    # --- shared Error / ConstraintViolation / ConfigurationMetadata canon
    #     (verbatim from plugins-api L4N / content-resources L4S RU) ---
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
    ("| Dynatrace version. |", "| Версия Dynatrace. |"),
    (
        "A sorted list of the version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    (
        "A sorted list of version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    ("Metadata useful for debugging", "Метаданные для отладки"),
    # ConstraintViolation object-intro line (standalone)
    ("\nA list of constraint violations\n", "\nСписок нарушений ограничений\n"),
    # --- Related-topics bullets (link-text = target RU H1 verbatim L4O/L4L;
    #     title-attr reused from established corpus) ---
    (
        '* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")',
        '* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")',
    ),
    (
        '* [Check application detection rules](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")',
        '* [Проверка правил обнаружения приложений](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Легко разберитесь в правилах обнаружения вашего RUM-приложения.")',
    ),
    (
        '* [Define applications for Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")',
        '* [Определение приложений для Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определять приложения с использованием предложенного, ручного подхода или правил обнаружения приложений.")',
    ),
]

# ---------------------------------------------------------------- PER-FILE
P = {}

# ---- parent ----
P["application-detection-configuration.md"] = [
    (
        "The **Applications detection rules** API enables you to manage the application detection rules.",
        "API **Applications detection rules** позволяет управлять правилами обнаружения приложений.",
    ),
    (
        'Get an overview of all application detection rules.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-all "View all application detection rules via the Dynatrace API.")[### View a rule',
        'Обзор всех правил обнаружения приложений.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-all "Просмотр всех правил обнаружения приложений через Dynatrace API.")[### Просмотр правила',
    ),
    (
        'Get parameters of an application detection rule by its ID.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-rule "View an application detection rule via the Dynatrace API.")[### Reorder rules',
        'Получить параметры правила обнаружения приложений по его ID.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-rule "Просмотр правила обнаружения приложений через Dynatrace API.")[### Изменение порядка правил',
    ),
    (
        "Application detection rules are evaluated one after another. The first matching rule is applied, and further processing stops.",
        "Правила обнаружения приложений оцениваются одно за другим. Применяется первое подходящее правило, дальнейшая обработка прекращается.",
    ),
    (
        'Reorder application detection rules to achieve the order of evaluation you need.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules "Reorder application detection rules via the Dynatrace API.")[### Create a rule',
        'Измените порядок правил обнаружения приложений, чтобы получить нужный порядок их оценки.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules "Изменение порядка правил обнаружения приложений через Dynatrace API.")[### Создание правила',
    ),
    (
        'Create a new rule with the exact parameters you need.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule "Create an application detection rule via the Dynatrace API.")[### Edit a rule',
        'Создать новое правило с точно нужными параметрами.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule "Создание правила обнаружения приложений через Dynatrace API.")[### Редактирование правила',
    ),
    (
        'Update an existing application detection rule or create a new rule with the specified ID.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-rule "Edit an application detection rule via the Dynatrace API.")[### Delete a rule',
        'Обновить существующее правило обнаружения приложений или создать новое правило с указанным ID.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-rule "Редактирование правила обнаружения приложений через Dynatrace API.")[### Удаление правила',
    ),
    (
        'Delete a rule you don\'t need anymore.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/del-rule "Delete an application detection rule via the Dynatrace API.")',
        'Удалить ненужное правило.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/del-rule "Удаление правила обнаружения приложений через Dynatrace API.")',
    ),
    (
        'Get an overview of host detection headers configuration.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-host-detection-config "Read the configuration of host detection headers via the Dynatrace API.")[### Update host detection headers',
        'Обзор конфигурации заголовков определения хоста.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-host-detection-config "Просмотр конфигурации заголовков определения хоста через Dynatrace API.")[### Обновление заголовков определения хоста',
    ),
    (
        'Update configuration of host detection headers configuration.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-host-detection-config "Update the configuration of host detection headers via the Dynatrace API.")',
        'Обновление конфигурации заголовков определения хоста.](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-host-detection-config "Обновление конфигурации заголовков определения хоста через Dynatrace API.")',
    ),
    ("[### List all", "[### Список всех правил"),
    ("[### View host detection headers", "[### Просмотр заголовков определения хоста"),
]

# ---- del-rule ----
P["application-detection-configuration/del-rule.md"] = [
    (
        "Deletes the specified application detection rule.",
        "Удаляет указанное правило обнаружения приложений.",
    ),
    (
        "| id | string | The ID of the application detection rule to be deleted. | path | Required |",
        "| id | string | ID удаляемого правила обнаружения приложений. | path | Required |",
    ),
    (
        'In this example, the request deletes the application detection rule from the [POST request example](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Create an application detection rule via the Dynatrace API."). The response code of **204** indicates that the deletion was successful.',
        'В этом примере запрос удаляет правило обнаружения приложений из примера [POST request](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Создание правила обнаружения приложений через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.',
    ),
]

# ---- get-all ----
P["application-detection-configuration/get-all.md"] = [
    (
        "Lists all application detection rules available in your Dynatrace environment.",
        "Перечисляет все правила обнаружения приложений, доступные в вашем окружении Dynatrace.",
    ),
    (
        "In this example, the request gets a list of application detection rules in the **mySampleEnv** environment.",
        "В этом примере запрос получает список правил обнаружения приложений в окружении **mySampleEnv**.",
    ),
    ("The result is truncated to three entries.", "Результат усечён до трёх записей."),
]

# ---- get-host-detection-config ----
P["application-detection-configuration/get-host-detection-config.md"] = [
    (
        "Gets the list of the host detection headers.",
        "Возвращает список заголовков определения хоста.",
    ),
]

# ---- get-rule ----
P["application-detection-configuration/get-rule.md"] = [
    (
        "Gets parameters of the specified application detection rule.",
        "Возвращает параметры указанного правила обнаружения приложений.",
    ),
    (
        "| id | string | The ID of the required application detection rule. | path | Required |",
        "| id | string | ID нужного правила обнаружения приложений. | path | Required |",
    ),
    (
        "In this example, the request gets the properties of the **easyTravel** rule, which has the ID **95b22afb-4e3d-4f9f-a37d-81bc3d388a33**.",
        "В этом примере запрос получает свойства правила **easyTravel** с ID **95b22afb-4e3d-4f9f-a37d-81bc3d388a33**.",
    ),
]

# ---- post-rule ----
P["application-detection-configuration/post-rule.md"] = [
    (
        'Creates a new application detection rule and adds it to the end of the rules list. To enforce a particular order, use the [PUT reorder rules](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules "Reorder application detection rules via the Dynatrace API.") request.',
        'Создаёт новое правило обнаружения приложений и добавляет его в конец списка правил. Чтобы задать определённый порядок, используйте запрос [PUT reorder rules](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules "Изменение порядка правил обнаружения приложений через Dynatrace API.").',
    ),
    (
        'You can create detection rules only for an existing application. If you need to create a rule for an application that doesn\'t exist yet, [create an application first](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.") and then configure detection rules for it.',
        'Правила обнаружения можно создавать только для существующего приложения. Если нужно создать правило для ещё не существующего приложения, [сначала создайте приложение](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Создание веб-приложения через Dynatrace API.") и затем настройте для него правила обнаружения.',
    ),
    (
        "The body must not provide an ID. An ID is assigned automatically by Dynatrace.",
        "В теле не должен передаваться ID. ID назначается Dynatrace автоматически.",
    ),
    (
        "The position of the new rule:  * `APPEND`: at the bottom of the rule list. * `PREPEND`: at the top of the rule list.  If not set, the `APPEND` is used.",
        "Позиция нового правила:  * `APPEND`: в конце списка правил. * `PREPEND`: в начале списка правил.  Если не задано, используется `APPEND`.",
    ),
    (
        "The JSON body of the request. Contains configuration of the new application detection rule.  You must not specify the ID of the rule.  The **order** field is ignored in this request. To enforce a particular order use the `PUT /applicationDetectionRules/order` request.",
        "JSON-тело запроса. Содержит конфигурацию нового правила обнаружения приложений.  Не указывайте ID правила.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /applicationDetectionRules/order`.",
    ),
    (
        "In this example, the request creates a new application detection rule for the **BookingApp** application that has the ID of **APPLICATION-900C1E36674F607D**.",
        "В этом примере запрос создаёт новое правило обнаружения приложений для приложения **BookingApp** с ID **APPLICATION-900C1E36674F607D**.",
    ),
    (
        "The new application detection rule looks like this in the UI:",
        "Новое правило обнаружения приложений выглядит в UI так:",
    ),
]

# ---- put-host-detection-config ----
P["application-detection-configuration/put-host-detection-config.md"] = [
    (
        "Updates the list of the host detection headers.",
        "Обновляет список заголовков определения хоста.",
    ),
    (
        "The JSON body of the request. Contains the configuration of host detection headers.",
        "JSON-тело запроса. Содержит конфигурацию заголовков определения хоста.",
    ),
]

# ---- put-rule ----
P["application-detection-configuration/put-rule.md"] = [
    (
        "Updates the specified application detection rule.",
        "Обновляет указанное правило обнаружения приложений.",
    ),
    (
        "If the application detection rule with the specified ID doesn't exist, a new rule is created and appended to the end of the rule list.",
        "Если правило обнаружения приложений с указанным ID не существует, создаётся новое правило и добавляется в конец списка правил.",
    ),
    (
        "If the order parameter is set for an existing rule, the request uses this value. Otherwise, it keeps the existing order of rules.",
        "Если для существующего правила задан параметр order, запрос использует это значение. Иначе сохраняется текущий порядок правил.",
    ),
    (
        "| id | string | The ID of the application detection rule to be updated.  If you set the ID in the body as well, it must match this ID. | path | Required |",
        "| id | string | ID обновляемого правила обнаружения приложений.  Если ID указан также в теле, он должен совпадать с этим ID. | path | Required |",
    ),
    (
        "The JSON body of the request. Contains updated parameters of the application detection rule.  If the **order** parameter is set, the rule is placed to this position.",
        "JSON-тело запроса. Содержит обновлённые параметры правила обнаружения приложений.  Если задан параметр **order**, правило помещается на эту позицию.",
    ),
    (
        'In this example, the request updates the application detection rule from the [POST request example](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Create an application detection rule via the Dynatrace API."). It changes the **order** of the rule to position **two** and changes the condition of the rule to the **domain** that **contains** the **booking.easyTravel** pattern.',
        'В этом примере запрос обновляет правило обнаружения приложений из примера [POST request](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Создание правила обнаружения приложений через Dynatrace API."). Он меняет **order** правила на позицию **two** и меняет условие правила на **domain**, который **contains** шаблон **booking.easyTravel**.',
    ),
]

# ---- reorder-rules ----
P["application-detection-configuration/reorder-rules.md"] = [
    (
        "Application detection rules are evaluated from top to bottom, the first matching rule applies.",
        "Правила обнаружения приложений оцениваются сверху вниз, применяется первое подходящее правило.",
    ),
    (
        "This request reorders the application detection rules according to the order of the IDs in the body of the request. Rules that are omitted in the body of the request will retain their relative order but will be placed **after** all those present in the request.",
        "Этот запрос меняет порядок правил обнаружения приложений в соответствии с порядком ID в теле запроса. Правила, опущенные в теле запроса, сохранят свой относительный порядок, но будут размещены **после** всех присутствующих в запросе.",
    ),
    (
        "The JSON body of the request. Contains the IDs of the application detection rules in the desired order. Any further properties (**name**, **description**) are ignored.",
        "JSON-тело запроса. Содержит ID правил обнаружения приложений в нужном порядке. Любые другие свойства (**name**, **description**) игнорируются.",
    ),
    (
        'In this example, the request reorders the detection rules from [GET all rules request example](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-all#example "View all application detection rules via the Dynatrace API."), enforcing the following order:',
        'В этом примере запрос меняет порядок правил обнаружения из примера [GET all rules request](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-all#example "Просмотр всех правил обнаружения приложений через Dynatrace API."), задавая следующий порядок:',
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
