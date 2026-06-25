---
title: OneAgent remote configuration management API - POST задание конфигурации
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/oneagent/post-config-job
scraped: 2026-05-12T11:55:04.939406
---

# OneAgent remote configuration management API - POST задание конфигурации

# OneAgent remote configuration management API - POST задание конфигурации

* Справочник
* Опубликовано 06 октября 2022 г.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `oneAgents.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

OneAgent идентифицируются по их ID. Используйте запрос [OneAgent on a host](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на ваших хостах через Dynatrace API.") чтобы узнать ID OneAgent, которые вы хотите сконфигурировать.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| restart | boolean | OneAgent будут перезапущены (`true`) или нет (`false`) после конфигурирования. По умолчанию OneAgent перезапускаются при переконфигурировании сетевой зоны, host group, тегов хоста или свойств хоста, перезапуск необходим для применения изменений. | query | Необязательный |
| body | [RemoteConfigurationManagementOperationOneAgentRequest](#openapi-definition-RemoteConfigurationManagementOperationOneAgentRequest) | JSON-тело запроса, содержащее определение задания remote configuration management. | body | Обязательный |

### Объекты тела запроса

#### Объект `RemoteConfigurationManagementOperationOneAgentRequest`

Запрос на создание операции remote configuration management.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| entities | string[] | Список ID сущностей, для которых нужно выполнить remote configuration management. | Обязательный |
| operations | [RemoteConfigurationManagementOperation[]](#openapi-definition-RemoteConfigurationManagementOperation) | Список операций remote configuration management для выполнения. | Обязательный |

#### Объект `RemoteConfigurationManagementOperation`

Определение одной операции remote configuration management.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attribute | string | Атрибут, на который влияет операция. Поле может принимать значения: * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` | Обязательный |
| operation | string | Операция, выполняемая над заданным атрибутом. Поле может принимать значения: * `clear` * `set` | Обязательный |
| value | string | Значение, которое нужно присвоить заданному атрибуту. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"entities": [



"HOST-D454A967666E7970",



"HOST-811760CFF2A5E872"



],



