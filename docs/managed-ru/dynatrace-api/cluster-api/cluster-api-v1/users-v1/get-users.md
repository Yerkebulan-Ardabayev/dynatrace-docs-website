---
title: Get users
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-users
scraped: 2026-05-12T12:12:50.359018
---

# Get users

# Get users

* Published Sep 13, 2021

Этот API-вызов возвращает список пользователей, существующих в кластере.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/users`

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UserConfig[]](#openapi-definition-UserConfig) | Успех |

### Объекты тела ответа

#### Объект `ResponseBody`

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
[



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



]
```

## Пример

В этом примере запрашиваются все пользователи Dynatrace Managed кластера. По каждому пользователю возвращается подробная информация и членство в группах.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/users" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/users
```

#### Тело ответа

```
[



{



"id": "john.wicked",



"email": "john.wicked@company.com",



"firstName": "John",



"lastName": "Wicked",



"passwordClearText": null,



"groups": [



"owners",



"users"



]



},



{



"id": "anne.brown",



"email": "anne.brown@company.com",



"firstName": "Anne",



"lastName": "Brown",



"passwordClearText": null,



"groups": ["users"]



}



]
```

#### Код ответа

`200`