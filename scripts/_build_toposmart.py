# -*- coding: utf-8 -*-
"""L4Z builder: environment-api/topology-and-smartscape/ = 21 files (DEPRECATED
subsection): applications-api (get-all/get-an-app/get-baseline/post-tags),
custom-device-api (create/report), hosts-api parent + del-tags/get-a-host/
get-all/post-tags, process-groups-api parent + get-all/get-a-process-group/
post-tags, processes-api (get-all/get-a-process), services-api (get-all/
get-a-service/get-baseline/post-tags).

Splice method (L98/L100/L4O/L4X/L4Y): start from EN, CRLF->LF, normalize
double-encoded mojibake + strip BOM (L4M), apply per-file then COMMON ordered
exact-string canon (longest/most-specific FIRST, L4T) -> byte-identical JSON/
code-fence + automatic line parity. Anything unreplaced stays EN-verbatim
(object/enum/JSON/scope, L99).

DEPRECATED subsection -> anchor = parent RU
docs/managed-ru/dynatrace-api/environment-api/topology-and-smartscape.md
(verified): both H1 EN-verbatim, `* Reference`/`* Updated on Mar 22, 2023`/
`* Deprecated` EN-verbatim; deprecated-banner prose -> exact RU from parent.
Plus L4Y env-api L99: "The element can hold these values" ->
"Возможные значения:" WITH colon; cell path/query/Required/Optional/types EN;
"#### Curl" EN ALLOWED_EN; shared Error/ErrorEnvelope/ConstraintViolation
verbatim from get-countries.md RU; "[Tokens and authentication]"/API-name
link-text EN (corpus 188:40, L87/L4S/L4Y).

Twin-splice (L4W): get-all<->get-a-X share byte-identical object element-desc
STRINGS (Application/Host/Service/ProcessGroup/ProcessGroupInstance/AgentVersion
/MonitoringState/TechnologyInfo/TagInfo/HostGroup/EntityShortRepresentation/
ProcessGroupInstanceModule + Error/ErrorEnvelope/ConstraintViolation) -> in
COMMON, translated ONCE -> applies to both twins regardless of line offset.
4 post-tags near-identical UpdateEntity -> COMMON. 2 custom-device share
CustomDevicePushMessage/EntityTimeseriesData/CustomDevicePushResult -> COMMON.

mojibake (verified by codepoint scan): 3-byte BOM `ï»¿` inside table-cell
link-text (hosts get-all/get-a-host `Dynatrace classic licensingï»¿`;
custom-device `Timeseries API v1 - PUT a custom metricï»¿`) -> stripped by
_normalize. U+00E2 lone (e2 only, NO C1 pair) in report-custom-device prose
`retrospectivelyâthe` = broken em-dash -> sentence translated wholesale
(CLAUDE#0 no em-dash). No mojibake inside ``` JSON fences ``` (byte-verbatim)."""

import os, io

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
EN = os.path.join(
    ROOT, r"docs\managed\dynatrace-api\environment-api\topology-and-smartscape"
)
RU = os.path.join(
    ROOT, r"docs\managed-ru\dynatrace-api\environment-api\topology-and-smartscape"
)

FILES = [
    "applications-api/get-all.md",
    "applications-api/get-an-app.md",
    "applications-api/get-baseline.md",
    "applications-api/post-tags.md",
    "custom-device-api/create-custom-device-via-dynatrace-api.md",
    "custom-device-api/report-custom-device-metric-via-rest-api.md",
    "hosts-api.md",
    "hosts-api/del-tags.md",
    "hosts-api/get-a-host.md",
    "hosts-api/get-all.md",
    "hosts-api/post-tags.md",
    "process-groups-api.md",
    "process-groups-api/get-all.md",
    "process-groups-api/get-a-process-group.md",
    "process-groups-api/post-tags.md",
    "processes-api/get-all.md",
    "processes-api/get-a-process.md",
    "services-api/get-all.md",
    "services-api/get-a-service.md",
    "services-api/get-baseline.md",
    "services-api/post-tags.md",
]


def _normalize(t):
    """Pure-ASCII source code: build fragile mojibake/BOM keys from codepoints
    so the literals never collapse on Write/Edit (L4X lesson 1)."""
    t = t.replace("\r\n", "\n")  # EN is CRLF; RU corpus convention is LF
    e2 = chr(0xE2)  # U+00E2; double-encoded unit = e2 + 2 C1 chars (L4W)
    for c1, c2, repl in (
        (0x80, 0x99, "'"),  # U+2019 right single quote / apostrophe
        (0x80, 0x98, "'"),  # U+2018 left single quote
        (0x80, 0x9C, '"'),  # U+201C left double quote
        (0x80, 0x9D, '"'),  # U+201D right double quote
        (0x80, 0x93, "-"),  # U+2013 en dash
        (0x80, 0x94, "-"),  # U+2014 em dash (double-encoded, if any)
    ):
        t = t.replace(e2 + chr(c1) + chr(c2), repl)
    t = t.replace(chr(0xFEFF), "")  # real BOM
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")  # 3-byte BOM (L4M)
    # lone U+00E2 broken em-dash in report-custom-device prose
    # ("retrospectivelyâthe") -> sentence is translated wholesale below, but
    # normalize the stray byte so it never leaks into RU.
    t = t.replace(e2, "-")
    return t


