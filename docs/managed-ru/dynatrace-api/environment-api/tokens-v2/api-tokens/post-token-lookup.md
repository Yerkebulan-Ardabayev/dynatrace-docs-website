---
title: Access tokens API - POST token lookup
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token-lookup
---

# Access tokens API - POST token lookup

# Access tokens API - POST token lookup

* Справочник
* Опубликовано 15 марта 2021 г.

Получает метаданные токена API по его секрету.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens/lookup` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens/lookup` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с **любым** scope.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ApiTokenSecret](#openapi-definition-ApiTokenSecret) | Тело JSON запроса. Содержит требуемый токен. | body | Обязательный |

### Объекты тела запроса

#### Объект `ApiTokenSecret`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| token | string | Токен API. | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"token": "dt0c01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApiToken](#openapi-definition-ApiToken) | Успешно |
| **404** | - | Ошибка. Запрошенный ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiToken`

Метаданные токена API.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalMetadata | object | Содержит дополнительные свойства для отдельных видов токенов. Примеры:  * Свойство `dashboardId` для токенов совместного доступа к дашбордам. * Свойство `reportId` для токенов совместного доступа к отчётам |
| creationDate | string | Дата создания токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| enabled | boolean | Токен включён (`true`) или отключён (`false`). |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  Если не задана, срок действия токена не ограничен. |
| id | string | ID токена, состоящий из префикса и публичной части токена. |
| lastUsedDate | string | Дата последнего использования токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| lastUsedIpAddress | string | IP-адрес последнего использования токена. |
| modifiedDate | string | Дата последнего изменения токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). Обновление scopes или имени считается изменением, включение или отключение токена, нет. |
| name | string | Имя токена. |
| owner | string | Владелец токена. |
| personalAccessToken | boolean | Токен является [personal access token﻿](https://dt-url.net/wm03sop?dt=m) (`true`) или токеном API (`false`). |
| scopes | string[] | Список scope, назначенных токену. Элемент может принимать следующие значения * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_smartscape` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |

### Модели JSON тела ответа

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

## Похожие темы

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")