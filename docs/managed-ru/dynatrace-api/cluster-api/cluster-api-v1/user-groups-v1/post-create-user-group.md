---
title: Create user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-user-group
scraped: 2026-05-12T12:12:49.149039
---

# Create user group

# Create user group

* Published Sep 13, 2021

Этот API-вызов создаёт группу пользователей кластера.

## Аутентификация

Для получения настроек политики паролей realm по умолчанию через Dynatrace API API-токену нужен scope `ServiceProviderAPI` (Service Provider API). С этим методом API можно задать пароль пользователя, передав значение `passwordClearText`. Это разрешено только при включённом специальном Feature Flag. Чтобы это сделать, обратитесь к product expert Dynatrace через live chat в вашем окружении.

## Endpoint

`/api/v1.0/onpremise/groups`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [GroupConfig](#openapi-definition-GroupConfig) | Тело запроса для создания новой группы пользователей. Для создания группы оставьте 'id' пустым; если передать 'id', вернётся 'Bad Request'. Попытка создать группу с уже существующим именем вернёт 'Not Acceptable'. Значение 'isAccessAccount' игнорируется, если 'Dynatrace Platform Subscription' не используется. | body | Optional |

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
| **400** | - | Операция не выполнена. Невалидный ввод. Возможные причины:  * Не передана информация о группе для запроса создания группы * Group ID не должен задаваться * Имя группы не может быть null или пустым * Хотя бы одно из указанных окружений не существует |
| **406** | - | Not acceptable. Группа уже существует |

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

В этом примере создаётся группа пользователей `Sales Group`, привязанная только к LDAP-группе `sales`. У этой группы будет полный доступ к Cluster Management Console и Account Management. В ответ вернётся текущее состояние сущности и сгенерированный ID.

#### Curl

```
curl -X 'POST' \



'https://myManaged.cluster.com/api/v1.0/onpremise/groups' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"id": "",



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