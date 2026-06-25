---
title: Delete user
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/delete-user
scraped: 2026-05-12T12:12:34.930433
---

# Delete user

# Delete user

* Published Sep 13, 2021

Этот API-вызов удаляет пользователя кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/users`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Path-параметр ID пользователя. Отсутствие или пустое значение вернёт 'Bad Request'. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UserConfig](#openapi-definition-UserConfig) | Успешно удалён. |
| **304** | - | Не изменено. |
| **400** | - | Не передан ID для запроса delete-user. |
| **406** | - | Неприемлемый запрос. |

### Объекты тела ответа

#### Объект `UserConfig`

Конфигурация пользователя.

| Элемент | Тип | Описание |
| --- | --- | --- |
| email | string | Email пользователя. |
| firstName | string | Имя пользователя. |
| groups | string[] | Список ID групп пользователя. |
| id | string | ID пользователя. |
| lastName | string | Фамилия пользователя. |
| passwordClearText | string | Пароль пользователя в открытом виде; используется только для задания начального пароля. |

### JSON-модели тела ответа

```
{



"email": "string",



"firstName": "string",



"groups": [



"string"



],



"id": "string",



"lastName": "string",



"passwordClearText": "string"



}
```

## Пример

В этом примере удаляется аккаунт пользователя `john.wicked`. Если аккаунт удалён, в ответ возвращаются детали удалённого пользователя. Если пользователь был удалён ранее, возвращается пустой payload с кодом `200`.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/v1.0/onpremise/users/john.wicked" -H  "accept: application/json"
```

#### URL запроса

```
https://mymanaged.cluster.com/api/v1.0/onpremise/users/john.wicked
```

#### Тело ответа

```
{



"id": "john.wicked",



"email": "john.wicked@company.com",



"firstName": "John",



"lastName": "Wicked",



"passwordClearText": null,



"groups": [



"admin"



]



}
```

#### Код ответа

`200`