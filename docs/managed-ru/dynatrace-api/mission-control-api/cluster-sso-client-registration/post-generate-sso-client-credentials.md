---
title: Generate SSO client credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/cluster-sso-client-registration/post-generate-sso-client-credentials
scraped: 2026-05-12T12:14:15.317269
---

# Generate SSO client credentials

# Generate SSO client credentials

* Published Mar 12, 2021

Этот API-вызов генерирует `OAuth API client`.

Можно создать до `100` OAuth API clients на аккаунт. Рекомендуется переиспользовать однажды созданный OAuth API client.

## Endpoint

`/public/v1.0/oauth/registration/withLicenseKey`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| clientType | string | - | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ClientCredentialsDto](#openapi-definition-ClientCredentialsDto) | Учётные данные кластера успешно сгенерированы |
| **401** | - | Невалидные учётные данные кластера |

### Объекты тела ответа

#### Объект `ClientCredentialsDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| clientId | string | - |
| clientSecret | string | - |
| scopes | string[] | - |

### JSON-модели тела ответа

```
{



"clientId": "string",



"clientSecret": "string",



"scopes": [



"string"



]



}
```

## Пример

В этом примере для генерации `OAuth API client` выполняется следующий REST-вызов.

где:

* `<cluster-identifier>` — идентификатор кластера (в Dynatrace, перейдите в **Licensing**). Например, `0a00a0a0-92ec-11e7-b1e6-12fbd1fb3732`
* `<license-key>` — лицензионный ключ, выданный во welcome-письме и видимый в **Licensing**. Например, `0a0aAAAA0jeUv6N`.

#### Curl

```
curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/registration/withLicenseKey"



-H "accept: application/json"



-u "<cluster-identifier>:<license-key>"
```

#### URL запроса

```
https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/registration/withLicenseKey
```

#### Тело ответа

```
{



"clientId": "dt0s04.AAAAAAAA",



"clientSecret": "dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL",



"scopes": [



"sso20-managed-cluster-offline-bundle",



"sso20-identity-linking"



]



}
```

#### Код ответа

`200`