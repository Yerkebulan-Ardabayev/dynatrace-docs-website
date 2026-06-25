---
title: Create cluster user accounts
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-users
scraped: 2026-05-12T12:12:39.936973
---

# Create cluster user accounts

# Create cluster user accounts

* Published Sep 13, 2021

Этот API-вызов создаёт несколько аккаунтов пользователей кластера за один раз.

## Аутентификация

Scope `ServiceProviderAPI` (Service Provider API) Api-Token нужен для получения конфигурации password policy realm-а по умолчанию через Dynatrace API. С помощью этого API-метода можно предустановить пароль пользователя, передав значение `passwordClearText`. Это разрешено только если включён соответствующий Feature Flag. Чтобы включить его, обратитесь к Dynatrace product expert через live chat в вашем окружении.

## Endpoint

`/api/v1.0/onpremise/users/bulk`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [UserConfig[]](#openapi-definition-UserConfig) | JSON-тело запроса, содержащее параметры пользователей. | body | Optional |

### Объекты тела запроса

#### Объект `RequestBody`

#### Объект `UserConfig`

Конфигурация пользователя.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| email | string | Email пользователя. | Required |
| firstName | string | Имя пользователя. | Required |
| groups | string[] | Список ID групп пользователя. | Optional |
| id | string | ID пользователя. | Required |
| lastName | string | Фамилия пользователя. | Required |
| passwordClearText | string | Пароль пользователя в открытом виде; используется только для задания начального пароля. | Optional |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её нужно адаптировать для реального запроса.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UserConfig[]](#openapi-definition-UserConfig) | Успех |
| **400** | - | Операция не удалась. Некорректный ввод. Возможные причины:  * Не получены данные пользователей для запроса create-users. * Не заданы обязательные значения (ID, email, имя, фамилия). * Некорректные данные пользователя. * Ввод содержит дубликаты ID. * Ввод содержит дубликаты email. * ID пользователя уже существует. * Email пользователя уже занят. * ID группы пользователей не существует. |
| **403** | - | Операция запрещена — включена интеграция с LDAP или SSO с назначением групп. |
| **406** | [UserConfig[]](#openapi-definition-UserConfig) | Неприемлемый или неполный запрос. Часть пользователей добавлена. |

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

В этом примере добавляются два пользователя — `john.wicked` и `ann.brown` — за один запрос. Это задаёт их данные и индивидуальное членство в группах. В ответ возвращается сохранённое состояние сущностей.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/v1.0/onpremise/users/bulk" -H  "accept: application/json" -H  "Content-Type: application/json" -d "[{\"id\":\"john.wicked\",\"email\":\"john.wicked@company.com\",\"firstName\":\"John\",\"lastName\":\"Wicked\",\"passwordClearText\":null,\"groups\":[\"owners\",\"users\"]},{\"id\":\"anne.brown\",\"email\":\"anne.brown@company.com\",\"firstName\":\"Anne\",\"lastName\":\"Brown\",\"passwordClearText\":null,\"groups\":[\"users\"]}]"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/users/bulk
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