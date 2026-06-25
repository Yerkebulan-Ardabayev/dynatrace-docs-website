---
title: Dynatrace API
source: https://docs.dynatrace.com/managed/dynatrace-api
scraped: 2026-05-12T11:37:36.983285
---

# Dynatrace API

# Dynatrace API

* Reference
* Updated on Feb 26, 2026

Используйте Dynatrace API для автоматизации задач мониторинга и экспорта различных типов данных в сторонние инструменты отчётности и анализа. Коммуникация через API обеспечивается безопасностью за счёт использования защищённого канала связи через протокол HTTPS.

## Основы

[Аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

[Коды ответов](/managed/dynatrace-api/basics/dynatrace-api-response-codes "Find out which HTTP response codes are used in the Dynatrace API.")

[Лимит доступа](/managed/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Предварительные и ранние релизы](/managed/dynatrace-api/basics/preview-early-access "How Preview and Early Access releases of Dynatrace API endpoints work")

[Руководства по миграции](/managed/dynatrace-api/basics/deprecation-migration-guides "Migrate your automation to newer endpoints of the Dynatrace API.")

## Конечные точки

Среда

Конфигурация

Управление аккаунтом

Кластер

Mission Control

### ActiveGate

[Информация](/managed/dynatrace-api/environment-api/activegates/activegate-info "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Конфигурация автообновления](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Задания автообновления](/managed/dynatrace-api/environment-api/activegates/auto-update-jobs "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Анонимизация

[Анонимизация](/managed/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Application Security

[Уязвимости](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
[Атаки](/managed/dynatrace-api/environment-api/application-security/attacks "Find out what the Dynatrace Attacks API offers.")

### Журналы аудита

[Журналы аудита](/managed/dynatrace-api/environment-api/audit-logs "Read Dynatrace audit logs via Dynatrace API.")

### Информация о кластере

[Информация о кластере](/managed/dynatrace-api/environment-api/cluster-information "Find out how to check the cluster version and time with Dynatrace API.")

### Хранилище учётных данных

[Хранилище учётных данных](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.")

### Пользовательские теги

[Пользовательские теги отслеживаемых сущностей](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")

### Развёртывание

[OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.")

[ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate "Download ActiveGate installers via Dynatrace API.")

[BOSH tarballs](/managed/dynatrace-api/environment-api/deployment/bosh "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Orchestration tarballs](/managed/dynatrace-api/environment-api/deployment/orchestration "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### События

[Список событий](/managed/dynatrace-api/environment-api/events-v2/get-events "List events of your monitoring environment via the Dynatrace API.")

[Список типов событий](/managed/dynatrace-api/environment-api/events-v2/get-event-types "List event types via the Dynatrace API.")

[Список свойств событий](/managed/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API.")

[Приём событий](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Возможности Hub

[Возможности Hub](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.")

### Log Monitoring

[Log Monitoring](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

### Метрики

#### Версия 1

[Основы](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.")

#### Версия 2

[Список метрик](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.")

[Получение точек данных](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.")

[Приём точек данных](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Metric selector](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")

[Metric expressions](/managed/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Единицы метрик

[Список единиц](/managed/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[Просмотр единицы](/managed/dynatrace-api/environment-api/metrics-units/get-unit "View metadata of a metric unit via the Dynatrace API.")

[Конвертация единиц](/managed/dynatrace-api/environment-api/metrics-units/get-unit-convert "Convert a metric value from one unit into another via the Dynatrace API.")

### Отслеживаемые сущности

[Отслеживаемые сущности](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")

### Сетевые зоны

[Сетевые зоны](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Проблемы

[Problems v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")

### Релизы

[Релизы](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.")

### Удалённая конфигурация

[OneAgent](/managed/dynatrace-api/environment-api/remote-configuration/oneagent "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](/managed/dynatrace-api/environment-api/remote-configuration/activegate "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Географические регионы](/managed/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API.")

[Пользовательские сессии](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.")

[Real User Monitoring JavaScript](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Settings

[Settings](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

### SLO

[Классические целевые уровни сервиса](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.")

### Synthetic

[Мониторы](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")

[Выполнение мониторов v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Местоположения v1](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations "Manage synthetic locations via the Synthetic v1 API.")

[Местоположения v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.")

[Узлы v1](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes "Get synthetic nodes information via the Synthetic v1 API.")

[Узлы v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.")

[Сторонний synthetic](/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic "Push third-party synthetic data to Dynatrace via API.")

### Токены

[Tokens v2](/managed/dynatrace-api/environment-api/tokens-v2 "Manage Dynatrace access tokens via Dynatrace API.")

### Обнаружение аномалий

[Приложения](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Learn what the Dynatrace Anomaly detection API for applications offers.")

[AWS](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Learn what the Dynatrace Anomaly detection API for AWS offers.")

[Сервисы баз данных](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Learn what the Dynatrace Anomaly detection API for database services offers.")

[События дисков](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Learn what the Dynatrace Anomaly detection API for disk events offers.")

[Хосты](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Learn what the Dynatrace Anomaly detection API for hosts offers.")

[Группы процессов](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups "Learn what the Dynatrace Anomaly detection API for process groups offers.")

[Сервисы](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Learn what the Dynatrace Anomaly detection API for services offers.")

[VMware](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Learn what the Dynatrace Anomaly detection API for VMware offers.")

### AWS

[Учётные данные AWS](/managed/dynatrace-api/configuration-api/aws-credentials-api "Learn what the Dynatrace AWS credentials config API offers.")

[AWS PrivateLink](/managed/dynatrace-api/configuration-api/aws-privatelink "Learn what the Dynatrace AWS PrivateLink config API offers.")

[Поддерживаемые сервисы AWS](/managed/dynatrace-api/configuration-api/aws-supported-services "Fetch a list of AWS supported services via the Dynatrace API.")

### Azure

[Учётные данные Azure](/managed/dynatrace-api/configuration-api/azure-credentials-api "Learn what the Dynatrace Azure credentials config API offers.")

[Поддерживаемые сервисы Azure](/managed/dynatrace-api/configuration-api/azure-supported-services "Fetch a list of Azure supported services via the Dynatrace API.")

### Вычисляемые метрики

[Метрики мобильных приложений](/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Manage calculated metrics for mobile and custom apps via the Dynatrace configuration API.")

[Метрики сервисов](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

[Синтетические метрики](/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Manage calculated synthetic metrics via the Dynatrace configuration API.")

[Метрики веб-приложений](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")

### Условное именование

[Условное именование](/managed/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

### Конфиденциальность данных

[Конфиденциальность данных](/managed/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.")

### Дашборды

[Дашборды](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

### Расширения

[Расширения](/managed/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

[Плагины](/managed/dynatrace-api/configuration-api/plugins-api "Find out how to manage plugins via Dynatrace configuration API.")

### Mobile

[Конфигурация мобильных и пользовательских приложений](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.")

[Символизация мобильных приложений](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.")

### OneAgent

[OneAgent на хосте](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")

[OneAgent в группе хостов](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Manage the configuration of OneAgent instances in your host groups via the Dynatrace API.")

[Конфигурация на уровне среды](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

### Удалённые среды

[Удалённые среды](/managed/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")

### Отчёты

[Отчёты](/managed/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.")

### RUM

[Разрешённые источники beacon для CORS](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors "Learn what the Dynatrace configuration API for allowed beacon origins for Cross Origin Resource Sharing offers.")

[Конфигурация обнаружения приложений](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration "Learn what the Dynatrace application detection API offers.")

[Вычисляемые метрики веб-приложений](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")

[Ресурсы контента](/managed/dynatrace-api/configuration-api/rum/content-resources "Learn what the Dynatrace configuration API for content resources offers.")

[Географические регионы — правила сопоставления IP-адресов](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Learn what the Dynatrace configuration API for IP address mapping rules offers.")

[Географические регионы — заголовки сопоставления IP](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header "Learn what the Dynatrace configuration API for IP mapping headers offers.")

[Конфигурация мобильных и пользовательских приложений](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.")

[Конфигурация веб-приложений](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers.")

### Сервисы

[Вычисляемые метрики сервисов](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

[Пользовательские сервисы](/managed/dynatrace-api/configuration-api/service-api/custom-services-api "Learn what the Dynatrace custom services config API offers.")

[Обнаружение сбоев](/managed/dynatrace-api/configuration-api/service-api/failure-detection "Learn what the Dynatrace failure detection config API offers.")

[Атрибуты запросов](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")

[Именование запросов](/managed/dynatrace-api/configuration-api/service-api/request-naming-api "Learn what the Dynatrace request naming config API offers.")

[Правила обнаружения сервисов](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")

[### Управление средами

Просмотр сред мониторинга вашего аккаунта Dynatrace.](/managed/dynatrace-api/account-management-api/environment-management-api/environment-management-api "View monitoring environments of your Dynatrace account via Environment management API.")[### Dynatrace Platform Subscription

Просмотр вашей подписки Dynatrace Platform Subscription и её использования.](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.")[### Справочные данные

Просмотр справочной информации о вашем аккаунте.](/managed/dynatrace-api/account-management-api/reference-data "Check the reference info of your account via the Reference data API.")

[### Cluster API

Используйте Cluster API для настройки и обслуживания кластера Managed.](/managed/dynatrace-api/cluster-api)

[### Mission Control API

Используйте Mission Control API для взаимодействия с Mission Control.](/managed/dynatrace-api/mission-control-api "Find out about Mission Control API for managing cluster updates and tokens.")

## API Explorer

Среда

Конфигурация

Управление аккаунтом

Вы можете получить доступ ко всем конечным точкам Dynatrace API с помощью API Explorer. В [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform") прокрутите вниз до **Dynatrace API** и выберите интересующий вас раздел API.

Кроме того, вы можете получить доступ к API Explorer по прямой ссылке `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой для отображения информации о токенах OAuth 2.0, защищающих эту конечную точку. Каждая конечная точка требует определённого типа токена.

Вы также можете разблокировать все конечные точки, нажав **Authorize**. В открывшемся диалоговом окне вы можете увидеть, какие права доступа к токену необходимы для каждой конечной точки API. Введя токен OAuth 2.0 в глобальное диалоговое окно **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Выполнение API-вызова

После ввода токена OAuth 2.0 вы можете напрямую выполнять API-вызовы в API Explorer. Просто нажмите **Try it out** для открытия раздела параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить тело запроса перед его выполнением нажатием **Execute**.

Вы можете получить доступ ко всем конечным точкам Dynatrace API с помощью API Explorer. В [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform") прокрутите вниз до **Dynatrace API** и выберите интересующий вас раздел API.

Кроме того, вы можете получить доступ к API Explorer по прямой ссылке `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой для отображения информации о токенах OAuth 2.0, защищающих эту конечную точку. Каждая конечная точка требует определённого типа токена.

Вы также можете разблокировать все конечные точки, нажав **Authorize**. В открывшемся диалоговом окне вы можете увидеть, какие права доступа к токену необходимы для каждой конечной точки API. Введя токен OAuth 2.0 в глобальное диалоговое окно **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Выполнение API-вызова

После ввода токена OAuth 2.0 вы можете напрямую выполнять API-вызовы в API Explorer. Просто нажмите **Try it out** для открытия раздела параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить тело запроса перед его выполнением нажатием **Execute**.

Вы можете получить доступ ко всем конечным точкам Dynatrace API с помощью API Explorer.

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/). Если у вас несколько аккаунтов, выберите нужный.
2. На верхней панели навигации перейдите в **Identity & access management** > **OAuth clients**.
3. В правом верхнем углу страницы выберите **Account Management API**.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой для отображения информации о токенах OAuth 2.0, защищающих эту конечную точку. Каждая конечная точка требует определённого типа токена.

Вы также можете разблокировать все конечные точки, нажав **Authorize**. В открывшемся диалоговом окне вы можете увидеть, какие права доступа к токену необходимы для каждой конечной точки API. Введя токен OAuth 2.0 в глобальное диалоговое окно **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Выполнение API-вызова

После ввода токена OAuth 2.0 вы можете напрямую выполнять API-вызовы в API Explorer. Просто нажмите **Try it out** для открытия раздела параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить тело запроса перед его выполнением нажатием **Execute**.