# -*- coding: utf-8 -*-
"""L4-AA builder: configuration-api/service-api/ partial = 14 files
request-attributes-api/ (6: parent + del/get-all/get-request-attribute/post/put)
+ request-naming-api/ (8: parent + create-use-case/delete/get-a-rule/get-all/
json-models/post-new-rule/put-a-rule). Two self-contained sub-subsections of
service-api/ closed 100%. ~3.7K EN lines, strong post<->put twins (RA 95%,
RN 96% identical) + json-models = canonical ComparisonInfo-variations (L4X
service-metrics twin). Continuation of config-api L4-era after L4X.

Splice method (L98/L100/L4X _build_servicemetrics): start from EN, CRLF->LF,
mojibake-normalize (L4W: e2+C1+C1 double-encoded -> ASCII via codepoints),
strip BOM (L4M), apply ordered exact-string canon -> byte-identical JSON +
line parity. Anything unreplaced stays EN-verbatim (object/enum/JSON/**bold**/
API-name, L99). Twin handled implicitly: identical EN shared strings get the
identical RU via the shared R-table.

ORDERING (L4T longest-first / embedding-anchor): TIER-0 = full sentences that
EMBED a link+title-attr (parent intro / post-new-rule intro / use-case link
steps) run FIRST with ORIGINAL-EN nested title-attrs, so a later standalone
(A) title-attr replacement cannot corrupt the embedding anchor (root cause of
L4-AA review-iter-1 SUSPECT-EN x13 in create-a-new-request-naming-rule).
Then (A) standalone title-attrs, (B) link-text, ... , (Z) global last.

ACTIVE API (no deprecated banner, * Reference / * Published EN-verbatim,
L89/L90). title/H1x2 EN-verbatim (L99). anchor = SAME-subsection-family newest
config-api RU = L4X calculated-metrics/service-metrics RU (shared Condition/
ComparisonInfo/Placeholder/PropagationSource/UniversalTag/TagInfo-short/
ConfigurationMetadata/EntityShortRepresentation/StubList/Error/ErrorEnvelope/
ConstraintViolation + all *ComparisonInfo/*Dto variation objects BYTE-IDENTICAL
EN -> reuse L4X (en,ru) pairs verbatim) + k8s/config shared (L4M/L4U).
json-models STRUCTURE = conditional-naming L3G (Variations intro / Refer-to-
JSON / type-headings EN / Parameters|JSON model tab-labels EN) BUT
"Возможные значения:" + EN-locks = L4O/L99 (NOT L3G "Элемент может принимать").
Related-topics link-text = target RU H1 verbatim (L4O/L4L: "Атрибуты запросов"/
"Настройка именования запросов"/"Определение пользовательских сервисов"),
title-attr translated. post-new-rule intro topic link-text = EN endpoint-name
(L4T), title-attr translated. L101: 400 "Failed. The input is invalid."
period BY SOURCE — ALL 14 files WITH period (grep-verified single form) ->
RU "Сбой. Невалидный ввод" + substring keeps source period. bare
"| Success |"->"| Успех |" (L4W/L4X). "Validated."-prefix EN-cell (L4I).
NO em-dash in RU (CLAUDE#0): position/argumentIndex rephrased w/o '—'.
create-a-new-request-naming-rule = use-case narrative (REST client / Dynatrace
API Explorer tab labels translated, numbered steps + image alt translated,
dt-cdn URLs verbatim, code fences force-synced)."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
SA = "service-api"
RA = f"{SA}/request-attributes-api"
RN = f"{SA}/request-naming-api"

FILES = [
    f"{RA}.md",
    f"{RA}/del-request-attribute.md",
    f"{RA}/get-all.md",
    f"{RA}/get-request-attribute.md",
    f"{RA}/post-request-attribute.md",
    f"{RA}/put-request-attribute.md",
    f"{RN}.md",
    f"{RN}/create-a-new-request-naming-rule.md",
    f"{RN}/delete-a-rule.md",
    f"{RN}/get-a-rule.md",
    f"{RN}/get-all.md",
    f"{RN}/json-models.md",
    f"{RN}/post-new-rule.md",
    f"{RN}/put-a-rule.md",
]

R = [
    # ========== TIER-0: embedding sentences (link+title-attr) — FIRST ==========
    # (parent intros / post-new-rule intro / use-case link steps; nested
    #  title-attrs in ORIGINAL EN so a later (A) cannot pre-corrupt the anchor)
    (
        'The **Request attributes** API enables you to manage the configuration of [request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").',
        'API **Request attributes** позволяет управлять конфигурацией [атрибутов запросов](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и как использовать их на всех уровнях всех представлений анализа сервисов.").',
    ),
    (
        'Creates a new request naming rule. See the detailed use case in the [Request naming API - Create a new rule](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Learn how to create a request naming rule via the Dynatrace API.") topic.',
        'Создаёт новое правило именования запросов. Подробный сценарий использования смотрите в разделе [Request naming API - Create a new rule](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Узнайте, как создать правило именования запросов через Dynatrace API.").',
    ),
    (
        'You can find descriptions of other fields in the **Parameters** section of the [**POST a new request naming rule** topic](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Create a request naming rule via the Dynatrace API.").',
        'Описания других полей смотрите в разделе **Parameters** темы [**POST a new request naming rule**](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Создание правила именования запросов через Dynatrace API.").',
    ),
    (
        'Now let\'s submit this configuration in an API call. How you execute REST calls is up to you-you can use any REST client or you can write a script like the one provided below. You can also use the Dynatrace [API Explorer](/managed/dynatrace-api#api-explorer "Find out what you need to use the Dynatrace API.") to familiarize yourself with endpoints and execute all the required requests.',
        'Теперь отправим эту конфигурацию в API-вызове. Способ выполнения REST-вызовов на ваше усмотрение: можно использовать любой REST-клиент или написать скрипт вроде приведённого ниже. Также можно использовать [API Explorer](/managed/dynatrace-api#api-explorer "Узнайте, что нужно для использования Dynatrace API.") Dynatrace, чтобы ознакомиться с эндпоинтами и выполнить все необходимые запросы.',
    ),
    (
        '1. Generate a new [access token for the Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API."). Be sure to assign **Read configuration** and **Write configuration** scopes to it.',
        '1. Сгенерируйте новый [токен доступа для Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API."). Обязательно назначьте ему scope **Read configuration** и **Write configuration**.',
    ),
    (
        '2. Execute the [**POST a new request naming rule** request](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Create a request naming rule via the Dynatrace API.") with the token you created in the first step and the JSON configuration of the request naming rule from an example above as a payload.',
        '2. Выполните запрос [**POST a new request naming rule**](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Создание правила именования запросов через Dynatrace API.") с токеном, созданным на первом шаге, и JSON-конфигурацией правила именования запросов из примера выше в качестве payload.',
    ),
    (
        '2. Open the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Navigate the Dynatrace Managed platform") from the previous Dynatrace web UI, and select **Dynatrace API > Configuration API**.',
        '2. Откройте [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Навигация по платформе Dynatrace Managed") в прежнем веб-интерфейсе Dynatrace и выберите **Dynatrace API > Configuration API**.',
    ),
    (
        "The **Request naming** API enables you to manage the configuration of request naming rules.",
        "API **Request naming** позволяет управлять конфигурацией правил именования запросов.",
    ),
    # ---------- (A) standalone Related/card title-attrs ----------
    (
        "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.",
        "Узнайте, что такое атрибуты запросов, и как использовать их на всех уровнях всех представлений анализа сервисов.",
    ),
    (
        "Adjust request naming and define the operations your services offer.",
        "Настройте именование запросов и определите операции, предоставляемые вашими сервисами.",
    ),
    (
        "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.",
        "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.",
    ),
    (
        "Learn how to create a request naming rule via the Dynatrace API.",
        "Узнайте, как создать правило именования запросов через Dynatrace API.",
    ),
    (
        "Find out what you need to use the Dynatrace API.",
        "Узнайте, что нужно для использования Dynatrace API.",
    ),
    (
        "Find out how to get authenticated to use the Dynatrace API.",
        "Узнайте, как пройти аутентификацию для использования Dynatrace API.",
    ),
    (
        "Navigate the Dynatrace Managed platform",
        "Навигация по платформе Dynatrace Managed",
    ),
    # ---------- (B) Related-topics link-text (= target RU H1; L4O/L4L) ----------
    ("[Request attributes](/managed/observe", "[Атрибуты запросов](/managed/observe"),
    ("[Set up request naming]", "[Настройка именования запросов]"),
    ("[Define custom services]", "[Определение пользовательских сервисов]"),
    # ---------- (C) parent card descriptions + group headings ----------
    (
        "Get an overview of all request attributes.",
        "Обзор всех атрибутов запросов.",
    ),
    (
        "Get parameters of a request attribute by its ID.",
        "Получить параметры атрибута запроса по его ID.",
    ),
    (
        "Create a new request attribute with the exact parameters you need.",
        "Создать новый атрибут запроса с нужными вам параметрами.",
    ),
    (
        "Update an existing request attribute or create a new request attribute with the specified ID.",
        "Обновить существующий атрибут запроса или создать новый атрибут запроса с указанным ID.",
    ),
    (
        "Delete a request attribute you don't need anymore.",
        "Удалить атрибут запроса, который вам больше не нужен.",
    ),
    ("### List all\n", "### Список всех\n"),
    ("### View a request attribute\n", "### Просмотр атрибута запроса\n"),
    ("### Create a request attribute\n", "### Создание атрибута запроса\n"),
    ("### Edit a request attribute\n", "### Редактирование атрибута запроса\n"),
    ("### Delete a request attribute\n", "### Удаление атрибута запроса\n"),
    (
        "Get an overview of all request naming rules defined in your environment.",
        "Обзор всех правил именования запросов, определённых в вашем окружении.",
    ),
    (
        "Get parameters of a request naming rule by its ID.",
        "Получить параметры правила именования запросов по его ID.",
    ),
    (
        "Create a new request naming rule with the exact parameters you need.",
        "Создать новое правило именования запросов с нужными вам параметрами.",
    ),
    (
        "Update a request naming rule. You can also create a new rule with the specified ID.",
        "Обновить правило именования запросов. Также можно создать новое правило с указанным ID.",
    ),
    (
        "Delete a request naming rule you don't need anymore.",
        "Удалить правило именования запросов, которое вам больше не нужно.",
    ),
    ("### List all rules\n", "### Список всех правил\n"),
    ("### View a rule\n", "### Просмотр правила\n"),
    ("### Create a rule\n", "### Создание правила\n"),
    ("### Edit a rule\n", "### Редактирование правила\n"),
    ("### Delete a rule\n", "### Удаление правила\n"),
    (
        "View all request attributes of your environment via the Dynatrace API.",
        "Просмотр всех атрибутов запросов вашего окружения через Dynatrace API.",
    ),
    (
        "View a request attribute via the Dynatrace API.",
        "Просмотр атрибута запроса через Dynatrace API.",
    ),
    (
        "Create a request attribute via the Dynatrace API.",
        "Создание атрибута запроса через Dynatrace API.",
    ),
    (
        "Update a request attribute via the Dynatrace API.",
        "Обновление атрибута запроса через Dynatrace API.",
    ),
    (
        "Delete a request attribute via the Dynatrace API.",
        "Удаление атрибута запроса через Dynatrace API.",
    ),
    (
        "View all request naming rules of your environment via the Dynatrace API.",
        "Просмотр всех правил именования запросов вашего окружения через Dynatrace API.",
    ),
    (
        "View a request naming rule via the Dynatrace API.",
        "Просмотр правила именования запросов через Dynatrace API.",
    ),
    (
        "Create a request naming rule via the Dynatrace API.",
        "Создание правила именования запросов через Dynatrace API.",
    ),
    (
        "Edit a request naming rule via the Dynatrace API.",
        "Редактирование правила именования запросов через Dynatrace API.",
    ),
    (
        "Delete a request naming rule via the Dynatrace API.",
        "Удаление правила именования запросов через Dynatrace API.",
    ),
    # ---------- (D) endpoint intro one-liners (non-embedding) ----------
    ("Deletes the specified request attribute.", "Удаляет указанный атрибут запроса."),
    (
        "Lists all request attributes available in your Dynatrace environment.",
        "Выводит список всех атрибутов запросов, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Gets parameters of the specified request attribute.",
        "Возвращает параметры указанного атрибута запроса.",
    ),
    ("Creates a new request attribute.", "Создаёт новый атрибут запроса."),
    (
        "Updates the specified request attribute.",
        "Обновляет указанный атрибут запроса.",
    ),
    (
        "Deletes the specified request naming rule. Deletion can't be undone.",
        "Удаляет указанное правило именования запросов. Удаление невозможно отменить.",
    ),
    (
        "Lists all request naming rules available in your Dynatrace environment.",
        "Выводит список всех правил именования запросов, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Gets parameters of the specified request naming rule.",
        "Возвращает параметры указанного правила именования запросов.",
    ),
    (
        "Updates the specified request naming rule. If the rule with the specified ID doesn't exist-creates a new rule with this ID.",
        "Обновляет указанное правило именования запросов. Если правила с указанным ID не существует, создаётся новое правило с этим ID.",
    ),
    (
        "The request returns the list of short representations of request naming rules-just ID, name, and description.",
        "Запрос возвращает список кратких представлений правил именования запросов: только ID, имя и описание.",
    ),
    (
        "The request returns the short representation of the newly created rule.",
        "Запрос возвращает краткое представление только что созданного правила.",
    ),
    (
        "The request returns the short representation of the updated or newly created rule.",
        "Запрос возвращает краткое представление обновлённого или только что созданного правила.",
    ),
    # ---------- (E) json-models structure (L3G pattern + L4X/L99 canon) ----------
    (
        "Some JSON models of the **Request naming** API vary, depending on the **type** of some objects. Here you can find JSON models for each variation.",
        "Некоторые JSON-модели API **Request naming** различаются в зависимости от поля **type** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.",
    ),
    (
        "## Variations of the `ComparisonInfo` object",
        "## Вариации объекта `ComparisonInfo`",
    ),
    (
        'Refer to [JSON models](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Learn the variations of JSON models in the Dynatrace request naming API.") to find all JSON models that depend on the **type** of the model.',
        'Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Изучите вариации JSON-моделей в Dynatrace API именования запросов.").',
    ),
    (
        "Type-specific comparison for attributes. The actual set of fields depends on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [Service metrics API - JSON models](https://dt-url.net/9803svb).",
        "Сравнение для атрибутов, зависящее от типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [Service metrics API - JSON models](https://dt-url.net/9803svb).",
    ),
    (
        "Defines the actual set of fields depending on the value. See one of the following objects:",
        "Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:",
    ),
    # ---------- (F) standard L99 phrases (L4X verbatim) ----------
    (
        "The request consumes and produces an `application/json` payload.",
        "Запрос принимает и возвращает payload `application/json`.",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает payload `application/json`.",
    ),
    (
        "The request consumes an `application/json` payload.",
        "Запрос принимает payload `application/json`.",
    ),
    (
        "To execute this request, you need an access token with `WriteConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `WriteConfig`.",
    ),
    (
        "To execute this request, you need an access token with `ReadConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `ReadConfig`.",
    ),
    (
        "To execute this request, you need an access token with `CaptureRequestData` scope.",
        "Для выполнения этого запроса нужен access token со scope `CaptureRequestData`.",
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
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.",
    ),
    # ---------- (G) headings (newline-anchored; ## Validate payload / #### Curl EN) ----------
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response\n", "\n### Ответ\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n#### Response codes\n", "\n#### Коды ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n#### Response body objects\n", "\n#### Объекты тела ответа\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n#### Response body JSON models\n", "\n#### JSON-модели тела ответа\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # ---------- (H) object headings -> #### Объект `X` (EN-lock object names) ----------
    ("#### The `RequestAttribute` object", "#### Объект `RequestAttribute`"),
    ("#### The `DataSource` object", "#### Объект `DataSource`"),
    ("#### The `ValueCondition` object", "#### Объект `ValueCondition`"),
    ("#### The `CapturedMethod` object", "#### Объект `CapturedMethod`"),
    ("#### The `MethodReference` object", "#### Объект `MethodReference`"),
    ("#### The `ScopeConditions` object", "#### Объект `ScopeConditions`"),
    ("#### The `ValueProcessing` object", "#### Объект `ValueProcessing`"),
    ("#### The `ExtractSubstring` object", "#### Объект `ExtractSubstring`"),
    ("#### The `RequestNaming` object", "#### Объект `RequestNaming`"),
    ("#### The `Condition` object", "#### Объект `Condition`"),
    ("#### The `ComparisonInfo` object", "#### Объект `ComparisonInfo`"),
    ("#### The `ConfigurationMetadata` object", "#### Объект `ConfigurationMetadata`"),
    ("#### The `Placeholder` object", "#### Объект `Placeholder`"),
    ("#### The `PropagationSource` object", "#### Объект `PropagationSource`"),
    ("#### The `UniversalTag` object", "#### Объект `UniversalTag`"),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    ("#### The `BooleanComparisonInfo` object", "#### Объект `BooleanComparisonInfo`"),
    (
        "#### The `ESBInputNodeTypeComparisonInfo` object",
        "#### Объект `ESBInputNodeTypeComparisonInfo`",
    ),
    ("#### The `ESBInputNodeTypeDto` object", "#### Объект `ESBInputNodeTypeDto`"),
    (
        "#### The `FailedStateComparisonInfo` object",
        "#### Объект `FailedStateComparisonInfo`",
    ),
    ("#### The `FailedStateDto` object", "#### Объект `FailedStateDto`"),
    (
        "#### The `FailureReasonComparisonInfo` object",
        "#### Объект `FailureReasonComparisonInfo`",
    ),
    ("#### The `FailureReasonDto` object", "#### Объект `FailureReasonDto`"),
    (
        "#### The `FastStringComparisonInfo` object",
        "#### Объект `FastStringComparisonInfo`",
    ),
    (
        "#### The `FlawStateComparisonInfo` object",
        "#### Объект `FlawStateComparisonInfo`",
    ),
    ("#### The `FlawStateDto` object", "#### Объект `FlawStateDto`"),
    (
        "#### The `HttpMethodComparisonInfo` object",
        "#### Объект `HttpMethodComparisonInfo`",
    ),
    ("#### The `HTTPMethodDto` object", "#### Объект `HTTPMethodDto`"),
    (
        "#### The `HttpStatusClassComparisonInfo` object",
        "#### Объект `HttpStatusClassComparisonInfo`",
    ),
    ("#### The `HTTPStatusClassDto` object", "#### Объект `HTTPStatusClassDto`"),
    (
        "#### The `IIBInputNodeTypeComparisonInfo` object",
        "#### Объект `IIBInputNodeTypeComparisonInfo`",
    ),
    ("#### The `IIBInputNodeTypeDto` object", "#### Объект `IIBInputNodeTypeDto`"),
    (
        "#### The `NumberComparisonInfo` object",
        "#### Объект `NumberComparisonInfo`",
    ),
    (
        "#### The `NumberRequestAttributeComparisonInfo` object",
        "#### Объект `NumberRequestAttributeComparisonInfo`",
    ),
    (
        "#### The `ServiceTypeComparisonInfo` object",
        "#### Объект `ServiceTypeComparisonInfo`",
    ),
    ("#### The `MethodServiceTypeDto` object", "#### Объект `MethodServiceTypeDto`"),
    (
        "#### The `StringComparisonInfo` object",
        "#### Объект `StringComparisonInfo`",
    ),
    (
        "#### The `StringRequestAttributeComparisonInfo` object",
        "#### Объект `StringRequestAttributeComparisonInfo`",
    ),
    (
        "#### The `StringOneAgentAttributeComparisonInfo` object",
        "#### Объект `StringOneAgentAttributeComparisonInfo`",
    ),
    ("#### The `TagComparisonInfo` object", "#### Объект `TagComparisonInfo`"),
    ("#### The `ZosComparisonInfo` object", "#### Объект `ZosComparisonInfo`"),
    ("#### The `ZosCallTypeDto` object", "#### Объект `ZosCallTypeDto`"),
    # ---------- (I) object/section descriptions (shared L4X + RA/RN-specific) ----------
    ("The request naming rule.", "Правило именования запросов."),
    ("A condition of a rule usage.", "Условие использования правила."),
    (
        "The custom placeholder to be used as a naming value pattern.",
        "Пользовательский плейсхолдер, используемый как шаблон значения для именования.",
    ),
    (
        "It enables you to extract a request attribute value or other request attribute and use it in the naming pattern.",
        "Он позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования.",
    ),
    (
        "Defines valid sources of request attributes for conditions or placeholders.",
        "Определяет допустимые источники атрибутов запросов для условий или плейсхолдеров.",
    ),
    (
        "Use only request attributes from services that have this tag. Use either this or `managementZone`",
        "Использовать только атрибуты запросов из сервисов с этим тегом. Используйте либо это, либо `managementZone`",
    ),
    ("Metadata useful for debugging", "Метаданные для отладки"),
    (
        "IBM integration bus label node name condition for which the value is captured.",
        "Условие имени узла-метки IBM integration bus, для которого захватывается значение.",
    ),
    (
        "Configuration of a method to be captured.",
        "Конфигурация захватываемого метода.",
    ),
    ("Conditions for data capturing.", "Условия захвата данных."),
    ("Process values as specified.", "Обработать значения заданным образом."),
    (
        "Preprocess by extracting a substring from the original value.",
        "Предобработка путём извлечения подстроки из исходного значения.",
    ),
    (
        "An ordered list of short representations of Dynatrace entities. |",
        "Упорядоченный список кратких представлений сущностей Dynatrace. |",
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
        "Comparison for `FAST_STRING` attributes. Use it for all service property attributes.",
        "Сравнение для атрибутов `FAST_STRING`. Используйте его для всех атрибутов свойств сервиса.",
    ),
    (
        "Comparison for `NUMBER_REQUEST_ATTRIBUTE` attributes, specifically of the generic **Number** type.",
        "Сравнение для атрибутов `NUMBER_REQUEST_ATTRIBUTE`, в частности обобщённого типа **Number**.",
    ),
    (
        "Comparison for `STRING_REQUEST_ATTRIBUTE` attributes, specifically of the **String** type.",
        "Сравнение для атрибутов `STRING_REQUEST_ATTRIBUTE`, в частности типа **String**.",
    ),
    ("Comparison for `BOOLEAN` attributes.", "Сравнение для атрибутов `BOOLEAN`."),
    (
        "Type-specific comparison information for attributes of type 'ESB\\_INPUT\\_NODE\\_TYPE'.This model also inherits fields from the parent model ComparisonInfo.",
        "Зависящая от типа информация о сравнении для атрибутов типа 'ESB\\_INPUT\\_NODE\\_TYPE'.Эта модель также наследует поля от родительской модели ComparisonInfo.",
    ),
    (
        "Comparison for `FAILED_STATE` attributes.",
        "Сравнение для атрибутов `FAILED_STATE`.",
    ),
    (
        "Comparison for `FAILURE_REASON` attributes.",
        "Сравнение для атрибутов `FAILURE_REASON`.",
    ),
    (
        "Comparison for `FLAW_STATE` attributes.",
        "Сравнение для атрибутов `FLAW_STATE`.",
    ),
    (
        "Comparison for `HTTP_METHOD` attributes.",
        "Сравнение для атрибутов `HTTP_METHOD`.",
    ),
    (
        "Comparison for `HTTP_STATUS_CLASS` attributes.",
        "Сравнение для атрибутов `HTTP_STATUS_CLASS`.",
    ),
    (
        "Comparison for `IIB_INPUT_NODE_TYPE` attributes.",
        "Сравнение для атрибутов `IIB_INPUT_NODE_TYPE`.",
    ),
    ("Comparison for `NUMBER` attributes.", "Сравнение для атрибутов `NUMBER`."),
    (
        "Comparison for `SERVICE_TYPE` attributes.",
        "Сравнение для атрибутов `SERVICE_TYPE`.",
    ),
    ("Comparison for `STRING` attributes.", "Сравнение для атрибутов `STRING`."),
    ("Comparison for `TAG` attributes.", "Сравнение для атрибутов `TAG`."),
    (
        "Comparison for `ZOS_CALL_TYPE` attributes.",
        "Сравнение для атрибутов `ZOS_CALL_TYPE`.",
    ),
    # ---------- (J) shared k8s/config canon (L4X verbatim) ----------
    (
        "A short description of the Dynatrace entity.",
        "Краткое описание сущности Dynatrace.",
    ),
    ("The ID of the Dynatrace entity.", "ID сущности Dynatrace."),
    ("The name of the Dynatrace entity.", "Имя сущности Dynatrace."),
    ("The HTTP status code", "HTTP-код статуса"),
    ("A list of constraint violations", "Список нарушений ограничений"),
    ("The error message", "Сообщение об ошибке"),
    ("Dynatrace version.", "Версия Dynatrace."),
    (
        "A sorted list of the version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    (
        "A sorted list of version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    # ---------- (K) table headers (longest first) ----------
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    (
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    ("| Code | Description |", "| Код | Описание |"),
    # ---------- (L) response-code cells (L101: ALL 14 files WITH period) ----------
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    (" | Success |", " | Успех |"),
    (
        "Validated. The submitted configuration is valid. Response does not have a body.",
        "Validated. Переданная конфигурация валидна. Ответ без тела.",
    ),
    ("Deleted. Response does not have a body.", "Удалено. Ответ без тела."),
    (
        "Success. The rule has been deleted. Response doesn't have a body.",
        "Успех. Правило удалено. Ответ без тела.",
    ),
    (
        "Success. The request attribute with the specified ID has been created. The ID of the new configuration is returned.",
        "Успех. Атрибут запроса с указанным ID создан. Возвращается ID новой конфигурации.",
    ),
    (
        "Success. Request attribute has been created. The ID of the new configuration is returned.",
        "Успех. Атрибут запроса создан. Возвращается ID новой конфигурации.",
    ),
    (
        "Success. Request attribute has been updated. Response doesn't have a body.",
        "Успех. Атрибут запроса обновлён. Ответ без тела.",
    ),
    (
        "Success. Request naming rule has been created. Response contains the new request naming rule's ID and name.",
        "Успех. Правило именования запросов создано. Тело ответа содержит ID и имя нового правила именования запросов.",
    ),
    (
        "Success. Request naming rule has been updated. Response doesn't have a body.",
        "Успех. Правило именования запросов обновлено. Ответ без тела.",
    ),
    (
        "Success. The request naming has been created. Response contains the new service's ID.",
        "Успех. Правило именования запросов создано. Тело ответа содержит ID нового сервиса.",
    ),
    # ---------- (M) parameter (path/query/body) cell descriptions ----------
    (
        "The ID of the request attribute to be updated.  If you set the ID in the body as well, it must match this ID.",
        "ID атрибута запроса, который нужно обновить.  Если вы также укажете ID в теле, он должен совпадать с этим ID.",
    ),
    (
        "The ID of the request attribute to be deleted.",
        "ID атрибута запроса, который нужно удалить.",
    ),
    (
        "The ID of the required request attribute.",
        "ID требуемого атрибута запроса.",
    ),
    (
        "Flag to include process group references to the response.  Process Group group references aren't compatible across environments.",
        "Флаг включения ссылок на группы процессов в ответ.  Ссылки на группы процессов несовместимы между окружениями.",
    ),
    (
        "The body must not provide an ID as IDs are automatically assigned.",
        "В теле не нужно указывать ID, поскольку идентификаторы назначаются автоматически.",
    ),
    (
        "The ID of the request naming rule to be deleted.",
        "ID правила именования запросов, которое нужно удалить.",
    ),
    (
        "The ID of the request naming rule you're inquiring.",
        "ID запрашиваемого правила именования запросов.",
    ),
    (
        "Order of the new request naming rule. Set to `PREPEND` to prepend it to the list, `APPEND` to append it. Defaults to `APPEND`.",
        "Порядок нового правила именования запросов. Установите `PREPEND`, чтобы добавить правило в начало списка, или `APPEND`, чтобы добавить в конец. По умолчанию `APPEND`.",
    ),
    (
        "The JSON body of the request containing parameters of the new request naming rule.  You must not specify the ID of the rule!",
        "JSON-тело запроса, содержащее параметры нового правила именования запросов.  Не указывайте ID правила!",
    ),
    (
        "The ID of the request naming to be updated.  The ID of the request naming in the body of the request must match this ID.",
        "ID правила именования запросов, которое нужно обновить.  ID правила именования запросов в теле запроса должен совпадать с этим ID.",
    ),
    (
        "The JSON body of the request containing updated parameters of the request naming.",
        "JSON-тело запроса, содержащее обновлённые параметры правила именования запросов.",
    ),
    # ---------- (N) RequestNaming element cells (shared get/post/put) ----------
    (
        "The set of conditions for the request naming rule usage.  You can specify several conditions. The request has to match **all** the specified conditions for the rule to trigger.",
        "Набор условий использования правила именования запросов.  Можно указать несколько условий. Запрос должен соответствовать **всем** указанным условиям, чтобы правило сработало.",
    ),
    (
        "The rule is enabled (`true`) or disabled (`false`).",
        "Правило включено (`true`) или отключено (`false`).",
    ),
    ("The ID of the request naming rule.", "ID правила именования запросов."),
    (
        "Specifies the management zones for which this rule should be applied.",
        "Указывает зоны управления, для которых должно применяться это правило.",
    ),
    (
        "The name to be assigned to matching requests.",
        "Имя, присваиваемое подходящим запросам.",
    ),
    (
        "The order string. Sorting request namings alphabetically by their order string determines their relative ordering.  Typically this is managed by Dynatrace internally and will not be present in GET responses nor used if present in PUT/POST requests, except where noted otherwise.",
        "Строка порядка. Сортировка именований запросов в алфавитном порядке по их строке порядка определяет их относительный порядок.  Обычно этим управляет Dynatrace внутренне; строка не присутствует в ответах GET и не используется, если присутствует в запросах PUT/POST, кроме случаев, где указано иное.",
    ),
    (
        "The list of custom placeholders to be used in the naming pattern.  It enables you to extract a request attribute value or other request attribute and use it in the request naming pattern.",
        "Список пользовательских плейсхолдеров для использования в шаблоне именования.  Он позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования запросов.",
    ),
    # Condition / ComparisonInfo (shared L4X verbatim)
    (
        "The attribute to be matched.  Note that for a service property attribute you must use the comparison of the `FAST_STRING` type.",
        "Сопоставляемый атрибут.  Учтите, что для атрибута свойства сервиса нужно использовать сравнение типа `FAST_STRING`.",
    ),
    (
        "Operator of the comparison. You can reverse it by setting **negate** to `true`.",
        "Оператор сравнения. Его можно инвертировать, установив **negate** в `true`.",
    ),
    (
        "Reverse the comparison **operator**. For example, it turns **equals** into **does not equal**.",
        "Инвертирует **оператор** сравнения. Например, превращает **equals** в **does not equal**.",
    ),
    ("The value to compare to.", "Значение для сравнения."),
    ("The values to compare to.", "Значения для сравнения."),
    (
        "The comparison is case-sensitive (`true`) or not case-sensitive (`false`).",
        "Сравнение чувствительно к регистру (`true`) или нечувствительно (`false`).",
    ),
    # Placeholder (shared L4X verbatim)
    (
        "Which value of the request attribute must be used when it occurs across multiple child requests.  Only applicable for the `SERVICE_REQUEST_ATTRIBUTE` attribute, when **useFromChildCalls** is `true`.  For the `COUNT` aggregation, the **kind** field is not applicable.",
        "Какое значение атрибута запроса использовать, когда он встречается в нескольких дочерних запросах.  Применимо только для атрибута `SERVICE_REQUEST_ATTRIBUTE`, когда **useFromChildCalls** равно `true`.  Для агрегации `COUNT` поле **kind** не применяется.",
    ),
    (
        "The attribute to extract from. You can only use attributes of the **string** type.",
        "Атрибут, из которого извлекать. Можно использовать только атрибуты типа **string**.",
    ),
    (
        "Depending on the **type** value:  * `REGEX_EXTRACTION`: The regular expression. * `BETWEEN_DELIMITER`: The opening delimiter string to look for. * All other values: The delimiter string to look for.",
        "В зависимости от значения **type**:  * `REGEX_EXTRACTION`: регулярное выражение. * `BETWEEN_DELIMITER`: искомая строка открывающего разделителя. * Все остальные значения: искомая строка разделителя.",
    ),
    (
        "The closing delimiter string to look for.  Required if the **kind** value is `BETWEEN_DELIMITER`. Not applicable otherwise.",
        "Искомая строка закрывающего разделителя.  Обязательно, если значение **kind** равно `BETWEEN_DELIMITER`. В остальных случаях не применяется.",
    ),
    (
        "The type of extraction.  Defines either usage of regular expression (`regex`) or the position of request attribute value to be extracted.  When the **attribute** is `SERVICE_REQUEST_ATTRIBUTE` attribute and **aggregation** is `COUNT`, needs to be set to `ORIGINAL_TEXT`",
        "Тип извлечения.  Определяет либо использование регулярного выражения (`regex`), либо позицию извлекаемого значения атрибута запроса.  Когда **attribute** равно `SERVICE_REQUEST_ATTRIBUTE`, а **aggregation** равно `COUNT`, должно быть установлено в `ORIGINAL_TEXT`",
    ),
    (
        "The name of the placeholder. Use it in the naming pattern as `{name}`.",
        "Имя плейсхолдера. Используйте его в шаблоне именования как `{name}`.",
    ),
    ("The format of the extracted string.", "Формат извлекаемой строки."),
    (
        "The One Agent attribute to extract from.  Required if the **kind** value is `ONE_AGENT_ATTRIBUTE`. Not applicable otherwise.",
        "Атрибут OneAgent, из которого извлекать.  Обязательно, если значение **kind** равно `ONE_AGENT_ATTRIBUTE`. В остальных случаях не применяется.",
    ),
    (
        "The request attribute to extract from.  Required if the **kind** value is `SERVICE_REQUEST_ATTRIBUTE`. Not applicable otherwise.",
        "Атрибут запроса, из которого извлекать.  Обязательно, если значение **kind** равно `SERVICE_REQUEST_ATTRIBUTE`. В остальных случаях не применяется.",
    ),
    (
        "If `true` request attribute will be taken from a child service call.  Only applicable for the `SERVICE_REQUEST_ATTRIBUTE` attribute. Defaults to `false`.",
        "Если `true`, атрибут запроса будет взят из дочернего вызова сервиса.  Применимо только для атрибута `SERVICE_REQUEST_ATTRIBUTE`. По умолчанию `false`.",
    ),
    # PropagationSource (shared L4X verbatim)
    (
        "Use only request attributes from services that belong to this management zone.. Use either this or `serviceTag`",
        "Использовать только атрибуты запросов из сервисов, принадлежащих этой зоне управления.. Используйте либо это, либо `serviceTag`",
    ),
    # UniversalTag LONG (mojibake normalized; L4X verbatim)
    (
        "The origin of the tag, such as AWS or Cloud Foundry. For custom tags use the `CONTEXTLESS` value.  The context is set for tags that are automatically imported by OneAgent (for example, from the AWS console or environment variables). It's useful for determining the origin of tags when not manually defined, and it also helps to prevent clashes with other existing tags. If the tag is not automatically imported, `CONTEXTLESS` set.",
        "Происхождение тега, например AWS или Cloud Foundry. Для пользовательских тегов используйте значение `CONTEXTLESS`.  Контекст устанавливается для тегов, автоматически импортируемых OneAgent (например, из консоли AWS или переменных окружения). Он полезен для определения происхождения тегов, когда они не заданы вручную, а также помогает предотвратить конфликты с другими существующими тегами. Если тег не импортирован автоматически, устанавливается `CONTEXTLESS`.",
    ),
    (
        "The key of the tag. For custom tags, put the tag value here.  The key allows categorization of multiple tags. It is possible that there are multiple values for a single key which will all be represented as standalone tags. Therefore, the key does not have the semantic of a map key but is more like a key of a key-value tuple. In some cases, for example custom tags, the key represents the actual tag value and the value field is not set - those are called valueless tags.",
        "Ключ тега. Для пользовательских тегов укажите здесь значение тега.  Ключ позволяет категоризировать несколько тегов. Возможно наличие нескольких значений для одного ключа, которые все будут представлены как отдельные теги. Поэтому ключ не имеет семантики ключа карты, а скорее похож на ключ пары ключ-значение. В некоторых случаях, например для пользовательских тегов, ключ представляет фактическое значение тега, а поле value не установлено: такие теги называются теги без значения.",
    ),
    (
        "The value of the tag. Not applicable to custom tags.  If a tag does have a separate key and value (in the textual representation they are split by the colon ':'), this field is set with the actual value. Key-value pairs can occur for automatically imported tags and tags set by rules if extractors are used.",
        "Значение тега. Не применяется к пользовательским тегам.  Если у тега есть отдельные ключ и значение (в текстовом представлении они разделены двоеточием ':'), в это поле записывается фактическое значение. Пары ключ-значение могут возникать для автоматически импортируемых тегов и тегов, заданных правилами при использовании экстракторов.",
    ),
    # TagInfo SHORT (L4X verbatim; json-models TagComparisonInfo variant)
    (
        "The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value.",
        "Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`.",
    ),
    (
        "The key of the tag.  Custom tags have the tag value here.",
        "Ключ тега.  У пользовательских тегов здесь находится значение тега.",
    ),
    (
        "The value of the tag.  Not applicable to custom tags.",
        "Значение тега.  Не применяется к пользовательским тегам.",
    ),
    # ---------- (O) RequestAttribute element cells ----------
    ("Aggregation type for the request values.", "Тип агрегации значений запроса."),
    (
        "Confidential data flag. Set `true` to treat the captured data as confidential.",
        "Флаг конфиденциальных данных. Установите `true`, чтобы считать захваченные данные конфиденциальными.",
    ),
    ("The list of data sources.", "Список источников данных."),
    ("The data type of the request attribute.", "Тип данных атрибута запроса."),
    (
        "The request attribute is enabled (`true`) or disabled (`false`).",
        "Атрибут запроса включён (`true`) или отключён (`false`).",
    ),
    ("The ID of the request attribute.", "ID атрибута запроса."),
    ("The name of the request attribute.", "Имя атрибута запроса."),
    (
        "String values transformation.  If the **dataType** is not `string`, set the `Original` here.",
        "Преобразование строковых значений.  Если **dataType** не `string`, укажите здесь `Original`.",
    ),
    (
        "Personal data masking flag. Set `true` to skip masking.  Warning: This will potentially access personalized data.",
        "Флаг маскирования персональных данных. Установите `true`, чтобы пропустить маскирование.  Предупреждение: при этом возможен доступ к персонализированным данным.",
    ),
    # DataSource element cells
    (
        "Specifies the location where the values are captured and stored.  Required if the **source** is one of the following: `GET_PARAMETER`, `URI`, `REQUEST_HEADER`, `RESPONSE_HEADER`.  Not applicable in other cases.  If the **source** value is `REQUEST_HEADER` or `RESPONSE_HEADER`, the `CAPTURE_AND_STORE_ON_BOTH` location is not allowed.",
        "Указывает место, где значения захватываются и хранятся.  Обязательно, если **source** равно одному из: `GET_PARAMETER`, `URI`, `REQUEST_HEADER`, `RESPONSE_HEADER`.  В остальных случаях не применяется.  Если значение **source** равно `REQUEST_HEADER` или `RESPONSE_HEADER`, расположение `CAPTURE_AND_STORE_ON_BOTH` не допускается.",
    ),
    (
        "CICS transaction call type condition for which the value is captured.  Required if the **source** is: `CICS_TRANSACTION_CALL_TYPE`.  Not applicable in other cases.",
        "Условие типа вызова транзакции CICS, для которого захватывается значение.  Обязательно, если **source** равно `CICS_TRANSACTION_CALL_TYPE`.  В остальных случаях не применяется.",
    ),
    (
        "The data source is enabled (`true`) or disabled (`false`).",
        "Источник данных включён (`true`) или отключён (`false`).",
    ),
    (
        "The IBM integration bus node type for which the value is captured.  This, iibNodeTypeCondition (different type of the same field) or `iibMethodNodeCondition` is required if the **source** is: `IIB_NODE`.  Not applicable in other cases.",
        "Тип узла IBM integration bus, для которого захватывается значение.  Это поле, iibNodeTypeCondition (другой тип того же поля) или `iibMethodNodeCondition` обязательно, если **source** равно `IIB_NODE`.  В остальных случаях не применяется.",
    ),
    (
        "IMS transaction call type condition for which the value is captured.  Required if the **source** is: `IMS_TRANSACTION_CALL_TYPE`.  Not applicable in other cases.",
        "Условие типа вызова транзакции IMS, для которого захватывается значение.  Обязательно, если **source** равно `IMS_TRANSACTION_CALL_TYPE`.  В остальных случаях не применяется.",
    ),
    (
        "The method specification if the **source** value is `METHOD_PARAM`.  Not applicable in other cases.",
        "Спецификация метода, если значение **source** равно `METHOD_PARAM`.  В остальных случаях не применяется.",
    ),
    (
        "The name of the web request parameter to capture.  Required if the **source** is one of the following: `POST_PARAMETER`, `GET_PARAMETER`, `REQUEST_HEADER`, `RESPONSE_HEADER`, `CUSTOM_ATTRIBUTE`.  Not applicable in other cases.",
        "Имя захватываемого параметра веб-запроса.  Обязательно, если **source** равно одному из: `POST_PARAMETER`, `GET_PARAMETER`, `REQUEST_HEADER`, `RESPONSE_HEADER`, `CUSTOM_ATTRIBUTE`.  В остальных случаях не применяется.",
    ),
    (
        "The technology of the server variable to capture if the **source** value is `SERVER_VARIABLE`. \\n\\n Not applicable in other cases.",
        "Технология захватываемой серверной переменной, если значение **source** равно `SERVER_VARIABLE`. \\n\\n В остальных случаях не применяется.",
    ),
    (
        "The technology of the session attribute to capture if the **source** value is `SESSION_ATTRIBUTE`. \\n\\n Not applicable in other cases.",
        "Технология захватываемого атрибута сессии, если значение **source** равно `SESSION_ATTRIBUTE`. \\n\\n В остальных случаях не применяется.",
    ),
    (
        "The source of the attribute to capture. Works in conjunction with **parameterName** or **methods** and **technology**.",
        "Источник захватываемого атрибута. Работает совместно с **parameterName** или **methods** и **technology**.",
    ),
    (
        "The key of the span attribute to capture.  Required if the **source** is: `SPAN_ATTRIBUTE`.  Not applicable in other cases.",
        "Ключ захватываемого атрибута span.  Обязательно, если **source** равно `SPAN_ATTRIBUTE`.  В остальных случаях не применяется.",
    ),
    (
        "The technology of the method to capture if the **source** value is `METHOD_PARAM`. \\n\\n Not applicable in other cases.",
        "Технология захватываемого метода, если значение **source** равно `METHOD_PARAM`. \\n\\n В остальных случаях не применяется.",
    ),
    # ValueCondition element cells
    ("Negate the comparison.", "Инвертировать сравнение."),
    (
        "Operator comparing the extracted value to the comparison value.",
        "Оператор, сравнивающий извлечённое значение со значением для сравнения.",
    ),
    # CapturedMethod element cells (no em-dash, CLAUDE#0)
    (
        "The index of the argument to capture. Set `0` to capture the return value, `1` or higher to capture a mehtod argument.  Required if the **capture** is set to `ARGUMENT`.  Not applicable in other cases.",
        "Индекс захватываемого аргумента. Установите `0`, чтобы захватить возвращаемое значение, `1` или больше, чтобы захватить аргумент метода.  Обязательно, если **capture** установлено в `ARGUMENT`.  В остальных случаях не применяется.",
    ),
    ("What to capture from the method.", "Что захватывать из метода."),
    (
        "The getter chain to apply to the captured object. It is required in one of the following cases:  The **capture** is set to `THIS`. The **capture** is set to `ARGUMENT`, and the argument is not a primitive, a primitive wrapper class, a string, or an array.  Not applicable in other cases.",
        "Цепочка геттеров, применяемая к захваченному объекту. Обязательна в одном из следующих случаев:  **capture** установлено в `THIS`. **capture** установлено в `ARGUMENT`, и аргумент не является примитивом, классом-обёрткой примитива, строкой или массивом.  В остальных случаях не применяется.",
    ),
    # MethodReference element cells
    ("The list of argument types.", "Список типов аргументов."),
    (
        "The class name where the method to capture resides.  Either this or the **fileName** must be set.",
        "Имя класса, в котором находится захватываемый метод.  Должно быть установлено либо это поле, либо **fileName**.",
    ),
    (
        "The file name where the method to capture resides.  Either this or **className** must be set.",
        "Имя файла, в котором находится захватываемый метод.  Должно быть установлено либо это поле, либо **className**.",
    ),
    (
        "The operator of the comparison.  If not set, `EQUALS` is used.",
        "Оператор сравнения.  Если не установлен, используется `EQUALS`.",
    ),
    ("The name of the method to capture.", "Имя захватываемого метода."),
    ("The modifiers of the method to capture.", "Модификаторы захватываемого метода."),
    ("The return type.", "Возвращаемый тип."),
    ("The visibility of the method to capture.", "Видимость захватываемого метода."),
    # ScopeConditions element cells
    ("Only applies to this host group.", "Применяется только к этой группе хостов."),
    (
        "Only applies to this process group. Note that this can't be transferred between different clusters or environments.",
        "Применяется только к этой группе процессов. Учтите, что это нельзя перенести между разными кластерами или окружениями.",
    ),
    (
        "Only applies to this service technology.",
        "Применяется только к этой технологии сервиса.",
    ),
    (
        "Only apply to process groups matching this tag.",
        "Применять только к группам процессов с этим тегом.",
    ),
    # ValueProcessing element cells
    (
        "Split (preprocessed) string values at this separator.",
        "Разбивать (предобработанные) строковые значения по этому разделителю.",
    ),
    ("Prune Whitespaces. Defaults to false.", "Удалять пробелы. По умолчанию false."),
    (
        "Extract value from captured data per regex.",
        "Извлечь значение из захваченных данных по регулярному выражению.",
    ),
    # ExtractSubstring element cells
    ("The delimiter string.", "Строка-разделитель."),
    (
        "The end-delimiter string.  Required if the **position** value is `BETWEEN`. Otherwise not allowed.",
        "Строка конечного разделителя.  Обязательна, если значение **position** равно `BETWEEN`. В остальных случаях не допускается.",
    ),
    (
        "The position of the extracted string relative to delimiters.",
        "Позиция извлекаемой строки относительно разделителей.",
    ),
    # ---------- (P) use-case create-a-new-request-naming-rule prose (non-link) ----------
    (
        "This use case shows you how to use the **Request naming** API to create a new request naming rule.",
        "Этот сценарий использования показывает, как с помощью API **Request naming** создать новое правило именования запросов.",
    ),
    (
        "Service request naming enables you to consolidate or refine requests across multiple services. Additionally, you can synchronize these rules across multiple Dynatrace environments.",
        "Именование запросов сервиса позволяет объединять или уточнять запросы в нескольких сервисах. Кроме того, можно синхронизировать эти правила между несколькими окружениями Dynatrace.",
    ),
    (
        "Let's assume we have two requests from Drupal (the open-source CMS) named `/node/1` and `/node/1/edit`. The last parts of both names (`/1` and `/1/edit`) don't carry any valuable information. We can remove those parts and consolidate the two separate requests into one named `/node`. To achieve this, we need a request naming rule to rename every request where the URL **begins with** `/node` into simply `/node`, thereby consolidating them.",
        "Предположим, у нас есть два запроса из Drupal (CMS с открытым исходным кодом) с именами `/node/1` и `/node/1/edit`. Последние части обоих имён (`/1` и `/1/edit`) не несут полезной информации. Мы можем убрать эти части и объединить два отдельных запроса в один с именем `/node`. Для этого нужно правило именования запросов, переименовывающее каждый запрос, URL которого **начинается с** `/node`, просто в `/node`, тем самым объединяя их.",
    ),
    (
        "The configuration for such a rule looks like this:",
        "Конфигурация такого правила выглядит так:",
    ),
    ("The important components are:", "Важные компоненты:"),
    (
        "* **conditions**-defines which requests will be renamed.",
        "* **conditions**: определяет, какие запросы будут переименованы.",
    ),
    (
        "* **namingPattern**-defines the resulting name.",
        "* **namingPattern**: определяет результирующее имя.",
    ),
    # image alt-text (matches its caption; "Try it out" UI button stays EN)
    ("![Access API explorer]", "![Доступ к API Explorer]"),
    ("![The payload]", "![Payload]"),
    ("![Successful request]", "![Успешный запрос]"),
    ("\nREST client\n", "\nREST-клиент\n"),
    ("\nDynatrace API Explorer\n", "\nDynatrace API Explorer\n"),
    ("Access API explorer\n", "Доступ к API Explorer\n"),
    (
        "3. In the API Explorer, select **Authorize**.  \n   The **Available authorizations** dialog appears.",
        "3. В API Explorer выберите **Authorize**.  \n   Появится диалог **Available authorizations**.",
    ),
    (
        "4. Paste your token into the **ReadConfigToken** and **WriteConfigToken** fields and click **Authorize**.",
        "4. Вставьте свой токен в поля **ReadConfigToken** и **WriteConfigToken** и нажмите **Authorize**.",
    ),
    (
        "5. Expand the **POST /service/requestNaming/** request and click **Try it out**.",
        "5. Разверните запрос **POST /service/requestNaming/** и нажмите **Try it out**.",
    ),
    (
        "6. Paste the JSON configuration of the request naming rule (see above) into the **body** field and click **Execute**.",
        "6. Вставьте JSON-конфигурацию правила именования запросов (см. выше) в поле **body** и нажмите **Execute**.",
    ),
    (
        "7. A successful request returns the **201** code and a short representation of the request naming rule.",
        "7. Успешный запрос возвращает код **201** и краткое представление правила именования запросов.",
    ),
    ("Try it out\n", "Try it out\n"),
    ("The payload\n", "Payload\n"),
    ("Successful request\n", "Успешный запрос\n"),
    # ---------- (Z) global LAST: element-can-hold -> Возможные значения: (L99) ----------
    ("The element can hold these values", "Возможные значения:"),
]


def _normalize(t):
    """Pure-ASCII source: build fragile mojibake/BOM keys from codepoints so the
    literals never get mangled (L4X lesson 1). EN CRLF -> LF (RU corpus conv)."""
    t = t.replace("\r\n", "\n")
    e2 = chr(0xE2)  # U+00E2; mojibake unit = e2 + 2 C1 chars (L4W)
    for c1, c2, repl in (
        (0x80, 0x99, "'"),  # U+2019 right single quote / apostrophe
        (0x80, 0x98, "'"),  # U+2018 left single quote
        (0x80, 0x9C, '"'),  # U+201C left double quote
        (0x80, 0x9D, '"'),  # U+201D right double quote
        (0x80, 0x93, "-"),  # U+2013 en dash
        (0x80, 0x94, "-"),  # U+2014 em dash (CLAUDE#0; sentence translated)
    ):
        t = t.replace(e2 + chr(c1) + chr(c2), repl)
    t = t.replace(chr(0xFEFF), "")  # real BOM
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")  # 3-char BOM (L4M)
    return t


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    with io.open(src, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    t = _normalize(t)
    for en, ru in R:
        t = t.replace(en, ru)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return dst


if __name__ == "__main__":
    for rel in FILES:
        print("wrote", build(rel))
