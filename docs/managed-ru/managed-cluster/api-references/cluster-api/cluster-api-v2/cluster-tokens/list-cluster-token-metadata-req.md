---
title: "List Cluster token metadata with request"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-req
updated: 2026-02-09
---

Этот API-вызов возвращает метаданные Dynatrace Cluster token по значению токена. Запрос принимает и возвращает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/tokens/lookup`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [Token](#openapi-definition-Token) | JSON-тело запроса. Содержит нужный токен. | body | Required |

### Объекты тела запроса

#### Объект `Token`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| token | string | Аутентификационный токен Dynatrace API. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{


"token": "abcdefjhij1234567890"


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Успех |

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

## Пример

В этом примере запрос возвращает метаданные токена `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/tokens/lookup"


-H  "accept: application/json; charset=utf-8"


-H  "Content-Type: application/json; charset=utf-8"


-d  "{  \"token\": \"abcdefjhij1234567890\"}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/tokens/lookup
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

`200`
