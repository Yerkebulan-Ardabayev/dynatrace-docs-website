# -*- coding: utf-8 -*-
from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/otlp-api"
FNAME = "ingest-logs.md"

TT_LOGMON = "Default limits for the latest version of Dynatrace Log Monitoring."
RU_LOGMON = "Ограничения по умолчанию для последней версии Dynatrace Log Monitoring."

TT_SEMATTR = "Supported semantic attributes that are indexed in Log Monitoring Classic."
RU_SEMATTR = (
    "Поддерживаемые семантические атрибуты, индексируемые в Log Monitoring Classic."
)

TT_POSTLOGS = "Send OpenTelemetry logs to Dynatrace via API."
RU_POSTLOGS = "Отправка логов OpenTelemetry в Dynatrace через API."

# Non-breaking hyphen U+2011 stays unchanged through norm(); must embed as literal.
# "X\xe2\x80\x91Dynatrace\xe2\x80\x91Options" — bytes are U+00E2 U+0080 U+0091 each.
_NBH = "â"  # mojibaked non-breaking hyphen, not handled by norm()
_ELL = "â¦"  # mojibaked ellipsis U+2026, not handled by norm()

TRANS = {
    # --- frontmatter ---
    "title: Ingest OTLP logs": "title: Приём логов OTLP",
    # --- page title (appears twice: H1 in frontmatter area and body) ---
    "# Ingest OTLP logs": "# Приём логов OTLP",
    # --- metadata bullets ---
    "* Reference": "* Справочник",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on May 04, 2026": "* Обновлено 04 мая 2026 г.",
    # --- intro ---
    "OpenTelemetry supports attributes at different levels in an OpenTelemetry log request, such as the resource level, scope level, and record level.": "OpenTelemetry поддерживает атрибуты на разных уровнях запроса логов OpenTelemetry: на уровне ресурса, уровне области видимости и уровне записи.",
    "The Log ingestion API collects and attempts to automatically transform log data.": "Log ingestion API собирает данные логов и выполняет их автоматическое преобразование.",
    # --- ## Data transformation ---
    "## Data transformation": "## Преобразование данных",
    "Each log record from the ingested batch is mapped to a single Dynatrace log record, which contains three special attributes: `timestamp`, `loglevel`, `content`, and a set of other key-value attributes. These properties are set based on keys present in the input object as follows.": "Каждая запись лога из принимаемого пакета сопоставляется с одной записью лога Dynatrace, которая содержит три специальных атрибута: `timestamp`, `loglevel`, `content`, а также набор других атрибутов в формате ключ-значение. Эти свойства задаются на основе ключей, присутствующих в объекте входных данных, следующим образом.",
    # --- ### Timestamp ---
    "### Timestamp": "### Timestamp",
    "* Set based on the **Timestamp** field of the input log record.": "* Задаётся на основе поля **Timestamp** входящей записи лога.",
    "* If the `timestamp` cannot be set based on the **Timestamp** field, `timestamp` is determined based on one of the following, evaluated in order:": "* Если `timestamp` не удаётся задать на основе поля **Timestamp**, `timestamp` определяется на основе одного из следующих источников в порядке их оценки:",
    "1. The content of the body (if the body is a map).": "1. Содержимое тела (если тело является отображением).",
    "2. The attributes of the OTLP log record.": "2. Атрибуты записи лога OTLP.",
    "* If the timestamp is taken from the body or OTLP log record, it is set based on the value of the first key from the following list, evaluated in the order presented in the list, and is case-insensitive: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.": "* Если метка времени берётся из тела или записи лога OTLP, она задаётся на основе значения первого ключа из следующего списка (оценка ведётся в порядке, указанном в списке; регистр не учитывается): `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.",
    # L33: norm() converts â\x80\x94 -> em-dash; key must use em-dash.
    "* Supported timestamp formats: Unix epoch time in UTC (seconds, milliseconds, or seconds with a fractional part — available from Dynatrace version 1.339), `RFC3339`, and `RFC3164`.": "* Поддерживаемые форматы меток времени: Unix epoch time в UTC (секунды, миллисекунды или секунды с дробной частью; доступно начиная с версии Dynatrace 1.339), `RFC3339` и `RFC3164`.",
    "* The default value is the current timestamp and the default timezone is UTC if it's missing in timestamp.": "* Значение по умолчанию: текущая метка времени; часовой пояс по умолчанию: UTC, если он не указан в метке времени.",
    "* Log events older than the **Log Age** limit are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time. See the [Ingestion limits](#ingestion-limits) section for details.": "* События лога, превышающие лимит **Log Age**, отбрасываются. Метки времени, опережающие текущее время более чем на 10 минут, заменяются текущим временем. Подробности см. в разделе [Лимиты приёма данных](#ingestion-limits).",
    # --- ### Log level ---
    "### Log level": "### Log level",
    "* Set based on the **SeverityText** field (first priority) or **SeverityNumber** field (second priority) of the input log record.": "* Задаётся на основе поля **SeverityText** (первый приоритет) или поля **SeverityNumber** (второй приоритет) входящей записи лога.",
    "* If the `loglevel` cannot be set based on the **SeverityText** or **SeverityNumber** field, `loglevel` is determined based on one of the following, evaluated in order:": "* Если `loglevel` не удаётся задать на основе поля **SeverityText** или **SeverityNumber**, `loglevel` определяется на основе одного из следующих источников в порядке их оценки:",
    "* If the `loglevel` is taken from the body or OTLP log record, it is set based on the value of the first key from the following list, evaluated in the order presented in the list, and is case-insensitive: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.": "* Если `loglevel` берётся из тела или записи лога OTLP, он задаётся на основе значения первого ключа из следующего списка (оценка ведётся в порядке, указанном в списке; регистр не учитывается): `loglevel`, `status`, `severity`, `level`, `syslog.severity`.",
    "* The default value is `NONE`.": "* Значение по умолчанию: `NONE`.",
    # --- ### Content ---
    "### Content": "### Content",
    "* The content is set based on the **Body** field of the input log record.": "* Содержимое задаётся на основе поля **Body** входящей записи лога.",
    "* If the **Body** field is of **kvlist\\_value** type (a list of key-value pairs), `content` is set based on the value of the first key found in **Body** from the following list, evaluated in the order presented in the list: `content`, `message`, `payload`, `body`, `log`.": "* Если поле **Body** имеет тип **kvlist\\_value** (список пар ключ-значение), `content` задаётся на основе значения первого найденного в **Body** ключа из следующего списка в указанном порядке: `content`, `message`, `payload`, `body`, `log`.",
    "* If no attribute is found among supported content keys, then `content` is set to an empty string.": "* Если ни один атрибут из поддерживаемых ключей содержимого не найден, `content` устанавливается в пустую строку.",
    "* If the **Body** field is not a string type, the value is stringified. In case of complex types, it is stringified as a JSON string.": "* Если поле **Body** не является строковым типом, значение преобразуется в строку. Для сложных типов значение преобразуется в строку JSON.",
    # --- ### Attributes ---
    "### Attributes": "### Attributes",
    "* Contains all other attributes from the input record's attributes contained in the sections: **Resource**, **InstrumentationScope**, and **Attributes**.": "* Содержит все остальные атрибуты из атрибутов входящей записи, содержащихся в разделах: **Resource**, **InstrumentationScope** и **Attributes**.",
    "* The `TraceID` and `SpanID` attributes are mapped to the `trace_id` and `span_id` fields, and their values are converted to hexadecimal representation (e.g., `0xCAFEBABE`).": "* Атрибуты `TraceID` и `SpanID` сопоставляются с полями `trace_id` и `span_id`, а их значения преобразуются в шестнадцатеричное представление (например, `0xCAFEBABE`).",
    "* Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.": "* Автоматический атрибут. Атрибут `dt.auth.origin` автоматически добавляется к каждой записи лога, принимаемой через API. Этот атрибут представляет собой открытую часть API-ключа, которую источник лога использует для авторизации подключения к универсальному API приёма логов.",
    # L64: EN typo "correctly.Refer" (missing space) — reproduced faithfully in value.
    'All attributes should preferably map to **semantic attributes** for Dynatrace to interpret them correctly.Refer to the [Semantic attributes (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes "%s") for more details.'
    % TT_SEMATTR: 'Все атрибуты предпочтительно должны сопоставляться с **семантическими атрибутами**, чтобы Dynatrace мог корректно их интерпретировать.Подробности см. в разделе [Семантические атрибуты (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes "%s").'
    % RU_SEMATTR,
    # --- ## Data types ---
    "## Data types": "## Типы данных",
    "Dynatrace supports OpenTelemetry data types as described in the sections below.": "Dynatrace поддерживает типы данных OpenTelemetry, описанные в разделах ниже.",
    # --- ### Scalar value ---
    "### Scalar value": "### Скалярное значение",
    "All attribute keys are lowercased and all attribute values are stringified. Custom attributes and semantic attributes can generally be used in queries.": "Все ключи атрибутов приводятся к нижнему регистру, а все значения атрибутов преобразуются в строки. Пользовательские атрибуты и семантические атрибуты, как правило, можно использовать в запросах.",
    # --- ### Byte array ---
    "### Byte array": "### Массив байтов",
    "Byte arrays are converted to base64-encoded strings. For example, the following array": "Массивы байтов преобразуются в строки в кодировке base64. Например, следующий массив",
    "is transformed and ingested as `aGVsbG8gd29yZA==`.": "преобразуется и принимается как `aGVsbG8gd29yZA==`.",
    # --- ### Array ---
    "### Array": "### Массив",
    "Array attribute values are converted to arrays of a uniform type. The target type is chosen according to the following rules:": "Значения атрибутов-массивов преобразуются в массивы однородного типа. Целевой тип выбирается по следующим правилам:",
    "* Complex values, such as arrays, or objects are mapped to JSON string values.": "* Сложные значения, такие как массивы или объекты, сопоставляются со строковыми значениями JSON.",
    "* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.": "* Если любое значение в массиве является строкой или если любое значение необходимо преобразовать в строку (например, объект или массив), целевой тип всего массива: строка.",
    "* If all values in the source array are numeric, the target array type is numeric.": "* Если все значения в исходном массиве числовые, целевой тип массива: числовой.",
    "* Null values are considered compatible with any type.": "* Значения null считаются совместимыми с любым типом.",
    # --- ### Map ---
    "### Map": "### Отображение",
    "Maps are ingested by extracting their keys recursively and storing the values as separate attributes, with names reflecting their position in the map hierarchy and prefixed with the map name. See [Log ingestion API processing](#otlp-structured-logs) for more details.": "Отображения принимаются путём рекурсивного извлечения их ключей с сохранением значений в виде отдельных атрибутов, имена которых отражают их положение в иерархии отображения и имеют префикс из имени отображения. Подробности см. в разделе [Обработка в Log ingestion API](#otlp-structured-logs).",
    # --- ## Ingestion limits ---
    "## Ingestion limits": "## Лимиты приёма данных",
    'See [Log Monitoring default limits (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "%s") for the limits applied to ingested log requests, their attributes, and their attribute values.'
    % TT_LOGMON: 'Лимиты, применяемые к принимаемым запросам логов, их атрибутам и значениям атрибутов, см. в разделе [Ограничения Log Monitoring по умолчанию (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "%s").'
    % RU_LOGMON,
    # --- ## Log ingestion API processing ---
    "## Log ingestion API processing": "## Обработка в Log ingestion API",
    "The content of structured logs is transformed as described in the sections below. All the following examples apply to Log ingestion API endpoints available on Environment ActiveGate.": "Содержимое структурированных логов преобразуется так, как описано в разделах ниже. Все приведённые примеры применимы к эндпоинтам Log ingestion API, доступным в Environment ActiveGate.",
    # --- #### Maps and arrays in attributes ---
    "#### Maps and arrays in attributes": "#### Отображения и массивы в атрибутах",
    "In this case, the map attribute values are flattened, i.e. replaced with keys concatenated using a dot (.) until a simple value is reached in the hierarchy, and the array attribute values are turned into a custom string.": "В этом случае значения атрибутов-отображений уплощаются, то есть заменяются ключами, объединёнными точкой (.), вплоть до достижения простого значения в иерархии, а значения атрибутов-массивов преобразуются в пользовательскую строку.",
    "| Input | Log ingestion API endpoint output |": "| Входные данные | Выходные данные эндпоинта Log ingestion API |",
    "Flattening proceeds up to the maximum nesting level specified by the **Nested objects** limit. Structures nested deeper than this are replaced with the string value `<truncated due to nesting limit>`. See the [Ingestion limits](#ingestion-limits) section for details.": "Уплощение продолжается до максимального уровня вложенности, заданного лимитом **Nested objects**. Структуры, вложенные глубже этого уровня, заменяются строковым значением `<truncated due to nesting limit>`. Подробности см. в разделе [Лимиты приёма данных](#ingestion-limits).",
    # --- #### Map in body ---
    "#### Map in body": "#### Отображение в теле",
    "If the **Body** field is of **kvlist\\_value** type (a list of key-value pairs), the structure is processed in the same way as log record attributes, including flattening and conflict resolution.": "Если поле **Body** имеет тип **kvlist\\_value** (список пар ключ-значение), структура обрабатывается так же, как атрибуты записи лога, включая уплощение и разрешение конфликтов.",
    "Attributes found in **Body** may also be used for setting the `timestamp`, `loglevel`, and `content` attributes of the log record, as described below.": "Атрибуты, найденные в **Body**, также могут использоваться для задания атрибутов `timestamp`, `loglevel` и `content` записи лога, как описано ниже.",
    # --- #### Body as array ---
    "#### Body as array": "#### Тело как массив",
    "In this case, the array in the body is stringified.": "В этом случае массив в теле преобразуется в строку.",
    # --- #### Name conflicts ---
    "#### Name conflicts": "#### Конфликты имён",
    "When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate.": "Когда атрибуты сохраняются в уплощённом виде на стороне Dynatrace, возможны конфликты имён, если атрибуты на разных уровнях имеют одинаковое имя. Dynatrace разрешает это, добавляя к дублирующимся атрибутам префикс `overwritten[COUNTER].`. Значение счётчика указывает, сколько раз данное имя атрибута уже встречалось как дубликат.",
    "For example, if you have three attributes all named `my.attribute` on the resource, scope, and log levels:": "Например, если на уровнях ресурса, области видимости и лога есть три атрибута с именем `my.attribute`:",
    "* the resource attribute is ingested as `my.attribute`": "* атрибут ресурса принимается как `my.attribute`",
    "* the scope attribute is ingested as `overwritten1.my.attribute`": "* атрибут области видимости принимается как `overwritten1.my.attribute`",
    "* the log attribute is ingested as `overwritten2.my.attribute`": "* атрибут лога принимается как `overwritten2.my.attribute`",
    # --- ## Additional attributers handling ---
    # EN heading typo "attributers" (= "attributes"); prose heading, no inbound anchor
    # links to that slug, so translated by intended meaning (not a code token per §3).
    "## Additional attributers handling": "## Обработка дополнительных атрибутов",
    "The Log ingestion API additionally accepts log attributes through:": "Log ingestion API дополнительно принимает атрибуты лога через:",
    "* Query parameters": "* Параметры запроса",
    "* Special header: `X-Dynatrace-Attr`": "* Специальный заголовок: `X-Dynatrace-Attr`",
    "These attributes are merged with those provided in the OpenTelemetry log request according to the rules described below.": "Эти атрибуты объединяются с атрибутами, переданными в запросе логов OpenTelemetry, согласно правилам, описанным ниже.",
    # --- ### Query parameter attributes ---
    "### Query parameter attributes": "### Атрибуты из параметров запроса",
    "* All query parameters passed to the Log ingestion API endpoint are added to the log record attributes.": "* Все параметры запроса, переданные в эндпоинт Log ingestion API, добавляются к атрибутам записи лога.",
    "* If a parameter key appears multiple times, all values are captured as an array attribute.": "* Если ключ параметра встречается несколько раз, все значения фиксируются как атрибут-массив.",
    "* Keys and values follow the same attribute parsing rules as log request attributes.": "* Ключи и значения следуют тем же правилам разбора атрибутов, что и атрибуты запроса логов.",
    # L157: mojibaked non-breaking hyphen \xe2\x80\x91 in "X—Dynatrace—Options".
    # norm() does NOT convert this sequence, so key must embed these chars literally.
    "* Certain parameters are processed by the API for internal purposes and never appear as log record attributes, even if explicitly provided (such as those used in the **X"
    + _NBH
    + "Dynatrace"
    + _NBH
    + 'Options** header). For the complete list of reserved parameter names and their processing behavior, see the [API documentation](/managed/dynatrace-api/environment-api/opentelemetry/post-logs#parameters "%s").'
    % TT_POSTLOGS: '* Некоторые параметры обрабатываются API во внутренних целях и никогда не появляются как атрибуты записи лога, даже если переданы явно (например, используемые в заголовке **X-Dynatrace-Options**). Полный список зарезервированных имён параметров и описание их поведения при обработке см. в [документации API](/managed/dynatrace-api/environment-api/opentelemetry/post-logs#parameters "%s").'
    % RU_POSTLOGS,
    # --- #### Example (query params) ---
    "#### Example": "#### Пример",
    "| Request URL | Resulting output |": "| URL запроса | Результирующий вывод |",
    # --- ### Header-based attributes ---
    "### Header-based attributes (X-Dynatrace-Attr)": "### Атрибуты на основе заголовка (X-Dynatrace-Attr)",
    "The API supports a special header for passing additional attributes:": "API поддерживает специальный заголовок для передачи дополнительных атрибутов:",
    "Rules:": "Правила:",
    "* Keys and values follow the same attribute parsing rules as query parameters.": "* Ключи и значения следуют тем же правилам разбора атрибутов, что и параметры запроса.",
    "* Multi-value behavior is also supported inside the header attributes.": "* Поведение для нескольких значений также поддерживается внутри атрибутов заголовка.",
    "* Same reserved parameter names restrictions apply.": "* Применяются те же ограничения на зарезервированные имена параметров.",
    # --- ### Attributes precedence rules ---
    "### Attributes precedence rules": "### Правила приоритета атрибутов",
    "When attributes appear in multiple places, the Log ingestion API applies attribute precedence while still preserving body values for auditability. The attributes are applied in the following order:": "Когда атрибуты присутствуют в нескольких местах, Log ingestion API применяет приоритет атрибутов, при этом сохраняя значения тела для возможности аудита. Атрибуты применяются в следующем порядке:",
    "* Query Parameters (highest precedence)": "* Параметры запроса (наивысший приоритет)",
    "* X-Dynatrace-Attr header": "* Заголовок X-Dynatrace-Attr",
    "* OpenTelemetry log request (lowest precedence; existing ingestion path)": "* Запрос логов OpenTelemetry (низший приоритет; существующий путь приёма)",
    # --- #### Override behavior ---
    "#### Override behavior": "#### Поведение при переопределении",
    "When attributes from query parameters or the header override log request attributes:": "Когда атрибуты из параметров запроса или заголовка переопределяют атрибуты запроса логов:",
    "* The final attribute value is set according to the attribute source precedence rules.": "* Конечное значение атрибута устанавливается согласно правилам приоритета источников атрибутов.",
    "* The values already present in the log request are preserved and mirrored under `overwrittenN.<attribute_key>`.": "* Значения, уже присутствующие в запросе логов, сохраняются и отражаются в `overwrittenN.<attribute_key>`.",
    # L205: mojibaked ellipsis \xe2\x80\xa6 inside prose. norm() does NOT convert this.
    # The line has 2-space indent; engine strips before lookup, re-applies after.
    "Where N is an incrementing integer (1, 2, "
    + _ELL
    + ") depending on how many log request-originating values had to be preserved. This ensures uniqueness, even when multiple conflicts occur.": "Где N: нарастающее целое число (1, 2, ...) в зависимости от того, сколько значений из запроса логов потребовалось сохранить. Это гарантирует уникальность даже при нескольких конфликтах.",
    "* Only values originating from the log request are preserved under the `overwrittenN.*` keys. Attributes overridden by higher-precedence sources do not generate overwritten copies.": "* Под ключами `overwrittenN.*` сохраняются только значения, исходящие из запроса логов. Атрибуты, переопределённые источниками с более высоким приоритетом, не создают перезаписанных копий.",
    # --- #### Example (override) ---
    "| Request | Resulting output |": "| Запрос | Результирующий вывод |",
    # --- ### Billing behavior ---
    "### Billing behavior": "### Поведение при тарификации",
    "Attributes provided through query parameters or headers are included in billing calculations.": "Атрибуты, переданные через параметры запроса или заголовки, включаются в расчёты тарификации.",
    "For multi-value attributes, the attribute key contributes to billing only once, regardless of how many values are present.": "Для атрибутов с несколькими значениями ключ атрибута учитывается в тарификации только один раз, независимо от числа присутствующих значений.",
    # --- ## Related topics ---
    "## Related topics": "## Связанные темы",
    '* [OpenTelemetry logs ingest API](/managed/dynatrace-api/environment-api/opentelemetry/post-logs "%s")'
    % TT_POSTLOGS: '* [API приёма логов OpenTelemetry](/managed/dynatrace-api/environment-api/opentelemetry/post-logs "%s")'
    % RU_POSTLOGS,
    '| ```  body: "Hello world!"  Resource:  - "any-attr-type-3": {"3" = "c"}  Scope:  - "any-attr-type-2" : {"2" = "b"}  Attributes:  - "any-attr-type-1" : {"1" = "a"}  - "any-attr-type-4" :  [ "val1", 10, -123.456, false, 0x01020304 ] ``` | ```  â\x80\x9ccontentâ\x80\x9d: "Hello world!"  "any-attr-type-1.1": "a"  "any-attr-type-2.2": "b"  "any-attr-type-3.3": "c"  "any-attr-type-4":  ["val1", 10, -123.456, false, "AQIDBA=="] ``` |': '| ```  body: "Hello world!"  Resource:  - "any-attr-type-3": {"3" = "c"}  Scope:  - "any-attr-type-2" : {"2" = "b"}  Attributes:  - "any-attr-type-1" : {"1" = "a"}  - "any-attr-type-4" :  [ "val1", 10, -123.456, false, 0x01020304 ] ``` | ```  "content": "Hello world!"  "any-attr-type-1.1": "a"  "any-attr-type-2.2": "b"  "any-attr-type-3.3": "c"  "any-attr-type-4":  ["val1", 10, -123.456, false, "AQIDBA=="] ``` |',
    **S,
}

