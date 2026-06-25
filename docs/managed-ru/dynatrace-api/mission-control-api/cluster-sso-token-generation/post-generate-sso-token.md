---
title: Generate SSO token
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/cluster-sso-token-generation/post-generate-sso-token
scraped: 2026-05-12T12:14:17.193792
---

# Generate SSO token

# Generate SSO token

* Published Mar 12, 2021

Этот API-вызов генерирует токен, позволяющий выполнять URL загрузки update-пакетов.

## Endpoint

`/public/v1.0/oauth/api-token`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [TokenGrantCredentialsDto](#openapi-definition-TokenGrantCredentialsDto) | - | body | Optional |

### Объекты тела запроса

#### Объект `TokenGrantCredentialsDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clientId | string | - | Optional |
| clientSecret | string | - | Optional |
| scope | string | - | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"clientId": "string",



"clientSecret": "string",



"scope": "string"



}
```

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Токен успешно сгенерирован |
| **401** | Невалидные учётные данные |
| **404** | Кластер не найден |

## Пример

В этом примере для генерации токена выполняется следующий REST-вызов:

#### Curl

```
curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/api-token"



-H "accept: application/json"



-H "Content-Type: application/json"



-d "{ \"clientId\": \"dt0s04.AAAAAAAA\", \"clientSecret\": \"dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL\", \"scope\": \"sso20-managed-cluster-offline-bundle\"}"
```

#### URL запроса

```
https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/api-token
```

#### Тело ответа

```
{



"token": "aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA",



"scopes": [



"sso20-managed-cluster-offline-bundle"



],



"expiresAt": 1615477153001



}
```

#### Код ответа

`200`