---
title: Environment management API - GET all environments of an account
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/environment-management-api/environment-management-api
scraped: 2026-05-12T11:06:36.171454
---

# Environment management API - GET all environments of an account

# Environment management API - GET all environments of an account

* Reference
* Published Jul 25, 2022

Возвращает список всех окружений и [management zones](/managed/manage/identity-access-management/permission-management/management-zones "Узнайте о концепциях management zones, как их определять и как использовать максимально эффективно.") аккаунта.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/env/v1/accounts/{accountUuid}/environments` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for environment resources** (`account-env-read`). О том, как его получить и использовать.

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** во время создания OAuth client. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EnvironmentResourceDto](#openapi-definition-EnvironmentResourceDto) | Успех. Ответ содержит список окружений аккаунта. |

### Объекты тела ответа

#### Объект `EnvironmentResourceDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| tenantResources | [TenantResourceDto[]](#openapi-definition-TenantResourceDto) | Список окружений в аккаунте. |
| managementZoneResources | [ManagementZoneResourceDto[]](#openapi-definition-ManagementZoneResourceDto) | Список management zones в аккаунте. |

#### Объект `TenantResourceDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя окружения. |
| id | string | ID окружения. |

#### Объект `ManagementZoneResourceDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| parent | string | ID окружения, к которому принадлежит management zone. |
| name | string | Имя management zone. |
| id | string | ID management zone. |

### JSON-модели тела ответа

```
{



"tenantResources": [



{



"name": "string",



"id": "string"



}



],



"managementZoneResources": [



{



"parent": "string",



"name": "string",



"id": "string"



}



]



}
```

## Пример

В этом примере запрос возвращает все окружения и management zones аккаунта с UUID **9ad20784-76c6-4167-bfba-9b0d8d72a71d**.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/env/v1/accounts/9ad20784-76c6-4167-bfba-9b0d8d72a71d/environments' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/env/v1/accounts/9ad20784-76c6-4167-bfba-9b0d8d72a71d/environments
```

#### Тело ответа

```
{



"tenantResources": [



{



"name": "Sample environment",



"id": "mySampleEnv"



},



{



"name": "Sample environment - staging",



"id": "mySampleEnvStaging"



}



],



"managementZoneResources": [



{



"name": "mobile app only",



"id": "154240256445017454",



"parent": "mySampleEnv"



},



{



"name": "load tests only",



"id": "144245256741917454",



"parent": "mySampleEnvStaging"



}



]



}
```

#### Код ответа

200