# ---------------------------------------------------------------- COMMON
# Applied AFTER per-file. Each entry is within-line (or newline-anchored
# heading) => line-parity preserved. Ordered longest/most-specific FIRST to
# avoid substring collisions (L4T: generic before specific = EN/RU hybrid).
COMMON = [
    # --- DEPRECATED banner prose (verbatim from parent RU; link-text
    #     `Monitored entities API` EN, title-attr translated, URL verbatim) ---
    (
        'This API is deprecated. Use the [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") instead.',
        'Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.',
    ),
    # --- structural headings (newline-anchored) ---
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n## Response headers\n", "\n## Заголовки ответа\n"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n## Example\n", "\n## Пример\n"),
    ("\n#### Request URL\n", "\n#### URL запроса\n"),
    ("\n#### Response body\n", "\n#### Тело ответа\n"),
    ("\n#### Request body\n", "\n#### Тело запроса\n"),
    ("\n#### Response code\n", "\n#### Код ответа\n"),
    ("\n#### Result\n", "\n#### Результат\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # `#### Curl` => EN-verbatim (L99 ALLOWED_EN)
    # --- table headers (longest/most-specific FIRST) ---
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    (
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Header | Type | Description |", "| Заголовок | Тип | Описание |"),
    # --- object headings -> #### Объект `X` (EN-lock backtick names; longer
    #     names first, defensively) ---
    (
        "#### The `CustomDevicePushMessage` object",
        "#### Объект `CustomDevicePushMessage`",
    ),
    (
        "#### The `CustomDevicePushResult` object",
        "#### Объект `CustomDevicePushResult`",
    ),
    (
        "#### The `ApplicationBaselineValues` object",
        "#### Объект `ApplicationBaselineValues`",
    ),
    (
        "#### The `ServiceBaselineValues` object",
        "#### Объект `ServiceBaselineValues`",
    ),
    (
        "#### The `ProcessGroupInstanceModule` object",
        "#### Объект `ProcessGroupInstanceModule`",
    ),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    (
        "#### The `EntityTimeseriesData` object",
        "#### Объект `EntityTimeseriesData`",
    ),
    (
        "#### The `ProcessGroupInstance` object",
        "#### Объект `ProcessGroupInstance`",
    ),
    (
        "#### The `EntityBaselineData` object",
        "#### Объект `EntityBaselineData`",
    ),
    (
        "#### The `ConstraintViolation` object",
        "#### Объект `ConstraintViolation`",
    ),
    ("#### The `MonitoringState` object", "#### Объект `MonitoringState`"),
    ("#### The `TechnologyInfo` object", "#### Объект `TechnologyInfo`"),
    ("#### The `ProcessGroup` object", "#### Объект `ProcessGroup`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `AgentVersion` object", "#### Объект `AgentVersion`"),
    ("#### The `Application` object", "#### Объект `Application`"),
    ("#### The `UpdateEntity` object", "#### Объект `UpdateEntity`"),
    ("#### The `ResponseBody` object", "#### Объект `ResponseBody`"),
    ("#### The `HostGroup` object", "#### Объект `HostGroup`"),
    ("#### The `AnyValue` object", "#### Объект `AnyValue`"),
    ("#### The `TagInfo` object", "#### Объект `TagInfo`"),
    ("#### The `Service` object", "#### Объект `Service`"),
    ("#### The `Host` object", "#### Объект `Host`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    # --- shared boilerplate prose (L99/L4Y) ---
    (
        "To execute this request, you need an access token with `DataExport` scope.",
        "Для выполнения запроса необходим access token со scope `DataExport`.",
    ),
    (
        "To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает данные в формате `application/json`.",
    ),
    (
        "The request consumes an `application/json` payload.",
        "Запрос принимает данные в формате `application/json`.",
    ),
    (
        "The request consumes and produces an `application/json` payload.",
        "Запрос принимает и возвращает данные в формате `application/json`.",
    ),
    # process-groups/post-tags source-quirk: truncated sentence (no
    # "payload." suffix). Mirror faithfully (L93). Must run AFTER the longer
    # "...payload." variants above (longest-first) — no collision since this
    # exact string has no period/payload tail.
    (
        "The request produces an `application/json`\n",
        "Запрос возвращает данные в формате `application/json`\n",
    ),
    (
        "The request doesn't provide any configurable parameters.",
        "Запрос не предоставляет настраиваемых параметров.",
    ),
    (
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.",
    ),
    (
        "The API token is passed in the **Authorization** header.",
        "API-токен передаётся в заголовке **Authorization**.",
    ),
    (
        "The full list can be lengthy, so you can narrow it down by specifying filter parameters, like tags. See the **Parameters** section for more details.",
        "Полный список может быть длинным, поэтому его можно сузить, указав параметры фильтрации, например теги. Подробнее см. в разделе **Parameters**.",
    ),
    (
        "You can additionally limit the output by using the pagination:",
        "Дополнительно можно ограничить вывод с помощью постраничной разбивки:",
    ),
    (
        "1. Specify the number of results per page in the **pageSize** query parameter.",
        "1. Укажите количество результатов на странице в query-параметре **pageSize**.",
    ),
    (
        "2. Then use the cursor from the **Next-Page-Key** response header in the **nextPageKey** query parameter to obtain subsequent pages.",
        "2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в query-параметре **nextPageKey**, чтобы получить следующие страницы.",
    ),
    (
        "The timeframe is restricted to a **maximum period of 3 days**.",
        "Временной диапазон ограничен **максимальным периодом в 3 дня**.",
    ),
    (
        'The usage of this API is limited to value-only tags. To assign key:value tags, use the [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.").',
        'Использование этого API ограничено тегами только со значением. Чтобы назначить теги key:value, используйте [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags/post-tags "Назначение пользовательских тегов отслеживаемым сущностям через Dynatrace API.").',
    ),
    (
        "A list of tags to be assigned to a Dynatrace entity.",
        "Список тегов для назначения сущности Dynatrace.",
    ),
    (
        "Configuration of a custom device.",
        "Конфигурация custom device.",
    ),
    (
        "Information about a metric and its data points.",
        "Информация о метрике и её точках данных.",
    ),
    (
        "The result of a custom device push request. The entity ID is calculated automatically.",
        "Результат запроса push для custom device. ID сущности вычисляется автоматически.",
    ),
    # --- "The element can hold these values" -> "Возможные значения:" WITH
    #     colon (L99; also handles leading-dash `-The element ...`) ---
    ("The element can hold these values", "Возможные значения:"),
    # --- response-code description cells (longest/most-specific FIRST; L101:
    #     trailing period stays OUTSIDE the matched span -> source-faithful) ---
    (
        "Success. The custom device has been created or updated.",
        "Успех. Custom device создан или обновлён.",
    ),
    (
        "Success. The parameters of the application have been updated.",
        "Успех. Параметры приложения обновлены.",
    ),
    (
        "Success. The parameters of the process group have been updated.",
        "Успех. Параметры группы процессов обновлены.",
    ),
    (
        "Success. The parameters of the service have been updated.",
        "Успех. Параметры сервиса обновлены.",
    ),
    (
        "Success. The parameters of the host have been updated.",
        "Успех. Параметры хоста обновлены.",
    ),
    (
        "Success. The tag of the host has been removed.",
        "Успех. Тег хоста удалён.",
    ),
    (
        "Failed. The requested resource doesn't exist.",
        "Сбой. Запрашиваемый ресурс не существует.",
    ),
    ("Failed. The input is invalid.", "Сбой. Невалидный ввод."),
    (
        "Failure. The tag could not be found.",
        "Сбой. Тег не найден.",
    ),
    ("Client side error.", "Ошибка на стороне клиента."),
    ("Server side error.", "Ошибка на стороне сервера."),
    ("| Success |", "| Успех |"),
    # --- shared Error / ConstraintViolation object cells (verbatim canon
    #     from docs/managed-ru/.../rum/geographic-regions/get-countries.md) ---
    (
        "| code | integer | The HTTP status code |",
        "| code | integer | HTTP-код состояния |",
    ),
    (
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |",
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |",
    ),
    (
        "| message | string | The error message |",
        "| message | string | Сообщение об ошибке |",
    ),
    # ConstraintViolation object-intro standalone line
    ("\nA list of constraint violations\n", "\nСписок нарушений ограничений\n"),
    # --- shared Response-headers cells (all list endpoints) ---
    (
        "| Total-Count | integer | The estimated number of results. |",
        "| Total-Count | integer | Оценочное количество результатов. |",
    ),
    (
        "| Next-Page-Key | string | The cursor for the next page of results. Without it you'll get the first page again. |",
        "| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него снова вернётся первая страница. |",
    ),
    (
        "| Page-Size | string | The maximum number of results per page. |",
        "| Page-Size | string | Максимальное количество результатов на странице. |",
    ),
    # --- shared entity-element cells (TWINS: get-all <-> get-a-X). Each
    #     byte-identical across the relevant twin pair => one COMMON entry
    #     renders both. Longest-first ordering preserved by length sort
    #     intuition; explicit ordering not needed (no substring nesting). ---
    # Application object (applications get-all + get-an-app)
    (
        "| applicationMatchTarget | string | -Возможные значения: * `DOMAIN` * `URL` |",
        "| applicationMatchTarget | string | -Возможные значения: * `DOMAIN` * `URL` |",
    ),  # already enum-only after element-can-hold replace; no-op safety
    (
        "| customizedName | string | The customized name of the entity |",
        "| customizedName | string | Пользовательское имя сущности |",
    ),
    (
        "| discoveredName | string | The discovered name of the entity |",
        "| discoveredName | string | Обнаруженное имя сущности |",
    ),
    (
        "| displayName | string | The name of the Dynatrace entity as displayed in the UI. |",
        "| displayName | string | Имя сущности Dynatrace в том виде, как оно отображается в UI. |",
    ),
    (
        "| entityId | string | The Dynatrace entity ID of the required entity. |",
        "| entityId | string | ID сущности Dynatrace для нужной сущности. |",
    ),
    (
        "| firstSeenTimestamp | integer | The timestamp of when the entity was first detected, in UTC milliseconds |",
        "| firstSeenTimestamp | integer | Метка времени, когда сущность была впервые обнаружена, в миллисекундах UTC |",
    ),
    (
        "| lastSeenTimestamp | integer | The timestamp of when the entity was last detected, in UTC milliseconds |",
        "| lastSeenTimestamp | integer | Метка времени, когда сущность была обнаружена в последний раз, в миллисекундах UTC |",
    ),
    (
        "| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | The management zones that the entity is part of. |",
        "| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Management zone'ы, частью которых является сущность. |",
    ),
    (
        "| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of entity tags. |",
        "| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |",
    ),
    (
        "| fromRelationships | object | The list of outgoing calls from the application. |",
        "| fromRelationships | object | Список исходящих вызовов от приложения. |",
    ),
    (
        "| toRelationships | object | The list of incoming calls to the application. |",
        "| toRelationships | object | Список входящих вызовов к приложению. |",
    ),
    # EntityShortRepresentation (shared by ALL list/single + baseline twins)
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
    # AnyValue (shared everywhere)
    (
        "A schema representing an arbitrary value type.",
        "Схема, представляющая произвольный тип значения.",
    ),
    # TagInfo (shared by all entity twins)
    (
        "Tag of a Dynatrace entity.",
        "Тег сущности Dynatrace.",
    ),
    (
        "| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |",
        "| context | string | Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |",
    ),
    (
        "| key | string | The key of the tag.  Custom tags have the tag value here. |",
        "| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |",
    ),
    (
        "| value | string | The value of the tag.  Not applicable to custom tags. |",
        "| value | string | Значение тега.  Не применимо к пользовательским тегам. |",
    ),
    # TechnologyInfo (shared host/pg/pgi/service twins) - all "-" cells, no-op
    # AgentVersion (shared host + pgi twins)
    (
        "Defines the version of the agent currently running on the entity.",
        "Определяет версию агента, который сейчас работает на сущности.",
    ),
    (
        "| major | integer | The major version number. |",
        "| major | integer | Старший номер версии. |",
    ),
    (
        "| minor | integer | The minor version number. |",
        "| minor | integer | Младший номер версии. |",
    ),
    (
        "| revision | integer | The revision number. |",
        "| revision | integer | Номер ревизии. |",
    ),
    (
        "| sourceRevision | string | A string representation of the SVN revision number. |",
        "| sourceRevision | string | Строковое представление номера ревизии SVN. |",
    ),
    (
        '| timestamp | string | A timestamp string: format "yyyymmdd-hhmmss |',
        '| timestamp | string | Строка метки времени: формат "yyyymmdd-hhmmss |',
    ),
    # HostGroup (hosts twins)
    (
        "| meId | string | The Dynatrace entity ID of the host group. |",
        "| meId | string | ID сущности Dynatrace для host group. |",
    ),
    (
        "| name | string | The name of the Dynatrace entity, displayed in the UI. |",
        "| name | string | Имя сущности Dynatrace, отображаемое в UI. |",
    ),
    # Host object (hosts get-all + get-a-host)
    (
        "Information about the host.",
        "Информация о хосте.",
    ),
    (
        "| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Defines the version of the agent currently running on the entity. |",
        "| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Определяет версию агента, который сейчас работает на сущности. |",
    ),
    (
        "| awsNameTag | string | The name inherited from AWS. |",
        "| awsNameTag | string | Имя, унаследованное от AWS. |",
    ),
    (
        "| boshAvailabilityZone | string | The Cloud Foundry BOSH availability zone. |",
        "| boshAvailabilityZone | string | Зона доступности Cloud Foundry BOSH. |",
    ),
    (
        "| boshDeploymentId | string | The Cloud Foundry BOSH deployment ID. |",
        "| boshDeploymentId | string | ID развёртывания Cloud Foundry BOSH. |",
    ),
    (
        "| boshInstanceId | string | The Cloud Foundry BOSH instance ID. |",
        "| boshInstanceId | string | ID экземпляра Cloud Foundry BOSH. |",
    ),
    (
        "| boshInstanceName | string | The Cloud Foundry BOSH instance name. |",
        "| boshInstanceName | string | Имя экземпляра Cloud Foundry BOSH. |",
    ),
    (
        "| boshName | string | The Cloud Foundry BOSH name. |",
        "| boshName | string | Имя Cloud Foundry BOSH. |",
    ),
    (
        "| boshStemcellVersion | string | The Cloud Foundry BOSH stemcell version. |",
        "| boshStemcellVersion | string | Версия stemcell Cloud Foundry BOSH. |",
    ),
    (
        "| cloudPlatformVendorVersion | string | Defines the cloud platform vendor version. |",
        "| cloudPlatformVendorVersion | string | Определяет версию вендора облачной платформы. |",
    ),
    (
        "| consumedHostUnits | string | Consumed Host Units. Applicable only for [Dynatrace classic licensing](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |",
        "| consumedHostUnits | string | Потреблённые Host Unit'ы. Применимо только для [Dynatrace classic licensing](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |",
    ),
    (
        "| gceInstanceId | string | The Google Compute Engine instance ID. |",
        "| gceInstanceId | string | ID экземпляра Google Compute Engine. |",
    ),
    (
        "| gceInstanceName | string | The Google Compute Engine instance name. |",
        "| gceInstanceName | string | Имя экземпляра Google Compute Engine. |",
    ),
    (
        "| gceMachineType | string | The Google Compute Engine machine type. |",
        "| gceMachineType | string | Тип машины Google Compute Engine. |",
    ),
    (
        "| gceProject | string | The Google Compute Engine project. |",
        "| gceProject | string | Проект Google Compute Engine. |",
    ),
    (
        "| gceProjectId | string | The Google Compute Engine numeric project ID. |",
        "| gceProjectId | string | Числовой ID проекта Google Compute Engine. |",
    ),
    (
        "| gcePublicIpAddresses | string[] | The public IP addresses of the Google Compute Engine. |",
        "| gcePublicIpAddresses | string[] | Публичные IP-адреса Google Compute Engine. |",
    ),
    (
        "| gcpZone | string | The Google Cloud Platform Zone. |",
        "| gcpZone | string | Зона Google Cloud Platform. |",
    ),
    (
        "| kubernetesCluster | string | The kubernetes cluster the entity is in. |",
        "| kubernetesCluster | string | Кластер Kubernetes, в котором находится сущность. |",
    ),
    (
        "| kubernetesLabels | object | The kubernetes labels defined on the entity. |",
        "| kubernetesLabels | object | Метки Kubernetes, заданные на сущности. |",
    ),
    (
        "| kubernetesNode | string | The kubernetes node the entity is in. |",
        "| kubernetesNode | string | Узел Kubernetes, в котором находится сущность. |",
    ),
    (
        "| logicalCpus | integer | The AIX instance logical CPU count. |",
        "| logicalCpus | integer | Количество логических CPU экземпляра AIX. |",
    ),
    (
        "| networkZoneId | string | The ID of network zone the entity is in. |",
        "| networkZoneId | string | ID сетевой зоны, в которой находится сущность. |",
    ),
    (
        "| oneAgentCustomHostName | string | The custom name defined in OneAgent config. |",
        "| oneAgentCustomHostName | string | Пользовательское имя, заданное в конфигурации OneAgent. |",
    ),
    (
        "| simultaneousMultithreading | integer | The AIX instance simultaneous threads count. |",
        "| simultaneousMultithreading | integer | Количество одновременных потоков экземпляра AIX. |",
    ),
    (
        "| virtualCpus | integer | The AIX instance virtual CPU count. |",
        "| virtualCpus | integer | Количество виртуальных CPU экземпляра AIX. |",
    ),
    (
        "| zosCPUModelNumber | string | The CPU model number. |",
        "| zosCPUModelNumber | string | Номер модели CPU. |",
    ),
    (
        "| zosCPUSerialNumber | string | The CPU serial number. |",
        "| zosCPUSerialNumber | string | Серийный номер CPU. |",
    ),
    (
        "| zosLpaName | string | Name of the LPAR. |",
        "| zosLpaName | string | Имя LPAR. |",
    ),
    (
        "| zosSystemName | string | Name of the system. |",
        "| zosSystemName | string | Имя системы. |",
    ),
    (
        "| zosTotalGeneralPurposeProcessors | integer | Number of assigned processors for this LPAR. |",
        "| zosTotalGeneralPurposeProcessors | integer | Количество назначенных процессоров для этого LPAR. |",
    ),
    (
        "| zosTotalPhysicalMemory | integer | Memory assigned to the host (Terabyte). |",
        "| zosTotalPhysicalMemory | integer | Память, назначенная хосту (терабайт). |",
    ),
    (
        "| zosTotalZiipProcessors | integer | Number of assigned support processors for this LPAR. |",
        "| zosTotalZiipProcessors | integer | Количество назначенных вспомогательных процессоров для этого LPAR. |",
    ),
    (
        "| zosVirtualization | string | Type of virtualization on the mainframe. |",
        "| zosVirtualization | string | Тип виртуализации на мейнфрейме. |",
    ),
    (
        "| autoInjection | string | Status of auto-injection Возможные значения: * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |",
        "| autoInjection | string | Статус авто-внедрения Возможные значения: * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |",
    ),
    (
        "| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | The versions of the PaaS agents currently running on the entity. |",
        "| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии PaaS-агентов, которые сейчас работают на сущности. |",
    ),
    # ProcessGroup object (process-groups get-all + get-a-process-group)
    (
        "Parameters of a process group.",
        "Параметры группы процессов.",
    ),
    # ProcessGroupInstance object (processes get-all + get-a-process)
    (
        "Parameters of a process.",
        "Параметры процесса.",
    ),
    (
        "| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Versions of OneAgents currently running on the entity. |",
        "| agentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии OneAgent'ов, которые сейчас работают на сущности. |",
    ),
    (
        "| monitoringState | [MonitoringState](#openapi-definition-MonitoringState) | Defines the current monitoring state of an entity. |",
        "| monitoringState | [MonitoringState](#openapi-definition-MonitoringState) | Определяет текущее состояние мониторинга сущности. |",
    ),
    # MonitoringState object (processes twins)
    (
        "Defines the current monitoring state of an entity.",
        "Определяет текущее состояние мониторинга сущности.",
    ),
    (
        "| actualMonitoringState | string | The current actual monitoring state on the entity. Возможные значения: * `OFF` * `ON` |",
        "| actualMonitoringState | string | Текущее фактическое состояние мониторинга на сущности. Возможные значения: * `OFF` * `ON` |",
    ),
    (
        "| expectedMonitoringState | string | The monitoring state that is expected from the configuration Возможные значения: * `OFF` * `ON` |",
        "| expectedMonitoringState | string | Состояние мониторинга, ожидаемое из конфигурации Возможные значения: * `OFF` * `ON` |",
    ),
    (
        "| restartRequired | boolean | Defines whether or not the process has to restarted to enable monitoring |",
        "| restartRequired | boolean | Определяет, нужно ли перезапустить процесс для включения мониторинга |",
    ),
    # Service object (services get-all + get-a-service)
    (
        "| akkaActorSystem | string | The services of the akka actor system. |",
        "| akkaActorSystem | string | Сервисы системы акторов akka. |",
    ),
    (
        "| esbApplicationName | string | The ESB application name. |",
        "| esbApplicationName | string | Имя ESB-приложения. |",
    ),
    (
        "| ibmCtgGatewayUrl | string | The IBM CTG gateway URL. |",
        "| ibmCtgGatewayUrl | string | URL шлюза IBM CTG. |",
    ),
    (
        "| ibmCtgServerName | string | The IBM CICS Transaction Gateway name. |",
        "| ibmCtgServerName | string | Имя IBM CICS Transaction Gateway. |",
    ),
    (
        "| iibApplicationName | string | The IIB application name. |",
        "| iibApplicationName | string | Имя IIB-приложения. |",
    ),
    (
        "| publicDomainName | object | Public domain name. |",
        "| publicDomainName | object | Публичное доменное имя. |",
    ),
    (
        "| remoteEndpoint | string | The endpoint of the remote service. |",
        "| remoteEndpoint | string | Endpoint удалённого сервиса. |",
    ),
    (
        "| remoteServiceName | string | The name of the remote service. |",
        "| remoteServiceName | string | Имя удалённого сервиса. |",
    ),
    (
        "| serviceDetectionAttributes | object | Attributes that contributed to the service id. |",
        "| serviceDetectionAttributes | object | Атрибуты, повлиявшие на service id. |",
    ),
    # EntityBaselineData object (applications + services get-baseline twins)
    (
        "The baseline data for a Dynatrace entity for a specific duration metric.",
        "Базовая линия для сущности Dynatrace по конкретной метрике длительности.",
    ),
    (
        "| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for child entities of this entity, for example a `SERVICE_METHOD` of a `SERVICE_METHOD_GROUP`. |",
        "| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для дочерних сущностей этой сущности, например `SERVICE_METHOD` у `SERVICE_METHOD_GROUP`. |",
    ),
    (
        "| displayName | string | The display name of the entity. |",
        "| displayName | string | Отображаемое имя сущности. |",
    ),
    (
        "| entityId | string | The ID of the Dynatrace entity. |",
        "| entityId | string | ID сущности Dynatrace. |",
    ),
    (
        "| errorRate | number | The error rate baseline. |",
        "| errorRate | number | Базовая линия частоты ошибок. |",
    ),
    (
        "| hasLoadBaseline | boolean | The entity has a load baseline (`true`) or doesn't (`false`). |",
        "| hasLoadBaseline | boolean | У сущности есть базовая линия нагрузки (`true`) или нет (`false`). |",
    ),
    (
        "| micros90thPercentile | number | The 90th percentile baseline, in microseconds. |",
        "| micros90thPercentile | number | Базовая линия 90-го перцентиля, в микросекундах. |",
    ),
    (
        "| microsMedian | number | The median baseline, in microseconds. |",
        "| microsMedian | number | Медианная базовая линия, в микросекундах. |",
    ),
    # CustomDevicePushMessage / EntityTimeseriesData / CustomDevicePushResult
    # (custom-device create + report twins) - byte-identical, COMMON.
    (
        "| configUrl | string | The URL of a configuration web page for the custom device, such as a login page for a firewall or router. | Optional |",
        "| configUrl | string | URL веб-страницы конфигурации custom device, например страница входа для firewall или роутера. | Optional |",
    ),
    (
        "| displayName | string | The name of the custom device that will appear in the user interface. | Optional |",
        "| displayName | string | Имя custom device, которое появится в пользовательском интерфейсе. | Optional |",
    ),
    (
        "| favicon | string | The icon to be displayed for your custom component within Smartscape. Provide the full URL of the icon file. | Optional |",
        "| favicon | string | Иконка, отображаемая для вашего пользовательского компонента в Smartscape. Укажите полный URL файла иконки. | Optional |",
    ),
    (
        "| group | string | User defined group ID of entity.  The group ID helps to keep a consistent picture of device-group relations. One of many cases where a proper group is important is service detection: you can define which custom devices should lead to the same service by defining the same group ID for them.  If you set a group ID, it will be hashed into the Dynatrace entity ID of the custom device. In that case the custom device can only be part of one custom device group.  If you don't set the group ID, Dynatrace will create it based on the ID or type of the custom device. Also, the group will not be hashed into the device ID which means the device may switch groups. | Optional |",
        "| group | string | Заданный пользователем ID группы сущности.  ID группы помогает поддерживать согласованную картину связей устройство-группа. Один из многих случаев, где важна правильная группа, это обнаружение сервисов: вы можете определить, какие custom device должны вести к одному сервису, задав им одинаковый ID группы.  Если вы задаёте ID группы, он будет захеширован в ID сущности Dynatrace для custom device. В этом случае custom device может быть частью только одной группы custom device.  Если вы не задаёте ID группы, Dynatrace создаст его на основе ID или типа custom device. Также группа не будет захеширована в ID устройства, что означает, что устройство может менять группы. | Optional |",
    ),
    (
        "| hostNames | string[] | The list of host names related to the custom device.  These names are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value, the existing values will be overwritten.  If you send `null` or an empty value; or omit this field, the existing values will be kept. | Optional |",
        "| hostNames | string[] | Список имён хостов, связанных с custom device.  Эти имена используются для автоматического обнаружения горизонтальной связи взаимодействия между этим компонентом и всеми другими наблюдаемыми компонентами в Smartscape. Как только связь обнаружена, она автоматически отображается на карте Smartscape.  Если вы отправляете значение, существующие значения будут перезаписаны.  Если вы отправляете `null` или пустое значение; или опускаете это поле, существующие значения будут сохранены. | Optional |",
    ),
    (
        "| ipAddresses | string[] | The list of IP addresses that belong to the custom device.  These addresses are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value (including an empty value), the existing values will be overwritten.  If you send `null` or omit this field, the existing values will be kept. | Optional |",
        "| ipAddresses | string[] | Список IP-адресов, принадлежащих custom device.  Эти адреса используются для автоматического обнаружения горизонтальной связи взаимодействия между этим компонентом и всеми другими наблюдаемыми компонентами в Smartscape. Как только связь обнаружена, она автоматически отображается на карте Smartscape.  Если вы отправляете значение (включая пустое значение), существующие значения будут перезаписаны.  Если вы отправляете `null` или опускаете это поле, существующие значения будут сохранены. | Optional |",
    ),
    (
        "| listenPorts | integer[] | The list of ports the custom devices listens to.  These ports are used to discover the horizontal communication relationship between this component and all other observed components within Smartscape.  Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If ports are specified, you should also add at least one IP address or a host name for the custom device.  If you send a value, the existing values will be overwritten.  If you send `null`, or an empty value, or omit this field, the existing values will be kept. | Optional |",
        "| listenPorts | integer[] | Список портов, которые слушает custom device.  Эти порты используются для обнаружения горизонтальной связи взаимодействия между этим компонентом и всеми другими наблюдаемыми компонентами в Smartscape.  Как только связь обнаружена, она автоматически отображается на карте Smartscape.  Если порты указаны, следует также добавить хотя бы один IP-адрес или имя хоста для custom device.  Если вы отправляете значение, существующие значения будут перезаписаны.  Если вы отправляете `null`, или пустое значение, или опускаете это поле, существующие значения будут сохранены. | Optional |",
    ),
    (
        "| properties | object | The list of key-value pair properties that will be shown beneath the infographics of your custom device. | Optional |",
        "| properties | object | Список свойств в виде пар ключ-значение, которые будут показаны под инфографикой вашего custom device. | Optional |",
    ),
    (
        "| series | [EntityTimeseriesData[]](#openapi-definition-EntityTimeseriesData) | The list of metric values that are reported for the custom device.  The metric you're reporting must already exist in Dynatrace. To learn how to create a custom metric, see [Timeseries API v1 - PUT a custom metric](https://dt-url.net/5k143rzb).  Dynatrace aggregates all the values you report for a custom device.  If you send a value (including an empty value), it will be added to the set of existing values.  If you send `null` or omit this field, the set of existing values won't change. | Optional |",
        "| series | [EntityTimeseriesData[]](#openapi-definition-EntityTimeseriesData) | Список значений метрик, которые сообщаются для custom device.  Метрика, которую вы сообщаете, уже должна существовать в Dynatrace. О том, как создать пользовательскую метрику, см. [Timeseries API v1 - PUT a custom metric](https://dt-url.net/5k143rzb).  Dynatrace агрегирует все значения, которые вы сообщаете для custom device.  Если вы отправляете значение (включая пустое значение), оно будет добавлено к набору существующих значений.  Если вы отправляете `null` или опускаете это поле, набор существующих значений не изменится. | Optional |",
    ),
    (
        "| tags | string[] | List of custom tags that you want to attach to your custom device. | Optional |",
        "| tags | string[] | Список пользовательских тегов, которые вы хотите прикрепить к вашему custom device. | Optional |",
    ),
    (
        "| type | string | The technology type definition of the custom device.  It must be the same technology type of the metric you're reporting.  If you send a value, the existing value will be overwritten.  If you send `null`, empty or omit this field, the existing value will be kept. | Optional |",
        "| type | string | Определение типа технологии custom device.  Оно должно совпадать с типом технологии метрики, которую вы сообщаете.  Если вы отправляете значение, существующее значение будет перезаписано.  Если вы отправляете `null`, пустое значение или опускаете это поле, существующее значение будет сохранено. | Optional |",
    ),
    (
        "| dataPoints | array[] | List of data points.  Each data point is an array, containing the timestamp and the value.  Timestamp is UTC milliseconds reported as a number, for example: `1520523365557`.  You have the guaranteed timeframe of **30 minutes** into the past.  A custom metric must be registered **before** you can report a metric value. Therefore, the timestamp for reporting a value must be after the registration time of the metric. | Required |",
        "| dataPoints | array[] | Список точек данных.  Каждая точка данных это массив, содержащий метку времени и значение.  Метка времени это миллисекунды UTC, сообщаемые как число, например: `1520523365557`.  У вас есть гарантированный временной диапазон в **30 минут** в прошлое.  Пользовательская метрика должна быть зарегистрирована **до** того, как вы сможете сообщить значение метрики. Поэтому метка времени для сообщения значения должна быть после времени регистрации метрики. | Required |",
    ),
    (
        "| dimensions | object | Dimensions of the data points you're posting.  The key of the metric dimension must be defined earlier in the metric definition. | Optional |",
        "| dimensions | object | Измерения точек данных, которые вы отправляете.  Ключ измерения метрики должен быть определён ранее в определении метрики. | Optional |",
    ),
    (
        "| timeseriesId | string | The ID of the metric, where you want to post data points. | Required |",
        "| timeseriesId | string | ID метрики, в которую вы хотите отправить точки данных. | Required |",
    ),
    (
        "| entityId | string | The Dynatrace entity ID of the custom device. |",
        "| entityId | string | ID сущности Dynatrace для custom device. |",
    ),
    (
        "| groupId | string | The Dynatrace entity ID of the custom device group. |",
        "| groupId | string | ID сущности Dynatrace для группы custom device. |",
    ),
    # custom-device shared Example prose
    (
        "The API token is passed in the **Authorization** header.",
        "API-токен передаётся в заголовке **Authorization**.",
    ),  # also covered above; harmless duplicate (idempotent)
    (
        "The request returns the IDs of the custom device (see `entityId`) and its group (see `groupId`) as confirmation.",
        "Запрос возвращает ID custom device (см. `entityId`) и его группы (см. `groupId`) в качестве подтверждения.",
    ),
    (
        "You can download or copy the example request body to try it out on your own.",
        "Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.",
    ),
]

# ---------------------------------------------------------------- PER-FILE
# Long/unique strings; applied BEFORE COMMON. Authored longest-first.
P = {}

# ---- applications-api/get-all ----
P["applications-api/get-all.md"] = [
    (
        'Fetches the list of all [applications](/managed/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.") in your Dynatrace environment, along with their parameters.',
        'Получает список всех [приложений](/managed/discover-dynatrace/get-started/glossary#app "Познакомьтесь с терминологией Dynatrace.") в вашем окружении Dynatrace вместе с их параметрами.',
    ),
    (
        "| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |",
        "| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |",
    ),
    (
        "| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |",
        "| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |",
    ),
    (
        "| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
        "| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
    ),
    (
        "| tag | string[] | Filters the resulting set of applications by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The application has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |",
        "| tag | string[] | Фильтрует результирующий набор приложений по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Приложение должно соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |",
    ),
    (
        "| entity | string[] | Filters result to the specified applications only.  To specify several applications use the following format: `entity=ID1&entity=ID2`. | query | Optional |",
        "| entity | string[] | Ограничивает результат только указанными приложениями.  Чтобы указать несколько приложений, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |",
    ),
    (
        "| managementZone | integer | Only return applications that are part of the specified management zone. | query | Optional |",
        "| managementZone | integer | Возвращать только приложения, входящие в указанную management zone. | query | Optional |",
    ),
    (
        "| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |",
        "| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |",
    ),
    (
        "| pageSize | integer | The number of applications per result page.  If not set, pagination is not used and the result contains all applications fitting the specified filtering criteria. | query | Optional |",
        "| pageSize | integer | Количество приложений на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все приложения, подходящие под указанные критерии фильтрации. | query | Optional |",
    ),
    (
        "| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |",
        "| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |",
    ),
    (
        "In this example, the request asks for a list all the applications in the environment.",
        "В этом примере запрос запрашивает список всех приложений в окружении.",
    ),
    (
        "The result is truncated to three entries.",
        "Результат усечён до трёх записей.",
    ),
    # Related-topics: link-text = target RU H1 (Мониторинг реальных
    # пользователей), title-attr translated
    (
        '* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")',
        '* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")',
    ),
]

# ---- applications-api/get-an-app ----
P["applications-api/get-an-app.md"] = [
    (
        "Gets the parameters of the specified application.",
        "Получает параметры указанного приложения.",
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required application. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужного приложения. | path | Required |",
    ),
    (
        "In this example, the request inquires about the properties of the **easyTravel Demo** application, which has the ID **MOBILE\\_APPLICATION-752C288D59734C79**.",
        "В этом примере запрос запрашивает свойства приложения **easyTravel Demo**, у которого ID **MOBILE\\_APPLICATION-752C288D59734C79**.",
    ),
    (
        '* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")',
        '* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")',
    ),
]

# ---- applications-api/get-baseline ----
P["applications-api/get-baseline.md"] = [
    (
        "Gets the baseline data of the specified application.",
        "Получает базовую линию указанного приложения.",
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required application. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужного приложения. | path | Required |",
    ),
    (
        "The baseline data for an application and its children for each available duration metric.",
        "Базовая линия для приложения и его дочерних элементов по каждой доступной метрике длительности.",
    ),
    (
        "A duration metric is one of the following:",
        "Метрика длительности это одна из следующих:",
    ),
    (
        "| applicationDomInteractiveBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **DOM interactive** duration metric. |",
        "| applicationDomInteractiveBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **DOM interactive**. |",
    ),
    (
        "| applicationHtmlDownloadedBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **HTML downloaded** duration metric. |",
        "| applicationHtmlDownloadedBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **HTML downloaded**. |",
    ),
    (
        "| applicationLoadEventEndBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Load event end** duration metric. |",
        "| applicationLoadEventEndBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Load event end**. |",
    ),
    (
        "| applicationLoadEventStartBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Load event start** duration metric. |",
        "| applicationLoadEventStartBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Load event start**. |",
    ),
    (
        "| applicationResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Response time** duration metric. |",
        "| applicationResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Response time**. |",
    ),
    (
        "| applicationSpeedIndexBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Speed index** duration metric. |",
        "| applicationSpeedIndexBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Speed index**. |",
    ),
    (
        "| applicationTimeToFirstByteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Time to first byte** duration metric. |",
        "| applicationTimeToFirstByteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Time to first byte**. |",
    ),
    (
        "| applicationVisualCompleteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Visually complete** duration metric. |",
        "| applicationVisualCompleteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Visually complete**. |",
    ),
    (
        "| displayName | string | The name of the application as displayed in the UI. |",
        "| displayName | string | Имя приложения в том виде, как оно отображается в UI. |",
    ),
    (
        "| entityId | string | The Dynatrace entity ID of the application. |",
        "| entityId | string | ID сущности Dynatrace для приложения. |",
    ),
    (
        '* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")',
        '* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")',
    ),
]

# ---- applications-api/post-tags ----
P["applications-api/post-tags.md"] = [
    (
        'Assigns [custom tags](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to the specified application. You only need to provide a tag value. The `CONTEXTLESS` context will be assigned automatically.',
        'Назначает [пользовательские теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") указанному приложению. Нужно указать только значение тега. Context `CONTEXTLESS` будет назначен автоматически.',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the application you want to update. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для приложения, которое вы хотите обновить. | path | Required |",
    ),
    (
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |",
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Список тегов для назначения сущности Dynatrace. | body | Optional |",
    ),
    (
        "| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |",
        "| tags | string[] | Список тегов для назначения сущности Dynatrace. | Required |",
    ),
    (
        "In this example, the request assigns the tags **iOS app** and **Android app** to the **easyTravel Demo** application, which has the ID **MOBILE\\_APPLICATION-752C288D59734C79**.",
        "В этом примере запрос назначает теги **iOS app** и **Android app** приложению **easyTravel Demo**, у которого ID **MOBILE\\_APPLICATION-752C288D59734C79**.",
    ),
    (
        '* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")',
        '* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")',
    ),
]

# ---- custom-device-api/create-custom-device-via-dynatrace-api ----
P["custom-device-api/create-custom-device-via-dynatrace-api.md"] = [
    (
        "The **Custom device** endpoint of the **Topology and Smartscape** API enables you to create a custom device with a specified name in your Dynatrace environment.",
        "Endpoint **Custom device** API **Topology and Smartscape** позволяет создать custom device с заданным именем в вашем окружении Dynatrace.",
    ),
    (
        "This page describes how to create a custom device without sending any data to it.",
        "На этой странице описано, как создать custom device, не отправляя в него никаких данных.",
    ),
    (
        'To learn how to report data to a custom device, see [Report custom device metric via REST API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").',
        'О том, как сообщать данные в custom device, см. [Report custom device metric via REST API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать Dynatrace API для отправки точки данных пользовательской метрики в custom device.").',
    ),
    (
        "For this use case, the **series** element of the request body must be **omitted**.",
        "Для этого сценария элемент **series** тела запроса должен быть **опущен**.",
    ),
    (
        "| customDeviceId | string | The ID of the custom device.  If you use the ID of an existing device, the respective parameters will be updated.  Don't use Dynatrace entity ID here. | path | Required |",
        "| customDeviceId | string | ID custom device.  Если вы используете ID существующего устройства, соответствующие параметры будут обновлены.  Не используйте здесь ID сущности Dynatrace. | path | Required |",
    ),
    (
        "| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | The JSON body of the request. Contains parameters of a custom device. | body | Optional |",
        "| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | JSON-тело запроса. Содержит параметры custom device. | body | Optional |",
    ),
    (
        "In this example, the request creates custom device `idOfmyCustomDevice` of type `F5-Firewall`, with IP address `172.16.115.211` and listen port `9999`. The request also specifies some additional parameters.",
        "В этом примере запрос создаёт custom device `idOfmyCustomDevice` типа `F5-Firewall`, с IP-адресом `172.16.115.211` и портом прослушивания `9999`. Запрос также указывает некоторые дополнительные параметры.",
    ),
    (
        'See [Report custom device metric via the Dynatrace API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.") to learn how to submit data to the newly created custom device.',
        'См. [Report custom device metric via the Dynatrace API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать Dynatrace API для отправки точки данных пользовательской метрики в custom device."), чтобы узнать, как отправить данные в только что созданный custom device.',
    ),
    (
        "![New custom device in Smartscape](https://dt-cdn.net/images/custom-device-smartscape-1103-ba9b69e490.png)",
        "![Новый custom device в Smartscape](https://dt-cdn.net/images/custom-device-smartscape-1103-ba9b69e490.png)",
    ),
    (
        "\nNew custom device in Smartscape\n",
        "\nНовый custom device в Smartscape\n",
    ),
    (
        "![Properties of the custom device](https://dt-cdn.net/images/custom-device-658-bb2295e42c.png)",
        "![Свойства custom device](https://dt-cdn.net/images/custom-device-658-bb2295e42c.png)",
    ),
    (
        "\nProperties of the custom device",
        "\nСвойства custom device",
    ),
]

# ---- custom-device-api/report-custom-device-metric-via-rest-api ----
P["custom-device-api/report-custom-device-metric-via-rest-api.md"] = [
    (
        "The **Custom device** endpoint of the **Topology and Smartscape** API enables you to send a custom metric data point to a custom device in Dynatrace. This request is also able to update the metadata of the custom device.",
        "Endpoint **Custom device** API **Topology and Smartscape** позволяет отправить точку данных пользовательской метрики в custom device в Dynatrace. Этот запрос также может обновлять метаданные custom device.",
    ),
    # newline-anchored: this exact sentence ALSO appears as a substring inside
    # the `series` table-cell (handled by COMMON); anchor to the standalone
    # prose line so per-file does NOT pre-empt the longer COMMON cell (L4T).
    (
        "\nThe metric you're reporting must already exist in Dynatrace.\n",
        "\nМетрика, которую вы сообщаете, уже должна существовать в Dynatrace.\n",
    ),
    (
        'See [Create custom device via the Dynatrace API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Learn how you can use the Dynatrace API to create a custom device.") to learn how to create a custom device without sending data to it.',
        'См. [Create custom device via the Dynatrace API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Узнайте, как использовать Dynatrace API для создания custom device."), чтобы узнать, как создать custom device, не отправляя в него данные.',
    ),
    # source-quirk: "retrospectivelyâthe" (lone U+00E2 broken em-dash).
    # _normalize maps the stray byte to "-"; we match the post-normalize form
    # and translate the whole sentence (CLAUDE#0: no em-dash in RU).
    (
        "You can send data to the custom device retrospectively-the **custom device** endpoint supports the reporting of data up to one hour in the past. However, to ensure the proper functioning of AI root-cause analysis and metric-based alerting, we recommend that data be sent in real time.",
        "Вы можете отправлять данные в custom device задним числом: endpoint **custom device** поддерживает сообщение данных до одного часа в прошлое. Однако, чтобы обеспечить корректную работу AI-анализа первопричин и оповещений на основе метрик, рекомендуется отправлять данные в реальном времени.",
    ),
    (
        "For this use case, the **series** element of the request body is **required**.",
        "Для этого сценария элемент **series** тела запроса **обязателен**.",
    ),
    (
        "| customDeviceId | string | The ID of the custom device.  If you use the ID of an existing device, the respective parameters will be updated.  Don't use Dynatrace entity ID here. | path | Required |",
        "| customDeviceId | string | ID custom device.  Если вы используете ID существующего устройства, соответствующие параметры будут обновлены.  Не используйте здесь ID сущности Dynatrace. | path | Required |",
    ),
    (
        "| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | The JSON body of the request. Contains parameters of a custom device. | body | Optional |",
        "| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | JSON-тело запроса. Содержит параметры custom device. | body | Optional |",
    ),
    (
        "In this example, the request reports two data points of `custom:firewall.connections.dropped` for the `idOfmyCustomDevice` device. The data points (with value `460` for the `1539860400000` timestamp and value `456` for the `1539860460000` timestamp) belong to the `ethernetcard1` value of the `nic` dimension.",
        "В этом примере запрос сообщает две точки данных `custom:firewall.connections.dropped` для устройства `idOfmyCustomDevice`. Точки данных (со значением `460` для метки времени `1539860400000` и значением `456` для метки времени `1539860460000`) относятся к значению `ethernetcard1` измерения `nic`.",
    ),
    (
        "The request also reports two more data points of the same metric, but for `ethernetcard2` in the same dimension, and it updates device metadata by adding a property and a tag.",
        "Запрос также сообщает ещё две точки данных той же метрики, но для `ethernetcard2` в том же измерении, и обновляет метаданные устройства, добавляя свойство и тег.",
    ),
    (
        "![Metrics of the custom device in chart](https://dt-cdn.net/images/custom-devices-chart-1410-2a46660659.png)",
        "![Метрики custom device на графике](https://dt-cdn.net/images/custom-devices-chart-1410-2a46660659.png)",
    ),
    (
        "\nMetrics of the custom device in chart",
        "\nМетрики custom device на графике",
    ),
]

# ---- hosts-api (parent) ----
P["hosts-api.md"] = [
    (
        "The **Hosts** endpoints of the **Topology and Smartscape** API enable you to get details of currently monitored hosts and to assign tags to them.",
        "Endpoint'ы **Hosts** API **Topology and Smartscape** позволяют получать детали отслеживаемых в данный момент хостов и назначать им теги.",
    ),
    (
        '[### Fetch the list\n\nGet an overview of all hosts in your environment.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "List all monitored hosts via Dynatrace API.")[### Get details\n\nGet parameters of a host by its ID.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "View a monitored host via Dynatrace API.")[### Assign tags\n\nAssign custom tags to your hosts.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Assign tags to a monitored host via Dynatrace API.")[### Delete tags\n\nRemove custom tags from your hosts.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/del-tags "Delete tags from a monitored host via Dynatrace API.")',
        '[### Получить список\n\nОбзор всех хостов в вашем окружении.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "Список всех отслеживаемых хостов через Dynatrace API.")[### Получить детали\n\nПолучить параметры хоста по его ID.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "Просмотр отслеживаемого хоста через Dynatrace API.")[### Назначить теги\n\nНазначить пользовательские теги вашим хостам.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Назначение тегов отслеживаемому хосту через Dynatrace API.")[### Удалить теги\n\nУдалить пользовательские теги с ваших хостов.](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/del-tags "Удаление тегов с отслеживаемого хоста через Dynatrace API.")',
    ),
    (
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")',
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на здоровье хоста, как настроить пользовательские имена хостов и многое другое.")',
    ),
]

# ---- hosts-api/del-tags ----
P["hosts-api/del-tags.md"] = [
    (
        'Deletes the specified [custom tag](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") from the specified host. Deletion cannot be undone.',
        'Удаляет указанный [пользовательский тег](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") с указанного хоста. Удаление нельзя отменить.',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the host. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для хоста. | path | Required |",
    ),
    (
        "| tag | string | The tag to be removed. | path | Required |",
        "| tag | string | Тег, который нужно удалить. | path | Required |",
    ),
    (
        "In this example, the request deletes the **Rack123** tag from the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.",
        "В этом примере запрос удаляет тег **Rack123** с хоста **tag009**, у которого ID **HOST-B7A6F9EE9F366CB5**.",
    ),
    (
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")',
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на здоровье хоста, как настроить пользовательские имена хостов и многое другое.")',
    ),
]

# ---- hosts-api/get-a-host ----
P["hosts-api/get-a-host.md"] = [
    (
        "Gets the parameters of the specified host.",
        "Получает параметры указанного хоста.",
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required host. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужного хоста. | path | Required |",
    ),
    (
        "In this example, the request queries the parameters of the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.",
        "В этом примере запрос запрашивает параметры хоста **tag009**, у которого ID **HOST-B7A6F9EE9F366CB5**.",
    ),
    (
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")',
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на здоровье хоста, как настроить пользовательские имена хостов и многое другое.")',
    ),
]

# ---- hosts-api/get-all ----
P["hosts-api/get-all.md"] = [
    (
        "Gets the list of all hosts in your Dynatrace environment, along with their parameters.",
        "Получает список всех хостов в вашем окружении Dynatrace вместе с их параметрами.",
    ),
    (
        "| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |",
        "| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |",
    ),
    (
        "| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |",
        "| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |",
    ),
    (
        "| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
        "| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
    ),
    (
        "| tag | string[] | Filters the resulting set of hosts by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The host has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |",
        "| tag | string[] | Фильтрует результирующий набор хостов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |",
    ),
    (
        "| showMonitoringCandidates | boolean | Includes (`true`) or excludes (`false`) a monitoring candidate in the response.  Monitoring candidates are network entities that are detected but not monitored. | query | Optional |",
        "| showMonitoringCandidates | boolean | Включает (`true`) или исключает (`false`) кандидата на мониторинг в ответе.  Кандидаты на мониторинг это сетевые сущности, которые обнаружены, но не отслеживаются. | query | Optional |",
    ),
    (
        "| entity | string[] | Filters result to the specified hosts only.  To specify several hosts use the following format: `entity=ID1&entity=ID2`. | query | Optional |",
        "| entity | string[] | Ограничивает результат только указанными хостами.  Чтобы указать несколько хостов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |",
    ),
    (
        "| managementZone | integer | Only return hosts that are part of the specified management zone. | query | Optional |",
        "| managementZone | integer | Возвращать только хосты, входящие в указанную management zone. | query | Optional |",
    ),
    (
        "| hostGroupId | string | Filters the resulting set of hosts by the specified host group.  Specify the Dynatrace IDs of the host group you're interested in. | query | Optional |",
        "| hostGroupId | string | Фильтрует результирующий набор хостов по указанной host group.  Укажите ID Dynatrace интересующей вас host group. | query | Optional |",
    ),
    (
        "| hostGroupName | string | Filters the resulting set of hosts by the specified host group.  Specify the name of the host group you're interested in. | query | Optional |",
        "| hostGroupName | string | Фильтрует результирующий набор хостов по указанной host group.  Укажите имя интересующей вас host group. | query | Optional |",
    ),
    (
        "| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |",
        "| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |",
    ),
    (
        "| pageSize | integer | The number of hosts per result page.  If not set, pagination is not used and the result contains all hosts fitting the specified filtering criteria. | query | Optional |",
        "| pageSize | integer | Количество хостов на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все хосты, подходящие под указанные критерии фильтрации. | query | Optional |",
    ),
    (
        "| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |",
        "| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |",
    ),
    (
        "In this example, the request lists all hosts in the environment.",
        "В этом примере запрос выводит список всех хостов в окружении.",
    ),
    (
        "The result is truncated to two entries.",
        "Результат усечён до двух записей.",
    ),
    (
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")',
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на здоровье хоста, как настроить пользовательские имена хостов и многое другое.")',
    ),
]

# ---- hosts-api/post-tags ----
P["hosts-api/post-tags.md"] = [
    (
        'Assigns [custom tags](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to the specified host. You only need to provide a tag value. The `CONTEXTLESS` context will be assigned automatically.',
        'Назначает [пользовательские теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") указанному хосту. Нужно указать только значение тега. Context `CONTEXTLESS` будет назначен автоматически.',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the host to be updated. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для хоста, который нужно обновить. | path | Required |",
    ),
    (
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |",
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Список тегов для назначения сущности Dynatrace. | body | Optional |",
    ),
    (
        "| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |",
        "| tags | string[] | Список тегов для назначения сущности Dynatrace. | Required |",
    ),
    (
        "In this example, the request assigns the **Linux** and **Rack 123** tags to the **tag009** host, which has the ID of **HOST-B7A6F9EE9F366CB5**.",
        "В этом примере запрос назначает теги **Linux** и **Rack 123** хосту **tag009**, у которого ID **HOST-B7A6F9EE9F366CB5**.",
    ),
    (
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Learn how to get started with host monitoring, understand which measures contribute to host health, how to set up custom host names, and more.")',
        '* [Hosts](/managed/observe/infrastructure-observability/hosts "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на здоровье хоста, как настроить пользовательские имена хостов и многое другое.")',
    ),
]

# ---- process-groups-api (parent) ----
P["process-groups-api.md"] = [
    (
        'The **Process groups** endpoints of the **Topology and Smartscape** API enable you to get details of currently monitored [process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") and assign tags to them.',
        'Endpoint\'ы **Process groups** API **Topology and Smartscape** позволяют получать детали отслеживаемых в данный момент [групп процессов](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.") и назначать им теги.',
    ),
    (
        '[### Fetch the list\n\nGet an overview of all process groups in your environment.](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "List all monitored process groups via Dynatrace API.")[### Get details\n\nGet parameters of a process group by its ID.](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "View a monitored process group via Dynatrace API.")[### Assign tags\n\nAssign custom tags to your hosts.](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Assign tags to a monitored process group via Dynatrace API.")',
        '[### Получить список\n\nОбзор всех групп процессов в вашем окружении.](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "Список всех отслеживаемых групп процессов через Dynatrace API.")[### Получить детали\n\nПолучить параметры группы процессов по её ID.](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "Просмотр отслеживаемой группы процессов через Dynatrace API.")[### Назначить теги\n\nНазначить пользовательские теги вашим хостам.](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Назначение тегов отслеживаемой группе процессов через Dynatrace API.")',
    ),
    (
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")',
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")',
    ),
]

# ---- process-groups-api/get-all ----
P["process-groups-api/get-all.md"] = [
    (
        'Gets the list of all [process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") in your Dynatrace environment, along with their parameters and relationships.',
        'Получает список всех [групп процессов](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.") в вашем окружении Dynatrace вместе с их параметрами и связями.',
    ),
    (
        "| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |",
        "| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |",
    ),
    (
        "| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |",
        "| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |",
    ),
    (
        "| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
        "| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
    ),
    (
        "| tag | string[] | Filters the resulting set of process groups by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The process group has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |",
        "| tag | string[] | Фильтрует результирующий набор групп процессов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Группа процессов должна соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |",
    ),
    (
        "| entity | string[] | Filters result to the specified process groups only.  To specify several process groups use the following format: `entity=ID1&entity=ID2`. | query | Optional |",
        "| entity | string[] | Ограничивает результат только указанными группами процессов.  Чтобы указать несколько групп процессов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |",
    ),
    (
        "| host | string[] | Filters process groups by the host they're running at.  Specify Dynatrace IDs of the host you're interested in.  To specify several hosts use the following format: `host=hostID1&host=hostID2`.  The **OR** logic applies. | query | Optional |",
        "| host | string[] | Фильтрует группы процессов по хосту, на котором они работают.  Укажите ID Dynatrace интересующего вас хоста.  Чтобы указать несколько хостов, используйте следующий формат: `host=hostID1&host=hostID2`.  Применяется логика **OR**. | query | Optional |",
    ),
    (
        "| managementZone | integer | Only return process groups that are part of the specified management zone. | query | Optional |",
        "| managementZone | integer | Возвращать только группы процессов, входящие в указанную management zone. | query | Optional |",
    ),
    (
        "| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |",
        "| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |",
    ),
    (
        "| pageSize | integer | The number of process groups per result page.  If not set, pagination is not used and the result contains all process groups fitting the specified filtering criteria. | query | Optional |",
        "| pageSize | integer | Количество групп процессов на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все группы процессов, подходящие под указанные критерии фильтрации. | query | Optional |",
    ),
    (
        "| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |",
        "| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |",
    ),
    (
        "In this example, the request lists all the process groups of the environment detected **within the last 5 minutes**.",
        "В этом примере запрос выводит список всех групп процессов окружения, обнаруженных **за последние 5 минут**.",
    ),
    (
        "The result is truncated to two entries.",
        "Результат усечён до двух записей.",
    ),
    (
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")',
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")',
    ),
]

# ---- process-groups-api/get-a-process-group ----
P["process-groups-api/get-a-process-group.md"] = [
    (
        'Gets the parameters of the specified [process group](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.").',
        'Получает параметры указанной [группы процессов](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.").',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required process group. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужной группы процессов. | path | Required |",
    ),
    (
        "In this example, the request gets the details of the **PHP-FPM** process group, which has the ID of **PROCESS\\_GROUP-E5C3CC7EC1F80B5B**.",
        "В этом примере запрос получает детали группы процессов **PHP-FPM**, у которой ID **PROCESS\\_GROUP-E5C3CC7EC1F80B5B**.",
    ),
    (
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")',
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")',
    ),
]

# ---- process-groups-api/post-tags ----
P["process-groups-api/post-tags.md"] = [
    (
        'Assigns [custom tags](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to the specified [process group](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."). You need only provide a tag value. The `CONTEXTLESS` context will be assigned automatically.',
        'Назначает [пользовательские теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") указанной [группе процессов](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов."). Нужно указать только значение тега. Context `CONTEXTLESS` будет назначен автоматически.',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the process group to be updated. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для группы процессов, которую нужно обновить. | path | Required |",
    ),
    (
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | The JSON body of the request. Contains tags to be added to the process group. | body | Optional |",
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | JSON-тело запроса. Содержит теги, которые нужно добавить к группе процессов. | body | Optional |",
    ),
    (
        "| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |",
        "| tags | string[] | Список тегов для назначения сущности Dynatrace. | Required |",
    ),
    (
        "In this example, the request assigns the **PHP** tag to the **PHP-FPM** process group, which has the ID of **PROCESS\\_GROUP-E5C3CC7EC1F80B5B**.",
        "В этом примере запрос назначает тег **PHP** группе процессов **PHP-FPM**, у которой ID **PROCESS\\_GROUP-E5C3CC7EC1F80B5B**.",
    ),
    (
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")',
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")',
    ),
]

# ---- processes-api/get-all ----
P["processes-api/get-all.md"] = [
    (
        'Fetches the list of all [processes](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") in your Dynatrace environment, along with their parameters and relationships.',
        'Получает список всех [процессов](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.") в вашем окружении Dynatrace вместе с их параметрами и связями.',
    ),
    (
        "| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |",
        "| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |",
    ),
    (
        "| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |",
        "| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |",
    ),
    (
        "| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
        "| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
    ),
    (
        "| tag | string[] | Filters the resulting set of processes by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The process has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |",
        "| tag | string[] | Фильтрует результирующий набор процессов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Процесс должен соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |",
    ),
    (
        "| entity | string[] | Filters result to the specified processes only.  To specify several processes use the following format: `entity=ID1&entity=ID2`. | query | Optional |",
        "| entity | string[] | Ограничивает результат только указанными процессами.  Чтобы указать несколько процессов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |",
    ),
    (
        "| hostTag | string[] | Filters processes by the host they're running at.  Specify tags of the host you're interested in. | query | Optional |",
        "| hostTag | string[] | Фильтрует процессы по хосту, на котором они работают.  Укажите теги интересующего вас хоста. | query | Optional |",
    ),
    (
        "| host | string[] | Filters processes by the host they're running at.  Specify Dynatrace IDs of the host you're interested in.  To specify several hosts use the following format: `host=hostID1&host=hostID2`.  The **OR** logic applies. | query | Optional |",
        "| host | string[] | Фильтрует процессы по хосту, на котором они работают.  Укажите ID Dynatrace интересующего вас хоста.  Чтобы указать несколько хостов, используйте следующий формат: `host=hostID1&host=hostID2`.  Применяется логика **OR**. | query | Optional |",
    ),
    (
        "| actualMonitoringState | string | Filters processes by the actual monitoring state of the process. The element can hold these values * `OFF` * `ON` | query | Optional |",
        "| actualMonitoringState | string | Фильтрует процессы по фактическому состоянию мониторинга процесса. Возможные значения: * `OFF` * `ON` | query | Optional |",
    ),
    (
        "| expectedMonitoringState | string | Filters processes by the expected monitoring state of the process. The element can hold these values * `OFF` * `ON` | query | Optional |",
        "| expectedMonitoringState | string | Фильтрует процессы по ожидаемому состоянию мониторинга процесса. Возможные значения: * `OFF` * `ON` | query | Optional |",
    ),
    (
        "| managementZone | integer | Only return processes that are part of the specified management zone. | query | Optional |",
        "| managementZone | integer | Возвращать только процессы, входящие в указанную management zone. | query | Optional |",
    ),
    (
        "| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |",
        "| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |",
    ),
    (
        "| pageSize | integer | The number of processes per result page.  If not set, pagination is not used and the result contains all processes fitting the specified filtering criteria. | query | Optional |",
        "| pageSize | integer | Количество процессов на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все процессы, подходящие под указанные критерии фильтрации. | query | Optional |",
    ),
    (
        "| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |",
        "| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |",
    ),
    (
        "In this example, the request lists all processes in your Dynatrace environment detected **within the last 5 minutes**.",
        "В этом примере запрос выводит список всех процессов в вашем окружении Dynatrace, обнаруженных **за последние 5 минут**.",
    ),
    (
        "The result is truncated to two entries.",
        "Результат усечён до двух записей.",
    ),
    (
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")',
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")',
    ),
]

# ---- processes-api/get-a-process ----
P["processes-api/get-a-process.md"] = [
    (
        'Gets the parameters of the specified [process](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.").',
        'Получает параметры указанного [процесса](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.").',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required process. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужного процесса. | path | Required |",
    ),
    (
        "In this example, the request gets the details of the **Apache Web Server apache2** process, which has the ID of **PROCESS\\_GROUP\\_INSTANCE-EC9688429EB24B6B**.",
        "В этом примере запрос получает детали процесса **Apache Web Server apache2**, у которого ID **PROCESS\\_GROUP\\_INSTANCE-EC9688429EB24B6B**.",
    ),
    (
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.")',
        '* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")',
    ),
]

# ---- services-api/get-all ----
P["services-api/get-all.md"] = [
    (
        "Gets a list of all services in your Dynatrace environment, along with their parameters and relationships.",
        "Получает список всех сервисов в вашем окружении Dynatrace вместе с их параметрами и связями.",
    ),
    (
        "| startTimestamp | integer | The start timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then 72 hours behind from now is used. | query | Optional |",
        "| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |",
    ),
    (
        "| endTimestamp | integer | The end timestamp of the requested timeframe, in milliseconds (UTC).  If not set, then the current timestamp is used.  The timeframe must not exceed 3 days. | query | Optional |",
        "| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |",
    ),
    (
        "| relativeTime | string | The relative timeframe, back from now. The element can hold these values * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
        "| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |",
    ),
    (
        "| tag | string[] | Filters the resulting set of services by the specified tag. You can specify several tags in the following format: `tag=tag1&tag=tag2`. The service has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags, use the following format: `tag=[context]key:value`. For custom key-value tags, omit the context: `tag=key:value`. | query | Optional |",
        "| tag | string[] | Фильтрует результирующий набор сервисов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Сервис должен соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |",
    ),
    (
        "| entity | string[] | Filters result to the specified services only.  To specify several services use the following format: `entity=ID1&entity=ID2`. | query | Optional |",
        "| entity | string[] | Ограничивает результат только указанными сервисами.  Чтобы указать несколько сервисов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |",
    ),
    (
        "| managementZone | integer | Only return services that are part of the specified management zone. | query | Optional |",
        "| managementZone | integer | Возвращать только сервисы, входящие в указанную management zone. | query | Optional |",
    ),
    (
        "| includeDetails | boolean | Includes (`true`) or excludes (`false`) details which are queried from related entities.  Excluding details may make queries faster.  If not set, then `true` is used. | query | Optional |",
        "| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |",
    ),
    (
        "| pageSize | integer | The number of services per result page.  If not set, pagination is not used and the result contains all services fitting the specified filtering criteria. | query | Optional |",
        "| pageSize | integer | Количество сервисов на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все сервисы, подходящие под указанные критерии фильтрации. | query | Optional |",
    ),
    (
        "| nextPageKey | string | The cursor for the next page of results. You can find it in the **Next-Page-Key** header of the previous response.  If you're using pagination, the first page is always returned without this cursor.  You must keep all other query parameters as they were in the first request to obtain subsequent pages. | query | Optional |",
        "| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |",
    ),
    (
        "In this example, the request lists all the services of the environment detected **within the last 5 minutes**.",
        "В этом примере запрос выводит список всех сервисов окружения, обнаруженных **за последние 5 минут**.",
    ),
    (
        "The result is truncated to two entries.",
        "Результат усечён до двух записей.",
    ),
    (
        '* [Services](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")',
        '* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")',
    ),
]

# ---- services-api/get-a-service ----
P["services-api/get-a-service.md"] = [
    (
        "Gets the parameters of a specified service.",
        "Получает параметры указанного сервиса.",
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required service. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужного сервиса. | path | Required |",
    ),
    (
        "In this example, the request gets the details of the **PHP-FPM via domain socket /run/php7-fpm.sock** service, which has the ID of **SERVICE-72503CBDD2AEF066**.",
        "В этом примере запрос получает детали сервиса **PHP-FPM via domain socket /run/php7-fpm.sock**, у которого ID **SERVICE-72503CBDD2AEF066**.",
    ),
    (
        '* [Services](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")',
        '* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")',
    ),
]

# ---- services-api/get-baseline ----
P["services-api/get-baseline.md"] = [
    (
        "Gets the baseline data of the specified service.",
        "Получает базовую линию указанного сервиса.",
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the required service. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для нужного сервиса. | path | Required |",
    ),
    (
        "The baseline data for a service and its children for the **Response time** duration metric.",
        "Базовая линия для сервиса и его дочерних элементов по метрике длительности **Response time**.",
    ),
    (
        "| displayName | string | The display name of the service. |",
        "| displayName | string | Отображаемое имя сервиса. |",
    ),
    (
        "| entityId | string | The ID of the service. |",
        "| entityId | string | ID сервиса. |",
    ),
    (
        "| serviceResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | The baseline data for the **Response time** duration metric. |",
        "| serviceResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Response time**. |",
    ),
    (
        '* [Services](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")',
        '* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")',
    ),
]

# ---- services-api/post-tags ----
P["services-api/post-tags.md"] = [
    (
        'Assigns [custom tags](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to the specified service. You need to provide only a tag value. The `CONTEXTLESS` context will be assigned automatically.',
        'Назначает [пользовательские теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") указанному сервису. Нужно указать только значение тега. Context `CONTEXTLESS` будет назначен автоматически.',
    ),
    (
        "| meIdentifier | string | The Dynatrace entity ID of the service you're inquiring. | path | Required |",
        "| meIdentifier | string | ID сущности Dynatrace для сервиса, который вы запрашиваете. | path | Required |",
    ),
    (
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | A list of tags to be assigned to a Dynatrace entity. | body | Optional |",
        "| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Список тегов для назначения сущности Dynatrace. | body | Optional |",
    ),
    (
        "| tags | string[] | A list of tags to be assigned to a Dynatrace entity. | Required |",
        "| tags | string[] | Список тегов для назначения сущности Dynatrace. | Required |",
    ),
    (
        "In this example, the request assigns the **PHP** tag to the **PHP-FPM via domain socket /run/php7-fpm.sock** service, which has the ID of **SERVICE-72503CBDD2AEF066**.",
        "В этом примере запрос назначает тег **PHP** сервису **PHP-FPM via domain socket /run/php7-fpm.sock**, у которого ID **SERVICE-72503CBDD2AEF066**.",
    ),
    (
        '* [Services](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")',
        '* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")',
    ),
]


def build():
    written = []
    bad = []
    total_en = total_ru = 0
    for rel in FILES:
        ep = os.path.join(EN, rel.replace("/", os.sep))
        rp = os.path.join(RU, rel.replace("/", os.sep))
        with io.open(ep, "r", encoding="utf-8", newline="") as f:
            txt = f.read()
        en_lines = txt.replace("\r\n", "\n").count("\n")
        txt = _normalize(txt)
        for en, ru in P.get(rel, []):
            if en not in txt:
                print(f"  !! MISS per-file in {rel}: {en[:70]!r}")
            txt = txt.replace(en, ru)
        for en, ru in COMMON:
            txt = txt.replace(en, ru)
        os.makedirs(os.path.dirname(rp), exist_ok=True)
        with io.open(rp, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        ru_lines = txt.count("\n")
        total_en += en_lines
        total_ru += ru_lines
        flag = "" if en_lines == ru_lines else "  <<< MISMATCH"
        if flag:
            bad.append(rel)
        print(f"{en_lines:5d} EN | {ru_lines:5d} RU  {rel}{flag}")
        written.append(rel)
    print(f"\nTOTAL  {total_en} EN | {total_ru} RU   files={len(written)}")
    if bad:
        print("MISMATCH FILES:", bad)
    else:
        print("OK: all files line-parity equal")
    return written


if __name__ == "__main__":
    build()
