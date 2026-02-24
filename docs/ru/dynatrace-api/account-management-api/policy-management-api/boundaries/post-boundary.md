---
title: Управление политиками API - POST границы политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary
scraped: 2026-02-24T21:30:43.970469
---

# Управление политиками API - POST границы политики

# Управление политиками API - POST границы политики

* Последнее Dynatrace
* Справочник
* Опубликовано 20 ноября 2025 г.

Создает новую границу политики внутри уровня. Создание глобальной границы политики невозможно, поскольку они управляются Dynatrace.

Запрос использует и производит полезную нагрузку `application/json`.

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Разрешить конфигурацию политики IAM для среды** (`iam-policies-management`) в вашем токене. Чтобы узнать, как получить и использовать его, см. [Клиенты OAuth](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью клиентов OAuth.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | путь | Обязательный |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | JSON тело запроса. Содержит новую границу политики | тело | Обязательный |

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



}



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

Мы рекомендуем проверить полезную нагрузку перед отправкой ее фактическим запросом. Код ответа **200** указывает на действительную полезную нагрузку.

Запрос использует полезную нагрузку `application/json`.

### Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Разрешить конфигурацию политики IAM для среды** (`iam-policies-management`) в вашем токене. Чтобы узнать, как получить и использовать его, см. [Клиенты OAuth](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью клиентов OAuth.").

### Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | путь | Обязательный |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | JSON тело запроса. Содержит новую границу политики | тело | Обязательный |

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

В этом примере запрос создает новую границу политики внутри уровня. Это создает новую границу политики для `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

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



)



],



"metadata": {}



}
```

#### Код ответа

201 - Успешный ответ - граница политики создана.