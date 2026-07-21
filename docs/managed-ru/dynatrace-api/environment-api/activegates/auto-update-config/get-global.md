---
title: ActiveGate auto-update configuration API - GET global
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-global
---

# ActiveGate auto-update configuration API - GET global

# ActiveGate auto-update configuration API - GET global

* Справочник
* Опубликовано 15 марта 2021 г.

Получает глобальную конфигурацию автообновления Environment ActiveGate.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/autoUpdate` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/autoUpdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.read`.

О том, как получить и использовать его, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateGlobalAutoUpdateConfig](#openapi-definition-ActiveGateGlobalAutoUpdateConfig) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateGlobalAutoUpdateConfig`

Глобальная конфигурация автообновления ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| globalSetting | string | Состояние автообновлений для всех ActiveGate, подключённых к среде или Managed-кластеру.  Эта настройка наследуется всеми ActiveGate, у которых установлена настройка `INHERITED`. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| targetVersion | string | Версия, до которой обновляется ActiveGate при включённых автоматических обновлениях.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например, `1.261`).  Применимо только если параметр **setting** установлен в `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание |
| --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в которых может начаться обновление OneAgent. Если значение отсутствует и обновление должно быть выполнено, оно начнётся при первой возможности. |

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
| code | integer | HTTP-код статуса |
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

### Примеры тела ответа JSON

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

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Разобраться в базовых концепциях, связанных с ActiveGate.")