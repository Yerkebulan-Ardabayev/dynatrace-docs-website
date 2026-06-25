---
title: Settings API - GET a schema
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/get-schema
scraped: 2026-05-12T11:31:24.476700
---

# Settings API - GET a schema

# Settings API - GET a schema

* Reference
* Published Feb 24, 2021

Возвращает параметры указанной settings schema.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/{schemaId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/schemas/{schemaId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| schemaId | string | ID требуемой schema. | path | Required |
| schemaVersion | string | Версия требуемой schema.  Если не задано, возвращается самая последняя версия. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SchemaDefinitionRestDto](#openapi-definition-SchemaDefinitionRestDto) | Успех |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Доступ запрещён. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Указанная schema не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SchemaDefinitionRestDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| allowedScopes | string[] | Список scopes, в которых может использоваться schema. |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | Список constraints, ограничивающих значения, принимаемые schema. |
| deletionConstraints | [DeletionConstraint[]](#openapi-definition-DeletionConstraint) | Constraints, ограничивающие удаляемые значения. |
| description | string | Краткое описание schema. |
| displayName | string | Отображаемое имя schema. |
| documentation | string | Расширенное описание schema и/или ссылки на документацию. |
| dynatrace | string | Версия формата данных. |
| enums | object | Список определений enum-свойств. |
| keyProperty | string | Имя ключевого свойства в этой schema. |
| maturity | string | Зрелость schema. Возможные значения:  * PREVIEW: функции preview, как правило, недоступны массово, но могут быть доступны в отдельных окружениях в рамках программ раннего доступа. У них наиболее высокая вероятность несовместимых изменений. * EARLY\_ADOPTER: функции с пометкой "early adopter" доступны во всех окружениях, но недостаточно зрелы для обозначения "general availability". Несовместимых изменений для них не ожидается, но учитывайте, что они пока не полностью стабильны и в редких случаях могут потребоваться несовместимые изменения. * GENERAL\_AVAILABILITY: функции с пометкой "general availability" наиболее стабильны. Schemas со временем продолжают развиваться, но это делается с сохранением обратной совместимости.  В любом случае автоматизации должны использовать поле `schemaVersion` при записи settings objects. Возможные значения: * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| maxObjects | integer | Максимальное количество объектов на scope.  Применимо, только если **multiObject** установлен в `true`. |
| metadata | object | Метаданные настройки. |
| multiObject | boolean | Разрешено несколько объектов на scope (`true`) или только один объект на scope (`false`). |
| ordered | boolean | Если `true`, порядок объектов имеет смысловое значение.  Применимо, только если **multiObject** установлен в `true`. |
| properties | object | Список свойств schema. |
| schemaConstraints | [SchemaConstraintRestDto[]](#openapi-definition-SchemaConstraintRestDto) | Constraints, ограничивающие значения, принимаемые в данном элементе конфигурации, как единое целое. |
| schemaGroups | string[] | Имена групп, к которым принадлежит schema. |
| schemaId | string | ID schema. |
| tableColumns | object | Определения колонок таблицы для использования в UI. |
| types | object | Список определений типов.  Тип, это сложное свойство, содержащее собственный набор под-свойств. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Кастомизация для UI-элементов |
| version | string | Версия schema. |

#### Объект `ComplexConstraint`

Constraint на значения, принимаемые для сложного settings-свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| checkAllProperties | boolean | Определяет, вызывает ли модификация любого свойства повторную проверку секретов. |
| customMessage | string | Пользовательское сообщение для невалидных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| maximumPropertyCount | integer | Максимальное количество свойств, которое можно задать. |
| minimumPropertyCount | integer | Минимальное количество свойств, которое должно быть задано. |
| properties | string[] | Список свойств (определённых по ID), которые используются для проверки constraint. |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении из UI. |
| timeout | integer | Максимальное время в секундах, отведённое для работы пользовательского валидатора. |
| type | string | Тип constraint. Возможные значения: * `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` * `SECRET_RESUBMISSION` * `UNKNOWN` |

#### Объект `DeletionConstraint`

Constraint на значения, которые будут удалены.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMessage | string | Пользовательское сообщение для невалидных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| schemaIds | string[] | ID schemas, которые нужно проверить на ссылки на данную schema. |
| timeout | integer | Максимальное время в секундах, отведённое для работы пользовательского валидатора. |
| type | string | Тип deletion-constraint. Возможные значения: * `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN` |

#### Объект `EnumType`

Определение enum-свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| enumClass | string | Существующий Java enum-класс, содержащий допустимые значения enum. |
| items | [EnumValue[]](#openapi-definition-EnumValue) | Список допустимых значений enum. |
| type | string | Тип свойства. Возможные значения: * `enum` |

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

Конфигурация свойства в settings schema.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | Список constraints, ограничивающих принимаемые значения. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Конфигурация источника данных для свойства. |
| default | string | Значение по умолчанию, используемое, если значение не задано.  Если не-singleton имеет значение `null`, это означает пустую коллекцию. |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| forceSecretResubmission | boolean | Определяет, разрешено ли изменение значения, когда секретные свойства не заданы |
| items | [Item](#openapi-definition-Item) | Элемент коллекционного свойства. |
| maxObjects | integer | Максимальное количество **объектов** в коллекционном свойстве.  Для singleton равно `1`. |
| metadata | object | Метаданные свойства. |
| migrationPattern | string | Шаблон со ссылками на свойства для создания нового значения. |
| minObjects | integer | Минимальное количество **объектов** в коллекционном свойстве. |
| modificationPolicy | string | Политика модификации свойства. Возможные значения: * `ALWAYS` * `DEFAULT` * `NEVER` |
| nullable | boolean | Значение может быть `null` (`true`) или не может быть `null` (`false`). |
| precondition | [Precondition](#openapi-definition-Precondition) | Предусловие видимости свойства. |
| referencedType | string | Тип, на который ссылается значение свойства |
| subType | string | Подтип значения свойства. |
| type | string | Тип значения свойства. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Кастомизация для UI-элементов |

#### Объект `Constraint`

Constraint на значения, принимаемые для settings-свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMessage | string | Пользовательское сообщение для невалидных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| disallowDangerousRegex | boolean | Запрещать ли использование опасных regex-выражений |
| maxLength | integer | Максимально допустимая длина строковых значений. |
| maximum | number | Максимально допустимое значение. |
| minLength | integer | Минимально требуемая длина строковых значений. |
| minimum | number | Минимально допустимое значение. |
| pattern | string | Шаблон регулярного выражения для валидных строковых значений. |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении из UI. |
| timeout | integer | Максимальное время в секундах, отведённое для работы пользовательского валидатора. |
| type | string | Тип constraint. Возможные значения: * `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` * `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | Список свойств, для которых комбинация значений должна быть уникальной. |

#### Объект `DatasourceDefinition`

Конфигурация источника данных для свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| filterProperties | string[] | Свойства, по которым фильтруются варианты источника данных. |
| fullContext | boolean | Ожидает ли этот источник данных полный payload настройки в качестве контекста. |
| identifier | string | Идентификатор пользовательского источника данных значения свойства. |
| resetValue | string | Когда сбрасывать значение источника данных в UI при изменении фильтра. Возможные значения: * `ALWAYS` * `INVALID_ONLY` * `NEVER` |
| useApiSearch | boolean | Если true, источник данных должен использовать api для фильтрации результатов вместо клиентской фильтрации. |
| validate | boolean | Валидировать ли ввод, чтобы разрешать только значения, возвращаемые источником данных. |

#### Объект `Item`

Элемент коллекционного свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | Список constraints, ограничивающих принимаемые значения. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Конфигурация источника данных для свойства. |
| description | string | Краткое описание элемента. |
| displayName | string | Отображаемое имя элемента. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| metadata | object | Метаданные элементов. |
| referencedType | string | Тип, на который ссылается значение элемента. |
| subType | string | Подтип значения элемента. |
| type | string | Тип значения элемента. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Кастомизация для UI-элементов |

#### Объект `UiCustomization`

Кастомизация для UI-элементов

| Элемент | Тип | Описание |
| --- | --- | --- |
| callback | [UiCallbackCustomization](#openapi-definition-UiCallbackCustomization) | Параметры UI-кастомизации для определения пользовательских callback-ов |
| expandable | [UiExpandableCustomization](#openapi-definition-UiExpandableCustomization) | UI-кастомизация для разворачиваемой секции |
| table | [UiTableCustomization](#openapi-definition-UiTableCustomization) | Кастомизация для UI-таблиц |
| tabs | [UiTabsCustomization](#openapi-definition-UiTabsCustomization) | UI-кастомизация для вкладок |

#### Объект `UiCallbackCustomization`

Параметры UI-кастомизации для определения пользовательских callback-ов

| Элемент | Тип | Описание |
| --- | --- | --- |
| buttons | [UiButtonCustomization[]](#openapi-definition-UiButtonCustomization) | UI-кастомизация для определения кнопок, вызывающих функции при нажатии |

#### Объект `UiButtonCustomization`

UI-кастомизация для определения кнопки, вызывающей функцию при нажатии

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание, отображаемое в подсказке при наведении на кнопку |
| displayName | string | Текст кнопки |
| identifier | string | Идентификатор функции, вызываемой при нажатии кнопки |
| insert | string | Позиция, в которой кнопка должна отображаться в UI. Возможные значения: * `FIRST` * `LAST` |

#### Объект `UiExpandableCustomization`

UI-кастомизация для разворачиваемой секции

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя |
| expanded | boolean | Определяет, должен ли элемент быть развёрнут по умолчанию |
| sections | [UiExpandableSectionCustomization[]](#openapi-definition-UiExpandableSectionCustomization) | Список секций |

#### Объект `UiExpandableSectionCustomization`

Кастомизация разворачиваемой секции для UI

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание |
| displayName | string | Отображаемое имя |
| expanded | boolean | Определяет, должна ли секция быть развёрнута по умолчанию |
| properties | string[] | Список свойств |

#### Объект `UiTableCustomization`

Кастомизация для UI-таблиц

| Элемент | Тип | Описание |
| --- | --- | --- |
| columns | [UiTableColumnCustomization[]](#openapi-definition-UiTableColumnCustomization) | Список колонок для UI-таблицы |
| emptyState | [UiEmptyStateCustomization](#openapi-definition-UiEmptyStateCustomization) | UI-кастомизация для пустого состояния таблицы |

#### Объект `UiTableColumnCustomization`

Кастомизация для колонок UI-таблиц

| Элемент | Тип | Описание |
| --- | --- | --- |
| builtinColumnRef | string | UI-специфичная встроенная реализация колонки для этой колонки. |
| columnRef | string | Колонка из свойства 'tableColumns' schema, на которую ссылается эта колонка. |
| displayName | string | Отображаемое имя для этой колонки. |
| id | string | ID этой колонки, используемый для фильтрации. Обязателен для конфликтующих или path-колонок, иначе используется ref. |
| items | [UiTableColumnItemCustomization[]](#openapi-definition-UiTableColumnItemCustomization) | Возможные элементы этой колонки. |
| propertyRef | string | Свойство, на которое ссылается эта колонка. |
| type | string | UI-специфичный тип для этой колонки. |
| width | string | Ширина, которую должна занимать эта колонка в таблице. |

#### Объект `UiTableColumnItemCustomization`

Кастомизация для элементов колонок UI-таблиц

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя этого элемента. |
| icon | string | Иконка этого элемента. |
| value | string | Значение этого элемента. |

#### Объект `UiEmptyStateCustomization`

UI-кастомизация для пустого состояния таблицы

| Элемент | Тип | Описание |
| --- | --- | --- |
| text | string | Текст для отображения в пустом состоянии |

#### Объект `UiTabsCustomization`

UI-кастомизация для вкладок

| Элемент | Тип | Описание |
| --- | --- | --- |
| groups | [UiTabGroupCustomization[]](#openapi-definition-UiTabGroupCustomization) | Список групп |

#### Объект `UiTabGroupCustomization`

Кастомизация группы вкладок для UI

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание |
| displayName | string | Отображаемое имя |
| properties | string[] | Список свойств |

#### Объект `Precondition`

Предусловие видимости свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| expectedValue | string | Ожидаемое значение свойства.  Применимо только для свойств типа `EQUALS`. |
| expectedValues | - | Список валидных значений свойства.  Применимо только для свойств типа `IN`. |
| pattern | string | Регулярное выражение, с которым сопоставляется свойство.  Применимо только для свойств типа `REGEX_MATCH`. |
| precondition | [Precondition](#openapi-definition-Precondition) | Предусловие видимости свойства. |
| preconditions | [Precondition[]](#openapi-definition-Precondition) | Список дочерних предусловий для оценки.  Применимо только для свойств типов `AND` и `OR`. |
| property | string | Оцениваемое свойство. |
| type | string | Тип предусловия. Возможные значения: * `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH` |

#### Объект `SchemaConstraintRestDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| byteLimit | integer | Максимально допустимый размер в байтах для суммы всех сохранённых значений schema |
| customMessage | string | Пользовательское сообщение для невалидных значений. |
| customValidatorId | string | ID пользовательского валидатора. |
| flattenCollections | boolean | Раскрывать ли коллекционные свойства при проверке уникальности, чтобы только непересекающиеся коллекции считались уникальными |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении из UI. |
| type | string | Тип schema-constraint. Возможные значения: * `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | Список свойств, для которых комбинация значений должна быть уникальной |

#### Объект `TableColumn`

Определение колонки таблицы для использования в UI.

| Элемент | Тип | Описание |
| --- | --- | --- |
| pattern | string | Шаблон со ссылками на свойства для создания единого значения колонки. |

#### Объект `SchemaType`

Список определений типов.

Тип, это сложное свойство, содержащее собственный набор под-свойств.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | Список constraints, ограничивающих принимаемые значения. |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| properties | object | Определение свойств, которые можно сохранять. |
| searchPattern | string | Шаблон для поиска по сводке (например, "Alert after *X* minutes.") конфигурации в UI. |
| summaryPattern | string | Шаблон для сводки (например, "Alert after *X* minutes.") конфигурации в UI. |
| type | string | Тип reference-типа. Возможные значения: * `object` |
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
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений constraints |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений constraints

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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