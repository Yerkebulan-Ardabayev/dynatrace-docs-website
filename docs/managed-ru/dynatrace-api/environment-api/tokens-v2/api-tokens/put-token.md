---
title: Access tokens API - PUT a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token
---

# Access tokens API - PUT a token

# Access tokens API - PUT a token

* Справка
* Опубликовано 15 марта 2021 г.

Обновляет указанный токен API. Можно:

* Изменить имя токена и его область действия.
* Отозвать токен. Отозванный токен по-прежнему существует в среде, но использовать его нельзя.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens/{id}` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `apiTokens.write`.

О том, как получить и использовать такой токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID токена, который нужно обновить.  Токен, который используется для аутентификации самого запроса, отключить нельзя. | path | Обязательный |
| body | [ApiTokenUpdate](#openapi-definition-ApiTokenUpdate) | Тело JSON запроса. Содержит обновлённые параметры токена API. | body | Обязательный |

### Объекты тела запроса

#### Объект `ApiTokenUpdate`

Обновление токена API.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Токен включён (`true`) или отключён (`false`) | Опционально |
| name | string | Имя токена. | Опционально |
| scopes | string[] | Список областей действия, назначенных токену.  Помимо новых областей действия, нужно передать и уже существующие, которые нужно сохранить. Любая существующая область действия, отсутствующая в теле запроса, удаляется.  * `InstallerDownload`: интеграция PaaS, загрузка установщика. * `DataExport`: доступ к ленте проблем и событий, метрикам и топологии. * `PluginUpload`: загрузка Extension. * `SupportAlert`: интеграция PaaS, оповещение поддержки. * `AdvancedSyntheticIntegration`: интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: RUM Browser Extension. * `LogExport`: чтение логов. * `ReadConfig`: чтение конфигурации. * `WriteConfig`: запись конфигурации. * `DTAQLAccess`: пользовательские сессии. * `UserSessionAnonymization`: анонимизация данных пользовательских сессий по соображениям приватности данных. * `DataPrivacy`: изменение настроек приватности данных. * `CaptureRequestData`: захват данных запросов. * `Davis`: интеграция модуля Dynatrace, Davis. * `DssFileManagement`: управление файлами символикации мобильных приложений. * `RumJavaScriptTagManagement`: управление JavaScript-тегом Real User Monitoring. * `TenantTokenManagement`: управление токенами. * `ActiveGateCertManagement`: управление сертификатами ActiveGate. * `RestRequestForwarding`: получение данных из удалённой среды. * `ReadSyntheticData`: чтение синтетических мониторов, локаций и узлов. * `DataImport`: приём данных, например метрик и событий. * `syntheticExecutions.write`: запись выполнений синтетических мониторов. * `syntheticExecutions.read`: чтение результатов выполнения синтетических мониторов. * `auditLogs.read`: чтение журналов аудита. * `metrics.read`: чтение метрик. * `metrics.write`: запись метрик. * `entities.read`: чтение сущностей. * `entities.write`: запись сущностей. * `problems.read`: чтение проблем. * `problems.write`: запись проблем. * `events.read`: чтение событий. * `events.ingest`: приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенный). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательский). * `openpipeline.events_security`: OpenPipeline, приём событий безопасности (встроенный). * `openpipeline.events_security.custom`: OpenPipeline, приём событий безопасности (пользовательский). * `openpipeline.events_sdlc`: OpenPipeline, приём событий жизненного цикла разработки ПО (встроенный). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий жизненного цикла разработки ПО (пользовательский). * `openpipeline.events_smartscape`: OpenPipeline, приём событий Smartscape (встроенный). * `bizevents.ingest`: приём бизнес-событий. * `networkZones.read`: чтение сетевых зон. * `networkZones.write`: запись сетевых зон. * `activeGates.read`: чтение ActiveGateов. * `activeGates.write`: запись ActiveGateов. * `activeGateTokenManagement.read`: чтение токенов ActiveGate. * `activeGateTokenManagement.create`: создание токенов ActiveGate. * `activeGateTokenManagement.write`: запись токенов ActiveGate. * `agentTokenManagement.read`: чтение токенов агента. * `credentialVault.read`: чтение записей хранилища учётных данных. * `credentialVault.write`: запись записей хранилища учётных данных. * `extensions.read`: чтение расширений. * `extensions.write`: запись расширений. * `extensionConfigurations.read`: чтение конфигураций мониторинга расширений. * `extensionConfigurations.write`: запись конфигураций мониторинга расширений. * `extensionEnvironment.read`: чтение конфигураций среды расширений. * `extensionEnvironment.write`: запись конфигураций среды расширений. * `metrics.ingest`: приём метрик. * `attacks.read`: чтение атак. * `attacks.write`: запись настроек Application Protection. * `securityProblems.read`: чтение проблем безопасности. * `securityProblems.write`: запись проблем безопасности. * `syntheticLocations.read`: чтение синтетических локаций. * `syntheticLocations.write`: запись синтетических локаций. * `settings.read`: чтение настроек. * `settings.write`: запись настроек. * `tenantTokenRotation.write`: ротация токена тенанта. * `slo.read`: чтение SLO. * `slo.write`: запись SLO. * `releases.read`: чтение релизов. * `apiTokens.read`: чтение токенов API. * `apiTokens.write`: запись токенов API. * `openTelemetryTrace.ingest`: приём трасс OpenTelemetry. * `logs.read`: чтение логов. * `logs.ingest`: приём логов. * `geographicRegions.read`: чтение географических регионов. * `oneAgents.read`: чтение OneAgentов. * `oneAgents.write`: запись OneAgentов. * `traces.lookup`: поиск отдельной трассы. * `unifiedAnalysis.read`: чтение страницы Unified Analysis. * `hub.read`: чтение данных, связанных с Hub. * `hub.write`: управление метаданными элементов Hub. * `hub.install`: установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: чтение файлов сопоставления JavaScript. * `javaScriptMappingFiles.write`: запись файлов сопоставления JavaScript. * `extensionConfigurationActions.write`: действия для конфигураций мониторинга расширений. * `rumCookieNames.read`: чтение имён cookie RUM. * `adaptiveTrafficManagement.read`: чтение конфигурации выборки для Adaptive Traffic Management. * `rumManualInsertionTags.read`: чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: чтение обнаруженных метрик JMX через расширения. * `extensionDiscoveryPmi.read`: чтение обнаруженных метрик PMI через расширения. Элемент может принимать следующие значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_smartscape` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` | Опционально |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"enabled": true,



"name": "myToken",



"scopes": [



"InstallerDownload"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные некорректны. |
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

## Связанные темы

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")