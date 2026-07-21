---
title: Tokens API v1 - POST a new token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/post-new-token
---

# Tokens API v1 - POST a new token

# Tokens API v1 - POST a new token

* Справка
* Обновлено 17 мая 2022 г.

Этот API устарел. Вместо него используй [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Создаёт новый токен аутентификации Dynatrace API. Ответ содержит новосозданный токен.

Новый токен принадлежит тому же пользователю, которому принадлежит токен, использованный для аутентификации вызова.

Запрос принимает полезную нагрузку `application/json`.

Запрос формирует полезную нагрузку одного из следующих типов:

* `application/json`
* `text/plain`
* `text/csv`

Используй заголовок **Accept**, чтобы задать нужный тип ответа.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `TenantTokenManagement`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CreateToken](#openapi-definition-CreateToken) | Тело JSON запроса. Содержит параметры нового токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `CreateToken`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| expiresIn | [Duration](#openapi-definition-Duration) | Задаёт период времени. | Опциональный |
| name | string | Имя токена. | Обязательный |
| scopes | string[] | Список scope, назначаемых токену.  * `InstallerDownload`: PaaS-интеграция, загрузка установщика. * `DataExport`: доступ к ленте проблем и событий, метрикам и топологии. * `PluginUpload`: загрузка Extension. * `SupportAlert`: PaaS-интеграция, оповещение поддержки. * `AdvancedSyntheticIntegration`: интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: RUM Browser Extension. * `LogExport`: чтение логов. * `ReadConfig`: чтение конфигурации. * `WriteConfig`: запись конфигурации. * `DTAQLAccess`: пользовательские сессии. * `UserSessionAnonymization`: анонимизация данных пользовательских сессий по соображениям приватности данных. * `DataPrivacy`: изменение настроек приватности данных. * `CaptureRequestData`: захват данных запросов. * `Davis`: интеграция модуля Dynatrace, Davis. * `DssFileManagement`: управление файлами символикации мобильных приложений. * `RumJavaScriptTagManagement`: управление JavaScript-тегом real user monitoring. * `TenantTokenManagement`: управление токенами. * `ActiveGateCertManagement`: управление сертификатами ActiveGate. * `RestRequestForwarding`: получение данных из удалённой среды. * `ReadSyntheticData`: чтение синтетических мониторов, локаций и узлов. * `DataImport`: приём данных, например метрик и событий. * `syntheticExecutions.write`: запись выполнений синтетических мониторов. * `syntheticExecutions.read`: чтение результатов выполнения синтетических мониторов. * `auditLogs.read`: чтение журналов аудита. * `metrics.read`: чтение метрик. * `metrics.write`: запись метрик. * `entities.read`: чтение сущностей. * `entities.write`: запись сущностей. * `problems.read`: чтение проблем. * `problems.write`: запись проблем. * `events.read`: чтение событий. * `events.ingest`: приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенный). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательский). * `openpipeline.events_security`: OpenPipeline, приём событий безопасности (встроенный). * `openpipeline.events_security.custom`: OpenPipeline, приём событий безопасности (пользовательский). * `openpipeline.events_sdlc`: OpenPipeline, приём событий жизненного цикла разработки ПО (встроенный). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий жизненного цикла разработки ПО (пользовательский). * `openpipeline.events_smartscape`: OpenPipeline, приём событий Smartscape (встроенный). * `bizevents.ingest`: приём бизнес-событий. * `networkZones.read`: чтение сетевых зон. * `networkZones.write`: запись сетевых зон. * `activeGates.read`: чтение ActiveGate. * `activeGates.write`: запись ActiveGate. * `activeGateTokenManagement.read`: чтение токенов ActiveGate. * `activeGateTokenManagement.create`: создание токенов ActiveGate. * `activeGateTokenManagement.write`: запись токенов ActiveGate. * `agentTokenManagement.read`: чтение токенов агентов. * `credentialVault.read`: чтение записей хранилища учётных данных. * `credentialVault.write`: запись записей хранилища учётных данных. * `extensions.read`: чтение extensions. * `extensions.write`: запись extensions. * `extensionConfigurations.read`: чтение конфигураций мониторинга extension. * `extensionConfigurations.write`: запись конфигураций мониторинга extension. * `extensionEnvironment.read`: чтение конфигураций окружения extension. * `extensionEnvironment.write`: запись конфигураций окружения extension. * `metrics.ingest`: приём метрик. * `attacks.read`: чтение атак. * `attacks.write`: запись настроек Application Protection. * `securityProblems.read`: чтение проблем безопасности. * `securityProblems.write`: запись проблем безопасности. * `syntheticLocations.read`: чтение синтетических локаций. * `syntheticLocations.write`: запись синтетических локаций. * `settings.read`: чтение настроек. * `settings.write`: запись настроек. * `tenantTokenRotation.write`: ротация токена клиента. * `slo.read`: чтение SLO. * `slo.write`: запись SLO. * `releases.read`: чтение релизов. * `apiTokens.read`: чтение токенов API. * `apiTokens.write`: запись токенов API. * `openTelemetryTrace.ingest`: приём трасс OpenTelemetry. * `logs.read`: чтение логов. * `logs.ingest`: приём логов. * `geographicRegions.read`: чтение географических регионов. * `oneAgents.read`: чтение OneAgent. * `oneAgents.write`: запись OneAgent. * `traces.lookup`: поиск отдельной трассы. * `unifiedAnalysis.read`: чтение страницы Unified Analysis. * `hub.read`: чтение данных, связанных с Hub. * `hub.write`: управление метаданными элементов Hub. * `hub.install`: установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: чтение файлов маппинга JavaScript. * `javaScriptMappingFiles.write`: запись файлов маппинга JavaScript. * `extensionConfigurationActions.write`: действия для конфигураций мониторинга extension. * `rumCookieNames.read`: чтение имён cookie RUM. * `adaptiveTrafficManagement.read`: чтение конфигурации семплирования для Adaptive Traffic Management. * `rumManualInsertionTags.read`: чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: чтение обнаруженных JMX-метрик через extensions. * `extensionDiscoveryPmi.read`: чтение обнаруженных PMI-метрик через extensions. Элемент может принимать следующие значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_smartscape` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` | Обязательный |

