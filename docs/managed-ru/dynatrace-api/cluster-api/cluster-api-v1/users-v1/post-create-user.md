---
title: Create user
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-user
scraped: 2026-05-12T12:13:01.851525
---

# Create user

# Create user

* Published Sep 13, 2021

Этот API-вызов создаёт аккаунт пользователя кластера.

## Аутентификация

Scope `ServiceProviderAPI` (Service Provider API) Api-Token нужен для получения конфигурации password policy realm-а по умолчанию через Dynatrace API. С помощью этого API-метода можно предустановить пароль пользователя, передав значение `passwordClearText`. Это разрешено только если включён соответствующий Feature Flag. Чтобы включить его, обратитесь к Dynatrace product expert через live chat в вашем окружении.

## Endpoint

`/api/v1.0/onpremise/users`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [UserConfig](#openapi-definition-UserConfig) | JSON-тело запроса, содержащее параметры пользователя. | body | Optional |

### Объекты тела запроса

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UserConfig](#openapi-definition-UserConfig) | Успешно создан. |
| **400** | - | Операция не удалась. Некорректный ввод. Возможные причины:  * Не заданы обязательные значения (ID, email, имя, фамилия). * Некорректные данные пользователя. * ID пользователя уже существует. * Email пользователя уже занят. * ID группы пользователей не существует. |
| **403** | - | Операция запрещена — пользователи и группы полностью управляются через LDAP или SSO. |
| **406** | - | Неприемлемый запрос. |
| **522** | - | Не удалось создать пользователя. |
| **523** | - | Пользователь уже существует. |
| **524** | - | Email уже зарегистрирован. |

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

В этом примере добавляется пользователь `john.wicked` и назначается в группу `admins`. В ответ возвращается сохранённое состояние сущности.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/users" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":\"john.wicked\",\"email\":\"john.wicked@company.com\",\"firstName\":\"John\",\"lastName\":\"Wicked\",\"passwordClearText\":null,\"groups\":[\"admin\"]}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/users
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