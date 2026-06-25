# -*- coding: utf-8 -*-
"""L4X builder: configuration-api/calculated-metrics/service-metrics/ = 7 files
(parent + del/get-all/get-calculated-metric/json-models/post/put). Closes
calculated-metrics/ subsection 100% (L4O deferred service-metrics as L42 due to
json-models 932 + post/put 767/798).

Splice method (L98/L100, L4O _build_calcmetrics): start from EN, CRLF->LF,
mojibake-normalize (L4W: â\x80\x99-family double-encoded -> ASCII), strip BOM
(L4M), apply ordered exact-string canon -> byte-identical JSON + line parity.
Anything unreplaced stays EN-verbatim (object/enum/JSON, L99).

ACTIVE API (no deprecated banner, * Reference/* Published EN-verbatim, L89/L90,
rum-metrics RU twin confirms). title/H1 EN-verbatim (L4O). anchor = SAME-
subsection L4O calculated-metrics RU (service strings already shipped in top
parent: "вычисляемая метрика сервиса"/"метрик сервиса") + k8s/config shared
objects (L4M/L4U). json-models STRUCTURE (Variations intro / Refer-to-JSON /
"Список фактических объектов см.") = conditional-naming L3G pattern (only
json-models precedent; L4O had none) BUT headers + "Возможные значения:" +
EN-locks = L4O/L99 (newer, same-subsection; NOT L3G "Элемент может принимать").
Related-topics link-text = target RU H1 verbatim ("Вычисляемые метрики для
сервисов"/"Многомерный анализ", L4O/L4L). Example canon = reports-api L4I/
alerting-profiles L4J ("## Пример"/"#### URL запроса"/.../"#### Curl" EN,
"API-токен передаётся в заголовке **Authorization**."). L101: 400 "Сбой.
Невалидный ввод" period BY SOURCE (here EN "Failed. The input is invalid" w/o
period -> w/o period). bare "| Success |"->"| Успех |" (L4V/L4W canon).
"calculated service metric"->"вычисляемая метрика сервиса" rendered ONLY inside
full sentences/cells (L4T longest-first, NO bare generic rule -> no hybrid)."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
SM = "calculated-metrics/service-metrics"

FILES = [
    f"{SM}.md",
    f"{SM}/del-calculated-metric.md",
    f"{SM}/get-all.md",
    f"{SM}/get-calculated-metric.md",
    f"{SM}/json-models.md",
    f"{SM}/post-calculated-metric.md",
    f"{SM}/put-calculated-metric.md",
]

# mojibake: file is UTF-8 of double-encoded text. After utf-8 decode the unit is
# "â" + two C1-range chars. Normalize BEFORE replacements (L4W lesson 1).
MOJI = [
    ("â", "'"),  # ’ right single quote / apostrophe
    ("â", "'"),  # ‘ left single quote
    ("â", '"'),  # “ left double quote
    ("â", '"'),  # ” right double quote
    ("â", "-"),  # – en dash
    ("â", "-"),  # — em dash (CLAUDE#0; sentence translated anyway)
]

R = [
    # ---------- (A) Related-topics title-attrs ----------
    (
        "Learn how to create a calculated metric based on web requests.",
        "Узнайте, как создать вычисляемую метрику на основе веб-запросов.",
    ),
    (
        "Configure a multidimensional analysis view and save it as a calculated metric.",
        "Настройте представление многомерного анализа и сохраните его как вычисляемую метрику.",
    ),
    # ---------- (B) Related-topics link-text (= target RU H1; L4O/L4L) ----------
    ("[Calculated metrics for services]", "[Вычисляемые метрики для сервисов]"),
    ("[Multidimensional analysis]", "[Многомерный анализ]"),
    # ---------- (C) parent card title-attrs (reuse L4O exact) ----------
    (
        "View all calculated service metrics of your environment via the Dynatrace API.",
        "Просмотр всех вычисляемых метрик сервиса вашего окружения мониторинга через Dynatrace API.",
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
    # ---------- (D) parent card descriptions + group headings ----------
    (
        "Get an overview of all calculated service metrics.",
        "Обзор всех вычисляемых метрик сервиса.",
    ),
    (
        "Get the descriptor of a calculated service metric by its ID.",
        "Получить дескриптор вычисляемой метрики сервиса по её ID.",
    ),
    (
        "Create a new calculated service metric with the exact parameters you need.",
        "Создать новую вычисляемую метрику сервиса с нужными вам параметрами.",
    ),
    (
        "Update an existing service metric. You can also create a new calculated service metric with the specified ID.",
        "Обновить существующую метрику сервиса. Также можно создать новую вычисляемую метрику сервиса с указанным ID.",
    ),
    (
        "Delete calculated service metrics you don't need anymore.",
        "Удалить вычисляемые метрики сервиса, которые вам больше не нужны.",
    ),
    ("### List all metrics", "### Список всех метрик"),
    ("### View a metric", "### Просмотр метрики"),
    ("### Create a metric", "### Создание метрики"),
    ("### Edit a metric", "### Редактирование метрики"),
    ("### Delete a metric", "### Удаление метрики"),
    # ---------- (E) endpoint intro one-liners ----------
    (
        "Deletes the specified calculated service metric. Deletion cannot be undone!",
        "Удаляет указанную вычисляемую метрику сервиса. Удаление невозможно отменить!",
    ),
    (
        "Lists all calculated service metrics.",
        "Выводит список всех вычисляемых метрик сервиса.",
    ),
    (
        "Gets the descriptor of the specified calculated service metric.",
        "Возвращает дескриптор указанной вычисляемой метрики сервиса.",
    ),
    (
        "Creates a new calculated service metric.",
        "Создаёт новую вычисляемую метрику сервиса.",
    ),
    (
        "Updates the specified calculated service metric.",
        "Обновляет указанную вычисляемую метрику сервиса.",
    ),
    (
        "If the calculated service metric with the specified key doesn't exist, a new metric is created.",
        "Если вычисляемой метрики сервиса с указанным ключом не существует, создаётся новая метрика.",
    ),
    # ---------- (F) json-models structure (conditional-naming L3G pattern) ----------
    (
        "Some JSON models of the **Calculated service metrics** API vary according to the **type** of some objects. Here you can find JSON models for each variation.",
        "Некоторые JSON-модели API **Calculated service metrics** различаются в зависимости от поля **type** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.",
    ),
    (
        "## Variations of the `ComparisonInfo` object",
        "## Вариации объекта `ComparisonInfo`",
    ),
    # ComparisonInfo recurring (Condition.comparisonInfo cell + ComparisonInfo obj-desc;
    # BOM in [...JSON modelsï»¿] stripped first -> link-text "Service metrics API - JSON models" EN)
    (
        "Type-specific comparison for attributes. The actual set of fields depends on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [Service metrics API - JSON models](https://dt-url.net/9803svb).",
        "Сравнение для атрибутов, зависящее от типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [Service metrics API - JSON models](https://dt-url.net/9803svb).",
    ),
    (
        'Refer to [JSON models](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/json-models "Variations of models in the calculated service metrics API") to find all JSON models that depend on the **type** of the model.',
        'Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/json-models "Вариации моделей в API вычисляемых метрик сервиса").',
    ),
    (
        "Defines the actual set of fields depending on the value. See one of the following objects:",
        "Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:",
    ),
    # ---------- (G) standard L99 phrases ----------
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
    # ---------- (H) headings (newline-anchored; ## Validate payload / #### Curl EN) ----------
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
    ("\n## Example\n", "\n## Пример\n"),
    ("\n#### Request URL\n", "\n#### URL запроса\n"),
    ("\n#### Request body\n", "\n#### Тело запроса\n"),
    ("\n#### Response body\n", "\n#### Тело ответа\n"),
    ("\n#### Response code\n", "\n#### Код ответа\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # ---------- (I) object headings -> #### Объект `X` (EN-lock object names) ----------
    (
        "#### The `CalculatedServiceMetric` object",
        "#### Объект `CalculatedServiceMetric`",
    ),
    ("#### The `Condition` object", "#### Объект `Condition`"),
    ("#### The `ComparisonInfo` object", "#### Объект `ComparisonInfo`"),
    (
        "#### The `DimensionDefinition` object",
        "#### Объект `DimensionDefinition`",
    ),
    ("#### The `Placeholder` object", "#### Объект `Placeholder`"),
    (
        "#### The `PropagationSource` object",
        "#### Объект `PropagationSource`",
    ),
    ("#### The `UniversalTag` object", "#### Объект `UniversalTag`"),
    ("#### The `TagInfo` object", "#### Объект `TagInfo`"),
    (
        "#### The `ConfigurationMetadata` object",
        "#### Объект `ConfigurationMetadata`",
    ),
    (
        "#### The `CalculatedMetricDefinition` object",
        "#### Объект `CalculatedMetricDefinition`",
    ),
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
    ("#### The `TagComparisonInfo` object", "#### Объект `TagComparisonInfo`"),
    ("#### The `ZosComparisonInfo` object", "#### Объект `ZosComparisonInfo`"),
    ("#### The `ZosCallTypeDto` object", "#### Объект `ZosCallTypeDto`"),
    # ---------- (J) object/section descriptions (shared get/post/put/json-models) ----------
    (
        "Parameters of a definition of a calculated service metric.",
        "Параметры определения вычисляемой метрики сервиса.",
    ),
    (
        "Descriptor of a calculated service metric.",
        "Дескриптор вычисляемой метрики сервиса.",
    ),
    (
        "The definition of a calculated service metric.",
        "Определение вычисляемой метрики сервиса.",
    ),
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
        "An ordered list of short representations of Dynatrace entities.",
        "Упорядоченный список кратких представлений сущностей Dynatrace.",
    ),
    (
        "The short representation of a Dynatrace entity.",
        "Краткое представление сущности Dynatrace.",
    ),
    ("Tag of a Dynatrace entity.", "Тег сущности Dynatrace."),
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
    # ---------- (K) shared k8s/config canon (EntityShortRep / Error / ConstraintViolation / CfgMeta) ----------
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
    # ---------- (L) table headers (longest first) ----------
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
    # ---------- (M) response-code cells (L101: EN "Failed. The input is invalid" w/o period) ----------
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    (" | Success |", " | Успех |"),
    (
        "Success. The calculated service metric has been created. Response contains the key of the new metric.",
        "Успех. Вычисляемая метрика сервиса создана. Тело ответа содержит ключ новой метрики.",
    ),
    (
        "Success. The new calculated service metric has been created. Response contains the key of the new metric.",
        "Успех. Новая вычисляемая метрика сервиса создана. Тело ответа содержит ключ новой метрики.",
    ),
    (
        "Success. The calculated service metric has been updated. Response doesn't have a body.",
        "Успех. Вычисляемая метрика сервиса обновлена. Ответ без тела.",
    ),
    (
        "Success. The calculated service metric has been deleted. Response doesn't have a body.",
        "Успех. Вычисляемая метрика сервиса удалена. Ответ без тела.",
    ),
    (
        "Validated. The submitted configuration is valid. Response doesn't have a body.",
        "Validated. Переданная конфигурация валидна. Ответ без тела.",
    ),
    # ---------- (N) parameter (path/body) cell descriptions ----------
    (
        "The key of the calculated service metric to be updated.  The key of the calculated service metric in the body of the request must match this key.",
        "Ключ вычисляемой метрики сервиса, которую нужно обновить.  Ключ вычисляемой метрики сервиса в теле запроса должен совпадать с этим ключом.",
    ),
    (
        "The key of the calculated service metric to be deleted.",
        "Ключ вычисляемой метрики сервиса, которую нужно удалить.",
    ),
    (
        "The key of the required calculated service metric.",
        "Ключ требуемой вычисляемой метрики сервиса.",
    ),
    (
        "The JSON body of the request. Contains parameters of the new calculated service metric.",
        "JSON-тело запроса. Содержит параметры новой вычисляемой метрики сервиса.",
    ),
    (
        "The JSON body of the request. Contains updated parameters of the calculated service metric.",
        "JSON-тело запроса. Содержит обновлённые параметры вычисляемой метрики сервиса.",
    ),
    # ---------- (O) CalculatedServiceMetric element cell descriptions (shared) ----------
    (
        "The set of conditions for the metric usage.  **All** the specified conditions must be fulfilled to use the metric.",
        "Набор условий использования метрики.  Для использования метрики должны выполняться **все** указанные условия.",
    ),
    (
        "The metric is enabled (`true`) or disabled (`false`).",
        "Метрика включена (`true`) или отключена (`false`).",
    ),
    (
        "Restricts the metric usage to the specified service.  This field is mutually exclusive with the **managementZones** field.",
        "Ограничивает использование метрики указанным сервисом.  Это поле взаимоисключающее с полем **managementZones**.",
    ),
    (
        "Metric should (`true`) or not (`false`) ignore muted requests.",
        "Метрика должна (`true`) или не должна (`false`) игнорировать отключённые запросы.",
    ),
    (
        "Restricts the metric usage to specified management zones.  This field is mutually exclusive with the **entityId** field.",
        "Ограничивает использование метрики указанными зонами управления.  Это поле взаимоисключающее с полем **entityId**.",
    ),
    ("The displayed name of the metric.", "Отображаемое имя метрики."),
    (
        "The key of the calculated service metric.",
        "Ключ вычисляемой метрики сервиса.",
    ),
    ("The unit of the metric.", "Единица измерения метрики."),
    (
        "The display name of the metric's unit.  Only applicable when the **unit** parameter is set to `UNSPECIFIED`.",
        "Отображаемое имя единицы измерения метрики.  Применимо только когда параметр **unit** установлен в `UNSPECIFIED`.",
    ),
    # Condition object
    (
        "The attribute to be matched.  Note that for a service property attribute you must use the comparison of the `FAST_STRING` type.",
        "Сопоставляемый атрибут.  Учтите, что для атрибута свойства сервиса нужно использовать сравнение типа `FAST_STRING`.",
    ),
    # ComparisonInfo object
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
    # DimensionDefinition object
    (
        "The dimension value pattern.  You can define custom placeholders in the **placeholders** field and use them here.",
        "Шаблон значения измерения.  Можно определить пользовательские плейсхолдеры в поле **placeholders** и использовать их здесь.",
    ),
    ("The name of the dimension.", "Имя измерения."),
    (
        "The list of custom placeholders to be used in a dimension value pattern.",
        "Список пользовательских плейсхолдеров для использования в шаблоне значения измерения.",
    ),
    (
        "The number of top values to be calculated.",
        "Количество верхних значений для расчёта.",
    ),
    ("The aggregation of the dimension.", "Агрегация измерения."),
    ("How to calculate the **topX** values.", "Как рассчитывать значения **topX**."),
    # Placeholder object
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
    # PropagationSource object
    (
        "Use only request attributes from services that belong to this management zone.. Use either this or `serviceTag`",
        "Использовать только атрибуты запросов из сервисов, принадлежащих этой зоне управления.. Используйте либо это, либо `serviceTag`",
    ),
    # UniversalTag object (mojibake already normalized: Itâs->It's, â:â->\":\", â->-)
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
    # TagInfo object
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
    # CalculatedMetricDefinition object
    ("The metric to be captured.", "Захватываемая метрика."),
    (
        "The request attribute to be captured.  Only applicable when the **metric** parameter is set to `REQUEST_ATTRIBUTE`.",
        "Захватываемый атрибут запроса.  Применимо только когда параметр **metric** установлен в `REQUEST_ATTRIBUTE`.",
    ),
    # NumberRequestAttribute / StringRequestAttribute shared fields
    (
        "If `true`, the request attribute is matched on child service calls.  Default is `false`.",
        "Если `true`, атрибут запроса сопоставляется на дочерних вызовах сервиса.  По умолчанию `false`.",
    ),
    (
        "The comparison is case-sensitive (`true`) or not case-sensitive (`false`).",
        "Сравнение чувствительно к регистру (`true`) или нечувствительно (`false`).",
    ),
    # StubList values cell
    (
        "An ordered list of short representations of Dynatrace entities. |",
        "Упорядоченный список кратких представлений сущностей Dynatrace. |",
    ),
    # ---------- (R) Example-section recurring canon (reports-api L4I) ----------
    (
        "The API token is passed in the **Authorization** header.",
        "API-токен передаётся в заголовке **Authorization**.",
    ),
    (
        "The result is truncated to two entries.",
        "Результат усечён до двух записей.",
    ),
    (
        "The response code of **204** indicates that the update was successful.",
        "Код ответа **204** означает, что обновление прошло успешно.",
    ),
    (
        'In this example, the request deletes the **Requests by code** calculated service metric created in the [POST request example](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric#example "Создание вычисляемой метрики сервиса через Dynatrace API.").',
        'В этом примере запрос удаляет вычисляемую метрику сервиса **Requests by code**, созданную в примере [POST request example](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric#example "Создание вычисляемой метрики сервиса через Dynatrace API.").',
    ),
    (
        "In this example, the request lists all calculated service metrics in the **mySampleEnv** environment.",
        "В этом примере запрос выводит список всех вычисляемых метрик сервиса в окружении **mySampleEnv**.",
    ),
    (
        "In this example, the request inquires about the descriptor of the **Top database calls per URL** metric, which has the metric key of **calc:service.topdbcallsperurl**. The metric tracks the number of HTTP calls to databases, where the method is POST. The values of the metric are split by the request name.",
        "В этом примере запрос запрашивает дескриптор метрики **Top database calls per URL**, у которой ключ метрики **calc:service.topdbcallsperurl**. Метрика отслеживает количество HTTP-вызовов к базам данных, где метод POST. Значения метрики разбиваются по имени запроса.",
    ),
    (
        "In this example, the request creates a calculated service metric that tracks the number of requests in services tagged with the **payment** tag. It splits the values by HTTP status class.",
        "В этом примере запрос создаёт вычисляемую метрику сервиса, которая отслеживает количество запросов в сервисах с тегом **payment**. Она разбивает значения по классу HTTP-статуса.",
    ),
    (
        "The metric key is **calc:service.requestsbycode** and the display name is **Requests by code**.",
        "Ключ метрики **calc:service.requestsbycode**, отображаемое имя **Requests by code**.",
    ),
    (
        "Because the request body is lengthy, it is truncated in this example **Curl** section. See the full body in the **Request body** section. You can download or copy the example request body to try it out on your own. Before using it, make sure that you're using a tag that is available in your environment.",
        "Поскольку тело запроса длинное, в этом примере оно усечено в секции **Curl**. Полное тело смотрите в секции **Request body**. Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно. Перед использованием убедитесь, что вы используете тег, доступный в вашем окружении.",
    ),
    (
        "The response contains the key and the name of the newly created metric.",
        "Ответ содержит ключ и имя только что созданной метрики.",
    ),
    (
        'In this example, the request modifies the **Requests by code** calculated service metric created in the [POST request example](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric#example "Создание вычисляемой метрики сервиса через Dynatrace API."). The request restricts the metric to the **Easytravel** management zone and adds the condition of process group having the **cardVerification** tag.',
        'В этом примере запрос изменяет вычисляемую метрику сервиса **Requests by code**, созданную в примере [POST request example](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric#example "Создание вычисляемой метрики сервиса через Dynatrace API."). Запрос ограничивает метрику зоной управления **Easytravel** и добавляет условие наличия у группы процессов тега **cardVerification**.',
    ),
    (
        "Because the request body is lengthy, it is truncated in this example **Curl** section. See the full body in the **Request body** section. You can download or copy the example request body to try it out on your own. Before using it, make sure that you're using management zone and tags that are available in your environment.",
        "Поскольку тело запроса длинное, в этом примере оно усечено в секции **Curl**. Полное тело смотрите в секции **Request body**. Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно. Перед использованием убедитесь, что вы используете зону управления и теги, доступные в вашем окружении.",
    ),
    # ---------- (Z) global LAST: element-can-hold -> Возможные значения: (L99) ----------
    ("The element can hold these values", "Возможные значения:"),
]


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    with io.open(src, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    t = t.replace("\r\n", "\n")  # EN is CRLF; RU corpus convention is LF
    # L4W: normalize double-encoded mojibake BEFORE replacements. Unit = U+00E2
    # + 2 C1 chars; keys built from codepoints to avoid literal-byte mismatch.
    # Data actually uses only U+2018/U+2019/U+2013 (verified); rest harmless.
    e2 = "â"
    for cp, repl in (
        ("", "'"),  # U+2019 right single quote / apostrophe
        ("", "'"),  # U+2018 left single quote
        ("", '"'),  # U+201C left double quote
        ("", '"'),  # U+201D right double quote
        ("", "-"),  # U+2013 en dash
        ("", "-"),  # U+2014 em dash (CLAUDE#0; sentence translated)
    ):
        t = t.replace(e2 + cp, repl)
    t = t.replace("﻿", "").replace("ï»¿", "")  # BOM (L4M)
    for en, ru in R:
        t = t.replace(en, ru)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return dst


def _normalize(t):
    """Pure-ASCII source: build fragile mojibake/BOM keys from codepoints so the
    literals never get mangled. Overrides the build() above (last def wins)."""
    t = t.replace("\r\n", "\n")  # EN CRLF -> LF (RU corpus convention)
    e2 = chr(0xE2)  # U+00E2; mojibake unit = e2 + 2 C1 chars (L4W)
    for c1, c2, repl in (
        (0x80, 0x99, "'"),  # U+2019 right single quote / apostrophe
        (0x80, 0x98, "'"),  # U+2018 left single quote
        (0x80, 0x9C, '"'),  # U+201C left double quote (harmless if absent)
        (0x80, 0x9D, '"'),  # U+201D right double quote (harmless if absent)
        (0x80, 0x93, "-"),  # U+2013 en dash
        (0x80, 0x94, "-"),  # U+2014 em dash (CLAUDE#0; sentence translated)
    ):
        t = t.replace(e2 + chr(c1) + chr(c2), repl)
    t = t.replace(chr(0xFEFF), "")  # real BOM
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")  # 3-char BOM (L4M)
    return t


def build(rel):  # noqa: F811 - intentional override of fragile literal version
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
