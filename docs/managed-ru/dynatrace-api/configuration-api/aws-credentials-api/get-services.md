---
title: AWS credentials API - GET monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/get-services
scraped: 2026-05-12T11:15:10.208971
---

# AWS credentials API - GET monitored services

# AWS credentials API - GET monitored services

* Reference
* Published Jul 28, 2022

Возвращает список AWS-сервисов, которые мониторятся AWS-конфигурацией.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID указанной конфигурации AWS credentials. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsMonitoredServicesDto](#openapi-definition-AwsMonitoredServicesDto) | Успех |

### Объекты тела ответа

#### Объект `AwsMonitoredServicesDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| services | [AwsSupportingServiceConfig[]](#openapi-definition-AwsSupportingServiceConfig) | Список AWS-сервисов для мониторинга. Доступные сервисы перечислены операцией [/aws/supportedServices](https://dt-url.net/me02sh2).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации](https://dt-url.net/r12v0pkl).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. Для встроенных сервисов изменение списка метрик не поддерживается, поэтому он должен быть null. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AwsSupportingServiceConfig`

Сервис для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric[]](#openapi-definition-AwsSupportingServiceMetric) | Список метрик для мониторинга этого сервиса. Если список null, мониторится рекомендуемый список метрик для этого сервиса. |
| name | string | Имя сервиса. Допустимые имена поддерживаемых сервисов можно узнать через restAPI /aws/supportedServices |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. |
| name | string | Имя метрики сервиса. |
| statistic | string | Статистика (агрегация), используемая для метрики. Значение AVG\_MIN\_MAX это 3 статистики сразу: AVERAGE, MINIMUM и MAXIMUM Возможные значения: * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

### JSON-модели тела ответа

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