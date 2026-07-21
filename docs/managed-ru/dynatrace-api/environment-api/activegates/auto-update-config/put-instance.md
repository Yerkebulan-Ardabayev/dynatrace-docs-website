---
title: ActiveGate auto-update configuration API - PUT an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/put-instance
---

# ActiveGate auto-update configuration API - PUT an ActiveGate

# ActiveGate auto-update configuration API - PUT an ActiveGate

* Справочник
* Опубликовано 15 марта 2021 г.

Изменяет конфигурацию автообновления указанного Environment ActiveGate.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |
| PUT | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.write`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID нужного ActiveGate. | path | Обязательный |
| body | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | JSON тело запроса, содержащее параметры автообновления. | body | Обязательный |

### Объекты тела запроса

#### Объект `ActiveGateAutoUpdateConfig`

Конфигурация автообновлений ActiveGate.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления ActiveGate.  Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из родительской настройки. В остальных случаях это просто дубликат значения **setting**. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` | Необязательный |
| setting | string | Состояние автообновления ActiveGate: включено, отключено или унаследовано.  Если установлено значение `INHERITED`, настройка наследуется из глобальной конфигурации, заданной на уровне окружения или кластера Managed. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` | Обязательный |
| targetVersion | string | Целевая версия ActiveGate.  Укажи версию в формате `<major>.<minor>` (например `1.342`) либо `latest`, `previous` или `older`. | Необязательный |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления | Необязательный |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в которых может начаться обновление OneAgent. Если значение не задано, а обновление должно быть выполнено, оно начнётся при первой возможности. | Обязательный |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | Идентификатор окна обслуживания | Обязательный |
| name | string | Название окна обслуживания | Необязательный |

### JSON модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Конфигурация автообновления обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

### JSON модели тела ответа

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

## Проверка payload

Рекомендуется проверять payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate/validator` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.write`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация автообновления корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

#### Объекты тела ответа

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

#### JSON модели тела ответа

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

## Похожие темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Понять базовые концепции, связанные с ActiveGate.")