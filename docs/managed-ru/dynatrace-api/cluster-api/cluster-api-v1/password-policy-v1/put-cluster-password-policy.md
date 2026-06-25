---
title: Update cluster password policy
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/put-cluster-password-policy
scraped: 2026-05-12T12:12:13.307907
---

# Update cluster password policy

# Update cluster password policy

* Published Nov 18, 2020

Этот API-вызов обновляет password policy кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/passwordPolicy`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [PasswordPolicy](#openapi-definition-PasswordPolicy) | JSON-тело запроса. Содержит параметры конфигурации password policy. | body | Optional |

### Объекты тела запроса

#### Объект `PasswordPolicy`

Конфигурация password policy.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| minNumberOfDigits | integer | Минимальное число цифр. | Required |
| minNumberOfLowercaseChars | integer | Минимальное число строчных символов. | Required |
| minNumberOfNonAlphanumericChars | integer | Минимальное число неалфавитно-цифровых символов. | Required |
| minNumberOfUppercaseChars | integer | Минимальное число прописных символов. | Required |
| minPasswordLength | integer | Минимальная длина пароля. | Required |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её нужно адаптировать для реального запроса.

```
{



"minNumberOfDigits": 1,



"minNumberOfLowercaseChars": 1,



"minNumberOfNonAlphanumericChars": 1,



"minNumberOfUppercaseChars": 1,



"minPasswordLength": 1



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно обновлено. Тело ответа пустое. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректный ввод. |
| **404** | - | Realm не найден. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-статус код. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Пример

В этом примере обновляется password policy для Dynatrace Managed развёртывания (`myManaged.cluster.com`). Задаются:

* Минимальная длина пароля.
* Минимальное число прописных символов.
* Минимальное число строчных символов.
* Минимальное число цифр.
* Минимальное число неалфавитно-цифровых символов.

В ответ возвращается код `204` — password policy успешно обновлён.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"realmId\":\"string\",\"minPasswordLength\":16,\"minNumberOfUppercaseChars\":2,\"minNumberOfLowercaseChars\":4,\"minNumberOfDigits\":2,\"minNumberOfNonAlphanumericChars\":4}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy
```

#### Тело ответа

Успешно обновлено. Тело ответа пустое.

#### Код ответа

`204`