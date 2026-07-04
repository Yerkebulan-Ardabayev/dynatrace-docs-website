---
title: "List Cluster token metadata with id"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-para
updated: 2026-02-09
---

Этот API-вызов возвращает метаданные Dynatrace Cluster token по ID токена.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/tokens`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного токена. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Запрошенный токен не найден. |

### Объекты тела ответа

#### Объект `TokenMetadata`

Метаданные токена.

| Элемент | Тип | Описание |
| --- | --- | --- |
| created | integer | Время создания как unix timestamp в миллисекундах. |
| expires | integer | Время истечения как unix timestamp в миллисекундах. |
| id | string | ID токена. |
| lastUse | integer | Unix timestamp в миллисекундах, когда токен был использован последний раз. |
| name | string | Имя токена. |
| personalAccessToken | boolean | Токен является [personal access token](https://dt-url.net/wm03sop) (`true`) или API-токеном (`false`). |
| revoked | boolean | Статус отзыва токена. Отозванные токены отключены. |
| scopes | string[] | Список scope'ов, назначенных токену. Возможные значения: * `ClusterTokenManagement` * `ControlManagement` * `DiagnosticExport` * `EnvironmentTokenManagement` * `ExternalSyntheticIntegration` * `Nodekeeper` * `ReadSyntheticData` * `ServiceProviderAPI` * `UnattendedInstall` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `apiTokens.read` * `apiTokens.write` * `settings.read` * `settings.write` |
| userId | string | Владелец токена. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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


"created": 1554076800000,


"expires": 1585976400000,


"id": "acbed0c4-4ef1-4303-991f-102510a69322",


"lastUse": 1554354000000,


"name": "myToken",


"personalAccessToken": true,


"revoked": true,


"scopes": [


"DataExport",


"ReadConfig",


"WriteConfig"


],


"userId": "john.smith"


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

В этом примере запрос возвращает метаданные токена с ID `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4"


-H  "accept: application/json; charset=utf-8"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4
```

#### Тело ответа

```
{


"id": "4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4",


"name": "myToken",


"userId": "john.smith",


"revoked": true,


"created": 1554076800000,


"expires": 1585976400000,


"lastUse": 1554354000000,


"scopes": [


"DataExport",


"ReadConfig",


"WriteConfig"


]


}
```

#### Код ответа

`204`
