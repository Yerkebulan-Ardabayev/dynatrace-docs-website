---
title: Applications API - GET an application
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app
scraped: 2026-05-12T12:01:37.095843
---

# Applications API - GET an application

# Applications API - GET an application

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.

Получает параметры указанного приложения.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | ID сущности Dynatrace для нужного приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Application](#openapi-definition-Application) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Application`

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationMatchTarget | string | -Возможные значения: * `DOMAIN` * `URL` |
| applicationType | string | -Возможные значения: * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| attributes | object | - |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace в том виде, как оно отображается в UI. |
| entityId | string | ID сущности Dynatrace для нужной сущности. |
| firstSeenTimestamp | integer | Метка времени, когда сущность была впервые обнаружена, в миллисекундах UTC |
| fromRelationships | object | Список исходящих вызовов от приложения. |
| lastSeenTimestamp | integer | Метка времени, когда сущность была обнаружена в последний раз, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Management zone'ы, частью которых является сущность. |
| ruleAppliedMatchType | string | -Возможные значения: * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | Список входящих вызовов к приложению. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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



"applicationMatchTarget": "DOMAIN",



"applicationType": "AGENTLESS_MONITORING",



"attributes": {



"empty": true



},



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



]



},



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"ruleAppliedMatchType": "ALL_URLS_AND_DOMAINS",



"ruleAppliedPattern": "string",



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"monitors": [



"string"



]



}



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

В этом примере запрос запрашивает свойства приложения **easyTravel Demo**, у которого ID **MOBILE\_APPLICATION-752C288D59734C79**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79
```

#### Тело ответа

```
{



"entityId": "MOBILE_APPLICATION-752C288D59734C79",



"displayName": "easyTravel Demo",



"customizedName": "easyTravel Demo",



"discoveredName": "752c288d-5973-4c79-b7d1-3a49d4d42ea0",



"firstSeenTimestamp": 1469613941393,



"lastSeenTimestamp": 1538656560201,



"tags": [



{



"context": "CONTEXTLESS",



"key": "portal"



},



{



"context": "CONTEXTLESS",



"key": "easyTravel"



}



],



"fromRelationships": {



"calls": [



"SERVICE-ED0B103392AC86BF"



]



},



"toRelationships": {},



"mobileOsFamily": [



"ANDROID",



"IOS",



"WINDOWS"



],



"managementZones": [



{



"id": "-6239538939987181652",



"name": "allTypes"



},



{



"id": "6518151499932123858",



"name": "mobile app name exists"



},



{



"id": "-4085081632192243904",



"name": "easyTravel"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")