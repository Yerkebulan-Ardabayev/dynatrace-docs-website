---
title: Access tokens API - POST токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token
scraped: 2026-05-12T11:13:59.599423
---

# Access tokens API - POST токена

# Access tokens API - POST токена

* Reference
* Published Mar 15, 2021

Создаёт новый API-токен.

Владельцем токена становится пользователь, чьим токеном выполнена аутентификация запроса.

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens` |

## Аутентификация

Для выполнения запроса необходим access token со scope `apiTokens.write`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| body | [ApiTokenCreate](#openapi-definition-ApiTokenCreate) | JSON-тело запроса. Содержит параметры нового API-токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `ApiTokenCreate`

Параметры нового API-токена.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| expirationDate | string | Дата истечения срока действия токена.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный интервал от текущего момента назад. Формат: `now-NU/A`, где `N` это количество, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад с выравниванием по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, токен не истекает. Дата истечения не должна находиться в прошлом. | Необязательный |
| name | string | Имя токена. | Обязательный |
| personalAccessToken | boolean | Токен является персональным access-токеном (`true`) или API-токеном (`false`).  Персональные access-токены привязаны к правам своего владельца. | Необязательный |
| scopes | string[] | Список scope, назначаемых токену.  * `InstallerDownload`: PaaS-интеграция, скачивание инсталлятора. * `DataExport`: Доступ к фиду проблем и событий, метрикам и топологии. * `PluginUpload`: Загрузка расширения. * `SupportAlert`: PaaS-интеграция, support-оповещение. * `AdvancedSyntheticIntegration`: Интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: Создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: RUM Browser Extension. * `LogExport`: Чтение логов. * `ReadConfig`: Чтение конфигурации. * `WriteConfig`: Запись конфигурации. * `DTAQLAccess`: Пользовательские сессии. * `UserSessionAnonymization`: Анонимизация данных пользовательских сессий в целях защиты приватности. * `DataPrivacy`: Изменение настроек приватности данных. * `CaptureRequestData`: Сбор данных запросов. * `Davis`: Интеграция модуля Dynatrace, Davis. * `DssFileManagement`: Управление файлами мобильной символикации. * `RumJavaScriptTagManagement`: Управление JavaScript-тегом RUM. * `TenantTokenManagement`: Управление токенами. * `ActiveGateCertManagement`: Управление сертификатами ActiveGate. * `RestRequestForwarding`: Получение данных из удалённого окружения. * `ReadSyntheticData`: Чтение синтетических мониторов, локаций и узлов. * `DataImport`: Приём данных (например, метрик и событий). * `syntheticExecutions.write`: Запись запусков синтетических мониторов. * `syntheticExecutions.read`: Чтение результатов запусков синтетических мониторов. * `auditLogs.read`: Чтение audit-логов. * `metrics.read`: Чтение метрик. * `metrics.write`: Запись метрик. * `entities.read`: Чтение сущностей. * `entities.write`: Запись сущностей. * `problems.read`: Чтение проблем. * `problems.write`: Запись проблем. * `events.read`: Чтение событий. * `events.ingest`: Приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенные). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательские). * `openpipeline.events_security`: OpenPipeline, приём security-событий (встроенные). * `openpipeline.events_security.custom`: OpenPipeline, приём security-событий (пользовательские). * `openpipeline.events_sdlc`: OpenPipeline, приём событий SDLC (встроенные). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий SDLC (пользовательские). * `bizevents.ingest`: Приём bizevents. * `networkZones.read`: Чтение network zones. * `networkZones.write`: Запись network zones. * `activeGates.read`: Чтение ActiveGate. * `activeGates.write`: Запись ActiveGate. * `activeGateTokenManagement.read`: Чтение токенов ActiveGate. * `activeGateTokenManagement.create`: Создание токенов ActiveGate. * `activeGateTokenManagement.write`: Запись токенов ActiveGate. * `agentTokenManagement.read`: Чтение Agent-токенов. * `credentialVault.read`: Чтение записей credential vault. * `credentialVault.write`: Запись записей credential vault. * `extensions.read`: Чтение расширений. * `extensions.write`: Запись расширений. * `extensionConfigurations.read`: Чтение monitoring-конфигураций расширений. * `extensionConfigurations.write`: Запись monitoring-конфигураций расширений. * `extensionEnvironment.read`: Чтение environment-конфигураций расширений. * `extensionEnvironment.write`: Запись environment-конфигураций расширений. * `metrics.ingest`: Приём метрик. * `attacks.read`: Чтение атак. * `attacks.write`: Запись настроек Application Protection. * `securityProblems.read`: Чтение проблем безопасности. * `securityProblems.write`: Запись проблем безопасности. * `syntheticLocations.read`: Чтение synthetic-локаций. * `syntheticLocations.write`: Запись synthetic-локаций. * `settings.read`: Чтение настроек. * `settings.write`: Запись настроек. * `tenantTokenRotation.write`: Ротация tenant-токена. * `slo.read`: Чтение SLO. * `slo.write`: Запись SLO. * `releases.read`: Чтение релизов. * `apiTokens.read`: Чтение API-токенов. * `apiTokens.write`: Запись API-токенов. * `openTelemetryTrace.ingest`: Приём OpenTelemetry-трейсов. * `logs.read`: Чтение логов. * `logs.ingest`: Приём логов. * `geographicRegions.read`: Чтение географических регионов. * `oneAgents.read`: Чтение OneAgent. * `oneAgents.write`: Запись OneAgent. * `traces.lookup`: Поиск одного трейса. * `unifiedAnalysis.read`: Чтение страницы Unified Analysis. * `hub.read`: Чтение данных Hub. * `hub.write`: Управление метаданными элементов Hub. * `hub.install`: Установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: Чтение JavaScript mapping-файлов. * `javaScriptMappingFiles.write`: Запись JavaScript mapping-файлов. * `extensionConfigurationActions.write`: Действия для monitoring-конфигураций расширений. * `rumCookieNames.read`: Чтение имён RUM-cookies. * `adaptiveTrafficManagement.read`: Чтение конфигурации сэмплирования для Adaptive Traffic Management. * `rumManualInsertionTags.read`: Чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: Чтение JMX-метрик, обнаруженных расширениями. Элемент может принимать значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для реального запроса.

```
{



"expirationDate": "now+14d",



"name": "tokenName",



"personalAccessToken": false,



"scopes": [



"metrics.read"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [ApiTokenCreated](#openapi-definition-ApiTokenCreated) | Успех. Токен создан. Тело ответа содержит секрет токена. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiTokenCreated`

Только что созданный токен.

| Элемент | Тип | Описание |
| --- | --- | --- |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| id | string | Идентификатор токена, состоящий из префикса и публичной части токена. |
| token | string | Секрет токена. |

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



"expirationDate": "2020-11-12T08:15:30.144Z",



"id": "dt0c01.ST2EY72KQINMH574WMNVI7YN",



"token": "dt0c01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM"



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

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Концепция access-токена и его scope.")