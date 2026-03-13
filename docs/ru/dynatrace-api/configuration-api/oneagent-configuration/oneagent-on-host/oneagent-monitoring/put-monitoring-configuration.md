---
title: OneAgent monitoring configuration API - PUT configuration
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration
scraped: 2026-02-06T16:31:13.607418
---

# API конфигурации мониторинга OneAgent — PUT-запрос конфигурации

# API конфигурации мониторинга OneAgent — PUT-запрос конфигурации

* Справочник
* Обновлено 23 июня 2022 г.
* Устарело

Этот API устарел. Вместо него используйте [Settings API](../../../../environment-api/settings.md "Узнайте о возможностях API настроек Dynatrace.") со схемой **Monitoring** (`builtin:host.monitoring`).

Обновляет конфигурацию мониторинга OneAgent на указанном хосте.

Запрос принимает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/config/v1/hosts/{id}/monitoring` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия `WriteConfig`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор сущности Dynatrace для требуемого хоста. | path | Обязательный |
| body | [MonitoringConfig](#openapi-definition-MonitoringConfig) | Тело запроса в формате JSON. Содержит параметры мониторинга OneAgent. | body | Необязательный |

### Объекты тела запроса

#### Объект `MonitoringConfig`

Конфигурация мониторинга OneAgent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoInjectionEnabled | boolean | Модули кода будут автоматически внедряться в контролируемые приложения, если эта настройка включена. Эта настройка не применяется, если автоматическое внедрение отключено через oneagentctl (см. https://dt-url.net/oneagentctl). | Необязательный |
| id | string | Идентификатор сущности Dynatrace хоста, на котором развёрнут OneAgent. | Необязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |
| monitoringEnabled | boolean | Мониторинг включён (`true`) или выключен (`false`). | Обязательный |
| monitoringMode | string | Режим мониторинга для хоста: полный стек или только инфраструктура. Элемент может содержать следующие значения: * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо скорректировать для использования в реальном запросе.

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
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Валидация полезной нагрузки

Мы рекомендуем валидировать полезную нагрузку перед отправкой с реальным запросом. Код ответа **204** указывает на валидную полезную нагрузку.

Запрос принимает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/config/v1/hosts/{id}/monitoring/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring/validator` |

### Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия `WriteConfig`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Валидация пройдена. Представленная конфигурация валидна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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
