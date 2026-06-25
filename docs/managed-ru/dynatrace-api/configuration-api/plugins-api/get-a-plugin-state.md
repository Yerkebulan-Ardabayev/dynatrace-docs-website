---
title: Plugins API - GET states of an ActiveGate plugin
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-a-plugin-state
scraped: 2026-05-12T11:20:54.392962
---

# Plugins API - GET states of an ActiveGate plugin

# Plugins API - GET states of an ActiveGate plugin

* Reference
* Published Jun 07, 2019

Выводит состояния эндпоинтов указанного плагина.

Состояния хранятся в памяти сервера и очищаются при перезапуске.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/states` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/states` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого плагина. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PluginStateList](#openapi-definition-PluginStateList) | Успех |

### Объекты тела ответа

#### Объект `PluginStateList`

Список состояний плагина.

| Элемент | Тип | Описание |
| --- | --- | --- |
| states | [PluginState[]](#openapi-definition-PluginState) | Список состояний плагина. |

#### Объект `PluginState`

Состояние плагина.

| Элемент | Тип | Описание |
| --- | --- | --- |
| endpointId | string | ID эндпоинта, где обнаружено состояние - только Active Gate. |
| hostId | string | ID хоста, на котором работает плагин. |
| pluginId | string | ID плагина. |
| processId | string | ID сущности, на которой активен плагин. |
| state | string | Состояние плагина. Возможные значения: * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` |
| stateDescription | string | Краткое описание состояния. |
| timestamp | integer | Временная метка обнаружения состояния, в миллисекундах UTC. |
| version | string | Версия плагина (например `1.0.0`). |

### JSON-модели тела ответа

```
{



"endpointId": "-8213819843595439277",



"pluginId": "custom.remote.python.demo",



"state": "ERROR_AUTH",



"stateDescription": "Could not authorize",



"timestamp": 1556199097994,



"version": "1.0.0"



}
```

## Пример

В этом примере запрос выводит состояния **MathPlugin** с ID **custom.remote.python.simple\_math**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/states \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/states
```

#### Тело ответа

```
{



"states": [



{



"pluginId": "custom.remote.python.simple_math",



"version": "1.02",



"endpointId": "575712901374982783",



"state": "OK",



"stateDescription": "",



"timestamp": 1560343244178



}



]



}
```

#### Код ответа

200