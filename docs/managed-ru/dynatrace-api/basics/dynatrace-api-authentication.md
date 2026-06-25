---
title: Dynatrace API - Токены и аутентификация
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/dynatrace-api-authentication
scraped: 2026-05-12T11:04:03.697731
---

# Dynatrace API - Токены и аутентификация

# Dynatrace API - Токены и аутентификация

* Reference
* Published Aug 23, 2018

Для аутентификации при работе с Dynatrace API нужен действительный [access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Концепция access token и его scopes.") или действительный [personal access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Концепция personal access token и его scopes."). Доступ к API детализированный: токену нужно назначить подходящие scopes. Смотрите описание каждого запроса, чтобы узнать, какие scopes требуются для его использования.

Подробнее об OAuth-клиентах смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth-клиенты.").

## Формат токена

Dynatrace использует уникальный формат токена из трёх компонентов, разделённых точками (`.`).

### Пример токена

`dt0s01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Компоненты токена

| Название компонента | Описание компонента |
| --- | --- |
| prefix | **Префикс** определяет тип токена.  В нашем примере: `dt0s01`  Таблицу стандартных префиксов смотрите в разделе [Префиксы токенов](#token-format-prefixes) ниже. |
| public portion | **Публичная часть** токена — это 24-символьный публичный идентификатор.  В нашем примере: `ST2EY72KQINMH574WMNVI7YN` |
| token identifier | **Идентификатор токена** — это сочетание **префикса** и **публичной части**. Идентификатор токена можно безопасно отображать в UI и использовать для логирования.  В нашем примере: `dt0s01.ST2EY72KQINMH574WMNVI7YN` |
| secret portion | **Секретная часть** токена — это 64-символьная строка, с которой нужно обращаться как с паролем:  * Не отображайте её * Не сохраняйте в лог-файлах * Срочно ротируйте при утечке  В нашем примере: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM` |

### Префиксы токенов

| Префикс | Описание |
| --- | --- |
| `dt0s01` | Это API-токен. Используется как метод авторизации: действительный токен позволяет пользователю вносить изменения в Dynatrace-аккаунт через SCIM.  * Генерируется один раз. * Не раскрывайте секретную часть токена `dt0s01`. * Публичная часть используется для идентификации в web UI, но в общем случае её тоже не следует раскрывать (как и любую часть этого токена). * Токен действует до тех пор, пока клиент его не отзовёт, поэтому при утечке его необходимо немедленно ротировать. |
| `dt0s02` | OAuth2-клиенты, создаваемые пользователями через Account Management для работы с Dynatrace Apps и Account Management API. |
| `dt0s03` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s04` | Chat и identity linking. |
| `dt0s06` | OAuth2 Refresh Token, который используется для получения нового Access Token и обычно меняется часто (как правило, каждые 5–15 минут). |
| `dt0s08` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s09` | Chat и identity linking. |
| `dt0s16` | Platform Token для программного доступа к платформенным сервисам Dynatrace. |

## Генерация токена

Access token

Personal access token

Чтобы создать access token:

1. Перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не требует уникальности имён токенов. Можно создавать несколько токенов с одним именем. Давайте каждому токену осмысленное имя. Правильное именование позволяет эффективно управлять токенами и удалять их, когда они больше не нужны.
4. Выберите нужные scopes для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Токен можно увидеть только один раз при создании. Позже посмотреть его нельзя.

Чтобы создать personal access token:

