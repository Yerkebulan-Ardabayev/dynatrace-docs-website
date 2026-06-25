---
title: Request naming API - GET a request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/get-a-rule
scraped: 2026-05-12T11:17:44.223882
---

# Request naming API - GET a request naming rule

# Request naming API - GET a request naming rule

* Reference
* Published Jun 25, 2019

Возвращает параметры указанного правила именования запросов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID запрашиваемого правила именования запросов. | path | Required |

## Ответ

Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Изучите вариации JSON-моделей в Dynatrace API именования запросов.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RequestNaming](#openapi-definition-RequestNaming) | Успех |

### Объекты тела ответа

#### Объект `RequestNaming`

Правило именования запросов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [Condition[]](#openapi-definition-Condition) | Набор условий использования правила именования запросов.  Можно указать несколько условий. Запрос должен соответствовать **всем** указанным условиям, чтобы правило сработало. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила именования запросов. |
| managementZones | string[] | Указывает зоны управления, для которых должно применяться это правило. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| namingPattern | string | Имя, присваиваемое подходящим запросам. |
| order | string | Строка порядка. Сортировка именований запросов в алфавитном порядке по их строке порядка определяет их относительный порядок.  Обычно этим управляет Dynatrace внутренне; строка не присутствует в ответах GET и не используется, если присутствует в запросах PUT/POST, кроме случаев, где указано иное. |
| placeholders | [Placeholder[]](#openapi-definition-Placeholder) | Список пользовательских плейсхолдеров для использования в шаблоне именования.  Он позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования запросов. |

#### Объект `Condition`

Условие использования правила.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attribute | string | Сопоставляемый атрибут.  Учтите, что для атрибута свойства сервиса нужно использовать сравнение типа `FAST_STRING`. Возможные значения: * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Сравнение для атрибутов, зависящее от типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [Service metrics API - JSON models](https://dt-url.net/9803svb). |

#### Объект `ComparisonInfo`

Сравнение для атрибутов, зависящее от типа. Фактический набор полей зависит от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [Service metrics API - JSON models](https://dt-url.net/9803svb).

| Элемент | Тип | Описание |
| --- | --- | --- |
| comparison | string | Оператор сравнения. Его можно инвертировать, установив **negate** в `true`. |
| negate | boolean | Инвертирует **оператор** сравнения. Например, превращает **equals** в **does not equal**. |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo Возможные значения: * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` |
| value | string | Значение для сравнения. |
| values | - | Значения для сравнения. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `Placeholder`

Пользовательский плейсхолдер, используемый как шаблон значения для именования.

Он позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Какое значение атрибута запроса использовать, когда он встречается в нескольких дочерних запросах.  Применимо только для атрибута `SERVICE_REQUEST_ATTRIBUTE`, когда **useFromChildCalls** равно `true`.  Для агрегации `COUNT` поле **kind** не применяется. Возможные значения: * `COUNT` * `FIRST` * `LAST` |
| attribute | string | Атрибут, из которого извлекать. Можно использовать только атрибуты типа **string**. Возможные значения: * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` |
| delimiterOrRegex | string | В зависимости от значения **type**:  * `REGEX_EXTRACTION`: регулярное выражение. * `BETWEEN_DELIMITER`: искомая строка открывающего разделителя. * Все остальные значения: искомая строка разделителя. |
| endDelimiter | string | Искомая строка закрывающего разделителя.  Обязательно, если значение **kind** равно `BETWEEN_DELIMITER`. В остальных случаях не применяется. |
| kind | string | Тип извлечения.  Определяет либо использование регулярного выражения (`regex`), либо позицию извлекаемого значения атрибута запроса.  Когда **attribute** равно `SERVICE_REQUEST_ATTRIBUTE`, а **aggregation** равно `COUNT`, должно быть установлено в `ORIGINAL_TEXT` Возможные значения: * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` |
| name | string | Имя плейсхолдера. Используйте его в шаблоне именования как `{name}`. |
| normalization | string | Формат извлекаемой строки. Возможные значения: * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| oneAgentAttributeKey | string | Атрибут OneAgent, из которого извлекать.  Обязательно, если значение **kind** равно `ONE_AGENT_ATTRIBUTE`. В остальных случаях не применяется. |
| requestAttribute | string | Атрибут запроса, из которого извлекать.  Обязательно, если значение **kind** равно `SERVICE_REQUEST_ATTRIBUTE`. В остальных случаях не применяется. |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Определяет допустимые источники атрибутов запросов для условий или плейсхолдеров. |
| useFromChildCalls | boolean | Если `true`, атрибут запроса будет взят из дочернего вызова сервиса.  Применимо только для атрибута `SERVICE_REQUEST_ATTRIBUTE`. По умолчанию `false`. |

#### Объект `PropagationSource`

Определяет допустимые источники атрибутов запросов для условий или плейсхолдеров.

| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZone | string | Использовать только атрибуты запросов из сервисов, принадлежащих этой зоне управления.. Используйте либо это, либо `serviceTag` |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | Использовать только атрибуты запросов из сервисов с этим тегом. Используйте либо это, либо `managementZone` |

#### Объект `UniversalTag`

Использовать только атрибуты запросов из сервисов с этим тегом. Используйте либо это, либо `managementZone`

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry. Для пользовательских тегов используйте значение `CONTEXTLESS`.  Контекст устанавливается для тегов, автоматически импортируемых OneAgent (например, из консоли AWS или переменных окружения). Он полезен для определения происхождения тегов, когда они не заданы вручную, а также помогает предотвратить конфликты с другими существующими тегами. Если тег не импортирован автоматически, устанавливается `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` |
| key | string | Ключ тега. Для пользовательских тегов укажите здесь значение тега.  Ключ позволяет категоризировать несколько тегов. Возможно наличие нескольких значений для одного ключа, которые все будут представлены как отдельные теги. Поэтому ключ не имеет семантики ключа карты, а скорее похож на ключ пары ключ-значение. В некоторых случаях, например для пользовательских тегов, ключ представляет фактическое значение тега, а поле value не установлено: такие теги называются теги без значения. |
| value | string | Значение тега. Не применяется к пользовательским тегам.  Если у тега есть отдельные ключ и значение (в текстовом представлении они разделены двоеточием ':'), в это поле записывается фактическое значение. Пары ключ-значение могут возникать для автоматически импортируемых тегов и тегов, заданных правилами при использовании экстракторов. |

### JSON-модели тела ответа

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