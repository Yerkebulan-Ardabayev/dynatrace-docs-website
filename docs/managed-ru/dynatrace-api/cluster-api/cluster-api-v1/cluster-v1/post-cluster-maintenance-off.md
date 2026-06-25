---
title: Turn off the maintenance of the cluster
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-off
scraped: 2026-05-12T12:12:55.998489
---

# Turn off the maintenance of the cluster

# Turn off the maintenance of the cluster

* Published Sep 29, 2025

Этот API-запрос выключает maintenance кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/cluster/maintenance/off`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [IpMigrationMaintenanceRequestDto](#openapi-definition-IpMigrationMaintenanceRequestDto) | JSON-тело запроса. Содержит базовую информацию о cluster maintenance. | body | Required |

### Объекты тела запроса

#### Объект `IpMigrationMaintenanceRequestDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| nodeId | integer | ID узла, на котором выполняется миграция. | Required |
| reason | string | Причина maintenance. Возможные значения: * `IP_MIGRATION` | Required |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её нужно адаптировать для реального запроса.

```
{



"nodeId": 1,



"reason": "IP_MIGRATION"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Успех. Maintenance выключен. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректный ввод. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-статус код. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

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

#### Тело запроса

```
{



"nodeId": 1,



"reason": "IP_MIGRATION"



}
```

#### Тело ответа

```
{



"error": {



"code": 0,



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

#### Код ответа

200