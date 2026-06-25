---
title: Access tokens API - GET все токены
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/get-all
scraped: 2026-05-12T12:01:08.958713
---

# Access tokens API - GET все токены

# Access tokens API - GET все токены

* Reference
* Published Mar 15, 2021

Возвращает список всех API-токенов, доступных в окружении.

Объём ответа можно ограничить через пагинацию:

1. Укажите количество результатов на страницу в query-параметре **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в query-параметре **nextPageKey** для получения последующих страниц.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens` |

## Аутентификация

Для выполнения запроса необходим access token со scope `apiTokens.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Если query-параметр **nextPageKey** не указан, всегда возвращается первая страница.  При указании **nextPageKey** для получения последующих страниц все остальные query-параметры должны быть опущены. | query | Необязательный |
| pageSize | integer | Количество API-токенов в одном payload ответа.  Максимально допустимый размер страницы 10000, минимально допустимый 100.  Если не задано, используется 200. | query | Необязательный |
| apiTokenSelector | string | Фильтрует возвращаемый набор токенов. В ответ попадают только токены, соответствующие указанным критериям.  Можно задать один или несколько следующих критериев:  * Владелец: `owner("value")`. Пользователь, владеющий токеном. Регистрозависимо. * Персональный access-токен: `personalAccessToken(false)`. Задайте `true` для включения только персональных access-токенов или `false` для включения только API-токенов. * Scope токена: `scope("scope1","scope2")`. Если задано несколько значений, применяется логика **OR**.  Чтобы задать несколько критериев, разделите их запятыми (`,`). В ответ попадают только результаты, удовлетворяющие **всем** критериям. | query | Необязательный |
| fields | string | Указывает поля, которые надо включить в ответ.  По умолчанию включены следующие поля:  * `id` * `name` * `enabled` * `owner` * `creationDate`  Чтобы убрать поля из ответа, укажите их с оператором минус (`-`) через запятую (например, `-creationDate,-owner`).  Можно включить дополнительные поля:  * `personalAccessToken` * `expirationDate` * `lastUsedDate` * `lastUsedIpAddress` * `modifiedDate` * `scopes` * `additionalMetadata`  Чтобы добавить поля в ответ, укажите их с оператором плюс (`+`) через запятую (например, `+expirationDate,+scopes`). Можно комбинировать добавление и удаление полей (например, `+scopes,-creationDate`).  Альтернативно можно задать желаемый набор полей ответа. Укажите нужные поля через запятую без операторов (например, `creationDate,expirationDate,owner`). ID всегда включается в ответ.  Строка **fields** должна быть URL-encoded. | query | Необязательный |
| from | string | Фильтрует токены по времени последнего использования. Начало запрашиваемого интервала времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный интервал от текущего момента назад. Формат: `now-NU/A`, где `N` это количество, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад с выравниванием по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы | query | Необязательный |
| to | string | Фильтрует токены по времени последнего использования. Конец запрашиваемого интервала времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный интервал от текущего момента назад. Формат: `now-NU/A`, где `N` это количество, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад с выравниванием по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| sort | string | Порядок сортировки списка токенов.  Доступна сортировка по следующим свойствам с префиксом знака для направления сортировки:  * `name`: имя токена (`+` а...я или `-` я...а) * `lastUsedDate` последнее использование (`+` сначала никогда не использованные, `-` сначала недавно использованные) * `creationDate` (`+` сначала самые старые, `-` сначала самые новые) * `expirationDate` (`+` сначала истекающие скоро, `-` сначала бессрочные) * `modifiedDate` последнее изменение (`+` сначала никогда не изменявшиеся, `-` сначала недавно изменённые)  Если префикс не указан, используется `+`.  Если не задано, токены сортируются по дате создания, сначала самые новые. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApiTokenList](#openapi-definition-ApiTokenList) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApiTokenList`

Список API-токенов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| apiTokens | [ApiToken[]](#openapi-definition-ApiToken) | Список API-токенов. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

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

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Концепция access-токена и его scope.")