---
title: Tokens API v1 - GET token metadata
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/get-token-metadata
---

# Tokens API v1 - GET token metadata

# Tokens API v1 - GET token metadata

* Справочник
* Обновлено 17 мая 2022 г.

Этот API устарел. Вместо него используй [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Выводит список метаданных токена аутентификации Dynatrace API по ID токена. Сам токен при этом **не** раскрывается.

Также можно получить метаданные, передав сам токен через вызов [POST token metadata](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Learn how to use the Dynatrace API to look up the metadata of a Dynatrace API authentication token.").

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `TenantTokenManagement`.

О том, как получить и использовать такой токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного токена. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Успешно |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Запрошенный токен не найден. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `TokenMetadata`

Метаданные токена.

| Элемент | Тип | Описание |
| --- | --- | --- |
| created | integer | Время создания в виде unix-времени в миллисекундах. |
| expires | integer | Время истечения срока действия в виде unix-времени в миллисекундах. |
| id | string | ID токена. |
| lastUse | integer | Unix-время в миллисекундах последнего использования токена. |
| name | string | Имя токена. |
| personalAccessToken | boolean | Указывает, является ли токен [персональным токеном доступа﻿](https://dt-url.net/wm03sop?dt=m) (`true`) или токеном API (`false`). |
| revoked | boolean | Статус отзыва токена. Отозванные токены отключены. |
| scopes | string[] | Список областей действия, назначенных токену. Элемент может содержать следующие значения * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_smartscape` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |
| userId | string | Владелец токена. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может содержать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

```
{



"created": 1554076800000,



"expires": 1585976400000,



"id": "acbed0c4-4ef1-4303-991f-102510a69322",



"lastUse": 1554354000000,



"name": "myToken",



"personalAccessToken": true,



"revoked": true,



"scopes": [



"DataExport",



"ReadConfig",



"WriteConfig"



],



"userId": "john.smith"



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

В этом примере запрос получает метаданные токена **admin**, у которого ID **d5836312-5790-4e80-afcf-09971954c3ea**.

Токен API передаётся в заголовке **Authorization**.

Токен, как он отображается в интерфейсе Dynatrace, имеет следующие настройки:

![Токен аутентификации Dynatrace API](https://dt-cdn.net/images/token-permissions-1283-6453dccd8a.png)

Токен аутентификации Dynatrace API

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/d5836312-5790-4e80-afcf-09971954c3ea \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/tokens/d5836312-5790-4e80-afcf-09971954c3ea
```

#### Тело ответа

```
{



"id": "d5836312-5790-4e80-afcf-09971954c3ea",



"name": "admin",



"userId": "admin@mysampleenv.com",



"created": "2019-03-13T09:45:40Z",



"lastUse": "2019-04-04T09:13:23Z",



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



"TenantTokenManagement"



]



}
```

#### Код ответа

200