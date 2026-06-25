---
title: OneAgent remote configuration management API - GET текущее задание
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/oneagent/get-current-job
scraped: 2026-05-12T11:55:15.393635
---

# OneAgent remote configuration management API - GET текущее задание

# OneAgent remote configuration management API - GET текущее задание

* Справочник
* Опубликовано 06 октября 2022 г.

Получает параметры выполняющегося в данный момент задания конфигурации для OneAgent.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/current` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/oneagents/remoteConfigurationManagement/current` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `oneAgents.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemoteConfigurationManagementJob](#openapi-definition-RemoteConfigurationManagementJob) | Успех |
| **204** | - | В данный момент не выполняется ни одно задание remote configuration management |
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

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

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