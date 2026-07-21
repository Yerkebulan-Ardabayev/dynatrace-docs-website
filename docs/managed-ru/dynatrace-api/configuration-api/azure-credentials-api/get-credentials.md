---
title: Azure credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/get-credentials
---

# Azure credentials API - GET credentials

# Azure credentials API - GET credentials

* Справка
* Опубликовано 25 февраля 2020 г.

Получает конфигурацию указанных Azure credentials.

Запрос возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужной конфигурации Azure credentials. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AzureCredentials](#openapi-definition-AzureCredentials) | Успешно |

### Объекты тела ответа

#### Объект `AzureCredentials`

Конфигурация учётных данных Azure на уровне приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или отключён (`false`).  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, старое значение остаётся без изменений. |
| appId | string | ID приложения (также называется client ID).  Поле **обязательно** при создании новой конфигурации credentials.  При обновлении поле игнорируется, старое значение остаётся без изменений. |
| autoTagging | boolean | Автоматический захват тегов Azure включён (`true`) или отключён (`false`). |
| directoryId | string | ID каталога (также называется tenant ID).  Поле **обязательно** при создании новой конфигурации credentials.  При обновлении поле игнорируется, старое значение остаётся без изменений. |
| id | string | ID сущности Dynatrace для конфигурации Azure credentials. |
| key | string | Секретный ключ, связанный с ID приложения.  По соображениям безопасности GET-запросы возвращают это поле как `null`.  Ключ нужно передавать при создании или обновлении конфигурации.  Поле **обязательно** при создании новой конфигурации credentials. Если поле опущено при обновлении, старое значение остаётся без изменений. |
| label | string | Уникальное имя конфигурации Azure credentials.  Допустимые символы: буквы, цифры и пробелы. Также допускаются специальные символы `.+-_`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| monitorOnlyExcludingTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, которые нужно исключить из мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, не будет мониториться.  Применимо только если параметр **monitorOnlyTaggedEntities** установлен в `true`. |
| monitorOnlyTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, которые нужно мониторить.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, мониторится.  Применимо только если параметр **monitorOnlyTaggedEntities** установлен в `true`. |
| monitorOnlyTaggedEntities | boolean | Мониторить только ресурсы с указанными тегами Azure (`true`) или все ресурсы (`false`). |
| supportingServices | [AzureSupportingService](#openapi-definition-AzureSupportingService)[] | **Устарело**. Для управления сервисами используй операцию [/azure/credentials/{id}/services﻿](https://dt-url.net/1w62s27?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов Azure, которые нужно мониторить. Доступные сервисы перечислены операцией [/azure/supportedServices﻿](https://dt-url.net/wt42sdq?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно проверить в [документации﻿](https://dt-url.net/kx2351b?dt=m).  Список метрик можно пропустить (установить в null), в этом случае для мониторинга будет выбран рекомендованный (по умолчанию) набор метрик и измерений. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

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
| value | string | Значение тега.  Если установлено в `null` или `""`, то мониторятся ресурсы с любым значением тега. |

#### Объект `AzureSupportingService`

Сервис, который нужно мониторить.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric](#openapi-definition-AzureMonitoredMetric)[] | Список метрик, которые нужно мониторить для этого сервиса. Он должен включать все рекомендованные метрики. Если список равен null, то будет мониториться рекомендованный список метрик для этого сервиса. |
| name | string | Имя сервиса. Допустимые названия поддерживаемых сервисов можно узнать через /azure/supportedServices restAPI |

#### Объект `AzureMonitoredMetric`

Метрика сервиса, которую нужно мониторить.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Он должен включать все рекомендованные измерения. |
| name | string | Имя метрики сервиса. |

### Модели тела ответа JSON

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

В этом примере запрос выводит список параметров конфигурации Azure credentials для **Booking application** с ID **AZURE\_CREDENTIALS-357FDA338DAAF338**.

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

## Похожие темы

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace на Azure с использованием OneAgent или OpenTelemetry.")