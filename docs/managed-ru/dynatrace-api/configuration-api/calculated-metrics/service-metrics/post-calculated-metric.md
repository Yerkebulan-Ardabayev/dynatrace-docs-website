---
title: Service metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric
scraped: 2026-05-12T11:15:54.027447
---

# Service metrics API - POST a metric

# Service metrics API - POST a metric

* Reference
* Published Dec 16, 2019

Создаёт новую вычисляемую метрику сервиса.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/json-models "Вариации моделей в API вычисляемых метрик сервиса").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CalculatedServiceMetric](#openapi-definition-CalculatedServiceMetric) | JSON-тело запроса. Содержит параметры новой вычисляемой метрики сервиса. | body | Required |

### Объекты тела запроса

#### Объект `CalculatedServiceMetric`

Дескриптор вычисляемой метрики сервиса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditions | [Condition[]](#openapi-definition-Condition) | Набор условий использования метрики.  Для использования метрики должны выполняться **все** указанные условия. | Optional |
| dimensionDefinition | [DimensionDefinition](#openapi-definition-DimensionDefinition) | Параметры определения вычисляемой метрики сервиса. | Optional |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). | Required |
| entityId | string | Ограничивает использование метрики указанным сервисом.  Это поле взаимоисключающее с полем **managementZones**. | Optional |
| ignoreMutedRequests | boolean | Метрика должна (`true`) или не должна (`false`) игнорировать отключённые запросы. | Optional |
| managementZones | string[] | Ограничивает использование метрики указанными зонами управления.  Это поле взаимоисключающее с полем **entityId**. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| metricDefinition | [CalculatedMetricDefinition](#openapi-definition-CalculatedMetricDefinition) | Определение вычисляемой метрики сервиса. | Required |
| name | string | Отображаемое имя метрики. | Required |
| tsmMetricKey | string | Ключ вычисляемой метрики сервиса. | Required |
| unit | string | Единица измерения метрики. Возможные значения: * `AMPERE` * `BILLION` * `BIT` * `BIT_PER_HOUR` * `BIT_PER_MINUTE` * `BIT_PER_SECOND` * `BYTE` * `BYTE_PER_HOUR` * `BYTE_PER_MINUTE` * `BYTE_PER_SECOND` * `CORES` * `COUNT` * `DAY` * `DECIBEL_MILLI_WATT` * `GIBI_BYTE` * `GIBI_BYTE_PER_HOUR` * `GIBI_BYTE_PER_MINUTE` * `GIBI_BYTE_PER_SECOND` * `GIGA` * `GIGA_BYTE` * `GIGA_BYTE_PER_HOUR` * `GIGA_BYTE_PER_MINUTE` * `GIGA_BYTE_PER_SECOND` * `HERTZ` * `HOUR` * `KIBI_BYTE` * `KIBI_BYTE_PER_HOUR` * `KIBI_BYTE_PER_MINUTE` * `KIBI_BYTE_PER_SECOND` * `KILO` * `KILO_BYTE` * `KILO_BYTE_PER_HOUR` * `KILO_BYTE_PER_MINUTE` * `KILO_BYTE_PER_SECOND` * `KILO_METRE_PER_HOUR` * `MEBI_BYTE` * `MEBI_BYTE_PER_HOUR` * `MEBI_BYTE_PER_MINUTE` * `MEBI_BYTE_PER_SECOND` * `MEGA` * `MEGA_BYTE` * `MEGA_BYTE_PER_HOUR` * `MEGA_BYTE_PER_MINUTE` * `MEGA_BYTE_PER_SECOND` * `METRE_PER_HOUR` * `METRE_PER_SECOND` * `MICRO_SECOND` * `MILLION` * `MILLI_CORES` * `MILLI_SECOND` * `MILLI_SECOND_PER_MINUTE` * `MINUTE` * `MONTH` * `MSU` * `NANO_SECOND` * `NANO_SECOND_PER_MINUTE` * `NOT_APPLICABLE` * `PERCENT` * `PER_HOUR` * `PER_MINUTE` * `PER_SECOND` * `PIXEL` * `PROMILLE` * `RATIO` * `SECOND` * `STATE` * `TRILLION` * `UNSPECIFIED` * `VOLT` * `WATT` * `WEEK` * `YEAR` | Required |
| unitDisplayName | string | Отображаемое имя единицы измерения метрики.  Применимо только когда параметр **unit** установлен в `UNSPECIFIED`. | Optional |

#### Объект `Condition`

Условие использования правила.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attribute | string | Сопоставляемый атрибут.  Учтите, что для атрибута свойства сервиса нужно использовать сравнение типа `FAST_STRING`. Возможные значения: * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Required |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Сравнение для атрибутов, зависящее от типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [Service metrics API - JSON models](https://dt-url.net/9803svb). | Required |

#### Объект `ComparisonInfo`

Сравнение для атрибутов, зависящее от типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [Service metrics API - JSON models](https://dt-url.net/9803svb).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comparison | string | Оператор сравнения. Его можно инвертировать, установив **negate** в `true`. | Required |
| negate | boolean | Инвертирует **оператор** сравнения. Например, превращает **equals** в **does not equal**. | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo Возможные значения: * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` | Required |
| value | string | Значение для сравнения. | Optional |
| values | - | Значения для сравнения. | Optional |

#### Объект `DimensionDefinition`

Параметры определения вычисляемой метрики сервиса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimension | string | Шаблон значения измерения.  Можно определить пользовательские плейсхолдеры в поле **placeholders** и использовать их здесь. | Required |
| name | string | Имя измерения. | Required |
| placeholders | [Placeholder[]](#openapi-definition-Placeholder) | Список пользовательских плейсхолдеров для использования в шаблоне значения измерения. | Optional |
| topX | integer | Количество верхних значений для расчёта. | Required |
| topXAggregation | string | Агрегация измерения. Возможные значения: * `AVERAGE` * `COUNT` * `MAX` * `MIN` * `OF_INTEREST_RATIO` * `OTHER_RATIO` * `SINGLE_VALUE` * `SUM` | Required |
| topXDirection | string | Как рассчитывать значения **topX**. Возможные значения: * `ASCENDING` * `DESCENDING` | Required |

#### Объект `Placeholder`

Пользовательский плейсхолдер, используемый как шаблон значения для именования.

Он позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Какое значение атрибута запроса использовать, когда он встречается в нескольких дочерних запросах.  Применимо только для атрибута `SERVICE_REQUEST_ATTRIBUTE`, когда **useFromChildCalls** равно `true`.  Для агрегации `COUNT` поле **kind** не применяется. Возможные значения: * `COUNT` * `FIRST` * `LAST` | Optional |
| attribute | string | Атрибут, из которого извлекать. Можно использовать только атрибуты типа **string**. Возможные значения: * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Required |
| delimiterOrRegex | string | В зависимости от значения **type**:  * `REGEX_EXTRACTION`: регулярное выражение. * `BETWEEN_DELIMITER`: искомая строка открывающего разделителя. * Все остальные значения: искомая строка разделителя. | Optional |
| endDelimiter | string | Искомая строка закрывающего разделителя.  Обязательно, если значение **kind** равно `BETWEEN_DELIMITER`. В остальных случаях не применяется. | Optional |
| kind | string | Тип извлечения.  Определяет либо использование регулярного выражения (`regex`), либо позицию извлекаемого значения атрибута запроса.  Когда **attribute** равно `SERVICE_REQUEST_ATTRIBUTE`, а **aggregation** равно `COUNT`, должно быть установлено в `ORIGINAL_TEXT` Возможные значения: * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` | Required |
| name | string | Имя плейсхолдера. Используйте его в шаблоне именования как `{name}`. | Required |
| normalization | string | Формат извлекаемой строки. Возможные значения: * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` | Optional |
| oneAgentAttributeKey | string | Атрибут OneAgent, из которого извлекать.  Обязательно, если значение **kind** равно `ONE_AGENT_ATTRIBUTE`. В остальных случаях не применяется. | Optional |
| requestAttribute | string | Атрибут запроса, из которого извлекать.  Обязательно, если значение **kind** равно `SERVICE_REQUEST_ATTRIBUTE`. В остальных случаях не применяется. | Optional |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Определяет допустимые источники атрибутов запросов для условий или плейсхолдеров. | Optional |
| useFromChildCalls | boolean | Если `true`, атрибут запроса будет взят из дочернего вызова сервиса.  Применимо только для атрибута `SERVICE_REQUEST_ATTRIBUTE`. По умолчанию `false`. | Optional |

#### Объект `PropagationSource`

Определяет допустимые источники атрибутов запросов для условий или плейсхолдеров.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | string | Использовать только атрибуты запросов из сервисов, принадлежащих этой зоне управления.. Используйте либо это, либо `serviceTag` | Optional |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | Использовать только атрибуты запросов из сервисов с этим тегом. Используйте либо это, либо `managementZone` | Optional |

#### Объект `UniversalTag`

Использовать только атрибуты запросов из сервисов с этим тегом. Используйте либо это, либо `managementZone`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry. Для пользовательских тегов используйте значение `CONTEXTLESS`.  Контекст устанавливается для тегов, автоматически импортируемых OneAgent (например, из консоли AWS или переменных окружения). Он полезен для определения происхождения тегов, когда они не заданы вручную, а также помогает предотвратить конфликты с другими существующими тегами. Если тег не импортирован автоматически, устанавливается `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` | Optional |
| key | string | Ключ тега. Для пользовательских тегов укажите здесь значение тега.  Ключ позволяет категоризировать несколько тегов. Возможно наличие нескольких значений для одного ключа, которые все будут представлены как отдельные теги. Поэтому ключ не имеет семантики ключа карты, а скорее похож на ключ пары ключ-значение. В некоторых случаях, например для пользовательских тегов, ключ представляет фактическое значение тега, а поле value не установлено: такие теги называются теги без значения. | Required |
| value | string | Значение тега. Не применяется к пользовательским тегам.  Если у тега есть отдельные ключ и значение (в текстовом представлении они разделены двоеточием ':'), в это поле записывается фактическое значение. Пары ключ-значение могут возникать для автоматически импортируемых тегов и тегов, заданных правилами при использовании экстракторов. | Optional |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `CalculatedMetricDefinition`

Определение вычисляемой метрики сервиса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| metric | string | Захватываемая метрика. Возможные значения: * `CPU_TIME` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DISK_IO_TIME` * `EXCEPTION_COUNT` * `FAILED_REQUEST_COUNT` * `FAILED_REQUEST_COUNT_CLIENT` * `FAILURE_RATE` * `FAILURE_RATE_CLIENT` * `HTTP_4XX_ERROR_COUNT` * `HTTP_4XX_ERROR_COUNT_CLIENT` * `HTTP_5XX_ERROR_COUNT` * `HTTP_5XX_ERROR_COUNT_CLIENT` * `IO_TIME` * `LOCK_TIME` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `PROCESSING_TIME` * `REQUEST_ATTRIBUTE` * `REQUEST_COUNT` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `SUCCESSFUL_REQUEST_COUNT` * `SUCCESSFUL_REQUEST_COUNT_CLIENT` * `WAIT_TIME` | Required |
| requestAttribute | string | Захватываемый атрибут запроса.  Применимо только когда параметр **metric** установлен в `REQUEST_ATTRIBUTE`. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"conditions": [



{



"attribute": "WEBREQUEST_URL_PATH",



"comparisonInfo": {



"caseSensitive": false,



"comparison": "BEGINS_WITH",



"negate": false,



"type": "STRING",



"value": "/url_path"



}



}



],



"dimensionDefinition": {



"dimension": "{myPlaceholder}",



"name": "my dimension",



"placeholders": [



{



"attribute": "WEBREQUEST_URL_PATH",



"delimiterOrRegex": "/booking",



"kind": "BEFORE_DELIMITER",



"name": "myPlaceholder",



"normalization": "ORIGINAL",



"useFromChildCalls": "false"



}



],



"topX": 10,



"topXAggregation": "AVERAGE",



"topXDirection": "DESCENDING"



},



"enabled": true,



"managementZones": [



"zone1"



],



"metricDefinition": {



"metric": "CPU_TIME"



},



"name": "My Metric",



"tsmMetricKey": "calc:service.mymetric",



"unit": "MICRO_SECOND"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Вычисляемая метрика сервиса создана. Тело ответа содержит ключ новой метрики. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

## Пример

В этом примере запрос создаёт вычисляемую метрику сервиса, которая отслеживает количество запросов в сервисах с тегом **payment**. Она разбивает значения по классу HTTP-статуса.

Ключ метрики **calc:service.requestsbycode**, отображаемое имя **Requests by code**.

API-токен передаётся в заголовке **Authorization**.

Поскольку тело запроса длинное, в этом примере оно усечено в секции **Curl**. Полное тело смотрите в секции **Request body**. Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно. Перед использованием убедитесь, что вы используете тег, доступный в вашем окружении.

Ответ содержит ключ и имя только что созданной метрики.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service \



-H 'Accept: Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service
```

#### Тело запроса

```
{



"tsmMetricKey": "calc:service.requestsbycode",



"name": "Requests by code",



"enabled": true,



"metricDefinition": {



"metric": "REQUEST_COUNT",



"requestAttribute": null



},



"unit": "COUNT",



"unitDisplayName": "",



"entityId": null,



"managementZones": [],



"conditions": [



{



"attribute": "PROCESS_GROUP_TAG",



"comparisonInfo": {



"type": "TAG",



"comparison": "TAG_KEY_EQUALS",



"value": {



"context": "CONTEXTLESS",



"key": "payment"



},



"negate": false



}



}



],



"dimensionDefinition": {



"name": "HTTP Status class",



"dimension": "{HTTP-StatusClass}",



"placeholders": [],



"topX": 10,



"topXDirection": "DESCENDING",



"topXAggregation": "SINGLE_VALUE"



}



}
```

#### Тело ответа

```
{



"id": "calc:service.requestsbycode",



"name": "Requests by code"



}
```

#### Код ответа

201

## Связанные темы

* [Вычисляемые метрики для сервисов](/managed/observe/application-observability/services/calculated-service-metric "Узнайте, как создать вычисляемую метрику на основе веб-запросов.")
* [Многомерный анализ](/managed/observe/application-observability/multidimensional-analysis "Настройте представление многомерного анализа и сохраните его как вычисляемую метрику.")