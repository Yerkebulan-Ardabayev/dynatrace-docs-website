---
title: Управление политиками API - GET все границы политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-all-boundaries
scraped: 2026-02-20T21:21:25.629547
---

# Управление политиками API - GET все границы политики

# Управление политиками API - GET все границы политики

* Последнее Dynatrace
* Справочник
* Опубликовано 20 ноября 2025 г.

Получает список границ политики внутри уровня.

Запрос производит полезную нагрузку `application/json`.

GET

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries`

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Разрешить конфигурацию политики IAM для среды** (`iam-policies-management`) в вашем токене. Чтобы узнать, как получить и использовать его, см. [Клиенты OAuth](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью клиентов OAuth.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| size | integer | - | query | Необязательно |
| page | integer | - | query | Необязательно |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательно |

## Ответ

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| size | integer | - | query | Необязательно |
| page | integer | - | query | Необязательно |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательно |

## Пример

В этом примере запрос получает все границы политики, которые применяются к учетной записи с `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**. Возвращаются только первые три записи.

#### Curl

```
curl --request GET \
 
--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890' \
 
--header 'accept: application/json' \
 
--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890
```

#### Тело ответа

```
{
 
"pageSize": 100,
 
"pageNumber": 1,
 
"totalCount": 22,
 
"content": [
 
{
 
"uuid": "a13f7b92-4c8e-4d3a-a1f7-9e3b6c2d8f01",
 
"levelType": "account",
 
"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",
 
"name": "Bnd1",
 
"boundaryQuery": "storage:dt.security_context = '${bindParam:bucket-name-param}';",
 
"boundaryConditions": [
 
{
 
"name": "storage:dt.security_context",
 
"operator": "EQ",
 
"values": [
 
"${bindParam:bucket-name-param}"
 
]
 
}
 
],
 
"metadata": {}
 
},
 
{
 
"uuid": "345a2b02-678e-45ff-92c1-4b4fd5er3b0f",
 
"levelType": "account",
 
"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",
 
"name": "bnd101",
 
"boundaryQuery": "storage:gcp.project.id = \"123\";",
 
"boundaryConditions": [
 
{
 
"name": "storage:gcp.project.id",
 
"operator": "EQ",
 
"values": [
 
"123"
 
]
 
}
 
],
 
"metadata": {}
 
},
 
{
 
"uuid": "a567b345-2345-4ab5-b8d1-0e9a65ae678f",
 
"levelType": "account",
 
"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",
 
"name": "bnd101_alpha",
 
"boundaryQuery": "storage:dt.security_context = 'alpha';\n//storage:bucket-name = 'alpha';",
 
"boundaryConditions": [
 
{
 
"name": "storage:dt.security_context",
 
"operator": "EQ",
 
"values": [
 
"alpha"
 
]
 
}
 
],
 
"metadata": {}
 
},
 
]
 
}
```

#### Код ответа

Успех (200) - Успешный ответ - список границ политики