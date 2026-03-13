---
title: Environment API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api
scraped: 2026-03-06T21:20:59.328501
---

# Environment API

# Environment API

* Справочник
* Опубликовано 1 апреля 2019

## Основы

[Аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

[Коды ответов](/docs/dynatrace-api/basics/dynatrace-api-response-codes "Find out which HTTP response codes are used in the Dynatrace API.")

[Ограничения доступа](/docs/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Предварительные и ранние релизы](/docs/dynatrace-api/basics/preview-early-access "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Руководства по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides "Migrate your automation to newer endpoints of the Dynatrace API.")

[API Grail](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Конечные точки

### ActiveGate

[Информация](/docs/dynatrace-api/environment-api/activegates/activegate-info "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Конфигурация автообновления](/docs/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Задания автообновления](/docs/dynatrace-api/environment-api/activegates/auto-update-jobs "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Анонимизация

[Анонимизация](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Безопасность приложений

[Уязвимости](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
[Атаки](/docs/dynatrace-api/environment-api/application-security/attacks "Find out what the Dynatrace Attacks API offers.")

### Журналы аудита

[Журналы аудита](/docs/dynatrace-api/environment-api/audit-logs "Read Dynatrace audit logs via Dynatrace API.")

![Business Observability](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Business Observability")

### Бизнес-события

[Бизнес-события](/docs/dynatrace-api/environment-api/business-analytics-v2 "Find out how you can ingest a business event with the Dynatrace Business Events API v2.")

### Информация о кластере

[Информация о кластере](/docs/dynatrace-api/environment-api/cluster-information "Find out how to check the cluster version and time with Dynatrace API.")

### Хранилище учётных данных

[Хранилище учётных данных](/docs/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.")

### Пользовательские теги

[Пользовательские теги мониторируемых сущностей](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")

### Развёртывание

[OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate "Download ActiveGate installers via Dynatrace API.")

[BOSH-архивы](/docs/dynatrace-api/environment-api/deployment/bosh "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Архивы для оркестрации](/docs/dynatrace-api/environment-api/deployment/orchestration "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### События

[Список событий](/docs/dynatrace-api/environment-api/events-v2/get-events "List events of your monitoring environment via the Dynatrace API.")

[Список типов событий](/docs/dynatrace-api/environment-api/events-v2/get-event-types "List event types via the Dynatrace API.")

[Список свойств событий](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API.")

[Приём событий](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Возможности Hub

[Возможности Hub](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.")

### Мониторинг логов

[Мониторинг логов](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

### Метрики

#### Версия 1

[Основы](/docs/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.")

#### Версия 2

[Список метрик](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.")

[Получение точек данных](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.")

[Приём точек данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Селектор метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")

[Выражения метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Единицы измерения метрик

[Список единиц](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[Просмотр единицы](/docs/dynatrace-api/environment-api/metrics-units/get-unit "View metadata of a metric unit via the Dynatrace API.")

[Конвертация единиц](/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert "Convert a metric value from one unit into another via the Dynatrace API.")

### Мониторируемые сущности

[Мониторируемые сущности](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")

### Сетевые зоны

[Сетевые зоны](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Проблемы

[Problems v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")

### Релизы

[Релизы](/docs/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.")

### Удалённая конфигурация

[OneAgent](/docs/dynatrace-api/environment-api/remote-configuration/oneagent "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/remote-configuration/activegate "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Географические регионы](/docs/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API.")

[Пользовательские сессии](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.")

[JavaScript для мониторинга реальных пользователей](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Настройки

[Настройки](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

### SLO

[Целевые уровни обслуживания](/docs/dynatrace-api/environment-api/service-level-objectives "Discover the API functionalities of the new Service-Level Objectives powered by Grail.")

### Синтетический мониторинг

[Мониторы](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")

[Выполнение мониторов v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Локации v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations "Manage synthetic locations via the Synthetic v1 API.")

[Локации v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.")

[Узлы v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-nodes "Get synthetic nodes information via the Synthetic v1 API.")

[Узлы v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.")

[Сторонний синтетический мониторинг](/docs/dynatrace-api/environment-api/synthetic/third-party-synthetic "Push third-party synthetic data to Dynatrace via API.")

### Токены

[Токены v2](/docs/dynatrace-api/environment-api/tokens-v2 "Manage Dynatrace access tokens via Dynatrace API.")

## API Explorer

Вы можете получить доступ ко всем конечным точкам Dynatrace API с помощью API Explorer.

* Актуальная версия Dynatrace Перейдите в **Access Tokens**, затем выберите ссылку **Dynatrace API Explorer**.
* Предыдущая версия Dynatrace Из [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the latest Dynatrace") прокрутите вниз до **Dynatrace API** и выберите интересующий вас раздел API.

Кроме того, вы можете получить доступ к API Explorer по прямой ссылке `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Нажмите на значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию о токенах OAuth 2.0, которые защищают эту конечную точку. Каждая конечная точка требует определённый тип токена.

Вы также можете разблокировать все конечные точки, нажав **Authorize**. В отображённом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Введя ваш токен OAuth 2.0 в глобальное диалоговое окно **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Выполнение API-вызова

После ввода токена OAuth 2.0 вы можете непосредственно выполнять API-вызовы в API Explorer. Просто нажмите **Try it out**, чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить тело запроса перед его выполнением, нажав **Execute**.