1. Перейдите в **Personal Access Tokens** (доступно через [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по платформе Dynatrace Managed") в предыдущем Dynatrace).
2. Нажмите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не требует уникальности имён токенов. Можно создавать несколько токенов с одним именем. Давайте каждому токену осмысленное имя. Правильное именование позволяет эффективно управлять токенами и удалять их, когда они больше не нужны.
4. Выберите нужные scopes для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Токен можно увидеть только один раз при создании. Позже посмотреть его нельзя.

Можно назначить несколько scopes одному токену или сгенерировать несколько токенов с разным уровнем доступа и использовать их соответственно: ориентируйтесь на политики безопасности вашей организации, чтобы выбрать лучший подход.

Чтобы изменить scope существующего токена, используйте вызов [PUT a token](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token "Обновление access token через Dynatrace API.") в Access tokens API. Учтите: чтобы сохранить существующие scopes, их нужно передать в запросе. Любой scope, отсутствующий в payload, будет удалён.

Альтернативно можно использовать вызов [POST a token](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Создание access token через Dynatrace API.") для создания токена.

## Token scopes

Access token

Personal access token

### OpenPipeline

| Название | API value | Описание |
| --- | --- | --- |
| OpenPipeline - Ingest Events | `openpipeline.events` | Доступ к запросу [POST Built-in generic events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle | `openpipeline.events_sdlc` | Доступ к запросу [POST Built-in SLDC events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle (Custom) | `openpipeline.events_sdlc.custom` | Доступ к запросу [POST Custom SLDC events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Built-in) | `openpipeline.events_security` | Доступ к запросу [POST Built-in security events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Custom) | `openpipeline.events_security.custom` | Доступ к запросу [POST Custom security events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events (Custom) | `openpipeline.events.custom` | Доступ к запросу [POST Custom generic event endpoint](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |

### API v2

| Название | API value | Описание |
| --- | --- | --- |
| Read ActiveGates | `activeGates.read` | Доступ к GET-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Возможности Dynatrace ActiveGate API."). |
| Write ActiveGates | `activeGates.write` | Доступ к POST- и DELETE-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Возможности Dynatrace ActiveGate API."). |
| Create ActiveGate tokens | `activeGateTokenManagement.create` | Доступ к POST-запросу ActiveGate tokens API. |
| Read ActiveGate tokens | `activeGateTokenManagement.read` | Доступ к GET-запросам ActiveGate tokens API. |
| Write ActiveGate tokens | `activeGateTokenManagement.write` | Доступ к POST- и DELETE-запросам ActiveGate tokens API. |
| Read API tokens | `apiTokens.read` | Доступ к GET-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Write API tokens | `apiTokens.write` | Доступ к POST-, PUT- и DELETE-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Read attacks | `attacks.read` | Доступ к GET-запросам Attacks API и [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API.") для Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, `builtin:appsec.attack-protection-allowlist-config schemas`). |
| Write Application Protection settings | `attacks.write` | Доступ к POST-, PUT- и DELETE-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API.") для Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, `builtin:appsec.attack-protection-allowlist-config schemas`). |
| Read audit logs | `auditLogs.read` | Доступ к [audit log](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Управление audit logs через API."). |
| Read credential vault entries | `credentialVault.read` | Доступ к GET-запросам [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Возможности Dynatrace API для credentials."). |
| Write credential vault entries | `credentialVault.write` | Доступ к POST-, PUT- и DELETE-запросам [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Возможности Dynatrace API для credentials."). |
| Read entities | `entities.read` | Доступ к GET-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "О Dynatrace Monitored entities API.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление custom tags отслеживаемых сущностей через Dynatrace API."). |
| Write entities | `entities.write` | Доступ к POST-, PUT- и DELETE-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "О Dynatrace Monitored entities API.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление custom tags отслеживаемых сущностей через Dynatrace API."). |
| Ingest events | `events.ingest` | Доступ к POST-запросу [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Возможности Dynatrace Events API v2."). |
| Read events | `events.read` | Доступ к GET-запросам [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Возможности Dynatrace Events API v2."). |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Доступ к GET-запросам секции **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Доступ к POST-, PUT- и DELETE-запросам секции **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Read extensions environment configuration | `extensionEnvironment.read` | Доступ к GET-запросам секции **Extensions environment configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Write extensions environment configuration | `extensionEnvironment.write` | Доступ к POST-, PUT- и DELETE-запросам секции **Extensions environment configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Read extensions | `extensions.read` | Доступ к GET-запросам секции **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Write extensions | `extensions.write` | Доступ к POST-, PUT- и DELETE-запросам секции **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Read Geographic regions | `geographicRegions.read` | Доступ к [Geographic regions API](/managed/dynatrace-api/environment-api/rum/geographic-regions "Доступные запросы Dynatrace Geographic regions API."). |
| Install and update Hub items | `hub.install` | Разрешение на установку и обновление расширений через [Hub items API](/managed/dynatrace-api/environment-api/hub "Доступ к функциям Dynatrace Hub через Hub items API."). |
| Read Hub related data | `hub.read` | Доступ к GET-запросам [Hub items API](/managed/dynatrace-api/environment-api/hub "Доступ к функциям Dynatrace Hub через Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Разрешение на управление метаданными Hub items через [Hub items API](/managed/dynatrace-api/environment-api/hub "Доступ к функциям Dynatrace Hub через Hub items API."). |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` |  |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` |  |
| Ingest logs | `logs.ingest` | Доступ к запросу [POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправка собственных логов в Dynatrace через Log Monitoring API v2.") Log Monitoring API v2, а также к [OpenTelemetry log ingest API](/managed/ingest-from/opentelemetry/otlp-api "OTLP API endpoints для экспорта данных OpenTelemetry в Dynatrace."). |
| Read logs | `logs.read` | Доступ к GET-запросам [Log Monitoring API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Возможности Log Monitoring API v2.") |
| Ingest metrics | `metrics.ingest` | Доступ к запросу [POST ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Отправка пользовательских метрик в Dynatrace через Metrics v2 API.") Metrics v2 API, а также к [OpenTelemetry metrics ingest API](/managed/ingest-from/opentelemetry/otlp-api "OTLP API endpoints для экспорта данных OpenTelemetry в Dynatrace."). |
| Read metrics | `metrics.read` | Доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API."). |
| Write metrics | `metrics.write` | Доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Удаление метрики, отправленной через Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление network zones через Dynatrace API."). |
| Write network zones | `networkZones.write` | Доступ к POST-, PUT- и DELETE-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление network zones через Dynatrace API."). |
| Read OneAgents | `oneAgents.read` | Доступ к GET-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Доступ к POST- и DELETE-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Ingest OpenTelemetry traces | `openTelemetryTrace.ingest` | Разрешение на [приём OpenTelemetry traces](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry (traces, metrics, logs) в Dynatrace."). |
| Read problems | `problems.read` | Доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Возможности Dynatrace Problems v2 API."). |
| Write problems | `problems.write` | Доступ к POST-, PUT- и DELETE-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Возможности Dynatrace Problems v2 API."). |
| Read releases | `releases.read` | Доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Возможности Dynatrace Releases API."). |
| Read security problems | `securityProblems.read` | Доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Возможности vulnerabilities API."). |
| Write security problems | `securityProblems.write` | Доступ к POST-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Возможности vulnerabilities API."). |
| Read settings | `settings.read` | Доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API."). |
| Write settings | `settings.write` | Доступ к POST- и DELETE-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API."). |
| Read SLO | `slo.read` | Доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Возможности Dynatrace SLO API classic."). |
| Write SLO | `slo.write` | Доступ к POST-, PUT- и DELETE-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Возможности Dynatrace SLO API classic."). |
| Read synthetic monitor execution results | `syntheticExecutions.read` | Доступ к GET-запросам API `/synthetic/executions`. |
| Write synthetic monitor execution results | `syntheticExecutions.write` | Доступ к POST-запросу API `/synthetic/executions`. |
| Read synthetic locations | `syntheticLocations.read` | Доступ к GET-запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление synthetic locations через Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление synthetic nodes через Synthetic v2 API."). |
| Write synthetic locations | `syntheticLocations.write` | Доступ к POST-, PUT- и DELETE-запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление synthetic locations через Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление synthetic nodes через Synthetic v2 API."). |
| Tenant token rotation | `tenantTokenRotation.write` | Доступ к [Tenant tokens API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Ротация tenant-токенов Dynatrace."). |
| Look up a single trace | `traces.lookup` | Проверка наличия trace в cross-environment tracing. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Доступ к Unified analysis schema в [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API."). |

### API v1

| Название | API value | Описание |
| --- | --- | --- |
| Access problems and event feed, metrics, and topology | `DataExport` | Доступ к различным вызовам [Environment API](/managed/dynatrace-api/environment-api "Что нужно для работы с environment-секцией Dynatrace API."). |
| Create and read synthetic monitors, locations, and nodes | `ExternalSyntheticIntegration` | Доступ к [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Возможности Dynatrace Synthetic v1 API."). |
| Read synthetic monitors, locations, and nodes | `ReadSyntheticData` | Доступ к GET-запросам [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Возможности Dynatrace Synthetic v1 API."). |
| Read configuration | `ReadConfig` | Доступ к GET-вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Что нужно для работы с configuration-секцией Dynatrace API."). |
| Write configuration | `WriteConfig` | Доступ к POST-, PUT- и DELETE-вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Что нужно для работы с configuration-секцией Dynatrace API."). |
| Change data privacy settings | `DataPrivacy` | Доступ к [Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api "Возможности Dynatrace data privacy config API.") и вызовам data privacy в [Web application configuration API](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Возможности Dynatrace web application config API."). |
| User sessions | `DTAQLAccess` | Доступ к [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Возможности Dynatrace User Sessions Query language API."). |
| Anonymize user sessions for data privacy reasons | `UserSessionAnonymization` | Доступ к [Anonymization API](/managed/dynatrace-api/environment-api/anonymization "Как выполнить требования GDPR, удаляя данные пользователей через Dynatrace API."). |
| Mobile symbol file management | `DssFileManagement` | Доступ к [Mobile symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление файлами символов мобильных приложений через Dynatrace API."). |
| Real User Monitoring JavaScript tag management | `RumJavaScriptTagManagement` | Доступ к [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Настройка и поддержка вручную внедряемых приложений через Real User Monitoring JavaScript API."). |
| ActiveGate certificate management | `ActiveGateCertManagement` | Разрешение на [настройку сертификата](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Настройка SSL-сертификата на ActiveGate.") на private ActiveGate. |
| Fetch data from a remote environment | `RestRequestForwarding` | Разрешение на получение данных с [remote Dynatrace environments](/managed/dynatrace-api/configuration-api/remote-environments "Управление конфигурациями удалённых Dynatrace environments через Dynatrace configuration API.") для multi-environment dashboarding. |
| Capture request data | `CaptureRequestData` | Доступ к [Request attributes API](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Возможности Dynatrace request attribute config API."). |
| Read log content | `LogExport` | Доступ к [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Возможности Log Monitoring API v2."). |

### PaaS

| Название | API value | Описание |
| --- | --- | --- |
| Download OneAgent and ActiveGate installers | `InstallerDownload` | Разрешает скачивание установщиков через [Deployment API](/managed/dynatrace-api/environment-api/deployment "Скачивание установщиков OneAgent и ActiveGate через Dynatrace API."). |
| Create support alerts | `SupportAlert` | Разрешает создание [support alerts](/managed/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Получение информации о падениях процессов через Dynatrace.") для crash analysis. |

### Прочее

| Название | API value | Описание |
| --- | --- | --- |
| Upload plugins using the command line | `PluginUpload` | Разрешение на загрузку расширений OneAgent через [Extension SDK](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace."). |

Dynatrace предоставляет следующие разрешения для personal access tokens. Их можно задавать в web UI описанным выше способом или через [**Access tokens** API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.").

| Название | API value | Описание |
| --- | --- | --- |
| Read API tokens | `apiTokens.read` | Доступ к GET-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Write API tokens | `apiTokens.write` | Доступ к POST-, PUT- и DELETE-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Read entities | `entities.read` | Доступ к GET-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "О Dynatrace Monitored entities API.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление custom tags отслеживаемых сущностей через Dynatrace API."). |
| Write entities | `entities.write` | Доступ к POST-, PUT- и DELETE-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "О Dynatrace Monitored entities API.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление custom tags отслеживаемых сущностей через Dynatrace API."). |
| Read metrics | `metrics.read` | Доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API."). |
| Write metrics | `metrics.write` | Доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Удаление метрики, отправленной через Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление network zones через Dynatrace API."). |
| Write network zones | `networkZones.write` | Доступ к POST-, PUT- и DELETE-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление network zones через Dynatrace API."). |
| Read problems | `problems.read` | Доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Возможности Dynatrace Problems v2 API."). |
| Write problems | `problems.write` | Доступ к POST-, PUT- и DELETE-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Возможности Dynatrace Problems v2 API."). |
| Read releases | `releases.read` | Доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Возможности Dynatrace Releases API."). |
| Read security problems | `securityProblems.read` | Доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Возможности vulnerabilities API."). |
| Write security problems | `securityProblems.write` | Доступ к POST-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Возможности vulnerabilities API."). |
| Read settings | `settings.read` | Доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API."). |
| Write settings | `settings.write` | Доступ к POST- и DELETE-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API."). |
| Read SLO | `slo.read` | Доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Возможности Dynatrace SLO API classic."). |
| Write SLO | `slo.write` | Доступ к POST-, PUT- и DELETE-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Возможности Dynatrace SLO API classic."). |

## Аутентификация

Передать API-токен можно двумя способами: в HTTP-заголовке **Authorization** или в query-параметре **api-token**.

Рекомендуем заголовок **Authorization**: URL (с токенами, передаваемыми в нём) может попадать в логи в разных местах. Пользователи могут добавить URL в закладки или поделиться им в открытом виде. Поэтому помещение токенов в URL повышает риск, что их перехватит злоумышленник.

HTTP header

Query parameter

Можно аутентифицироваться, передав токен в HTTP-заголовке **Authorization** с realm **Api-Token**.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Следующий пример показывает аутентификацию через HTTP-заголовок.

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Также можно аутентифицироваться, передав токен в качестве значения query-параметра **api-token**.

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Аутентификация в API Explorer

Нажмите иконку замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любым endpoint, чтобы посмотреть информацию о токенах OAuth 2.0, защищающих этот endpoint. Каждому endpoint нужен определённый тип токена.

Также можно разблокировать все endpoints, нажав **Authorize**. В появившемся диалоге будут видны разрешения токена, нужные каждому API endpoint. Введя свой OAuth 2.0 токен в общем диалоге **Available authorizations**, вы разблокируете все связанные API endpoints.

## Связанные темы

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Концепция access token и его scopes.")