---
title: Get user groups
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-user-groups
scraped: 2026-05-12T12:12:20.172147
---

# Get user groups

# Get user groups

* Published Sep 13, 2021

Этот API-вызов возвращает информацию о конкретных группах пользователей кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups`

## Параметр

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [GroupConfig[]](#openapi-definition-GroupConfig) | Успех |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `GroupConfig`

Конфигурация группы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accessRight | object | Права доступа |
| id | string | ID группы. Оставьте пустым при создании группы. Заполните при обновлении группы. |
| isAccessAccount | boolean | (применимо только к лицензионной модели Dynatrace Platform Subscription) Если `true`, у группы есть права "Access account". Пользователи такой группы могут заходить в account.dynatrace.com, чтобы видеть утилизацию Dynatrace Platform Subscription и управлять квотами лицензии. |
| isClusterAdminGroup | boolean | Если `true`, у группы есть права "cluster administrator". Пользователи такой группы автоматически получают права администратора во всех окружениях. У них есть доступ к Cluster Management Console, и они могут управлять окружениями мониторинга и Dynatrace Server. Также пользователи групп с этим разрешением могут: добавлять новые ноды Dynatrace Server, обновлять Dynatrace Server, управлять пользователями и группами Dynatrace Managed, устанавливать Dynatrace OneAgent в любое окружение мониторинга, настраивать параметры мониторинга в любом окружении. |
| isManageAccount | boolean | Если `true`, у группы есть права "Edit billing & account info". Пользователи такой группы могут заходить в myaccount.dynatrace.com, чтобы видеть статистику использования продукта, утилизацию лицензии и информацию об аккаунте. |
| ldapGroupNames | string[] | Имена LDAP-групп |
| name | string | Имя группы |
| ssoGroupNames | string[] | Имена SSO-групп. Если задано, используется для маппинга имени SSO-группы на имя группы Dynatrace; иначе маппинг выполняется по имени группы. |

### JSON-модели тела ответа

```
[



{



"accessRight": {},



"id": "string",



"isAccessAccount": true,



"isClusterAdminGroup": true,



"isManageAccount": true,



"ldapGroupNames": [



"string"



],



"name": "string",



"ssoGroupNames": [



"string"



]



}



]
```

## Пример

В этом примере запрашиваются группы пользователей с деталями.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/groups' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP'
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/onpremise/groups
```

#### Тело ответа

```
[



{



"isClusterAdminGroup": true,



"isManageAccount": true,



"isAccessAccount": true,



"id": "owners",



"name": "Owners",



"ldapGroupNames": [



"LDAPM_ClusterBasicAccess"



],



"ssoGroupNames": [],



"accessRight": {}



},



{



"isClusterAdminGroup": false,



"isManageAccount": false,



"isAccessAccount": false,



"id": "mobile",



"name": "TeamPh",



"ldapGroupNames": [



"TeamPh"



],



"ssoGroupNames": [],



"accessRight": {



"VIEWER": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"MANAGE_SETTINGS": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"AGENT_INSTALL": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"LOG_VIEWER": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"VIEW_SENSITIVE_REQUEST_DATA": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"CONFIGURE_REQUEST_CAPTURE_DATA": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"REPLAY_SESSION_DATA": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



]



}



}



]
```

#### Код ответа

`200`