---
title: Tokens API v1 - PUT существующий токен
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/put-token
scraped: 2026-05-12T12:11:15.802820
---

# Tokens API v1 - PUT существующий токен

# Tokens API v1 - PUT существующий токен

* Справочник
* Обновлено 17 мая 2022 г.

Этот API устарел. Используйте вместо него [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.").

Обновляет указанный токен аутентификации Dynatrace API. Вы можете:

* Изменить имя токена.
* Добавить или удалить scope токена.
* Отозвать токен. Отозванный токен всё ещё существует в среде, но не может быть использован.

Запрос потребляет payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `TenantTokenManagement`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| id | string | ID обновляемого токена.  Вы не можете обновить токен, используемый для аутентификации запроса. | path | Обязательный |
| body | [UpdateToken](#openapi-definition-UpdateToken) | JSON-тело запроса. Содержит обновлённые параметры токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `UpdateToken`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| name | string | Имя токена. | Опциональный |
| revoked | boolean | Токен отозван (`true`) или активен (`false`). | Опциональный |
| scopes | string[] | Список разрешений, назначенных токену.  Помимо новых разрешений, необходимо также отправить существующие разрешения, которые вы хотите сохранить. Любое существующее разрешение, отсутствующее в payload, отзывается.  * `InstallerDownload`: PaaS-интеграция, скачивание инсталлятора. * `DataExport`: Доступ к ленте проблем и событий, метрикам и топологии. * `PluginUpload`: Загрузка расширения. * `SupportAlert`: PaaS-интеграция, оповещение поддержки. * `AdvancedSyntheticIntegration`: Интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: Создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: Браузерное расширение RUM. * `LogExport`: Чтение логов. * `ReadConfig`: Чтение конфигурации. * `WriteConfig`: Запись конфигурации. * `DTAQLAccess`: Пользовательские сессии. * `UserSessionAnonymization`: Анонимизация данных пользовательских сессий в целях конфиденциальности данных. * `DataPrivacy`: Изменение настроек конфиденциальности данных. * `CaptureRequestData`: Захват данных запросов. * `Davis`: Интеграция модуля Dynatrace, Davis. * `DssFileManagement`: Управление файлами мобильной символикации. * `RumJavaScriptTagManagement`: Управление JavaScript-тегами мониторинга реальных пользователей. * `TenantTokenManagement`: Управление токенами. * `ActiveGateCertManagement`: Управление сертификатами ActiveGate. * `RestRequestForwarding`: Получение данных из удалённой среды. * `ReadSyntheticData`: Чтение синтетических мониторов, локаций и узлов. * `DataImport`: Приём данных, например метрик и событий. * `syntheticExecutions.write`: Запись выполнений синтетических мониторов. * `syntheticExecutions.read`: Чтение результатов выполнения синтетических мониторов. * `auditLogs.read`: Чтение журналов аудита. * `metrics.read`: Чтение метрик. * `metrics.write`: Запись метрик. * `entities.read`: Чтение сущностей. * `entities.write`: Запись сущностей. * `problems.read`: Чтение проблем. * `problems.write`: Запись проблем. * `events.read`: Чтение событий. * `events.ingest`: Приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенные). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательские). * `openpipeline.events_security`: OpenPipeline, приём событий безопасности (встроенные). * `openpipeline.events_security.custom`: OpenPipeline, приём событий безопасности (пользовательские). * `openpipeline.events_sdlc`: OpenPipeline, приём событий жизненного цикла разработки ПО (встроенные). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий жизненного цикла разработки ПО (пользовательские). * `bizevents.ingest`: Приём bizevents. * `networkZones.read`: Чтение сетевых зон. * `networkZones.write`: Запись сетевых зон. * `activeGates.read`: Чтение ActiveGate. * `activeGates.write`: Запись ActiveGate. * `activeGateTokenManagement.read`: Чтение токенов ActiveGate. * `activeGateTokenManagement.create`: Создание токенов ActiveGate. * `activeGateTokenManagement.write`: Запись токенов ActiveGate. * `agentTokenManagement.read`: Чтение токенов агента. * `credentialVault.read`: Чтение записей хранилища учётных данных. * `credentialVault.write`: Запись записей хранилища учётных данных. * `extensions.read`: Чтение расширений. * `extensions.write`: Запись расширений. * `extensionConfigurations.read`: Чтение конфигураций мониторинга расширений. * `extensionConfigurations.write`: Запись конфигураций мониторинга расширений. * `extensionEnvironment.read`: Чтение конфигураций среды расширений. * `extensionEnvironment.write`: Запись конфигураций среды расширений. * `metrics.ingest`: Приём метрик. * `attacks.read`: Чтение атак. * `attacks.write`: Запись настроек Application Protection. * `securityProblems.read`: Чтение проблем безопасности. * `securityProblems.write`: Запись проблем безопасности. * `syntheticLocations.read`: Чтение синтетических локаций. * `syntheticLocations.write`: Запись синтетических локаций. * `settings.read`: Чтение настроек. * `settings.write`: Запись настроек. * `tenantTokenRotation.write`: Ротация tenant-токена. * `slo.read`: Чтение SLO. * `slo.write`: Запись SLO. * `releases.read`: Чтение релизов. * `apiTokens.read`: Чтение API-токенов. * `apiTokens.write`: Запись API-токенов. * `openTelemetryTrace.ingest`: Приём трейсов OpenTelemetry. * `logs.read`: Чтение логов. * `logs.ingest`: Приём логов. * `geographicRegions.read`: Чтение географических регионов. * `oneAgents.read`: Чтение OneAgent. * `oneAgents.write`: Запись OneAgent. * `traces.lookup`: Поиск одного трейса. * `unifiedAnalysis.read`: Чтение страницы Unified Analysis. * `hub.read`: Чтение данных, связанных с Hub. * `hub.write`: Управление метаданными элементов Hub. * `hub.install`: Установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: Чтение файлов сопоставления JavaScript. * `javaScriptMappingFiles.write`: Запись файлов сопоставления JavaScript. * `extensionConfigurationActions.write`: Действия для конфигураций мониторинга расширений. * `rumCookieNames.read`: Чтение имён cookie RUM. * `adaptiveTrafficManagement.read`: Чтение конфигурации сэмплирования для Adaptive Traffic Management. * `rumManualInsertionTags.read`: Чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: Чтение обнаруженных JMX-метрик через расширения. Элемент может принимать значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Токен обновлён. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Вы не можете обновить токен, используемый для аутентификации запроса. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный токен не найден. |
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

В этом примере запрос запрашивает метаданные токена **admin**, который имеет ID **d5836312-5790-4e80-afcf-09971954c3ea**. Он назначает два новых scope: **Real user monitoring JavaScript tag management** и **ActiveGate certificate management**. Имя и срок действия токена остаются без изменений. Код ответа **204** указывает, что обновление прошло успешно.

Токен, как он отображается в интерфейсе Dynatrace, имеет следующие настройки до редактирования:

![Токен аутентификации Dynatrace API](https://dt-cdn.net/images/token-permissions-1283-6453dccd8a.png)

Токен аутентификации Dynatrace API

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

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

#### URL запроса

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

Обновлённый токен, как он отображается в интерфейсе Dynatrace, имеет следующие параметры:

![Токен аутентификации Dynatrace API, обновлённый](https://dt-cdn.net/images/token-permissions-upd-1283-3c4befedf4.png)

Токен аутентификации Dynatrace API, обновлённый