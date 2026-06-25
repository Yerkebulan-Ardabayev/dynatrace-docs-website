---
title: Update Cluster token
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/update-cluster-token
scraped: 2026-05-12T11:06:07.279909
---

# Update Cluster token

# Update Cluster token

* Published Feb 12, 2020

Этот API-вызов обновляет указанный Dynatrace Cluster token. Можно:

* Изменить имя токена.
* Отозвать токен.
  Отозванный токен остаётся в окружении, но использовать его нельзя.
* Изменить scope токена.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID токена для обновления.  Нельзя обновить токен, который используется для аутентификации запроса. | path | Required |
| body | [UpdateToken](#openapi-definition-UpdateToken) | JSON-тело запроса. Содержит обновлённые параметры токена. | body | Required |

### Объекты тела запроса

#### Объект `UpdateToken`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя токена. | Optional |
| revoked | boolean | Токен отозван (`true`) или активен (`false`). | Optional |
| scopes | string[] | Список разрешений, назначенных токену.  Кроме новых разрешений, нужно передать также существующие разрешения, которые надо сохранить. Любое существующее разрешение, отсутствующее в payload, будет отозвано.  * `DiagnosticExport`: DiagnosticExport. * `ControlManagement`: ControlManagement. * `UnattendedInstall`: UnattendedInstall. * `ServiceProviderAPI`: Service Provider API. * `ExternalSyntheticIntegration`: Создание и чтение synthetic monitors, locations и nodes. * `ClusterTokenManagement`: Cluster token management. * `ReadSyntheticData`: Чтение synthetic monitors, locations и nodes. * `Nodekeeper`: Доступ Nodekeeper для управления нодами. * `EnvironmentTokenManagement`: Создание токенов "Token Management" для существующих окружений. * `activeGateTokenManagement.read`: Чтение ActiveGate-токенов. * `activeGateTokenManagement.create`: Создание ActiveGate-токенов. * `activeGateTokenManagement.write`: Запись ActiveGate-токенов. * `settings.read`: Чтение настроек. * `settings.write`: Запись настроек. * `apiTokens.read`: Чтение API-токенов. * `apiTokens.write`: Запись API-токенов. Возможные значения: * `DiagnosticExport` * `ControlManagement` * `UnattendedInstall` * `ServiceProviderAPI` * `ExternalSyntheticIntegration` * `ClusterTokenManagement` * `ReadSyntheticData` * `Nodekeeper` * `EnvironmentTokenManagement` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `settings.read` * `settings.write` * `apiTokens.read` * `apiTokens.write` | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"name": "string",



"revoked": true,



"scopes": [



"DiagnosticExport"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Токен обновлён. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Нельзя обновить токен, который используется для аутентификации запроса. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Запрошенный токен не найден. |

### Объекты тела ответа

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

В этом примере запрос обращается к метаданным конкретного токена с ID `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`. Он меняет scope токена через обновление метаданных. Имя и срок действия токена остаются прежними. Код ответа 204 означает успешное обновление.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4"



-H  "accept: application/json; charset=utf-8"



-H  "Content-Type: application/json; charset=utf-8"



-d  "{  \"revoked\": \"true\",  \"name\": \"updated token\",  \"scopes\": [    \"UnattendedInstall\"  ]}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4
```

#### Тело запроса

```
{



"revoked": "true",



"name": "updated token",



"scopes": ["UnattendedInstall"]



}
```

#### Код ответа

`204`