#### Объект `Duration`

Задаёт период времени.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| unit | string | Единица времени.  Если не задана, используется миллисекунда. Элемент может принимать следующие значения * `DAYS` * `HOURS` * `MILLIS` * `MINUTES` * `SECONDS` | Опциональный |
| value | integer | Величина времени. | Обязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать перед использованием в реальном запросе.

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
| `application/json` | Ответ содержит JSON полезную нагрузку с токеном. |
| `text/plain` | Ответ содержит токен в текстовом формате. |
| `accept: text/csv; header=present; charset=utf-8` | Ответ содержит токен в формате CSV. |
| `accept: text/csv; header=absent; charset=utf-8` | Ответ содержит токен в формате CSV, перед которым идёт заголовок **token**. |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [Token](#openapi-definition-Token) | Успешно. Токен создан. Тело ответа содержит сам токен. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. Подробности приведены в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Token`

| Элемент | Тип | Описание |
| --- | --- | --- |
| token | string | Dynatrace API токен аутентификации. |

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

### Модели тела ответа JSON

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

В этом примере запрос создаёт новый токен с именем **REST example**. Он действителен в течение **24 часов** и имеет следующие области действия:

* Доступ к ленте проблем и событий, метрикам и топологии
* Чтение конфигурации
* Запись конфигурации

Заголовок **Accept** задаёт тип содержимого ответа как `text/plain`.

Код ответа **201** означает, что создание прошло успешно. Ответ содержит новый токен в виде обычного текста.

Токен API передаётся в заголовке **Authorization**.

Можно скачать или скопировать тело примера запроса, чтобы попробовать его самостоятельно.

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

![Dynatrace API токен аутентификации - новый](https://dt-cdn.net/images/token-permissions-new-1289-2369d8c7e5.png)

Dynatrace API токен аутентификации - новый