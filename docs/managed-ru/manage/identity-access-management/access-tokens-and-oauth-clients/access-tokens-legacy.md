---
title: Токены доступа
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy
scraped: 2026-05-12T12:01:26.665309
---

# Токены доступа

# Токены доступа

* Reference
* 3-min read
* Published Nov 03, 2018

Любой внешний доступ к окружению мониторинга Dynatrace основан на двух составляющих: [идентификаторе окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Понять и научиться работать с окружениями мониторинга.") и *токене доступа*.

Dynatrace использует несколько типов токенов:

* API-токены и персональные токены доступа обеспечивают доступ к [Dynatrace API](/managed/dynatrace-api "Узнайте, что необходимо для использования Dynatrace API.").
* PaaS-токены позволяют загружать установщики OneAgent и ActiveGate.
* Токены арендатора позволяют OneAgent передавать данные в Dynatrace.
* Модульные токены предоставляют доступ к модульным интеграциям.

## Формат токена

Dynatrace использует уникальный формат токена, состоящий из трёх компонентов, разделённых точками (`.`).

### Пример токена

`dt0s01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Компоненты токена

| Название компонента | Описание компонента |
| --- | --- |
| prefix (префикс) | **Префикс** определяет тип токена.  В нашем примере: `dt0s01`  Таблицу стандартных префиксов см. в разделе [Префиксы токенов](#token-format-prefixes) ниже. |
| public portion (открытая часть) | **Открытая часть** токена — это 24-символьный публичный идентификатор.  В нашем примере: `ST2EY72KQINMH574WMNVI7YN` |
| token identifier (идентификатор токена) | **Идентификатор токена** — это сочетание **префикса** и **открытой части**. Идентификатор токена можно безопасно отображать в интерфейсе и использовать в целях журналирования.  В нашем примере: `dt0s01.ST2EY72KQINMH574WMNVI7YN` |
| secret portion (секретная часть) | **Секретная часть** токена — строка из 64 символов, которую следует хранить как пароль:  * Не отображать * Не записывать в файлы журналов * Немедленно сменить в случае утечки  В нашем примере: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM` |

### Префиксы токенов

| Префикс | Описание |
| --- | --- |
| `dt0s01` | API-токен. Используется как метод авторизации: действительный токен позволяет вносить изменения в учётную запись Dynatrace через SCIM.  * Генерируется однократно. * Не раскрывать секретную часть токена `dt0s01`. * Открытая часть используется для идентификации в веб-интерфейсе, но в целом не следует раскрывать её (или любую часть этого токена). * Токен действует до аннулирования клиентом, поэтому его необходимо немедленно сменить в случае утечки. |
| `dt0s02` | OAuth2-клиенты, созданные пользователями через Account Management для использования с Dynatrace Apps и Account Management API. |
| `dt0s03` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s04` | Чат и связывание идентификаторов. |
| `dt0s06` | OAuth2 Refresh Token, используемый для получения нового токена доступа; как правило, часто меняется (обычно каждые 5–15 минут). |
| `dt0s08` | OAuth2-клиенты для внутренних и внешних сервисов и интеграций. |
| `dt0s09` | Чат и связывание идентификаторов. |
| `dt0s16` | Platform Token, обеспечивающий программный доступ к сервисам платформы Dynatrace. |

Предсказуемый формат предоставляет ряд преимуществ:

* Использование Git pre-commit хуков для предотвращения попадания токенов в репозитории исходного кода (например, с помощью инструментов типа [git-secrets](https://github.com/awslabs/git-secrets)).
* Определение правил маскирования для обфускации секретных частей токенов при записи файлов журналов.
* Обнаружение токенов во внутренних файлах или сообщениях.
* Подключение [сервиса сканирования секретов GitHub](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning#about-secret-scanning-for-public-repositories) для выявления любого токена, отправленного в публичный репозиторий GitHub.

Для поиска токенов используйте следующее регулярное выражение:

```
dt0[a-zA-Z]{1}[0-9]{2}\.[A-Z0-9]{24}\.[A-Z0-9]{64}
```

С выходом Dynatrace версии 1.210 этот формат включён по умолчанию (все вновь генерируемые токены используют новый формат).

Все существующие токены старого формата остаются действительными.

### Отключение нового формата

В течение ограниченного времени можно отказаться от использования нового формата токенов. Настройку можно найти в веб-интерфейсе CMC в разделе **Settings > API tokens**.

## API-токен

API-токены используются Dynatrace API для аутентификации различных [вызовов API](/managed/dynatrace-api "Узнайте, что необходимо для использования Dynatrace API."). API-токены имеют детальные области доступа для ограничения доступа к конкретным функциям продукта в целях безопасности.

### Области доступа токена

Просмотр доступных областей

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
| Read ActiveGates | `activeGates.read` | Предоставляет доступ к GET-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Узнайте о возможностях Dynatrace ActiveGate API."). |
| Write ActiveGates | `activeGates.write` | Предоставляет доступ к POST и DELETE запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Узнайте о возможностях Dynatrace ActiveGate API."). |
| Create ActiveGate tokens | `activeGateTokenManagement.create` | Предоставляет доступ к POST-запросу ActiveGate tokens API. |
| Read ActiveGate tokens | `activeGateTokenManagement.read` | Предоставляет доступ к GET-запросам ActiveGate tokens API. |
| Write ActiveGate tokens | `activeGateTokenManagement.write` | Предоставляет доступ к POST и DELETE запросам ActiveGate tokens API. |
| Read API tokens | `apiTokens.read` | Предоставляет доступ к GET-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Write API tokens | `apiTokens.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Read attacks | `attacks.read` | Предоставляет доступ к GET-запросам Attacks API и [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте о возможностях Dynatrace Settings API.") для Application Protection. |
| Write Application Protection settings | `attacks.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте о возможностях Dynatrace Settings API.") для Application Protection. |
| Read audit logs | `auditLogs.read` | Предоставляет доступ к [журналу аудита](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Управление журналами аудита через API."). |
| Read credential vault entries | `credentialVault.read` | Предоставляет доступ к GET-запросам [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте о возможностях Dynatrace API для учётных данных."). |
| Write credential vault entries | `credentialVault.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте о возможностях Dynatrace API для учётных данных."). |
| Read entities | `entities.read` | Предоставляет доступ к GET-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Изучите Dynatrace Monitored entities API.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами отслеживаемых объектов через Dynatrace API."). |
| Write entities | `entities.write` | Предоставляет доступ к POST, PUT и DELETE запросам API Monitored entities и Custom tags. |
| Ingest events | `events.ingest` | Предоставляет доступ к POST-запросу [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте о возможностях Dynatrace Events API v2."). |
| Read events | `events.read` | Предоставляет доступ к GET-запросам [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте о возможностях Dynatrace Events API v2."). |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Предоставляет доступ к GET-запросам раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Управление расширениями через Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions monitoring configuration** Extensions 2.0 API. |
| Read extensions environment configuration | `extensionEnvironment.read` | Предоставляет доступ к GET-запросам раздела **Extensions environment configuration** Extensions 2.0 API. |
| Write extensions environment configuration | `extensionEnvironment.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions environment configuration** Extensions 2.0 API. |
| Read extensions | `extensions.read` | Предоставляет доступ к GET-запросам раздела **Extensions** Extensions 2.0 API. |
| Write extensions | `extensions.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions** Extensions 2.0 API. |
| Read Geographic regions | `geographicRegions.read` | Предоставляет доступ к [Geographic regions API](/managed/dynatrace-api/environment-api/rum/geographic-regions "Просмотр запросов, доступных через Dynatrace Geographic regions API."). |
| Install and update Hub items | `hub.install` | Предоставляет разрешение на установку и обновление расширений через [Hub items API](/managed/dynatrace-api/environment-api/hub "Доступ к функциям Dynatrace Hub через Hub items API."). |
| Read Hub related data | `hub.read` | Предоставляет доступ к GET-запросам [Hub items API](/managed/dynatrace-api/environment-api/hub "Доступ к функциям Dynatrace Hub через Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Предоставляет разрешение на управление метаданными элементов Hub через Hub items API. |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` |  |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` |  |
| Ingest logs | `logs.ingest` | Предоставляет доступ к запросу [POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправка пользовательских журналов в Dynatrace через Log Monitoring API v2.") Log Monitoring API v2, а также [OpenTelemetry log ingest API](/managed/ingest-from/opentelemetry/otlp-api "OTLP API для экспорта данных OpenTelemetry в Dynatrace."). |
| Read logs | `logs.read` | Предоставляет доступ к GET-запросам [Log Monitoring API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте о возможностях Log Monitoring API v2."). |
| Ingest metrics | `metrics.ingest` | Предоставляет доступ к запросу [POST ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Приём пользовательских метрик в Dynatrace через Metrics v2 API.") Metrics v2 API, а также OpenTelemetry metrics ingest API. |
| Read metrics | `metrics.read` | Предоставляет доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API."). |
| Write metrics | `metrics.write` | Предоставляет доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Удаление метрики, принятой через Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Предоставляет доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API."). |
| Write network zones | `networkZones.write` | Предоставляет доступ к POST, PUT и DELETE запросам Network zones API. |
| Read OneAgents | `oneAgents.read` | Предоставляет доступ к GET-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Предоставляет доступ к POST и DELETE запросам OneAgents API. |
| Ingest OpenTelemetry traces | `openTelemetryTrace.ingest` | Предоставляет разрешение на [приём трасс OpenTelemetry](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry в Dynatrace."). |
| Read problems | `problems.read` | Предоставляет доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте о возможностях Dynatrace Problems v2 API."). |
| Write problems | `problems.write` | Предоставляет доступ к POST, PUT и DELETE запросам Problems API v2. |
| Read releases | `releases.read` | Предоставляет доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Узнайте о возможностях Dynatrace Releases API."). |
| Read security problems | `securityProblems.read` | Предоставляет доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте о возможностях vulnerabilities API."). |
| Write security problems | `securityProblems.write` | Предоставляет доступ к POST-запросам Security problems API. |
| Read settings | `settings.read` | Предоставляет доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте о возможностях Dynatrace Settings API."). |
| Write settings | `settings.write` | Предоставляет доступ к POST и DELETE запросам Settings API. |
| Read SLO | `slo.read` | Предоставляет доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте о возможностях Dynatrace SLO API classic."). |
| Write SLO | `slo.write` | Предоставляет доступ к POST, PUT и DELETE запросам Service-level objectives API. |
| Read synthetic monitor execution results | `syntheticExecutions.read` | Предоставляет доступ к GET-запросам API `/synthetic/executions`. |
| Write synthetic monitor execution results | `syntheticExecutions.write` | Предоставляет доступ к POST-запросу API `/synthetic/executions`. |
| Read synthetic locations | `syntheticLocations.read` | Предоставляет доступ к GET-запросам [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими локациями через Synthetic v2 API.") и [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через Synthetic v2 API."). |
| Write synthetic locations | `syntheticLocations.write` | Предоставляет доступ к POST, PUT и DELETE запросам Synthetic locations API v2 и Synthetic nodes API v2. |
| Tenant token rotation | `tenantTokenRotation.write` | Предоставляет доступ к [Tenant tokens API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Ротация токенов арендатора Dynatrace."). |
| Look up a single trace | `traces.lookup` | Проверяет наличие трассы в межокружённой трассировке. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Предоставляет доступ к схеме Unified analysis в [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте о возможностях Dynatrace Settings API."). |

### API v1

| Название | Значение API | Описание |
| --- | --- | --- |
| Access problems and event feed, metrics, and topology | `DataExport` | Предоставляет доступ к различным вызовам [Environment API](/managed/dynatrace-api/environment-api "Узнайте о разделе окружения Dynatrace API."). |
| Create and read synthetic monitors, locations, and nodes | `ExternalSyntheticIntegration` | Предоставляет доступ к [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Узнайте о возможностях Dynatrace Synthetic v1 API."). |
| Read synthetic monitors, locations, and nodes | `ReadSyntheticData` | Предоставляет доступ к GET-запросам [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Узнайте о возможностях Dynatrace Synthetic v1 API."). |
| Read configuration | `ReadConfig` | Предоставляет доступ к GET-вызовам [Configuration API](/managed/dynatrace-api/configuration-api "Узнайте о разделе конфигурации Dynatrace API."). |
| Write configuration | `WriteConfig` | Предоставляет доступ к POST, PUT и DELETE вызовам Configuration API. |
| Change data privacy settings | `DataPrivacy` | Предоставляет доступ к [Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api "Узнайте о Dynatrace data privacy config API.") и вызовам конфиденциальности данных [Web application configuration API](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Узнайте о Dynatrace web application config API."). |
| User sessions | `DTAQLAccess` | Предоставляет доступ к [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте о Dynatrace User Sessions Query language API."). |
| Anonymize user sessions for data privacy reasons | `UserSessionAnonymization` | Предоставляет доступ к [Anonymization API](/managed/dynatrace-api/environment-api/anonymization "Выполнение требований GDPR через Dynatrace API для удаления данных пользователей."). |
| Mobile symbol file management | `DssFileManagement` | Предоставляет доступ к [Mobile symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление файлами символов мобильных приложений через Dynatrace API."). |
| Real User Monitoring JavaScript tag management | `RumJavaScriptTagManagement` | Предоставляет доступ к [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Настройка приложений с ручной инъекцией через Real User Monitoring JavaScript API."). |
| ActiveGate certificate management | `ActiveGateCertManagement` | Предоставляет разрешение на [настройку сертификата](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Настройка SSL-сертификата на ActiveGate.") на частных ActiveGate. |
| Fetch data from a remote environment | `RestRequestForwarding` | Предоставляет разрешение на получение данных из [удалённых окружений Dynatrace](/managed/dynatrace-api/configuration-api/remote-environments "Управление конфигурациями удалённых окружений Dynatrace через Dynatrace configuration API.") для мультиокружённых дашбордов. |
| Capture request data | `CaptureRequestData` | Предоставляет доступ к [Request attributes API](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Узнайте о Dynatrace request attribute config API."). |
| Read log content | `LogExport` | Предоставляет доступ к [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте о возможностях Log Monitoring API v2."). |

### PaaS

| Название | Значение API | Описание |
| --- | --- | --- |
| Download OneAgent and ActiveGate installers | `InstallerDownload` | Разрешает загрузку установщиков через [Deployment API](/managed/dynatrace-api/environment-api/deployment "Загрузка установщиков OneAgent и ActiveGate через Dynatrace API."). |
| Create support alerts | `SupportAlert` | Разрешает создание [оповещений поддержки](/managed/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Анализ сбоев процессов с помощью Dynatrace.") для анализа сбоев. |

### Другое

| Название | Значение API | Описание |
| --- | --- | --- |
| Upload plugins using the command line | `PluginUpload` | Предоставляет разрешение на загрузку расширений OneAgent через [Extension SDK](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace."). |

### Создание API-токена

Для генерации API-токена

1. Перейдите в **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя токена.
4. Найдите и выберите необходимые разрешения для токена в списке областей доступа.
5. Нажмите **Generate token**.
6. Нажмите **Copy**, чтобы скопировать сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Одному токену можно назначить несколько разрешений, или создать несколько токенов с разными уровнями доступа и использовать их соответственно — проверьте политику безопасности вашей организации для выбора оптимального подхода.

В качестве альтернативы можно использовать вызов [POST a token](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Создание токена доступа через Dynatrace API.") Access tokens API для генерации токена.

Dynatrace не требует уникальности имён токенов. Можно создать несколько токенов с одинаковым именем. Присваивайте каждому токену содержательное имя. Правильное именование помогает эффективно управлять токенами и при необходимости удалять устаревшие.

## PaaS-токен

PaaS-токены используются для загрузки установщиков OneAgent и ActiveGate. Для генерации PaaS-токена

1. Перейдите в **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя токена.
4. Найдите и выберите необходимые разрешения в списке областей доступа.
5. Нажмите **Generate token**.
6. Нажмите **Copy**, чтобы скопировать сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей.

В качестве альтернативы можно использовать вызов API [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Создание нового токена аутентификации Dynatrace API.") для генерации токена с разрешениями `InstallerDownload` и `SupportAlert`.

## Токен арендатора

Токен арендатора используется OneAgent и ActiveGate для передачи данных в Dynatrace. Dynatrace автоматически генерирует токен арендатора и добавляет его в установщики OneAgent и ActiveGate при загрузке.

### Получение токена арендатора

Для получения токена арендатора вашего окружения выполните запрос [GET connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "Просмотр сведений о подключении OneAgent через Dynatrace API.") Deployment API. Токен арендатора находится в поле `tenantToken` тела ответа. Для аутентификации запроса потребуется PaaS-токен.

### Ротация токена арендатора

Токен арендатора можно изменять по мере необходимости (например, для соблюдения внутренних политик безопасности или в ответ на непреднамеренное раскрытие). Процедура смены токена арендатора называется *ротацией токена арендатора*. Подробнее о ротации токенов арендатора см. в разделе [Токен арендатора](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Что такое токен арендатора и как его сменить.").

## Персональный токен доступа

Все перечисленные выше типы токенов требуют прав администратора для генерации. **Персональные токены доступа** позволяют генерировать токен для использования API без прав администратора. Доступные области ограничены вашими разрешениями: через API можно использовать только те функции, к которым у вас уже есть доступ. Также данные ограничены зонами управления, к которым у вас есть доступ.

Персональный токен доступа привязан к вам. Сгенерировать персональный токен для другого пользователя невозможно.

### Включение персональных токенов доступа

Для включения этой функции требуются права администратора. После включения любой пользователь может генерировать персональный токен доступа.

Для включения персональных токенов доступа

1. Перейдите в **Settings** и выберите **Integration** > **Token settings**.
2. Включите **Enable personal access tokens**.

### Генерация персональных токенов доступа

Для генерации персонального токена доступа

1. Перейдите в **Personal Access Tokens** (доступно через [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по платформе Dynatrace Managed") в предыдущем Dynatrace).
2. Нажмите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не требует уникальности имён токенов. Можно создать несколько токенов с одинаковым именем. Присваивайте каждому токену содержательное имя для эффективного управления.
4. Выберите необходимые области доступа для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей.

   Токен доступен только один раз — при создании. Впоследствии просмотреть его невозможно.

### Области доступа токена

Просмотр доступных областей

Dynatrace предоставляет следующие разрешения для персональных токенов доступа. Их можно установить в веб-интерфейсе (описано выше) или через [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.").

| Название | Значение API | Описание |
| --- | --- | --- |
| Read API tokens | `apiTokens.read` | Предоставляет доступ к GET-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Write API tokens | `apiTokens.write` | Предоставляет доступ к POST, PUT и DELETE запросам Access tokens API. |
| Read entities | `entities.read` | Предоставляет доступ к GET-запросам API Monitored entities и Custom tags. |
| Write entities | `entities.write` | Предоставляет доступ к POST, PUT и DELETE запросам API Monitored entities и Custom tags. |
| Read metrics | `metrics.read` | Предоставляет доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API."). |
| Write metrics | `metrics.write` | Предоставляет доступ к запросу DELETE a custom metric Metrics API v2. |
| Read network zones | `networkZones.read` | Предоставляет доступ к GET-запросам Network zones API. |
| Write network zones | `networkZones.write` | Предоставляет доступ к POST, PUT и DELETE запросам Network zones API. |
| Read problems | `problems.read` | Предоставляет доступ к GET-запросам Problems API v2. |
| Write problems | `problems.write` | Предоставляет доступ к POST, PUT и DELETE запросам Problems API v2. |
| Read releases | `releases.read` | Предоставляет доступ к Releases API. |
| Read security problems | `securityProblems.read` | Предоставляет доступ к GET-запросам Security problems API. |
| Write security problems | `securityProblems.write` | Предоставляет доступ к POST-запросам Security problems API. |
| Read settings | `settings.read` | Предоставляет доступ к GET-запросам Settings API. |
| Write settings | `settings.write` | Предоставляет доступ к POST и DELETE запросам Settings API. |
| Read SLO | `slo.read` | Предоставляет доступ к GET-запросам Service-level objectives API. |
| Write SLO | `slo.write` | Предоставляет доступ к POST, PUT и DELETE запросам Service-level objectives API. |