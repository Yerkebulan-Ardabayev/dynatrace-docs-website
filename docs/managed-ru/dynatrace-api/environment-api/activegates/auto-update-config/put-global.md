---
title: ActiveGate auto-update configuration API - PUT global
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/put-global
---

# ActiveGate auto-update configuration API - PUT global

# ActiveGate auto-update configuration API - PUT global

* Справочник
* Опубликовано 15 марта 2021 г.

Редактирует глобальную конфигурацию автообновления ActiveGate-ов Environment.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/autoUpdate` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/autoUpdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.write`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ActiveGateGlobalAutoUpdateConfig](#openapi-definition-ActiveGateGlobalAutoUpdateConfig) | Тело JSON запроса, содержащее глобальные параметры автообновления. | body | Обязательный |

### Объекты тела запроса

#### Объект `ActiveGateGlobalAutoUpdateConfig`

Глобальная конфигурация автообновления ActiveGate-ов.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| globalSetting | string | Состояние автообновлений для всех ActiveGate-ов, подключённых к среде или кластеру Managed.  Этот параметр наследуется всеми ActiveGate-ами, у которых установлен параметр `INHERITED`. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` | Обязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| targetVersion | string | Версия, до которой обновляется ActiveGate при включённых автоматических обновлениях.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например, `1.261`).  Применимо только когда параметр **setting** установлен в `ENABLED`. | Опциональный |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления | Опциональный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в течение которых может начаться обновление OneAgent. Если значение не указано и обновление должно быть выполнено, оно начнётся при первой возможности. | Обязательный |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | Идентификатор окна обслуживания | Обязательный |
| name | string | Название окна обслуживания | Опциональный |

### Пример модели тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"globalSetting": "ENABLED",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



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
| **204** | - | Успешно. Глобальная конфигурация автообновления обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
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

### Примеры моделей тела JSON ответа

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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед её отправкой в составе реального запроса. Код ответа **204** указывает на корректную полезную нагрузку.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/autoUpdate/validator` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/autoUpdate/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.write`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
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

#### Примеры моделей тела JSON ответа

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

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")