---
title: Управление политиками API - POST граница политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary
scraped: 2026-02-22T21:24:06.310938
---

# Управление политиками API - POST граница политики

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Создает новую границу политики внутри уровня. Вы не можете создать глобальную границу политики, поскольку они управляются Dynatrace.

Запрос потребляет и производит полезную нагрузку `application/json`.

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries`

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`) назначенное вашему токену. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательный |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | JSON тело запроса. Содержит новую границу политики | body | Обязательный |

### Объекты тела запроса

#### Объект `PolicyBoundaryDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Отображаемое имя границы политики. | Обязательный |
| boundaryQuery | string | Запрос границы политики. | Обязательный |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. | Обязательный |

#### Объект `Map`

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Ее необходимо скорректировать для использования в фактическом запросе.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Успешный ответ - граница политики создана |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Неудача. Запрос недействителен |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Неудача. Указанный ресурс не найден. |

### Объекты тела ответа

#### Объект `PolicyBoundaryOverview`

| Элемент | Тип | Описание |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | Отображаемое имя границы политики. |
| boundaryQuery | string | Запрос границы политики. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. |

#### Объект `Condition`

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя условия.  Оно указывает, какая часть **сервисов** проверяется условием. |
| operator | string | Оператор условия. |
| values | string[] | Список ссылочных значений условия. |

#### Объект `Map`

#### Объект `ErrorDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки. |
| message | string | Краткое описание ошибки. |
| errorsMap | object | - |

### Модели тела ответа JSON

```
{



"uuid": "string",



"levelType": "string",



"levelId": "string",



"name": "string",



"boundaryQuery": "string",



"boundaryConditions": [



{



"name": "string",



"operator": "string",



"values": [



"string"



]



)



],



"metadata": {}



}
```

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Проверка полезной нагрузки

Мы рекомендуем проверить полезную нагрузку перед отправкой ее с фактическим запросом. Код ответа **200** указывает на действительную полезную нагрузку.

Запрос потребляет полезную нагрузку `application/json`.

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/validation`

### Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`) назначенное вашему токену. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

### Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательный |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | JSON тело запроса. Содержит новую границу политики | body | Обязательный |

### Объекты тела запроса

#### Объект `PolicyBoundaryDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Отображаемое имя границы политики. | Обязательный |
| boundaryQuery | string | Запрос границы политики. | Обязательный |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. | Обязательный |

#### Объект `Map`

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Ее необходимо скорректировать для использования в фактическом запросе.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Пример

В этом примере запрос создает новую границу политики внутри уровня. Это новая граница политики для `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request POST \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries \



--header 'accept: application/json' \



--header 'Authorization: Bearer abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "name_string",



"boundaryQuery": "boundaryQuery",



"metadata": {}



}'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries
```

#### Тело запроса

```
{



"name": "bnd_teamAA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AA\";",



"metadata": {}



}
```

#### Тело ответа

```
{



"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd_teamAA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AA\";",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"TEAM-AA"



]



}



],



"metadata": {}



}
```

#### Код ответа

201 - Успешный ответ - граница политики создана.