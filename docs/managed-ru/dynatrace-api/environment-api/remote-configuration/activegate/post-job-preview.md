---
title: ActiveGate remote configuration management API - POST предпросмотр задания
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/activegate/post-job-preview
scraped: 2026-05-12T11:55:39.387768
---

# ActiveGate remote configuration management API - POST предпросмотр задания

# ActiveGate remote configuration management API - POST предпросмотр задания

* Справочник
* Опубликовано 06 октября 2022 г.

Можно сгенерировать предпросмотр перед выполнением фактического изменения конфигурации.

Предпросмотр сообщает:

* Сколько сущностей в данный момент сконфигурировано так, как описано в payload
* Сколько сущностей будет сконфигурировано таким образом при отправке запроса на переконфигурирование

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/remoteConfigurationManagement/preview` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/remoteConfigurationManagement/preview` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `activeGates.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [RemoteConfigurationManagementOperationActiveGateRequest](#openapi-definition-RemoteConfigurationManagementOperationActiveGateRequest) | JSON-тело запроса, содержащее определение задания remote configuration management. | body | Обязательный |

### Объекты тела запроса

#### Объект `RemoteConfigurationManagementOperationActiveGateRequest`

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



"0x2b7c0b02",



"0x4928065d"



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
| **200** | [RemoteConfigurationManagementPreviewList](#openapi-definition-RemoteConfigurationManagementPreviewList) | Успех |
| **400** | [RemoteConfigurationManagementValidationResult](#openapi-definition-RemoteConfigurationManagementValidationResult) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RemoteConfigurationManagementPreviewList`

Список предпросмотров заданий remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| previews | [RemoteConfigurationManagementJobPreview[]](#openapi-definition-RemoteConfigurationManagementJobPreview) | Список предпросмотров заданий remote configuration management. |

#### Объект `RemoteConfigurationManagementJobPreview`

Предпросмотр задания remote configuration management.

| Поле | Тип | Описание |
| --- | --- | --- |
| alreadyConfiguredEntitiesCount | integer | Количество сущностей, которые в данный момент сконфигурированы согласно операции remote configuration management. |
| attribute | string | Атрибут, на который влияет операция. Поле может принимать значения: * `group` * `hostGroup` * `hostProperty` * `hostTag` * `networkZone` |
| operation | string | Операция, выполняемая над заданным атрибутом. Поле может принимать значения: * `clear` * `set` |
| targetEntitiesCount | integer | Количество сущностей, которые будут сконфигурированы согласно remote configuration management после его завершения. |
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



"previews": [



{



"alreadyConfiguredEntitiesCount": 1,



"attribute": "networkZone",



"operation": "set",



"targetEntitiesCount": 2,



"value": "exampleNetworkZoneName"



}



]



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