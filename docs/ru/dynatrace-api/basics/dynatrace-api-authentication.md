---
title: Dynatrace API - Токены и аутентификация
source: https://www.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication
scraped: 2026-02-19T21:19:54.535387
---

# Dynatrace API - Токены и аутентификация

# Dynatrace API - Токены и аутентификация

* Ссылка
* Опубликовано 23 августа 2018 г.

Чтобы быть аутентифицированным для использования Dynatrace API, вам нужен действительный [токен доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Изучите концепцию токена доступа и его области.") или действительный [личный токен доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Изучите концепцию личного токена доступа и его области."). Доступ к API является тонко-зернистым, то есть вам также нужны соответствующие области, назначенные токену. См. описание каждого запроса, чтобы узнать, какие области необходимы для его использования.

Для получения подробной информации об OAuth-клиентах см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управляйте аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Формат токена

Dynatrace использует уникальный формат токена, состоящий из трех компонентов, разделенных точками (`.`).

### Пример токена

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Компоненты токена

Название компонента

Описание компонента

prefix

**Префикс** идентифицирует тип токена.

В нашем примере: `dt0s01`

См. [Префиксы токена](#token-format-prefixes) ниже для таблицы стандартных префиксов.

public portion

**Публичная часть** токена - это 24-символьный публичный идентификатор.

В нашем примере: `ST2EY72KQINMH574WMNVI7YN`

token identifier

**Идентификатор токена** - это сочетание **префикса** и **публичной части**. Идентификатор токена можно безопасно отображать в интерфейсе пользователя и использовать для целей ведения журнала.

В нашем примере: `<DYNATRACE_TOKEN_PLACEHOLDER>`

secret portion

**Секретная часть** токена - это 64-символьная строка, которую следует behand как пароль:

* Не отображайте ее
* Не храните в файлах журнала
* Немедленно замените, если она была скомпрометирована

В нашем примере: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Префиксы токена

Префикс

Описание

`dt0s01`

Это токен API. Он используется в качестве метода аутентификации: действительный токен позволяет пользователю вносить изменения в учетную запись Dynatrace через SCIM.

* Он генерируется один раз.
* Не раскрывайте секретную часть токена `dt0s01`.
* Публичная часть используется для идентификации в веб-интерфейсе, но вы обычно не должны раскрывать ее (или любую часть этого токена).
* Этот токен остается в силе до тех пор, пока не будет отменен клиентом, поэтому вы должны немедленно заменить его, если он был скомпрометирован.

`dt0s02`

OAuth2-клиенты, созданные пользователями через Управление учетной записью для использования с приложениями Dynatrace и API Управления учетной записью.

`dt0s03`

OAuth2-клиенты для внутренних и внешних сервисов и интеграций.

`dt0s04`

Связывание чата и идентификации.

`dt0s06`

Это OAuth2-токен обновления, который используется для получения нового токена доступа и обычно часто меняется (обычно каждые 5-15 минут).

`dt0s08`

OAuth2-клиенты для внутренних и внешних сервисов и интеграций.

`dt0s09`

Связывание чата и идентификации.

`dt0s16`

Платформенный токен, обеспечивающий программный доступ к сервисам платформы Dynatrace.

## Генерация токена

Токен доступа

Личный токен доступа

Чтобы сгенерировать токен доступа:

1. Перейдите к ![Токены доступа](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Токены доступа") **Токены доступа**.
2. Выберите **Сгенерировать новый токен**.
3. Введите имя для вашего токена.  
   Dynatrace не обеспечивает уникальность имен токенов. Вы можете создать несколько токенов с одинаковым именем. Убедитесь, что вы предоставляете осмысленное имя для каждого сгенерированного токена. Правильное именование помогает вам эффективно управлять токенами и, возможно, удалять их, когда они больше не нужны.
4. Выберите необходимые области для токена.
5. Выберите **Сгенерировать токен**.
6. Скопируйте сгенерированный токен в буфер обмена. Храните токен в менеджере паролей для будущего использования.

   Вы можете получить доступ к вашему токену только один раз при создании. Вы не сможете получить к нему доступ позже.

Чтобы сгенерировать личный токен доступа:

1. Перейдите к **Личным токенам доступа** (доступно через [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Перейдите к последнему Dynatrace") в предыдущем Dynatrace).
2. Выберите **Сгенерировать новый токен**.
3. Введите имя для вашего токена.  
   Dynatrace не обеспечивает уникальность имен токенов. Вы можете создать несколько токенов с одинаковым именем. Убедитесь, что вы предоставляете осмысленное имя для каждого сгенерированного токена. Правильное именование помогает вам эффективно управлять токенами и, возможно, удалять их, когда они больше не нужны.
4. Выберите необходимые области для токена.
5. Выберите **Сгенерировать токен**.
6. Скопируйте сгенерированный токен в буфер обмена. Храните токен в менеджере паролей для будущего использования.

   Вы можете получить доступ к вашему токену только один раз при создании. Вы не сможете получить к нему доступ позже.

Вы можете назначить несколько областей одному токену или сгенерировать несколько токенов, каждый с разными уровнями доступа, и использовать их соответствующим образом - проверьте политику безопасности вашей организации для лучшей практики.

Чтобы изменить область существующего токена, используйте вызов [PUT токена](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token "Обновите токен доступа через Dynatrace API.") API токенов доступа. Обратите внимание, что вам необходимо передать существующие области, если вы хотите сохранить их. Любая существующая область, отсутствующая в полезной нагрузке, удаляется.

Альтернативно вы можете использовать вызов [POST токена](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Создайте токен доступа через Dynatrace API.") для генерации токена.

## Области токена

Токен доступа

Личный токен доступа

### OpenPipeline

Имя

API значение

Описание

OpenPipeline - Ингестируемые события

`openpipeline.events`

Предоставляет доступ к запросу [POST Встроенные общие события](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ингестируйте общие события из встроенных конечных точек через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингестируемые события, Жизненный цикл разработки программного обеспечения

`openpipeline.events_sdlc`

Предоставляет доступ к запросу [POST Встроенные события SDLC](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ингестируйте события SDLC из встроенных конечных точек через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингестируемые события, Жизненный цикл разработки программного обеспечения (Пользовательский)

`openpipeline.events_sdlc.custom`

Предоставляет доступ к запросу [POST Пользовательские события SDLC](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Настройте пользовательскую конечную точку события SDLC через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингестируемые события безопасности (Встроенные)

`openpipeline.events_security`

Предоставляет доступ к запросу [POST Встроенные события безопасности](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ингестируйте события безопасности из встроенных конечных точек через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингестируемые события безопасности (Пользовательские)

`openpipeline.events_security.custom`

Предоставляет доступ к запросу [POST Пользовательские события безопасности](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Настройте пользовательскую конечную точку события безопасности через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингестируемые события (Пользовательские)

`openpipeline.events.custom`

Предоставляет доступ к запросу [POST Пользовательская конечная точка общего события](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Настройте пользовательскую конечную точку общего события через OpenPipeline Ingest API.") API OpenPipeline Ingest.

### API v2

Имя

API значение

Описание

Чтение ActiveGate

`activeGates.read`

Предоставляет доступ к GET-запросам [ActiveGate API](/docs/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API.").

Запись ActiveGate

`activeGates.write`

Предоставляет доступ к POST- и DELETE-запросам [ActiveGate API](/docs/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API.").

Создание токенов ActiveGate

`activeGateTokenManagement.create`

Предоставляет доступ к POST-запросу токенов ActiveGate API.

Чтение токенов ActiveGate

`activeGateTokenManagement.read`

Предоставляет доступ к GET-запросам токенов ActiveGate API.

Запись токенов ActiveGate

`activeGateTokenManagement.write`

Предоставляет доступ к POST- и DELETE-запросам токенов ActiveGate API.

Чтение токенов API

`apiTokens.read`

Предоставляет доступ к GET-запросам [Access токенов API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте Dynatrace API аутентификационными токенами.").

Запись токенов API

`apiTokens.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Access токенов API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте Dynatrace API аутентификационными токенами.").

Чтение атак

`attacks.read`

Предоставляет доступ к GET-запросам Атак API и [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") для Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config` и `builtin:appsec.attack-protection-allowlist-config schemas`).

Запись настроек Application Protection

`attacks.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") для Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config` и `builtin:appsec.attack-protection-allowlist-config schemas`).

Чтение аудитных журналов

`auditLogs.read`

Предоставляет доступ к [аудитному журналу](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Узнайте, как управлять аудитными журналами с помощью API.").

Чтение записей хранилища учетных данных

`credentialVault.read`

Предоставляет доступ к GET-запросам [Хранилища учетных данных API](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для учетных данных.").

Запись записей хранилища учетных данных

`credentialVault.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Хранилища учетных данных API](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для учетных данных.").

Чтение сущностей

`entities.read`

Предоставляет доступ к GET-запросам [Отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте об Dynatrace Отслеживаемых сущностях API.") и [Пользовательских тегов](/docs/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.") API.

Запись сущностей

`entities.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте об Dynatrace Отслеживаемых сущностях API.") и [Пользовательских тегов](/docs/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.") API.

Ввод событий

`events.ingest`

Предоставляет доступ к POST-запросу [Событий API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Событий API v2.").

Чтение событий

`events.read`

Предоставляет доступ к GET-запросам [Событий API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Событий API v2.").

Чтение конфигурации мониторинга расширений

`extensionConfigurations.read`

Предоставляет доступ к GET-запросам из раздела **Конфигурация мониторинга расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Запись конфигурации мониторинга расширений

`extensionConfigurations.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам из раздела **Конфигурация мониторинга расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Чтение конфигурации окружения расширений

`extensionEnvironment.read`

Предоставляет доступ к GET-запросам из раздела **Конфигурация окружения расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Запись конфигурации окружения расширений

`extensionEnvironment.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам из раздела **Конфигурация окружения расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Чтение расширений

`extensions.read`

Предоставляет доступ к GET-запросам из раздела **Расширения** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Запись расширений

`extensions.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам из раздела **Расширения** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Чтение географических регионов

`geographicRegions.read`

Предоставляет доступ к [Географическим регионам API](/docs/dynatrace-api/environment-api/rum/geographic-regions "Просмотрите запросы, доступные через Dynatrace Географические регионы API.").

Установка и обновление элементов Hub

`hub.install`

Предоставляет разрешение на установку и обновление расширений через [Элементы Hub API](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.").

Чтение данных, связанных с Hub

`hub.read`

Предоставляет доступ к GET-запросам [Элементов Hub API](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.").

Управление метаданными элементов Hub

`hub.write`

Предоставляет разрешение на управление метаданными элементов Hub через [Элементы Hub API](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.").

Чтение файлов сопоставления JavaScript

`javaScriptMappingFiles.read`

Запись файлов сопоставления JavaScript

`javaScriptMappingFiles.write`

Ввод журналов

`logs.ingest`

Предоставляет доступ к запросу [POST ввод журналов](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправьте пользовательские журналы в Dynatrace через Мониторинг журналов API v2.") Мониторинга журналов API v2, а также [OpenTelemetry журнал ввод API](/docs/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API конечных точках, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Чтение журналов

`logs.read`

Предоставляет доступ к GET-запросам [Мониторинга журналов API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно сделать с помощью Мониторинга журналов API v2.").

Ввод метрик

`metrics.ingest`

Предоставляет доступ к запросу [POST ввод данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ввод пользовательских метрик в Dynatrace через Метрики v2 API.") Метрик v2 API, а также [OpenTelemetry метрик ввод API](/docs/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API конечных точках, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Чтение метрик

`metrics.read`

Предоставляет доступ к GET-запросам [Метрик API v2](/docs/dynatrace-api/environment-api/metric-v2 "Получите информацию о метриках через Метрики v2 API.").

Запись метрик

`metrics.write`

Предоставляет доступ к запросу [Удаление пользовательской метрики](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Удалите метрику, введенную через Метрики v2 API.") Метрик API v2.

Чтение сетевых зон

`networkZones.read`

Предоставляет доступ к GET-запросам [Сетевые зоны API](/docs/dynatrace-api/environment-api/network-zones "Управляйте сетевыми зонами через Dynatrace API.").

Запись сетевых зон

`networkZones.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Сетевые зоны API](/docs/dynatrace-api/environment-api/network-zones "Управляйте сетевыми зонами через Dynatrace API.").

Чтение OneAgent

`oneAgents.read`

Предоставляет доступ к GET-запросам [OneAgent API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверьте конфигурацию экземпляров OneAgent на ваших хостах через Dynatrace API.").

Запись OneAgent

`oneAgents.write`

Предоставляет доступ к POST- и DELETE-запросам [OneAgent API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверьте конфигурацию экземпляров OneAgent на ваших хостах через Dynatrace API.").

Ввод трасс OpenTelemetry

`openTelemetryTrace.ingest`

Предоставляет разрешение на [ввод трасс OpenTelemetry](/docs/ingest-from/opentelemetry "Узнайте, как интегрировать и вводить данные OpenTelemetry (трассы, метрики и журналы) в Dynatrace.").

Чтение проблем

`problems.read`

Предоставляет доступ к GET-запросам [Проблем API v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.").

Запись проблем

`problems.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Проблем API v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.").

Чтение выпусков

`releases.read`

Предоставляет доступ к [Выпускам API](/docs/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Выпуски API.").

Чтение проблем безопасности

`securityProblems.read`

Grants access to GET requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Write security problems

`securityProblems.write`

Grants access to POST requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Read settings

`settings.read`

Grants access to GET requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Write settings

`settings.write`

Grants access to POST and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Read SLO

`slo.read`

Grants access to GET requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Read synthetic monitor execution results

`syntheticExecutions.read`

Grants access to GET requests of the `/synthetic/executions` API.

Write synthetic monitor execution results

`syntheticExecutions.write`

Grants access to POST request of `/synthetic/executions` API.

Read synthetic locations

`syntheticLocations.read`

Grants access to GET requests of the [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.").

Write synthetic locations

`syntheticLocations.write`

Grants access to POST, PUT, and DELETE requests of the [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.").

Tenant token rotation

`tenantTokenRotation.write`

Grants access to the [Tenant tokens API](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens.").

Look up a single trace

`traces.lookup`

Checks for the presence of a trace in cross-environment tracing.

Read Unified Analysis page

`unifiedAnalysis.read`

Grants access to the Unified analysis schema in the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").



### API v1

Name

API value

Description

Access problems and event feed, metrics, and topology

`DataExport`

Grants access to various calls of [Environment API](/docs/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API.").

Create and read synthetic monitors, locations, and nodes

`ExternalSyntheticIntegration`

Grants access to the [Synthetic API](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.").

Read synthetic monitors, locations, and nodes

`ReadSyntheticData`

Grants access to GET requests of [Synthetic API](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.").

Read configuration

`ReadConfig`

Grants access to GET calls of [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Write configuration

`WriteConfig`

Grants access to POST, PUT, and DELETE calls of [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Change data privacy settings

`DataPrivacy`

Grants access to [Data privacy API](/docs/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.") and data privacy calls of [Web application configuration API](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers.").

User sessions

`DTAQLAccess`

Grants access to [User sessions API](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.").

Anonymize user sessions for data privacy reasons

`UserSessionAnonymization`

Grants access to [Anonymization API](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.").

Mobile symbol file management

`DssFileManagement`

Grants access to [Mobile symbolication API](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.").

Real User Monitoring JavaScript tag management

`RumJavaScriptTagManagement`

Grants access to [Real User Monitoring JavaScript API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").

ActiveGate certificate management

`ActiveGateCertManagement`

Grants permission to [configure certificate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.") on private ActiveGates.

Fetch data from a remote environment

`RestRequestForwarding`

Grants permission to fetch data from [remote Dynatrace environments](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.") for multi-environment dashboarding.

Capture request data

`CaptureRequestData`

Grants access to [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.").

Read log content

`LogExport`

Grants access to [Log Monitoring API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.").

### PaaS

Name

API value

Description

Download OneAgent and ActiveGate installers

`InstallerDownload`

Allows download of installers via [Deployment API](/docs/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API.").

Create support alerts

`SupportAlert`

Allows creation of [support alerts](/docs/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Learn how Dynatrace can help you gain insight into process crashes.") for crash analysis.

### Other

Name

API value

Description

Upload plugins using the command line

`PluginUpload`

Grants permission to upload OneAgent extensions via [Extension SDK](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.").

Dynatrace provides the following permissions for personal access tokens. You can set them in the web UI as described above or via the [**Access tokens** API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Name

API value

Description

Read API tokens

`apiTokens.read`

Grants access to GET requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Write API tokens

`apiTokens.write`

Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Read entities

`entities.read`

Grants access to GET requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Write entities

`entities.write`

Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Read metrics

`metrics.read`

Grants access to GET requests of the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

Write metrics

`metrics.write`

Grants access to the [DELETE a custom metric](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2.

Read network zones

`networkZones.read`

Grants access to GET requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Write network zones

`networkZones.write`

Grants access to POST, PUT, and DELETE requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Read problems

`problems.read`

Grants access to GET requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Write problems

`problems.write`

Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Read releases

`releases.read`

Grants access to the [Releases API](/docs/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.").

Read security problems

`securityProblems.read`

Grants access to GET requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Write security problems

`securityProblems.write`

Grants access to POST requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Read settings

`settings.read`

Grants access to GET requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Write settings

`settings.write`

Grants access to POST and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Read SLO

`slo.read`

Grants access to GET requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

## Authenticate

You have two options to pass your API token: in the **Authorization** HTTP header or in the **api-token** query parameter.

We recommend that you use the **Authorization** header, as URLs (along with tokens passed within them) might be logged in various locations. Users might also bookmark the URLs or share them in plain text. Therefore, placing authentication tokens into the URL increases the risk that they will be captured by an attacker.

HTTP header

Query parameter

You can authenticate by attaching the token to the **Authorization** HTTP header preceding the **Api-Token** realm.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

The following example shows authentication via HTTP header.

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

You can authenticate by adding the token as the value of the **api-token** query parameter.

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Authentication in the API Explorer



Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

## Related topics

* [Access tokens classic](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")