---
title: Azure credentials API - POST new credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials
scraped: 2026-05-12T11:16:28.596059
---

# Azure credentials API - POST new credentials

# Azure credentials API - POST new credentials

* Reference
* Published Feb 25, 2020

Создаёт новую конфигурацию Azure credentials.

В теле не должно быть ID. Dynatrace Server назначает ID автоматически.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AzureCredentialsCreation](#openapi-definition-AzureCredentialsCreation) | JSON-тело запроса. Содержит параметры новой конфигурации Azure credentials. | body | Optional |

### Объекты тела запроса

#### Объект `AzureCredentialsCreation`

Конфигурация Azure credentials уровня приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или выключен (`false`).  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| appId | string | ID приложения (также называется client ID).  Поле **обязательно** при создании новой конфигурации credentials.  Поле игнорируется при обновлении, прежнее значение сохраняется. | Required |
| autoTagging | boolean | Автоматический сбор Azure-тегов включён (`true`) или выключен (`false`). | Required |
| directoryId | string | ID каталога (также называется tenant ID).  Поле **обязательно** при создании новой конфигурации credentials.  Поле игнорируется при обновлении, прежнее значение сохраняется. | Required |
| id | string | ID сущности Dynatrace для конфигурации Azure credentials. | Optional |
| key | string | Секретный ключ, связанный с ID приложения.  По соображениям безопасности GET-запросы возвращают это поле как `null`.  Отправляйте ключ при создании или обновлении конфигурации.  Поле **обязательно** при создании новой конфигурации credentials. Если поле опущено при обновлении, прежнее значение сохраняется. | Required |
| label | string | Уникальное имя конфигурации Azure credentials.  Допустимые символы: буквы, цифры и пробелы. Также разрешены специальные символы `.+-_`. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| monitorOnlyExcludingTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | Список Azure-тегов, исключаемых из мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, не мониторится.  Применяется только когда параметр **monitorOnlyTaggedEntities** установлен в `true`. | Optional |
| monitorOnlyTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | Список Azure-тегов для мониторинга.  Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, мониторится.  Применяется только когда параметр **monitorOnlyTaggedEntities** установлен в `true`. | Optional |
| monitorOnlyTaggedEntities | boolean | Мониторить только ресурсы с указанными Azure-тегами (`true`) или все ресурсы (`false`). | Required |
| supportingServices | [AzureSupportingService[]](#openapi-definition-AzureSupportingService) | **Устарело**. Для управления сервисами используйте операцию [/azure/credentials/{id}/services](https://dt-url.net/1w62s27). Встроенные сервисы здесь не поддерживаются.  Список Azure-сервисов для мониторинга. Доступные сервисы перечислены операцией [/azure/supportedServices](https://dt-url.net/wt42sdq).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации](https://dt-url.net/kx2351b).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. | Optional |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `CloudTag`

Облачный тег.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя тега. | Optional |
| value | string | Значение тега.  Если задано `null` или `""`, мониторятся ресурсы с любым значением тега. | Optional |

#### Объект `AzureSupportingService`

Сервис для мониторинга.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric[]](#openapi-definition-AzureMonitoredMetric) | Список метрик для мониторинга этого сервиса. Он должен включать все рекомендуемые метрики. Если список null, для мониторинга используется рекомендуемый список метрик для этого сервиса. | Optional |
| name | string | Имя сервиса. Допустимые имена поддерживаемых сервисов можно узнать через restAPI /azure/supportedServices | Required |

#### Объект `AzureMonitoredMetric`

Метрика сервиса для мониторинга.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Он должен включать все рекомендуемые измерения. | Required |
| name | string | Имя метрики сервиса. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая конфигурация Azure credentials создана. Тело ответа содержит ID конфигурации. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

В этом примере запрос создаёт новую конфигурацию Azure credentials уровня приложения.

API-токен передаётся в заголовке **Authorization**.

Поскольку тело запроса объёмное, в этом примере оно усечено в секции Curl. Полное тело смотрите в секции **Тело запроса**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials
```

#### Тело запроса

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

#### Тело ответа

```
{



"id": "AZURE_CREDENTIALS-357FDA338DAAF338",



"name": "Booking application"



}
```

#### Код ответа

201

## Связанные темы

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")