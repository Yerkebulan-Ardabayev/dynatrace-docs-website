---
title: Extensions 2.0 API - GET schema extension
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema
scraped: 2026-05-12T11:56:30.601236
---

# Extensions 2.0 API - GET schema extension

# Extensions 2.0 API - GET schema extension

* Справочник
* Опубликовано 22 января 2021 г.

Возвращает schema указанной версии Extensions 2.0 extension.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/{extensionVersion}/schema` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/{extensionVersion}/schema` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensions.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| extensionVersion | string | Версия требуемого extension 2.0 | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SchemaDefinitionRestDto](#openapi-definition-SchemaDefinitionRestDto) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SchemaDefinitionRestDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| allowedScopes | string[] | Список scope, где может использоваться schema. |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | Список ограничений, ограничивающих значения, принимаемые schema. |
| deletionConstraints | [DeletionConstraint[]](#openapi-definition-DeletionConstraint) | Ограничения, ограничивающие удаляемые значения. |
| description | string | Краткое описание schema. |
| displayName | string | Отображаемое имя schema. |
| documentation | string | Расширенное описание schema и/или ссылки на документацию. |
| dynatrace | string | Версия формата данных. |
| enums | object | Список определений enum-свойств. |
| keyProperty | string | Имя ключевого свойства в этой schema. |
| maturity | string | Зрелость schema. Возможные значения:  * PREVIEW: функции в режиме preview обычно недоступны, но могут быть доступны в отдельных окружениях в рамках программ раннего доступа. Они с наибольшей вероятностью изменятся несовместимым образом. * EARLY\_ADOPTER: функции, помеченные "early adopter", доступны во всех окружениях, но недостаточно зрелы, чтобы получить обозначение "general availability". Несовместимых изменений для них мы не ожидаем, но учтите, что они ещё не полностью стабильны и в редких случаях несовместимые изменения могут оказаться необходимыми. * GENERAL\_AVAILABILITY: функции, помеченные "general availability", наиболее стабильны. Хотя schemas со временем всё равно будут развиваться, изменения будут вноситься только обратно совместимым образом.  В любом случае автоматизация должна использовать поле `schemaVersion` при записи объектов настроек. Элемент может принимать значения * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| maxObjects | integer | Максимальное количество объектов на scope.  Применимо только когда **multiObject** установлено в `true`. |
| metadata | object | Метаданные настройки. |
| multiObject | boolean | Разрешено несколько (`true`) объектов на scope или разрешён один (`false`) объект на scope. |
| ordered | boolean | Если `true`, порядок объектов имеет семантическое значение.  Применимо только когда **multiObject** установлено в `true`. |
| properties | object | Список свойств schema. |
| schemaConstraints | [SchemaConstraintRestDto[]](#openapi-definition-SchemaConstraintRestDto) | Ограничения, ограничивающие значения в целом, принимаемые в этом элементе конфигурации. |
| schemaGroups | string[] | Имена групп, к которым принадлежит schema. |
| schemaId | string | ID schema. |
| tableColumns | object | Определения столбцов таблицы для использования в интерфейсе. |
| types | object | Список определений типов.  Тип, это сложное свойство, содержащее собственный набор подсвойств. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Кастомизация элементов интерфейса |
| version | string | Версия schema. |

#### Объект `ComplexConstraint`

Ограничение на значения, принимаемые для сложного свойства настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| checkAllProperties | boolean | Определяет, запускает ли модификация любого свойства проверку повторной отправки секрета. |
| customMessage | string | Пользовательское сообщение для некорректных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| maximumPropertyCount | integer | Максимальное количество свойств, которое можно задать. |
| minimumPropertyCount | integer | Минимальное количество свойств, которое необходимо задать. |
| properties | string[] | Список свойств (заданных по ID), используемых для проверки ограничения. |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении из интерфейса. |
| timeout | integer | Максимальное время в секундах, в течение которого разрешено выполняться пользовательскому валидатору. |
| type | string | Тип ограничения. Элемент может принимать значения * `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` * `SECRET_RESUBMISSION` * `UNKNOWN` |

#### Объект `DeletionConstraint`

Ограничение на значения, которые будут удалены.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMessage | string | Пользовательское сообщение для некорректных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| schemaIds | string[] | ID schemas, которые следует проверять на ссылки на эту schema. |
| timeout | integer | Максимальное время в секундах, в течение которого разрешено выполняться пользовательскому валидатору. |
| type | string | Тип ограничения удаления. Элемент может принимать значения * `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN` |

#### Объект `EnumType`

Определение enum-свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| enumClass | string | Существующий Java enum-класс, содержащий допустимые значения enum. |
| items | [EnumValue[]](#openapi-definition-EnumValue) | Список допустимых значений enum. |
| type | string | Тип свойства. Элемент может принимать значения * `enum` |

#### Объект `EnumValue`

Допустимое значение для enum-свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание значения. |
| displayName | string | Отображаемое имя значения. |
| enumInstance | string | Имя значения в существующем Java enum-классе. |
| icon | string | Иконка значения. |
| value | string | Допустимое значение enum. |

#### Объект `AnyValue`

Schema, представляющая произвольный тип значения.

#### Объект `PropertyDefinition`

Конфигурация свойства в schema настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | Список ограничений, ограничивающих принимаемые значения. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Конфигурация источника данных для свойства. |
| default | string | Значение по умолчанию, используемое, когда значение не предоставлено.  Если у не-синглтона значение `null`, это означает пустую коллекцию. |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| forceSecretResubmission | boolean | Определяет, разрешено ли изменять значение, когда секретные свойства не заданы |
| items | [Item](#openapi-definition-Item) | Элемент свойства-коллекции. |
| maxObjects | integer | Максимальное количество **объектов** в свойстве-коллекции.  Имеет значение `1` для синглтонов. |
| metadata | object | Метаданные свойства. |
| migrationPattern | string | Шаблон со ссылками на свойства для создания нового значения. |
| minObjects | integer | Минимальное количество **объектов** в свойстве-коллекции. |
| modificationPolicy | string | Политика модификации свойства. Элемент может принимать значения * `ALWAYS` * `DEFAULT` * `NEVER` |
| nullable | boolean | Значение может (`true`) или не может (`false`) быть `null`. |
| precondition | [Precondition](#openapi-definition-Precondition) | Предусловие видимости свойства. |
| referencedType | string | Тип, на который ссылается значение свойства |
| subType | string | Подтип значения свойства. |
| type | string | Тип значения свойства. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Кастомизация элементов интерфейса |

#### Объект `Constraint`

Ограничение на значения, принимаемые для свойства настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMessage | string | Пользовательское сообщение для некорректных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| disallowDangerousRegex | boolean | Запрещать ли использование опасных регулярных выражений |
| maxLength | integer | Максимально допустимая длина строковых значений. |
| maximum | number | Максимально допустимое значение. |
| minLength | integer | Минимально требуемая длина строковых значений. |
| minimum | number | Минимально допустимое значение. |
| pattern | string | Шаблон регулярного выражения для корректных строковых значений. |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении из интерфейса. |
| timeout | integer | Максимальное время в секундах, в течение которого разрешено выполняться пользовательскому валидатору. |
| type | string | Тип ограничения. Элемент может принимать значения * `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` * `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | Список свойств, для которых комбинация значений должна быть уникальной. |

#### Объект `DatasourceDefinition`

Конфигурация источника данных для свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| filterProperties | string[] | Свойства, по которым фильтруются варианты источника данных. |
| fullContext | boolean | Ожидает ли этот источник данных полный payload настройки в качестве контекста. |
| identifier | string | Идентификатор пользовательского источника данных значения свойства. |
| resetValue | string | Когда сбрасывать значение источника данных в интерфейсе при изменении фильтра. Элемент может принимать значения * `ALWAYS` * `INVALID_ONLY` * `NEVER` |
| useApiSearch | boolean | Если true, источник данных должен использовать API для фильтрации результатов вместо фильтрации на стороне клиента. |
| validate | boolean | Валидировать ли ввод, чтобы разрешать только значения, возвращаемые источником данных. |

#### Объект `Item`

Элемент свойства-коллекции.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | Список ограничений, ограничивающих принимаемые значения. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Конфигурация источника данных для свойства. |
| description | string | Краткое описание элемента. |
| displayName | string | Отображаемое имя элемента. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| metadata | object | Метаданные элементов. |
| referencedType | string | Тип, на который ссылается значение элемента. |
| subType | string | Подтип значения элемента. |
| type | string | Тип значения элемента. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Кастомизация элементов интерфейса |

#### Объект `UiCustomization`

Кастомизация элементов интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| callback | [UiCallbackCustomization](#openapi-definition-UiCallbackCustomization) | Опции кастомизации интерфейса для определения пользовательских колбэков |
| expandable | [UiExpandableCustomization](#openapi-definition-UiExpandableCustomization) | Кастомизация интерфейса для разворачиваемой секции |
| table | [UiTableCustomization](#openapi-definition-UiTableCustomization) | Кастомизация для таблиц интерфейса |
| tabs | [UiTabsCustomization](#openapi-definition-UiTabsCustomization) | Кастомизация интерфейса для вкладок |

#### Объект `UiCallbackCustomization`

Опции кастомизации интерфейса для определения пользовательских колбэков

| Элемент | Тип | Описание |
| --- | --- | --- |
| buttons | [UiButtonCustomization[]](#openapi-definition-UiButtonCustomization) | Кастомизация интерфейса для определения кнопок, вызывающих функции при нажатии |

#### Объект `UiButtonCustomization`

Кастомизация интерфейса для определения кнопки, вызывающей функцию при нажатии

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание, показываемое в подсказке при наведении на кнопку |
| displayName | string | Подпись кнопки |
| identifier | string | Идентификатор функции, вызываемой при нажатии кнопки |
| insert | string | Позиция, где кнопка должна отображаться в интерфейсе Элемент может принимать значения * `FIRST` * `LAST` |

#### Объект `UiExpandableCustomization`

Кастомизация интерфейса для разворачиваемой секции

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя |
| expanded | boolean | Определяет, должен ли элемент быть развёрнут по умолчанию |
| sections | [UiExpandableSectionCustomization[]](#openapi-definition-UiExpandableSectionCustomization) | Список секций |

#### Объект `UiExpandableSectionCustomization`

Кастомизация разворачиваемой секции для интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание |
| displayName | string | Отображаемое имя |
| expanded | boolean | Определяет, должна ли секция быть развёрнута по умолчанию |
| properties | string[] | Список свойств |

#### Объект `UiTableCustomization`

Кастомизация для таблиц интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| columns | [UiTableColumnCustomization[]](#openapi-definition-UiTableColumnCustomization) | Список столбцов для таблицы интерфейса |
| emptyState | [UiEmptyStateCustomization](#openapi-definition-UiEmptyStateCustomization) | Кастомизация интерфейса для пустого состояния таблицы |

#### Объект `UiTableColumnCustomization`

Кастомизация для столбцов таблицы интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| builtinColumnRef | string | Специфичная для интерфейса встроенная реализация столбца для этого столбца. |
| columnRef | string | Столбец, на который ссылаются, из свойства 'tableColumns' schema для этого столбца. |
| displayName | string | Отображаемое имя для этого столбца. |
| id | string | ID для этого столбца, используемый для фильтрации. Требуется для конфликтующих столбцов или столбцов с путём, в остальных случаях используется ссылка. |
| items | [UiTableColumnItemCustomization[]](#openapi-definition-UiTableColumnItemCustomization) | Возможные элементы этого столбца. |
| propertyRef | string | Свойство, на которое ссылается этот столбец. |
| type | string | Специфичный для интерфейса тип для этого столбца. |
| width | string | Ширина, которую должен занимать этот столбец в таблице. |

#### Объект `UiTableColumnItemCustomization`

Кастомизация для элементов столбца таблицы интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя этого элемента. |
| icon | string | Иконка этого элемента. |
| value | string | Значение этого элемента. |

#### Объект `UiEmptyStateCustomization`

Кастомизация интерфейса для пустого состояния таблицы

| Элемент | Тип | Описание |
| --- | --- | --- |
| text | string | Текст, показываемый в пустом состоянии |

#### Объект `UiTabsCustomization`

Кастомизация интерфейса для вкладок

| Элемент | Тип | Описание |
| --- | --- | --- |
| groups | [UiTabGroupCustomization[]](#openapi-definition-UiTabGroupCustomization) | Список групп |

#### Объект `UiTabGroupCustomization`

Кастомизация группы вкладок для интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание |
| displayName | string | Отображаемое имя |
| properties | string[] | Список свойств |

#### Объект `Precondition`

Предусловие видимости свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| expectedValue | string | Ожидаемое значение свойства.  Применимо только к свойствам типа `EQUALS`. |
| expectedValues | - | Список допустимых значений свойства.  Применимо только к свойствам типа `IN`. |
| pattern | string | Регулярное выражение, которое сопоставляется со свойством.  Применимо только к свойствам типа `REGEX_MATCH`. |
| precondition | [Precondition](#openapi-definition-Precondition) | Предусловие видимости свойства. |
| preconditions | [Precondition[]](#openapi-definition-Precondition) | Список дочерних предусловий для вычисления.  Применимо только к свойствам типов `AND` и `OR`. |
| property | string | Свойство, которое вычисляется. |
| type | string | Тип предусловия. Элемент может принимать значения * `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH` |

#### Объект `SchemaConstraintRestDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| byteLimit | integer | Максимально допустимый размер в байтах для суммы по всем сохраняемым значениям schema |
| customMessage | string | Пользовательское сообщение для некорректных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| flattenCollections | boolean | Уплощать ли свойства-коллекции при проверке на уникальность, чтобы уникальными считались только непересекающиеся коллекции |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении из интерфейса. |
| type | string | Тип ограничения schema. Элемент может принимать значения * `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | Список свойств, для которых комбинация значений должна быть уникальной |

#### Объект `TableColumn`

Определение столбца таблицы для использования в интерфейсе.

| Элемент | Тип | Описание |
| --- | --- | --- |
| pattern | string | Шаблон со ссылками на свойства для создания единственного значения для столбца. |

#### Объект `SchemaType`

Список определений типов.

Тип, это сложное свойство, содержащее собственный набор подсвойств.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | Список ограничений, ограничивающих принимаемые значения. |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| properties | object | Определение свойств, которые можно сохранять. |
| searchPattern | string | Шаблон для поиска по сводке (например, "Alert after *X* minutes.") конфигурации в интерфейсе. |
| summaryPattern | string | Шаблон для сводки (например, "Alert after *X* minutes.") конфигурации в интерфейсе. |
| type | string | Тип ссылочного типа. Элемент может принимать значения * `object` |
| version | string | Версия типа. |
| versionInfo | string | Краткое описание версии. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"allowedScopes": [



"host",



"application"



],



"constraints": [



{



"checkAllProperties": false,



"customMessage": "string",



"customValidatorId": "my-min-max",



"maximumPropertyCount": 2,



"minimumPropertyCount": 1,



"properties": [



"string"



],



"skipAsyncValidation": false,



"timeout": 5,



"type": "CUSTOM_VALIDATOR_REF"



}



],



"deletionConstraints": [



{



"customMessage": "string",



"customValidatorId": "my-min-max",



"schemaIds": [



"my-schema-id"



],



"timeout": 5,



"type": "CUSTOM_VALIDATOR_REF"



}



],



"description": "Dynatrace disables monitoring of containers that do not run any applications",



"displayName": "Built-in container monitoring rules",



"documentation": "string",



"dynatrace": "1",



"enums": {},



"keyProperty": "keyProperty",



"maturity": "GENERAL_AVAILABILITY",



"maxObjects": 10,



"metadata": {},



"multiObject": true,



"ordered": true,



"properties": {},



"schemaConstraints": [



{



"byteLimit": 500000,



"customMessage": "string",



"customValidatorId": "my-min-max",



"flattenCollections": true,



"skipAsyncValidation": false,



"type": "BYTE_SIZE_LIMIT",



"uniqueProperties": [



"my-prop-1",



"my-prop-2"



]



}



],



"schemaGroups": [



"group:some.1",



"group:some.2"



],



"schemaId": "builtin:container.built-in-monitoring-rule",



"tableColumns": {},



"types": {},



"uiCustomization": {



"callback": {



"buttons": [



{



"description": "string",



"displayName": "string",



"identifier": "string",



"insert": "FIRST"



}



]



},



"expandable": {



"displayName": "string",



"expanded": true,



"sections": [



{



"description": "string",



"displayName": "string",



"expanded": true,



"properties": [



"string"



]



}



]



},



"table": {



"columns": [



{



"builtinColumnRef": "summary",



"columnRef": "myCustomColumn",



"displayName": "Color",



"id": "color",



"items": [



{



"displayName": "Active",



"icon": "CRITICAL",



"value": "ACTIVE"



}



],



"propertyRef": "apiColor",



"type": "cell-color-picker",



"width": "10%"



}



],



"emptyState": {



"text": "string"



}



},



"tabs": {



"groups": [



{



"description": "string",



"displayName": "string",



"properties": [



"string"



]



}



]



}



},



"version": "1.4.2"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")