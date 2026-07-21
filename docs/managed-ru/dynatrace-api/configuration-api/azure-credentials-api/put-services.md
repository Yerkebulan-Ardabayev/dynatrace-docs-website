---
title: Azure credentials API - PUT monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/put-services
---

# Azure credentials API - PUT monitored services

# Azure credentials API - PUT monitored services

* Справочная информация
* Опубликовано 28 июля 2022 г.

Обновляет список служб Azure, которые отслеживаются конфигурацией Azure. Обрати внимание, что запрос перезаписывает существующую конфигурацию. Все службы, отслеживание которых нужно продолжить, должны быть указаны в теле запроса.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID учётных данных Azure, для которых обновляется конфигурация отслеживаемых служб. | path | Обязательный |
| body | [AzureMonitoredServicesDto](#openapi-definition-AzureMonitoredServicesDto) | JSON тело запроса. Содержит обновлённую конфигурацию отслеживаемых служб для учётных данных Azure. | body | Опциональный |

### Объекты тела запроса

#### Объект `AzureMonitoredServicesDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| services | [AzureSupportingService](#openapi-definition-AzureSupportingService)[] | Список служб Azure для отслеживания. Доступные службы перечислены операцией [/azure/supportedServices﻿](https://dt-url.net/wt42sdq?dt=m).  Для каждой службы можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретной службы можно посмотреть в [документации﻿](https://dt-url.net/kx2351b?dt=m).  Список метрик можно пропустить (задав значение null), в этом случае для отслеживания будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. Для встроенных служб настройка списка метрик не поддерживается, поэтому значение должно быть null. | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `AzureSupportingService`

Служба для отслеживания.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric](#openapi-definition-AzureMonitoredMetric)[] | Список метрик, отслеживаемых для этой службы. Должен включать все рекомендуемые метрики. Если список равен null, для этой службы будет отслеживаться рекомендуемый список метрик. | Опциональный |
| name | string | Имя службы. Допустимые имена поддерживаемых служб можно узнать с помощью /azure/supportedServices restAPI | Обязательный |

#### Объект `AzureMonitoredMetric`

Отслеживаемая метрика службы.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Должен включать все рекомендуемые измерения. | Обязательный |
| name | string | Имя метрики службы. | Обязательный |

### JSON модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



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



"services": [



{



"monitoredMetrics": [



{



"dimensions": [



"string"



],



"name": "string"



}



],



"name": "string"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Конфигурация учётных данных Azure обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

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

Рекомендуется проверить payload перед отправкой в реальном запросе. Код ответа **204** означает, что payload действителен.

Запрос принимает данные в формате `application/json`.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация действительна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

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

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")