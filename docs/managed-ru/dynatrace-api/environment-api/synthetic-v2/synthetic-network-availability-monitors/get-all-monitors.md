---
title: Synthetic monitors API v2 - GET все мониторы Synthetic
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-all-monitors
scraped: 2026-05-12T12:15:48.529986
---

# Synthetic monitors API v2 - GET все мониторы Synthetic

# Synthetic monitors API v2 - GET все мониторы Synthetic

* Справочник
* Updated on May 05, 2026

Возвращает список всех мониторов Synthetic в вашем окружении.

Метод доступен только для браузерных и NAM-мониторов.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `settings.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| monitorSelector | string | Определяет область запроса. В ответ попадают только мониторы, удовлетворяющие указанным критериям.  Можно добавить один или несколько перечисленных ниже критериев. Для каждого критерия можно указать несколько значений через запятую, если не оговорено иное. Если указано несколько значений, применяется логика **OR**.  * Тип монитора: `type(HTTP,MULTI_PROTOCOL)`. Возможные значения: 'HTTP', 'BROWSER', 'THIRD\_PARTY', 'MULTI\_PROTOCOL' (учтите, что в настоящее время поддерживаются только 'BROWSER' и 'MULTI\_PROTOCOL'). * ID зоны управления: `managementZoneId(1, 2)`. * Synthetic Location ME ID: `location(SYNTHETIC_LOCATION-123)`. * Monitored host ME ID: `monitoredEntity(HOST-123)`. * Теги монитора: `tag([context]key:value,key:value,key)`. Теги в форматах `[context]key:value`, `key:value` и `key` распознаются и разбираются автоматически. Если тег только с ключом содержит двоеточие (`:`), его необходимо экранировать обратной косой (`\`). Иначе тег будет разобран как `key:value tag`. Все значения тегов регистрозависимы. * Включённость монитора: `enabled(true)`.  Чтобы указать несколько критериев, перечислите их через запятую (`,`). В ответ попадут только результаты, соответствующие **всем** критериям. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticMonitorListDto](#openapi-definition-SyntheticMonitorListDto) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticMonitorListDto`

Список доступных синтетических мониторов.

| Поле | Тип | Описание |
| --- | --- | --- |
| monitors | [SyntheticMonitorSummaryDto[]](#openapi-definition-SyntheticMonitorSummaryDto) | Список мониторов. |

#### Объект `SyntheticMonitorSummaryDto`

Базовые данные монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Если true, монитор включён. |
| entityId | string | Entity id монитора. |
| name | string | Имя монитора. |
| type | string | -Поле может принимать значения: * `BROWSER` * `HTTP` * `MULTI_PROTOCOL` * `THIRD_PARTY` |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"monitors": [



{



"enabled": "true",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1",



"name": "My network availability monitor",



"type": "MULTI_PROTOCOL"



},



{



"enabled": "false",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D2",



"name": "Disabled network availability monitor",



"type": "MULTI_PROTOCOL"



}



]



}
```

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

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")