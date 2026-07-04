---
title: "Create new Cluster token"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens
updated: 2026-02-09
---

Этот API-вызов создаёт новый cluster token.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

Создаёт новый Dynatrace Cluster token. Ответ содержит созданный токен.

Запрос принимает и возвращает payload `application/json`.

## Endpoint

`/api/cluster/v2/tokens`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CreateToken](#openapi-definition-CreateToken) | JSON-тело запроса. Содержит параметры нового токена. | body | Required |

### Объекты тела запроса

#### Объект `CreateToken`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| expiresIn | [Duration](#openapi-definition-Duration) | Определяет промежуток времени. | Optional |
| name | string | Имя токена. | Required |
| scopes | string[] | Список scope'ов, назначаемых токену.  * `DiagnosticExport`: DiagnosticExport. * `ControlManagement`: ControlManagement. * `UnattendedInstall`: UnattendedInstall. * `ServiceProviderAPI`: Service Provider API. * `ExternalSyntheticIntegration`: Создание и чтение synthetic monitors, locations и nodes. * `ClusterTokenManagement`: Cluster token management. * `ReadSyntheticData`: Чтение synthetic monitors, locations и nodes. * `Nodekeeper`: Доступ Nodekeeper для управления нодами. * `EnvironmentTokenManagement`: Создание токенов "Token Management" для существующих окружений. * `activeGateTokenManagement.read`: Чтение ActiveGate-токенов. * `activeGateTokenManagement.create`: Создание ActiveGate-токенов. * `activeGateTokenManagement.write`: Запись ActiveGate-токенов. * `settings.read`: Чтение настроек. * `settings.write`: Запись настроек. * `apiTokens.read`: Чтение API-токенов. * `apiTokens.write`: Запись API-токенов. Возможные значения: * `DiagnosticExport` * `ControlManagement` * `UnattendedInstall` * `ServiceProviderAPI` * `ExternalSyntheticIntegration` * `ClusterTokenManagement` * `ReadSyntheticData` * `Nodekeeper` * `EnvironmentTokenManagement` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `settings.read` * `settings.write` * `apiTokens.read` * `apiTokens.write` | Required |

#### Объект `Duration`

Определяет промежуток времени.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| unit | string | Единица времени.  Если не задана, используется миллисекунда. Возможные значения: * `DAYS` * `HOURS` * `MILLIS` * `MINUTES` * `SECONDS` | Optional |
| value | integer | Количество времени. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{


"expiresIn": {


"unit": "DAYS",


"value": 1


},


"name": "string",


"scopes": [


"DiagnosticExport"


]


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [Token](#openapi-definition-Token) | Успех. Токен создан. Тело ответа содержит сам токен. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. Тело ответа содержит детали. |

### Объекты тела ответа

#### Объект `Token`

| Элемент | Тип | Описание |
| --- | --- | --- |
| token | string | Аутентификационный токен Dynatrace API. |

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


"token": "abcdefjhij1234567890"


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

В этом примере запрос создаёт новый токен с именем `Mytoken`, действительный 24 часа. С этим токеном можно выполнить diagnostic export (`DiagnosticExport`) и unattended install (`UnattendedInstall`).

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/tokens"


-H "accept: application/json; charset=utf-8"


-H "Content-Type: application/json; charset=utf-8"


-d "{  \"name\": \"MyToken\",  \"scopes\": [    \"DiagnosticExport\",    \"UnattendedInstall\"  ],  \"expiresIn\": {    \"value\": 24,    \"unit\": \"HOURS\"  }}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/tokens
```

#### Тело запроса

```
{


"name": "MyToken",


"scopes": ["DiagnosticExport", "UnattendedInstall"],


"expiresIn": {


"value": 24,


"unit": "HOURS"


}


}
```

#### Тело ответа

```
{


"token": "abcdefjhij1234567890"


}
```

#### Код ответа

`201`
