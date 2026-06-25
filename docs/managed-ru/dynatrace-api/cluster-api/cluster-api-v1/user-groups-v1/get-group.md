---
title: Get user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-group
scraped: 2026-05-12T12:13:03.887148
---

# Get user group

# Get user group

* Published Sep 13, 2021

Этот API-вызов возвращает информацию о конкретной группе пользователей кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| groupId | string | Path-параметр ID группы. Отсутствие или пустое значение вернёт 'Bad Request'. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [GroupConfig](#openapi-definition-GroupConfig) | Успех |
| **400** | - | Не передан ID для запроса get group |
| **404** | - | Не найдено |

### Объекты тела ответа

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
```

## Пример

В этом примере запрашиваются детали группы пользователей `salesgroup`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/groups/salesgroup" -H  "accept: application/json" -H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP'
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/groups/salesgroup
```

#### Тело ответа

```
{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"id": "salesgroup",



"name": "Sales Group",



"ldapGroupNames": [



"sales"



]



}
```

#### Код ответа

`200`