---
title: Get cluster password policy
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/get-cluster-password-policy
scraped: 2026-05-12T12:12:17.046187
---

# Get cluster password policy

# Get cluster password policy

* Published Nov 18, 2020

Этот API-вызов возвращает password policy кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/passwordPolicy`

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PasswordPolicy](#openapi-definition-PasswordPolicy) | Успех |
| **404** | - | Realm не найден. |

### Объекты тела ответа

#### Объект `PasswordPolicy`

Конфигурация password policy.

| Элемент | Тип | Описание |
| --- | --- | --- |
| minNumberOfDigits | integer | Минимальное число цифр. |
| minNumberOfLowercaseChars | integer | Минимальное число строчных символов. |
| minNumberOfNonAlphanumericChars | integer | Минимальное число неалфавитно-цифровых символов. |
| minNumberOfUppercaseChars | integer | Минимальное число прописных символов. |
| minPasswordLength | integer | Минимальная длина пароля. |

### JSON-модели тела ответа

```
{



"minNumberOfDigits": 1,



"minNumberOfLowercaseChars": 1,



"minNumberOfNonAlphanumericChars": 1,



"minNumberOfUppercaseChars": 1,



"minPasswordLength": 1



}
```

## Пример

В этом примере запрашивается password policy Dynatrace Managed развёртывания (`myManaged.cluster.com`). В ответ возвращается информация о текущих настройках password policy.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/passwordPolicy
```

#### Тело ответа

```
{



"realmId": "string",



"minPasswordLength": 12,



"minNumberOfUppercaseChars": 1,



"minNumberOfLowercaseChars": 1,



"minNumberOfDigits": 1,



"minNumberOfNonAlphanumericChars": 10



}
```

#### Код ответа

`200`