---
title: Персональный токен доступа
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token
scraped: 2026-05-12T11:14:04.904893
---

# Персональный токен доступа

# Персональный токен доступа

* 6-min read
* Published Sep 15, 2021

Обычно для создания токенов доступа требуются права администратора. Однако *персональные токены доступа* позволяют создавать токены для работы с API без прав администратора. Доступные области доступа не фильтруются заранее на основе ваших разрешений. Вместо этого ваши разрешения проверяются каждый раз при использовании персонального токена доступа для авторизации запроса. Кроме того, вы ограничены данными из зон управления, к которым у вас есть доступ.

Персональный токен доступа привязан к вашей учётной записи. Создать персональный токен доступа для другого пользователя невозможно.

## Включение персональных токенов доступа

Для включения этой функции необходимы права администратора. После включения любой пользователь может создавать персональные токены доступа.

Включение персональных токенов доступа

1. Перейдите в **Settings** и выберите **Integration** > **Access tokens**.
2. Включите параметр **Enable personal access tokens**.

## Создание персональных токенов доступа

Создание персонального токена доступа

1. Перейдите в **Personal Access Tokens** (доступно через [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по платформе Dynatrace Managed") в предыдущей версии Dynatrace).
2. Нажмите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не требует уникальных имён токенов. Можно создать несколько токенов с одним именем. Назначайте значимые имена каждому токену. Правильное именование упрощает управление токенами и их удаление, когда они больше не нужны.
4. Выберите необходимые области доступа для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Доступ к токену предоставляется только один раз при его создании. Впоследствии просмотреть токен невозможно.

## Доступные области доступа

| Название | Значение API | Описание |
| --- | --- | --- |
| Read ActiveGates | `activeGates.read` | Предоставляет доступ к GET-запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API."). |
| Write ActiveGates | `activeGates.write` | Предоставляет доступ к POST и DELETE запросам [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Узнайте, что предлагает Dynatrace ActiveGate API."). |
| Read analyzers | `analyzers.read` |  |
| Write and execute analyzers | `analyzers.write` |  |
| Read API tokens | `apiTokens.read` | Предоставляет доступ к GET-запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Write API tokens | `apiTokens.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API."). |
| Read attacks | `attacks.read` | Предоставляет доступ к GET-запросам Attacks API и схемам, связанным с атаками, в [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |
| Write Application Protection settings | `attacks.write` | Предоставляет доступ к POST, PUT и DELETE запросам Settings API для Application Protection. |
| Read entities | `entities.read` | Предоставляет доступ к GET-запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте об API отслеживаемых объектов Dynatrace.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами отслеживаемых объектов через Dynatrace API."). |
| Write entities | `entities.write` | Предоставляет доступ к POST, PUT и DELETE запросам API [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте об API отслеживаемых объектов Dynatrace.") и [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами отслеживаемых объектов через Dynatrace API."). |
| Ingest events | `events.ingest` | Предоставляет доступ к POST-запросу [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2."). |
| Read events | `events.read` | Предоставляет доступ к GET-запросам [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2."). |
| Actions for extension monitoring configurations | `extensionConfigurationActions.write` |  |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Предоставляет доступ к GET-запросам раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions monitoring configuration** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Read extensions | `extensions.read` | Предоставляет доступ к GET-запросам раздела **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Write extensions | `extensions.write` | Предоставляет доступ к POST, PUT и DELETE запросам раздела **Extensions** [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). |
| Read Geographic regions | `geographicRegions.read` | Предоставляет доступ к GET-запросам Geographic regions API. |
| Install and update Hub items | `hub.install` | Предоставляет разрешение на установку и обновление расширений через [Hub items API](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API."). |
| Read Hub-related data | `hub.read` | Предоставляет доступ к GET-запросам [Hub items API](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Предоставляет разрешение на управление метаданными [Hub items API](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API."). |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` | Предоставляет доступ к GET-запросам JavaScript mapping files API. |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` | Предоставляет доступ к PUT и DELETE запросам JavaScript mapping files API. |
| Read metrics | `metrics.read` | Предоставляет доступ к GET-запросам [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API."). |
| Write metrics | `metrics.write` | Предоставляет доступ к запросу [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Удаление метрики, принятой через Metrics v2 API.") Metrics API v2. |
| Read network zones | `networkZones.read` | Предоставляет доступ к GET-запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API."). |
| Write network zones | `networkZones.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API."). |
| Read OneAgents | `oneAgents.read` | Предоставляет доступ к GET-запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Предоставляет доступ к POST и DELETE запросам [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API."). |
| Read problems | `problems.read` | Предоставляет доступ к GET-запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Problems v2 API."). |
| Write problems | `problems.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Problems v2 API."). |
| Read releases | `releases.read` | Предоставляет доступ к [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Releases API."). |
| Read RUM cookie names | `rumCookieNames.read` |  |
| Read security problems | `securityProblems.read` | Предоставляет доступ к GET-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей."). |
| Write security problems | `securityProblems.write` | Предоставляет доступ к POST-запросам [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей."). |
| Read settings | `settings.read` | Предоставляет доступ к GET-запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |
| Write settings | `settings.write` | Предоставляет доступ к POST и DELETE запросам [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |
| Read SLOs | `slo.read` | Предоставляет доступ к GET-запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает классический Dynatrace SLO API."). |
| Write SLOs | `slo.write` | Предоставляет доступ к POST, PUT и DELETE запросам [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает классический Dynatrace SLO API."). |
| Look up a single trace | `traces.lookup` | Проверяет наличие трассировки. Требуется для межокружённой трассировки. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Предоставляет доступ к схеме Unified analysis в [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). |

## Связанные темы

* [Tokens API v1](/managed/dynatrace-api/environment-api/tokens-v1 "Узнайте, как управлять токенами аутентификации Dynatrace API в вашем окружении.")