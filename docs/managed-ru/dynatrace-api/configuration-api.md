---
title: Configuration API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api
scraped: 2026-05-12T11:02:59.960540
---

# Configuration API

# Configuration API

* Reference
* Published Oct 18, 2018

Автоматизация — ключ к успешным IT-операциям. Автоматизация также ключ к успешному мониторингу и тому, как вы настраиваете окружение мониторинга или software intelligence-платформу.

Управление конфигурацией критически важно: вы вряд ли позволите кому-то менять конфигурацию production-окружения мониторинга без надлежащих staging-тестов.

Отслеживание всех изменений в конфигурациях, это ещё один важный аспект того, что обычно называется *configuration as code*.

Configuration as code вводит стратегию управления конфигурациями мониторинга Dynatrace так же, как вы управляете исходным кодом. Управление конфигурациями должно следовать тем же принципам и правилам, что вы применяете к критическому production-коду. Конфигурации должны валидироваться, тестироваться, разворачиваться и версионироваться контролируемо и воспроизводимо.

Без таких правил настройка ваших окружений может превратиться в хаос с потерей гибкости, скорости и стабильности.

Dynatrace configuration API помогает отслеживать конфигурации окружений мониторинга Dynatrace. Он предоставляет endpoints, перечисленные в секции **Endpoints** ниже.

## Basics

[Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.")

[Response codes](/managed/dynatrace-api/basics/dynatrace-api-response-codes "Узнайте, какие HTTP-коды ответа используются в Dynatrace API.")

[Access limit](/managed/dynatrace-api/basics/access-limit "Узнайте о лимитах payload и throttling запросов, которые могут влиять на использование Dynatrace API.")

[Preview and Early Access releases](/managed/dynatrace-api/basics/preview-early-access "Как работают Preview и Early Access релизы endpoints Dynatrace API")

[Migration guides](/managed/dynatrace-api/basics/deprecation-migration-guides "Мигрируйте автоматизацию на новые endpoints Dynatrace API.")

## Endpoints

### Anomaly detection

[Applications](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Узнайте, что предлагает Dynatrace Anomaly detection API для приложений.")

[AWS](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Узнайте, что предлагает Dynatrace Anomaly detection API для AWS.")

[Database services](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Узнайте, что предлагает Dynatrace Anomaly detection API для database services.")

[Disk events](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Узнайте, что предлагает Dynatrace Anomaly detection API для disk events.")

[Hosts](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Узнайте, что предлагает Dynatrace Anomaly detection API для хостов.")

[Process groups](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups "Узнайте, что предлагает Dynatrace Anomaly detection API для process groups.")

[Services](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Узнайте, что предлагает Dynatrace Anomaly detection API для services.")

[VMware](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Узнайте, что предлагает Dynatrace Anomaly detection API для VMware.")

### AWS

[AWS credentials](/managed/dynatrace-api/configuration-api/aws-credentials-api "Узнайте, что предлагает Dynatrace AWS credentials config API.")

[AWS PrivateLink](/managed/dynatrace-api/configuration-api/aws-privatelink "Узнайте, что предлагает Dynatrace AWS PrivateLink config API.")

[AWS supported services](/managed/dynatrace-api/configuration-api/aws-supported-services "Получить список поддерживаемых AWS-сервисов через Dynatrace API.")

### Azure

[Azure credentials](/managed/dynatrace-api/configuration-api/azure-credentials-api "Узнайте, что предлагает Dynatrace Azure credentials config API.")

[Azure supported services](/managed/dynatrace-api/configuration-api/azure-supported-services "Получить список поддерживаемых Azure-сервисов через Dynatrace API.")

### Calculated metrics

[Mobile app metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Управление calculated metrics для mobile и custom apps через Dynatrace configuration API.")

[Service metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Управление calculated service metrics через Dynatrace configuration API.")

[Synthetic metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Управление calculated synthetic metrics через Dynatrace configuration API.")

[Web application metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Управление calculated web application metrics через Dynatrace configuration API.")

### Conditional naming

[Conditional naming](/managed/dynatrace-api/configuration-api/conditional-naming "Узнайте, что предлагает Dynatrace configuration API для conditional naming.")

### Data privacy

[Data privacy](/managed/dynatrace-api/configuration-api/data-privacy-api "Узнайте, что предлагает Dynatrace data privacy config API.")

### Dashboards

[Dashboards](/managed/dynatrace-api/configuration-api/dashboards-api "Узнайте, как управлять конфигурацией дашбордов через Dynatrace Classic configuration API.")

### Extensions

[Extensions](/managed/dynatrace-api/configuration-api/extensions-api "Узнайте, что предлагает Dynatrace Extension API.")

[Plugins](/managed/dynatrace-api/configuration-api/plugins-api "Узнайте, как управлять плагинами через Dynatrace configuration API.")

### Mobile

[Mobile and custom app configuration](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace mobile и custom app config API.")

[Mobile symbolication](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление mobile symbol files через Dynatrace API.")

### OneAgent

[OneAgent on a host](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Управление конфигурацией OneAgent-инстансов на ваших хостах через Dynatrace API.")

[OneAgent in a host group](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Управление конфигурацией OneAgent-инстансов в host groups через Dynatrace API.")

[Environment-wide configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Управление environment-wide конфигурацией OneAgent через Dynatrace API.")

### Remote environments

[Remote environments](/managed/dynatrace-api/configuration-api/remote-environments "Управление конфигурациями remote Dynatrace-окружений через Dynatrace configuration API.")

### Reports

[Reports](/managed/dynatrace-api/configuration-api/reports-api "Управление отчётами через Dynatrace configuration API.")

### RUM

[Allowed beacon origins for CORS](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors "Узнайте, что предлагает Dynatrace configuration API для разрешённых beacon origins для Cross Origin Resource Sharing.")

[Applications detection configuration](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration "Узнайте, что предлагает Dynatrace application detection API.")

[Calculated web application metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Управление calculated web application metrics через Dynatrace configuration API.")

[Content resources](/managed/dynatrace-api/configuration-api/rum/content-resources "Узнайте, что предлагает Dynatrace configuration API для content resources.")

[Geographic regions - IP address mapping rules](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнайте, что предлагает Dynatrace configuration API для IP address mapping rules.")

[Geographic regions - IP mapping headers](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header "Узнайте, что предлагает Dynatrace configuration API для IP mapping headers.")

[Mobile and custom app configuration](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace mobile и custom app config API.")

[Web application configuration](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Узнайте, что предлагает Dynatrace web application config API.")

### Services

[Calculated service metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Управление calculated service metrics через Dynatrace configuration API.")

[Custom services](/managed/dynatrace-api/configuration-api/service-api/custom-services-api "Узнайте, что предлагает Dynatrace custom services config API.")

[Failure detection](/managed/dynatrace-api/configuration-api/service-api/failure-detection "Узнайте, что предлагает Dynatrace failure detection config API.")

[Request attributes](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Узнайте, что предлагает Dynatrace request attribute config API.")

[Request naming](/managed/dynatrace-api/configuration-api/service-api/request-naming-api "Узнайте, что предлагает Dynatrace request naming config API.")

[Service detection rules](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Узнайте, что предлагает Dynatrace service detection rules config API.")

## API Explorer

Доступ ко всем endpoints Dynatrace API можно получить через API Explorer. Из [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по платформе Dynatrace Managed") прокрутите вниз до **Dynatrace API** и выберите интересующую секцию API.

Альтернативно можно получить доступ к API Explorer по прямой ссылке `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Authentication в API Explorer

Выберите иконку замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любым endpoint, чтобы увидеть информацию о токенах OAuth 2.0, защищающих этот endpoint. Каждому endpoint нужен конкретный тип токена.

Также можно разблокировать все endpoints, выбрав **Authorize**. В появившемся диалоге будет видно, какие разрешения токена нужны для каждого API-endpoint. Введя свой OAuth 2.0 токен в глобальный диалог **Available authorizations**, вы сможете разблокировать все связанные API-endpoints.

### Попробовать API-вызов

Введя свой OAuth 2.0 токен, можно напрямую выполнять API-вызовы в API explorer. Просто выберите **Try it out**, чтобы открыть секцию параметров выбранного API-endpoint, где можно ввести дополнительные параметры и изменить payload запроса перед выполнением через **Execute**.