---
title: AWS credentials API - GET monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/get-services
---

# AWS credentials API - GET monitored services

# AWS credentials API - GET monitored services

* Справка
* Опубликовано 28 июля 2022 г.

Выводит список сервисов AWS, которые отслеживаются конфигурацией AWS.

Запрос выдаёт полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать такой токен, рассказано в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID указанной конфигурации учётных данных AWS. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsMonitoredServicesDto](#openapi-definition-AwsMonitoredServicesDto) | Успех |

### Объекты тела ответа

#### Объект `AwsMonitoredServicesDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| services | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | Список сервисов AWS, которые нужно отслеживать. Доступные сервисы перечислены в операции [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации﻿](https://dt-url.net/r12v0pkl?dt=m).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. Для встроенных сервисов настройка списка метрик не поддерживается, поэтому значение должно быть null. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AwsSupportingServiceConfig`

Сервис, который нужно отслеживать.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | Список метрик, которые нужно отслеживать для этого сервиса. Если список равен null, для этого сервиса будет отслеживаться рекомендуемый список метрик. |
| name | string | Название сервиса. Допустимые поддерживаемые названия сервисов можно узнать через /aws/supportedServices restAPI |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса, которую нужно отслеживать.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список названий измерений метрики. |
| name | string | Название метрики сервиса. |
| statistic | string | Статистика (агрегация), которая будет использоваться для метрики. Значение AVG\_MIN\_MAX это сразу 3 статистики: AVERAGE, MINIMUM и MAXIMUM. Элемент может принимать следующие значения * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

### Модели тела ответа JSON

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