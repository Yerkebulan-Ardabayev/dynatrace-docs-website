---
title: Tokens API v1 - PUT an existing token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/put-token
---

# Tokens API v1 - PUT an existing token

# Tokens API v1 - PUT an existing token

* Справка
* Обновлено 17 мая 2022 г.

Этот API устарел. Вместо него используй [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Обновляет указанный токен аутентификации Dynatrace API. Можно:

* Изменить название токена.
* Добавить или удалить область действия токена.
* Отозвать токен. Отозванный токен по-прежнему существует в среде, но использовать его нельзя.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `TenantTokenManagement`.

О том, как получить и использовать его, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID обновляемого токена.  Нельзя обновить токен, который используется для аутентификации самого запроса. | path | Обязательный |
| body | [UpdateToken](#openapi-definition-UpdateToken) | Тело JSON запроса. Содержит обновлённые параметры токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `UpdateToken`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Название токена. | Необязательный |
| revoked | boolean | Токен отозван (`true`) или активен (`false`). | Необязательный |
| scopes | string[] | Список разрешений, назначенных токену.  Помимо новых разрешений, нужно передать и уже существующие разрешения, которые нужно сохранить. Любое существующее разрешение, отсутствующее в полезной нагрузке, будет отозвано.  * `InstallerDownload`: PaaS-интеграция, скачивание инсталлятора. * `DataExport`: доступ к ленте проблем и событий, метрикам и топологии. * `PluginUpload`: загрузка Extension. * `SupportAlert`: PaaS-интеграция, оповещение поддержки. * `AdvancedSyntheticIntegration`: интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: RUM Browser Extension. * `LogExport`: чтение логов. * `ReadConfig`: чтение конфигурации. * `WriteConfig`: запись конфигурации. * `DTAQLAccess`: пользовательские сессии. * `UserSessionAnonymization`: анонимизация данных пользовательских сессий по требованиям приватности данных. * `DataPrivacy`: изменение настроек приватности данных. * `CaptureRequestData`: захват данных запроса. * `Davis`: интеграция модуля Dynatrace, Davis. * `DssFileManagement`: управление файлами символикации для мобильных устройств. * `RumJavaScriptTagManagement`: управление JavaScript-тегом Real User Monitoring. * `TenantTokenManagement`: управление токенами. * `ActiveGateCertManagement`: управление сертификатами ActiveGate. * `RestRequestForwarding`: получение данных из удалённой среды. * `ReadSyntheticData`: чтение синтетических мониторов, локаций и узлов. * `DataImport`: приём данных, например метрик и событий. * `syntheticExecutions.write`: запись выполнений синтетических мониторов. * `syntheticExecutions.read`: чтение результатов выполнения синтетических мониторов. * `auditLogs.read`: чтение журналов аудита. * `metrics.read`: чтение метрик. * `metrics.write`: запись метрик. * `entities.read`: чтение сущностей. * `entities.write`: запись сущностей. * `problems.read`: чтение проблем. * `problems.write`: запись проблем. * `events.read`: чтение событий. * `events.ingest`: приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенное). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательское). * `openpipeline.events_security`: OpenPipeline, приём событий безопасности (встроенное). * `openpipeline.events_security.custom`: OpenPipeline, приём событий безопасности (пользовательское). * `openpipeline.events_sdlc`: OpenPipeline, приём событий жизненного цикла разработки ПО (встроенное). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий жизненного цикла разработки ПО (пользовательское). * `openpipeline.events_smartscape`: OpenPipeline, приём событий Smartscape (встроенное). * `bizevents.ingest`: приём bizevents. * `networkZones.read`: чтение сетевых зон. * `networkZones.write`: запись сетевых зон. * `activeGates.read`: чтение ActiveGate. * `activeGates.write`: запись ActiveGate. * `activeGateTokenManagement.read`: чтение токенов ActiveGate. * `activeGateTokenManagement.create`: создание токенов ActiveGate. * `activeGateTokenManagement.write`: запись токенов ActiveGate. * `agentTokenManagement.read`: чтение токенов агента. * `credentialVault.read`: чтение записей хранилища учётных данных. * `credentialVault.write`: запись записей хранилища учётных данных. * `extensions.read`: чтение расширений. * `extensions.write`: запись расширений. * `extensionConfigurations.read`: чтение конфигураций мониторинга расширений. * `extensionConfigurations.write`: запись конфигураций мониторинга расширений. * `extensionEnvironment.read`: чтение конфигураций среды расширений. * `extensionEnvironment.write`: запись конфигураций среды расширений. * `metrics.ingest`: приём метрик. * `attacks.read`: чтение атак. * `attacks.write`: запись настроек Application Protection. * `securityProblems.read`: чтение проблем безопасности. * `securityProblems.write`: запись проблем безопасности. * `syntheticLocations.read`: чтение синтетических локаций. * `syntheticLocations.write`: запись синтетических локаций. * `settings.read`: чтение настроек. * `settings.write`: запись настроек. * `tenantTokenRotation.write`: ротация токена тенанта. * `slo.read`: чтение SLO. * `slo.write`: запись SLO. * `releases.read`: чтение релизов. * `apiTokens.read`: чтение токенов API. * `apiTokens.write`: запись токенов API. * `openTelemetryTrace.ingest`: приём трасс OpenTelemetry. * `logs.read`: чтение логов. * `logs.ingest`: приём логов. * `geographicRegions.read`: чтение географических регионов. * `oneAgents.read`: чтение OneAgent. * `oneAgents.write`: запись OneAgent. * `traces.lookup`: поиск отдельной трассы. * `unifiedAnalysis.read`: чтение страницы Unified Analysis. * `hub.read`: чтение данных, связанных с Hub. * `hub.write`: управление метаданными элементов Hub. * `hub.install`: установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: чтение файлов JavaScript-маппинга. * `javaScriptMappingFiles.write`: запись файлов JavaScript-маппинга. * `extensionConfigurationActions.write`: действия для конфигураций мониторинга расширений. * `rumCookieNames.read`: чтение имён cookie RUM. * `adaptiveTrafficManagement.read`: чтение конфигурации сэмплирования для Adaptive Traffic Management. * `rumManualInsertionTags.read`: чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: чтение обнаруженных метрик JMX через расширения. * `extensionDiscoveryPmi.read`: чтение обнаруженных метрик PMI через расширения. Элемент может содержать следующие значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_smartscape` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` | Необязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"name": "string",



