---
title: Export license data for 1 hour
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/export-license-data/get-export-license-data-hour
scraped: 2026-05-12T12:07:14.913245
---

# Export license data for 1 hour

# Export license data for 1 hour

* Updated on Nov 25, 2025

Этот API-вызов экспортирует агрегированное почасовое использование лицензии всех ваших окружений как ZIP-файл за один час.

Этот API совместим только с [классическим лицензированием Dynatrace](/managed/license/monitoring-consumption-classic "Узнайте, как рассчитывается потребление мониторинга Dynatrace для классического лицензирования.") и не содержит данных оплаченного потребления.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/license/consumption/hour`

## Формат ответа

Запрос возвращает payload `application/json`.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LicenseConsumption](#openapi-definition-LicenseConsumption) | Успех |
| **400** | - | Bad request. Указан некорректный timestamp. |
| **422** | - | Несовместимая лицензионная модель. |
| **500** | - | Операция не выполнена |

### Объекты тела ответа

#### Объект `LicenseConsumption`

Описывает час потребления лицензии для каждого окружения в кластере

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterUuid | string | Идентификатор кластера |
| environmentBillingEntries | [EnvironmentLicenseConsumption[]](#openapi-definition-EnvironmentLicenseConsumption) | Потребления окружений |
| timeFrameEnd | string | Конец timeframe экспорта данных потребления |
| timeFrameStart | string | Начало timeframe экспорта данных потребления |

#### Объект `EnvironmentLicenseConsumption`

Описывает потребление лицензии окружением

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMetrics | [CustomMetricDto[]](#openapi-definition-CustomMetricDto) | Потребление Custom metrics |
| davisDataUnits | [DavisDataUnitsUsageDto[]](#openapi-definition-DavisDataUnitsUsageDto) | Потребление Davis Data Units |
| downloads | [DownloadsDto[]](#openapi-definition-DownloadsDto) | Не используется |
| environmentUuid | string | Идентификатор окружения |
| highAvailabilityCluster | boolean | Указывает, имеет ли кластер избыточность через high availability. |
| hostUsages | [HostConsumption[]](#openapi-definition-HostConsumption) | Потребление мониторящихся хостов |
| internalUse | boolean | Окружение предназначено для внутреннего использования (например, self-monitoring) |
| logStorageUsageBytes | integer | Объём использования хранилища Log monitoring в байтах |
| logUploadVolumeBytes | integer | Объём загрузки Log monitoring в байтах |
| mobileSessionReplays | integer | Количество потреблённых mobile user session replays |
| mobileSessions | integer | Количество потреблённых mobile user sessions |
| newProblems | integer | Не используется |
| sessionReplays | integer | Количество потреблённых user session replays |
| syntheticBillingUsage | [SyntheticBillingUsageDto[]](#openapi-definition-SyntheticBillingUsageDto) | Потребление Synthetic monitoring |
| syntheticUsages | [SyntheticUsageDto[]](#openapi-definition-SyntheticUsageDto) | Не используется |
| totalRUMUserPropertiesUsed | integer | Количество определённых user session properties |
| trial | boolean | Флаг типа окружения |
| visits | integer | Количество потреблённых user sessions |

#### Объект `CustomMetricDto`

Потребление Custom metrics

| Элемент | Тип | Описание |
| --- | --- | --- |
| source | string | Имя источника определения custom metric |
| total | integer | Количество custom metrics |

#### Объект `DavisDataUnitsUsageDto`

Потребление Davis Data Units.

| Элемент | Тип | Описание |
| --- | --- | --- |
| pool | string | Имя пула Davis Data Units |
| total | number | Количество потреблённых Davis Data Units |

#### Объект `DownloadsDto`

Не используется

| Элемент | Тип | Описание |
| --- | --- | --- |
| downloadCount | integer | - |
| firstDownloadTime | string | - |
| type | string | - |
| version | string | - |

#### Объект `HostConsumption`

Описывает потребление лицензии мониторящимся хостом.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentUsages | [AgentConsumption[]](#openapi-definition-AgentConsumption) | Детали агента |
| hasContainers | boolean | Хост запускает контейнеры |
| hostCategory | string | Символ размера host unit |
| hostMemoryBytes | integer | RAM хоста в байтах |
| hostName | string | Не используется |
| infrastructureOnly | boolean | Режим мониторинга только инфраструктуры |
| osiId | integer | Идентификатор хоста |
| paas | boolean | Режим application-only мониторинга |
| passMemoryLimit | integer | Лимит памяти контейнера |
| premiumLogAnalytics | boolean | Premium Log monitoring |
| vendorTypeId | integer | Идентификатор вендора Platform as a Service |

#### Объект `AgentConsumption`

Описывает потребление лицензии OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentId | integer | Уникальный идентификатор агента |
| agentTypeId | integer | ID типа агента; 1 для OS-агента |
| agentUsageRecords | [AgentActivity[]](#openapi-definition-AgentActivity) | Периоды активности агента в течение часа |
| networkTraffic | integer | Не используется |

#### Объект `AgentActivity`

Описывает период времени, когда OneAgent активно потреблял лицензию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| endTime | string | Время окончания работы агента в течение часа |
| startTime | string | Время начала работы агента в течение часа |

#### Объект `SyntheticBillingUsageDto`

Потребление Synthetic monitoring

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitorTypeId | integer | ID типа Synthetic monitor; 1 для browser monitor, 2 для HTTP monitor |
| privateExecutions | integer | Количество выполнений с private locations |
| publicExecutions | integer | Количество выполнений с public locations |
| testId | integer | Уникальный идентификатор Synthetic monitor |

#### Объект `SyntheticUsageDto`

Не используется

| Элемент | Тип | Описание |
| --- | --- | --- |
| failureCount | integer | - |
| monitorDefinitionId | string | - |
| monitorDescription | string | - |
| monitorTypeId | integer | - |
| performedSyntheticActions | integer | - |
| successCount | integer | - |
| syntheticActionCount | integer | - |

### JSON-модели тела ответа

```
{



"clusterUuid": "string",



"environmentBillingEntries": [



{



"customMetrics": [



{



"source": "JMX, Dynatrace API",



"total": 1



}



],



"davisDataUnits": [



{



"pool": "Metrics, Serverless Functions, Log",



"total": 1



}



],



"downloads": [



{



"downloadCount": 1,



"firstDownloadTime": "string",



"type": "string",



"version": "string"



}



],



"environmentUuid": "string",



"highAvailabilityCluster": true,



"hostUsages": [



{



"agentUsages": [



{



"agentId": 1,



"agentTypeId": 1,



"agentUsageRecords": [



{



"endTime": "string",



"startTime": "string"



}



],



"networkTraffic": 1



}



],



"hasContainers": true,



"hostCategory": "string",



"hostMemoryBytes": 1,



"hostName": "string",



"infrastructureOnly": true,



"osiId": 1,



"paas": true,



"passMemoryLimit": 1,



"premiumLogAnalytics": true,



"vendorTypeId": 1



}



],



"internalUse": true,



"logStorageUsageBytes": 1,



"logUploadVolumeBytes": 1,



"mobileSessionReplays": 1,



"mobileSessions": 1,



"newProblems": 1,



"sessionReplays": 1,



"syntheticBillingUsage": [



{



"monitorTypeId": 1,



"privateExecutions": 1,



"publicExecutions": 1,



"testId": 1



}



],



"syntheticUsages": [



{



"failureCount": 1,



"monitorDefinitionId": "string",



"monitorDescription": "string",



"monitorTypeId": 1,



"performedSyntheticActions": 1,



"successCount": 1,



"syntheticActionCount": 1



}



],



"totalRUMUserPropertiesUsed": 1,



"trial": true,



"visits": 1



}



],



"timeFrameEnd": "string",



"timeFrameStart": "string"



}
```

## Пример

В этом примере запрашивается час данных лицензии за понедельник, 10 января 2022 10:00:00 GMT (1641808800000)

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/license/consumption/hour?startTs=1641810541000"



-H "accept: application/json; charset=utf-8"



-H "Authorization: Api-Token abcdefjhij1234567890"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/license/consumption/hour?startTs=1641808800000
```

