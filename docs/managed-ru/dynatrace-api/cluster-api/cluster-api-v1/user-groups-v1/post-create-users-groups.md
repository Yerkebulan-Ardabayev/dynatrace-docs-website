---
title: Create user groups
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-users-groups
scraped: 2026-05-12T12:12:31.012772
---

# Create user groups

# Create user groups

* Published Sep 13, 2021

Этот API-вызов создаёт сразу несколько групп пользователей кластера.

## Аутентификация

Для получения настроек политики паролей realm по умолчанию через Dynatrace API API-токену нужен scope `ServiceProviderAPI` (Service Provider API). С этим методом API можно задать пароль пользователя, передав значение `passwordClearText`. Это разрешено только при включённом специальном Feature Flag. Чтобы это сделать, обратитесь к product expert Dynatrace через live chat в вашем окружении.

## Endpoint

`/api/v1.0/onpremise/groups/bulk`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [GroupConfig[]](#openapi-definition-GroupConfig) | - | body | Optional |

### Объекты тела запроса

#### Объект `RequestBody`

#### Объект `GroupConfig`

Конфигурация группы.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accessRight | object | Права доступа | Optional |
| id | string | ID группы. Оставьте пустым при создании группы. Заполните при обновлении группы. | Required |
| isAccessAccount | boolean | (применимо только к лицензионной модели Dynatrace Platform Subscription) Если `true`, у группы есть права "Access account". Пользователи такой группы могут заходить в account.dynatrace.com, чтобы видеть утилизацию Dynatrace Platform Subscription и управлять квотами лицензии. | Optional |
| isClusterAdminGroup | boolean | Если `true`, у группы есть права "cluster administrator". Пользователи такой группы автоматически получают права администратора во всех окружениях. У них есть доступ к Cluster Management Console, и они могут управлять окружениями мониторинга и Dynatrace Server. Также пользователи групп с этим разрешением могут: добавлять новые ноды Dynatrace Server, обновлять Dynatrace Server, управлять пользователями и группами Dynatrace Managed, устанавливать Dynatrace OneAgent в любое окружение мониторинга, настраивать параметры мониторинга в любом окружении. | Required |
| isManageAccount | boolean | Если `true`, у группы есть права "Edit billing & account info". Пользователи такой группы могут заходить в myaccount.dynatrace.com, чтобы видеть статистику использования продукта, утилизацию лицензии и информацию об аккаунте. | Optional |
| ldapGroupNames | string[] | Имена LDAP-групп | Optional |
| name | string | Имя группы | Required |
| ssoGroupNames | string[] | Имена SSO-групп. Если задано, используется для маппинга имени SSO-группы на имя группы Dynatrace; иначе маппинг выполняется по имени группы. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [GroupConfig[]](#openapi-definition-GroupConfig) | Успех |
| **400** | - | Не передана информация о группе для запроса create-group |
| **406** | [GroupConfig[]](#openapi-definition-GroupConfig) | Unacceptable или неполный запрос. Часть групп была добавлена. |

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

В этом примере одним запросом добавляются группы пользователей `Sales Group` и `Developers`. Это задаст их данные и привяжет права доступа к окружениям. В ответ вернётся персистентное состояние сущностей.

#### Curl

```
curl -X 'POST' \



'https://mymanaged.cluster.com/api/v1.0/onpremise/groups/bulk' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '[



{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"name": "Sales Group",



"ldapGroupNames": [



"sales-group"



],



"ssoGroupNames": [



"sales-group"



],



"accessRight": {



"VIEWER": [



"3fcc5d83-d9e5-4bf9-9e00-d997f9c4c63d"



],



"REPLAY_SESSION_DATA": [



"3fcc5d83-d9e5-4bf9-9e00-d997f9c4c63d"



]



}



},



{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"name": "Developers",



"ldapGroupNames": [



"dev-group"



],



"ssoGroupNames": [



"dev-group"



],



"accessRight": {



"VIEWER": [



"3fcc5d83-d9e5-4bf9-9e00-d997f9c4c63d"



]



}



}



]'
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/groups/bulk
```

#### Тело ответа

```
[



{



"isClusterAdminGroup": true,



"isManageAccount": true,



"isAccessAccount": true,



"id": "salesgroup",



"name": "Sales Group",



"ldapGroupNames": [



"sales-group"



],



"ssoGroupNames": [



"sales-group"



],



"accessRight": {}



},



{



"isClusterAdminGroup": true,



"isManageAccount": true,



"isAccessAccount": true,



"id": "developers",



"name": "Developers",



"ldapGroupNames": [



"dev-group"



],



"ssoGroupNames": [



"dev-group"



],



"accessRight": {}



}



]
```

#### Код ответа

`200`