"revoked": true,



"scopes": [



"InstallerDownload"



]



}
```

## Ответ

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Токен обновлён. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Нельзя обновить токен, который используется для аутентификации запроса. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Запрошенный токен не найден. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

В этом примере запрос запрашивает метаданные токена **admin** с ID **d5836312-5790-4e80-afcf-09971954c3ea**. Он назначает две новые области действия: **Real user monitoring JavaScript tag management** и **ActiveGate certificate management**. Имя и срок действия токена остаются без изменений. Код ответа **204** указывает на то, что обновление прошло успешно.

Токен, отображаемый в интерфейсе Dynatrace, до редактирования имеет следующие настройки:

![Dynatrace API authentication token](https://dt-cdn.net/images/token-permissions-1283-6453dccd8a.png)

Dynatrace API authentication token

Токен API передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса, чтобы опробовать его самостоятельно.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/d5836312-5790-4e80-afcf-09971954c3ea \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"scopes": [



"ExternalSyntheticIntegration",



"DataPrivacy",



"WriteConfig",



"DssFileManagement",



"LogExport",



"DTAQLAccess",



"ReadConfig",



"CaptureRequestData",



"ReadSyntheticData",



"DataExport",



"UserSessionAnonymization",



"MaintenanceWindows",



"LogImport",



"TenantTokenManagement",



"ActiveGateCertManagement",



"RumJavaScriptTagManagement"



]



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/tokens/d5836312-5790-4e80-afcf-09971954c3ea
```

#### Тело запроса

```
{



"scopes": [



"ExternalSyntheticIntegration",



"DataPrivacy",



"WriteConfig",



"DssFileManagement",



"LogExport",



"DTAQLAccess",



"ReadConfig",



"CaptureRequestData",



"ReadSyntheticData",



"DataExport",



"UserSessionAnonymization",



"MaintenanceWindows",



"LogImport",



"TenantTokenManagement",



"ActiveGateCertManagement",



"RumJavaScriptTagManagement"



]



}
```

#### Код ответа

204

#### Результат

Обновлённый токен, отображаемый в интерфейсе Dynatrace, имеет следующие параметры:

![Dynatrace API authentication token - updated](https://dt-cdn.net/images/token-permissions-upd-1283-3c4befedf4.png)

Dynatrace API authentication token - updated