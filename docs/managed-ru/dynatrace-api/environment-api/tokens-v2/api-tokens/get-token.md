---
title: Access tokens API - GET a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/get-token
---

# Access tokens API - GET a token

# Access tokens API - GET a token

* Справочник
* Опубликовано 15 марта 2021 г.

Получает метаданные токена API по его ID.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace для Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens/{id}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `apiTokens.read`.

О том, как получить и использовать такой токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID токена. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApiToken](#openapi-definition-ApiToken) | Успешно |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
| **404** | - | Ошибка. Запрошенный ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiToken`

Метаданные токена API.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalMetadata | object | Содержит дополнительные свойства для определённых типов токенов. Примеры:  * свойство `dashboardId` для токенов совместного доступа к дашбордам; * свойство `reportId` для токенов совместного доступа к отчётам |
| creationDate | string | Дата создания токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| enabled | boolean | Токен включён (`true`) или отключён (`false`). |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  Если не задана, токен никогда не истекает. |
| id | string | ID токена, состоящий из префикса и публичной части токена. |
| lastUsedDate | string | Дата последнего использования токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| lastUsedIpAddress | string | IP-адрес последнего использования токена. |
| modifiedDate | string | Дата последнего изменения токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). Обновление областей действия или имени считается изменением, включение или отключение токена, нет. |
| name | string | Имя токена. |
| owner | string | Владелец токена. |
| personalAccessToken | boolean | Токен является [персональным токеном доступа﻿](https://dt-url.net/wm03sop?dt=m) (`true`) или токеном API (`false`). |
| scopes | string[] | Список областей действия, назначенных токену. Элемент может принимать следующие значения * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_smartscape` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |

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
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

```
{



"additionalMetadata": {



"dashboardId": "82402bab-7370-4359-924d-88ed13c8919a"



},



"creationDate": "2020-11-05T08:15:30.144Z",



"enabled": true,



"expirationDate": "2020-11-12T08:15:30.144Z",



"id": "dt0c01.ST2EY72KQINMH574WMNVI7YN",



"lastUsedDate": "2020-11-12T08:15:30.144Z",



"lastUsedIpAddress": "34.197.2.44",



"modifiedDate": "2020-11-12T08:15:30.144Z",



"name": "myToken",



"owner": "john.smith",



"personalAccessToken": true,



"scopes": [



"metrics.read"



]



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

## Связанные темы

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")