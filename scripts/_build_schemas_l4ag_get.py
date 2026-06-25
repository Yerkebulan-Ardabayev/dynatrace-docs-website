# -*- coding: utf-8 -*-
"""L4-AG.0 builder: schemas/get-all.md + schemas/get-schema.md (2 files).
These two are the GET-endpoint twins of L4-AE objects/get-X.md (NOT the 307
builtin-* schema-tables). Class includes `## Response` + `### Response codes`
+ `### Response body objects` + `#### The X object` + fenced JSON code-block
(`### Response body JSON models`), so the structural template is L4-AE
objects/get-objects.md, NOT L4-AF schemas-table.

ACTIVE Settings 2.0 API (no deprecated banner). title/source/scraped +
BOTH `# Settings API - GET ...` H1 + `* Reference` + `* Published <date>`
EN-verbatim. URLs verbatim. Code-blocks (JSON models) verbatim. Line-parity
EXACT EN==RU.

anchor = shipped L4-AE settings/objects/get-objects.md (same subsection, same
endpoint class, same response/JSON structure, same auth 2-absatz split).
"""

import os, io

EN = "docs/managed/dynatrace-api/environment-api/settings"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings"

FILES = ["schemas/get-all.md", "schemas/get-schema.md"]

# ----------------------------------------------------------------------------
# (1) Structural exact-string canon (whole-line / newline-anchored where safe).
#     Anchors come from shipped L4-AE objects/get-objects.md.
# ----------------------------------------------------------------------------
STRUCT = [
    # Section headings
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    # Lead absatz (single line) per file, plus the shared payload sentence
    (
        "Lists all settings schemas available in your environment.",
        "Возвращает список всех settings schemas, доступных в вашем окружении.",
    ),
    (
        "Gets parameters of the specified settings schema.",
        "Возвращает параметры указанной settings schema.",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает данные в формате `application/json`.",
    ),
    # Auth-paragraph 2-absatz split (shipped L4-AE objects/get-objects canon)
    (
        "To execute this request, you need an access token with `settings.read` scope.",
        "Для выполнения запроса необходим access token со scope `settings.read`.",
    ),
    (
        "To learn how to obtain and use it, see [Tokens and authentication]"
        "(/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "О том, как получить и использовать токен, см. [Tokens and authentication]"
        "(/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    # Table headers (separator `| --- | --- | --- |` is identical EN/RU)
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    (
        "| Code | Type | Description |",
        "| Код | Тип | Описание |",
    ),
    (
        "| Element | Type | Description |",
        "| Элемент | Тип | Описание |",
    ),
]

# ----------------------------------------------------------------------------
# (2) Response-code description cells (3-col Code/Type/Description rows).
#     The 200-row description is endpoint-specific (e.g. "Success. Available
#     objects are returned." -> "Успех. ..."), others reuse L4-AE canon.
# ----------------------------------------------------------------------------
RESPONSE_CODE_DESC = {
    "Success": "Успех",
    "Failed. Forbidden.": "Сбой. Доступ запрещён.",
    "Failed. The specified schema doesn't exist.": "Сбой. Указанная schema не существует.",
    "Client side error.": "Ошибка на стороне клиента.",
    "Server side error.": "Ошибка на стороне сервера.",
}

# ----------------------------------------------------------------------------
# (3) Parameter-row descriptions (5-col Parameter/Type/Desc/In/Required).
#     Only 3 unique descriptions across both files.
# ----------------------------------------------------------------------------
PARAM_DESC = {
    "The ID of the required schema.": "ID требуемой schema.",
    "The version of the required schema.  If not set, the most recent version is returned.": (
        "Версия требуемой schema.  Если не задано, возвращается самая последняя версия."
    ),
    (
        "A list of fields to be included to the response. The provided set of fields "
        "replaces the default set.  Specify the required top-level fields, separated "
        "by commas (for example, `schemaId,displayName`).  Supported fields: `schemaId`, "
        "`displayName`, `maturity`, `latestSchemaVersion`, `multiObject`, `ordered`, "
        "`ownerBasedAccessControl`."
    ): (
        "Список полей, включаемых в ответ. Предоставленный набор полей заменяет набор "
        "по умолчанию.  Укажите нужные поля верхнего уровня, разделённые запятыми "
        "(например, `schemaId,displayName`).  Поддерживаемые поля: `schemaId`, "
        "`displayName`, `maturity`, `latestSchemaVersion`, `multiObject`, `ordered`, "
        "`ownerBasedAccessControl`."
    ),
}

# ----------------------------------------------------------------------------
# (4) Element-row descriptions (3-col Element/Type/Desc). Comprehensive map
#     covering every unique description across get-schema.md + get-all.md.
#     Empty-cell ("-") passes through verbatim. EN-locked vocab inside RU
#     follows shipped L4-AE: settings object/schema/scope/property EN per
#     parent same-subsection L4T#1.
# ----------------------------------------------------------------------------
DESC = {
    # SchemaList / SchemaStub (get-all.md)
    "A list of settings schemas.": "Список settings schemas.",
    "The number of schemas in the list.": "Количество schemas в списке.",
    "The name of the schema.": "Имя schema.",
    "The most recent version of the schema.": "Самая последняя версия schema.",
    (
        "The maturity of the schema. Possible values:  "
        "* PREVIEW: Preview features are not generally available, but might be available "
        "in specific environments as part of early-access programs. These are the most "
        "likely to change in incompatible ways. "
        '* EARLY\\_ADOPTER: Features marked "early adopter" are available in all '
        'environments, but are not mature enough to warrant the "general availability" '
        "designation. We don't expect incompatible changes for these, but please be "
        "aware, that these are not fully stable yet and incompatible changes may be "
        "necessary in rare cases. "
        '* GENERAL\\_AVAILABILITY: Features marked "general availability" are the most '
        "stable. While the schemas will still evolve over time, care will be taken to "
        "only do so in a backward-compatible manner.  "
        "In any case, automations should make use of the `schemaVersion` field when "
        "writing settings objects. The element can hold these values "
        "* `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW`"
    ): (
        "Зрелость schema. Возможные значения:  "
        "* PREVIEW: функции preview, как правило, недоступны массово, но могут быть "
        "доступны в отдельных окружениях в рамках программ раннего доступа. У них "
        "наиболее высокая вероятность несовместимых изменений. "
        '* EARLY\\_ADOPTER: функции с пометкой "early adopter" доступны во всех '
        'окружениях, но недостаточно зрелы для обозначения "general availability". '
        "Несовместимых изменений для них не ожидается, но учитывайте, что они пока "
        "не полностью стабильны и в редких случаях могут потребоваться несовместимые "
        "изменения. "
        '* GENERAL\\_AVAILABILITY: функции с пометкой "general availability" наиболее '
        "стабильны. Schemas со временем продолжают развиваться, но это делается с "
        "сохранением обратной совместимости.  "
        "В любом случае автоматизации должны использовать поле `schemaVersion` при "
        "записи settings objects. Возможные значения: "
        "* `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW`"
    ),
    "Multi-object flag. `True` if the schema is a multi-object schema": (
        "Флаг multi-object. `True`, если schema является multi-object."
    ),
    "Ordered flag. `True` if the schema is an ordered multi-object schema.": (
        "Флаг ordered. `True`, если schema является упорядоченной multi-object schema."
    ),
    "Owner based access control flag. `True` if the schema has owner based access control enabled.": (
        "Флаг owner based access control. `True`, если у schema включён owner based access control."
    ),
    "The ID of the schema.": "ID schema.",
    # SchemaDefinitionRestDto (get-schema.md)
    "A list of scopes where the schema can be used.": "Список scopes, в которых может использоваться schema.",
    "A list of constrains limiting the values to be accepted by the schema.": (
        "Список constraints, ограничивающих значения, принимаемые schema."
    ),
    "Constraints limiting the values to be deleted.": "Constraints, ограничивающие удаляемые значения.",
    "A short description of the schema.": "Краткое описание schema.",
    "The display name of the schema.": "Отображаемое имя schema.",
    "An extended description of the schema and/or links to documentation.": (
        "Расширенное описание schema и/или ссылки на документацию."
    ),
    "The version of the data format.": "Версия формата данных.",
    "A list of definitions of enum properties.": "Список определений enum-свойств.",
    "Name of the key property in this schema.": "Имя ключевого свойства в этой schema.",
    (
        "The maximum amount of objects per scope.  Only applicable when **multiObject** "
        "is set to `true`."
    ): (
        "Максимальное количество объектов на scope.  Применимо, только если "
        "**multiObject** установлен в `true`."
    ),
    "Metadata of the setting.": "Метаданные настройки.",
    (
        "Multiple (`true`) objects per scope are permitted or a single (`false`) object "
        "per scope is permitted."
    ): (
        "Разрешено несколько объектов на scope (`true`) или только один объект на "
        "scope (`false`)."
    ),
    (
        "If `true` the order of objects has semantic significance.  Only applicable "
        "when **multiObject** is set to `true`."
    ): (
        "Если `true`, порядок объектов имеет смысловое значение.  Применимо, только "
        "если **multiObject** установлен в `true`."
    ),
    "A list of schema's properties.": "Список свойств schema.",
    (
        "Constraints limiting the values as a whole to be accepted in this configuration "
        "element."
    ): (
        "Constraints, ограничивающие значения, принимаемые в данном элементе "
        "конфигурации, как единое целое."
    ),
    "Names of the groups, which the schema belongs to.": "Имена групп, к которым принадлежит schema.",
    "Table column definitions for use in the ui.": "Определения колонок таблицы для использования в UI.",
    (
        "A list of definitions of types.  A type is a complex property that contains "
        "its own set of subproperties."
    ): (
        "Список определений типов.  Тип, это сложное свойство, содержащее собственный "
        "набор под-свойств."
    ),
    "Customization for UI elements": "Кастомизация для UI-элементов",
    "The version of the schema.": "Версия schema.",
    # ComplexConstraint / Constraint / SchemaConstraintRestDto / DeletionConstraint
    ("Defines if modification of any property triggers secret resubmission check."): (
        "Определяет, вызывает ли модификация любого свойства повторную проверку секретов."
    ),
    "A custom message for invalid values.": "Пользовательское сообщение для невалидных значений.",
    "The ID of a custom validator.": "ID пользовательского валидатора.",
    "The maximum number of properties that can be set.": "Максимальное количество свойств, которое можно задать.",
    "The minimum number of properties that must be set.": "Минимальное количество свойств, которое должно быть задано.",
    "A list of properties (defined by IDs) that are used to check the constraint.": (
        "Список свойств (определённых по ID), которые используются для проверки constraint."
    ),
    "Whether to skip validation on a change made from the UI.": (
        "Пропускать ли валидацию при изменении из UI."
    ),
    "The maximum time in seconds the custom validator is allowed to run.": (
        "Максимальное время в секундах, отведённое для работы пользовательского валидатора."
    ),
    (
        "The type of the constraint. The element can hold these values "
        "* `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` "
        "* `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` "
        "* `SECRET_RESUBMISSION` * `UNKNOWN`"
    ): (
        "Тип constraint. Возможные значения: "
        "* `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` "
        "* `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` "
        "* `SECRET_RESUBMISSION` * `UNKNOWN`"
    ),
    "The IDs of schemas that should be checked for references to this schema.": (
        "ID schemas, которые нужно проверить на ссылки на данную schema."
    ),
    (
        "The type of the deletion constraint. The element can hold these values "
        "* `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN`"
    ): (
        "Тип deletion-constraint. Возможные значения: "
        "* `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN`"
    ),
    "Whether to disallow usage of dangerous regexes": (
        "Запрещать ли использование опасных regex-выражений"
    ),
    "The maximum allowed length of string values.": "Максимально допустимая длина строковых значений.",
    "The maximum allowed value.": "Максимально допустимое значение.",
    "The minimum required length of string values.": "Минимально требуемая длина строковых значений.",
    "The minimum allowed value.": "Минимально допустимое значение.",
    "The regular expression pattern for valid string values.": (
        "Шаблон регулярного выражения для валидных строковых значений."
    ),
    (
        "The type of the constraint. The element can hold these values "
        "* `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` "
        "* `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` "
        "* `UNIQUE` * `UNKNOWN`"
    ): (
        "Тип constraint. Возможные значения: "
        "* `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` "
        "* `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` "
        "* `UNIQUE` * `UNKNOWN`"
    ),
    "A list of properties for which the combination of values must be unique.": (
        "Список свойств, для которых комбинация значений должна быть уникальной."
    ),
    # SchemaConstraintRestDto
    "The maximum allowed size in bytes for the sum over all persisted values for the schema": (
        "Максимально допустимый размер в байтах для суммы всех сохранённых значений schema"
    ),
    (
        "Whether to flatten collection properties when checking for uniqueness, so "
        "only disjoint collections are considered unique"
    ): (
        "Раскрывать ли коллекционные свойства при проверке уникальности, чтобы "
        "только непересекающиеся коллекции считались уникальными"
    ),
    (
        "The type of the schema constraint. The element can hold these values "
        "* `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` "
        "* `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN`"
    ): (
        "Тип schema-constraint. Возможные значения: "
        "* `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` "
        "* `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN`"
    ),
    "The list of properties for which the combination of values needs to be unique": (
        "Список свойств, для которых комбинация значений должна быть уникальной"
    ),
    # EnumType / EnumValue / AnyValue
    "A short description of the property.": "Краткое описание свойства.",
    "The display name of the property.": "Отображаемое имя свойства.",
    "An extended description and/or links to documentation.": (
        "Расширенное описание и/или ссылки на документацию."
    ),
    "An existing Java enum class that holds the allowed values of the enum.": (
        "Существующий Java enum-класс, содержащий допустимые значения enum."
    ),
    "A list of allowed values of the enum.": "Список допустимых значений enum.",
    "The type of the property. The element can hold these values * `enum`": (
        "Тип свойства. Возможные значения: * `enum`"
    ),
    "A short description of the value.": "Краткое описание значения.",
    "The display name of the value.": "Отображаемое имя значения.",
    "The name of the value in an existing Java enum class.": (
        "Имя значения в существующем Java enum-классе."
    ),
    "The icon of the value.": "Иконка значения.",
    "The allowed value of the enum.": "Допустимое значение enum.",
    # PropertyDefinition / Item
    "A list of constraints limiting the values to be accepted.": (
        "Список constraints, ограничивающих принимаемые значения."
    ),
    "Configuration of a datasource for a property.": "Конфигурация источника данных для свойства.",
    (
        "The default value to be used when no value is provided.  If a non-singleton "
        "has the value of `null`, it means an empty collection."
    ): (
        "Значение по умолчанию, используемое, если значение не задано.  Если не-singleton "
        "имеет значение `null`, это означает пустую коллекцию."
    ),
    "Defines if value is allowed to be modified when secret properties are not": (
        "Определяет, разрешено ли изменение значения, когда секретные свойства не заданы"
    ),
    "An item of a collection property.": "Элемент коллекционного свойства.",
    (
        "The maximum number of **objects** in a collection property.  Has the value of "
        "`1` for singletons."
    ): (
        "Максимальное количество **объектов** в коллекционном свойстве.  Для singleton "
        "равно `1`."
    ),
    "Metadata of the property.": "Метаданные свойства.",
    "Pattern with references to properties to create a new value.": (
        "Шаблон со ссылками на свойства для создания нового значения."
    ),
    "The minimum number of **objects** in a collection property.": (
        "Минимальное количество **объектов** в коллекционном свойстве."
    ),
    (
        "Modification policy of the property. The element can hold these values "
        "* `ALWAYS` * `DEFAULT` * `NEVER`"
    ): (
        "Политика модификации свойства. Возможные значения: "
        "* `ALWAYS` * `DEFAULT` * `NEVER`"
    ),
    "The value can (`true`) or can't (`false`) be `null`.": (
        "Значение может быть `null` (`true`) или не может быть `null` (`false`)."
    ),
    "A precondition for visibility of a property.": "Предусловие видимости свойства.",
    "The type referenced by the property value": "Тип, на который ссылается значение свойства",
    "The subtype of the property's value.": "Подтип значения свойства.",
    "The type of the property's value.": "Тип значения свойства.",
    "A short description of the item.": "Краткое описание элемента.",
    "The display name of the item.": "Отображаемое имя элемента.",
    "Metadata of the items.": "Метаданные элементов.",
    "The type referenced by the item's value.": "Тип, на который ссылается значение элемента.",
    "The subtype of the item's value.": "Подтип значения элемента.",
    "The type of the item's value.": "Тип значения элемента.",
    # DatasourceDefinition
    "The properties to filter the datasource options on.": (
        "Свойства, по которым фильтруются варианты источника данных."
    ),
    "Whether this datasource expects full setting payload as the context.": (
        "Ожидает ли этот источник данных полный payload настройки в качестве контекста."
    ),
    "The identifier of a custom data source of the property's value.": (
        "Идентификатор пользовательского источника данных значения свойства."
    ),
    (
        "When to reset datasource value in the UI on filter change. The element "
        "can hold these values * `ALWAYS` * `INVALID_ONLY` * `NEVER`"
    ): (
        "Когда сбрасывать значение источника данных в UI при изменении фильтра. "
        "Возможные значения: * `ALWAYS` * `INVALID_ONLY` * `NEVER`"
    ),
    (
        "If true, the datasource should use the api to filter the results instead "
        "of client-side filtering."
    ): (
        "Если true, источник данных должен использовать api для фильтрации "
        "результатов вместо клиентской фильтрации."
    ),
    "Whether to validate input to only allow values returned by the datasource.": (
        "Валидировать ли ввод, чтобы разрешать только значения, возвращаемые источником данных."
    ),
    # UiCustomization family
    "UI customization options for defining custom callbacks": (
        "Параметры UI-кастомизации для определения пользовательских callback-ов"
    ),
    "UI customization for expandable section": "UI-кастомизация для разворачиваемой секции",
    "Customization for UI tables": "Кастомизация для UI-таблиц",
    "UI customization for tabs": "UI-кастомизация для вкладок",
    "UI customization for defining buttons that call functions when pressed": (
        "UI-кастомизация для определения кнопок, вызывающих функции при нажатии"
    ),
    "The description to be shown in a tooltip when hovering over the button": (
        "Описание, отображаемое в подсказке при наведении на кнопку"
    ),
    "The label of the button": "Текст кнопки",
    "The identifier of the function to be called when the button is pressed": (
        "Идентификатор функции, вызываемой при нажатии кнопки"
    ),
    (
        "The position where the button should be shown in the UI The element can "
        "hold these values * `FIRST` * `LAST`"
    ): (
        "Позиция, в которой кнопка должна отображаться в UI. Возможные значения: "
        "* `FIRST` * `LAST`"
    ),
    "The display name": "Отображаемое имя",
    "Defines if the item should be expanded by default": (
        "Определяет, должен ли элемент быть развёрнут по умолчанию"
    ),
    "A list of sections": "Список секций",
    "The description": "Описание",
    "Defines if the section should be expanded by default": (
        "Определяет, должна ли секция быть развёрнута по умолчанию"
    ),
    "A list of properties": "Список свойств",
    "A list of columns for the UI table": "Список колонок для UI-таблицы",
    "UI customization for empty state in a table": "UI-кастомизация для пустого состояния таблицы",
    "The ui specific builtin column-implementation for this column.": (
        "UI-специфичная встроенная реализация колонки для этой колонки."
    ),
    (
        "The referenced column from the 'tableColumns' property of the schema for "
        "this column."
    ): ("Колонка из свойства 'tableColumns' schema, на которую ссылается эта колонка."),
    "The display name for this column.": "Отображаемое имя для этой колонки.",
    (
        "The id for this column used for filtering. Required for conflicting or "
        "pathed columns - otherwise the ref is used."
    ): (
        "ID этой колонки, используемый для фильтрации. Обязателен для конфликтующих "
        "или path-колонок, иначе используется ref."
    ),
    "The possible items of this column.": "Возможные элементы этой колонки.",
    "The referenced property for this column.": "Свойство, на которое ссылается эта колонка.",
    "The ui specific type for this column.": "UI-специфичный тип для этой колонки.",
    "The width this column should take up on the table.": (
        "Ширина, которую должна занимать эта колонка в таблице."
    ),
    "The display name of this item.": "Отображаемое имя этого элемента.",
    "The icon of this item.": "Иконка этого элемента.",
    "The value of this item.": "Значение этого элемента.",
    "The text to be shown in the empty state": "Текст для отображения в пустом состоянии",
    "A list of groups": "Список групп",
    # Precondition
    (
        "The expected value of the property.  Only applicable to properties of the "
        "`EQUALS` type."
    ): ("Ожидаемое значение свойства.  Применимо только для свойств типа `EQUALS`."),
    (
        "A list of valid values of the property.  Only applicable to properties of "
        "the `IN` type."
    ): ("Список валидных значений свойства.  Применимо только для свойств типа `IN`."),
    (
        "The Regular expression which is matched against the property.  Only "
        "applicable to properties of the `REGEX_MATCH` type."
    ): (
        "Регулярное выражение, с которым сопоставляется свойство.  Применимо "
        "только для свойств типа `REGEX_MATCH`."
    ),
    (
        "A list of child preconditions to be evaluated.  Only applicable to "
        "properties of the `AND` and `OR` types."
    ): (
        "Список дочерних предусловий для оценки.  Применимо только для свойств "
        "типов `AND` и `OR`."
    ),
    "The property to be evaluated.": "Оцениваемое свойство.",
    (
        "The type of the precondition. The element can hold these values "
        "* `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH`"
    ): (
        "Тип предусловия. Возможные значения: "
        "* `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH`"
    ),
    # TableColumn / SchemaType
    "The definition of a table column to be used in the ui.": (
        "Определение колонки таблицы для использования в UI."
    ),
    "Pattern with references to properties to create a single value for the column.": (
        "Шаблон со ссылками на свойства для создания единого значения колонки."
    ),
    "Definition of properties that can be persisted.": "Определение свойств, которые можно сохранять.",
    (
        'The pattern for the summary search(for example, "Alert after *X* minutes.") '
        "of the configuration in the UI."
    ): (
        'Шаблон для поиска по сводке (например, "Alert after *X* minutes.") '
        "конфигурации в UI."
    ),
    (
        'The pattern for the summary (for example, "Alert after *X* minutes.") '
        "of the configuration in the UI."
    ): ('Шаблон для сводки (например, "Alert after *X* minutes.") конфигурации в UI.'),
    "Type of the reference type. The element can hold these values * `object`": (
        "Тип reference-типа. Возможные значения: * `object`"
    ),
    "The version of the type.": "Версия типа.",
    "A short description of the version.": "Краткое описание версии.",
    # Error / ConstraintViolation (shared with L4-AE objects/ canon)
    "The HTTP status code": "HTTP-код статуса",
    "A list of constraint violations": "Список нарушений constraints",
    "The error message": "Сообщение об ошибке",
    (
        "-The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` "
        "* `QUERY`"
    ): ("-Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY`"),
}

# ----------------------------------------------------------------------------
# (5) Object-block leading-line descriptions (the single-line absatz that
#     appears between `#### The X object` and its table). These are NOT inside
#     table cells, so they are matched as whole lines via `\n<EN>\n` anchor.
# ----------------------------------------------------------------------------
OBJECT_LEAD = {
    "The list of available settings schemas.": "Список доступных settings schemas.",
    "The short representation of the settings schema.": "Краткое представление settings schema.",
    "A schema representing an arbitrary value type.": "Schema, представляющая произвольный тип значения.",
    "Configuration of a property in a settings schema.": "Конфигурация свойства в settings schema.",
    "A constraint on the values accepted for a complex settings property.": (
        "Constraint на значения, принимаемые для сложного settings-свойства."
    ),
    "A constraint on the values that are going to be deleted.": (
        "Constraint на значения, которые будут удалены."
    ),
    "Definition of an enum property.": "Определение enum-свойства.",
    "An allowed value for an enum property.": "Допустимое значение для enum-свойства.",
    "A constraint on the values accepted for a settings property.": (
        "Constraint на значения, принимаемые для settings-свойства."
    ),
    "Configuration of a datasource for a property.": "Конфигурация источника данных для свойства.",
    "An item of a collection property.": "Элемент коллекционного свойства.",
    "Customization for UI elements": "Кастомизация для UI-элементов",
    "UI customization options for defining custom callbacks": (
        "Параметры UI-кастомизации для определения пользовательских callback-ов"
    ),
    "UI customization for defining a button that calls a function when pressed": (
        "UI-кастомизация для определения кнопки, вызывающей функцию при нажатии"
    ),
    "UI customization for expandable section": "UI-кастомизация для разворачиваемой секции",
    "Expandable section customization for UI": "Кастомизация разворачиваемой секции для UI",
    "Customization for UI tables": "Кастомизация для UI-таблиц",
    "Customization for UI table columns": "Кастомизация для колонок UI-таблиц",
    "Customization for UI table column items": "Кастомизация для элементов колонок UI-таблиц",
    "UI customization for empty state in a table": "UI-кастомизация для пустого состояния таблицы",
    "UI customization for tabs": "UI-кастомизация для вкладок",
    "Tab group customization for UI": "Кастомизация группы вкладок для UI",
    "A precondition for visibility of a property.": "Предусловие видимости свойства.",
    "The definition of a table column to be used in the ui.": (
        "Определение колонки таблицы для использования в UI."
    ),
    "A list of definitions of types.": "Список определений типов.",
    "A type is a complex property that contains its own set of subproperties.": (
        "Тип, это сложное свойство, содержащее собственный набор под-свойств."
    ),
    "A list of constraint violations": "Список нарушений constraints",
}


def _normalize(t):
    t = t.replace("\r\n", "\n")
    t = t.replace(chr(0xFEFF), "")
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")
    return t


def _object_heading(line):
    """`#### The `X` object` -> `#### Объект `X``. Keep hash-level and code."""
    s = line.lstrip("#")
    hashes = line[: len(line) - len(s)]
    s = s.strip()
    if s.startswith("The `") and s.endswith("` object"):
        code = s[len("The ") : -len(" object")]
        return hashes + " Объект " + code
    return None


def _element_row(line):
    """`| <name> | <type> | <desc> |` -> translate <desc> via DESC; name/type
    EN-verbatim. Header `| Element | Type | Description |` and separator
    `| --- | --- | --- |` are caught upstream by STRUCT and left to passthrough.
    """
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 3:
        return None
    c0, c1, c2 = cells
    # leave separator + header rows alone (they are translated by STRUCT)
    if c0 == "---" or c0 == "Element" or c0 == "Код" or c0 == "Элемент":
        return None
    new_desc = DESC.get(c2, c2)
    return "| " + c0 + " | " + c1 + " | " + new_desc + " |"


def _response_code_row(line):
    """`| **CODE** | [Type](...) | <desc> |` -> translate <desc>. Code+type
    cells EN-verbatim. Only the description cell is replaced when known."""
    if not line.startswith("| **") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 3:
        return None
    c0, c1, c2 = cells
    if not c0.startswith("**") or not c0.endswith("**"):
        return None
    new_desc = RESPONSE_CODE_DESC.get(c2, c2)
    return "| " + c0 + " | " + c1 + " | " + new_desc + " |"


def _parameter_row(line):
    """5-col `| <name> | <type> | <desc> | <in> | <req> |` -> translate <desc>
    via PARAM_DESC. Name/type/in/req EN-verbatim."""
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 5:
        return None
    c0, c1, c2, c3, c4 = cells
    if c0 == "---" or c0 == "Parameter" or c0 == "Параметр":
        return None
    new_desc = PARAM_DESC.get(c2, c2)
    return "| " + c0 + " | " + c1 + " | " + new_desc + " | " + c3 + " | " + c4 + " |"


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    # whole-line OBJECT_LEAD applied first
    for en, ru in OBJECT_LEAD.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    # structural canon
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    # per-line transforms with code-block passthrough
    out = []
    in_code = False
    for line in t.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        nl = (
            _object_heading(line)
            or _response_code_row(line)
            or _parameter_row(line)
            or _element_row(line)
        )
        out.append(nl if nl is not None else line)
    t = "\n".join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return src, dst


if __name__ == "__main__":
    bad = 0
    for rel in FILES:
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
        print("%-32s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print("OK" if bad == 0 else "BAD: %d files" % bad)
