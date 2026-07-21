---
title: Request naming API - POST a new request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule
---

# Request naming API - POST a new request naming rule

# Request naming API - POST a new request naming rule

* Справочная информация
* Опубликовано 25 июня 2019 г.

Создаёт новое правило именования запросов. Подробный пример использования смотри в разделе [Request naming API - Create a new rule](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Learn how to create a request naming rule via the Dynatrace API.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, смотри в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Список всех моделей JSON, зависящих от **типа** модели, приведён в разделе [JSON models](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Learn the variations of JSON models in the Dynatrace request naming API.").

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| position | string | Порядок нового правила именования запросов. Значение `PREPEND` добавляет правило в начало списка, `APPEND`, в конец. По умолчанию используется `APPEND`. Элемент может принимать следующие значения * `APPEND` * `PREPEND` | query | Необязательный |
| body | [RequestNaming](#openapi-definition-RequestNaming) | Тело запроса JSON, содержащее параметры нового правила именования запросов. Указывать ID правила нельзя! | body | Необязательный |

### Объекты тела запроса


#### Объект `RequestNaming`


Правило именования запроса.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditions | [Condition](#openapi-definition-Condition)[] | Набор условий для применения правила именования запроса. Можно указать несколько условий. Для срабатывания правила запрос должен соответствовать **всем** указанным условиям. | Обязательный |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Обязательный |
| id | string | ID правила именования запроса. | Опциональный |
| managementZones | string[] | Указывает management zones, для которых применяется это правило. | Опциональный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| namingPattern | string | Имя, которое присваивается совпадающим запросам. | Обязательный |
| order | string | Строка порядка. Сортировка правил именования запросов по алфавиту согласно их строке порядка определяет их относительный порядок. Обычно это управляется Dynatrace внутренне и не присутствует в ответах GET, а также не используется, если присутствует в запросах PUT/POST, за исключением случаев, отдельно оговорённых. | Опциональный |
| placeholders | [Placeholder](#openapi-definition-Placeholder)[] | Список пользовательских плейсхолдеров для использования в шаблоне именования. Позволяет извлечь значение атрибута запроса или другого атрибута запроса и использовать его в шаблоне именования запроса. | Опциональный |


#### Объект `Condition`


Условие применения правила.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attribute | string | Атрибут, который нужно сопоставить. Обрати внимание, что для атрибута service property нужно использовать сравнение типа `FAST_STRING`. Примечание для Phase 3: `SERVICE_TAG` не поддерживается (service tags недоступны). `PROCESS_GROUP_TAG` устарел и больше не будет вычисляться, вместо него нужно использовать primary tags. `SERVICE_DISPLAY_NAME` вычисляет обнаруженное имя сервиса вместо этого. Элемент может принимать следующие значения * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Обязательный |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Сравнение атрибутов, специфичное для типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или в [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m). | Обязательный |


#### Объект `ComparisonInfo`


Сравнение атрибутов, специфичное для типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или в [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m).


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comparison | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`. | Обязательный |
| negate | boolean | Инвертирует оператор сравнения **operator**. Например, превращает **equals** в **does not equal**. | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo Элемент может принимать следующие значения * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` | Обязательный |
| value | - | Значение для сравнения. | Опциональный |
| values | - | Значения для сравнения. | Опциональный |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |


#### Объект `Placeholder`


Пользовательский плейсхолдер для использования в качестве шаблона значения именования.


Позволяет извлечь значение атрибута запроса или другого атрибута запроса и использовать его в шаблоне именования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Какое значение атрибута запроса нужно использовать, если он встречается в нескольких дочерних запросах.  Применимо только к атрибуту `SERVICE_REQUEST_ATTRIBUTE`, когда **useFromChildCalls** равно `true`.  Для агрегации `COUNT` поле **kind** неприменимо. Элемент может принимать следующие значения * `COUNT` * `FIRST` * `LAST` | Необязательный |
| attribute | string | Атрибут, из которого производится извлечение. Можно использовать только атрибуты типа **string**.  Примечание для Phase 3:  `SERVICE_TAG` не поддерживается (теги сервисов недоступны).  `PROCESS_GROUP_TAG` устарел и больше не будет обрабатываться, вместо него нужно использовать основные теги.  `SERVICE_DISPLAY_NAME` вместо этого использует определённое имя сервиса. Элемент может принимать следующие значения * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Обязательный |
| delimiterOrRegex | string | В зависимости от значения **type**:  * `REGEX_EXTRACTION`: регулярное выражение. * `BETWEEN_DELIMITER`: строка открывающего разделителя для поиска. * Все остальные значения: строка разделителя для поиска. | Необязательный |
| endDelimiter | string | Строка закрывающего разделителя для поиска.  Обязательно, если значение **kind** равно `BETWEEN_DELIMITER`. В остальных случаях неприменимо. | Необязательный |
| kind | string | Тип извлечения.  Определяет использование регулярного выражения (`regex`) либо позицию значения атрибута запроса, которое нужно извлечь.  Когда **attribute** равен `SERVICE_REQUEST_ATTRIBUTE`, а **aggregation** равен `COUNT`, нужно установить значение `ORIGINAL_TEXT`. Элемент может принимать следующие значения * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` | Обязательный |
| name | string | Имя плейсхолдера. Использовать его в шаблоне именования как `{name}`. | Обязательный |
| normalization | string | Формат извлечённой строки. Элемент может принимать следующие значения * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` | Необязательный |
| oneAgentAttributeKey | string | Атрибут OneAgent, из которого производится извлечение.  Обязательно, если значение **kind** равно `ONE_AGENT_ATTRIBUTE`. В остальных случаях неприменимо. | Необязательный |
| requestAttribute | string | Атрибут запроса, из которого производится извлечение.  Обязательно, если значение **kind** равно `SERVICE_REQUEST_ATTRIBUTE`. В остальных случаях неприменимо. | Необязательный |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Определяет допустимые источники атрибутов запроса для условий или плейсхолдеров. | Необязательный |
| useFromChildCalls | boolean | Если `true`, атрибут запроса будет взят из дочернего вызова сервиса.  Применимо только к атрибуту `SERVICE_REQUEST_ATTRIBUTE`. По умолчанию `false`. | Необязательный |


#### Объект `PropagationSource`


Определяет допустимые источники атрибутов запроса для условий или плейсхолдеров.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | string | Использовать только атрибуты запроса от сервисов, принадлежащих этой management zone. Использовать либо это поле, либо `serviceTag`. | Необязательный |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | - | Необязательный |


#### Объект `UniversalTag`


Использовать только атрибуты запроса от сервисов, у которых есть этот тег. Использовать либо это поле, либо `managementZone`.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник происхождения тега, например AWS или Cloud Foundry. Для пользовательских тегов использовать значение `CONTEXTLESS`.  Context задаётся для тегов, автоматически импортированных OneAgent (например, из консоли AWS или переменных окружения). Это полезно для определения происхождения тегов, не заданных вручную, а также помогает предотвратить конфликты с другими существующими тегами. Если тег не импортирован автоматически, устанавливается `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` | Необязательный |
| key | string | Ключ тега. Для пользовательских тегов сюда помещается значение тега.  Ключ позволяет категоризировать несколько тегов. Возможна ситуация, когда одному ключу соответствует несколько значений, каждое из которых представлено как отдельный тег. Поэтому ключ не имеет семантики ключа map, а скорее является ключом пары ключ-значение. В некоторых случаях, например для пользовательских тегов, ключ представляет собой фактическое значение тега, а поле value не задаётся, такие теги называются тегами без значения. | Обязательный |
| value | string | Значение тега. Неприменимо для пользовательских тегов.  Если у тега есть отдельные ключ и значение (в текстовом представлении они разделены двоеточием «:»), это поле содержит фактическое значение. Пары ключ-значение могут встречаться у автоматически импортированных тегов и тегов, заданных правилами, если используются экстракторы. | Необязательный |

### Тело запроса, модели JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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



"value": "/url"



}



}



],



"enabled": true,



"namingPattern": "renamed request"



}
```

## Ответ

Запрос возвращает краткое представление вновь созданного правила.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Именование запроса создано. Ответ содержит ID новой службы. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Название сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

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

## Валидация полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой в составе реального запроса. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела ответа JSON

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