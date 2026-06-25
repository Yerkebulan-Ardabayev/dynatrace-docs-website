---
title: Update user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-user-groups
scraped: 2026-05-12T12:12:32.982816
---

# Update user group

# Update user group

* Published Sep 13, 2021

Этот API-вызов обновляет группу пользователей кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [GroupConfig](#openapi-definition-GroupConfig) | Тело запроса для обновления существующей группы пользователей. Для обновления группы укажите корректный 'id'; если 'id' не задан, вернётся 'Bad Request'. Попытка изменить имя группы на уже существующее вернёт 'Bad Request'. Попытка обновить несуществующую группу вернёт 'Not Acceptable'. Значение 'isAccessAccount' игнорируется, если 'Dynatrace Platform Subscription' не используется. | body | Optional |

### Объекты тела запроса

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [GroupConfig](#openapi-definition-GroupConfig) | Успешно обновлено |
| **400** | - | Операция не выполнена. Невалидный ввод. Возможные причины:  * Не передана информация о группе для запроса создания группы * Group ID не задан * Имя группы не может быть null или пустым * Хотя бы одно из указанных окружений не существует |
| **406** | - | Not acceptable. Имя группы уже существует или группа не найдена |

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

В этом примере группа пользователей `Sales Group` обновляется так, что привязывается только к LDAP-группе `sales`. У этой группы будет полный доступ к Cluster Management Console и Account Management. В ответ вернётся текущее состояние сущности.

#### Curl

```
curl -X 'PUT' \



'https://myManaged.cluster.com/api/v1.0/onpremise/groups' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"id": "salesgroup",



"name": "Sales Group",



"ldapGroupNames": [



"sales"



]



}



}'
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/groups
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