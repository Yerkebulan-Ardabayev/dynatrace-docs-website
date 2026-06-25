# -*- coding: utf-8 -*-
"""L4-AB builder: configuration-api/service-api/ remaining = 49 files
(parent service-api.md + custom-services-api/ 6 + detection-rules/ 27 incl
models.md + 4 web-rule families x6 + failure-detection/ 15). Closes the
service-api/ subsection 100% (L4-AA 14 + L4-AB 49 = 63). ACTIVE API
(no deprecated banner; * Reference / * Published EN-verbatim; title/H1x2
EN-verbatim, L99). Line parity EXACT EN==RU.

Splice method (L4-AA _build_serviceapi continuation): start from EN,
CRLF->LF, mojibake codepoint-normalize (L4W/L4X), strip BOM (L4M), apply
ordered exact-string canon -> byte-identical JSON + line parity. Anything
unreplaced stays EN-verbatim (object/enum/JSON/**bold**/API-name, L99).
Twin handled implicitly: identical EN shared strings across the 4 web-rule
families + get-all<->get-a-rule<->post<->put receive the identical RU via
the single shared R-table (deterministic global t.replace).

R = full L4-AA R reused verbatim (covers ALL shared objects: Configuration
Metadata/Error/ErrorEnvelope/ConstraintViolation/EntityShortRepresentation/
StubList/Condition/ComparisonInfo/Placeholder/... + headings + L99 phrases +
"Failed. The input is invalid" substring [L101 source period preserved] +
"| Success |" + table headers) APPENDED with L4-AB-specific entries in the
same TIER discipline (TIER-0 embedding sentences FIRST/longest-first;
"Возможные значения:" global LAST).

L101 MIXED: "Failed. The input is invalid" WITHOUT period in the 5 reorder
files, WITH period in 39 others -> the L4-AA substring entry
("Failed. The input is invalid","Сбой. Невалидный ввод") preserves source
period automatically (L4X#3, grep-verified per cell).

NEW canon (L4Y#4/style-guide §Links): intra-API navigation bullet link-text
in detection-rules.md is DESCRIPTIVE prose -> TRANSLATED
("Полные веб-запросы"/"Непрозрачные веб-запросы"/"Полные веб-сервисы"/
"Непрозрачные веб-сервисы"). Related-topics cross-ref link-text = target
page H1 which is EN (targets not yet RU) -> EN-verbatim, title-attr
translated (L4Y#5/L4O/L4L). json-models structure = L3G pattern
("### TYPE"/"#### TYPE"/ObjectName/Parameters/JSON model tab-labels EN);
"Возможные значения:" + EN-locks = L4O/L99 (NOT L3G "Элемент может
принимать"). Domain: service detection rule -> правило обнаружения
сервисов, failure detection -> обнаружение сбоев, parameter set -> набор
параметров, custom service -> пользовательский сервис, full/opaque web
request/service -> полный/непрозрачный веб-запрос/веб-сервис, reorder ->
изменить порядок. Product/tech names + inline-code/enum-backtick/**field**/
object names EN-lock. Source-quirk L93: "remain intact" (typo),
"queue entry point type.." (double dot), ".This"/".The transformation"
no-space, "isHttp404NotFoundFailureEnabled" referenced (field is
http404NotFoundFailureEnabled) -> mirrored verbatim-by-meaning."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
SA = "service-api"
CS = f"{SA}/custom-services-api"
DR = f"{SA}/detection-rules"
FD = f"{SA}/failure-detection"

FILES = [
    f"{SA}.md",
    f"{CS}.md",
    f"{CS}/del-rule.md",
    f"{CS}/get-all.md",
    f"{CS}/get-rule.md",
    f"{CS}/post-rule.md",
    f"{CS}/put-rule.md",
    f"{CS}/reorder-rules.md",
    f"{DR}.md",
    f"{DR}/full-web-request/del-a-rule.md",
    f"{DR}/full-web-request/get-a-rule.md",
    f"{DR}/full-web-request/get-all.md",
    f"{DR}/full-web-request/post-a-rule.md",
    f"{DR}/full-web-request/put-a-rule.md",
    f"{DR}/full-web-request/reorder-rules.md",
    f"{DR}/full-web-service/del-a-rule.md",
    f"{DR}/full-web-service/get-a-rule.md",
    f"{DR}/full-web-service/get-all.md",
    f"{DR}/full-web-service/post-a-rule.md",
    f"{DR}/full-web-service/put-a-rule.md",
    f"{DR}/full-web-service/reorder-rules.md",
    f"{DR}/models.md",
    f"{DR}/opaque-web-request/del-a-rule.md",
    f"{DR}/opaque-web-request/get-a-rule.md",
    f"{DR}/opaque-web-request/get-all.md",
    f"{DR}/opaque-web-request/post-a-rule.md",
    f"{DR}/opaque-web-request/put-a-rule.md",
    f"{DR}/opaque-web-request/reorder-rules.md",
    f"{DR}/opaque-web-service/delete-rule.md",
    f"{DR}/opaque-web-service/get-all.md",
    f"{DR}/opaque-web-service/get-rule.md",
    f"{DR}/opaque-web-service/post-rule.md",
    f"{DR}/opaque-web-service/put-rule.md",
    f"{DR}/opaque-web-service/reorder-rules.md",
    f"{FD}.md",
    f"{FD}/detection-rules/change-id.md",
    f"{FD}/detection-rules/delete-rule.md",
    f"{FD}/detection-rules/get-all.md",
    f"{FD}/detection-rules/get-rule.md",
    f"{FD}/detection-rules/post-rule.md",
    f"{FD}/detection-rules/put-rule.md",
    f"{FD}/detection-rules/reorder-rules.md",
    f"{FD}/json-models.md",
    f"{FD}/parameter-set/change-id.md",
    f"{FD}/parameter-set/delete-parameter-set.md",
    f"{FD}/parameter-set/get-all.md",
    f"{FD}/parameter-set/get-parameter-set.md",
    f"{FD}/parameter-set/post-parameter-set.md",
    f"{FD}/parameter-set/put-parameter-set.md",
]

# ============================================================================
# PART 1: full L4-AA R reused verbatim (shared objects/headings/L99/L101).
# ============================================================================
R_L4AA = [
    # ---------- (A) standalone Related/card title-attrs ----------
    (
        "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.",
        "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.",
    ),
    # ---------- (G) headings (newline-anchored) ----------
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
    # ---------- shared object headings (EN-lock names) ----------
    ("#### The `ConfigurationMetadata` object", "#### Объект `ConfigurationMetadata`"),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    # ---------- (F) standard L99 phrases ----------
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
    # ---------- (J) shared k8s/config canon ----------
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
    ("Metadata useful for debugging", "Метаданные для отладки"),
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
    # ---------- (L) response-code cells (L101 substring keeps source period) ----------
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    (" | Success |", " | Успех |"),
    ("Deleted. Response does not have a body.", "Удалено. Ответ без тела."),
    ("Deleted. Response doesn't have a body.", "Удалено. Ответ без тела."),
]

# ============================================================================
# PART 2: L4-AB-specific entries (TIER discipline).
# ============================================================================
R_L4AB = [
    # ===== TIER-0: embedding sentences (link+title-attr), longest-first =====
    (
        'Creates a new request naming rule. See the detailed use case in the [Request naming API - Create a new rule](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Learn how to create a request naming rule via the Dynatrace API.") topic.',
        'Создаёт новое правило именования запросов. Подробный сценарий использования смотрите в разделе [Request naming API - Create a new rule](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Узнайте, как создать правило именования запросов через Dynatrace API.").',
    ),
    (
        'The **Request attributes** API enables you to manage the configuration of [request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").',
        'API **Request attributes** позволяет управлять конфигурацией [атрибутов запросов](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и как использовать их на всех уровнях всех представлений анализа сервисов.").',
    ),
    # ===== TIER-0b: embedding bullets in failure-detection.md (run BEFORE the
    # (A) standalone title-attr "Edit a failure detection ..." entries, else
    # the generic pre-converts the nested title-attr -> leftover trailing text;
    # L4-AA Lesson 1 longest-first) =====
    (
        '* [Update an existing parameter set](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/put-parameter-set "Edit a failure detection parameter set via the Dynatrace API.") for failure detection rules.',
        '* [Update an existing parameter set](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/put-parameter-set "Редактирование набора параметров обнаружения сбоев через Dynatrace API.") для правил обнаружения сбоев.',
    ),
    (
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/change-id "Change the ID of a failure detection parameter set via the Dynatrace API.") of a parameter set.',
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/change-id "Изменение ID набора параметров обнаружения сбоев через Dynatrace API.") набора параметров.',
    ),
    (
        '* [Update an existing](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/put-rule "Edit a failure detection rule via the Dynatrace API.") failure detection rule.',
        '* [Update an existing](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/put-rule "Редактирование правила обнаружения сбоев через Dynatrace API.") правило обнаружения сбоев.',
    ),
    (
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/change-id "Change the ID of a failure detection rule via the Dynatrace API.") of a rule.',
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/change-id "Изменение ID правила обнаружения сбоев через Dynatrace API.") правила.',
    ),
    # ===== TIER-0c: full multi-sentence object/cell descriptions that CONTAIN
    # fragment-substrings ("You have two ..."/"* Override ..."/intro lines) —
    # MUST run before those fragments (L4-AA Lesson 1 longest-first). =====
    (
        "The contribution to the service ID calculation from the detected application ID.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution to the service ID calculation from the detected context root.  The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.  You have two options:  * Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field. * Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.  You can use one or both options. If you use both, the transformation applies to the modified URL.",
        "Вклад в расчёт ID сервиса от обнаруженного context root.  Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.  Есть два варианта:  * Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.",
    ),
    (
        "The contribution to the service ID calculation from the detected server name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution to the service ID calculation from the detected web service name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution to the service ID calculation from the detected web service name space.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution to the service ID calculation from the domain name where the web request has been detected.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от доменного имени, на котором обнаружен веб-запрос.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution from the URL, where the web request has been detected, into service ID calculation.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от URL, на котором обнаружен веб-запрос.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    # standalone object-intro lines (newline-anchored; run before fragments)
    (
        "\nThe contribution to the service ID calculation from the detected application ID.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного ID приложения.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected context root.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного context root.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected server name.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного имени сервера.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected web service name.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected web service name space.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the port, where the web request has been detected.\n",
        "\nВклад в расчёт ID сервиса от порта, на котором обнаружен веб-запрос.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the domain name where the web request has been detected.\n",
        "\nВклад в расчёт ID сервиса от доменного имени, на котором обнаружен веб-запрос.\n",
    ),
    (
        "\nThe contribution from the URL, where the web request has been detected, into service ID calculation.\n",
        "\nВклад в расчёт ID сервиса от URL, на котором обнаружен веб-запрос.\n",
    ),
    # FdpTagPredicate / FdcPredicate cell form (double-space + leading prefix) —
    # MUST run before the standalone 2nd-paragraph fragment. BOM ï»¿ already
    # stripped by _normalize() so keys here are BOM-free (L4X#1 corollary).
    (
        "The predicate that tests the value of the tag.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models](https://dt-url.net/9sg3swf).",
        "Предикат, проверяющий значение тега.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf).",
    ),
    (
        "The predicate that tests the value of the attribute.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models](https://dt-url.net/9sg3swf).",
        "Предикат, проверяющий значение атрибута.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf).",
    ),
    # FdpTagPredicate / FdcPredicate standalone object-intro (2nd paragraph,
    # BOM-free; runs after the cell form above)
    (
        "The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models](https://dt-url.net/9sg3swf).",
        "Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf).",
    ),
    (
        "The predicate that tests the value of the tag.\n",
        "Предикат, проверяющий значение тега.\n",
    ),
    (
        "The predicate that tests the value of the attribute.\n",
        "Предикат, проверяющий значение атрибута.\n",
    ),
    # ExceptionPattern: full cell form (double-space) BEFORE standalone "If an
    # exception ..." fragment + the standalone object-intro line.
    (
        "A list of faulty exceptions.  If an exception on *any* node of the service matches *any* of these patterns it is considered a failure.",
        "Список ошибочных исключений.  Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.",
    ),
    (
        "\nA list of faulty exceptions.\n",
        "\nСписок ошибочных исключений.\n",
    ),
    # FD detection-rules/parameter-set post/put body-param cells
    (
        "The JSON body of the request. Contains the configuration of the new failure detection rule.  Dynatrace will generate a random UUID for you, if you don't specify an ID.",
        "JSON-тело запроса. Содержит конфигурацию нового правила обнаружения сбоев.  Dynatrace сгенерирует для вас случайный UUID, если вы не укажете ID.",
    ),
    (
        "The JSON body of the request. Contains the updated configuration of the failure detection rule.  You can't update the ID with this request. Use the change ID request instead.",
        "JSON-тело запроса. Содержит обновлённую конфигурацию правила обнаружения сбоев.  Этим запросом нельзя обновить ID. Вместо этого используйте запрос смены ID.",
    ),
    (
        "The JSON body of the request. Contains the new failure detection parameter set.  Dynatrace will generate a random UUID for you, if you don't specify an ID.",
        "JSON-тело запроса. Содержит новый набор параметров обнаружения сбоев.  Dynatrace сгенерирует для вас случайный UUID, если вы не укажете ID.",
    ),
    (
        "The JSON body of the request. Contains the updated failure detection parameter set.  You can't update the ID with this request. Use the change ID request instead.",
        "JSON-тело запроса. Содержит обновлённый набор параметров обнаружения сбоев.  Этим запросом нельзя обновить ID. Вместо этого используйте запрос смены ID.",
    ),
    # response-code cells with trailing "Response doesn't/does not have a body"
    (
        "Validated. The submitted configuration is valid. Response does not have a body.",
        "Validated. Переданная конфигурация валидна. Ответ без тела.",
    ),
    (
        "Success. The submitted configuration is valid. Response doesn't have a body.",
        "Успех. Переданная конфигурация валидна. Ответ без тела.",
    ),
    (
        "Success. The configuration has been updated. Response doesn't have a body.",
        "Успех. Конфигурация обновлена. Ответ без тела.",
    ),
    (
        "Success. The failure detection rule has been deleted. Response doesn't have a body.",
        "Успех. Правило обнаружения сбоев удалено. Ответ без тела.",
    ),
    # request-line word-order variant (failure-detection/detection-rules/post)
    (
        "The request produces and consumes an `application/json` payload.",
        "Запрос возвращает и принимает payload `application/json`.",
    ),
    # ===== TIER-0d: embedding sentences with [reorder request] link + body
    # cells embedding `PUT /service/detectionRules/<TYPE>/reorder` inline-code.
    # MUST run before the (A) standalone "Change the order of failure detection
    # rules via the Dynatrace API." title-attr conversion (L4-AA Lesson 1).
    # Link-text [reorder request] -> TRANSLATED (descriptive prose, L4Y#4;
    # orchestrator-decided). inline-code `PUT ...` stays EN-verbatim. =====
    (
        'The new rule is appended to the end of the rule list. Rules are evaluated from top to bottom; the first matching rule applies. To enforce a particular order, use the [reorder request](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Change the order of failure detection rules via the Dynatrace API.").',
        'Новое правило добавляется в конец списка правил. Правила вычисляются сверху вниз; применяется первое совпавшее правило. Чтобы задать определённый порядок, используйте [запрос на изменение порядка](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Изменение порядка правил обнаружения сбоев через Dynatrace API.").',
    ),
    (
        'If a rule with the specified ID doesn\'t exist, a new one is created and appended to the end of the rule list. Rules are evaluated from top to bottom; the first matching rule applies. To enforce a particular order, use the [reorder request](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Change the order of failure detection rules via the Dynatrace API.").',
        'Если правила с указанным ID не существует, создаётся новое и добавляется в конец списка правил. Правила вычисляются сверху вниз; применяется первое совпавшее правило. Чтобы задать определённый порядок, используйте [запрос на изменение порядка](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Изменение порядка правил обнаружения сбоев через Dynatrace API.").',
    ),
    # service-detection POST body cells (4 family variants; exact source
    # punctuation; <TYPE> reorder path stays EN inside inline code). NOTE:
    # full-web-request POST/PUT use ". Contains"/"order, use" form (already
    # covered by (M) entries); the other 3 use "containing"/("order, use" for
    # opaque-web-request, "order use" for full-web-service & opaque-web-service).
    (
        "The JSON body of the request containing parameters of the new service detection rule.  You must not specify the ID of the rule!  The **order** field is ignored in this request. To enforce a particular order use the `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder` request.",
        "JSON-тело запроса, содержащее параметры нового правила обнаружения сервисов.  Не указывайте ID правила!  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder`.",
    ),
    (
        "The JSON body of the request containing parameters of the new service detection rule.  You must not specify the ID of the rule!  The **order** field is ignored in this request. To enforce a particular order, use the `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/reorder` request.",
        "JSON-тело запроса, содержащее параметры нового правила обнаружения сервисов.  Не указывайте ID правила!  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/reorder`.",
    ),
    (
        "The JSON body of the request containing parameters of the new service detection rule.  You must not specify the ID of the rule!  The **order** field is ignored in this request. To enforce a particular order use the `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/reorder` request.",
        "JSON-тело запроса, содержащее параметры нового правила обнаружения сервисов.  Не указывайте ID правила!  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/reorder`.",
    ),
    # service-detection PUT body cells (3 non-FWR family variants)
    (
        "The JSON body of the request containing updated parameters of the service detection rule.  The **order** field is ignored in this request. To enforce a particular order use the `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder` request.",
        "JSON-тело запроса, содержащее обновлённые параметры правила обнаружения сервисов.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder`.",
    ),
    (
        "The JSON body of the request containing updated parameters of the service detection rule.  The **order** field is ignored in this request. To enforce a particular order, use the `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/reorder` request.",
        "JSON-тело запроса, содержащее обновлённые параметры правила обнаружения сервисов.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/reorder`.",
    ),
    (
        "The JSON body of the request containing updated parameters of the service detection rule.  The **order** field is ignored in this request. To enforce a particular order use the `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/reorder` request.",
        "JSON-тело запроса, содержащее обновлённые параметры правила обнаружения сервисов.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE/reorder`.",
    ),
    # full-web-request POST/PUT body cells (". Contains"/"order, use" form)
    (
        "The JSON body of the request. Contains parameters of the new service detection rule.  You must not specify the ID of the rule!  The **order** field is ignored in this request. To enforce a particular order, use the `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder` request.",
        "JSON-тело запроса. Содержит параметры нового правила обнаружения сервисов.  Не указывайте ID правила!  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder`.",
    ),
    (
        "The JSON body of the request. Contains updated parameters of the service detection rule.  The **order** field is ignored in this request. To enforce a particular order, use the `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder` request.",
        "JSON-тело запроса. Содержит обновлённые параметры правила обнаружения сервисов.  Поле **order** в этом запросе игнорируется. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder`.",
    ),
    # detection-rules put-a-rule (4 families) standalone intro (post-normalize
    # 'doesnât' -> "doesn't"); orchestrator string #5.
    (
        "If a rule with the specified ID doesn't exist, a new rule is created and appended to the end of the rule list.",
        "Если правила с указанным ID не существует, создаётся новое правило и добавляется в конец списка правил.",
    ),
    # FD post/put intro 2nd sentence; orchestrator string #4.
    (
        "The failure detection parameter set used by the rule must exist at the time of rule creation.",
        "Набор параметров обнаружения сбоев, используемый правилом, должен существовать на момент создания правила.",
    ),
    # FD post/put body-param "The body must not provide an ID..."; #3.
    (
        "The body must not provide an ID. An ID is assigned automatically by Dynatrace and returned as part of the response.",
        "В теле не нужно указывать ID. Идентификатор назначается автоматически Dynatrace и возвращается в составе ответа.",
    ),
    # custom-services put-rule endpoint-name H2 anomaly -> KEEP EN (L99/L4T;
    # corpus has zero "## VERB" headings; mirror anomalous source). #11.
    ("## PUT a custom service rule", "## PUT a custom service rule"),
    (
        "Updates the specified custom service rule.",
        "Обновляет указанное правило пользовательского сервиса.",
    ),
    # detection-rules.md inline card descriptions (NOT card-glue form)
    (
        "Service detection rules are evaluated one after another. The first matching rule is applied and further processing stops. Reorder service detection rules to achieve the order of evaluation you need.",
        "Правила обнаружения сервисов выполняются одно за другим. Применяется первое совпавшее правило, дальнейшая обработка прекращается. Измените порядок правил обнаружения сервисов, чтобы получить нужный порядок выполнения.",
    ),
    (
        "Get an overview of all service detection rules for:",
        "Обзор всех правил обнаружения сервисов для:",
    ),
    (
        "Get parameters of a service detection rule for:",
        "Получить параметры правила обнаружения сервисов для:",
    ),
    (
        "Create a new service detection rule for:",
        "Создать новое правило обнаружения сервисов для:",
    ),
    (
        "Update an existing service detection rule or create a new rule with the specified ID.",
        "Обновить существующее правило обнаружения сервисов или создать новое правило с указанным ID.",
    ),
    (
        "Delete a service detection rule you don't need anymore.",
        "Удалить правило обнаружения сервисов, которое вам больше не нужно.",
    ),
    # detection-rules / failure-detection attributeType/attribute cell prefix
    # (the enum-list "The element can hold these values" -> Z global LAST)
    (
        "The type of the attribute to be checked.",
        "Тип проверяемого атрибута.",
    ),
    (
        "The attribute to be checked.",
        "Проверяемый атрибут.",
    ),
    # json-models.md `values`/`value` cell forms. FULL-CELL forms FIRST
    # (longest-first / L4-AA Lesson 1: the second-sentence fragment must NOT
    # pre-fire and orphan the "A list of reference values."/"The reference
    # value." prefix). string[] uses "A list of reference values." prefix,
    # integer[] uses "The reference value." prefix.
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) equals *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (строка) равен *любому* из этих значений.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) start with *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (строка) начинается с *любого* из этих значений.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) ends with *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (строка) заканчивается *любым* из этих значений.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) contains *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (строка) содержит *любое* из этих значений.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a long) equals *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (long) равен *любому* из этих значений.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is an integer) equals *any* of these.",
        "Эталонное значение. Условие выполняется, когда атрибут (целое число) равен *любому* из этих значений.",
    ),
    # second-sentence-only fragments (FdpTag* single-value cells where the cell
    # is JUST this sentence; run AFTER the full-cell forms above)
    (
        "The condition is fulfilled when the attribute (which is an integer) equals *any* of these.",
        "Условие выполняется, когда атрибут (целое число) равен *любому* из этих значений.",
    ),
    (
        "The condition is fulfilled when the attribute (which is a long) equals *any* of these.",
        "Условие выполняется, когда атрибут (long) равен *любому* из этих значений.",
    ),
    (
        "The condition is fulfilled when the attribute (which is a string) equals *any* of these.",
        "Условие выполняется, когда атрибут (строка) равен *любому* из этих значений.",
    ),
    (
        "The condition is fulfilled when the attribute (which is a string) start with *any* of these.",
        "Условие выполняется, когда атрибут (строка) начинается с *любого* из этих значений.",
    ),
    (
        "The condition is fulfilled when the attribute (which is a string) ends with *any* of these.",
        "Условие выполняется, когда атрибут (строка) заканчивается *любым* из этих значений.",
    ),
    (
        "The condition is fulfilled when the attribute (which is a string) contains *any* of these.",
        "Условие выполняется, когда атрибут (строка) содержит *любое* из этих значений.",
    ),
    # ----- parent service-api.md group headings (### Foo, newline-anchored) -----
    ("\n### Calculated service metrics\n", "\n### Вычисляемые метрики сервиса\n"),
    ("\n### Custom services\n", "\n### Пользовательские сервисы\n"),
    ("\n### Failure detection\n", "\n### Обнаружение сбоев\n"),
    ("\n### Request attributes\n", "\n### Атрибуты запросов\n"),
    ("\n### Request naming\n", "\n### Именование запросов\n"),
    (
        "\n### Detection rules - Full web request\n",
        "\n### Правила обнаружения - Полные веб-запросы\n",
    ),
    (
        "\n### Detection rules - Opaque web request\n",
        "\n### Правила обнаружения - Непрозрачные веб-запросы\n",
    ),
    (
        "\n### Detection rules - Full web service\n",
        "\n### Правила обнаружения - Полные веб-сервисы\n",
    ),
    (
        "\n### Detection rules - Opaque web service\n",
        "\n### Правила обнаружения - Непрозрачные веб-сервисы\n",
    ),
    # ----- parent group headings shared (### List all etc) -----
    ("\n### List all parameter sets\n", "\n### Список всех наборов параметров\n"),
    ("\n### List all rules\n", "\n### Список всех правил\n"),
    ("\n### List all\n", "\n### Список всех\n"),
    ("\n### View a parameter set\n", "\n### Просмотр набора параметров\n"),
    ("\n### View a rule\n", "\n### Просмотр правила\n"),
    ("\n### Create a parameter set\n", "\n### Создание набора параметров\n"),
    ("\n### Create a rule\n", "\n### Создание правила\n"),
    ("\n### Edit a parameter set\n", "\n### Редактирование набора параметров\n"),
    ("\n### Edit a rule\n", "\n### Редактирование правила\n"),
    ("\n### Delete a parameter set\n", "\n### Удаление набора параметров\n"),
    ("\n### Delete a rule\n", "\n### Удаление правила\n"),
    ("\n### Reorder rules\n", "\n### Изменение порядка правил\n"),
    # ----- parent card title-attrs (standalone, A) -----
    (
        "View all calculated service metrics of your environment via the Dynatrace API.",
        "Просмотр всех вычисляемых метрик сервиса вашего окружения через Dynatrace API.",
    ),
    (
        "View a calculated service metric via the Dynatrace API.",
        "Просмотр вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "Create a calculated service metric via the Dynatrace API.",
        "Создание вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "Update a calculated service metric via the Dynatrace API.",
        "Обновление вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "Delete a calculated service metric via the Dynatrace API.",
        "Удаление вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "View all custom service rules of your environment via the Dynatrace API.",
        "Просмотр всех правил пользовательских сервисов вашего окружения через Dynatrace API.",
    ),
    (
        "View a custom service rule via the Dynatrace API.",
        "Просмотр правила пользовательского сервиса через Dynatrace API.",
    ),
    (
        "Create a custom service rule via the Dynatrace API.",
        "Создание правила пользовательского сервиса через Dynatrace API.",
    ),
    (
        "Edit a custom service rule via the Dynatrace API.",
        "Редактирование правила пользовательского сервиса через Dynatrace API.",
    ),
    (
        "Delete a custom service rule via the Dynatrace API.",
        "Удаление правила пользовательского сервиса через Dynatrace API.",
    ),
    (
        "Change the order of custom service rules via the Dynatrace API.",
        "Изменение порядка правил пользовательских сервисов через Dynatrace API.",
    ),
    (
        "View all failure detection parameter sets of your monitoring environment via the Dynatrace API.",
        "Просмотр всех наборов параметров обнаружения сбоев вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View a failure detection parameter set via the Dynatrace API.",
        "Просмотр набора параметров обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Create a failure detection parameter set via the Dynatrace API.",
        "Создание набора параметров обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Edit a failure detection parameter set via the Dynatrace API.",
        "Редактирование набора параметров обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Delete a failure detection parameter set via the Dynatrace API.",
        "Удаление набора параметров обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Change the ID of a failure detection parameter set via the Dynatrace API.",
        "Изменение ID набора параметров обнаружения сбоев через Dynatrace API.",
    ),
    (
        "View all failure detection rules of your monitoring environment via the Dynatrace API.",
        "Просмотр всех правил обнаружения сбоев вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View a failure detection rule via the Dynatrace API.",
        "Просмотр правила обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Create a failure detection rule via the Dynatrace API.",
        "Создание правила обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Edit a failure detection rule via the Dynatrace API.",
        "Редактирование правила обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Delete a failure detection rule via the Dynatrace API.",
        "Удаление правила обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Change the order of failure detection rules via the Dynatrace API.",
        "Изменение порядка правил обнаружения сбоев через Dynatrace API.",
    ),
    (
        "Change the ID of a failure detection rule via the Dynatrace API.",
        "Изменение ID правила обнаружения сбоев через Dynatrace API.",
    ),
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
    # detection-rules family card title-attrs (per family, longest variants)
    (
        "View all service detection rules for opaque and external web requests via the Dynatrace API.",
        "Просмотр всех правил обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.",
    ),
    (
        "View a service detection rule for opaque and external web requests via the Dynatrace API.",
        "Просмотр правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.",
    ),
    (
        "Create a service detection rule for opaque and external web requests via the Dynatrace API.",
        "Создание правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.",
    ),
    (
        "Edit a service detection rule for opaque and external web requests via the Dynatrace API.",
        "Редактирование правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.",
    ),
    (
        "Delete a service detection rule for opaque and external web requests via the Dynatrace API.",
        "Удаление правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.",
    ),
    (
        "Reorder service detection rules for opaque and external web requests via the Dynatrace API.",
        "Изменение порядка правил обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.",
    ),
    (
        "View all service detection rules for external and opaque web services via the Dynatrace API.",
        "Просмотр всех правил обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.",
    ),
    (
        "View a service detection rule for external and opaque web services via the Dynatrace API.",
        "Просмотр правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.",
    ),
    (
        "Create a service detection rule for external and opaque web services via the Dynatrace API.",
        "Создание правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.",
    ),
    (
        "Edit a service detection rule for external and opaque web services via the Dynatrace API.",
        "Редактирование правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.",
    ),
    (
        "Delete a service detection rule for external and opaque web services via the Dynatrace API.",
        "Удаление правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.",
    ),
    (
        "Reorder service detection rules for external and opaque web services via the Dynatrace API.",
        "Изменение порядка правил обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.",
    ),
    (
        "View all service detection rules for full web requests via the Dynatrace API.",
        "Просмотр всех правил обнаружения сервисов для полных веб-запросов через Dynatrace API.",
    ),
    (
        "View a service detection rule for full web requests via the Dynatrace API.",
        "Просмотр правила обнаружения сервисов для полных веб-запросов через Dynatrace API.",
    ),
    (
        "Create a service detection rule for full web requests via the Dynatrace API.",
        "Создание правила обнаружения сервисов для полных веб-запросов через Dynatrace API.",
    ),
    (
        "Edit a service detection rule for full web requests via the Dynatrace API.",
        "Редактирование правила обнаружения сервисов для полных веб-запросов через Dynatrace API.",
    ),
    (
        "Delete a service detection rule for full web requests via the Dynatrace API.",
        "Удаление правила обнаружения сервисов для полных веб-запросов через Dynatrace API.",
    ),
    (
        "Reorder service detection rules for full web requests via the Dynatrace API.",
        "Изменение порядка правил обнаружения сервисов для полных веб-запросов через Dynatrace API.",
    ),
    (
        "View all service detection rules for full web services via the Dynatrace API.",
        "Просмотр всех правил обнаружения сервисов для полных веб-сервисов через Dynatrace API.",
    ),
    (
        "View a service detection rule for full web services via the Dynatrace API.",
        "Просмотр правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.",
    ),
    (
        "Create a service detection rule for full web services via the Dynatrace API.",
        "Создание правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.",
    ),
    (
        "Edit a service detection rule for full web services via the Dynatrace API.",
        "Редактирование правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.",
    ),
    (
        "Delete a service detection rule for full web services via the Dynatrace API.",
        "Удаление правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.",
    ),
    (
        "Reorder service detection rules for full web services via the Dynatrace API.",
        "Изменение порядка правил обнаружения сервисов для полных веб-сервисов через Dynatrace API.",
    ),
    # ----- (B) descriptive intra-API navigation bullet link-text (L4Y#4) -----
    ("[Full web requests](", "[Полные веб-запросы]("),
    ("[Opaque web requests](", "[Непрозрачные веб-запросы]("),
    ("[Full web services](", "[Полные веб-сервисы]("),
    ("[Opaque web services](", "[Непрозрачные веб-сервисы]("),
    # service-api.md top-level nav-bullet link-text (descriptive endpoint-action
    # prose -> TRANSLATED for consistency with [Full web requests] decision +
    # L4Y#4; bracket-anchored on "](" so title-attr [already RU] untouched).
    # [Service monitoring settings] = Related-topics cross-ref -> stays EN
    # (canon d). Longest-first not needed: each is a distinct ]( -anchored key.
    (
        "[View all calculated service metrics](",
        "[Просмотр всех вычисляемых метрик сервиса](",
    ),
    (
        "[View a calculated service metric](",
        "[Просмотр вычисляемой метрики сервиса](",
    ),
    (
        "[Create a calculated service metric](",
        "[Создание вычисляемой метрики сервиса](",
    ),
    (
        "[Edit a calculated service metric](",
        "[Редактирование вычисляемой метрики сервиса](",
    ),
    (
        "[Delete a calculated service metric](",
        "[Удаление вычисляемой метрики сервиса](",
    ),
    (
        "[View all custom service rules](",
        "[Просмотр всех правил пользовательских сервисов](",
    ),
    ("[View a custom service rule](", "[Просмотр правила пользовательского сервиса]("),
    (
        "[Create a custom service rule](",
        "[Создание правила пользовательского сервиса](",
    ),
    (
        "[Edit a custom service rule](",
        "[Редактирование правила пользовательского сервиса](",
    ),
    (
        "[Delete a custom service rule](",
        "[Удаление правила пользовательского сервиса](",
    ),
    (
        "[Reorder custom service rules](",
        "[Изменение порядка правил пользовательских сервисов](",
    ),
    ("[View all parameter sets](", "[Просмотр всех наборов параметров]("),
    ("[View a parameter set](", "[Просмотр набора параметров]("),
    ("[Create a parameter set](", "[Создание набора параметров]("),
    ("[Edit a parameter set](", "[Редактирование набора параметров]("),
    ("[Delete a parameter set](", "[Удаление набора параметров]("),
    ("[Change the ID of a parameter set](", "[Изменение ID набора параметров]("),
    ("[View all detection rules](", "[Просмотр всех правил обнаружения]("),
    ("[View a detection rule](", "[Просмотр правила обнаружения]("),
    ("[Create a detection rule](", "[Создание правила обнаружения]("),
    ("[Edit a detection rule](", "[Редактирование правила обнаружения]("),
    ("[Delete a detection rule](", "[Удаление правила обнаружения]("),
    ("[Reorder detection rules](", "[Изменение порядка правил обнаружения]("),
    ("[Change the ID of a detection rule](", "[Изменение ID правила обнаружения]("),
    ("[View all request attributes](", "[Просмотр всех атрибутов запросов]("),
    ("[View a request attribute](", "[Просмотр атрибута запроса]("),
    ("[Create a request attribute](", "[Создание атрибута запроса]("),
    ("[Edit a request attribute](", "[Редактирование атрибута запроса]("),
    ("[Delete a request attribute](", "[Удаление атрибута запроса]("),
    ("[View all request naming rules](", "[Просмотр всех правил именования запросов]("),
    ("[View a request naming rule](", "[Просмотр правила именования запросов]("),
    ("[Create a request naming rule](", "[Создание правила именования запросов]("),
    ("[Edit a request naming rule](", "[Редактирование правила именования запросов]("),
    ("[Delete a request naming rule](", "[Удаление правила именования запросов]("),
    # detection-rules.md per-row bullets: "View rules"/"View a rule"/"Create a
    # rule"/"Edit a rule"/"Delete a rule"/"Reorder rules" (Detection rules -
    # <Type> sections). Distinct from [Full web requests] family-name bullets.
    ("[View rules](", "[Просмотр правил]("),
    ("[View a rule](", "[Просмотр правила]("),
    ("[Create a rule](", "[Создание правила]("),
    ("[Edit a rule](", "[Редактирование правила]("),
    ("[Delete a rule](", "[Удаление правила]("),
    ("[Reorder rules](", "[Изменение порядка правил]("),
    # failure-detection.md embedding-bullet link-text (descriptive, L4Y#4) —
    # title-attr + trailing text already handled by TIER-0b; link-text here.
    (
        "[Update an existing parameter set](",
        "[Обновление существующего набора параметров](",
    ),
    ("[Update an existing](", "[Обновление существующего]("),
    ("[Change the ID](", "[Изменение ID]("),
    # ----- (C) parent card descriptions (custom-services / failure-detection) -----
    (
        "Get an overview of all custom service rules.",
        "Обзор всех правил пользовательских сервисов.",
    ),
    (
        "Get parameters of a custom service rule by its ID.",
        "Получить параметры правила пользовательского сервиса по его ID.",
    ),
    (
        "Custom service rules are evaluated one after another. The first matching rule is applied, and further processing stops.",
        "Правила пользовательских сервисов выполняются одно за другим. Применяется первое совпавшее правило, дальнейшая обработка прекращается.",
    ),
    (
        "Reorder custom service rules to achieve the order of evaluation you need.",
        "Измените порядок правил пользовательских сервисов, чтобы получить нужный порядок выполнения.",
    ),
    (
        "Create a new rule with the exact parameters you need.",
        "Создать новое правило с нужными вам параметрами.",
    ),
    (
        "Update an existing custom service rule or create a new rule with the specified ID.",
        "Обновить существующее правило пользовательского сервиса или создать новое правило с указанным ID.",
    ),
    (
        "Delete a rule you don't need anymore.",
        "Удалить правило, которое вам больше не нужно.",
    ),
    (
        "Get an overview of all parameter sets for failure detection rules.",
        "Обзор всех наборов параметров для правил обнаружения сбоев.",
    ),
    (
        "View the configuration of all parameter sets for failure detection rules.",
        "Просмотр конфигурации всех наборов параметров для правил обнаружения сбоев.",
    ),
    (
        "Create a new parameter set for failure detection rules.",
        "Создать новый набор параметров для правил обнаружения сбоев.",
    ),
    (
        "Delete a parameter set for failure detection rules.",
        "Удалить набор параметров для правил обнаружения сбоев.",
    ),
    (
        "Get an overview of all failure detection rules.",
        "Обзор всех правил обнаружения сбоев.",
    ),
    (
        "View the configuration of a failure detection rule.",
        "Просмотр конфигурации правила обнаружения сбоев.",
    ),
    (
        "Failure detection rules are evaluated one after another. The first matching rule is applied, and further processing stops.",
        "Правила обнаружения сбоев выполняются одно за другим. Применяется первое совпавшее правило, дальнейшая обработка прекращается.",
    ),
    (
        "Reorder the rules to achieve the order of evaluation you need.",
        "Измените порядок правил, чтобы получить нужный порядок выполнения.",
    ),
    (
        "Create a new failure detection rule.",
        "Создать новое правило обнаружения сбоев.",
    ),
    (
        "Delete a failure detection rule you don't need anymore.",
        "Удалить правило обнаружения сбоев, которое вам больше не нужно.",
    ),
    # failure-detection.md "Edit" sub-bullets (link-text EN-name, prose translated)
    (
        '* [Update an existing parameter set](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/put-parameter-set "Edit a failure detection parameter set via the Dynatrace API.") for failure detection rules.',
        '* [Update an existing parameter set](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/put-parameter-set "Редактирование набора параметров обнаружения сбоев через Dynatrace API.") для правил обнаружения сбоев.',
    ),
    (
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/change-id "Change the ID of a failure detection parameter set via the Dynatrace API.") of a parameter set.',
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/change-id "Изменение ID набора параметров обнаружения сбоев через Dynatrace API.") набора параметров.',
    ),
    (
        '* [Update an existing](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/put-rule "Edit a failure detection rule via the Dynatrace API.") failure detection rule.',
        '* [Update an existing](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/put-rule "Редактирование правила обнаружения сбоев через Dynatrace API.") правило обнаружения сбоев.',
    ),
    (
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/change-id "Change the ID of a failure detection rule via the Dynatrace API.") of a rule.',
        '* [Change the ID](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/change-id "Изменение ID правила обнаружения сбоев через Dynatrace API.") правила.',
    ),
    # ----- (A2) Related-topics title-attrs (link-text EN, target H1 not RU) -----
    (
        "Learn about service monitoring tuning options in Dynatrace.",
        "Узнайте о параметрах настройки мониторинга сервисов в Dynatrace.",
    ),
    (
        "Find out how Dynatrace Service Detection v1 detects and names different types of services.",
        "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.",
    ),
    (
        "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.",
        "Узнайте, какие типы ошибок сервиса Dynatrace обнаруживает автоматически, и как настроить параметры обнаружения сбоев под ваши конкретные требования.",
    ),
    (
        "Understand what opaque services are.",
        "Узнайте, что такое непрозрачные сервисы.",
    ),
    # ----- (D) endpoint intro one-liners -----
    (
        "The **Custom services** API enables you to manage the custom service detection rules.",
        "API **Custom services** позволяет управлять правилами обнаружения пользовательских сервисов.",
    ),
    (
        "The **Rule-based service detection** API enables you to manage the configuration of service detection rules.",
        "API **Rule-based service detection** позволяет управлять конфигурацией правил обнаружения сервисов.",
    ),
    (
        "Lists all custom service rules available in your Dynatrace environment.",
        "Выводит список всех правил пользовательских сервисов, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Gets parameters of the specified custom service rule.",
        "Возвращает параметры указанного правила пользовательского сервиса.",
    ),
    (
        "Creates a new custom service rule.",
        "Создаёт новое правило пользовательского сервиса.",
    ),
    (
        "Deletes the specified custom service rule.",
        "Удаляет указанное правило пользовательского сервиса.",
    ),
    (
        "Custom service rules are evaluated from top to bottom; the first matching rule applies.",
        "Правила пользовательских сервисов выполняются сверху вниз; применяется первое совпавшее правило.",
    ),
    (
        "This request reorders the custom service rules according to the order of the IDs in the body of the request. Rules that are omitted from the body of the request will retain their relative order but will be placed **after** all those present in the request.",
        "Этот запрос изменяет порядок правил пользовательских сервисов в соответствии с порядком ID в теле запроса. Правила, отсутствующие в теле запроса, сохраняют свой относительный порядок, но помещаются **после** всех правил, присутствующих в запросе.",
    ),
    (
        "Lists all service detection rules for full web requests.",
        "Выводит список всех правил обнаружения сервисов для полных веб-запросов.",
    ),
    (
        "Lists all service detection rules for full web services.",
        "Выводит список всех правил обнаружения сервисов для полных веб-сервисов.",
    ),
    (
        "Lists all service detection rules for opaque and external web requests.",
        "Выводит список всех правил обнаружения сервисов для непрозрачных и внешних веб-запросов.",
    ),
    (
        "Lists all service detection rules for opaque and external web services.",
        "Выводит список всех правил обнаружения сервисов для непрозрачных и внешних веб-сервисов.",
    ),
    (
        "Shows the properties of the specified service detection rule for full web requests.",
        "Показывает свойства указанного правила обнаружения сервисов для полных веб-запросов.",
    ),
    (
        "Shows the properties of the specified service detection rule for full web services.",
        "Показывает свойства указанного правила обнаружения сервисов для полных веб-сервисов.",
    ),
    (
        "Shows the properties of the specified service detection rule for opaque and external web requests.",
        "Показывает свойства указанного правила обнаружения сервисов для непрозрачных и внешних веб-запросов.",
    ),
    (
        "Shows the properties of the specified service detection rule for opaque and external web services.",
        "Показывает свойства указанного правила обнаружения сервисов для непрозрачных и внешних веб-сервисов.",
    ),
    (
        "Creates a new service detection rule for full web requests.",
        "Создаёт новое правило обнаружения сервисов для полных веб-запросов.",
    ),
    (
        "Creates a new service detection rule for full web services.",
        "Создаёт новое правило обнаружения сервисов для полных веб-сервисов.",
    ),
    (
        "Creates a new service detection rule for opaque and external web requests.",
        "Создаёт новое правило обнаружения сервисов для непрозрачных и внешних веб-запросов.",
    ),
    (
        "Creates a new service detection rule for opaque and external web services.",
        "Создаёт новое правило обнаружения сервисов для непрозрачных и внешних веб-сервисов.",
    ),
    (
        "Updates an existing service detection rule for full web requests.",
        "Обновляет существующее правило обнаружения сервисов для полных веб-запросов.",
    ),
    (
        "Updates an existing service detection rule for full web services.",
        "Обновляет существующее правило обнаружения сервисов для полных веб-сервисов.",
    ),
    (
        "Updates an existing service detection rule for opaque and external web requests.",
        "Обновляет существующее правило обнаружения сервисов для непрозрачных и внешних веб-запросов.",
    ),
    (
        "Updates an existing service detection rule for opaque and external web services.",
        "Обновляет существующее правило обнаружения сервисов для непрозрачных и внешних веб-сервисов.",
    ),
    (
        "Deletes the specified service detection rule for full web requests.",
        "Удаляет указанное правило обнаружения сервисов для полных веб-запросов.",
    ),
    (
        "Deletes the specified service detection rule for full web services.",
        "Удаляет указанное правило обнаружения сервисов для полных веб-сервисов.",
    ),
    (
        "Deletes the specified service detection rule for opaque and external web requests.",
        "Удаляет указанное правило обнаружения сервисов для непрозрачных и внешних веб-запросов.",
    ),
    (
        "Deletes the specified service detection rule for opaque web services.",
        "Удаляет указанное правило обнаружения сервисов для непрозрачных веб-сервисов.",
    ),
    (
        "Reorders the service detection rules for full web requests according to the order of the IDs in the body of the request.",
        "Изменяет порядок правил обнаружения сервисов для полных веб-запросов в соответствии с порядком ID в теле запроса.",
    ),
    (
        "Reorders the service detection rules for full web services according to the order of the IDs in the body of the request.",
        "Изменяет порядок правил обнаружения сервисов для полных веб-сервисов в соответствии с порядком ID в теле запроса.",
    ),
    (
        "Reorders the service detection rules for opaque and external web requests according to the order of the IDs in the body of the request.",
        "Изменяет порядок правил обнаружения сервисов для непрозрачных и внешних веб-запросов в соответствии с порядком ID в теле запроса.",
    ),
    (
        "Reorders the service detection rules for external and opaque web services to the order of the IDs in the body of the request.",
        "Изменяет порядок правил обнаружения сервисов для внешних и непрозрачных веб-сервисов в соответствии с порядком ID в теле запроса.",
    ),
    (
        "Rules that are omitted from the body of the request retain their relative order but are placed after all those present in the request.",
        "Правила, отсутствующие в теле запроса, сохраняют свой относительный порядок, но помещаются после всех правил, присутствующих в запросе.",
    ),
    (
        "Gets the specified failure detection parameter set.",
        "Возвращает указанный набор параметров обнаружения сбоев.",
    ),
    (
        "Gets the specified failure detection rule.",
        "Возвращает указанное правило обнаружения сбоев.",
    ),
    (
        "Lists all available failure detection parameter sets.",
        "Выводит список всех доступных наборов параметров обнаружения сбоев.",
    ),
    (
        "Lists all available failure detection rules.",
        "Выводит список всех доступных правил обнаружения сбоев.",
    ),
    (
        "Creates a new failure detection parameter set.",
        "Создаёт новый набор параметров обнаружения сбоев.",
    ),
    (
        "Creates a new failure detection rule.",
        "Создаёт новое правило обнаружения сбоев.",
    ),
    (
        "Updates the specified failure detection parameter set.",
        "Обновляет указанный набор параметров обнаружения сбоев.",
    ),
    (
        "Updates the specified failure detection rule.",
        "Обновляет указанное правило обнаружения сбоев.",
    ),
    (
        "Deletes the specified failure detection parameter set.",
        "Удаляет указанный набор параметров обнаружения сбоев.",
    ),
    (
        "Deletes the specified failure detection rule.",
        "Удаляет указанное правило обнаружения сбоев.",
    ),
    (
        "Changes the ID of the specified failure detection parameter set.",
        "Изменяет ID указанного набора параметров обнаружения сбоев.",
    ),
    (
        "Changes the ID of the specified failure detection rule.",
        "Изменяет ID указанного правила обнаружения сбоев.",
    ),
    (
        "Reorders the failure detection rules according to the order of the IDs in the body of the request.",
        "Изменяет порядок правил обнаружения сбоев в соответствии с порядком ID в теле запроса.",
    ),
    # put-rule custom-services H2 quirk
    ("## PUT a custom service rule", "## PUT a custom service rule"),
    # ----- (E) json-models structure (L3G pattern; EN tab-labels stay EN) -----
    (
        "JSON models of the **Service detection rules** API vary greatly, depending on the **type** of some objects. Here you can find JSON models for each variation.",
        "JSON-модели API **Service detection rules** сильно различаются в зависимости от поля **type** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.",
    ),
    (
        "JSON models of the **Failure detection rules** API vary greatly, depending on the **type** of some objects. Here you can find JSON models for each variation.",
        "JSON-модели API **Failure detection rules** сильно различаются в зависимости от поля **type** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.",
    ),
    (
        "## Variations of the `ServiceDetectionRule` object",
        "## Вариации объекта `ServiceDetectionRule`",
    ),
    (
        "## Variations of the `CompareOperation` object",
        "## Вариации объекта `CompareOperation`",
    ),
    (
        "## Variations of the `TransformationBase` object",
        "## Вариации объекта `TransformationBase`",
    ),
    (
        "## Variations of the `FdpTagPredicate` object",
        "## Вариации объекта `FdpTagPredicate`",
    ),
    (
        "## Variations of the `FdcPredicate` object",
        "## Вариации объекта `FdcPredicate`",
    ),
    (
        "The `ServiceDetectionRule` object is the base for all service detection rules. The actual set of fields depends on the **type** of the rule.",
        "Объект `ServiceDetectionRule` является базовым для всех правил обнаружения сервисов. Фактический набор полей зависит от поля **type** правила.",
    ),
    (
        "The `CompareOperation` object is the base for all comparison operations. The actual set of fields depends on the **type** of the comparison.",
        "Объект `CompareOperation` является базовым для всех операций сравнения. Фактический набор полей зависит от поля **type** сравнения.",
    ),
    (
        "The `TransformationBase` object is the base for all transformation operations. The actual set of fields depends on the **type** of the transformation.",
        "Объект `TransformationBase` является базовым для всех операций преобразования. Фактический набор полей зависит от поля **type** преобразования.",
    ),
    (
        "The `FdpTagPredicate` object is the base of tag conditions for failure detection parameter sets. The actual set of fields depends on the **type** of the condition.",
        "Объект `FdpTagPredicate` является базовым для условий по тегам в наборах параметров обнаружения сбоев. Фактический набор полей зависит от поля **type** условия.",
    ),
    (
        "The `FdcPredicate` object is the base for predicates of a failure detection rule's condition. The actual set of fields depends on the **type** of the condition.",
        "Объект `FdcPredicate` является базовым для предикатов условия правила обнаружения сбоев. Фактический набор полей зависит от поля **type** условия.",
    ),
    # ----- json-models Refer-to / type-field intro shared phrases -----
    (
        'Refer to [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API.") to find all JSON models that depend on the type of the model.',
        'Все JSON-модели, зависящие от типа модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Изучите вариации JSON-моделей в Dynatrace API правил обнаружения сервисов.").',
    ),
    (
        'To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").',
        'Чтобы найти все вариации модели, зависящие от типа модели, смотрите [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Изучите вариации JSON-моделей в Dynatrace API обнаружения сбоев.").',
    ),
    (
        "The actual set of fields depends on the type of the transformation. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON models",
        "Фактический набор полей зависит от типа преобразования. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models",
    ),
    (
        "The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON models",
        "Фактический набор полей зависит от типа условия. Список фактических объектов см. в описании поля **type** или см. [Service detection API - JSON models",
    ),
    (
        "The predicate that tests the value of the tag.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models",
        "Предикат, проверяющий значение тега.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models",
    ),
    (
        "The predicate that tests the value of the attribute.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON models",
        "Предикат, проверяющий значение атрибута.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models",
    ),
    (
        "The predicate that tests the value of the tag.",
        "Предикат, проверяющий значение тега.",
    ),
    (
        "The predicate that tests the value of the attribute.",
        "Предикат, проверяющий значение атрибута.",
    ),
    (
        "Defines the actual set of fields depending on the value. See one of the following objects:",
        "Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:",
    ),
    (
        "The actual set of fields depends on the `type` of the transformation.",
        "Фактический набор полей зависит от поля `type` преобразования.",
    ),
    # ----- (H) NEW object headings -> #### Объект `X` -----
    ("#### The `FullWebRequestRule` object", "#### Объект `FullWebRequestRule`"),
    ("#### The `FullWebServiceRule` object", "#### Объект `FullWebServiceRule`"),
    (
        "#### The `OpaqueAndExternalWebRequestRule` object",
        "#### Объект `OpaqueAndExternalWebRequestRule`",
    ),
    (
        "#### The `OpaqueAndExternalWebServiceRule` object",
        "#### Объект `OpaqueAndExternalWebServiceRule`",
    ),
    ("#### The `ApplicationId` object", "#### Объект `ApplicationId`"),
    ("#### The `TransformationBase` object", "#### Объект `TransformationBase`"),
    (
        "#### The `ConditionsFullWebRequestAttributeTypeDto` object",
        "#### Объект `ConditionsFullWebRequestAttributeTypeDto`",
    ),
    (
        "#### The `ConditionsFullWebServiceAttributeTypeDto` object",
        "#### Объект `ConditionsFullWebServiceAttributeTypeDto`",
    ),
    (
        "#### The `ConditionsOpaqueAndExternalWebRequestAttributeTypeDto` object",
        "#### Объект `ConditionsOpaqueAndExternalWebRequestAttributeTypeDto`",
    ),
    (
        "#### The `ConditionsOpaqueAndExternalWebServiceAttributeTypeDto` object",
        "#### Объект `ConditionsOpaqueAndExternalWebServiceAttributeTypeDto`",
    ),
    ("#### The `CompareOperation` object", "#### Объект `CompareOperation`"),
    (
        "#### The `ContextRootTransformation` object",
        "#### Объект `ContextRootTransformation`",
    ),
    ("#### The `ContextRoot` object", "#### Объект `ContextRoot`"),
    ("#### The `ServerName` object", "#### Объект `ServerName`"),
    ("#### The `WebServiceNameSpace` object", "#### Объект `WebServiceNameSpace`"),
    ("#### The `WebServiceName` object", "#### Объект `WebServiceName`"),
    ("#### The `PublicDomainName` object", "#### Объект `PublicDomainName`"),
    ("#### The `Port` object", "#### Объект `Port`"),
    ("#### The `UrlPath` object", "#### Объект `UrlPath`"),
    (
        "#### The `StringContainsCompareOperation` object",
        "#### Объект `StringContainsCompareOperation`",
    ),
    (
        "#### The `StringEqualsCompareOperation` object",
        "#### Объект `StringEqualsCompareOperation`",
    ),
    (
        "#### The `StartsWithCompareOperation` object",
        "#### Объект `StartsWithCompareOperation`",
    ),
    (
        "#### The `EndsWithCompareOperation` object",
        "#### Объект `EndsWithCompareOperation`",
    ),
    (
        "#### The `ExistsCompareOperation` object",
        "#### Объект `ExistsCompareOperation`",
    ),
    (
        "#### The `IpInRangeCompareOperation` object",
        "#### Объект `IpInRangeCompareOperation`",
    ),
    (
        "#### The `IntEqualsCompareOperation` object",
        "#### Объект `IntEqualsCompareOperation`",
    ),
    (
        "#### The `LessThanCompareOperation` object",
        "#### Объект `LessThanCompareOperation`",
    ),
    (
        "#### The `GreaterThanCompareOperation` object",
        "#### Объект `GreaterThanCompareOperation`",
    ),
    ("#### The `BeforeTransformation` object", "#### Объект `BeforeTransformation`"),
    ("#### The `AfterTransformation` object", "#### Объект `AfterTransformation`"),
    ("#### The `BetweenTransformation` object", "#### Объект `BetweenTransformation`"),
    (
        "#### The `ReplaceBetweenTransformation` object",
        "#### Объект `ReplaceBetweenTransformation`",
    ),
    (
        "#### The `RemoveNumbersTransformation` object",
        "#### Объект `RemoveNumbersTransformation`",
    ),
    (
        "#### The `RemoveCreditCardNumbersTransformation` object",
        "#### Объект `RemoveCreditCardNumbersTransformation`",
    ),
    (
        "#### The `RemoveIBANsTransformation` object",
        "#### Объект `RemoveIBANsTransformation`",
    ),
    (
        "#### The `RemoveIPsTransformation` object",
        "#### Объект `RemoveIPsTransformation`",
    ),
    (
        "#### The `SplitSelectTransformation` object",
        "#### Объект `SplitSelectTransformation`",
    ),
    (
        "#### The `TakeSegmentsTransformation` object",
        "#### Объект `TakeSegmentsTransformation`",
    ),
    ("#### The `CustomService` object", "#### Объект `CustomService`"),
    ("#### The `DetectionRule` object", "#### Объект `DetectionRule`"),
    ("#### The `MethodRule` object", "#### Объект `MethodRule`"),
    (
        "#### The `FailureDetectionParameterSet` object",
        "#### Объект `FailureDetectionParameterSet`",
    ),
    ("#### The `ExceptionPattern` object", "#### Объект `ExceptionPattern`"),
    ("#### The `FdpTagCondition` object", "#### Объект `FdpTagCondition`"),
    ("#### The `FdpTagPredicate` object", "#### Объект `FdpTagPredicate`"),
    (
        "#### The `FdpTagStringStartsWith` object",
        "#### Объект `FdpTagStringStartsWith`",
    ),
    ("#### The `FdpTagStringEquals` object", "#### Объект `FdpTagStringEquals`"),
    ("#### The `FdpTagStringEndsWith` object", "#### Объект `FdpTagStringEndsWith`"),
    (
        "#### The `FdpTagStringContainsSubstring` object",
        "#### Объект `FdpTagStringContainsSubstring`",
    ),
    ("#### The `FdpTagIntegerEquals` object", "#### Объект `FdpTagIntegerEquals`"),
    (
        "#### The `FdpTagIntegerLessThanOrEqual` object",
        "#### Объект `FdpTagIntegerLessThanOrEqual`",
    ),
    ("#### The `FdpTagIntegerLessThan` object", "#### Объект `FdpTagIntegerLessThan`"),
    (
        "#### The `FdpTagIntegerGreaterThanOrEqual` object",
        "#### Объект `FdpTagIntegerGreaterThanOrEqual`",
    ),
    (
        "#### The `FdpTagIntegerGreaterThan` object",
        "#### Объект `FdpTagIntegerGreaterThan`",
    ),
    ("#### The `FdpTagDoubleEquals` object", "#### Объект `FdpTagDoubleEquals`"),
    (
        "#### The `FdpTagDoubleLessThanOrEqual` object",
        "#### Объект `FdpTagDoubleLessThanOrEqual`",
    ),
    ("#### The `FdpTagDoubleLessThan` object", "#### Объект `FdpTagDoubleLessThan`"),
    (
        "#### The `FdpTagDoubleGreaterThanOrEqual` object",
        "#### Объект `FdpTagDoubleGreaterThanOrEqual`",
    ),
    (
        "#### The `FdpTagDoubleGreaterThan` object",
        "#### Объект `FdpTagDoubleGreaterThan`",
    ),
    ("#### The `FailureDetectionRule` object", "#### Объект `FailureDetectionRule`"),
    (
        "#### The `FailureDetectionCondition` object",
        "#### Объект `FailureDetectionCondition`",
    ),
    ("#### The `FdcPredicate` object", "#### Объект `FdcPredicate`"),
    (
        "#### The `FdcPredicateStringEquals` object",
        "#### Объект `FdcPredicateStringEquals`",
    ),
    (
        "#### The `FdcPredicateStringStartsWith` object",
        "#### Объект `FdcPredicateStringStartsWith`",
    ),
    (
        "#### The `FdcPredicateStringEndsWith` object",
        "#### Объект `FdcPredicateStringEndsWith`",
    ),
    (
        "#### The `FdcPredicateStringContains` object",
        "#### Объект `FdcPredicateStringContains`",
    ),
    (
        "#### The `FdcPredicateIntegerEquals` object",
        "#### Объект `FdcPredicateIntegerEquals`",
    ),
    (
        "#### The `FdcPredicateIntegerLessThanOrEqual` object",
        "#### Объект `FdcPredicateIntegerLessThanOrEqual`",
    ),
    (
        "#### The `FdcPredicateIntegerLessThan` object",
        "#### Объект `FdcPredicateIntegerLessThan`",
    ),
    (
        "#### The `FdcPredicateIntegerGreaterThanOrEqual` object",
        "#### Объект `FdcPredicateIntegerGreaterThanOrEqual`",
    ),
    (
        "#### The `FdcPredicateIntegerGreaterThan` object",
        "#### Объект `FdcPredicateIntegerGreaterThan`",
    ),
    (
        "#### The `FdcPredicateLongEquals` object",
        "#### Объект `FdcPredicateLongEquals`",
    ),
    (
        "#### The `FdcPredicateLongLessThanOrEqual` object",
        "#### Объект `FdcPredicateLongLessThanOrEqual`",
    ),
    (
        "#### The `FdcPredicateLongLessThan` object",
        "#### Объект `FdcPredicateLongLessThan`",
    ),
    (
        "#### The `FdcPredicateLongGreaterThanOrEqual` object",
        "#### Объект `FdcPredicateLongGreaterThanOrEqual`",
    ),
    (
        "#### The `FdcPredicateLongGreaterThan` object",
        "#### Объект `FdcPredicateLongGreaterThan`",
    ),
    (
        "#### The `FdcPredicateTagKeyEquals` object",
        "#### Объект `FdcPredicateTagKeyEquals`",
    ),
    ("#### The `FdcPredicateTagEquals` object", "#### Объект `FdcPredicateTagEquals`"),
    (
        "#### The `FdcPredicateServiceTypeEquals` object",
        "#### Объект `FdcPredicateServiceTypeEquals`",
    ),
    (
        "#### The `FdcPredicateManagementZonesContainsAll` object",
        "#### Объект `FdcPredicateManagementZonesContainsAll`",
    ),
    ("#### The `FdpSelectionRuleOrder` object", "#### Объект `FdpSelectionRuleOrder`"),
    # ----- (I) object/section intro descriptions (newline-anchored where needed) -----
    (
        "\nThe service detection rule of the `FULL_WEB_REQUEST` type.\n",
        "\nПравило обнаружения сервисов типа `FULL_WEB_REQUEST`.\n",
    ),
    (
        "\nThe service detection rule of the `FULL_WEB_SERVICE` type.\n",
        "\nПравило обнаружения сервисов типа `FULL_WEB_SERVICE`.\n",
    ),
    (
        "\nThe service detection rule of the `OPAQUE_AND_EXTERNAL_WEB_REQUEST` type.\n",
        "\nПравило обнаружения сервисов типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.\n",
    ),
    (
        "\nThe service detection rule of the `OPAQUE_AND_EXTERNAL_WEB_SERVICE` type\n",
        "\nПравило обнаружения сервисов типа `OPAQUE_AND_EXTERNAL_WEB_SERVICE`\n",
    ),
    (
        "If you have a condition with the **attributeType** set to `FRAMEWORK`, the **values** field from **compareOperations** is limited to the following possible values:",
        "Если у вас есть условие с **attributeType**, установленным в `FRAMEWORK`, поле **values** из **compareOperations** ограничено следующими возможными значениями:",
    ),
    (
        "A condition of the service detection rule.",
        "Условие правила обнаружения сервисов.",
    ),
    ("\nThe condition of the rule.\n", "\nУсловие правила.\n"),
    (
        "\nThe contribution to the service ID calculation from the detected application ID.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного ID приложения.\n",
    ),
    (
        "\nConfiguration of transformation of the detected value.\n",
        "\nКонфигурация преобразования обнаруженного значения.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected context root.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного context root.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected server name.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного имени сервера.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected web service name.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the detected web service name space.\n",
        "\nВклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the port, where the web request has been detected.\n",
        "\nВклад в расчёт ID сервиса от порта, на котором обнаружен веб-запрос.\n",
    ),
    (
        "\nThe contribution to the service ID calculation from the domain name where the web request has been detected.\n",
        "\nВклад в расчёт ID сервиса от доменного имени, на котором обнаружен веб-запрос.\n",
    ),
    (
        "\nThe contribution from the URL, where the web request has been detected, into service ID calculation.\n",
        "\nВклад в расчёт ID сервиса от URL, на котором обнаружен веб-запрос.\n",
    ),
    (
        "The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.",
        "Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.",
    ),
    (
        "You have two mutually exclusive options:",
        "Есть два взаимоисключающих варианта:",
    ),
    ("You have two options:", "Есть два варианта:"),
    (
        "* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.",
        "* Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**.",
    ),
    (
        "* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "* Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "* Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field.",
        "* Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**.",
    ),
    (
        "* Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.",
        "* Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "You can use one or both options. If you use both, the transformation applies to the modified URL.",
        "Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.",
    ),
    (
        "If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.",
        "Если указано несколько преобразований, они обрабатываются последовательно сверху вниз. Каждое преобразование применяется к результату предыдущего преобразования. Например, второе преобразование применяется к результату первого преобразования.",
    ),
    # per-type CompareOperation intros
    (
        "The condition of the `STRING_CONTAINS` type.",
        "Условие типа `STRING_CONTAINS`.",
    ),
    ("The condition of the `STRING_EQUALS` type.", "Условие типа `STRING_EQUALS`."),
    ("The condition of the `STARTS_WITH` type.", "Условие типа `STARTS_WITH`."),
    ("The condition of the `ENDS_WITH` type.", "Условие типа `ENDS_WITH`."),
    ("The condition of the `EXISTS` type.", "Условие типа `EXISTS`."),
    ("The condition of the `IP_IN_RANGE` type.", "Условие типа `IP_IN_RANGE`."),
    ("The condition of the `INT_EQUALS` type.", "Условие типа `INT_EQUALS`."),
    ("The condition of the `LESS_THAN` type.", "Условие типа `LESS_THAN`."),
    ("The condition of the `GREATER_THAN` type.", "Условие типа `GREATER_THAN`."),
    (
        "The condition checks whether the string value contains the specified text.",
        "Условие проверяет, содержит ли строковое значение указанный текст.",
    ),
    (
        "The condition checks whether the string value equals the specified text.",
        "Условие проверяет, равно ли строковое значение указанному тексту.",
    ),
    (
        "The condition checks whether the string value starts with the specified text.",
        "Условие проверяет, начинается ли строковое значение с указанного текста.",
    ),
    (
        "The condition checks whether the string value ends with the specified text.",
        "Условие проверяет, заканчивается ли строковое значение указанным текстом.",
    ),
    (
        "The condition checks whether the specified attribute exists.",
        "Условие проверяет, существует ли указанный атрибут.",
    ),
    (
        "The condition checks whether the IP address belongs to a specified range.",
        "Условие проверяет, принадлежит ли IP-адрес указанному диапазону.",
    ),
    (
        "The condition checks whether the integer value equals the specified value.",
        "Условие проверяет, равно ли целочисленное значение указанному значению.",
    ),
    (
        "The condition checks whether the integer value is less than the specified value.",
        "Условие проверяет, меньше ли целочисленное значение указанного значения.",
    ),
    (
        "The condition checks whether the integer value is greater than the specified value.",
        "Условие проверяет, больше ли целочисленное значение указанного значения.",
    ),
    # per-type Transformation intros (source-quirk: .This / .The no-space mirrored)
    ("The transformation of the `BEFORE` type.", "Преобразование типа `BEFORE`."),
    (
        "The transformation of the `AFTER` type.The transformation removes everything before the specified delimiter and keeps the value after it.",
        "Преобразование типа `AFTER`.Преобразование удаляет всё до указанного разделителя и сохраняет значение после него.",
    ),
    (
        "The transformation of the `BETWEEN` type.The transformation keeps value between the specified delimiters and removes everything outside them.",
        "Преобразование типа `BETWEEN`.Преобразование сохраняет значение между указанными разделителями и удаляет всё за их пределами.",
    ),
    (
        "The transformation of the `REPLACE_BETWEEN` type.",
        "Преобразование типа `REPLACE_BETWEEN`.",
    ),
    (
        "The transformation of the `REMOVE_NUMBERS` type.",
        "Преобразование типа `REMOVE_NUMBERS`.",
    ),
    (
        "The transformation of the `REMOVE_CREDIT_CARDS` type.",
        "Преобразование типа `REMOVE_CREDIT_CARDS`.",
    ),
    (
        "The transformation of the `REMOVE_IBANS` type.",
        "Преобразование типа `REMOVE_IBANS`.",
    ),
    (
        "The transformation of the `REMOVE_IPS` type.",
        "Преобразование типа `REMOVE_IPS`.",
    ),
    (
        "The transformation of the `SPLIT_SELECT` type.",
        "Преобразование типа `SPLIT_SELECT`.",
    ),
    (
        "The transformation of the `TAKE_SEGMENTS` type.",
        "Преобразование типа `TAKE_SEGMENTS`.",
    ),
    (
        "The transformation keeps the value before the specified delimiter and removes everything after it.",
        "Преобразование сохраняет значение до указанного разделителя и удаляет всё после него.",
    ),
    (
        "The transformation replaces the content in between specified delimiters with the specified value. The rest of the string remains intact.",
        "Преобразование заменяет содержимое между указанными разделителями указанным значением. Остальная часть строки остаётся без изменений.",
    ),
    (
        "The transformation removes any numbers from the detected value.",
        "Преобразование удаляет любые числа из обнаруженного значения.",
    ),
    (
        "The transformation automatically detects and removes credit card numbers. No additional parameters needed.",
        "Преобразование автоматически обнаруживает и удаляет номера кредитных карт. Дополнительные параметры не нужны.",
    ),
    (
        "The transformation automatically detects and removes International Bank Account Numbers (IBAN). No additional parameters needed.",
        "Преобразование автоматически обнаруживает и удаляет международные номера банковских счетов (IBAN). Дополнительные параметры не нужны.",
    ),
    (
        "The transformation automatically detects and removes IP addresses. No additional parameters needed.",
        "Преобразование автоматически обнаруживает и удаляет IP-адреса. Дополнительные параметры не нужны.",
    ),
    (
        "The transformation splits the detected value into an array and keeps the specified element of the array.",
        "Преобразование разбивает обнаруженное значение на массив и сохраняет указанный элемент массива.",
    ),
    (
        "The transformation splits the detected value into an array and keeps the specified number of first or last elements.",
        "Преобразование разбивает обнаруженное значение на массив и сохраняет указанное количество первых или последних элементов.",
    ),
    # FdpTag / Fdc predicate intros (per type)
    (
        "The predicate of the `STRING_STARTS_WITH` type. It checks whether the tag (which is a string) starts with the reference value.",
        "Предикат типа `STRING_STARTS_WITH`. Он проверяет, начинается ли тег (являющийся строкой) с эталонного значения.",
    ),
    (
        "The predicate of the `STRING_EQUALS` type. It checks whether the tag (which is a string) equals the reference value.",
        "Предикат типа `STRING_EQUALS`. Он проверяет, равен ли тег (являющийся строкой) эталонному значению.",
    ),
    (
        "The predicate of the `STRING_ENDS_WITH` type. It checks whether the tag (which is a string) ends with the reference value.",
        "Предикат типа `STRING_ENDS_WITH`. Он проверяет, заканчивается ли тег (являющийся строкой) эталонным значением.",
    ),
    (
        "The predicate of the `STRING_CONTAINS_SUBSTRING` type. It checks whether the tag (which is a string) contains the reference value.",
        "Предикат типа `STRING_CONTAINS_SUBSTRING`. Он проверяет, содержит ли тег (являющийся строкой) эталонное значение.",
    ),
    (
        "The predicate of the `INTEGER_EQUALS` type. It checks whether the tag (which is an integer) equals the reference value.",
        "Предикат типа `INTEGER_EQUALS`. Он проверяет, равен ли тег (являющийся целым числом) эталонному значению.",
    ),
    (
        "The predicate of the `INTEGER_LESS_THAN` type. It checks whether the tag (which is an integer) is less than the reference value.",
        "Предикат типа `INTEGER_LESS_THAN`. Он проверяет, меньше ли тег (являющийся целым числом) эталонного значения.",
    ),
    (
        "The predicate of the `INTEGER_LESS_THAN_OR_EQUAL` type. It checks whether the tag (which is an integer) is less than or equals the reference value.",
        "Предикат типа `INTEGER_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли тег (являющийся целым числом) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `INTEGER_GREATER_THAN` type. It checks whether the tag (which is an integer) is greater than the reference value.",
        "Предикат типа `INTEGER_GREATER_THAN`. Он проверяет, больше ли тег (являющийся целым числом) эталонного значения.",
    ),
    (
        "The predicate of the `INTEGER_GREATER_THAN_OR_EQUAL` type. It checks whether the tag (which is an integer) is greater than or equals the reference value.",
        "Предикат типа `INTEGER_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли тег (являющийся целым числом) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `DOUBLE_EQUALS` type. It checks whether the tag (which is a double) equals the reference value.",
        "Предикат типа `DOUBLE_EQUALS`. Он проверяет, равен ли тег (являющийся числом с плавающей точкой) эталонному значению.",
    ),
    (
        "The predicate of the `DOUBLE_LESS_THAN` type. It checks whether the tag (which is a double) is less than the reference value.",
        "Предикат типа `DOUBLE_LESS_THAN`. Он проверяет, меньше ли тег (являющийся числом с плавающей точкой) эталонного значения.",
    ),
    (
        "The predicate of the `DOUBLE_LESS_THAN_OR_EQUAL` type. It checks whether the tag (which is a double) is less than or equals the reference value.",
        "Предикат типа `DOUBLE_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли тег (являющийся числом с плавающей точкой) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `DOUBLE_GREATER_THAN` type. It checks whether the tag (which is a double) is greater than the reference value.",
        "Предикат типа `DOUBLE_GREATER_THAN`. Он проверяет, больше ли тег (являющийся числом с плавающей точкой) эталонного значения.",
    ),
    (
        "The predicate of the `DOUBLE_GREATER_THAN_OR_EQUAL` type. It checks whether the tag (which is a double) is greater than or equals the reference value.",
        "Предикат типа `DOUBLE_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли тег (являющийся числом с плавающей точкой) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `STRING_EQUALS` type. It checks whether the attribute (which is a string) equals one of the reference values.",
        "Предикат типа `STRING_EQUALS`. Он проверяет, равен ли атрибут (являющийся строкой) одному из эталонных значений.",
    ),
    (
        "The predicate of the `STRING_STARTS_WITH` type. It checks whether the attribute (which is a string) starts with one of the reference values.",
        "Предикат типа `STRING_STARTS_WITH`. Он проверяет, начинается ли атрибут (являющийся строкой) с одного из эталонных значений.",
    ),
    (
        "The predicate of the `STRING_ENDS_WITH`  type. It checks whether the attribute (which is a string) ends with one of the reference values.",
        "Предикат типа `STRING_ENDS_WITH`.  Он проверяет, заканчивается ли атрибут (являющийся строкой) одним из эталонных значений.",
    ),
    (
        "The predicate of the `STRING_CONTAINS_SUBSTRING` type. It checks whether the attribute (which is a string) contains one of the reference values.",
        "Предикат типа `STRING_CONTAINS_SUBSTRING`. Он проверяет, содержит ли атрибут (являющийся строкой) одно из эталонных значений.",
    ),
    (
        "The predicate of the `INTEGER_EQUALS` type. It checks whether the attribute (which is an integer) equals one of the reference values.",
        "Предикат типа `INTEGER_EQUALS`. Он проверяет, равен ли атрибут (являющийся целым числом) одному из эталонных значений.",
    ),
    (
        "The predicate of the `INTEGER_LESS_THAN` type. It checks whether the attribute (which is an integer) is less than the reference value.",
        "Предикат типа `INTEGER_LESS_THAN`. Он проверяет, меньше ли атрибут (являющийся целым числом) эталонного значения.",
    ),
    (
        "The predicate of the `INTEGER_LESS_THAN_OR_EQUAL` type. It checks whether the attribute (which is an integer) is less than or equals the reference value.",
        "Предикат типа `INTEGER_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли атрибут (являющийся целым числом) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `INTEGER_GREATER_THAN` type. It checks whether the attribute (which is an integer) is greater than the reference value.",
        "Предикат типа `INTEGER_GREATER_THAN`. Он проверяет, больше ли атрибут (являющийся целым числом) эталонного значения.",
    ),
    (
        "The predicate of the `INTEGER_GREATER_THAN_OR_EQUAL` type. It checks whether the attribute (which is an integer) is greater than or equals the reference value.",
        "Предикат типа `INTEGER_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли атрибут (являющийся целым числом) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `LONG_EQUALS` type. It checks whether the attribute (which is a long) equals one of the reference values.",
        "Предикат типа `LONG_EQUALS`. Он проверяет, равен ли атрибут (являющийся long) одному из эталонных значений.",
    ),
    (
        "The predicate of the `LONG_LESS_THAN` type. It checks whether the attribute (which is a long) is less than the reference value.",
        "Предикат типа `LONG_LESS_THAN`. Он проверяет, меньше ли атрибут (являющийся long) эталонного значения.",
    ),
    (
        "The predicate of the `LONG_LESS_THAN_OR_EQUAL` type. It checks whether the attribute (which is a long) is less than or equals the reference value.",
        "Предикат типа `LONG_LESS_THAN_OR_EQUAL`. Он проверяет, меньше ли атрибут (являющийся long) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `LONG_GREATER_THAN` type. It checks whether the attribute (which is a long) is greater than the reference value.",
        "Предикат типа `LONG_GREATER_THAN`. Он проверяет, больше ли атрибут (являющийся long) эталонного значения.",
    ),
    (
        "The predicate of the `LONG_GREATER_THAN_OR_EQUAL` type. It checks whether the attribute (which is a long) is greater than or equals the reference value.",
        "Предикат типа `LONG_GREATER_THAN_OR_EQUAL`. Он проверяет, больше ли атрибут (являющийся long) эталонного значения или равен ему.",
    ),
    (
        "The predicate of the `TAG_KEY_EQUALS` type. It checks whether the attribute (which is the key of a tag) equals one of the reference values.",
        "Предикат типа `TAG_KEY_EQUALS`. Он проверяет, равен ли атрибут (являющийся ключом тега) одному из эталонных значений.",
    ),
    (
        "The predicate of the `TAG_EQUALS` type. It checks whether the attribute (which is a key:value pair) equals one of the reference values.",
        "Предикат типа `TAG_EQUALS`. Он проверяет, равен ли атрибут (являющийся парой ключ:значение) одному из эталонных значений.",
    ),
    (
        "The reference value is a key:value pair, consisting of a key and a value that are at the **same position** in the respective list.",
        "Эталонное значение это пара ключ:значение, состоящая из ключа и значения, находящихся на **одной и той же позиции** в соответствующих списках.",
    ),
    (
        "The predicate of the `SERVICE_TYPE_EQUALS` type. It checks whether the attribute (which is the type of the service) equals one of the reference values.",
        "Предикат типа `SERVICE_TYPE_EQUALS`. Он проверяет, равен ли атрибут (являющийся типом сервиса) одному из эталонных значений.",
    ),
    (
        "The predicate of the `MANAGEMENT_ZONES_CONTAINS_ALL` type. It checks whether the attribute (which is a set of management zones) contains **all** the reference values.",
        "Предикат типа `MANAGEMENT_ZONES_CONTAINS_ALL`. Он проверяет, содержит ли атрибут (являющийся набором зон управления) **все** эталонные значения.",
    ),
    # CustomService / FailureDetection object intros
    (
        "Configuration of the failure detection rule.",
        "Конфигурация правила обнаружения сбоев.",
    ),
    (
        "The condition of the failure detection rule.",
        "Условие правила обнаружения сбоев.",
    ),
    (
        "\nA set of failure detection parameters (FDP).\n",
        "\nНабор параметров обнаружения сбоев (FDP).\n",
    ),
    (
        "These parameters define the conditions of failure and success.",
        "Эти параметры определяют условия сбоя и успеха.",
    ),
    (
        "\nA list of faulty exceptions.\n",
        "\nСписок ошибочных исключений.\n",
    ),
    (
        "If an exception on *any* node of the service matches *any* of these patterns it is considered a failure.",
        "Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.",
    ),
    (
        "Configuration of the tag condition in the FDP set.",
        "Конфигурация условия по тегу в наборе FDP.",
    ),
    (
        "The order of the rules in the ruleset.",
        "Порядок правил в наборе правил.",
    ),
    # ----- (M) parameter (path/query/body) cell descriptions -----
    (
        "The ID of the required service detection rule.",
        "ID требуемого правила обнаружения сервисов.",
    ),
    (
        "The ID of the service detection rule to be deleted.",
        "ID правила обнаружения сервисов, которое нужно удалить.",
    ),
    ("The ID of the rule to be updated.", "ID правила, которое нужно обновить."),
    (
        "The position of the new rule:  * `APPEND`: at the bottom of the rule list. * `PREPEND`: at the top of the rule list.  If not set, the `APPEND` is used.",
        "Позиция нового правила:  * `APPEND`: внизу списка правил. * `PREPEND`: вверху списка правил.  Если не задано, используется `APPEND`.",
    ),
    (
        "The position of the new rule:  * `APPEND`: at the end of the rule list. * `PREPEND`: on top of the rule list.",
        "Позиция нового правила:  * `APPEND`: в конце списка правил. * `PREPEND`: вверху списка правил.",
    ),
    (
        "The JSON body of the request. Contains parameters of the new service detection rule.  You must not specify the ID of the rule!  The **order** field is ignored in this request. To enforce a particular order, use the `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder` request.",
        "JSON-тело запроса. Содержит параметры нового правила обнаружения сервисов.  Не указывайте ID правила!  Поле **order** игнорируется в этом запросе. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder`.",
    ),
    (
        "The JSON body of the request. Contains updated parameters of the service detection rule.  The **order** field is ignored in this request. To enforce a particular order, use the `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder` request.",
        "JSON-тело запроса. Содержит обновлённые параметры правила обнаружения сервисов.  Поле **order** игнорируется в этом запросе. Чтобы задать определённый порядок, используйте запрос `PUT /service/detectionRules/FULL_WEB_REQUEST/reorder`.",
    ),
    (
        "The JSON body of the request containing the service detection rules in the required order.",
        "JSON-тело запроса, содержащее правила обнаружения сервисов в требуемом порядке.",
    ),
    (
        "Technology of the required custom services.",
        "Технология требуемых пользовательских сервисов.",
    ),
    (
        "Technology of the custom service you're inquiring.",
        "Технология запрашиваемого пользовательского сервиса.",
    ),
    (
        "The ID of the custom service you're inquiring.",
        "ID запрашиваемого пользовательского сервиса.",
    ),
    (
        "Flag to include process group references to the response.  Process group references aren't compatible across environments.  `false` is used if the value is not set.",
        "Флаг включения ссылок на группы процессов в ответ.  Ссылки на группы процессов несовместимы между окружениями.  Если значение не задано, используется `false`.",
    ),
    (
        "Technology of the custom service to delete.",
        "Технология пользовательского сервиса, который нужно удалить.",
    ),
    (
        "The ID of the custom service to delete.",
        "ID пользовательского сервиса, который нужно удалить.",
    ),
    (
        "Technology of custom services to update.",
        "Технология пользовательских сервисов для обновления.",
    ),
    (
        "JSON body of the request containing the IDs of the custom services in the desired order. Any further properties (*name*, *description*) will be ignored.",
        "JSON-тело запроса, содержащее ID пользовательских сервисов в нужном порядке. Любые дополнительные свойства (*name*, *description*) игнорируются.",
    ),
    (
        "Technology of the new custom service.",
        "Технология нового пользовательского сервиса.",
    ),
    (
        "Order of the new custom service. Set to `PREPEND` to prepend it to the list, `APPEND` to append it. Defaults to `APPEND`.",
        "Порядок нового пользовательского сервиса. Установите `PREPEND`, чтобы добавить его в начало списка, или `APPEND`, чтобы добавить в конец. По умолчанию `APPEND`.",
    ),
    (
        "JSON body of the request containing definition of the new custom service.  You must not specify the IDs for the custom service or any of its rules. The *order* field is not allowed either.",
        "JSON-тело запроса, содержащее определение нового пользовательского сервиса.  Не указывайте ID для пользовательского сервиса или любого из его правил. Поле *order* также не допускается.",
    ),
    (
        "Technology of the custom service to update.",
        "Технология пользовательского сервиса для обновления.",
    ),
    (
        "The ID of the custom service to update.  The ID of the custom service in the body of the request must match this ID.",
        "ID пользовательского сервиса для обновления.  ID пользовательского сервиса в теле запроса должен совпадать с этим ID.",
    ),
    (
        "JSON body of the request containing updated definition of the custom service. If *order* is present, it will be used.",
        "JSON-тело запроса, содержащее обновлённое определение пользовательского сервиса. Если присутствует *order*, оно будет использовано.",
    ),
    (
        "The ID of the required failure detection parameter set. Needs to be a valid RFC 4122 UUID.",
        "ID требуемого набора параметров обнаружения сбоев. Должен быть валидным UUID по RFC 4122.",
    ),
    (
        "The ID of the required failure detection rule. Needs to be a valid RFC 4122 UUID.",
        "ID требуемого правила обнаружения сбоев. Должен быть валидным UUID по RFC 4122.",
    ),
    (
        "The JSON body of the request. Contains the new ID of the set. All other fields are ignored.",
        "JSON-тело запроса. Содержит новый ID набора. Все остальные поля игнорируются.",
    ),
    (
        "The JSON body of the request. Contains the new ID of the rule. All other fields are ignored.",
        "JSON-тело запроса. Содержит новый ID правила. Все остальные поля игнорируются.",
    ),
    (
        "The JSON body of the request. Contains the failure detection rules in the required order.",
        "JSON-тело запроса. Содержит правила обнаружения сбоев в требуемом порядке.",
    ),
    # ----- response-code cells (L101 substring keeps source period) -----
    (
        "Success. The new service detection rule has been created. The response body contains the ID of the rule.",
        "Успех. Новое правило обнаружения сервисов создано. Тело ответа содержит ID правила.",
    ),
    (
        "Success. The new service detection rule has been created. The response contains short representation of the rule, including the ID.",
        "Успех. Новое правило обнаружения сервисов создано. Тело ответа содержит краткое представление правила, включая ID.",
    ),
    (
        "Success. The service detection rule has been updated. Response doesn't have a body.",
        "Успех. Правило обнаружения сервисов обновлено. Ответ без тела.",
    ),
    (
        "Success. Service detection rules have been reordered. Response doesn't have a body.",
        "Успех. Порядок правил обнаружения сервисов изменён. Ответ без тела.",
    ),
    (
        "Success. The response contains properties of the specified rule.",
        "Успех. Тело ответа содержит свойства указанного правила.",
    ),
    (
        "Success. The response contains the ordered list of rules.",
        "Успех. Тело ответа содержит упорядоченный список правил.",
    ),
    (
        "Failed. The rule with the specified ID doesn't exist.",
        "Сбой. Правило с указанным ID не существует.",
    ),
    (
        "Failed. The specified entity doesn't exist.",
        "Сбой. Указанная сущность не существует.",
    ),
    (
        "Validated. The service detection rule is valid. Response doesn't have a body.",
        "Validated. Правило обнаружения сервисов валидно. Ответ без тела.",
    ),
    (
        "Success. Custom service has been created. Response contains the new service's ID and name.",
        "Успех. Пользовательский сервис создан. Тело ответа содержит ID и имя нового сервиса.",
    ),
    (
        "Success. The custom service has been created. Response contains the new service's ID and name.",
        "Успех. Пользовательский сервис создан. Тело ответа содержит ID и имя нового сервиса.",
    ),
    (
        "Success. Custom service has been updated. Response doesn't have a body.",
        "Успех. Пользовательский сервис обновлён. Ответ без тела.",
    ),
    (
        "Success. Custom services have been updated. Response doesn't have a body.",
        "Успех. Пользовательские сервисы обновлены. Ответ без тела.",
    ),
    (
        "Success. The failure detection parameter set has been updated. Response doesn't have a body.",
        "Успех. Набор параметров обнаружения сбоев обновлён. Ответ без тела.",
    ),
    (
        "Success. The failure detection rule has been updated. Response doesn't have a body.",
        "Успех. Правило обнаружения сбоев обновлено. Ответ без тела.",
    ),
    (
        "Success. The new failure detection parameter set has been created. The response contains the ID of the new set.",
        "Успех. Новый набор параметров обнаружения сбоев создан. Тело ответа содержит ID нового набора.",
    ),
    (
        "Success. The new failure detection rule has been created. The response contains the ID of the new rule.",
        "Успех. Новое правило обнаружения сбоев создано. Тело ответа содержит ID нового правила.",
    ),
    (
        "Success. The failure detection parameter set has been deleted. Response doesn't have a body.",
        "Успех. Набор параметров обнаружения сбоев удалён. Ответ без тела.",
    ),
    # ----- (O) element-cell descriptions (detection-rules/custom/failure) -----
    (
        "The contribution to the service ID calculation from the detected application ID.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного ID приложения.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "A list of conditions of the rule.  If several conditions are specified, the AND logic applies.",
        "Список условий правила.  Если указано несколько условий, применяется логика AND.",
    ),
    (
        "A list of conditions for the rule.  If several conditions are specified, the AND logic applies.",
        "Список условий правила.  Если указано несколько условий, применяется логика AND.",
    ),
    (
        "The contribution to the service ID calculation from the detected context root.  The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.  You have two options:  * Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field. * Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.  You can use one or both options. If you use both, the transformation applies to the modified URL.",
        "Вклад в расчёт ID сервиса от обнаруженного context root.  Context root это первый сегмент URL запроса после имени сервера. Например, в URL `www.dynatrace.com/support/help/dynatrace-api/` context root равен `support`.  Есть два варианта:  * Сохранить часть обнаруженного URL. Укажите количество сохраняемых сегментов в поле **segmentsToCopyFromUrlPath**. * Динамически преобразовать обнаруженный URL. Укажите параметры преобразования в поле **transformations**.  Можно использовать один или оба варианта. Если используются оба, преобразование применяется к изменённому URL.",
    ),
    ("A short description of the rule.", "Краткое описание правила."),
    (
        "The rule is enabled(`true`) or disabled (`false`).",
        "Правило включено (`true`) или отключено (`false`).",
    ),
    (
        "The rule is enabled (`true`) or disabled (`false`).",
        "Правило включено (`true`) или отключено (`false`).",
    ),
    ("The ID of the service detection rule.", "ID правила обнаружения сервисов."),
    (
        "The management zone (specified by the ID) of the process group for which this service detection rule should be created.  You can specify only 1 management zone here.",
        "Зона управления (указанная по ID) группы процессов, для которой должно быть создано это правило обнаружения сервисов.  Здесь можно указать только 1 зону управления.",
    ),
    ("The name of the rule.", "Имя правила."),
    (
        "The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies.",
        "Порядок правила в списке правил.  Правила выполняются сверху вниз. Применяется первое совпавшее правило.",
    ),
    (
        "The contribution to the service ID calculation from the detected server name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного имени сервера.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    ("The type of the service detection rule.", "Тип правила обнаружения сервисов."),
    (
        "The contribution to the service ID calculation from the detected web service name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного имени веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution to the service ID calculation from the detected web service name space.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от обнаруженного пространства имён веб-сервиса.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution to the service ID calculation from the port, where the web request has been detected.",
        "Вклад в расчёт ID сервиса от порта, на котором обнаружен веб-запрос.",
    ),
    (
        "The contribution to the service ID calculation from the domain name where the web request has been detected.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от доменного имени, на котором обнаружен веб-запрос.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "The contribution from the URL, where the web request has been detected, into service ID calculation.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.",
        "Вклад в расчёт ID сервиса от URL, на котором обнаружен веб-запрос.  Есть два взаимоисключающих варианта:  * Переопределить обнаруженное значение заданным статическим значением. Укажите новое значение в поле **valueOverride**. * Динамически преобразовать обнаруженное значение. Укажите параметры преобразования в поле **transformations**.",
    ),
    (
        "Detect the matching requests as full web services (`false`) or web request services (`true`).  Setting this field to `true` prevents detecting of matching requests as full web services. A web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate rule of the `FULL_WEB_REQUEST` type.  Default is `false`, detecting matching requests as full web services.",
        "Обнаруживать совпадающие запросы как полные веб-сервисы (`false`) или как сервисы веб-запросов (`true`).  Установка этого поля в `true` предотвращает обнаружение совпадающих запросов как полных веб-сервисов. Вместо этого создаётся сервис веб-запросов. Если нужно дополнительно изменить получившийся сервис веб-запросов, создайте отдельное правило типа `FULL_WEB_REQUEST`.  По умолчанию `false`, совпадающие запросы обнаруживаются как полные веб-сервисы.",
    ),
    (
        "Detect the matching requests as web services (`false`) or web request services (`true`).  Setting this field to `true` prevents detecting of matching requests as opaque web services. An opaque web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate rule of the `OPAQUE_AND_EXTERNAL_WEB_REQUEST` type.  Default is `false`, detecting matching requests as opaque web services.",
        "Обнаруживать совпадающие запросы как веб-сервисы (`false`) или как сервисы веб-запросов (`true`).  Установка этого поля в `true` предотвращает обнаружение совпадающих запросов как непрозрачных веб-сервисов. Вместо этого создаётся непрозрачный сервис веб-запросов. Если нужно дополнительно изменить получившийся сервис веб-запросов, создайте отдельное правило типа `OPAQUE_AND_EXTERNAL_WEB_REQUEST`.  По умолчанию `false`, совпадающие запросы обнаруживаются как непрозрачные веб-сервисы.",
    ),
    (
        "Transformations to be applied to the detected value.",
        "Преобразования, применяемые к обнаруженному значению.",
    ),
    (
        "The value to be used instead of the detected value.",
        "Значение, используемое вместо обнаруженного значения.",
    ),
    (
        "The number of segments of the URL to be kept.  The URL is divided by slashes (`/`), the indexing starts with 1 at context root.  For example, if you specify `2` for the `www.dynatrace.com/support/help/dynatrace-api/` URL, the value of `support/help` is used.",
        "Количество сохраняемых сегментов URL.  URL делится слешами (`/`), индексация начинается с 1 в context root.  Например, если вы укажете `2` для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`.",
    ),
    (
        "The port is used (`false`) or isn't used (`true`) in the service ID calculation.",
        "Порт используется (`false`) или не используется (`true`) в расчёте ID сервиса.",
    ),
    (
        "Use (`true`) or don't use (`false`) the detected host name as base for transformation.  Not applicable if the override is specified.",
        "Использовать (`true`) или не использовать (`false`) обнаруженное имя хоста как основу для преобразования.  Не применяется, если задано переопределение.",
    ),
    # CompareOperation element cells
    (
        "The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive.",
        "Условие чувствительно к регистру (`false`) или нечувствительно (`true`).  Если не задано, используется `false`, делая условие чувствительным к регистру.",
    ),
    (
        "Inverts the operation of the condition. Set to `true` to turn **contains** into **does not contain**.  If not set, then `false` is used.",
        "Инвертирует операцию условия. Установите `true`, чтобы превратить **contains** в **does not contain**.  Если не задано, используется `false`.",
    ),
    (
        "Inverts the operation of the condition. Set to `true` to turn **equals** into **does not equal**.  If not set, then `false` is used.",
        "Инвертирует операцию условия. Установите `true`, чтобы превратить **equals** в **does not equal**.  Если не задано, используется `false`.",
    ),
    (
        "Inverts the operation of the condition. Set to `true` to turn **starts with** into **does not start with**.  If not set, then `false` is used.",
        "Инвертирует операцию условия. Установите `true`, чтобы превратить **starts with** в **does not start with**.  Если не задано, используется `false`.",
    ),
    (
        "Inverts the operation of the condition. Set to `true` to turn **ends with** into **does not end with**.  If not set, then `false` is used.",
        "Инвертирует операцию условия. Установите `true`, чтобы превратить **ends with** в **does not end with**.  Если не задано, используется `false`.",
    ),
    (
        "Inverts the operation of the condition. Set to `true` to turn **exists** into **does not exist**.  If not set, then `false` is used.",
        "Инвертирует операцию условия. Установите `true`, чтобы превратить **exists** в **does not exist**.  Если не задано, используется `false`.",
    ),
    (
        "Inverts the operation of the condition. Set to `true` to turn **IP is in range** into **IP is not in range**.  If not set, then `false` is used.",
        "Инвертирует операцию условия. Установите `true`, чтобы превратить **IP is in range** в **IP is not in range**.  Если не задано, используется `false`.",
    ),
    (
        "The value to compare to.  If several values are specified, the OR logic applies.",
        "Значение для сравнения.  Если указано несколько значений, применяется логика OR.",
    ),
    ("The value to compare to.", "Значение для сравнения."),
    ("The lower boundary of the IP range.", "Нижняя граница диапазона IP."),
    ("The upper boundary of the IP range.", "Верхняя граница диапазона IP."),
    # Transformation element cells
    (
        "The delimiter of the transformation. The transformation keeps everything before this delimiter and removes everything after it.  The delimiter itself is not kept.  If several delimiters appear in the initial value, only the first one is used.",
        "Разделитель преобразования. Преобразование сохраняет всё до этого разделителя и удаляет всё после него.  Сам разделитель не сохраняется.  Если в исходном значении несколько разделителей, используется только первый.",
    ),
    (
        "The delimiter of the transformation. The transformation removes everything before this delimiter and keeps everything after it.  The delimiter itself is not kept.  If several delimiters appear in the initial value, only the first one is used.",
        "Разделитель преобразования. Преобразование удаляет всё до этого разделителя и сохраняет всё после него.  Сам разделитель не сохраняется.  Если в исходном значении несколько разделителей, используется только первый.",
    ),
    (
        "The starting delimiter. The transformation removes everything before it. The delimiter itself is not kept.",
        "Начальный разделитель. Преобразование удаляет всё до него. Сам разделитель не сохраняется.",
    ),
    (
        "The ending delimiter. The transformation removes everything after it. The delimiter itself is not kept.",
        "Конечный разделитель. Преобразование удаляет всё после него. Сам разделитель не сохраняется.",
    ),
    (
        "The starting delimiter. The transformation replaces everything from here until ending delimiter. The delimiter itself remain intact.",
        "Начальный разделитель. Преобразование заменяет всё отсюда до конечного разделителя. Сам разделитель остаётся без изменений.",
    ),
    (
        "The ending delimiter. The transformation replaces everything from starting delimiter until here. The delimiter itself remain intact.",
        "Конечный разделитель. Преобразование заменяет всё от начального разделителя до этого места. Сам разделитель остаётся без изменений.",
    ),
    (
        "The value to be used instead of the content between delimiters.",
        "Значение, используемое вместо содержимого между разделителями.",
    ),
    (
        "Remove (`true`) or keep (`false`) hexadecimal numbers.  If not set, then `false` is used, keeping hexadecimal numbers.",
        "Удалять (`true`) или сохранять (`false`) шестнадцатеричные числа.  Если не задано, используется `false`, сохраняя шестнадцатеричные числа.",
    ),
    (
        "Remove numbers that contain at least *X* digits.",
        "Удалять числа, содержащие не менее *X* цифр.",
    ),
    (
        "The delimiter for splitting the detected value. The delimiter itself is not kept.",
        "Разделитель для разбиения обнаруженного значения. Сам разделитель не сохраняется.",
    ),
    (
        "The index of the element in the split array to be used. Indexing starts with `1`.",
        "Индекс используемого элемента в разбитом массиве. Индексация начинается с `1`.",
    ),
    ("The number of elements to be kept.", "Количество сохраняемых элементов."),
    (
        "Keeps the first (`false`) or last (`true`) elements.  If not set, then `false` is used, keeping the first elements.",
        "Сохраняет первые (`false`) или последние (`true`) элементы.  Если не задано, используется `false`, сохраняя первые элементы.",
    ),
    # CustomService / DetectionRule / MethodRule element cells
    ("Custom service enabled/disabled.", "Пользовательский сервис включён/отключён."),
    ("The ID of the custom service.", "ID пользовательского сервиса."),
    (
        "The name of the custom service, displayed in the UI.",
        "Имя пользовательского сервиса, отображаемое в UI.",
    ),
    (
        "The order string. Sorting custom services alphabetically by their order string determines their relative ordering.  Typically this is managed by Dynatrace internally and will not be present in GET responses.",
        "Строка порядка. Сортировка пользовательских сервисов в алфавитном порядке по их строке порядка определяет их относительный порядок.  Обычно этим управляет Dynatrace внутренне, и строка не присутствует в ответах GET.",
    ),
    (
        "The list of process groups the custom service should belong to.",
        "Список групп процессов, к которым должен принадлежать пользовательский сервис.",
    ),
    (
        "The queue entry point flag.  Set to `true` for custom messaging services.",
        "Флаг точки входа очереди.  Установите `true` для пользовательских сервисов обмена сообщениями.",
    ),
    ("The queue entry point type..", "Тип точки входа очереди.."),
    (
        "The list of rules defining the custom service.",
        "Список правил, определяющих пользовательский сервис.",
    ),
    (
        "Additional annotations filter of the rule.  Only classes where all listed annotations are available in the class itself or any of its superclasses are instrumented.  Not applicable to PHP.",
        "Дополнительный фильтр аннотаций правила.  Инструментируются только классы, в которых все перечисленные аннотации присутствуют в самом классе или в любом из его суперклассов.  Не применяется к PHP.",
    ),
    (
        "The fully qualified class or interface to instrument.  Required for Java and .NET custom services.  Not applicable to PHP.",
        "Полностью квалифицированный класс или интерфейс для инструментирования.  Обязательно для пользовательских сервисов Java и .NET.  Не применяется к PHP.",
    ),
    ("Rule enabled/disabled.", "Правило включено/отключено."),
    (
        "The PHP file containing the class or methods to instrument.  Required for PHP custom service.  Not applicable to Java and .NET.",
        "PHP-файл, содержащий класс или методы для инструментирования.  Обязательно для пользовательского сервиса PHP.  Не применяется к Java и .NET.",
    ),
    (
        "Matcher applying to the file name. Default value is `ENDS_WITH` (if applicable).",
        "Сопоставитель, применяемый к имени файла. Значение по умолчанию `ENDS_WITH` (если применимо).",
    ),
    ("The ID of the detection rule.", "ID правила обнаружения."),
    (
        "Matcher applying to the class name. `STARTS_WITH` can only be used if there is at least one annotation defined. Default value is `EQUALS`.",
        "Сопоставитель, применяемый к имени класса. `STARTS_WITH` можно использовать, только если определена хотя бы одна аннотация. Значение по умолчанию `EQUALS`.",
    ),
    (
        "List of methods to instrument.",
        "Список методов для инструментирования.",
    ),
    (
        "Fully qualified types of argument the method expects.",
        "Полностью квалифицированные типы аргументов, которые ожидает метод.",
    ),
    ("The ID of the method rule.", "ID правила метода."),
    ("The method to instrument.", "Метод для инструментирования."),
    ("The modifiers of the method rule.", "Модификаторы правила метода."),
    (
        "Fully qualified type the method returns.",
        "Полностью квалифицированный тип, возвращаемый методом.",
    ),
    ("The visibility of the method rule.", "Видимость правила метода."),
    # FailureDetectionParameterSet element cells
    (
        "A list of domains for the special handling of the 404 HTTP response code.  If the top domain of the *Referer* is presented in the list OR equals the top domain of the request's host, the 404 code is considered a failure.  Only applicable when **isHttp404NotFoundFailureEnabled** is set to `true`.",
        "Список доменов для особой обработки HTTP-кода ответа 404.  Если верхний домен *Referer* присутствует в списке ИЛИ равен верхнему домену хоста запроса, код 404 считается сбоем.  Применимо только когда **isHttp404NotFoundFailureEnabled** установлено в `true`.",
    ),
    (
        "The missing HTTP response code on the client side is a failure (`true`) or a success (`false`).  If not set, `false` is used.",
        "Отсутствующий HTTP-код ответа на стороне клиента считается сбоем (`true`) или успехом (`false`).  Если не задано, используется `false`.",
    ),
    ("A short description of the FDP set.", "Краткое описание набора FDP."),
    (
        "A list of faulty exceptions.  If an exception on *any* node of the service matches *any* of these patterns it is considered a failure.",
        "Список ошибочных исключений.  Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.",
    ),
    (
        "A list of client side HTTP response codes that are considered a failure.  The format is a list of ranges and individual values (for example, `500-599, 400-499, 1008`).  If not set, the range of `400-599` is used.",
        "Список HTTP-кодов ответа на стороне клиента, которые считаются сбоем.  Формат это список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).  Если не задано, используется диапазон `400-599`.",
    ),
    (
        "A list of server side HTTP response codes that are considered a failure.  The format is a list of ranges and individual values (for example, `500-599, 400-499, 1008`).If not set, the range of `500-599` is used.",
        "Список HTTP-кодов ответа на стороне сервера, которые считаются сбоем.  Формат это список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).Если не задано, используется диапазон `500-599`.",
    ),
    (
        "Special handling of the 404 HTTP response code is enabled (`true`) or disabled (`false`). See **brokenLinkDomains** for special handling details.  Only applicable when 404 is NOT in the list of failing HTTP response codes and only for the server side.  If not set, `false` is used.",
        "Особая обработка HTTP-кода ответа 404 включена (`true`) или отключена (`false`). Подробности особой обработки см. в **brokenLinkDomains**.  Применимо только когда 404 НЕ входит в список HTTP-кодов ответа, считающихся сбоем, и только для стороны сервера.  Если не задано, используется `false`.",
    ),
    ("The ID of the parameter set.", "ID набора параметров."),
    (
        "If set to true all exceptions will be ignored. Which means defined exception patterns will not have any effect.",
        "Если установлено в true, все исключения будут игнорироваться. Это означает, что заданные шаблоны исключений не будут иметь никакого эффекта.",
    ),
    (
        "If set to true span failure detection will be ignored.",
        "Если установлено в true, обнаружение сбоев по span будет игнорироваться.",
    ),
    (
        "A list of ignored exceptions.  If an exception on the entry node of the service matches *any* of these patterns it is ignored by failure detection.",
        "Список игнорируемых исключений.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно игнорируется обнаружением сбоев.",
    ),
    (
        "The display name of the FDP set.  The length of the name is limited to 150 characters.",
        "Отображаемое имя набора FDP.  Длина имени ограничена 150 символами.",
    ),
    (
        "The missing HTTP response code on the server side is a failure (`true`) or a success (`false`).  If not set, `false` is used.",
        "Отсутствующий HTTP-код ответа на стороне сервера считается сбоем (`true`) или успехом (`false`).  Если не задано, используется `false`.",
    ),
    (
        "A list of success exceptions.  If an exception on the entry node of the service matches *any* of these patterns it is considered a success.",
        "Список исключений успеха.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно считается успехом.",
    ),
    (
        "A list of tag-based conditions.  If *any* condition is fulfilled the request is considered a failure.",
        "Список условий на основе тегов.  Если выполнено *любое* условие, запрос считается сбоем.",
    ),
    (
        "The predicate that tests the value of the tag.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON modelsï»¿](https://dt-url.net/9sg3swf).",
        "Предикат, проверяющий значение тега.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON modelsï»¿](https://dt-url.net/9sg3swf).",
    ),
    ("The key of the tag to be checked.", "Ключ проверяемого тега."),
    # FailureDetectionRule / FailureDetectionCondition element cells
    (
        "A list of conditions of the rule.  The rule applies when **all** conditions are fulfilled.",
        "Список условий правила.  Правило применяется, когда выполнены **все** условия.",
    ),
    (
        "The failure detection parameter (FDP) set of the rule.  Specify the ID of the set here. The FDP set must exist at the time of rule creation.",
        "Набор параметров обнаружения сбоев (FDP) правила.  Укажите здесь ID набора. Набор FDP должен существовать на момент создания правила.",
    ),
    ("The ID of the rule.", "ID правила."),
    (
        "The display name of the rule.  The length of the name is limited to 150 characters.",
        "Отображаемое имя правила.  Длина имени ограничена 150 символами.",
    ),
    (
        "The predicate that tests the value of the attribute.  The actual set of fields depends on the type of the predicate. Find the list of actual objects in the description of the **type** field or see [Failure detection API - JSON modelsï»¿](https://dt-url.net/9sg3swf).",
        "Предикат, проверяющий значение атрибута.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON modelsï»¿](https://dt-url.net/9sg3swf).",
    ),
    # Fdc/FdpTag predicate element cells (reference value variants)
    (
        "The reference value. The condition is fulfilled when the tag (which is a string) starts with this value.",
        "Эталонное значение. Условие выполняется, когда тег (являющийся строкой) начинается с этого значения.",
    ),
    (
        "The reference value. The condition is fulfilled when the tag (which is a string) equals this value.",
        "Эталонное значение. Условие выполняется, когда тег (являющийся строкой) равен этому значению.",
    ),
    (
        "The reference value. The condition is fulfilled when the tag (which is a string) ends with this value.",
        "Эталонное значение. Условие выполняется, когда тег (являющийся строкой) заканчивается этим значением.",
    ),
    (
        "The reference value. The condition is fulfilled when the tag (which is a string) contains this value.",
        "Эталонное значение. Условие выполняется, когда тег (являющийся строкой) содержит это значение.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is an integer) is less than this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) меньше этого значения.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is an integer) is less than or equals this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) меньше этого значения или равен ему.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is an integer) is greater than this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) больше этого значения.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is an integer) is greater than or equals this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) больше этого значения или равен ему.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is a long) is less than this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся long) меньше этого значения.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is a long) is less than or equals this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся long) меньше этого значения или равен ему.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is a long) is greater than this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся long) больше этого значения.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is a long) is greater than or equals this value.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся long) больше этого значения или равен ему.",
    ),
    ("The reference value.", "Эталонное значение."),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) equals *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся строкой) равен *любому* из них.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) start with *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся строкой) начинается с *любого* из них.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) ends with *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся строкой) заканчивается *любым* из них.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a string) contains *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся строкой) содержит *любое* из них.",
    ),
    (
        "The reference value. The condition is fulfilled when the attribute (which is an integer) equals *any* of these.",
        "Эталонное значение. Условие выполняется, когда атрибут (являющийся целым числом) равен *любому* из них.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a long) equals *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся long) равен *любому* из них.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is the key of a tag) equals *any* of these.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся ключом тега) равен *любому* из них.",
    ),
    (
        "A list of reference tag keys.  The condition is fulfilled when the tag matches *any* key:value pair, consisting of a key and a value that are at the **same position** in the respective list.",
        "Список эталонных ключей тегов.  Условие выполняется, когда тег соответствует *любой* паре ключ:значение, состоящей из ключа и значения, находящихся на **одной и той же позиции** в соответствующих списках.",
    ),
    (
        "A list of reference tag values.  The condition is fulfilled when the tag matches *any* key:value pair, consisting of a key and a value that are at the **same position** in the respective list.",
        "Список эталонных значений тегов.  Условие выполняется, когда тег соответствует *любой* паре ключ:значение, состоящей из ключа и значения, находящихся на **одной и той же позиции** в соответствующих списках.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is the type of the service) equals *any* of these.The possible values are: WebRequest, WebService, Database, Method, WebSite, Messaging, Mobile, Process, Rmi, External, QueueListener, QueueInteraction, RemoteCall, SaasVendor, CustomApplication, Cics, Ims, CicsInteraction, ImsInteraction, EnterpriseServiceBus, ZosConnect.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся типом сервиса) равен *любому* из них.Возможные значения: WebRequest, WebService, Database, Method, WebSite, Messaging, Mobile, Process, Rmi, External, QueueListener, QueueInteraction, RemoteCall, SaasVendor, CustomApplication, Cics, Ims, CicsInteraction, ImsInteraction, EnterpriseServiceBus, ZosConnect.",
    ),
    (
        "A list of reference values. The condition is fulfilled when the attribute (which is a set of management zones) contains **all** the reference values.  Specify the ID or the name of the management zone here.",
        "Список эталонных значений. Условие выполняется, когда атрибут (являющийся набором зон управления) содержит **все** эталонные значения.  Укажите здесь ID или имя зоны управления.",
    ),
    (
        "A list of the rule IDs. The rules in the ruleset are arranged such that their IDs form the same sequence as this list. The ID of each rule in the ruleset must occur exactly once in the list.",
        "Список ID правил. Правила в наборе располагаются так, чтобы их ID образовывали ту же последовательность, что и этот список. ID каждого правила в наборе должен встречаться в списке ровно один раз.",
    ),
    # ----- (Z) global LAST: element-can-hold -> Возможные значения: (L99) ----------
    ("The element can hold these values", "Возможные значения:"),
]

R = R_L4AA + R_L4AB


def _normalize(t):
    """Pure-ASCII source: build fragile mojibake/BOM keys from codepoints so
    the literals never get mangled (L4X#1). EN CRLF -> LF (RU corpus conv)."""
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
