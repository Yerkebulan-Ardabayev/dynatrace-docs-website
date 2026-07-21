---
title: ActiveGate auto-update configuration API - GET an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-instance
---

# ActiveGate auto-update configuration API - GET an ActiveGate

# ActiveGate auto-update configuration API - GET an ActiveGate

* Справка
* Опубликовано 15 марта 2021 г.

Получает конфигурацию автообновления указанного Environment ActiveGate.

Запрос возвращает содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace для Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.read`.

Подробнее о том, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID нужного ActiveGate. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | Успешно |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено. Подробности см. в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateAutoUpdateConfig`

Конфигурация автообновлений ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления ActiveGate.  Применимо только если параметр **setting** установлен в значение `INHERITED`. В этом случае значение берётся из родительской настройки. В противном случае это просто дубликат значения **setting**. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| setting | string | Состояние автообновления ActiveGate: включено, отключено или унаследовано.  Если установлено значение `INHERITED`, настройка наследуется из глобальной конфигурации, заданной на уровне окружения или Managed-кластера. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Целевая версия ActiveGate.  Версию нужно указывать в формате `<major>.<minor>` (например, `1.342`) или использовать значения `latest`, `previous` или `older`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание |
| --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, когда может начаться обновление OneAgent. Если значение отсутствует и обновление должно быть выполнено, оно начнётся при первой возможности. |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор окна обслуживания |
| name | string | Название окна обслуживания |

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
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON моделей тела ответа

```
{



"effectiveSetting": "ENABLED",



"setting": "INHERITED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



}



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

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Понять базовые концепции, связанные с ActiveGate.")