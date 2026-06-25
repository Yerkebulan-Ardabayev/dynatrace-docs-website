---
title: Azure credentials API - GET monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/get-services
scraped: 2026-05-12T11:16:32.256513
---

# Azure credentials API - GET monitored services

# Azure credentials API - GET monitored services

* Reference
* Published Jul 28, 2022

Возвращает список Azure-сервисов, которые мониторятся Azure-конфигурацией.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID указанной конфигурации Azure credentials. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AzureMonitoredServicesDto](#openapi-definition-AzureMonitoredServicesDto) | Успех |

### Объекты тела ответа

#### Объект `AzureMonitoredServicesDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| services | [AzureSupportingService[]](#openapi-definition-AzureSupportingService) | Список Azure-сервисов для мониторинга. Доступные сервисы перечислены операцией [/azure/supportedServices](https://dt-url.net/wt42sdq).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации](https://dt-url.net/kx2351b).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. Для встроенных сервисов изменение списка метрик не поддерживается, поэтому он должен быть null. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AzureSupportingService`

Сервис для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric[]](#openapi-definition-AzureMonitoredMetric) | Список метрик для мониторинга этого сервиса. Он должен включать все рекомендуемые метрики. Если список null, для мониторинга используется рекомендуемый список метрик для этого сервиса. |
| name | string | Имя сервиса. Допустимые имена поддерживаемых сервисов можно узнать через restAPI /azure/supportedServices |

#### Объект `AzureMonitoredMetric`

Метрика сервиса для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Он должен включать все рекомендуемые измерения. |
| name | string | Имя метрики сервиса. |

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



"name": "string"



}



],



"name": "string"



}



]



}
```

## Связанные темы

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")