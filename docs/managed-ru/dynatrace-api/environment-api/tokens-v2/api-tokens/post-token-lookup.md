---
title: Access tokens API - POST поиск токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token-lookup
scraped: 2026-05-12T12:01:13.018046
---

# Access tokens API - POST поиск токена

# Access tokens API - POST поиск токена

* Reference
* Published Mar 15, 2021

Возвращает метаданные API-токена по его секрету.

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens/lookup` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens/lookup` |

## Аутентификация

Для выполнения запроса необходим access token с **любым** scope.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| body | [ApiTokenSecret](#openapi-definition-ApiTokenSecret) | JSON-тело запроса. Содержит искомый токен. | body | Обязательный |

### Объекты тела запроса

#### Объект `ApiTokenSecret`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| token | string | API-токен. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для реального запроса.

```
{



"token": "dt0c01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApiToken](#openapi-definition-ApiToken) | Успех |
| **404** | - | Неудача. Запрошенный ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiToken`

Метаданные API-токена.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalMetadata | object | Содержит дополнительные свойства для определённых типов токенов. Примеры:  * Свойство `dashboardId` для токенов общего доступа к дашборду. * Свойство `reportId` для токенов общего доступа к отчёту |
| creationDate | string | Дата создания токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| enabled | boolean | Токен включён (`true`) или отключён (`false`). |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  Если не задано, токен не истекает. |
| id | string | Идентификатор токена, состоящий из префикса и публичной части токена. |
| lastUsedDate | string | Дата последнего использования токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| lastUsedIpAddress | string | IP-адрес последнего использования токена. |
| modifiedDate | string | Дата последнего изменения токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). Обновление scope или имени считается изменением, включение или отключение токена нет. |
| name | string | Имя токена. |
| owner | string | Владелец токена. |
| personalAccessToken | boolean | Токен является [персональным access-токеном](https://dt-url.net/wm03sop) (`true`) или API-токеном (`false`). |
| scopes | string[] | Список scope, назначенных токену. Элемент может принимать значения * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |

### JSON-модели тела ответа

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

## Связанные темы

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Концепция access-токена и его scope.")