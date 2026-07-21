---
title: Azure credentials API - PUT credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/put-credentials
---

# Azure credentials API - PUT credentials

# Azure credentials API - PUT credentials

* Справочник
* Опубликовано 25 февраля 2020

Обновляет существующую конфигурацию учётных данных Azure. Проверить статус подключения этих учётных данных можно через 10 минут с помощью запроса [GET credentials](/managed/dynatrace-api/configuration-api/azure-credentials-api/get-credentials "View an Azure credentials configuration via the Dynatrace API.").

Если конфигурация учётных данных с указанным ID не существует, создаётся новая конфигурация.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID конфигурации учётных данных Azure, которую нужно обновить. | path | Обязательный |
| body | [AzureCredentials](#openapi-definition-AzureCredentials) | Тело запроса JSON. Содержит обновлённые параметры конфигурации учётных данных Azure. | body | Опциональный |

### Объекты тела запроса

#### Объект `AzureCredentials`

Конфигурация учётных данных уровня приложения Azure.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или отключён (`false`). Если не задано при создании, используется значение `true`. Если поле опущено при обновлении, старое значение остаётся без изменений. | Опциональный |
| appId | string | ID приложения (также называется client ID). Поле **обязательно** при создании новой конфигурации учётных данных. При обновлении поле игнорируется, старое значение остаётся без изменений. | Опциональный |
| autoTagging | boolean | Автоматический захват тегов Azure включён (`true`) или отключён (`false`). | Обязательный |
| directoryId | string | ID каталога (также называется tenant ID). Поле **обязательно** при создании новой конфигурации учётных данных. При обновлении поле игнорируется, старое значение остаётся без изменений. | Опциональный |
| id | string | ID сущности Dynatrace для конфигурации учётных данных Azure. | Опциональный |
| key | string | Секретный ключ, связанный с ID приложения. По соображениям безопасности GET-запросы возвращают это поле как `null`. Ключ нужно передавать при создании или обновлении конфигурации. Поле **обязательно** при создании новой конфигурации учётных данных. Если поле опущено при обновлении, старое значение остаётся без изменений. | Опциональный |
| label | string | Уникальное имя конфигурации учётных данных Azure. Допустимые символы, буквы, цифры и пробелы. Также допускаются специальные символы `.+-_`. | Обязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| monitorOnlyExcludingTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, которые нужно исключить из мониторинга. Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, не будет мониториться. Применяется только если параметр **monitorOnlyTaggedEntities** установлен в `true`. | Опциональный |
| monitorOnlyTagPairs | [CloudTag](#openapi-definition-CloudTag)[] | Список тегов Azure, которые нужно мониторить. Можно указать до 20 тегов. Ресурс, помеченный *любым* из указанных тегов, мониторится. Применяется только если параметр **monitorOnlyTaggedEntities** установлен в `true`. | Опциональный |
| monitorOnlyTaggedEntities | boolean | Мониторить только ресурсы с указанными тегами Azure (`true`) или все ресурсы (`false`). | Обязательный |
| supportingServices | [AzureSupportingService](#openapi-definition-AzureSupportingService)[] | **Устарело**. Для управления сервисами используй операцию [/azure/credentials/{id}/services﻿](https://dt-url.net/1w62s27?dt=m). Встроенные сервисы здесь не поддерживаются. Список сервисов Azure, которые нужно мониторить. Доступные сервисы перечислены операцией [/azure/supportedServices﻿](https://dt-url.net/wt42sdq?dt=m). Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно проверить в [документации﻿](https://dt-url.net/kx2351b?dt=m). Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. | Опциональный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `CloudTag`

Облачный тег.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя тега. | Опциональный |
| value | string | Значение тега. Если задано `null` или `""`, то мониторятся ресурсы с любым значением тега. | Опциональный |

#### Объект `AzureSupportingService`

Сервис, который нужно мониторить.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric](#openapi-definition-AzureMonitoredMetric)[] | Список метрик, которые нужно мониторить для этого сервиса. Должен включать все рекомендуемые метрики. Если список равен null, для мониторинга будет использован рекомендуемый список метрик для этого сервиса. | Опциональный |
| name | string | Имя сервиса. Допустимые поддерживаемые имена сервисов можно узнать с помощью /azure/supportedServices restAPI | Обязательный |

#### Объект `AzureMonitoredMetric`

Метрика сервиса, которую нужно мониторить.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. Должен включать все рекомендуемые измерения. | Обязательный |
| name | string | Имя метрики сервиса. | Обязательный |

### Пример JSON тела запроса

Это пример тела запроса, показывающий возможные элементы. Его нужно скорректировать для использования в реальном запросе.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Новая конфигурация учётных данных Azure создана. Тело ответа содержит ID конфигурации. |
| **204** | - | Успешно. Конфигурация учётных данных Azure обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недопустимы. |

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
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Примеры JSON тела ответа

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

## Валидация полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её в составе реального запроса. Код ответа **204** означает, что полезная нагрузка допустима.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читайте в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

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

В этом примере запрос обновляет конфигурацию учётных данных Azure из [примера запроса POST](/managed/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials#example "Создание конфигурации учётных данных Azure через Dynatrace API.").

Запрос указывает новый пароль и меняет режим мониторинга с ресурсов с указанными тегами на все ресурсы:

* значение **monitorOnlyTaggedEntities** изменено на `false`
* массив **monitorOnlyTagPairs** пуст.

Токен API передаётся в заголовке **Authorization**.

Поскольку тело запроса объёмное, в разделе Curl этого примера оно сокращено. Полное тело смотрите в разделе **Тело запроса**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338
```

#### Тело запроса

```
{



"id": "AZURE_CREDENTIALS-357FDA338DAAF338",



"label": "Booking application",



"appId": "c4431dec-34fe-4d4c-ad93-aea38b4f944e",



"directoryId": "f836b63d-8c92-4ad8-a314-bb1eeka46aa1",



"key": "p459-346vs;ojkg[]",



"active": true,



"autoTagging": true,



"monitorOnlyTaggedEntities": false,



"monitorOnlyTagPairs": []



}
```

#### Код ответа

204

## Похожие темы

* [Интеграции Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace на Azure с помощью OneAgent или OpenTelemetry.")