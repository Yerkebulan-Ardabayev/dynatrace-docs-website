---
title: Tokens API v1 - POST новый токен
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/post-new-token
scraped: 2026-05-12T12:11:13.535372
---

# Tokens API v1 - POST новый токен

# Tokens API v1 - POST новый токен

* Справочник
* Обновлено 17 мая 2022 г.

Этот API устарел. Используйте вместо него [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.").

Создаёт новый токен аутентификации Dynatrace API. Ответ содержит вновь созданный токен.

Новый токен принадлежит тому же пользователю, который владеет токеном, используемым для аутентификации вызова.

Запрос потребляет payload `application/json`.

Запрос возвращает один из следующих типов payload:

* `application/json`
* `text/plain`
* `text/csv`

Используйте заголовок **Accept**, чтобы задать требуемый тип ответа.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens` |

## Аутентификация

Для выполнения запроса необходим access token со scope `TenantTokenManagement`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| body | [CreateToken](#openapi-definition-CreateToken) | JSON-тело запроса. Содержит параметры нового токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `CreateToken`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| expiresIn | [Duration](#openapi-definition-Duration) | Задаёт период времени. | Опциональный |
| name | string | Имя токена. | Обязательный |
| scopes | string[] | Список scope, назначаемых токену.  * `InstallerDownload`: PaaS-интеграция, скачивание инсталлятора. * `DataExport`: Доступ к ленте проблем и событий, метрикам и топологии. * `PluginUpload`: Загрузка расширения. * `SupportAlert`: PaaS-интеграция, оповещение поддержки. * `AdvancedSyntheticIntegration`: Интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: Создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: Браузерное расширение RUM. * `LogExport`: Чтение логов. * `ReadConfig`: Чтение конфигурации. * `WriteConfig`: Запись конфигурации. * `DTAQLAccess`: Пользовательские сессии. * `UserSessionAnonymization`: Анонимизация данных пользовательских сессий в целях конфиденциальности данных. * `DataPrivacy`: Изменение настроек конфиденциальности данных. * `CaptureRequestData`: Захват данных запросов. * `Davis`: Интеграция модуля Dynatrace, Davis. * `DssFileManagement`: Управление файлами мобильной символикации. * `RumJavaScriptTagManagement`: Управление JavaScript-тегами мониторинга реальных пользователей. * `TenantTokenManagement`: Управление токенами. * `ActiveGateCertManagement`: Управление сертификатами ActiveGate. * `RestRequestForwarding`: Получение данных из удалённой среды. * `ReadSyntheticData`: Чтение синтетических мониторов, локаций и узлов. * `DataImport`: Приём данных, например метрик и событий. * `syntheticExecutions.write`: Запись выполнений синтетических мониторов. * `syntheticExecutions.read`: Чтение результатов выполнения синтетических мониторов. * `auditLogs.read`: Чтение журналов аудита. * `metrics.read`: Чтение метрик. * `metrics.write`: Запись метрик. * `entities.read`: Чтение сущностей. * `entities.write`: Запись сущностей. * `problems.read`: Чтение проблем. * `problems.write`: Запись проблем. * `events.read`: Чтение событий. * `events.ingest`: Приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенные). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательские). * `openpipeline.events_security`: OpenPipeline, приём событий безопасности (встроенные). * `openpipeline.events_security.custom`: OpenPipeline, приём событий безопасности (пользовательские). * `openpipeline.events_sdlc`: OpenPipeline, приём событий жизненного цикла разработки ПО (встроенные). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий жизненного цикла разработки ПО (пользовательские). * `bizevents.ingest`: Приём bizevents. * `networkZones.read`: Чтение сетевых зон. * `networkZones.write`: Запись сетевых зон. * `activeGates.read`: Чтение ActiveGate. * `activeGates.write`: Запись ActiveGate. * `activeGateTokenManagement.read`: Чтение токенов ActiveGate. * `activeGateTokenManagement.create`: Создание токенов ActiveGate. * `activeGateTokenManagement.write`: Запись токенов ActiveGate. * `agentTokenManagement.read`: Чтение токенов агента. * `credentialVault.read`: Чтение записей хранилища учётных данных. * `credentialVault.write`: Запись записей хранилища учётных данных. * `extensions.read`: Чтение расширений. * `extensions.write`: Запись расширений. * `extensionConfigurations.read`: Чтение конфигураций мониторинга расширений. * `extensionConfigurations.write`: Запись конфигураций мониторинга расширений. * `extensionEnvironment.read`: Чтение конфигураций среды расширений. * `extensionEnvironment.write`: Запись конфигураций среды расширений. * `metrics.ingest`: Приём метрик. * `attacks.read`: Чтение атак. * `attacks.write`: Запись настроек Application Protection. * `securityProblems.read`: Чтение проблем безопасности. * `securityProblems.write`: Запись проблем безопасности. * `syntheticLocations.read`: Чтение синтетических локаций. * `syntheticLocations.write`: Запись синтетических локаций. * `settings.read`: Чтение настроек. * `settings.write`: Запись настроек. * `tenantTokenRotation.write`: Ротация tenant-токена. * `slo.read`: Чтение SLO. * `slo.write`: Запись SLO. * `releases.read`: Чтение релизов. * `apiTokens.read`: Чтение API-токенов. * `apiTokens.write`: Запись API-токенов. * `openTelemetryTrace.ingest`: Приём трейсов OpenTelemetry. * `logs.read`: Чтение логов. * `logs.ingest`: Приём логов. * `geographicRegions.read`: Чтение географических регионов. * `oneAgents.read`: Чтение OneAgent. * `oneAgents.write`: Запись OneAgent. * `traces.lookup`: Поиск одного трейса. * `unifiedAnalysis.read`: Чтение страницы Unified Analysis. * `hub.read`: Чтение данных, связанных с Hub. * `hub.write`: Управление метаданными элементов Hub. * `hub.install`: Установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: Чтение файлов сопоставления JavaScript. * `javaScriptMappingFiles.write`: Запись файлов сопоставления JavaScript. * `extensionConfigurationActions.write`: Действия для конфигураций мониторинга расширений. * `rumCookieNames.read`: Чтение имён cookie RUM. * `adaptiveTrafficManagement.read`: Чтение конфигурации сэмплирования для Adaptive Traffic Management. * `rumManualInsertionTags.read`: Чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: Чтение обнаруженных JMX-метрик через расширения. Элемент может принимать значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` | Обязательный |

#### Объект `Duration`

Задаёт период времени.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| unit | string | Единица времени.  Если не задано, используется миллисекунда. Элемент может принимать значения * `DAYS` * `HOURS` * `MILLIS` * `MINUTES` * `SECONDS` | Опциональный |
| value | integer | Количество времени. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"expiresIn": {



"unit": "DAYS",



"value": 1



},



"name": "string",



"scopes": [



"InstallerDownload"



]



}
```

## Заголовки запроса

| Значение заголовка Accept | Описание |
| --- | --- |
| `application/json` | Ответ содержит JSON-payload с токеном. |
| `text/plain` | Ответ содержит токен в формате простого текста. |
| `accept: text/csv; header=present; charset=utf-8` | Ответ содержит токен в формате CSV. |
| `accept: text/csv; header=absent; charset=utf-8` | Ответ содержит токен в формате CSV, которому предшествует заголовок **token**. |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [Token](#openapi-definition-Token) | Успех. Токен создан. Тело ответа содержит сам токен. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. Тело ответа содержит подробности. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Token`