#### Тело ответа

```
{



"clusterUuid": "02ed02ed-02ed-02ed-02ed-02ed02ed02ed",



"timeFrameStart": 1641808800000,



"timeFrameEnd": 1641812400000,



"environmentBillingEntries": [



{



"environmentUuid": "590939093-9093-9093-9093-909390903909",



"visits": 323,



"mobileSessions": 101,



"totalRUMUserPropertiesUsed": 10,



"newProblems": 0,



"hostUsages": [



{



"osiId": -5174977934749450000,



"hostName": null,



"hostCategory": "L",



"agentUsages": [



{



"networkTraffic": null,



"agentId": 2000000008,



"agentTypeId": 1,



"agentUsageRecords": [



{



"startTime": 1641808800000,



"endTime": 1641812400000



}



]



}



],



"infrastructureOnly": false,



"paas": false,



"passMemoryLimit": 0,



"vendorTypeId": null,



"hostMemoryBytes": 8538218496,



"premiumLogAnalytics": true,



"hasContainers": false



}



],



"downloads": [],



"syntheticUsages": [],



"syntheticBillingUsage": [],



"customMetrics": null,



"davisDataUnits": [



{



"pool": "Metrics",



"total": 31



},



{



"pool": "Log",



"total": 233



},



{



"pool": "Events",



"total": 123



},



{



"pool": "Traces",



"total": 15.46369



},



{



"pool": "Serverless",



"total": 4



}



],



"trial": false,



"internalUse": false,



"highAvailabilityCluster": false,



"logStorageUsageBytes": 0,



"logUploadVolumeBytes": 0,



"sessionReplays": 3123,



"mobileSessionReplays": 1232



}



]



}
```

#### Код ответа

`200`