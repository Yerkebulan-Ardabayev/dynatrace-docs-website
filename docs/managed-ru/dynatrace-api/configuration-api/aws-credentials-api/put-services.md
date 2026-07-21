---
title: AWS credentials API - PUT monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/put-services
---

# AWS credentials API - PUT monitored services

# AWS credentials API - PUT monitored services

* Справочник
* Опубликовано 28 июля 2022 г.

Обновляет список сервисов AWS, которые отслеживаются конфигурацией AWS. Обрати внимание, что запрос перезаписывает существующую конфигурацию. Все сервисы, мониторинг которых нужно продолжить, должны присутствовать в теле запроса.

Запрос принимает тело в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID учётных данных AWS, для которых нужно обновить конфигурацию отслеживаемых сервисов. | path | Обязательный |
| body | [AwsMonitoredServicesDto](#openapi-definition-AwsMonitoredServicesDto) | Тело JSON запроса. Содержит обновлённую конфигурацию отслеживаемых сервисов для учётных данных AWS. | body | Опциональный |

### Объекты тела запроса

#### Объект `AwsMonitoredServicesDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| services | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | Список сервисов AWS, которые нужно отслеживать. Доступные сервисы перечислены операцией [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно проверить в [документации﻿](https://dt-url.net/r12v0pkl?dt=m).  Список метрик можно пропустить (задать значение null), в этом случае для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. Для встроенных сервисов изменение списка метрик не поддерживается, поэтому значение должно быть null. | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `AwsSupportingServiceConfig`

Сервис, который нужно отслеживать.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | Список метрик, которые нужно отслеживать для этого сервиса. Если список равен null, для этого сервиса будет отслеживаться рекомендуемый список метрик. | Опциональный |
| name | string | Название сервиса. Действительные поддерживаемые названия сервисов можно узнать через /aws/supportedServices restAPI | Обязательный |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса, которую нужно отслеживать.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список названий измерений метрики. | Обязательный |
| name | string | Название метрики сервиса. | Обязательный |
| statistic | string | Статистика (агрегация), которая будет использоваться для метрики. Значение AVG\_MIN\_MAX представляет собой сразу 3 статистики: AVERAGE, MINIMUM и MAXIMUM. Элемент может содержать следующие значения * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` | Обязательный |

### JSON модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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



"name": "string",



"statistic": "AVERAGE"



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
| **204** | - | Успешно. Конфигурация учётных данных AWS обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

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
| parameterLocation | string | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Валидация тела запроса

Рекомендуется валидировать тело запроса перед отправкой в составе реального запроса. Код ответа **204** означает, что тело запроса корректно.

Запрос принимает тело в формате `application/json`.

Запрос принимает тело в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

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
| parameterLocation | string | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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