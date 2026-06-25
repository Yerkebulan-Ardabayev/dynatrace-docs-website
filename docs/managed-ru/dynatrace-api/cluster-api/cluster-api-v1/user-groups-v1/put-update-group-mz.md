---
title: Update management zones for user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-group-mz
scraped: 2026-05-12T12:12:45.884962
---

# Update management zones for user group

# Update management zones for user group

* Published Sep 13, 2021

Этот API-вызов обновляет права доступа к management zones для одной группы пользователей.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups/managementZones`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [MzPermissionsForGroup](#openapi-definition-MzPermissionsForGroup) | - | body | Optional |

### Объекты тела запроса

#### Объект `MzPermissionsForGroup`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| groupId | string | ID группы | Optional |
| mzPermissionsPerEnvironment | [MzListForEnvironment[]](#openapi-definition-MzListForEnvironment) | Список прав доступа к management zones по каждому окружению | Optional |

#### Объект `MzListForEnvironment`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| environmentUuid | string | UUID окружения | Optional |
| mzPermissions | [MzPermissionsList[]](#openapi-definition-MzPermissionsList) | Список моделей management zone с правами доступа | Optional |

#### Объект `MzPermissionsList`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| mzId | string | ID нужной management zone | Optional |
| permissions | string[] | Список прав доступа к нужной management zone. Возможные значения: * `DEMO_USER` * `LOG_VIEWER` * `MANAGE_SECURITY_PROBLEMS` * `MANAGE_SETTINGS` * `REPLAY_SESSION_DATA` * `REPLAY_SESSION_DATA_WITHOUT_MASKING` * `VIEWER` * `VIEW_SECURITY_PROBLEMS` * `VIEW_SENSITIVE_REQUEST_DATA` | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успешно обновлено |
| **400** | Переданная модель некорректна или в ней не хватает обязательных элементов |
| **404** | Группа, окружение или management zone не существует |
| **510** | Операция не выполнена |

## Пример

В этом примере группе пользователей `salesgroup` назначаются права доступа к management zones окружения `5c6cf54c-5fe3-47e8-af18-54439090370b`.

#### Curl

```
curl -X 'PUT' \



'https://mymanaged.cluster.com/api/v1.0/onpremise/groups/managementZones' \



-H 'accept: */*' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '{



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



}'
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/groups/managementZones
```

#### Тело ответа

Тело ответа отсутствует

#### Код ответа

`200`