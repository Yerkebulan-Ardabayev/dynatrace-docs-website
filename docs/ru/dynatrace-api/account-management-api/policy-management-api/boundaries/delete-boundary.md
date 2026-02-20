---
title: Управление политиками API - УДАЛИТЬ границу политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/delete-boundary
scraped: 2026-02-20T21:27:17.254942
---

# Управление политиками API - УДАЛИТЬ границу политики

# Управление политиками API - УДАЛИТЬ границу политики

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Удаляет границу политики по uuid внутри уровня. Вы не можете удалить глобальную границу, поскольку они управляются Dynatrace.

DELETE

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`) присвоенное к вашему токену. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | ID необходимой границы. | path | Обязательный |
| accountId | - | ID уровня границы политики. Используйте UUID учетной записи. | path | Обязательный |

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешный ответ - граница политики удалена |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Неудача. Запрос недействителен |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Неудача. Указанный ресурс не найден. |

### Объекты ответа

#### Объект `ErrorDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки. |
| message | string | Краткое описание ошибки. |
| errorsMap | object | - |

### Модели ответа JSON

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Пример

В этом примере запрос удаляет границу политики с UUID границы **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** для `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request DELETE \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345 \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Код ответа

204 - Успешный ответ - граница политики удалена.