"operations": [



{



"attribute": "networkZone",



"operation": "set",



"value": "exampleNetworkZoneName"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [RemoteConfigurationManagementJob](#openapi-definition-RemoteConfigurationManagementJob) | Создано |
| **400** | [RemoteConfigurationManagementValidationResult](#openapi-definition-RemoteConfigurationManagementValidationResult) | Неудача. Входные данные некорректны. |
| **409** | - | В данный момент выполняется другое задание remote configuration management |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemoteConfigurationManagementJob`

Задание remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| endTime | string | Дата (в формате ISO 8601: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') завершения задания remote configuration management. Это поле присутствует только для завершённых заданий. |
| entityType | string | Тип сущностей, изменяемых remote configuration management. Поле может принимать значения: * `ACTIVE_GATE` * `ONE_AGENT` |
| failedEntities | [RemoteIdentityOperationFailedEntityDto[]](#openapi-definition-RemoteIdentityOperationFailedEntityDto) | Список неудавшихся заданий remote configuration management. |
| id | string | ID задания remote configuration management. |
| inProgressEntities | string[] | Список выполняющихся заданий remote configuration management. |
| operations | [RemoteConfigurationManagementOperation[]](#openapi-definition-RemoteConfigurationManagementOperation) | Список выполненных (успешных и неудавшихся) заданий remote configuration management. |
| processedEntitiesCount | integer | Количество сущностей, уже обработанных на момент создания ответа. |
| startTime | string | Дата (в формате ISO 8601: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') запуска задания remote configuration management. |
| timeoutTime | string | Дата (в формате ISO 8601: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') истечения времени ожидания выполняющегося задания remote configuration management. Это поле присутствует только для выполняющихся заданий. |
| totalEntitiesCount | integer | Общее количество сущностей для обработки. |

#### Объект `RemoteIdentityOperationFailedEntityDto`

Информация о неудавшемся remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | Entity ID, для которого запрос remote configuration management не удался |
| failureMessage | string | Описание ошибки изменения настроек связи |
| failureReason | string | Причина сбоя изменения настроек связи. Поле может принимать значения: * `CONNECTION_FAILURE` * `TIMEOUT` |

#### Объект `RemoteConfigurationManagementOperation`

Определение одной операции remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| attribute | string | Атрибут, на который влияет операция. Поле может принимать значения: * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | Операция, выполняемая над заданным атрибутом. Поле может принимать значения: * `clear` * `set` |
| value | string | Значение, которое нужно присвоить заданному атрибуту. |

#### Объект `RemoteConfigurationManagementValidationResult`

Результат валидации remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| invalidEntities | [RemoteConfigurationManagementEntityValidationError[]](#openapi-definition-RemoteConfigurationManagementEntityValidationError) | Список ошибок валидации для сущностей. |
| invalidOperations | [RemoteConfigurationManagementOperationValidationError[]](#openapi-definition-RemoteConfigurationManagementOperationValidationError) | Список ошибок валидации для операций. |

#### Объект `RemoteConfigurationManagementEntityValidationError`

Ошибка валидации сущности для remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| entity | string | ID сущности, для которой валидация не удалась. |
| reasons | string[] | Причина сбоя валидации сущности. Поле может принимать значения: * `CLOUD_NATIVE_NOT_SUPPORTED` * `NOT_ALLOWED_WITH_CLUSTER_ACTIVE_GATE` * `NOT_CONNECTED` * `RUNNING_IN_CONTAINER` * `STANDALONE_NOT_SUPPORTED` * `VERSION_NOT_SUPPORTED` |

#### Объект `RemoteConfigurationManagementOperationValidationError`

Ошибка валидации определения операции remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| attribute | string | Атрибут, на который влияет операция. Поле может принимать значения: * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | Операция, выполняемая над заданным атрибутом. Поле может принимать значения: * `clear` * `set` |
| reason | string | Причина сбоя валидации. |
| value | string | Значение, которое нужно присвоить заданному атрибуту. |

### JSON-модели тела ответа

```
{



"endTime": "2020-11-05T08:15:30.144Z",



"entityType": "ACTIVE_GATE or ONE_AGENT",



"failedEntities": [



{



"entityId": "HOST-D454A967666E7970",



"failureMessage": "Failed to access new tenant: f47ac10b-58cc-4372-a567-0e02b2c3d479",



"failureReason": "CONNECTION_FAILURE"



}



],



"id": "7974003406714390819",



"inProgressEntities": [



"HOST-D454A967666E7970"



],



"operations": [



{



"attribute": "networkZone",



"operation": "set",



"value": "exampleNetworkZoneName"



}



],



"processedEntitiesCount": 1,



"startTime": "2020-11-05T08:15:30.144Z",



"timeoutTime": "2020-11-05T08:15:30.144Z",



"totalEntitiesCount": 1



}
```

```
{



"invalidEntities": [



{



"entity": "entityId",



"reasons": [



"RUNNING_IN_CONTAINER"



]



}



],



"invalidOperations": [



{



"attribute": "networkZone",



"operation": "set",



"reason": "Value must not start with a period",



"value": ".exampleInvalidNetworkZoneName"



}



]



}
```

Ответ не отправляется клиенту, пока не обработаны все OneAgent, указанные в payload. OneAgent считается обработанным, когда ему отправлено сообщение о переконфигурировании; фактическое переконфигурирование выполняется OneAgent независимо.

## Проверка payload

Рекомендуется проверить payload перед отправкой реального запроса. Код ответа **204** означает корректный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/validator` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/validator` |

### Аутентификация

Для выполнения запроса нужен access-токен со scope `oneAgents.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Ответ не содержит тела. |
| **400** | [RemoteConfigurationManagementValidationResult](#openapi-definition-RemoteConfigurationManagementValidationResult) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

#### Объекты тела ответа

#### Объект `RemoteConfigurationManagementValidationResult`

Результат валидации remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| invalidEntities | [RemoteConfigurationManagementEntityValidationError[]](#openapi-definition-RemoteConfigurationManagementEntityValidationError) | Список ошибок валидации для сущностей. |
| invalidOperations | [RemoteConfigurationManagementOperationValidationError[]](#openapi-definition-RemoteConfigurationManagementOperationValidationError) | Список ошибок валидации для операций. |

#### Объект `RemoteConfigurationManagementEntityValidationError`

Ошибка валидации сущности для remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| entity | string | ID сущности, для которой валидация не удалась. |
| reasons | string[] | Причина сбоя валидации сущности. Поле может принимать значения: * `CLOUD_NATIVE_NOT_SUPPORTED` * `NOT_ALLOWED_WITH_CLUSTER_ACTIVE_GATE` * `NOT_CONNECTED` * `RUNNING_IN_CONTAINER` * `STANDALONE_NOT_SUPPORTED` * `VERSION_NOT_SUPPORTED` |

#### Объект `RemoteConfigurationManagementOperationValidationError`

Ошибка валидации определения операции remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| attribute | string | Атрибут, на который влияет операция. Поле может принимать значения: * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | Операция, выполняемая над заданным атрибутом. Поле может принимать значения: * `clear` * `set` |
| reason | string | Причина сбоя валидации. |
| value | string | Значение, которое нужно присвоить заданному атрибуту. |

#### JSON-модели тела ответа

```
{



"invalidEntities": [



{



"entity": "entityId",



"reasons": [



"RUNNING_IN_CONTAINER"



]



}



],



"invalidOperations": [



{



"attribute": "networkZone",



"operation": "set",



"reason": "Value must not start with a period",



"value": ".exampleInvalidNetworkZoneName"



}



]



}
```