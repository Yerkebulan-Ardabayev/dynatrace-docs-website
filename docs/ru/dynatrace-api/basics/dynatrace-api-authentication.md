---
title: Dynatrace API - Токены и аутентификация
source: https://www.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication
scraped: 2026-02-20T21:17:27.658549
---

# Dynatrace API - Токены и аутентификация

# Dynatrace API - Токены и аутентификация

* Ссылка
* Опубликовано 23 августа 2018 г.

Чтобы быть аутентифицированным для использования Dynatrace API, вам нужен действительный [токен доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Изучите концепцию токена доступа и его области.") или действительный [личный токен доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Изучите концепцию личного токена доступа и его области."). Доступ к API имеет тонкую настройку, что означает, что вам также нужны соответствующие области, назначенные токену. См. описание каждого запроса, чтобы узнать, какие области необходимы для его использования.

Для получения подробной информации об OAuth-клиентах см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управляйте аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Формат токена

Dynatrace использует уникальный формат токена, состоящий из трех компонентов, разделенных точками (`.`).

### Пример токена

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Компоненты токена

Название компонента

Описание компонента

префикс

**Префикс** идентифицирует тип токена.

В нашем примере: `dt0s01`

См. [Префиксы токена](#token-format-prefixes) ниже для таблицы стандартных префиксов.

публичная часть

**Публичная часть** токена - это 24-символьный публичный идентификатор.

В нашем примере: `ST2EY72KQINMH574WMNVI7YN`

идентификатор токена

**Идентификатор токена** - это сочетание **префикса** и **публичной части**. Идентификатор токена можно безопасно отображать в интерфейсе пользователя и использовать для целей ведения журнала.

В нашем примере: `<DYNATRACE_TOKEN_PLACEHOLDER>`

секретная часть

**Секретная часть** токена - это 64-символьная строка, которая должна быть behandelt как пароль:

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
* Публичная часть используется для идентификации в веб-интерфейсе, но обычно вы не должны раскрывать ее (или любую часть этого токена).
* Этот токен остается в силе до тех пор, пока не будет отменен клиентом, поэтому вы должны немедленно заменить его, если он был скомпрометирован.

`dt0s02`

OAuth2-клиенты, созданные пользователями через Управление учетными записями для использования с приложениями Dynatrace и API Управления учетными записями.

`dt0s03`

OAuth2-клиенты для внутренних и внешних сервисов и интеграций.

`dt0s04`

Связывание чата и идентификации.

`dt0s06`

Это токен обновления OAuth2, который используется для получения нового токена доступа и обычно часто меняется (обычно каждые 5-15 минут).

`dt0s08`

OAuth2-клиенты для внутренних и внешних сервисов и интеграций.

`dt0s09`

Связывание чата и идентификации.

`dt0s16`

Токен платформы, обеспечивающий программный доступ к сервисам платформы Dynatrace.

## Генерация токена

Токен доступа

Личный токен доступа

Чтобы сгенерировать токен доступа:

1. Перейдите к ![Токены доступа](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Токены доступа") **Токены доступа**.
2. Выберите **Сгенерировать новый токен**.
3. Введите имя для вашего токена.  
   Dynatrace не требует уникальных имен токенов. Вы можете создать несколько токенов с одинаковым именем. Убедитесь, что вы предоставили осмысленное имя для каждого сгенерированного токена. Правильное именование помогает вам эффективно управлять токенами и, возможно, удалять их, когда они больше не нужны.
4. Выберите необходимые области для токена.
5. Выберите **Сгенерировать токен**.
6. Скопируйте сгенерированный токен в буфер обмена. Храните токен в менеджере паролей для будущего использования.

   Вы можете получить доступ к вашему токену только один раз при его создании. Вы не сможете получить к нему доступ позже.

Чтобы сгенерировать личный токен доступа

1. Перейдите к **Личным токенам доступа** (доступно через [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по последнему Dynatrace") в предыдущем Dynatrace).
2. Выберите **Сгенерировать новый токен**.
3. Введите имя для вашего токена.  
   Dynatrace не требует уникальных имен токенов. Вы можете создать несколько токенов с одинаковым именем. Убедитесь, что вы предоставили осмысленное имя для каждого сгенерированного токена. Правильное именование помогает вам эффективно управлять токенами и, возможно, удалять их, когда они больше не нужны.
4. Выберите необходимые области для токена.
5. Выберите **Сгенерировать токен**.
6. Скопируйте сгенерированный токен в буфер обмена. Храните токен в менеджере паролей для будущего использования.

   Вы можете получить доступ к вашему токену только один раз при его создании. Вы не сможете получить к нему доступ позже.

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

OpenPipeline - Ингест событий

`openpipeline.events`

Предоставляет доступ к запросу [POST Встроенные общие события](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ингест общие события из встроенных конечных точек через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингест событий, Жизненный цикл разработки программного обеспечения

`openpipeline.events_sdlc`

Предоставляет доступ к запросу [POST Встроенные события SDLC](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ингест события SDLC из встроенных конечных точек через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингест событий, Жизненный цикл разработки программного обеспечения (Пользовательский)

`openpipeline.events_sdlc.custom`

Предоставляет доступ к запросу [POST Пользовательские события SDLC](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Настройте пользовательскую конечную точку события SDLC через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингест событий безопасности (Встроенные)

`openpipeline.events_security`

Предоставляет доступ к запросу [POST Встроенные события безопасности](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ингест события безопасности из встроенных конечных точек через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингест событий безопасности (Пользовательский)

`openpipeline.events_security.custom`

Предоставляет доступ к запросу [POST Пользовательские события безопасности](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Настройте пользовательскую конечную точку события безопасности через OpenPipeline Ingest API.") API OpenPipeline Ingest.

OpenPipeline - Ингест событий (Пользовательский)

`openpipeline.events.custom`

Предоставляет доступ к запросу [POST Пользовательская конечная точка общего события](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Настройте пользовательскую конечную точку общего события через OpenPipeline Ingest API.") API OpenPipeline Ingest.

### API v2

Name

API значение

Описание

Чтение ActiveGate

`activeGates.read`

Предоставляет доступ к запросам GET [ActiveGate API](/docs/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API.").

Запись ActiveGate

`activeGates.write`

Предоставляет доступ к запросам POST и DELETE [ActiveGate API](/docs/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API.").

Создание токенов ActiveGate

`activeGateTokenManagement.create`

Предоставляет доступ к запросу POST токенов ActiveGate API.

Чтение токенов ActiveGate

`activeGateTokenManagement.read`

Предоставляет доступ к запросам GET токенов ActiveGate API.

Запись токенов ActiveGate

`activeGateTokenManagement.write`

Предоставляет доступ к запросам POST и DELETE токенов ActiveGate API.

Чтение токенов API

`apiTokens.read`

Предоставляет доступ к запросам GET [Токенов доступа API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте токенами аутентификации Dynatrace API.").

Запись токенов API

`apiTokens.write`

Предоставляет доступ к запросам POST, PUT и DELETE [Токенов доступа API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте токенами аутентификации Dynatrace API.").

Чтение атак

`attacks.read`

Предоставляет доступ к запросам GET Атак API и [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") для Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config` и `builtin:appsec.attack-protection-allowlist-config schemas`).

Запись настроек Application Protection

`attacks.write`

Предоставляет доступ к запросам POST, PUT и DELETE [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") для Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config` и `builtin:appsec.attack-protection-allowlist-config schemas`).

Чтение аудитных журналов

`auditLogs.read`

Предоставляет доступ к [аудитному журналу](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Узнайте, как управлять аудитными журналами с помощью API.").

Чтение записей хранилища учетных данных

`credentialVault.read`

Предоставляет доступ к запросам GET [Хранилища учетных данных API](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace Хранилище учетных данных API для учетных данных.").

Запись записей хранилища учетных данных

`credentialVault.write`

Предоставляет доступ к запросам POST, PUT и DELETE [Хранилища учетных данных API](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace Хранилище учетных данных API для учетных данных.").

Чтение сущностей

`entities.read`

Предоставляет доступ к запросам GET [Отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте об Dynatrace Отслеживаемых сущностях API.") и [Пользовательских тегов](/docs/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.") API.

Запись сущностей

`entities.write`

Предоставляет доступ к запросам POST, PUT и DELETE [Отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте об Dynatrace Отслеживаемых сущностях API.") и [Пользовательских тегов](/docs/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.") API.

Ввод событий

`events.ingest`

Предоставляет доступ к запросу POST [Событий API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Событий API v2.").

Чтение событий

`events.read`

Предоставляет доступ к запросам GET [Событий API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Событий API v2.").

Чтение конфигурации мониторинга расширений

`extensionConfigurations.read`

Предоставляет доступ к запросам GET из раздела **Конфигурация мониторинга расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Запись конфигурации мониторинга расширений

`extensionConfigurations.write`

Предоставляет доступ к запросам POST, PUT и DELETE из раздела **Конфигурация мониторинга расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Чтение конфигурации окружения расширений

`extensionEnvironment.read`

Предоставляет доступ к запросам GET из раздела **Конфигурация окружения расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Запись конфигурации окружения расширений

`extensionEnvironment.write`

Предоставляет доступ к запросам POST, PUT и DELETE из раздела **Конфигурация окружения расширений** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Чтение расширений

`extensions.read`

Предоставляет доступ к запросам GET из раздела **Расширения** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Запись расширений

`extensions.write`

Предоставляет доступ к запросам POST, PUT и DELETE из раздела **Расширения** [Расширений 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Расширений 2.0 API.").

Чтение географических регионов

`geographicRegions.read`

Предоставляет доступ к [Географическим регионам API](/docs/dynatrace-api/environment-api/rum/geographic-regions "Просмотрите запросы, доступные через Dynatrace Географические регионы API.").

Установка и обновление элементов Hub

`hub.install`

Предоставляет разрешение на установку и обновление расширений через [Элементы Hub API](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.").

Чтение данных, связанных с Hub

`hub.read`

Предоставляет доступ к запросам GET [Элементов Hub API](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.").

Управление метаданными элементов Hub

`hub.write`

Предоставляет разрешение на управление метаданными элементов Hub через [Элементы Hub API](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.").

Чтение файлов сопоставления JavaScript

`javaScriptMappingFiles.read`

Запись файлов сопоставления JavaScript

`javaScriptMappingFiles.write`

Ввод журналов

`logs.ingest`

Предоставляет доступ к запросу [POST ввода журналов](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправьте пользовательские журналы в Dynatrace через Мониторинг журналов API v2.") Мониторинга журналов API v2, а также к [Конечной точке OpenTelemetry для ввода журналов](/docs/ingest-from/opentelemetry/otlp-api "Узнайте об конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Чтение журналов

`logs.read`

Предоставляет доступ к запросам GET [Мониторинга журналов API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно сделать с помощью Мониторинга журналов API v2.").

Ввод метрик

`metrics.ingest`

Предоставляет доступ к запросу [POST ввода данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ввод пользовательских метрик в Dynatrace через Метрики v2 API.") Метрик v2 API, а также к [Конечной точке OpenTelemetry для ввода метрик](/docs/ingest-from/opentelemetry/otlp-api "Узнайте об конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

Чтение метрик

`metrics.read`

Предоставляет доступ к запросам GET [Метрик API v2](/docs/dynatrace-api/environment-api/metric-v2 "Получите информацию о метриках через Метрики v2 API.").

Запись метрик

`metrics.write`

Предоставляет доступ к запросу [Удаление пользовательской метрики](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Удалите метрику, введенную через Метрики v2 API.") Метрик API v2.

Чтение сетевых зон

`networkZones.read`

Предоставляет доступ к запросам GET [Сетевых зон API](/docs/dynatrace-api/environment-api/network-zones "Управляйте сетевыми зонами через Dynatrace API.").

Запись сетевых зон

`networkZones.write`

Предоставляет доступ к запросам POST, PUT и DELETE [Сетевых зон API](/docs/dynatrace-api/environment-api/network-zones "Управляйте сетевыми зонами через Dynatrace API.").

Чтение OneAgent

`oneAgents.read`

Предоставляет доступ к запросам GET [OneAgent API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверьте конфигурацию экземпляров OneAgent на ваших хостах через Dynatrace API.").

Запись OneAgent

`oneAgents.write`

Предоставляет доступ к запросам POST и DELETE [OneAgent API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверьте конфигурацию экземпляров OneAgent на ваших хостах через Dynatrace API.").

Ввод трасс OpenTelemetry

`openTelemetryTrace.ingest`

Предоставляет разрешение на [ввод трасс OpenTelemetry](/docs/ingest-from/opentelemetry "Узнайте, как интегрировать и вводить данные OpenTelemetry (трассы, метрики и журналы) в Dynatrace.").

Чтение проблем

`problems.read`

Предоставляет доступ к запросам GET [Проблем API v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.").

Запись проблем

`problems.write`

Предоставляет доступ к запросам POST, PUT и DELETE [Проблем API v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.").

Чтение релизов

`releases.read`

Предоставляет доступ к [Релизам API](/docs/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Релизы API.").

Чтение проблем безопасности

`securityProblems.read`

Предоставляет доступ к GET-запросам [проблем безопасности API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагают уязвимости API.").

Запись проблем безопасности

`securityProblems.write`

Предоставляет доступ к POST-запросам [проблем безопасности API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагают уязвимости API.").

Чтение настроек

`settings.read`

Предоставляет доступ к GET-запросам [настроек API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагают настройки Dynatrace API.").

Запись настроек

`settings.write`

Предоставляет доступ к POST- и DELETE-запросам [настроек API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагают настройки Dynatrace API.").

Чтение SLO

`slo.read`

Предоставляет доступ к GET-запросам [целевых показателей обслуживания API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагают классические SLO Dynatrace API.").

Запись SLO

`slo.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [целевых показателей обслуживания API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагают классические SLO Dynatrace API.").

Чтение результатов выполнения синтетического мониторинга

`syntheticExecutions.read`

Предоставляет доступ к GET-запросам `/synthetic/executions` API.

Запись результатов выполнения синтетического мониторинга

`syntheticExecutions.write`

Предоставляет доступ к POST-запросу `/synthetic/executions` API.

Чтение синтетических местоположений

`syntheticLocations.read`

Предоставляет доступ к GET-запросам [синтетических местоположений API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими местоположениями через Synthetic v2 API.") и [синтетических узлов API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через Synthetic v2 API.").

Запись синтетических местоположений

`syntheticLocations.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [синтетических местоположений API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими местоположениями через Synthetic v2 API.") и [синтетических узлов API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через Synthetic v2 API.").

Ротация токенов арендатора

`tenantTokenRotation.write`

Предоставляет доступ к [токенам арендатора API](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Поворот Dynatrace токенов арендатора.").

Поиск одной трассы

`traces.lookup`

Проверяет наличие трассы в межсредовой трассировке.

Чтение объединенной аналитики

`unifiedAnalysis.read`

Предоставляет доступ к схеме объединенной аналитики в [настройках API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагают настройки Dynatrace API.")

### API v1

Имя

API значение

Описание

Проблемы доступа и лента событий, метрики и топология

`DataExport`

Предоставляет доступ к различным вызовам [Environment API](/docs/dynatrace-api/environment-api "Узнайте, что вам нужно использовать для раздела среды Dynatrace API.").

Создание и чтение синтетических мониторов, местоположений и узлов

`ExternalSyntheticIntegration`

Предоставляет доступ к [Синтетическому API](/docs/dynatrace-api/environment-api/synthetic "Узнайте, что предлагает Dynatrace Синтетический v1 API.").

Чтение синтетических мониторов, местоположений и узлов

`ReadSyntheticData`

Предоставляет доступ к GET-запросам [Синтетического API](/docs/dynatrace-api/environment-api/synthetic "Узнайте, что предлагает Dynatrace Синтетический v1 API.").

Чтение конфигурации

`ReadConfig`

Предоставляет доступ к GET-запросам [Конфигурации API](/docs/dynatrace-api/configuration-api "Узнайте, что вам нужно использовать для раздела конфигурации Dynatrace API.").

Запись конфигурации

`WriteConfig`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Конфигурации API](/docs/dynatrace-api/configuration-api "Узнайте, что вам нужно использовать для раздела конфигурации Dynatrace API.").

Изменение настроек конфиденциальности данных

`DataPrivacy`

Предоставляет доступ к [Настройкам конфиденциальности данных API](/docs/dynatrace-api/configuration-api/data-privacy-api "Узнайте, что предлагает Dynatrace конфигурация конфиденциальности данных API.") и вызовам конфиденциальности данных [Конфигурации веб-приложения API](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Узнайте, что предлагает Dynatrace конфигурация веб-приложения API.").

Сессии пользователей

`DTAQLAccess`

Предоставляет доступ к [Сессиям пользователей API](/docs/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает Dynatrace язык запросов сессий пользователей API.").

Анонимизация сессий пользователей по причинам конфиденциальности данных

`UserSessionAnonymization`

Предоставляет доступ к [Анонимизации API](/docs/dynatrace-api/environment-api/anonymization "Узнайте, как выполнить требования GDPR, используя Dynatrace API для удаления данных пользователей.").

Управление файлами символов мобильных устройств

`DssFileManagement`

Предоставляет доступ к [Символизации мобильных устройств API](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Управляйте файлами символов мобильных устройств через Dynatrace API.").

Real User Monitoring управление тегами JavaScript

`RumJavaScriptTagManagement`

Предоставляет доступ к [Тегам JavaScript API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как вы можете использовать Dynatrace API, чтобы настроить и поддерживать ваши вручную инъектированные приложения, используя теги JavaScript API.").

ActiveGate управление сертификатами

`ActiveGateCertManagement`

Предоставляет разрешение на [настройку сертификата](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить сертификат SSL на вашем ActiveGate.") на частных ActiveGate.

Получение данных из удаленной среды

`RestRequestForwarding`

Предоставляет разрешение на получение данных из [удаленных сред Dynatrace](/docs/dynatrace-api/configuration-api/remote-environments "Управляйте конфигурациями удаленных сред Dynatrace через Dynatrace конфигурацию API.") для панелей мониторинга нескольких сред.

Получение данных запросов

`CaptureRequestData`

Предоставляет доступ к [Атрибутам запросов API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Узнайте, что предлагает Dynatrace конфигурация атрибутов запросов API.").

Чтение содержимого журнала

`LogExport`

Предоставляет доступ к [Мониторингу журналов API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что вы можете делать с помощью Мониторинга журналов API v2.").

### PaaS

Имя

API значение

Описание

Загрузка установщиков OneAgent и ActiveGate

`InstallerDownload`

Позволяет загрузить установщики через [Раздел развертывания API](/docs/dynatrace-api/environment-api/deployment "Загрузите установщики OneAgent и ActiveGate через Dynatrace API.").

Создание оповещений поддержки

`SupportAlert`

Позволяет создавать [оповещения поддержки](/docs/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Узнайте, как Dynatrace может помочь вам получить информацию о сбоях процессов.") для анализа сбоев.

### Другое

Имя

API значение

Описание

Загрузка плагинов через командную строку

`PluginUpload`

Предоставляет разрешение на загрузку расширений OneAgent через [Раздел расширений SDK](/docs/ingest-from/extensions/develop-your-extensions "Разработайте свои собственные расширения Extensions в Dynatrace.").

Dynatrace предоставляет следующие разрешения для личных токенов доступа. Вы можете настроить их в веб-интерфейсе, как описано выше, или через [**Токены доступа** API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте токенами аутентификации Dynatrace API.").

Имя

API значение

Описание

Чтение токенов API

`apiTokens.read`

Предоставляет доступ к GET-запросам [Токенов доступа API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте токенами аутентификации Dynatrace API.").

Запись токенов API

`apiTokens.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Токенов доступа API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Управляйте токенами аутентификации Dynatrace API.").

Чтение сущностей

`entities.read`

Предоставляет доступ к GET-запросам [Отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о сущностях Dynatrace API.") и [Пользовательских тегов](/docs/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.") API.

Запись сущностей

`entities.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о сущностях Dynatrace API.") и [Пользовательских тегов](/docs/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.") API.

Чтение метрик

`metrics.read`

Предоставляет доступ к GET-запросам [Метрик API v2](/docs/dynatrace-api/environment-api/metric-v2 "Получите информацию о метриках через Метрики v2 API.").

Запись метрик

`metrics.write`

Предоставляет доступ к DELETE-запросу [Метрик API v2](/docs/dynatrace-api/environment-api/metric-v2 "Получите информацию о метриках через Метрики v2 API.").

Чтение сетевых зон

`networkZones.read`

Предоставляет доступ к GET-запросам [Сетевых зон API](/docs/dynatrace-api/environment-api/network-zones "Управляйте сетевыми зонами через Dynatrace API.").

Запись сетевых зон

`networkZones.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Сетевых зон API](/docs/dynatrace-api/environment-api/network-zones "Управляйте сетевыми зонами через Dynatrace API.").

Чтение проблем

`problems.read`

Предоставляет доступ к GET-запросам [Проблем API v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.").

Запись проблем

`problems.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Проблем API v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.").

Чтение релизов

`releases.read`

Предоставляет доступ к [Релизам API](/docs/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Релизы API.").

Чтение проблем безопасности

`securityProblems.read`

Предоставляет доступ к GET-запросам [Проблем безопасности API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает уязвимости API.").

Запись проблем безопасности

`securityProblems.write`

Предоставляет доступ к POST-запросам [Проблем безопасности API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает уязвимости API.").

Чтение настроек

`settings.read`

Предоставляет доступ к GET-запросам [Настроек API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.").

Запись настроек

`settings.write`

Предоставляет доступ к POST- и DELETE-запросам [Настроек API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.").

Чтение SLO

`slo.read`

Предоставляет доступ к GET-запросам [Целей обслуживания API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает Dynatrace SLO API классический.").

Запись SLO

`slo.write`

Предоставляет доступ к POST-, PUT- и DELETE-запросам [Целей обслуживания API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает Dynatrace SLO API классический.").

## Аутентификация

У вас есть два варианта передачи токена API: в заголовке HTTP **Authorization** или в параметре запроса **api-token**.

Мы рекомендуем использовать заголовок **Authorization**, поскольку URL (вместе с переданными в них токенами) могут быть записаны в различных местах. Пользователи также могут добавлять URL в закладки или делиться ими в открытом тексте. Следовательно, размещение токенов аутентификации в URL увеличивает риск их перехвата злоумышленником.

Заголовок HTTP

Параметр запроса

Вы можете аутентифицироваться, прикрепив токен к заголовку HTTP **Authorization** перед областью **Api-Token**.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Следующий пример показывает аутентификацию через заголовок HTTP.

```
curl --request GET \
 
--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \
 
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Вы можете аутентифицироваться, добавив токен в качестве значения параметра запроса **api-token**.

```
curl --request GET \
 
--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой API конечной точки. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные API конечные точки.

## Связанные темы

* [Классические токены доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Изучите понятие токена доступа и его области.")