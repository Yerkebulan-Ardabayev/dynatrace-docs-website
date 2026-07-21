---
title: OneAgent monitoring configuration API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration
---

# OneAgent monitoring configuration API - PUT configuration

# OneAgent monitoring configuration API - PUT configuration

* Справка
* Обновлено 23 июня 2022 г.
* Устарело

Этот API устарел. Вместо него используй [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") со схемой **Monitoring** (`builtin:host.monitoring`).

Обновляет конфигурацию мониторинга OneAgent на указанном хосте.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace нужного хоста. | path | Обязательный |
| body | [MonitoringConfig](#openapi-definition-MonitoringConfig) | Тело JSON запроса. Содержит параметры мониторинга OneAgent. | body | Опциональный |

### Объекты тела запроса

#### Объект `MonitoringConfig`

Конфигурация мониторинга OneAgent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoInjectionEnabled | boolean | Если этот параметр включён, модули кода будут внедряться в отслеживаемые приложения автоматически. Этот параметр не применяется, если автовнедрение отключено через oneagentctl (см. https://dt-url.net/oneagentctl?dt=m). | Опциональный |
| id | string | ID сущности Dynatrace хоста, на котором развёрнут OneAgent. | Опциональный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| monitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`). | Обязательный |
| monitoringMode | string | Режим мониторинга хоста: полный стек или только инфраструктура. Элемент может принимать следующие значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать перед использованием в реальном запросе.

```
{



"autoInjectionEnabled": true,



"id": "HOST-0123456789ABCDE",



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



"monitoringEnabled": true,



"monitoringMode": "FULL_STACK"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны |

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

### JSON-модели тела ответа

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

Рекомендуется проверить полезную нагрузку перед её отправкой в реальном запросе. Код ответа **204** указывает на корректную полезную нагрузку.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны |

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

#### JSON-модели тела ответа

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