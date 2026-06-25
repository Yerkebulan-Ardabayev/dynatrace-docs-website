---
title: Azure credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/get-credentials
scraped: 2026-05-12T11:16:35.158582
---

# Azure credentials API - GET credentials

# Azure credentials API - GET credentials

* Reference
* Published Feb 25, 2020

Возвращает конфигурацию указанных Azure credentials.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |

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
| **200** | [AzureCredentials](#openapi-definition-AzureCredentials) | Успех |

### Объекты тела ответа

#### Объект `AzureCredentials`

Конфигурация Azure credentials уровня приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или выключен (`false`).  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, прежнее значение сохраняется. |
| appId | string | ID приложения (также называется client ID).  Поле **обязательно** при создании новой конфигурации credentials.  Поле игнорируется при обновлении, прежнее значение сохраняется. |
| autoTagging | boolean | Автоматический сбор Azure-тегов включён (`true`) или выключен (`false`). |
| directoryId | string | ID каталога (также называется tenant ID).  Поле **обязательно** при создании новой конфигурации credentials.  Поле игнорируется при обновлении, прежнее значение сохраняется. |
| id | string | ID сущности Dynatrace для конфигурации Azure credentials. |
| key | string | Секретный ключ, связанный с ID приложения.  По соображениям безопасности GET-запросы возвращают это поле как `null`.  Отправляйте ключ при создании или обновлении конфигурации.  Поле **обязательно** при создании новой конфигурации credentials. Если поле опущено при обновлении, прежнее значение сохраняется. |
| label | string | Уникальное имя конфигурации Azure credentials.  Допустимые символы: буквы, цифры и пробелы. Также разрешены специальные символы `.+-_`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| monitorOnlyExcludingTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | Список Azure-тегов, исключаемых из мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, не мониторится.  Применяется только когда параметр **monitorOnlyTaggedEntities** установлен в `true`. |
| monitorOnlyTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | Список Azure-тегов для мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, мониторится.  Применяется только когда параметр **monitorOnlyTaggedEntities** установлен в `true`. |
| monitorOnlyTaggedEntities | boolean | Мониторить только ресурсы с указанными Azure-тегами (`true`) или все ресурсы (`false`). |
| supportingServices | [AzureSupportingService[]](#openapi-definition-AzureSupportingService) | **Устарело**. Для управления сервисами используйте операцию [/azure/credentials/{id}/services](https://dt-url.net/1w62s27). Встроенные сервисы здесь не поддерживаются.  Список Azure-сервисов для мониторинга. Доступные сервисы перечислены операцией [/azure/supportedServices](https://dt-url.net/wt42sdq).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации](https://dt-url.net/kx2351b).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `CloudTag`

Облачный тег.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя тега. |
| value | string | Значение тега.  Если задано `null` или `""`, мониторятся ресурсы с любым значением тега. |

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



"active": true,



"appId": "string",



"autoTagging": true,



"directoryId": "string",



"id": "string",



"key": "string",



"label": "string",



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



"monitorOnlyExcludingTagPairs": [



{



"name": "string",



"value": "string"



}



],



"monitorOnlyTagPairs": [



{}



],



"monitorOnlyTaggedEntities": true,



"supportingServices": [



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

## Пример

В этом примере запрос возвращает параметры конфигурации Azure credentials **Booking application** с ID **AZURE\_CREDENTIALS-357FDA338DAAF338**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.189.0.20200225-180731"



},



"id": "AZURE_CREDENTIALS-357FDA338DAAF338",



"label": "Booking application",



"appId": "c4431dec-34fe-4d4c-ad93-aea38b4f944e",



"directoryId": "f836b63d-8c92-4ad8-a314-bb1eeka46aa1",



"key": null,



"active": true,



"autoTagging": true,



"monitorOnlyTaggedEntities": true,



"monitorOnlyTagPairs": [



{



"name": "bookingApp",



"value": "mobile"



},



{



"name": "bookingApp",



"value": "browser"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")