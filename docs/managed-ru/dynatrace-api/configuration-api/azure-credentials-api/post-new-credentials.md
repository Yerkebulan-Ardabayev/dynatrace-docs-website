---
title: Azure credentials API - POST new credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials
---

# Azure credentials API - POST new credentials

# Azure credentials API - POST new credentials

* Справочник
* Опубликовано 25 февраля 2020 г.

Создаёт новую конфигурацию учётных данных Azure.

Тело запроса не должно содержать ID. Сервер Dynatrace присваивает ID автоматически.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AzureCredentialsCreation](#openapi-definition-AzureCredentialsCreation) | Тело JSON запроса. Содержит параметры новой конфигурации учётных данных Azure. | body | Опционально |

### Объекты тела запроса

#### Объект `AzureCredentialsCreation`

Конфигурация учётных данных Azure уровня приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или выключен (`false`).  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, старое значение остаётся без изменений. | Опционально |
| appId | string | ID приложения (также называется client ID).  Поле **обязательно** при создании новой конфигурации учётных данных.  При обновлении поле игнорируется, старое значение остаётся без изменений. | Обязательно |
| autoTagging | boolean | Автоматический захват тегов Azure включён (`true`) или выключен (`false`). | Обязательно |
| directoryId | string | ID каталога (также называется tenant ID).  Поле **обязательно** при создании новой конфигурации учётных данных.  При обновлении поле игнорируется, старое значение остаётся без изменений. | Обязательно |
| id | string | ID сущности Dynatrace для конфигурации учётных данных Azure. | Опционально |
| key | string | Секретный ключ, связанный с ID приложения.  По соображениям безопасности GET-запросы возвращают это поле как `null`.  Передавай ключ при создании или обновлении конфигурации.  Поле **обязательно** при создании новой конфигурации учётных данных. Если поле опущено при обновлении, старое значение остаётся без изменений. | Обязательно |
| label | string | Уникальное имя конфигурации учётных данных Azure.  Допустимые символы: буквы, цифры и пробелы. Также допустимы специальные символы `.+-_`. | Обязательно |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| monitorOnlyExcludingTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, исключаемых из мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, не будет мониториться.  Применимо только когда параметр **monitorOnlyTaggedEntities** установлен в `true`. | Опционально |
| monitorOnlyTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, подлежащих мониторингу.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, мониторится.  Применимо только когда параметр **monitorOnlyTaggedEntities** установлен в `true`. | Опционально |
| monitorOnlyTaggedEntities | boolean | Мониторить только ресурсы, у которых заданы теги Azure (`true`), или все ресурсы (`false`). | Обязательно |
| supportingServices | [AzureSupportingService](#openapi-definition-AzureSupportingService)[] | **Устарело**. Для управления сервисами используй операцию [/azure/credentials/{id}/services﻿](https://dt-url.net/1w62s27?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов Azure, подлежащих мониторингу. Доступные сервисы перечисляются операцией [/azure/supportedServices﻿](https://dt-url.net/wt42sdq?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно проверить в [документации﻿](https://dt-url.net/kx2351b?dt=m).  Список метрик можно пропустить (установить в null), в этом случае для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. | Опционально |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |

#### Объект `CloudTag`

Облачный тег.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя тега. | Опционально |
| value | string | Значение тега.  Если установлено в `null` или `""`, тогда мониторятся ресурсы с любым значением тега. | Опционально |

#### Объект `AzureSupportingService`

Сервис, подлежащий мониторингу.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric](#openapi-definition-AzureMonitoredMetric)[] | Список метрик, подлежащих мониторингу для этого сервиса. Должен включать все рекомендуемые метрики. Если список равен null, для этого сервиса будет мониториться рекомендуемый список метрик. | Опционально |
| name | string | Имя сервиса. Действительные поддерживаемые имена сервисов можно узнать с помощью /azure/supportedServices restAPI | Обязательно |

#### Объект `AzureMonitoredMetric`

Метрика сервиса, подлежащая мониторингу.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Должен включать все рекомендуемые измерения. | Обязательно |
| name | string | Имя метрики сервиса. | Обязательно |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая конфигурация учётных данных Azure создана. Тело ответа содержит ID конфигурации. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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

### Модели тела JSON ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

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

Рекомендуется проверять payload перед отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

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

#### Модели тела ответа JSON

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

## Пример

В этом примере запрос создаёт новую конфигурацию учётных данных Azure на уровне приложения.

Токен API передаётся в заголовке **Authorization**.

Поскольку тело запроса объёмное, в этом примере раздела Curl оно усечено. Полное тело смотри в разделе **Request body**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials
```

#### Request body

```
{



"label": "Booking application",



"appId": "c4431dec-34fe-4d4c-ad93-aea38b4f944e",



"directoryId": "f836b63d-8c92-4ad8-a314-bb1eeka46aa1",



"key": "fzksjdfsjdfghsrtgbh",



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

#### Response body

```
{



"id": "AZURE_CREDENTIALS-357FDA338DAAF338",



"name": "Booking application"



}
```

#### Response code

201

## Связанные темы

* [Интеграции Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace на Azure с помощью OneAgent или OpenTelemetry.")