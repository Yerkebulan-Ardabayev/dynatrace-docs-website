---
title: Azure credentials API - DELETE credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/delete-credentials
---

# Azure credentials API - DELETE credentials

# Azure credentials API - DELETE credentials

* Справка
* Опубликовано 25 февр. 2020 г.

Удаляет указанную конфигурацию учётных данных Azure. Отменить удаление нельзя.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужной конфигурации учётных данных Azure. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AzureCredentials](#openapi-definition-AzureCredentials) | Успех |

### Объекты тела ответа

#### Объект `AzureCredentials`

Конфигурация учётных данных уровня приложения Azure.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или выключен (`false`).  Если не задано при создании, используется значение `true`.  Если поле не указано при обновлении, старое значение сохраняется без изменений. |
| appId | string | ID приложения (также называется client ID).  Поле **обязательно** при создании новой конфигурации учётных данных.  При обновлении поле игнорируется, старое значение сохраняется без изменений. |
| autoTagging | boolean | Автоматический захват тегов Azure включён (`true`) или выключен (`false`). |
| directoryId | string | ID каталога (также называется tenant ID).  Поле **обязательно** при создании новой конфигурации учётных данных.  При обновлении поле игнорируется, старое значение сохраняется без изменений. |
| id | string | ID сущности Dynatrace конфигурации учётных данных Azure. |
| key | string | Секретный ключ, связанный с ID приложения.  По соображениям безопасности GET-запросы возвращают это поле как `null`.  Ключ нужно передавать при создании или обновлении конфигурации.  Поле **обязательно** при создании новой конфигурации учётных данных. Если поле не указано при обновлении, старое значение сохраняется без изменений. |
| label | string | Уникальное имя конфигурации учётных данных Azure.  Разрешены буквы, цифры и пробелы, а также специальные символы `.+-_`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| monitorOnlyExcludingTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, которые нужно исключить из мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, не будет мониториться.  Применимо только если параметр **monitorOnlyTaggedEntities** установлен в `true`. |
| monitorOnlyTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, которые нужно мониторить.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, мониторится.  Применимо только если параметр **monitorOnlyTaggedEntities** установлен в `true`. |
| monitorOnlyTaggedEntities | boolean | Мониторить только ресурсы с указанными тегами Azure (`true`) или все ресурсы (`false`). |
| supportingServices | [AzureSupportingService](#openapi-definition-AzureSupportingService)[] | **Устарело**. Для управления сервисами используй операцию [/azure/credentials/{id}/services﻿](https://dt-url.net/1w62s27?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов Azure, которые нужно мониторить. Доступные сервисы перечислены операцией [/azure/supportedServices﻿](https://dt-url.net/wt42sdq?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации﻿](https://dt-url.net/kx2351b?dt=m).  Список метрик можно не указывать (значение null), тогда для мониторинга выбирается рекомендуемый (стандартный) набор метрик и измерений. |

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
| value | string | Значение тега.  Если установлено в `null` или `""`, мониторятся ресурсы с любым значением тега. |

#### Объект `AzureSupportingService`

Сервис, который нужно мониторить.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric](#openapi-definition-AzureMonitoredMetric)[] | Список метрик, которые нужно мониторить для этого сервиса. Должен включать все рекомендуемые метрики. Если список равен null, для мониторинга будет использован рекомендуемый список метрик для этого сервиса. |
| name | string | Имя сервиса. Допустимые поддерживаемые имена сервисов можно узнать через /azure/supportedServices restAPI |

#### Объект `AzureMonitoredMetric`

Метрика сервиса, которую нужно мониторить.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Должен включать все рекомендуемые измерения. |
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

В этом примере запрос удаляет учётные данные уровня приложения Azure из [примера POST-запроса](/managed/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials#example "Создание конфигурации учётных данных Azure через Dynatrace API."). Код ответа **204** означает, что удаление выполнено успешно.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338
```

#### Код ответа

204

## Похожие темы

* [Интеграции Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")