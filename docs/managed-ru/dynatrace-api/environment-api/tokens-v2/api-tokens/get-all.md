---
title: Access tokens API - GET all tokens
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/get-all
---

# Access tokens API - GET all tokens

# Access tokens API - GET all tokens

* Справка
* Опубликовано 15 марта 2021 г.

Выводит список всех токенов API, доступных в среде.

Ограничить вывод можно с помощью пагинации:

1. Указать количество результатов на странице в параметре запроса **pageSize**.
2. Затем использовать курсор из поля **nextPageKey** предыдущего ответа в параметре запроса **nextPageKey**, чтобы получить последующие страницы.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `apiTokens.read`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Если параметр запроса **nextPageKey** не указан, всегда возвращается первая страница.  Когда **nextPageKey** задан для получения последующих страниц, нужно опустить все остальные параметры запроса. | query | Опциональный |
| pageSize | integer | Количество токенов API в одном ответе.  Максимально допустимый размер страницы 10000, минимально допустимый 100.  Если не задан, используется значение 200. | query | Опциональный |
| apiTokenSelector | string | Фильтрует результирующий набор токенов. В ответ попадают только токены, соответствующие указанным критериям.  Можно задать один или несколько следующих критериев:  * Владелец: `owner("value")`. Пользователь, которому принадлежит токен. Учитывает регистр. * Персональный токен доступа: `personalAccessToken(false)`. Установить `true`, чтобы включить только персональные токены доступа, или `false`, чтобы включить только токены API. * Область действия токена: `scope("scope1","scope2")`. Если указано несколько значений, применяется логика **ИЛИ**.  Чтобы задать несколько критериев, нужно разделить их запятыми (`,`). В ответ попадают только результаты, соответствующие **всем** критериям. | query | Опциональный |
| fields | string | Определяет поля, которые нужно включить в ответ.  По умолчанию включаются следующие поля:  * `id` * `name` * `enabled` * `owner` * `creationDate`  Чтобы удалить поля из ответа, нужно указать их через оператор минус (`-`) в виде списка через запятую (например, `-creationDate,-owner`).  Можно включить дополнительные поля:  * `personalAccessToken` * `expirationDate` * `lastUsedDate` * `lastUsedIpAddress` * `modifiedDate` * `scopes` * `additionalMetadata`  Чтобы добавить поля в ответ, нужно указать их через оператор плюс (`+`) в виде списка через запятую (например, `+expirationDate,+scopes`). Добавление и удаление полей можно комбинировать (например, `+scopes,-creationDate`).  Также можно определить желаемый набор полей в ответе напрямую. Для этого нужно указать требуемые поля в виде списка через запятую, без операторов (например, `creationDate,expirationDate,owner`). ID всегда включается в ответ.  Строка **fields** должна быть закодирована в URL. | query | Опциональный |
| from | string | Фильтрует токены по времени последнего использования. Начало запрашиваемого периода времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Понятный человеку формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный период времени, отсчитываемый назад от текущего момента. Формат `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это один год назад, выровненный по неделе.   Также можно указать относительный период времени без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного периода: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы | query | Опциональный |
| to | string | Фильтрует токены по времени последнего использования. Конец запрашиваемого периода времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Понятный человеку формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный период времени, отсчитываемый назад от текущего момента. Формат `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это один год назад, выровненный по неделе.   Также можно указать относительный период времени без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного периода: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задан, используется текущая метка времени. | query | Опциональный |
| sort | string | Порядок сортировки списка токенов.  Сортировать можно по следующим свойствам со знаком-префиксом для порядка сортировки:  * `name`: имя токена (`+` a...z или `-` z...a) * `lastUsedDate` последнее использование (`+` сначала никогда не использовавшиеся токены `-` сначала недавно использовавшиеся токены) * `creationDate` (`+` сначала самые старые токены `-` сначала самые новые токены) * `expirationDate` (`+` сначала токены, срок действия которых истекает раньше всего `-` сначала неограниченные токены) * `modifiedDate` последнее изменение (`+` сначала никогда не изменявшиеся токены `-` сначала недавно изменённые токены)  Если префикс не задан, используется +.  Если не задан, токены сортируются по дате создания, сначала самые новые. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApiTokenList](#openapi-definition-ApiTokenList) | Успешно |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введены недопустимые данные. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiTokenList`

Список токенов API.

| Элемент | Тип | Описание |
| --- | --- | --- |
| apiTokens | [ApiToken](#openapi-definition-ApiToken)[] | Список токенов API. |
| nextPageKey | string | Курсор для следующей страницы результатов. Имеет значение `null` на последней странице. Используется в параметре запроса **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `ApiToken`

Метаданные токена API.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalMetadata | object | Содержит дополнительные свойства для определённых видов токена. Примеры:  * Свойство `dashboardId` для токенов совместного доступа к дашборду. * Свойство `reportId` для токенов совместного доступа к отчёту |
| creationDate | string | Дата создания токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| enabled | boolean | Токен включён (`true`) или отключён (`false`). |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  Если не задано, срок действия токена не истекает. |
| id | string | Идентификатор токена, состоящий из префикса и публичной части токена. |
| lastUsedDate | string | Дата последнего использования токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| lastUsedIpAddress | string | IP-адрес последнего использования токена. |
| modifiedDate | string | Дата последнего изменения токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). Изменение scopes или имени считается модификацией, включение или отключение токена, нет. |
| name | string | Имя токена. |
| owner | string | Владелец токена. |
| personalAccessToken | boolean | Токен является [персональным токеном доступа﻿](https://dt-url.net/wm03sop?dt=m) (`true`) или токеном API (`false`). |
| scopes | string[] | Список scopes, назначенных токену. Элемент может принимать следующие значения * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_smartscape` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |

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

### JSON модели тела ответа

```
{



"apiTokens": {



"additionalMetadata": {



"dashboardId": "82402bab-7370-4359-924d-88ed13c8919a"



},



"creationDate": "2020-11-05T08:15:30.144Z",



"disabled": "false",



"expirationDate": "2020-11-12T08:15:30.144Z",



"id": "dt0c01.ST2EY72KQINMH574WMNVI7YN",



"lastUsedDate": "2020-11-12T08:15:30.144Z",



"lastUsedIpAddress": "34.197.2.44",



"name": "tokenName",



"owner": "john.smith",



"personalAccessToken": "true",



"scopes": [



"metrics.read"



]



},



"pageSize": "1",



"totalCount": "1"



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