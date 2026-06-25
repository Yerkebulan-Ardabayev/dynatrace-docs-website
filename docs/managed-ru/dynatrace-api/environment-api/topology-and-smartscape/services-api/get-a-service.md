---
title: Services API - GET a service
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service
scraped: 2026-05-12T12:02:06.716545
---

# Services API - GET a service

# Services API - GET a service

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.

Получает параметры указанного сервиса.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | ID сущности Dynatrace для нужного сервиса. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Service](#openapi-definition-Service) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Service`

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentTechnologyType | string | -Возможные значения: * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | Сервисы системы акторов akka. |
| attributes | object | - |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | Пользовательское имя сущности |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace в том виде, как оно отображается в UI. |
| entityId | string | ID сущности Dynatrace для нужной сущности. |
| esbApplicationName | string | Имя ESB-приложения. |
| firstSeenTimestamp | integer | Метка времени, когда сущность была впервые обнаружена, в миллисекундах UTC |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | URL шлюза IBM CTG. |
| ibmCtgServerName | string | Имя IBM CICS Transaction Gateway. |
| iibApplicationName | string | Имя IIB-приложения. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | Метка времени, когда сущность была обнаружена в последний раз, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Management zone'ы, частью которых является сущность. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Публичное доменное имя. |
| remoteEndpoint | string | Endpoint удалённого сервиса. |
| remoteServiceName | string | Имя удалённого сервиса. |
| serviceDetectionAttributes | object | Атрибуты, повлиявшие на service id. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -Возможные значения: * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TechnologyInfo`

| Элемент | Тип | Описание |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



"attributes": {



"empty": true



},



"className": "string",



"contextRoot": "string",



"customizedName": "string",



"databaseHostNames": [



"string"



],



"databaseName": "string",



"databaseVendor": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esbApplicationName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



],



"runsOn": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"ibmCtgGatewayUrl": "string",



"ibmCtgServerName": "string",



"iibApplicationName": "string",



"ipAddresses": [



"string"



],



"isExternalService": true,



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"path": "string",



"port": 1,



"publicDomainName": {},



"remoteEndpoint": "string",



"remoteServiceName": "string",



"serviceDetectionAttributes": {},



"serviceTechnologyTypes": [



"string"



],



"serviceType": "Cics",



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"calls": [



"string"



]



},



"webApplicationId": "string",



"webServerName": "string",



"webServiceName": "string",



"webServiceNamespace": "string"



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

## Пример

В этом примере запрос получает детали сервиса **PHP-FPM via domain socket /run/php7-fpm.sock**, у которого ID **SERVICE-72503CBDD2AEF066**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services/SERVICE-72503CBDD2AEF066
```

#### Тело ответа

```
{



"entityId": "SERVICE-72503CBDD2AEF066",



"displayName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"discoveredName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"firstSeenTimestamp": 1505902015554,



"lastSeenTimestamp": 1546010106998,



"tags": [],



"fromRelationships": {



"runsOnProcessGroupInstance": [



"PROCESS_GROUP_INSTANCE-9BA70456D770536E",



"PROCESS_GROUP_INSTANCE-7E988C3503AE8803"



],



"runsOn": [



"PROCESS_GROUP-E5C3CC7EC1F80B5B"



]



},



"toRelationships": {



"calls": [



"SERVICE-5304CCF4AFBFF35E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest",



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")