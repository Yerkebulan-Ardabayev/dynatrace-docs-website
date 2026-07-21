---
title: Access tokens API - POST a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token
---

# Access tokens API - POST a token

# Access tokens API - POST a token

* Справочник
* Опубликовано 15 марта 2021 г.

Создаёт новый API токен.

Владельцем токена становится пользователь, которому принадлежит токен, использованный для аутентификации запроса.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `apiTokens.write`.

О том, как получить и использовать его, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ApiTokenCreate](#openapi-definition-ApiTokenCreate) | JSON тело запроса. Содержит параметры нового API токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `ApiTokenCreate`

Параметры нового API токена.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| expirationDate | string | Дата истечения срока действия токена. Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный временной диапазон, отсчитываемый назад от текущего момента. Формат `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` означает год назад, выровненный по неделе. Также можно указать относительный диапазон без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, срок действия токена не истекает никогда. Нужно убедиться, что дата истечения срока действия не указана в прошлом. | Необязательный |
| name | string | Название токена. | Обязательный |
| personalAccessToken | boolean | Токен является персональным токеном доступа (`true`) или API токеном (`false`). Персональные токены доступа привязаны к правам своего владельца. | Необязательный |
| scopes | string[] | Список областей действия, назначаемых токену.  * `InstallerDownload`: интеграция PaaS, загрузка установщика. * `DataExport`: доступ к ленте проблем и событий, метрикам и топологии. * `PluginUpload`: загрузка расширения. * `SupportAlert`: интеграция PaaS, оповещение поддержки. * `AdvancedSyntheticIntegration`: интеграция модуля Dynatrace, Synthetic Classic. * `ExternalSyntheticIntegration`: создание и чтение синтетических мониторов, локаций и узлов. * `RumBrowserExtension`: расширение браузера RUM. * `LogExport`: чтение логов. * `ReadConfig`: чтение конфигурации. * `WriteConfig`: запись конфигурации. * `DTAQLAccess`: пользовательские сессии. * `UserSessionAnonymization`: анонимизация данных пользовательских сессий в целях защиты конфиденциальности. * `DataPrivacy`: изменение настроек конфиденциальности данных. * `CaptureRequestData`: захват данных запросов. * `Davis`: интеграция модуля Dynatrace, Davis. * `DssFileManagement`: управление файлами символикации для мобильных устройств. * `RumJavaScriptTagManagement`: управление JavaScript-тегом мониторинга реальных пользователей. * `TenantTokenManagement`: управление токенами. * `ActiveGateCertManagement`: управление сертификатами ActiveGate. * `RestRequestForwarding`: получение данных из удалённого окружения. * `ReadSyntheticData`: чтение синтетических мониторов, локаций и узлов. * `DataImport`: приём данных, например метрик и событий. * `syntheticExecutions.write`: запись выполнений синтетических мониторов. * `syntheticExecutions.read`: чтение результатов выполнения синтетических мониторов. * `auditLogs.read`: чтение журналов аудита. * `metrics.read`: чтение метрик. * `metrics.write`: запись метрик. * `entities.read`: чтение сущностей. * `entities.write`: запись сущностей. * `problems.read`: чтение проблем. * `problems.write`: запись проблем. * `events.read`: чтение событий. * `events.ingest`: приём событий. * `openpipeline.events`: OpenPipeline, приём событий (встроенный). * `openpipeline.events.custom`: OpenPipeline, приём событий (пользовательский). * `openpipeline.events_security`: OpenPipeline, приём событий безопасности (встроенный). * `openpipeline.events_security.custom`: OpenPipeline, приём событий безопасности (пользовательский). * `openpipeline.events_sdlc`: OpenPipeline, приём событий жизненного цикла разработки ПО (встроенный). * `openpipeline.events_sdlc.custom`: OpenPipeline, приём событий жизненного цикла разработки ПО (пользовательский). * `openpipeline.events_smartscape`: OpenPipeline, приём событий Smartscape (встроенный). * `bizevents.ingest`: приём бизнес-событий. * `networkZones.read`: чтение сетевых зон. * `networkZones.write`: запись сетевых зон. * `activeGates.read`: чтение ActiveGateов. * `activeGates.write`: запись ActiveGateов. * `activeGateTokenManagement.read`: чтение токенов ActiveGate. * `activeGateTokenManagement.create`: создание токенов ActiveGate. * `activeGateTokenManagement.write`: запись токенов ActiveGate. * `agentTokenManagement.read`: чтение токенов Agent. * `credentialVault.read`: чтение записей хранилища учётных данных. * `credentialVault.write`: запись записей хранилища учётных данных. * `extensions.read`: чтение расширений. * `extensions.write`: запись расширений. * `extensionConfigurations.read`: чтение конфигураций мониторинга расширений. * `extensionConfigurations.write`: запись конфигураций мониторинга расширений. * `extensionEnvironment.read`: чтение конфигураций окружения расширений. * `extensionEnvironment.write`: запись конфигураций окружения расширений. * `metrics.ingest`: приём метрик. * `attacks.read`: чтение атак. * `attacks.write`: запись настроек Application Protection. * `securityProblems.read`: чтение проблем безопасности. * `securityProblems.write`: запись проблем безопасности. * `syntheticLocations.read`: чтение синтетических локаций. * `syntheticLocations.write`: запись синтетических локаций. * `settings.read`: чтение настроек. * `settings.write`: запись настроек. * `tenantTokenRotation.write`: ротация токена тенанта. * `slo.read`: чтение SLO. * `slo.write`: запись SLO. * `releases.read`: чтение релизов. * `apiTokens.read`: чтение API токенов. * `apiTokens.write`: запись API токенов. * `openTelemetryTrace.ingest`: приём трасс OpenTelemetry. * `logs.read`: чтение логов. * `logs.ingest`: приём логов. * `geographicRegions.read`: чтение географических регионов. * `oneAgents.read`: чтение OneAgentов. * `oneAgents.write`: запись OneAgentов. * `traces.lookup`: поиск отдельной трассы. * `unifiedAnalysis.read`: чтение страницы Unified Analysis. * `hub.read`: чтение данных, связанных с Hub. * `hub.write`: управление метаданными элементов Hub. * `hub.install`: установка и обновление элементов Hub. * `javaScriptMappingFiles.read`: чтение файлов JavaScript-маппинга. * `javaScriptMappingFiles.write`: запись файлов JavaScript-маппинга. * `extensionConfigurationActions.write`: действия для конфигураций мониторинга расширений. * `rumCookieNames.read`: чтение имён cookie RUM. * `adaptiveTrafficManagement.read`: чтение конфигурации сэмплирования для Adaptive Traffic Management. * `rumManualInsertionTags.read`: чтение тегов ручной вставки RUM. * `extensionDiscoveryJmx.read`: чтение обнаруженных метрик JMX через расширения. * `extensionDiscoveryPmi.read`: чтение обнаруженных метрик PMI через расширения. Элемент может принимать следующие значения * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_smartscape` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` | Обязательный |

### Пример тела запроса JSON модели

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiTokenCreated`

Новый созданный токен.

| Элемент | Тип | Описание |
| --- | --- | --- |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| id | string | ID токена, состоящий из префикса и публичной части токена. |
| token | string | Секрет токена. |

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

### Пример тела ответа JSON моделей

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

## Похожие темы

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Узнайте о концепции токена доступа и его областей действия.")