# Lines kept verbatim (EN): table separator rows and table data rows containing
# inline code examples that must not be translated.
PASS = {
    # table separators
    "| --- | --- |",
    # table data rows with inline code (L111, L123, L131, L163, L212)
    '| ```  Body:  {  "content" = "Hello World!",  "my-body-attr-1": "abc",  "my-body-nested-1": {  "subkey": "val"  },  "@timestamp": "2025-06-01 13:01:02.123",  "loglevel": "INFO"  }  Attributes:  - "any-attr-type-1" : "my-attr" ``` | ```  "content": "Hello world!"  "timestamp": "2025-06-01 13:01:02.123"  "loglevel": "INFO"    "any-attr-type-1": "my-attr"  "my-body-attr-1": "abc"  "my-body-nested-1.subkey": "val" ``` |',
    '| ```  Body:  [ "string-val", true, 12, 12.34, 0x6279746573 ] ``` | ```  "content": "[\\"string-val\\",true,12,12.34,\\"Ynl0ZXM=\\"]"  ... ``` |',
    '| ```  otlphttp:  logs_endpoint: /api/v2/otlp/v1/logs?env=prod&env=blue&team=payments ```  ```  Body: "Hello World!" ``` | ```  {  "content": "Hello World!",  "env": ["prod", "blue"],  "team": "payments"  } ``` |',
    '| ```  otlphttp:  logs_endpoint: /api/v2/otlp/v1/logs?team=frontend ```  Log Request:  ```  Body: "Hello World!"  Attributes:  - "team": "backend" ``` | ```  {  "content": "Hello World!",  "team": "frontend",  "overwritten1.team": "backend"  } ``` |',
}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
