---
title: Tokens API v1 - POST поиск токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata
scraped: 2026-05-12T12:11:17.840201
---

# Tokens API v1 - POST поиск токена

# Tokens API v1 - POST поиск токена

* Справочник
* Обновлено 17 мая 2022 г.

Этот API устарел. Используйте вместо него [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.").

Перечисляет метаданные токена аутентификации Dynatrace API по самому токену.

Кроме того, метаданные можно получить, отправив ID токена через вызов [GET token metadata](/managed/dynatrace-api/environment-api/tokens-v1/get-token-metadata "Узнайте, как использовать Dynatrace API для получения метаданных токена аутентификации Dynatrace API.").

Запрос потребляет и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/lookup` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/lookup` |

## Аутентификация

Для выполнения запроса необходим access token с **любым** scope.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| body | [Token](#openapi-definition-Token) | JSON-тело запроса. Содержит требуемый токен. | body | Обязательный |

### Объекты тела запроса

#### Объект `Token`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| token | string | Токен аутентификации Dynatrace API. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"token": "abcdefjhij1234567890"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `TokenMetadata`

Метаданные токена.

| Элемент | Тип | Описание |
| --- | --- | --- |
| created | integer | Время создания в виде unix-метки времени в миллисекундах. |
| expires | integer | Время истечения срока действия в виде unix-метки времени в миллисекундах. |
| id | string | ID токена. |
| lastUse | integer | Unix-метка времени в миллисекундах, когда токен использовался в последний раз. |
| name | string | Имя токена. |
| personalAccessToken | boolean | Токен является [персональным access-токеном](https://dt-url.net/wm03sop) (`true`) или API-токеном (`false`). |
| revoked | boolean | Статус отзыва токена. Отозванные токены отключены. |
| scopes | string[] | Список scope, назначенных токену. Элемент может принимать значения * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |
| userId | string | Владелец токена. |

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

В этом примере запрос запрашивает метаданные токена **abcdefjhij1234567890**.

API-токен передаётся в заголовке **Authorization**.

Токен, как он отображается в интерфейсе Dynatrace, имеет следующие настройки:

![Токен аутентификации Dynatrace API](https://dt-cdn.net/images/token-permissions-1283-6453dccd8a.png)

Токен аутентификации Dynatrace API

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/lookup \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"token": "abcdefjhij1234567890"



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/tokens/lookup
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