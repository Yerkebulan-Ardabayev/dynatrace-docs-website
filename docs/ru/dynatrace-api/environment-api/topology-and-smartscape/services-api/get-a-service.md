---
title: Services API - GET a service
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service
scraped: 2026-03-05T21:27:06.244954
---

# Services API — получение сервиса

# Services API — получение сервиса

* Справочник
* Обновлено 22 марта 2023 г.
* Устарело

Этот API устарел. Используйте вместо него [API мониторируемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте об API мониторируемых сущностей Dynatrace."). Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Перенесите вашу автоматизацию на API мониторируемых сущностей.").

Получает параметры указанного сервиса.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace для запрашиваемого сервиса. | path | Обязательный |

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
| agentTechnologyType | string | -Элемент может содержать следующие значения: * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | Сервисы системы акторов Akka. |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | Пользовательское имя сущности |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace для запрашиваемой сущности. |
| esbApplicationName | string | Имя приложения ESB. |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности в миллисекундах UTC |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | URL шлюза IBM CTG. |
| ibmCtgServerName | string | Имя IBM CICS Transaction Gateway. |
| iibApplicationName | string | Имя приложения IIB. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, к которым принадлежит сущность. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Публичное доменное имя. |
| remoteEndpoint | string | Конечная точка удалённого сервиса. |
| remoteServiceName | string | Имя удалённого сервиса. |
| serviceDetectionAttributes | object | Атрибуты, участвующие в определении идентификатора сервиса. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -Элемент может содержать следующие значения: * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | Идентификатор сущности Dynatrace. |
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
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Для пользовательских тегов здесь содержится значение тега. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

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
| parameterLocation | string | -Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



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

В этом примере запрос получает данные сервиса **PHP-FPM via domain socket /run/php7-fpm.sock** с идентификатором **SERVICE-72503CBDD2AEF066**.

Токен API передаётся в заголовке **Authorization**.

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

* [Сервисы](/docs/observe/application-observability/services "Узнайте, как мониторить и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")