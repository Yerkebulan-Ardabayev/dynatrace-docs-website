---
title: Get management zones for user groups
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-groups-mz
scraped: 2026-05-12T12:12:59.431245
---

# Get management zones for user groups

# Get management zones for user groups

* Published Sep 13, 2021

Этот API-вызов возвращает информацию о правах доступа к management zone для всех групп пользователей.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups/managementZones`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| includeEmptyEntries | boolean | Включать ли пустые записи в ответ | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MzPermissionsForGroup[]](#openapi-definition-MzPermissionsForGroup) | Успех |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `MzPermissionsForGroup`

| Элемент | Тип | Описание |
| --- | --- | --- |
| groupId | string | ID группы |
| mzPermissionsPerEnvironment | [MzListForEnvironment[]](#openapi-definition-MzListForEnvironment) | Список прав доступа к management zone по каждому окружению |

#### Объект `MzListForEnvironment`

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentUuid | string | UUID окружения |
| mzPermissions | [MzPermissionsList[]](#openapi-definition-MzPermissionsList) | Список моделей management zone с правами доступа |

#### Объект `MzPermissionsList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| mzId | string | ID нужной management zone |
| permissions | string[] | Список прав доступа к нужной management zone. Возможные значения: * `DEMO_USER` * `LOG_VIEWER` * `MANAGE_SECURITY_PROBLEMS` * `MANAGE_SETTINGS` * `REPLAY_SESSION_DATA` * `REPLAY_SESSION_DATA_WITHOUT_MASKING` * `VIEWER` * `VIEW_SECURITY_PROBLEMS` * `VIEW_SENSITIVE_REQUEST_DATA` |

### JSON-модели тела ответа

```
[



{



"groupId": "string",



"mzPermissionsPerEnvironment": [



{



"environmentUuid": "string",



"mzPermissions": [



{



"mzId": "string",



"permissions": [



"DEMO_USER"



]



}



]



}



]



}



]
```

## Пример

В этом примере запрашиваются management zones для всех групп пользователей.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/groups/managementZones' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP'
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/onpremise/groups/managementZones
```

#### Тело ответа

```
[



{



"groupId": "aaa",



"mzPermissionsPerEnvironment": [



{



"environmentUuid": "4667c7df-c41a-800a-2c81-3c789c24faac",



"mzPermissions": []



},



{



"environmentUuid": "702822e6-c4d5-98b6-68f0-2fa6e916d83a",



"mzPermissions": [



{



"mzId": "1082937102825552837",



"permissions": []



},



{



"mzId": "3256863855844402130",



"permissions": []



},



{



"mzId": "9010752233197751135",



"permissions": []



},



{



"mzId": "6704521539267660126",



"permissions": []



},



{



"mzId": "9988288124425157928",



"permissions": []



},



{



"mzId": "3762222045561554923",



"permissions": []



}



]



},



{



"environmentUuid": "ff484b4b-4391-109e-429f-ce16dac3325a",



"mzPermissions": []



},



{



"environmentUuid": "a3d7fa42-a74d-ebd6-8aee-003b6c2abd6f",



"mzPermissions": []



},



{



"environmentUuid": "75188d7f-4e59-d4d3-c1ab-cb6eb5a095b8",



"mzPermissions": [



{



"mzId": "3695265796834015735",



"permissions": []



}



]



},



{



"environmentUuid": "560db49c-c2f5-8d41-3811-1623e4c4dd17",



"mzPermissions": []



},



{



"environmentUuid": "96cfb5d9-94e9-e5a3-96e6-b4ecced9f0ec",



"mzPermissions": []



},



{



"environmentUuid": "7e6cb304-79c5-6b90-9168-60f16deb1b00",



"mzPermissions": [



{



"mzId": "6978718201709411367",



"permissions": []



},



{



"mzId": "1884001224662458062",



"permissions": []



}



]



}



]



}



]
```

#### Код ответа

`200`