---
title: Request naming API - PUT a request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/put-a-rule
---

# Request naming API - PUT a request naming rule

# Request naming API - PUT a request naming rule

* Справочная информация
* Опубликовано 25 июня 2019 г.

Обновляет указанное правило именования запросов. Если правило с указанным ID не существует, создаётся новое правило с этим ID.

Запрос принимает и возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Модели JSON, которые зависят от **type** модели, перечислены в разделе [JSON models](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Learn the variations of JSON models in the Dynatrace request naming API.").

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID именования запросов, которое нужно обновить.  ID именования запросов в теле запроса должен совпадать с этим ID. | path | Обязательный |
| body | [RequestNaming](#openapi-definition-RequestNaming) | Тело JSON запроса, содержащее обновлённые параметры именования запросов. | body | Необязательный |

### Объекты тела запроса


#### Объект `RequestNaming`


Правило именования запроса.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| conditions | [Condition](#openapi-definition-Condition)[] | Набор условий использования правила именования запросов. Можно указать несколько условий. Чтобы правило сработало, запрос должен соответствовать **всем** указанным условиям. | Обязательно |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Обязательно |
| id | string | ID правила именования запроса. | Опционально |
| managementZones | string[] | Задаёт management zones, для которых применяется это правило. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные при отладке | Опционально |
| namingPattern | string | Имя, присваиваемое соответствующим запросам. | Обязательно |
| order | string | Строка порядка. Сортировка именований запросов по алфавиту с помощью строки порядка определяет их относительный порядок. Как правило, это управляется Dynatrace внутренне и не присутствует в ответах GET, а также не используется, если указано в запросах PUT/POST, кроме случаев, отдельно оговорённых. | Опционально |
| placeholders | [Placeholder](#openapi-definition-Placeholder)[] | Список пользовательских плейсхолдеров для использования в шаблоне именования. Позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования запроса. | Опционально |


#### Объект `Condition`


Условие использования правила.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| attribute | string | Атрибут, который нужно сопоставить. Обрати внимание: для атрибута свойства сервиса нужно использовать сравнение типа `FAST_STRING`. Обрати внимание для Phase 3: `SERVICE_TAG` не поддерживается (теги сервисов недоступны). `PROCESS_GROUP_TAG` устарел и больше не будет вычисляться, вместо него нужно использовать основные теги. `SERVICE_DISPLAY_NAME` вычисляет вместо этого обнаруженное имя сервиса. Элемент может принимать следующие значения * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Обязательно |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Специфичное для типа сравнение атрибутов. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или в [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m). | Обязательно |


#### Объект `ComparisonInfo`


Специфичное для типа сравнение атрибутов. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или в [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m).


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| comparison | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`. | Обязательно |
| negate | boolean | Инвертирует оператор сравнения **operator**. Например, превращает **equals** в **does not equal**. | Обязательно |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo Элемент может принимать следующие значения * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` | Обязательно |
| value | - | Значение для сравнения. | Опционально |
| values | - | Значения для сравнения. | Опционально |


#### Объект `ConfigurationMetadata`


Метаданные, полезные при отладке


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |


#### Объект `Placeholder`


Пользовательский плейсхолдер для использования в качестве шаблона значения именования.


Позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Какое значение атрибута запроса нужно использовать, если оно встречается сразу в нескольких дочерних запросах.  Применимо только к атрибуту `SERVICE_REQUEST_ATTRIBUTE`, когда **useFromChildCalls** равен `true`.  Для агрегации `COUNT` поле **kind** неприменимо. Элемент может принимать следующие значения * `COUNT` * `FIRST` * `LAST` | Опционально |
| attribute | string | Атрибут, из которого производится извлечение. Можно использовать только атрибуты типа **string**.  Примечание для Phase 3:  `SERVICE_TAG` не поддерживается (теги сервисов недоступны).  `PROCESS_GROUP_TAG` устарел и больше не будет обрабатываться, вместо него нужно использовать основные теги.  `SERVICE_DISPLAY_NAME` вместо этого использует обнаруженное имя сервиса. Элемент может принимать следующие значения * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Обязательно |
| delimiterOrRegex | string | В зависимости от значения **type**:  * `REGEX_EXTRACTION`: регулярное выражение. * `BETWEEN_DELIMITER`: открывающая строка-разделитель для поиска. * Все остальные значения: строка-разделитель для поиска. | Опционально |
| endDelimiter | string | Закрывающая строка-разделитель для поиска.  Обязательно, если значение **kind** равно `BETWEEN_DELIMITER`. В остальных случаях неприменимо. | Опционально |
| kind | string | Тип извлечения.  Определяет либо использование регулярного выражения (`regex`), либо позицию значения атрибута запроса, которое нужно извлечь.  Когда **attribute** равен `SERVICE_REQUEST_ATTRIBUTE`, а **aggregation** равна `COUNT`, нужно установить значение `ORIGINAL_TEXT`. Элемент может принимать следующие значения * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` | Обязательно |
| name | string | Имя плейсхолдера. Использовать его в шаблоне именования как `{name}`. | Обязательно |
| normalization | string | Формат извлечённой строки. Элемент может принимать следующие значения * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` | Опционально |
| oneAgentAttributeKey | string | Атрибут One Agent, из которого производится извлечение.  Обязательно, если значение **kind** равно `ONE_AGENT_ATTRIBUTE`. В остальных случаях неприменимо. | Опционально |
| requestAttribute | string | Атрибут запроса, из которого производится извлечение.  Обязательно, если значение **kind** равно `SERVICE_REQUEST_ATTRIBUTE`. В остальных случаях неприменимо. | Опционально |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Определяет допустимые источники атрибутов запроса для условий или плейсхолдеров. | Опционально |
| useFromChildCalls | boolean | Если `true`, атрибут запроса будет взят из дочернего вызова сервиса.  Применимо только к атрибуту `SERVICE_REQUEST_ATTRIBUTE`. По умолчанию `false`. | Опционально |


#### Объект `PropagationSource`


Определяет допустимые источники атрибутов запроса для условий или плейсхолдеров.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZone | string | Использовать только атрибуты запроса от сервисов, принадлежащих этой management zone. Использовать либо это поле, либо `serviceTag`. | Опционально |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | - | Опционально |


#### Объект `UniversalTag`


Использовать только атрибуты запроса от сервисов, у которых есть этот тег. Использовать либо это поле, либо `managementZone`.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник происхождения тега, такой как AWS или Cloud Foundry. Для пользовательских тегов использовать значение `CONTEXTLESS`.  Context устанавливается для тегов, которые автоматически импортируются OneAgent (например, из консоли AWS или переменных окружения). Это полезно для определения происхождения тегов, когда они не заданы вручную, а также помогает предотвратить конфликты с другими существующими тегами. Если тег не импортирован автоматически, устанавливается `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` | Опционально |
| key | string | Ключ тега. Для пользовательских тегов сюда помещается значение тега.  Ключ позволяет категоризировать несколько тегов. Возможна ситуация, когда для одного ключа существует несколько значений, и все они представлены как самостоятельные теги. Поэтому ключ не имеет семантики ключа карты (map key), а скорее является ключом кортежа ключ-значение. В некоторых случаях, например для пользовательских тегов, ключ представляет собой фактическое значение тега, а поле value не задано, такие теги называются тегами без значения. | Обязательно |
| value | string | Значение тега. Неприменимо к пользовательским тегам.  Если у тега есть отдельные ключ и значение (в текстовом представлении они разделены двоеточием «:»), в этом поле устанавливается фактическое значение. Пары ключ-значение могут встречаться у автоматически импортированных тегов и тегов, заданных правилами, если используются извлекатели (extractors). | Опционально |

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

Запрос возвращает краткое представление обновлённого или вновь созданного правила.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Правило именования запросов создано. Ответ содержит ID и имя нового правила именования запросов. |
| **204** | - | Успешно. Правило именования запросов обновлено. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

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
| code | integer | Код статуса HTTP |
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

## Проверка payload

Рекомендуется проверять payload перед отправкой его в реальном запросе. Код ответа **204** означает, что payload действителен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация действительна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
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