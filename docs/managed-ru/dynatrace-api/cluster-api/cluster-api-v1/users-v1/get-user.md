---
title: Get user
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-user
scraped: 2026-05-12T12:12:14.511582
---

# Get user

# Get user

* Published Sep 13, 2021

Этот API-вызов возвращает информацию о конкретном пользователе кластера.

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
| **200** | [UserConfig](#openapi-definition-UserConfig) | Успех |
| **400** | - | Не передан ID для запроса get-user. |
| **404** | - | Не найдено. |

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

В этом примере запрашиваются детали пользователя `john.wicked`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/users/john.wicked" -H  "accept: application/json"
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