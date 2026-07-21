---
title: Synthetic monitors API v2 - GET all Synthetic monitors
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-all-monitors
---

# Synthetic monitors API v2 - GET all Synthetic monitors

# Synthetic monitors API v2 - GET all Synthetic monitors

* Справка
* Обновлено 05 мая 2026 г.

Выводит список всех Synthetic мониторов в среде.

Метод доступен только для browser и NAM мониторов.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `settings.read`.

О том, как получить и использовать токен, читайте в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| monitorSelector | string | Определяет область запроса. В ответ попадают только мониторы, соответствующие указанным критериям.  Можно добавить один или несколько критериев из перечисленных ниже. Для каждого критерия можно указать несколько значений через запятую, если не указано иное. Если указано несколько значений, применяется логика **ИЛИ**.  * Тип монитора: `type(HTTP,MULTI_PROTOCOL)`. Возможные значения: 'HTTP', 'BROWSER', 'THIRD\_PARTY', 'MULTI\_PROTOCOL' (обратите внимание, что в настоящее время поддерживаются только 'BROWSER' и 'MULTI\_PROTOCOL'). * ID management zone: `managementZoneId(1, 2)`. * ME ID Synthetic Location: `location(SYNTHETIC_LOCATION-123)`. * ME ID отслеживаемого хоста: `monitoredEntity(HOST-123)`. * Теги монитора: `tag([context]key:value,key:value,key)`. Теги в форматах `[context]key:value`, `key:value` и `key` определяются и разбираются автоматически. Если тег, состоящий только из ключа, содержит двоеточие (`:`), нужно экранировать двоеточие обратной косой чертой (`\`). В противном случае тег будет разобран как `key:value tag`. Все значения тегов чувствительны к регистру. * Включение монитора: `enabled(true)`.  Чтобы задать несколько критериев, разделяйте их запятой (`,`). В ответ попадают только результаты, соответствующие **всем** критериям. | query | Опционально |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticMonitorListDto](#openapi-definition-SyntheticMonitorListDto) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticMonitorListDto`

Список доступных Synthetic мониторов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitors | [SyntheticMonitorSummaryDto](#openapi-definition-SyntheticMonitorSummaryDto)[] | Список мониторов. |

#### Объект `SyntheticMonitorSummaryDto`

Базовые данные монитора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Если true, монитор включён. |
| entityId | string | ID сущности монитора. |
| name | string | Название монитора. |
| type | string | Тип монитора. Элемент может содержать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Примеры моделей тела ответа JSON

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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать монитор для одного URL типа browser, browser clickpath или HTTP-монитор.")