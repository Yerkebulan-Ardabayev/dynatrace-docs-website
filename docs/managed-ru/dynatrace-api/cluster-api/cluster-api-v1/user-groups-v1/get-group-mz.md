---
title: Get management zones for user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-group-mz
scraped: 2026-05-12T12:12:27.836583
---

# Get management zones for user group

# Get management zones for user group

* Published Sep 13, 2021

Этот API-вызов возвращает информацию о правах доступа к management zones для конкретной группы пользователей.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups/managementZones`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| groupId | string | Path-параметр ID группы. Отсутствие или пустое значение вернёт 'Bad Request'. | path | Required |
| includeEmptyEntries | boolean | Включать ли пустые записи в ответ | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MzPermissionsForGroup](#openapi-definition-MzPermissionsForGroup) | Успех |
| **400** | - | Не передан ID для запроса прав доступа группы к MZ |
| **404** | - | Группа не найдена |

### Объекты тела ответа

#### Объект `MzPermissionsForGroup`

| Элемент | Тип | Описание |
| --- | --- | --- |
| groupId | string | ID группы |
| mzPermissionsPerEnvironment | [MzListForEnvironment[]](#openapi-definition-MzListForEnvironment) | Список прав доступа к management zones по каждому окружению |

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
```

## Пример

Этот API-вызов возвращает информацию о правах доступа к management zones для группы пользователей `salesgroup`.

#### Curl

```
curl -X 'GET' \



'https://mymanaged.cluster.com/api/v1.0/onpremise/groups/managementZones/salesgroup' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token dt0c01.FDAI5YOMUQDKWFTPGON3V7SR.IE7R5J2Q4ZX5G67EKBTW7GT7T2H4GL3O6BV7CT53CCITSSS35PA3HAQDSJGY4C7W'
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/groups/managementZones/salesgroup
```

#### Тело ответа

```
{



"groupId": "salesgroup",



"mzPermissionsPerEnvironment": [



{



"environmentUuid": "5c6cf54c-5fe3-47e8-af18-54439090370b",



"mzPermissions": [



{



"mzId": "-3223778520145835472",



"permissions": [



"REPLAY_SESSION_DATA",



"VIEWER",



"MANAGE_SECURITY_PROBLEMS",



"REPLAY_SESSION_DATA_WITHOUT_MASKING"



]



}



]



}



]



}
```

#### Код ответа

`200`