---
title: Remote environments API - DELETE a remote environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/del-remote-environment
scraped: 2026-05-12T11:20:40.064285
---

# Remote environments API - DELETE a remote environment configuration

# Remote environments API - DELETE a remote environment configuration

* Reference
* Published Nov 19, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Remote environment** (`builtin:remote.environment`).

Удаляет указанную конфигурацию удалённого окружения.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемой конфигурации. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Конфигурация удалена. Ответ без тела. |

## Пример

В этом примере запрос удаляет удалённое окружение **Pre-Production**, созданное в примере [POST request](/managed/dynatrace-api/configuration-api/remote-environments/post-remote-environment#example "Создание удалённого окружения Dynatrace через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/c89b9d9f-8c59-4c5b-b7ef-1a082d11e9ba \



-H 'Authorization: Api-token abcdefghij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/c89b9d9f-8c59-4c5b-b7ef-1a082d11e9ba
```

#### Код ответа

204