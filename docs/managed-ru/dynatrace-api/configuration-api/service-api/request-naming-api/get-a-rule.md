---
title: Request naming API - GET a request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/get-a-rule
---

# Request naming API - GET a request naming rule

# Request naming API - GET a request naming rule

* Справочник
* Опубликовано 25 июня 2019 г.

Возвращает параметры указанного правила именования запросов.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать его, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID правила именования запросов, о котором запрашиваются сведения. | path | Обязательный |

## Ответ

Модели [JSON](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Learn the variations of JSON models in the Dynatrace request naming API.") зависят от **типа** модели, полный список вариантов смотри там.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RequestNaming](#openapi-definition-RequestNaming) | Успешно |

### Объекты тела ответа


#### Объект `RequestNaming`


Правило именования запросов.


| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [Condition](#openapi-definition-Condition)[] | Набор условий для использования правила именования запросов. Можно указать несколько условий. Запрос должен соответствовать **всем** указанным условиям, чтобы правило сработало. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| id | string | ID правила именования запросов. |
| managementZones | string[] | Указывает management zones, для которых применяется данное правило. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| namingPattern | string | Имя, которое присваивается соответствующим запросам. |
| order | string | Строка порядка. Сортировка именований запросов по алфавиту на основе строки порядка определяет их относительный порядок. Обычно это управляется Dynatrace внутренне и не присутствует в ответах GET, а также не используется, если присутствует в запросах PUT/POST, за исключением случаев, отдельно оговорённых. |
| placeholders | [Placeholder](#openapi-definition-Placeholder)[] | Список пользовательских плейсхолдеров для использования в шаблоне именования. Позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования запроса. |


#### Объект `Condition`


Условие использования правила.


| Элемент | Тип | Описание |
| --- | --- | --- |
| attribute | string | Атрибут, по которому выполняется сопоставление. Обрати внимание: для атрибута свойства службы нужно использовать сравнение типа `FAST_STRING`. Примечание для фазы 3: `SERVICE_TAG` не поддерживается (теги службы недоступны). `PROCESS_GROUP_TAG` устарел и больше не будет оцениваться, вместо него нужно использовать primary tags. `SERVICE_DISPLAY_NAME` вычисляет обнаруженное имя службы вместо этого. Элемент может принимать следующие значения * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Специфичное для типа сравнение для атрибутов. Фактический набор полей зависит от типа сравнения. Список фактических объектов приведён в описании поля **type** или см. [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m). |


#### Объект `ComparisonInfo`


Специфичное для типа сравнение для атрибутов. Фактический набор полей зависит от типа сравнения. Список фактических объектов приведён в описании поля **type** или см. [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m).


| Элемент | Тип | Описание |
| --- | --- | --- |
| comparison | string | Оператор сравнения. Можно инвертировать его, установив **negate** в `true`. |
| negate | boolean | Инвертирует оператор сравнения **operator**. Например, превращает **equals** в **does not equal**. |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo Элемент может принимать следующие значения * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` |
| value | - | Значение для сравнения. |
| values | - | Значения для сравнения. |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |


#### Объект `Placeholder`


Пользовательский плейсхолдер для использования в качестве шаблона значения именования.


Позволяет извлечь значение атрибута запроса или другой атрибут запроса и использовать его в шаблоне именования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Какое значение атрибута запроса нужно использовать, если он встречается в нескольких дочерних запросах. Применимо только к атрибуту `SERVICE_REQUEST_ATTRIBUTE`, когда **useFromChildCalls** равен `true`. Для агрегации `COUNT` поле **kind** неприменимо. Элемент может принимать следующие значения * `COUNT` * `FIRST` * `LAST` |
| attribute | string | Атрибут, из которого выполняется извлечение. Можно использовать только атрибуты типа **string**. Примечание для Phase 3: `SERVICE_TAG` не поддерживается (теги сервисов недоступны). `PROCESS_GROUP_TAG` устарел и больше не будет обрабатываться, вместо него нужно использовать основные теги. `SERVICE_DISPLAY_NAME` вместо этого использует обнаруженное имя сервиса. Элемент может принимать следующие значения * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` |
| delimiterOrRegex | string | В зависимости от значения **type**: * `REGEX_EXTRACTION`: регулярное выражение. * `BETWEEN_DELIMITER`: строка открывающего разделителя для поиска. * Все остальные значения: строка разделителя для поиска. |
| endDelimiter | string | Строка закрывающего разделителя для поиска. Требуется, если значение **kind** равно `BETWEEN_DELIMITER`. В остальных случаях неприменимо. |
| kind | string | Тип извлечения. Определяет либо использование регулярного выражения (`regex`), либо позицию значения атрибута запроса, которое нужно извлечь. Если **attribute** равен `SERVICE_REQUEST_ATTRIBUTE`, а **aggregation** равен `COUNT`, нужно задать значение `ORIGINAL_TEXT`. Элемент может принимать следующие значения * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` |
| name | string | Имя плейсхолдера. Используется в шаблоне именования как `{name}`. |
| normalization | string | Формат извлечённой строки. Элемент может принимать следующие значения * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| oneAgentAttributeKey | string | Атрибут OneAgent, из которого выполняется извлечение. Требуется, если значение **kind** равно `ONE_AGENT_ATTRIBUTE`. В остальных случаях неприменимо. |
| requestAttribute | string | Атрибут запроса, из которого выполняется извлечение. Требуется, если значение **kind** равно `SERVICE_REQUEST_ATTRIBUTE`. В остальных случаях неприменимо. |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Определяет допустимые источники атрибутов запроса для условий или плейсхолдеров. |
| useFromChildCalls | boolean | Если `true`, атрибут запроса будет взят из вызова дочернего сервиса. Применимо только к атрибуту `SERVICE_REQUEST_ATTRIBUTE`. По умолчанию `false`. |


#### Объект `PropagationSource`


Определяет допустимые источники атрибутов запроса для условий или плейсхолдеров.


| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZone | string | Использовать только атрибуты запроса из сервисов, принадлежащих этой management zone. Использовать либо это, либо `serviceTag`. |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | - |


#### Объект `UniversalTag`


Использовать только атрибуты запроса из сервисов, у которых есть этот тег. Использовать либо это, либо `managementZone`.


| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Для пользовательских тегов используется значение `CONTEXTLESS`. Контекст задаётся для тегов, которые автоматически импортируются OneAgent (например, из консоли AWS или переменных окружения). Это полезно для определения происхождения тегов, когда они не заданы вручную, а также помогает избежать конфликтов с другими существующими тегами. Если тег не был импортирован автоматически, задаётся `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` |
| key | string | Ключ тега. Для пользовательских тегов сюда помещается значение тега. Ключ позволяет категоризировать несколько тегов. Возможно, что для одного ключа существует несколько значений, каждое из которых представлено как отдельный тег. Поэтому ключ не имеет семантики ключа карты (map), а скорее похож на ключ кортежа "ключ-значение". В некоторых случаях, например для пользовательских тегов, ключ представляет собой фактическое значение тега, а поле value не задано, такие теги называются тегами без значения. |
| value | string | Значение тега. Неприменимо к пользовательским тегам. Если у тега есть отдельные ключ и значение (в текстовом представлении они разделены двоеточием «:»), в этом поле задаётся фактическое значение. Пары ключ-значение могут встречаться у автоматически импортированных тегов и тегов, заданных правилами, если используются экстракторы. |

### Тело ответа для моделей JSON

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