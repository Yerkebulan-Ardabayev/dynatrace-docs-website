---
title: Settings API - Получение схемы (GET)
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/get-schema
scraped: 2026-03-06T21:19:38.146283
---

Получает параметры указанной схемы настроек.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/{schemaId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/schemas/{schemaId}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `settings.read`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| schemaId | string | Идентификатор требуемой схемы. | path | Обязательный |
| schemaVersion | string | Версия требуемой схемы. Если не задана, возвращается самая последняя версия. | query | Необязательный |

## Ответ

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SchemaDefinitionRestDto](#openapi-definition-SchemaDefinitionRestDto) | Успех |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Доступ запрещён. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Указанная схема не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SchemaDefinitionRestDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| allowedScopes | string[] | Список областей, в которых может использоваться схема. |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | Список ограничений, определяющих допустимые значения для схемы. |
| deletionConstraints | [DeletionConstraint[]](#openapi-definition-DeletionConstraint) | Ограничения, определяющие допустимые значения для удаления. |
| description | string | Краткое описание схемы. |
| displayName | string | Отображаемое имя схемы. |
| documentation | string | Расширенное описание схемы и/или ссылки на документацию. |
| dynatrace | string | Версия формата данных. |
| enums | object | Список определений свойств перечислений. |
| keyProperty | string | Имя ключевого свойства в этой схеме. |
| maturity | string | Уровень зрелости схемы. Возможные значения:  * PREVIEW: Функции предварительного просмотра не являются общедоступными, но могут быть доступны в определённых средах в рамках программ раннего доступа. Они с наибольшей вероятностью могут быть изменены несовместимым образом. * EARLY\_ADOPTER: Функции, отмеченные как «ранний последователь», доступны во всех средах, но недостаточно зрелые для обозначения «общая доступность». Мы не ожидаем несовместимых изменений, но учтите, что они ещё не полностью стабильны, и несовместимые изменения могут потребоваться в редких случаях. * GENERAL\_AVAILABILITY: Функции, отмеченные как «общая доступность», являются наиболее стабильными. Хотя схемы будут продолжать развиваться, будет приложено максимум усилий для обеспечения обратной совместимости.  В любом случае автоматизация должна использовать поле `schemaVersion` при записи объектов настроек. Элемент может содержать следующие значения * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| maxObjects | integer | Максимальное количество объектов на область. Применимо только если **multiObject** установлено в `true`. |
| metadata | object | Метаданные настройки. |
| multiObject | boolean | Допускается несколько (`true`) объектов на область или один (`false`) объект на область. |
| ordered | boolean | Если `true`, порядок объектов имеет семантическое значение. Применимо только если **multiObject** установлено в `true`. |
| properties | object | Список свойств схемы. |
| schemaConstraints | [SchemaConstraintRestDto[]](#openapi-definition-SchemaConstraintRestDto) | Ограничения, определяющие допустимые значения конфигурационного элемента в целом. |
| schemaGroups | string[] | Имена групп, к которым принадлежит схема. |
| schemaId | string | Идентификатор схемы. |
| tableColumns | object | Определения столбцов таблицы для использования в пользовательском интерфейсе. |
| types | object | Список определений типов. Тип — это сложное свойство, содержащее собственный набор подсвойств. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Настройка элементов пользовательского интерфейса |
| version | string | Версия схемы. |

#### Объект `ComplexConstraint`

Ограничение на значения, допустимые для сложного свойства настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| checkAllProperties | boolean | Определяет, вызывает ли изменение любого свойства проверку повторной отправки секрета. |
| customMessage | string | Пользовательское сообщение для недопустимых значений. |
| customValidatorId | string | Идентификатор пользовательского валидатора. |
| maximumPropertyCount | integer | Максимальное количество свойств, которые могут быть установлены. |
| minimumPropertyCount | integer | Минимальное количество свойств, которые должны быть установлены. |
| properties | string[] | Список свойств (определённых по идентификаторам), используемых для проверки ограничения. |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении через пользовательский интерфейс. |
| timeout | integer | Максимальное время в секундах, в течение которого пользовательский валидатор может выполняться. |
| type | string | Тип ограничения. Элемент может содержать следующие значения * `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` * `SECRET_RESUBMISSION` * `UNKNOWN` |

#### Объект `DeletionConstraint`

Ограничение на значения, которые будут удалены.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMessage | string | Пользовательское сообщение для недопустимых значений. |
| customValidatorId | string | Идентификатор пользовательского валидатора. |
| schemaIds | string[] | Идентификаторы схем, которые должны быть проверены на наличие ссылок на данную схему. |
| timeout | integer | Максимальное время в секундах, в течение которого пользовательский валидатор может выполняться. |
| type | string | Тип ограничения удаления. Элемент может содержать следующие значения * `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN` |

#### Объект `EnumType`

Определение свойства перечисления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| enumClass | string | Существующий Java-класс перечисления, содержащий допустимые значения. |
| items | [EnumValue[]](#openapi-definition-EnumValue) | Список допустимых значений перечисления. |
| type | string | Тип свойства. Элемент может содержать следующие значения * `enum` |

#### Объект `EnumValue`

Допустимое значение для свойства перечисления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание значения. |
| displayName | string | Отображаемое имя значения. |
| enumInstance | string | Имя значения в существующем Java-классе перечисления. |
| icon | string | Иконка значения. |
| value | string | Допустимое значение перечисления. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `PropertyDefinition`

Конфигурация свойства в схеме настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | Список ограничений, определяющих допустимые значения. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Конфигурация источника данных для свойства. |
| default | string | Значение по умолчанию, используемое при отсутствии указанного значения. Если не-синглтон имеет значение `null`, это означает пустую коллекцию. |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| forceSecretResubmission | boolean | Определяет, разрешено ли изменение значения, когда секретные свойства не |
| items | [Item](#openapi-definition-Item) | Элемент свойства коллекции. |
| maxObjects | integer | Максимальное количество **объектов** в свойстве коллекции. Для синглтонов имеет значение `1`. |
| metadata | object | Метаданные свойства. |
| migrationPattern | string | Шаблон со ссылками на свойства для создания нового значения. |
| minObjects | integer | Минимальное количество **объектов** в свойстве коллекции. |
| modificationPolicy | string | Политика модификации свойства. Элемент может содержать следующие значения * `ALWAYS` * `DEFAULT` * `NEVER` |
| nullable | boolean | Значение может (`true`) или не может (`false`) быть `null`. |
| precondition | [Precondition](#openapi-definition-Precondition) | Предусловие для видимости свойства. |
| referencedType | string | Тип, на который ссылается значение свойства |
| subType | string | Подтип значения свойства. |
| type | string | Тип значения свойства. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Настройка элементов пользовательского интерфейса |

#### Объект `Constraint`

Ограничение на значения, допустимые для свойства настроек.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMessage | string | Пользовательское сообщение для недопустимых значений. |
| customValidatorId | string | Идентификатор пользовательского валидатора. |
| disallowDangerousRegex | boolean | Запрещать ли использование опасных регулярных выражений |
| maxLength | integer | Максимально допустимая длина строковых значений. |
| maximum | number | Максимально допустимое значение. |
| minLength | integer | Минимально требуемая длина строковых значений. |
| minimum | number | Минимально допустимое значение. |
| pattern | string | Шаблон регулярного выражения для допустимых строковых значений. |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении через пользовательский интерфейс. |
| timeout | integer | Максимальное время в секундах, в течение которого пользовательский валидатор может выполняться. |
| type | string | Тип ограничения. Элемент может содержать следующие значения * `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` * `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | Список свойств, для которых комбинация значений должна быть уникальной. |

#### Объект `DatasourceDefinition`

Конфигурация источника данных для свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| filterProperties | string[] | Свойства для фильтрации параметров источника данных. |
| fullContext | boolean | Ожидает ли этот источник данных полную полезную нагрузку настройки в качестве контекста. |
| identifier | string | Идентификатор пользовательского источника данных значения свойства. |
| resetValue | string | Когда сбрасывать значение источника данных в пользовательском интерфейсе при изменении фильтра. Элемент может содержать следующие значения * `ALWAYS` * `INVALID_ONLY` * `NEVER` |
| useApiSearch | boolean | Если true, источник данных должен использовать API для фильтрации результатов вместо фильтрации на стороне клиента. |
| validate | boolean | Валидировать ли ввод, разрешая только значения, возвращённые источником данных. |

#### Объект `Item`

Элемент свойства коллекции.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | Список ограничений, определяющих допустимые значения. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Конфигурация источника данных для свойства. |
| description | string | Краткое описание элемента. |
| displayName | string | Отображаемое имя элемента. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| metadata | object | Метаданные элементов. |
| referencedType | string | Тип, на который ссылается значение элемента. |
| subType | string | Подтип значения элемента. |
| type | string | Тип значения элемента. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Настройка элементов пользовательского интерфейса |

#### Объект `UiCustomization`

Настройка элементов пользовательского интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| callback | [UiCallbackCustomization](#openapi-definition-UiCallbackCustomization) | Параметры настройки пользовательского интерфейса для определения пользовательских обратных вызовов |
| expandable | [UiExpandableCustomization](#openapi-definition-UiExpandableCustomization) | Настройка пользовательского интерфейса для раскрываемой секции |
| table | [UiTableCustomization](#openapi-definition-UiTableCustomization) | Настройка таблиц пользовательского интерфейса |
| tabs | [UiTabsCustomization](#openapi-definition-UiTabsCustomization) | Настройка пользовательского интерфейса для вкладок |

#### Объект `UiCallbackCustomization`

Параметры настройки пользовательского интерфейса для определения пользовательских обратных вызовов

| Элемент | Тип | Описание |
| --- | --- | --- |
| buttons | [UiButtonCustomization[]](#openapi-definition-UiButtonCustomization) | Настройка пользовательского интерфейса для определения кнопок, вызывающих функции при нажатии |

#### Объект `UiButtonCustomization`

Настройка пользовательского интерфейса для определения кнопки, вызывающей функцию при нажатии

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание, отображаемое во всплывающей подсказке при наведении на кнопку |
| displayName | string | Метка кнопки |
| identifier | string | Идентификатор функции, вызываемой при нажатии кнопки |
| insert | string | Позиция, в которой кнопка должна отображаться в пользовательском интерфейсе. Элемент может содержать следующие значения * `FIRST` * `LAST` |

#### Объект `UiExpandableCustomization`

Настройка пользовательского интерфейса для раскрываемой секции

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя |
| expanded | boolean | Определяет, должен ли элемент быть развёрнут по умолчанию |
| sections | [UiExpandableSectionCustomization[]](#openapi-definition-UiExpandableSectionCustomization) | Список секций |

#### Объект `UiExpandableSectionCustomization`

Настройка раскрываемой секции для пользовательского интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание |
| displayName | string | Отображаемое имя |
| expanded | boolean | Определяет, должна ли секция быть развёрнута по умолчанию |
| properties | string[] | Список свойств |

#### Объект `UiTableCustomization`

Настройка таблиц пользовательского интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| columns | [UiTableColumnCustomization[]](#openapi-definition-UiTableColumnCustomization) | Список столбцов для таблицы пользовательского интерфейса |
| emptyState | [UiEmptyStateCustomization](#openapi-definition-UiEmptyStateCustomization) | Настройка пользовательского интерфейса для пустого состояния таблицы |

#### Объект `UiTableColumnCustomization`

Настройка столбцов таблицы пользовательского интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| builtinColumnRef | string | Встроенная реализация столбца для пользовательского интерфейса. |
| columnRef | string | Ссылка на столбец из свойства 'tableColumns' схемы для этого столбца. |
| displayName | string | Отображаемое имя для этого столбца. |
| id | string | Идентификатор этого столбца, используемый для фильтрации. Обязателен для конфликтующих или составных столбцов — в остальных случаях используется ref. |
| items | [UiTableColumnItemCustomization[]](#openapi-definition-UiTableColumnItemCustomization) | Возможные элементы этого столбца. |
| propertyRef | string | Ссылка на свойство для этого столбца. |
| type | string | Тип этого столбца для пользовательского интерфейса. |
| width | string | Ширина, которую этот столбец должен занимать в таблице. |

#### Объект `UiTableColumnItemCustomization`

Настройка элементов столбца таблицы пользовательского интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя этого элемента. |
| icon | string | Иконка этого элемента. |
| value | string | Значение этого элемента. |

#### Объект `UiEmptyStateCustomization`

Настройка пользовательского интерфейса для пустого состояния таблицы

| Элемент | Тип | Описание |
| --- | --- | --- |
| text | string | Текст, отображаемый в пустом состоянии |

#### Объект `UiTabsCustomization`

Настройка пользовательского интерфейса для вкладок

| Элемент | Тип | Описание |
| --- | --- | --- |
| groups | [UiTabGroupCustomization[]](#openapi-definition-UiTabGroupCustomization) | Список групп |

#### Объект `UiTabGroupCustomization`

Настройка группы вкладок для пользовательского интерфейса

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание |
| displayName | string | Отображаемое имя |
| properties | string[] | Список свойств |

#### Объект `Precondition`

Предусловие для видимости свойства.

| Элемент | Тип | Описание |
| --- | --- | --- |
| expectedValue | string | Ожидаемое значение свойства. Применимо только к свойствам типа `EQUALS`. |
| expectedValues | - | Список допустимых значений свойства. Применимо только к свойствам типа `IN`. |
| pattern | string | Регулярное выражение, сопоставляемое со свойством. Применимо только к свойствам типа `REGEX_MATCH`. |
| precondition | [Precondition](#openapi-definition-Precondition) | Предусловие для видимости свойства. |
| preconditions | [Precondition[]](#openapi-definition-Precondition) | Список дочерних предусловий для оценки. Применимо только к свойствам типов `AND` и `OR`. |
| property | string | Свойство для оценки. |
| type | string | Тип предусловия. Элемент может содержать следующие значения * `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH` |

#### Объект `SchemaConstraintRestDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| byteLimit | integer | Максимально допустимый размер в байтах для суммы всех сохранённых значений схемы |
| customMessage | string | Пользовательское сообщение для недопустимых значений. |
| customValidatorId | string | Идентификатор пользовательского валидатора. |
| flattenCollections | boolean | Следует ли разворачивать свойства коллекций при проверке уникальности, чтобы только непересекающиеся коллекции считались уникальными |
| skipAsyncValidation | boolean | Пропускать ли валидацию при изменении через пользовательский интерфейс. |
| type | string | Тип ограничения схемы. Элемент может содержать следующие значения * `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | Список свойств, для которых комбинация значений должна быть уникальной |

#### Объект `TableColumn`

Определение столбца таблицы для использования в пользовательском интерфейсе.

| Элемент | Тип | Описание |
| --- | --- | --- |
| pattern | string | Шаблон со ссылками на свойства для создания одного значения для столбца. |

#### Объект `SchemaType`

Список определений типов.

Тип — это сложное свойство, содержащее собственный набор подсвойств.

| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | Список ограничений, определяющих допустимые значения. |
| description | string | Краткое описание свойства. |
| displayName | string | Отображаемое имя свойства. |
| documentation | string | Расширенное описание и/или ссылки на документацию. |
| properties | object | Определение свойств, которые могут быть сохранены. |
| searchPattern | string | Шаблон для поиска сводки (например, "Оповещение через *X* минут.") конфигурации в пользовательском интерфейсе. |
| summaryPattern | string | Шаблон для сводки (например, "Оповещение через *X* минут.") конфигурации в пользовательском интерфейсе. |
| type | string | Тип ссылочного типа. Элемент может содержать следующие значения * `object` |
| version | string | Версия типа. |
| versionInfo | string | Краткое описание версии. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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