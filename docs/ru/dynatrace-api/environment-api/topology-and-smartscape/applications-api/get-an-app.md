---
title: Applications API - GET an application
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app
scraped: 2026-03-05T21:27:16.489433
---

# Applications API - GET an application

# Applications API - GET an application

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API является устаревшим. Вместо него используйте [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API."). Дополнительную информацию о переходе на новый API см. в [руководстве по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Перенесите вашу автоматизацию на Monitored entities API.").

Получает параметры указанного приложения.

Запрос формирует ответ в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace требуемого приложения. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Application](#openapi-definition-Application) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Application`

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationMatchTarget | string | -Элемент может содержать следующие значения: * `DOMAIN` * `URL` |
| applicationType | string | -Элемент может содержать следующие значения: * `AGENTLESS_MONITORING` * `AUTO_INJECTED` * `DEFAULT` * `SAAS_VENDOR` |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace требуемой сущности. |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности, в миллисекундах UTC |
| fromRelationships | object | Список исходящих вызовов из приложения. |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, к которым принадлежит сущность. |
| ruleAppliedMatchType | string | -Элемент может содержать следующие значения: * `ALL_URLS_AND_DOMAINS` * `CONTAINS` * `ENDS` * `EQUALS` * `MATCHES` * `STARTS` |
| ruleAppliedPattern | string | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | Список входящих вызовов к приложению. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | Идентификатор сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Пользовательские теги содержат значение тега здесь. |
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



"applicationMatchTarget": "DOMAIN",



"applicationType": "AGENTLESS_MONITORING",



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

В этом примере запрос запрашивает свойства приложения **easyTravel Demo**, которое имеет идентификатор **MOBILE\_APPLICATION-752C288D59734C79**.

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

* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
