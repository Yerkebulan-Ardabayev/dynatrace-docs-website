---
title: Remote environments API - GET a remote environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/get-remote-environment
scraped: 2026-05-12T11:20:41.412265
---

# Remote environments API - GET a remote environment configuration

# Remote environments API - GET a remote environment configuration

* Reference
* Published Nov 19, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Remote environment** (`builtin:remote.environment`).

Возвращает свойства указанной конфигурации удалённого окружения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужной конфигурации. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemoteEnvironmentConfigDto](#openapi-definition-RemoteEnvironmentConfigDto) | Успех |

### Объекты тела ответа

#### Объект `RemoteEnvironmentConfigDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя удалённого окружения. |
| id | string | ID конфигурации. |
| networkScope | string | Сетевая область удалённого окружения:  * `EXTERNAL`: удалённое окружение находится в другой сети. * `INTERNAL`: удалённое окружение находится в той же сети. * `CLUSTER`: удалённое окружение находится в том же кластере.  Dynatrace SaaS может использовать только `EXTERNAL`.  Если не задано, используется `EXTERNAL`. Возможные значения: * `CLUSTER` * `EXTERNAL` * `INTERNAL` |
| token | string | API-токен, дающий доступ к удалённому окружению.  Токен должен иметь scope **Fetch data from a remote environment** (`RestRequestForwarding`).  По соображениям безопасности GET-запросы возвращают это поле как `null`. |
| uri | string | URI удалённого окружения. |

### JSON-модели тела ответа

```
{



"displayName": "string",



"id": "string",



"networkScope": "EXTERNAL",



"token": "string",



"uri": "string"



}
```

## Пример

В этом примере запрос запрашивает свойства удалённого окружения **Production North**, у которого ID **b597955c-4706-40f6-b188-212faba25e1f**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/b597955c-4706-40f6-b188-212faba25e1f \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/b597955c-4706-40f6-b188-212faba25e1f
```

#### Тело ответа

```
{



"id": "b597955c-4706-40f6-b188-212faba25e1f",



"displayName": "Production North",



"uri": "https://prodNorth.live.dynatrace.com",



"token": null,



"networkScope": "EXTERNAL"



}
```

#### Код ответа

200