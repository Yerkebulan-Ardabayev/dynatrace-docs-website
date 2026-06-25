---
title: Remote environments API - GET all environments
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/get-all
scraped: 2026-05-12T11:20:42.755090
---

# Remote environments API - GET all environments

# Remote environments API - GET all environments

* Reference
* Published Nov 19, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Remote environment** (`builtin:remote.environment`).

Возвращает список всех конфигураций удалённых окружений.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemoteEnvironmentConfigListDto](#openapi-definition-RemoteEnvironmentConfigListDto) | Успех |

### Объекты тела ответа

#### Объект `RemoteEnvironmentConfigListDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [RemoteEnvironmentConfigStub[]](#openapi-definition-RemoteEnvironmentConfigStub) | - |

#### Объект `RemoteEnvironmentConfigStub`

Краткое представление удалённого окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | - |
| name | string | - |
| networkScope | string | Сетевая область удалённого окружения:  * `EXTERNAL`: удалённое окружение находится в другой сети. * `INTERNAL`: удалённое окружение находится в той же сети. * `CLUSTER`: удалённое окружение находится в том же кластере.  Dynatrace SaaS может использовать только `EXTERNAL`.  Если не задано, используется `EXTERNAL`. Возможные значения: * `CLUSTER` * `EXTERNAL` * `INTERNAL` |
| uri | string | Отображаемое имя удалённого окружения. |

### JSON-модели тела ответа

```
{



"values": [



{



"id": "string",



"name": "string",



"networkScope": "CLUSTER",



"uri": "string"



}



]



}
```

## Пример

В этом примере запрос запрашивает список всех конфигураций удалённых окружений в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до двух записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/ \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/
```

#### Тело ответа

```
{



"values": [



{



"id": "b597955c-4706-40f6-b188-212faba25e1f",



"name": "Production North",



"uri": "https://prodNorth.live.dynatrace.com",



"networkScope": "EXTERNAL"



},



{



"id": "4f3b0f62-6ec0-407d-be50-5109a8516edf",



"name": "Production South",



"uri": "https://prodSouth.live.dynatrace.com",



"networkScope": "EXTERNAL"



}



]



}
```

#### Код ответа

200