---
title: OneAgent мониторинговая конфигурация API - PUT конфигурация
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration
scraped: 2026-02-06T16:31:13.607418
---

* Устаревшее

Эта API устарела. Вместо нее используйте Настройки API с схемой **Мониторинг** (`builtin:host.monitoring`).

Обновляет мониторинговую конфигурацию OneAgent на указанном хосте.

Запрос использует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | Managed | `https://{your-environment-id}.live.dynatrace.com/api/config/v1/hosts/{id}/monitoring` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring` |

## Аутентификация

Чтобы выполнить этот запрос, вам нужен токен доступа с областью `WriteConfig`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор сущности Dynatrace необходимого хоста. | path | Обязательный |
| body | [MonitoringConfig](#openapi-definition-MonitoringConfig) | Тело запроса JSON. Содержит параметры мониторинга OneAgent. | body | Необязательный |

### Объекты тела запроса

#### Объект `MonitoringConfig`

Мониторинговая конфигурация OneAgent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoInjectionEnabled | boolean | Кодовые модули будут автоматически внедрены в контролируемые приложения, если это настройка включена. Это настройка не будет применена, если автоматическое внедрение отключено через oneagentctl (см. https://dt-url.net/oneagentctl). | Необязательный |
| id | string | Идентификатор сущности Dynatrace хоста, где развернут OneAgent. | Необязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |
| monitoringEnabled | boolean | Мониторинг включен (`true`) или отключен (`false`). | Обязательный |
| monitoringMode | string | Режим мониторинга для хоста: полный стек или только инфраструктура. Элемент может иметь следующие значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Ее необходимо скорректировать для использования в фактическом запросе.

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

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ не имеет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные неверны |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код HTTP-статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может иметь следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

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


)


],


"message": "string"


)


}
```

## Проверка полезной нагрузки

Мы рекомендуем проверить полезную нагрузку перед отправкой ее с фактическим запросом. Код ответа **204** указывает на действительную полезную нагрузку.

Запрос использует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | Managed | `https://{your-environment-id}.live.dynatrace.com/api/config/v1/hosts/{id}/monitoring/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring/validator` |

### Аутентификация

Чтобы выполнить этот запрос, вам нужен токен доступа с областью `WriteConfig`.

Чтобы узнать, как получить и использовать его, см. Токены и аутентификация.

### Ответ

#### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Представленная конфигурация действительна. Ответ не имеет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные неверны |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код HTTP-статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может иметь следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела ответа JSON

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


)


],


"message": "string"


)


}
```