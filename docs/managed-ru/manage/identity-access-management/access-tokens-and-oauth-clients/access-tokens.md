---
title: Токены доступа
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
scraped: 2026-05-12T11:14:08.123186
---

# Токены доступа

# Токены доступа

* Reference
* 2-min read
* Updated on Oct 25, 2023

Весь внешний доступ к вашему окружению мониторинга Dynatrace основан на двух элементах: [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Понять и научиться работать с окружениями мониторинга.") и *токене доступа*.

Dynatrace использует несколько типов токенов:

* Токены доступа и персональные токены доступа предоставляют доступ к:

  + [Dynatrace API](/managed/dynatrace-api "Узнайте, что необходимо для использования Dynatrace API.")
  + Загрузке установщиков OneAgent и ActiveGate
* [Персональные токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Узнайте о концепции персонального токена доступа и его областях доступа.") предоставляют доступ к некоторым конечным точкам Dynatrace API
* [Токены тенанта](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен тенанта и как его сменить.") позволяют OneAgent передавать данные в Dynatrace

## Формат токена

Dynatrace использует уникальный формат токена, состоящий из трёх компонентов, разделённых точками (`.`).

### Пример токена

`dt0s01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Компоненты токена

| Название компонента | Описание компонента |
| --- | --- |
| prefix | **Префикс** определяет тип токена.  В примере: `dt0s01`  Таблица стандартных префиксов приведена в разделе [Префиксы токенов](#token-format-prefixes) ниже. |
| public portion | **Публичная часть** токена — это 24-символьный открытый идентификатор.  В примере: `ST2EY72KQINMH574WMNVI7YN` |
| token identifier | **Идентификатор токена** — комбинация **префикса** и **публичной части**. Идентификатор токена можно безопасно отображать в интерфейсе и использовать в логах.  В примере: `dt0s01.ST2EY72KQINMH574WMNVI7YN` |
| secret portion | **Секретная часть** токена — это 64-символьная строка, которую следует хранить как пароль:  * Не отображать * Не хранить в лог-файлах * Немедленно заменить при утечке  В примере: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM` |

### Префиксы токенов

| Префикс | Описание |
| --- | --- |
| `dt0s01` | API-токен. Используется как метод авторизации: действительный токен позволяет вносить изменения в учётную запись Dynatrace через SCIM.  * Генерируется однократно. * Не раскрывайте секретную часть токена `dt0s01`. * Публичная часть используется для идентификации в веб-интерфейсе, однако в общем случае не следует раскрывать её (или любую часть этого токена). * Токен действует до момента отзыва клиентом, поэтому при утечке необходимо немедленно его сменить. |
| `dt0s02` | OAuth2-клиенты, созданные пользователями через Account Management для использования с Dynatrace Apps и Account Management API. |
| `dt0s03` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s04` | Чат и связывание удостоверений. |
| `dt0s06` | OAuth2 Refresh Token, используемый для получения нового токена доступа; как правило, меняется часто (обычно каждые 5–15 минут). |
| `dt0s08` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s09` | Чат и связывание удостоверений. |
| `dt0s16` | Platform Token, обеспечивающий программный доступ к сервисам платформы Dynatrace. |

Предсказуемый формат токена открывает ряд возможностей:

* Использование Git pre-commit хуков для предотвращения отправки токенов в репозитории исходного кода (например, с помощью инструментов [git-secrets](https://github.com/awslabs/git-secrets))
* Определение правил маскирования для скрытия секретных частей токенов при записи лог-файлов
* Обнаружение токенов во внутренних файлах или переписке
* Использование [сервиса сканирования секретов GitHub](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning#about-secret-scanning-for-public-repositories) для выявления токенов, попавших в публичные репозитории

Для поиска токенов используйте следующее регулярное выражение:

```
dt0[a-zA-Z]{1}[0-9]{2}\.[A-Z0-9]{24}\.[A-Z0-9]{64}
```

Начиная с Dynatrace версии 1.210 этот формат включён по умолчанию (все новые токены создаются в новом формате).

Все существующие токены старого формата остаются действительными.

### Отключение нового формата

В течение ограниченного времени можно отказаться от использования нового формата токенов:

1. В веб-интерфейсе CMC перейдите в **Settings > API tokens**.
2. Отключите параметр **Create Dynatrace API tokens in the new format**.

## Создание токена доступа

Для создания токена доступа:

1. Перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не требует уникальных имён токенов. Можно создать несколько токенов с одним именем. Назначайте значимые имена каждому токену. Правильное именование упрощает управление токенами и их удаление, когда они больше не нужны.
4. Выберите необходимые области доступа для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Доступ к токену предоставляется только один раз при его создании. Впоследствии просмотреть токен невозможно.

## Области доступа токена

Токены доступа имеют детализированные области доступа для ограничения доступа к конкретному функционалу продукта в целях безопасности.

### OpenPipeline

| Название | Значение API | Описание |
| --- | --- | --- |
| OpenPipeline - Ingest Events | `openpipeline.events` | Предоставляет доступ к запросу [POST Built-in generic events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle | `openpipeline.events_sdlc` | Предоставляет доступ к запросу [POST Built-in SLDC events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle (Custom) | `openpipeline.events_sdlc.custom` | Предоставляет доступ к запросу [POST Custom SLDC events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Built-in) | `openpipeline.events_security` | Предоставляет доступ к запросу [POST Built-in security events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Custom) | `openpipeline.events_security.custom` | Предоставляет доступ к запросу [POST Custom security events](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events (Custom) | `openpipeline.events.custom` | Предоставляет доступ к запросу [POST Custom generic event endpoint](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") OpenPipeline Ingest API. |

### API v2

| Название | Значение API | Описание |
| --- | --- | --- |
| Read ActiveGates | `activeGates.read` | Предоставляет доступ к GET-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API."). |
| Write ActiveGates | `activeGates.write` | Предоставляет доступ к POST и DELETE запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API."). |
| Create ActiveGate tokens | `activeGateTokenManagement.create` | Предоставляет доступ к POST-запросу ActiveGate tokens API. |
| Read ActiveGate tokens | `activeGateTokenManagement.read` | Предоставляет доступ к GET-запросам ActiveGate tokens API. |
| Write ActiveGate tokens | `activeGateTokenManagement.write` | Предоставляет доступ к POST и DELETE запросам ActiveGate tokens API. |
| Read API tokens | `apiTokens.read` | Предоставляет доступ к GET-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Write API tokens | `apiTokens.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Read attacks | `attacks.read` | Предоставляет доступ к GET-запросам Attacks API и [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") для Application Protection. |
| Write Application Protection settings | `attacks.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") для Application Protection. |
| Read audit logs | `auditLogs.read` | Предоставляет доступ к [журналу аудита](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Узнайте, как управлять журналами аудита с помощью API."). |
| Read credential vault entries | `credentialVault.read` | Предоставляет доступ к GET-запросам [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для учётных данных."). |
| Write credential vault entries | `credentialVault.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для учётных данных."). |
| Read entities | `entities.read` | Предоставляет доступ к GET-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте об API отслеживаемых объектов Dynatrace.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами отслеживаемых объектов через Dynatrace API."). |
| Write entities | `entities.write` | Предоставляет доступ к POST, PUT и DELETE запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте об API отслеживаемых объектов Dynatrace.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами отслеживаемых объектов через Dynatrace API."). |
| Ingest events | `events.ingest` | Предоставляет доступ к POST-запросу [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2."). |
| Read events | `events.read` | Предоставляет доступ к GET-запросам [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2."). |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Предоставляет доступ к GET-запросам раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Read extensions environment configuration | `extensionEnvironment.read` | Предоставляет доступ к GET-запросам раздела **Extensions environment configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Write extensions environment configuration | `extensionEnvironment.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions environment configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Read extensions | `extensions.read` | Предоставляет доступ к GET-запросам раздела **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Write extensions | `extensions.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Read Geographic regions | `geographicRegions.read` | Предоставляет доступ к [Geographic regions API](/managed/dynatrace-api/environment-api/rum/geographic-regions "Просмотр запросов, доступных через Dynatrace Geographic regions API."). |
| Install and update Hub items | `hub.install` | Предоставляет разрешение на установку и обновление расширений через [Hub items API](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API."). |
| Read Hub related data | `hub.read` | Предоставляет доступ к GET-запросам [Hub items API](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Предоставляет разрешение на управление метаданными элементов Hub через [Hub items API](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API."). |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` |  |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` |  |
| Ingest logs | `logs.ingest` | Предоставляет доступ к запросу [POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправка пользовательских логов в Dynatrace через Log Monitoring API v2.") Log Monitoring API v2, а также к [OpenTelemetry log ingest API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API для экспорта данных OpenTelemetry в Dynatrace."). |
| Read logs | `logs.read` | Предоставляет доступ к GET-запросам [Log Monitoring API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно делать с Log Monitoring API v2."). |
| Ingest metrics | `metrics.ingest` | Предоставляет доступ к запросу [POST ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Приём пользовательских метрик в Dynatrace через Metrics v2 API.") Metrics v2 API, а также к [OpenTelemetry metrics ingest API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API для экспорта данных OpenTelemetry в Dynatrace."). |
| Read metrics | `metrics.read` | Предоставляет доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API."). |
| Write metrics | `metrics.write` | Предоставляет доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Удаление метрики, принятой через Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Предоставляет доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API."). |
| Write network zones | `networkZones.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API."). |
| Read OneAgents | `oneAgents.read` | Предоставляет доступ к GET-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Предоставляет доступ к POST и DELETE запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Ingest OpenTelemetry traces | `openTelemetryTrace.ingest` | Предоставляет разрешение на [приём трассировок OpenTelemetry](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."). |
| Read problems | `problems.read` | Предоставляет доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Problems v2 API."). |
| Write problems | `problems.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Problems v2 API."). |
| Read releases | `releases.read` | Предоставляет доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Releases API."). |
| Read security problems | `securityProblems.read` | Предоставляет доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей."). |
| Write security problems | `securityProblems.write` | Предоставляет доступ к POST-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей."). |
| Read settings | `settings.read` | Предоставляет доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |
| Write settings | `settings.write` | Предоставляет доступ к POST и DELETE запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |
| Read SLO | `slo.read` | Предоставляет доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает классический Dynatrace SLO API."). |
| Write SLO | `slo.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает классический Dynatrace SLO API."). |
| Read synthetic monitor execution results | `syntheticExecutions.read` | Предоставляет доступ к GET-запросам API `/synthetic/executions`. |
| Write synthetic monitor execution results | `syntheticExecutions.write` | Предоставляет доступ к POST-запросу API `/synthetic/executions`. |
| Read synthetic locations | `syntheticLocations.read` | Предоставляет доступ к GET-запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими локациями через Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через Synthetic v2 API."). |
| Write synthetic locations | `syntheticLocations.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими локациями через Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через Synthetic v2 API."). |
| Tenant token rotation | `tenantTokenRotation.write` | Предоставляет доступ к [Tenant tokens API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Ротация токенов тенанта Dynatrace."). |
| Look up a single trace | `traces.lookup` | Проверяет наличие трассировки при межокружённой трассировке. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Предоставляет доступ к схеме Unified analysis в [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |

### API v1

| Название | Значение API | Описание |
| --- | --- | --- |
| Access problems and event feed, metrics, and topology | `DataExport` | Предоставляет доступ к различным вызовам [Environment API](/managed/dynatrace-api/environment-api "Узнайте, что необходимо для использования секции environment Dynatrace API."). |
| Create and read synthetic monitors, locations, and nodes | `ExternalSyntheticIntegration` | Предоставляет доступ к [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Узнайте, что предлагает Dynatrace Synthetic v1 API."). |
| Read synthetic monitors, locations, and nodes | `ReadSyntheticData` | Предоставляет доступ к GET-запросам [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Узнайте, что предлагает Dynatrace Synthetic v1 API."). |
| Read configuration | `ReadConfig` | Предоставляет доступ к GET-вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Узнайте, что необходимо для использования секции configuration Dynatrace API."). |
| Write configuration | `WriteConfig` | Предоставляет доступ к POST, PUT и DELETE вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Узнайте, что необходимо для использования секции configuration Dynatrace API."). |
| Change data privacy settings | `DataPrivacy` | Предоставляет доступ к [Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api "Узнайте, что предлагает Dynatrace data privacy config API.") и вызовам управления конфиденциальностью данных [Web application configuration API](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Узнайте, что предлагает Dynatrace web application config API."). |
| User sessions | `DTAQLAccess` | Предоставляет доступ к [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает Dynatrace User Sessions Query language API."). |
| Anonymize user sessions for data privacy reasons | `UserSessionAnonymization` | Предоставляет доступ к [Anonymization API](/managed/dynatrace-api/environment-api/anonymization "Узнайте, как выполнять требования GDPR с помощью Dynatrace API для удаления пользовательских данных."). |
| Mobile symbol file management | `DssFileManagement` | Предоставляет доступ к [Mobile symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление файлами мобильной символизации через Dynatrace API."). |
| Real User Monitoring JavaScript tag management | `RumJavaScriptTagManagement` | Предоставляет доступ к [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как использовать Dynatrace API для настройки приложений с ручной инъекцией через Real User Monitoring JavaScript API."). |
| ActiveGate certificate management | `ActiveGateCertManagement` | Предоставляет разрешение на [настройку сертификата](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.") на частных ActiveGate. |
| Fetch data from a remote environment | `RestRequestForwarding` | Предоставляет разрешение на получение данных из [удалённых окружений Dynatrace](/managed/dynatrace-api/configuration-api/remote-environments "Управление конфигурациями удалённых окружений Dynatrace через Dynatrace configuration API.") для мультиокружённых дашбордов. |
| Capture request data | `CaptureRequestData` | Предоставляет доступ к [Request attributes API](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Узнайте, что предлагает Dynatrace request attribute config API."). |
| Read log content | `LogExport` | Предоставляет доступ к [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно делать с Log Monitoring API v2."). |

### PaaS

| Название | Значение API | Описание |
| --- | --- | --- |
| Download OneAgent and ActiveGate installers | `InstallerDownload` | Разрешает загрузку установщиков через [Deployment API](/managed/dynatrace-api/environment-api/deployment "Загрузка установщиков OneAgent и ActiveGate через Dynatrace API."). |
| Create support alerts | `SupportAlert` | Разрешает создание [оповещений поддержки](/managed/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Узнайте, как Dynatrace помогает анализировать сбои процессов.") для анализа сбоев. |

### Прочее

| Название | Значение API | Описание |
| --- | --- | --- |
| Upload plugins using the command line | `PluginUpload` | Предоставляет разрешение на загрузку расширений OneAgent через [Extension SDK](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace."). |

## Связанные темы

* [Tokens API v1](/managed/dynatrace-api/environment-api/tokens-v1 "Узнайте, как управлять токенами аутентификации Dynatrace API в вашем окружении.")