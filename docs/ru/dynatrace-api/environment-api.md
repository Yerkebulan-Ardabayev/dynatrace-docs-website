---
title: Environment API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api
scraped: 2026-03-06T21:20:59.328501
---

# Environment API


* Справочник
* Опубликовано 1 апреля 2019

## Основы

[Аутентификация](basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.")

[Коды ответов](basics/dynatrace-api-response-codes.md "Find out which HTTP response codes are used in the Dynatrace API.")

[Ограничения доступа](basics/access-limit.md "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Предварительные и ранние релизы](basics/preview-early-access.md "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Руководства по миграции](basics/deprecation-migration-guides.md "Migrate your automation to newer endpoints of the Dynatrace API.")

[API Grail](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Конечные точки

### ActiveGate

[Информация](environment-api/activegates/activegate-info.md "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Конфигурация автообновления](environment-api/activegates/auto-update-config.md "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Задания автообновления](environment-api/activegates/auto-update-jobs.md "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Анонимизация

[Анонимизация](environment-api/anonymization.md "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Безопасность приложений

[Уязвимости](environment-api/application-security/vulnerabilities.md "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](environment-api/application-security/davis-security-advice.md "View the Davis Security Advisor recommendations via Dynatrace API.")
[Атаки](environment-api/application-security/attacks.md "Find out what the Dynatrace Attacks API offers.")

### Журналы аудита

[Журналы аудита](environment-api/audit-logs.md "Read Dynatrace audit logs via Dynatrace API.")

![Business Observability](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Business Observability")

### Бизнес-события

[Бизнес-события](environment-api/business-analytics-v2.md "Find out how you can ingest a business event with the Dynatrace Business Events API v2.")

### Информация о кластере

[Информация о кластере](environment-api/cluster-information.md "Find out how to check the cluster version and time with Dynatrace API.")

### Хранилище учётных данных

[Хранилище учётных данных](environment-api/credential-vault.md "Learn what the Dynatrace API for credentials offers.")

### Пользовательские теги

[Пользовательские теги мониторируемых сущностей](environment-api/custom-tags.md "Manage custom tags of the monitored entities via the Dynatrace API.")

### Развёртывание

[OneAgent](environment-api/deployment/oneagent.md "Download OneAgent installers via Dynatrace API.")

[ActiveGate](environment-api/deployment/activegate.md "Download ActiveGate installers via Dynatrace API.")

[BOSH-архивы](environment-api/deployment/bosh.md "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Архивы для оркестрации](environment-api/deployment/orchestration.md "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### События

[Список событий](environment-api/events-v2/get-events.md "List events of your monitoring environment via the Dynatrace API.")

[Список типов событий](environment-api/events-v2/get-event-types.md "List event types via the Dynatrace API.")

[Список свойств событий](environment-api/events-v2/get-event-properties.md "List all event properties via the Dynatrace API.")

[Приём событий](environment-api/events-v2/post-event.md "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](environment-api/extensions-20.md "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Возможности Hub

[Возможности Hub](environment-api/hub.md "Learn how to access Dynatrace Hub features via the Hub items API.")

### Мониторинг логов

[Мониторинг логов](environment-api/log-monitoring-v2.md "Find out what you can do with the Log Monitoring API v2.")

### Метрики

#### Версия 1

[Основы](environment-api/metric-v1.md "Retrieve metric information via Timeseries v1 API.")

#### Версия 2

[Список метрик](environment-api/metric-v2/get-all-metrics.md "List all metrics available in your monitoring environment via Metrics v2 API.")

[Получение точек данных](environment-api/metric-v2/get-data-points.md "Read data points of one or multiple metrics via Metrics v2 API.")

[Приём точек данных](environment-api/metric-v2/post-ingest-metrics.md "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Селектор метрик](environment-api/metric-v2/metric-selector.md "Configure the metric selector for the Metric v2 API.")

[Выражения метрик](environment-api/metric-v2/metric-expressions.md "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Единицы измерения метрик

[Список единиц](environment-api/metrics-units/get-all-units.md "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[Просмотр единицы](environment-api/metrics-units/get-unit.md "View metadata of a metric unit via the Dynatrace API.")

[Конвертация единиц](environment-api/metrics-units/get-unit-convert.md "Convert a metric value from one unit into another via the Dynatrace API.")

### Мониторируемые сущности

[Мониторируемые сущности](environment-api/entity-v2.md "Learn about the Dynatrace Monitored entities API.")

### Сетевые зоны

[Сетевые зоны](environment-api/network-zones.md "Manage network zones via the Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Проблемы

[Problems v2](environment-api/problems-v2.md "Find out what the Dynatrace Problems v2 API offers.")

### Релизы

[Релизы](environment-api/releaseapi.md "Find out what the Dynatrace Releases API offers.")

### Удалённая конфигурация

[OneAgent](environment-api/remote-configuration/oneagent.md "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](environment-api/remote-configuration/activegate.md "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Географические регионы](environment-api/rum/geographic-regions.md "View requests available through the Dynatrace Geographic regions API.")

[Пользовательские сессии](environment-api/rum/user-sessions.md "Learn what the Dynatrace User Sessions Query language API offers.")

[JavaScript для мониторинга реальных пользователей](environment-api/rum/real-user-monitoring-javascript-code.md "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Настройки

[Настройки](environment-api/settings.md "Find out what the Dynatrace Settings API offers.")

### SLO

[Целевые уровни обслуживания](environment-api/service-level-objectives.md "Discover the API functionalities of the new Service-Level Objectives powered by Grail.")

### Синтетический мониторинг

[Мониторы](environment-api/synthetic/synthetic-monitors.md "Manage synthetic monitors via the Synthetic v1 API.")

[Выполнение мониторов v2](environment-api/synthetic-v2/synthetic-monitor-execution.md "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Локации v1](environment-api/synthetic/synthetic-locations.md "Manage synthetic locations via the Synthetic v1 API.")

[Локации v2](environment-api/synthetic-v2/synthetic-locations-v2.md "Manage synthetic locations via the Synthetic v2 API.")

[Узлы v1](environment-api/synthetic/synthetic-nodes.md "Get synthetic nodes information via the Synthetic v1 API.")

[Узлы v2](environment-api/synthetic-v2/synthetic-nodes-v2.md "Manage synthetic nodes via the Synthetic v2 API.")

[Сторонний синтетический мониторинг](environment-api/synthetic/third-party-synthetic.md "Push third-party synthetic data to Dynatrace via API.")

### Токены

[Токены v2](environment-api/tokens-v2.md "Manage Dynatrace access tokens via Dynatrace API.")

## API Explorer

Вы можете получить доступ ко всем конечным точкам Dynatrace API с помощью API Explorer.

* Актуальная версия Dynatrace Перейдите в **Access Tokens**, затем выберите ссылку **Dynatrace API Explorer**.
* Предыдущая версия Dynatrace Из [меню пользователя](../discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Navigate the latest Dynatrace") прокрутите вниз до **Dynatrace API** и выберите интересующий вас раздел API.

Кроме того, вы можете получить доступ к API Explorer по прямой ссылке `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Нажмите на значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию о токенах OAuth 2.0, которые защищают эту конечную точку. Каждая конечная точка требует определённый тип токена.

Вы также можете разблокировать все конечные точки, нажав **Authorize**. В отображённом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Введя ваш токен OAuth 2.0 в глобальное диалоговое окно **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Выполнение API-вызова

После ввода токена OAuth 2.0 вы можете непосредственно выполнять API-вызовы в API Explorer. Просто нажмите **Try it out**, чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить тело запроса перед его выполнением, нажав **Execute**.
