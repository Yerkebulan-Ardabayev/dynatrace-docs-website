---
title: Управление политиками API - GET границы политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-boundary
scraped: 2026-02-22T21:28:19.984135
---

# Управление политиками API - GET границы политики

# Управление политиками API - GET границы политики

* Latest Dynatrace
* Справка
* Опубликовано 20 ноября 2025 г.

Получает границу политики внутри уровня.

Запрос производит полезную нагрузку `application/json`.

GET

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`) в вашем токене. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | Идентификатор необходимой границы. | path | Обязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательный |

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Успешный ответ - граница политики |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Не найдено. Указанный ресурс не найден. |

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

## Пример

В этом примере запрос извлекает подробную информацию о границе политики с UUID **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** для учетной записи с `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Тело ответа

```
{



"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bndry_teamA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AB\";",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"TEAM-A"



]



)



],



"metadata": {}



}
```

#### Код ответа

200 - Успешный ответ - граница политики.