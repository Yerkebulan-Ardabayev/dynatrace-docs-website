---
title: Credential vault API - DELETE a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/del-credentials
scraped: 2026-05-12T12:05:40.550208
---

# Credential vault API - DELETE a set of credentials

# Credential vault API - DELETE a set of credentials

* Reference
* Published Oct 14, 2019

Этот API устарел. Используйте [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для credentials.") из Environment API.

Удаляет указанный набор учётных данных для [synthetic-мониторов](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `credentialVault.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого набора учётных данных. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Набор учётных данных удалён. Ответ без тела. |

## Пример

В этом примере запрос удаляет набор учётных данных, созданный в примере [POST request example](/managed/dynatrace-api/configuration-api/credential-vault/post-credentials#example "Создание конфигурации учётных данных через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-1E6EA5075AF7E85D \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-1E6EA5075AF7E85D
```

#### Код ответа

204

## Связанные темы

* [Configure browser monitors](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке browser-мониторов и clickpath.")
* [Configure HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")