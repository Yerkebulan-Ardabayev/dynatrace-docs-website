---
title: Dynatrace API — токены и аутентификация
source: https://docs.dynatrace.com/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication
scraped: 2026-05-12T11:19:02.313552
---

# Dynatrace API — токены и аутентификация

# Dynatrace API — токены и аутентификация

* Reference
* Published Aug 23, 2018

Для аутентификации в Dynatrace API необходим действующий [токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") или действующий [персональный токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes."). Доступ к API является детализированным, то есть токену также должны быть назначены соответствующие области доступа (scopes). Описание каждого запроса содержит перечень областей, необходимых для его использования.

Подробнее об OAuth-клиентах см. в разделе [OAuth-клиенты](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Формат токена

Dynatrace использует уникальный формат токена, состоящий из трёх компонентов, разделённых точками (`.`).

### Пример токена

`dt0s01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Компоненты токена

| Название компонента | Описание компонента |
| --- | --- |
| prefix (префикс) | **Префикс** определяет тип токена.  В нашем примере: `dt0s01`  Таблицу стандартных префиксов см. в разделе [Префиксы токенов](#token-format-prefixes) ниже. |
| public portion (публичная часть) | **Публичная часть** токена — 24-символьный публичный идентификатор.  В нашем примере: `ST2EY72KQINMH574WMNVI7YN` |
| token identifier (идентификатор токена) | **Идентификатор токена** — это комбинация **префикса** и **публичной части**. Идентификатор токена можно безопасно отображать в UI и использовать для целей журналирования.  В нашем примере: `dt0s01.ST2EY72KQINMH574WMNVI7YN` |
| secret portion (секретная часть) | **Секретная часть** токена — 64-символьная строка, с которой следует обращаться как с паролем:  * Не отображать её * Не хранить в файлах журналов * Незамедлительно ротировать при утечке  В нашем примере: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM` |

### Префиксы токенов

| Префикс | Описание |
| --- | --- |
| `dt0s01` | API-токен. Используется как метод авторизации: действующий токен позволяет пользователю вносить изменения в учётную запись Dynatrace через SCIM.  * Генерируется однократно. * Не раскрывайте секретную часть токена `dt0s01`. * Публичная часть используется для идентификации в веб-интерфейсе, однако в общем случае её также не следует раскрывать (как и любую часть этого токена). * Токен остаётся действующим до аннулирования клиентом, поэтому при его утечке необходимо незамедлительно ротировать его. |
| `dt0s02` | OAuth2-клиенты, создаваемые пользователями через Account Management для использования с приложениями Dynatrace и Account Management API. |
| `dt0s03` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s04` | Привязка чата и идентификации. |
| `dt0s06` | Это токен обновления OAuth2 (OAuth2 Refresh Token), используемый для получения нового токена доступа; как правило, часто меняется (обычно каждые 5–15 минут). |
| `dt0s08` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s09` | Привязка чата и идентификации. |
| `dt0s16` | Токен платформы (Platform Token), обеспечивающий программный доступ к сервисам платформы Dynatrace. |

## Создание токена

Токен доступа

Персональный токен доступа

Для создания токена доступа:

1. Перейдите в раздел ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя для токена.  
   Dynatrace не обеспечивает уникальность имён токенов. Можно создать несколько токенов с одинаковым именем. Для каждого создаваемого токена укажите понятное имя. Правильное именование помогает эффективно управлять токенами и при необходимости удалять их.
4. Выберите необходимые области доступа для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для последующего использования.

   Токен доступен для просмотра только один раз при создании. Впоследствии его нельзя отобразить снова.

Для создания персонального токена доступа

1. Перейдите в раздел **Personal Access Tokens** (доступен через [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform") в предыдущей версии Dynatrace).
2. Нажмите **Generate new token**.
3. Введите имя для токена.  
   Dynatrace не обеспечивает уникальность имён токенов. Можно создать несколько токенов с одинаковым именем. Для каждого создаваемого токена укажите понятное имя. Правильное именование помогает эффективно управлять токенами и при необходимости удалять их.
4. Выберите необходимые области доступа для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для последующего использования.

   Токен доступен для просмотра только один раз при создании. Впоследствии его нельзя отобразить снова.

Одному токену можно назначить несколько областей доступа либо создать несколько токенов с разными уровнями доступа и использовать их соответственно — проверьте политики безопасности вашей организации для выбора оптимального подхода.

Для изменения области доступа существующего токена используйте [PUT-запрос токена](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token "Update an access token via Dynatrace API.") в API токенов доступа. Учтите, что для сохранения существующих областей их необходимо указывать в запросе. Любая существующая область, отсутствующая в запросе, будет удалена.

Также можно использовать [POST-запрос токена](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Create an access token via Dynatrace API.") для создания токена.

## Области доступа токена

Токен доступа

Персональный токен доступа

### OpenPipeline

| Название | Значение API | Описание |
| --- | --- | --- |
| OpenPipeline - Ingest Events | `openpipeline.events` | Предоставляет доступ к запросу [POST Built-in generic events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle | `openpipeline.events_sdlc` | Предоставляет доступ к запросу [POST Built-in SLDC events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle (Custom) | `openpipeline.events_sdlc.custom` | Предоставляет доступ к запросу [POST Custom SLDC events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Built-in) | `openpipeline.events_security` | Предоставляет доступ к запросу [POST Built-in security events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Custom) | `openpipeline.events_security.custom` | Предоставляет доступ к запросу [POST Custom security events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events (Custom) | `openpipeline.events.custom` | Предоставляет доступ к запросу [POST Custom generic event endpoint](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в OpenPipeline Ingest API. |

### API v2

| Название | Значение API | Описание |
| --- | --- | --- |
| Read ActiveGates | `activeGates.read` | Предоставляет доступ к GET-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers."). |
| Write ActiveGates | `activeGates.write` | Предоставляет доступ к POST- и DELETE-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers."). |
| Create ActiveGate tokens | `activeGateTokenManagement.create` | Предоставляет доступ к POST-запросу API токенов ActiveGate. |
| Read ActiveGate tokens | `activeGateTokenManagement.read` | Предоставляет доступ к GET-запросам API токенов ActiveGate. |
| Write ActiveGate tokens | `activeGateTokenManagement.write` | Предоставляет доступ к POST- и DELETE-запросам API токенов ActiveGate. |
| Read API tokens | `apiTokens.read` | Предоставляет доступ к GET-запросам [API токенов доступа](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Write API tokens | `apiTokens.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [API токенов доступа](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Read attacks | `attacks.read` | Предоставляет доступ к GET-запросам Attacks API и [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") для Application Protection. |
| Write Application Protection settings | `attacks.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") для Application Protection. |
| Read audit logs | `auditLogs.read` | Предоставляет доступ к [журналу аудита](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API."). |
| Read credential vault entries | `credentialVault.read` | Предоставляет доступ к GET-запросам [API хранилища учётных данных](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers."). |
| Write credential vault entries | `credentialVault.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [API хранилища учётных данных](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers."). |
| Read entities | `entities.read` | Предоставляет доступ к GET-запросам API [отслеживаемых сущностей](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") и [пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API."). |
| Write entities | `entities.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам API [отслеживаемых сущностей](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") и [пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API."). |
| Ingest events | `events.ingest` | Предоставляет доступ к POST-запросу [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). |
| Read events | `events.read` | Предоставляет доступ к GET-запросам [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Предоставляет доступ к GET-запросам из раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам из раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read extensions environment configuration | `extensionEnvironment.read` | Предоставляет доступ к GET-запросам из раздела **Extensions environment configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions environment configuration | `extensionEnvironment.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам из раздела **Extensions environment configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read extensions | `extensions.read` | Предоставляет доступ к GET-запросам из раздела **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions | `extensions.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам из раздела **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read Geographic regions | `geographicRegions.read` | Предоставляет доступ к [Geographic regions API](/managed/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API."). |
| Install and update Hub items | `hub.install` | Предоставляет разрешение на установку и обновление расширений через [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Read Hub related data | `hub.read` | Предоставляет доступ к GET-запросам [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Предоставляет разрешение на управление метаданными элементов Hub через [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` |  |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` |  |
| Ingest logs | `logs.ingest` | Предоставляет доступ к запросу [POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") Log Monitoring API v2, а также к [OpenTelemetry log ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). |
| Read logs | `logs.read` | Предоставляет доступ к GET-запросам [Log Monitoring API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2."). |
| Ingest metrics | `metrics.ingest` | Предоставляет доступ к запросу [POST ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") Metrics v2 API, а также к [OpenTelemetry metrics ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). |
| Read metrics | `metrics.read` | Предоставляет доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). |
| Write metrics | `metrics.write` | Предоставляет доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Предоставляет доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Write network zones | `networkZones.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Read OneAgents | `oneAgents.read` | Предоставляет доступ к GET-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Предоставляет доступ к POST- и DELETE-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API."). |
| Ingest OpenTelemetry traces | `openTelemetryTrace.ingest` | Предоставляет разрешение на [приём трейсов OpenTelemetry](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."). |
| Read problems | `problems.read` | Предоставляет доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Write problems | `problems.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Read releases | `releases.read` | Предоставляет доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers."). |
| Read security problems | `securityProblems.read` | Предоставляет доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Write security problems | `securityProblems.write` | Предоставляет доступ к POST-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Read settings | `settings.read` | Предоставляет доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Write settings | `settings.write` | Предоставляет доступ к POST- и DELETE-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Read SLO | `slo.read` | Предоставляет доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Write SLO | `slo.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Read synthetic monitor execution results | `syntheticExecutions.read` | Предоставляет доступ к GET-запросам API `/synthetic/executions`. |
| Write synthetic monitor execution results | `syntheticExecutions.write` | Предоставляет доступ к POST-запросу API `/synthetic/executions`. |
| Read synthetic locations | `syntheticLocations.read` | Предоставляет доступ к GET-запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API."). |
| Write synthetic locations | `syntheticLocations.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API."). |
| Tenant token rotation | `tenantTokenRotation.write` | Предоставляет доступ к [Tenant tokens API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens."). |
| Look up a single trace | `traces.lookup` | Проверяет наличие трейса при межсредовой трассировке. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Предоставляет доступ к схеме Unified analysis в [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |

### API v1

| Название | Значение API | Описание |
| --- | --- | --- |
| Access problems and event feed, metrics, and topology | `DataExport` | Предоставляет доступ к различным вызовам [Environment API](/managed/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API."). |
| Create and read synthetic monitors, locations, and nodes | `ExternalSyntheticIntegration` | Предоставляет доступ к [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers."). |
| Read synthetic monitors, locations, and nodes | `ReadSyntheticData` | Предоставляет доступ к GET-запросам [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers."). |
| Read configuration | `ReadConfig` | Предоставляет доступ к GET-вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API."). |
| Write configuration | `WriteConfig` | Предоставляет доступ к POST-, PUT- и DELETE-вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API."). |
| Change data privacy settings | `DataPrivacy` | Предоставляет доступ к [Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.") и вызовам конфиденциальности данных [Web application configuration API](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers."). |
| User sessions | `DTAQLAccess` | Предоставляет доступ к [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers."). |
| Anonymize user sessions for data privacy reasons | `UserSessionAnonymization` | Предоставляет доступ к [Anonymization API](/managed/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data."). |
| Mobile symbol file management | `DssFileManagement` | Предоставляет доступ к [Mobile symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API."). |
| Real User Monitoring JavaScript tag management | `RumJavaScriptTagManagement` | Предоставляет доступ к [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API."). |
| ActiveGate certificate management | `ActiveGateCertManagement` | Предоставляет разрешение на [настройку сертификата](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.") на частных ActiveGate. |
| Fetch data from a remote environment | `RestRequestForwarding` | Предоставляет разрешение на получение данных из [удалённых сред Dynatrace](/managed/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.") для многосредовых дашбордов. |
| Capture request data | `CaptureRequestData` | Предоставляет доступ к [Request attributes API](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers."). |
| Read log content | `LogExport` | Предоставляет доступ к [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2."). |

### PaaS

| Название | Значение API | Описание |
| --- | --- | --- |
| Download OneAgent and ActiveGate installers | `InstallerDownload` | Позволяет загружать установщики через [Deployment API](/managed/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API."). |
| Create support alerts | `SupportAlert` | Позволяет создавать [оповещения поддержки](/managed/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Learn how Dynatrace can help you gain insight into process crashes.") для анализа сбоев. |

### Прочее

| Название | Значение API | Описание |
| --- | --- | --- |
| Upload plugins using the command line | `PluginUpload` | Предоставляет разрешение на загрузку расширений OneAgent через [Extension SDK](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace."). |

Dynatrace предоставляет следующие разрешения для персональных токенов доступа. Их можно задать в веб-интерфейсе, как описано выше, или через [API **Access tokens**](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

| Название | Значение API | Описание |
| --- | --- | --- |
| Read API tokens | `apiTokens.read` | Предоставляет доступ к GET-запросам [API токенов доступа](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Write API tokens | `apiTokens.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [API токенов доступа](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Read entities | `entities.read` | Предоставляет доступ к GET-запросам API [отслеживаемых сущностей](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") и [пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API."). |
| Write entities | `entities.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам API [отслеживаемых сущностей](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") и [пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API."). |
| Read metrics | `metrics.read` | Предоставляет доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). |
| Write metrics | `metrics.write` | Предоставляет доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Предоставляет доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Write network zones | `networkZones.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Read problems | `problems.read` | Предоставляет доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Write problems | `problems.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Read releases | `releases.read` | Предоставляет доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers."). |
| Read security problems | `securityProblems.read` | Предоставляет доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Write security problems | `securityProblems.write` | Предоставляет доступ к POST-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Read settings | `settings.read` | Предоставляет доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Write settings | `settings.write` | Предоставляет доступ к POST- и DELETE-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Read SLO | `slo.read` | Предоставляет доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Write SLO | `slo.write` | Предоставляет доступ к POST-, PUT- и DELETE-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |

## Аутентификация

Токен API можно передавать двумя способами: в HTTP-заголовке **Authorization** или в параметре запроса **api-token**.

Рекомендуется использовать заголовок **Authorization**, поскольку URL-адреса (вместе с токенами, переданными в них) могут быть записаны в различных местах. Пользователи также могут добавлять URL в закладки или передавать их в открытом виде. Поэтому включение токенов аутентификации в URL повышает риск их перехвата злоумышленником.

HTTP-заголовок

Параметр запроса

Аутентификацию можно выполнить, добавив токен в HTTP-заголовок **Authorization** с указанием realm **Api-Token**.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Следующий пример демонстрирует аутентификацию через HTTP-заголовок.

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Аутентификацию можно выполнить, добавив токен в качестве значения параметра запроса **api-token**.

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Аутентификация в API Explorer

Нажмите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, защищающих эту конечную точку. Для каждой конечной точки требуется определённый тип токена.

Также можно разблокировать все конечные точки, нажав **Authorize**. В отображаемом диалоговом окне можно видеть, какие разрешения токена необходимы для каждой конечной точки API. Введя OAuth 2.0-токен в глобальном диалоге **Available authorizations**, можно разблокировать все связанные конечные точки API.

## Связанные темы

* [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")