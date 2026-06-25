---
title: Extensions API - GET states of an extension
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-state
scraped: 2026-05-12T11:19:53.366984
---

# Extensions API - GET states of an extension

# Extensions API - GET states of an extension

* Reference
* Published Mar 06, 2020

Выводит состояния эндпоинтов указанного расширения.

Состояния хранятся в памяти сервера и очищаются при перезапуске.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/states` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/states` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого расширения. | path | Required |
| pageSize | integer | Количество результатов на страницу. Должно быть от 1 до 500 | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. | query | Optional |
| state | string | Состояние расширения для фильтрации. Возможные значения: * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionStateList](#openapi-definition-ExtensionStateList) | Успех |

### Объекты тела ответа

#### Объект `ExtensionStateList`

Список состояний расширения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| states | [ExtensionState[]](#openapi-definition-ExtensionState) | Список состояний расширения. |
| totalResults | integer | Общее количество записей в результате. |

#### Объект `ExtensionState`

Состояние расширения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| endpointId | string | ID эндпоинта, где обнаружено состояние - только Active Gate. |
| extensionId | string | ID расширения. |
| hostId | string | ID хоста, на котором работает расширение. |
| processId | string | ID сущности, на которой активно расширение. |
| state | string | Состояние расширения. Возможные значения: * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` |
| stateDescription | string | Краткое описание состояния. |
| timestamp | integer | Временная метка обнаружения состояния, в миллисекундах UTC. |
| version | string | Версия расширения (например `1.0.0`). |

### JSON-модели тела ответа

```
{



"nextPageToken": "LlUdYmu5S2MfX/ppfCInR9M=",



"states": [



{



"endpointId": "null",



"extensionId": "custom.python.connectionpool",



"hostId": "HOST-01A7DEFA5340A86D",



"processId": "PROCESS_GROUP_INSTANCE-2182DF2E20E3E067",



"state": "OK",



"stateDescription": "",



"timestamp": 1578578108213,



"version": "1.82"



}



],



"totalResults": 9



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")