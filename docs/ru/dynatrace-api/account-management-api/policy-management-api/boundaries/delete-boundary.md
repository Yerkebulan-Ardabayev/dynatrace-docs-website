---
title: Управление политикой API - УДАЛИТЬ границу политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/delete-boundary
scraped: 2026-03-06T21:29:29.616618
---

# API управления политиками — УДАЛЕНИЕ границы политики


Удаляет границу политики по UUID в рамках уровня. Невозможно удалить границу глобального уровня, так как ими управляет Dynatrace.

## Аутентификация

Для выполнения этого запроса необходимо разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`), назначенное вашему токену. Чтобы узнать, как получить и использовать его, см. OAuth-клиенты.

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | Идентификатор требуемой границы. | path | Обязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID аккаунта. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешный ответ — граница политики удалена |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Ошибка. Запрос некорректен |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Ошибка. Указанный ресурс не найден. |

### Объекты тела ответа

#### Объект `ErrorDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки. |
| message | string | Краткое описание ошибки. |
| errorsMap | object | - |

### JSON-модели тела ответа

```
{


"code": 1,


"message": "string",


"errorsMap": {}


}
```

## Пример

В этом примере запрос удаляет границу политики с `UUID` границы политики **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** для `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

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

204 — Успешный ответ — граница политики удалена.
