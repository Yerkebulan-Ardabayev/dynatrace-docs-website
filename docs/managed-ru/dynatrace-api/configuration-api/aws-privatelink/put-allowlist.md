---
title: AWS PrivateLink API - PUT allowlist
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/put-allowlist
scraped: 2026-05-12T11:21:15.565203
---

# AWS PrivateLink API - PUT allowlist

# AWS PrivateLink API - PUT allowlist

* Reference
* Published Nov 19, 2020

Добавляет AWS-аккаунт в allowlist AWS PrivateLink.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID AWS-аккаунта для обновления в allowlist AWS PrivateLink. Должен совпадать с id в переданном payload. | path | Required |
| body | [AllowlistedAwsAccount](#openapi-definition-AllowlistedAwsAccount) | ID AWS-аккаунта для обновления в allowlist AWS PrivateLink. Должен совпадать с id в path. | body | Required |

### Объекты тела запроса

#### Объект `AllowlistedAwsAccount`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID AWS-аккаунта для добавления в allowlist | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"id": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [AllowlistedAwsAccount](#openapi-definition-AllowlistedAwsAccount) | Успех. Account id добавлен в allowlist PrivateLink. |
| **204** | - | Успех. Account id уже есть в allowlist PrivateLink. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Неверный формат AWS account id (длина = 12 символов, только цифры). |

### Объекты тела ответа

#### Объект `AllowlistedAwsAccount`

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID AWS-аккаунта для добавления в allowlist |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"id": "string"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```