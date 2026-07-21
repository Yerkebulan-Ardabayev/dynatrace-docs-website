---
title: Azure credentials API - GET monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/get-services
---

# Azure credentials API - GET monitored services

# Azure credentials API - GET monitored services

* Справочник
* Опубликовано 28 июля 2022

Выводит список сервисов Azure, которые отслеживает конфигурация Azure.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужной конфигурации учётных данных Azure. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AzureMonitoredServicesDto](#openapi-definition-AzureMonitoredServicesDto) | Успешно |

### Объекты тела ответа

#### Объект `AzureMonitoredServicesDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| services | [AzureSupportingService](#openapi-definition-AzureSupportingService)[] | Список отслеживаемых сервисов Azure. Доступные сервисы перечислены операцией [/azure/supportedServices﻿](https://dt-url.net/wt42sdq?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации﻿](https://dt-url.net/kx2351b?dt=m).  Список метрик можно пропустить (задать значение null), в этом случае для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. Для встроенных сервисов изменение списка метрик не поддерживается, поэтому для них значение должно быть null. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AzureSupportingService`

Сервис, который нужно отслеживать.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric](#openapi-definition-AzureMonitoredMetric)[] | Список метрик, которые нужно отслеживать для этого сервиса. Он должен включать все рекомендуемые метрики. Если список равен null, для этого сервиса будет отслеживаться рекомендуемый список метрик. |
| name | string | Название сервиса. Действующие поддерживаемые названия сервисов можно узнать с помощью /azure/supportedServices restAPI |

#### Объект `AzureMonitoredMetric`

Метрика сервиса, которую нужно отслеживать.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список названий измерений метрики. Он должен включать все рекомендуемые измерения. |
| name | string | Название метрики сервиса. |

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



"name": "string"



}



],



"name": "string"



}



]



}
```

## Похожие темы

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настрой глубокий мониторинг кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")