| Элемент | Тип | Описание |
| --- | --- | --- |
| token | string | Токен аутентификации Dynatrace API. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"token": "abcdefjhij1234567890"



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

## Пример

В этом примере запрос создаёт новый токен с именем **REST example**. Он действителен **24 часа** и имеет следующие scope:

* Доступ к ленте проблем и событий, метрикам и топологии
* Чтение конфигурации
* Запись конфигурации

Заголовок **Accept** задаёт тип содержимого ответа как `text/plain`.

Код ответа **201** указывает, что создание прошло успешно. Ответ содержит новый токен в виде простого текста.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/ \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-H 'Accept: text/plain'



-d '{



"name": "REST example",



"scopes": [



"WriteConfig",



"ReadConfig",



"DataExport"



],



"expiresIn": {



"value": 24,



"unit": "HOURS"



}



}



'
```

#### Тело запроса

```
{



"name": "REST example",



"scopes": ["WriteConfig", "ReadConfig", "DataExport"],



"expiresIn": {



"value": 24,



"unit": "HOURS"



}



}
```

#### Тело ответа

```
0987654321jihgfedcba
```

#### Код ответа

201

#### Результат

Новый токен выглядит так в интерфейсе Dynatrace:

![Токен аутентификации Dynatrace API, новый](https://dt-cdn.net/images/token-permissions-new-1289-2369d8c7e5.png)

Токен аутентификации Dynatrace API, новый