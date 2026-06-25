---
title: Environment API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api
scraped: 2026-05-12T11:03:54.479919
---

# Environment API

# Environment API

* Reference
* Published Apr 01, 2019

## Basics

[Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.")

[Response codes](/managed/dynatrace-api/basics/dynatrace-api-response-codes "Узнайте, какие HTTP-коды ответа используются в Dynatrace API.")

[Access limit](/managed/dynatrace-api/basics/access-limit "Узнайте о лимитах payload и throttling запросов, которые могут влиять на использование Dynatrace API.")

[Preview and Early Access releases](/managed/dynatrace-api/basics/preview-early-access "Как работают Preview и Early Access релизы endpoints Dynatrace API")

[Migration guides](/managed/dynatrace-api/basics/deprecation-migration-guides "Мигрируйте автоматизацию на новые endpoints Dynatrace API.")

## Endpoints

### ActiveGate

[Information](/managed/dynatrace-api/environment-api/activegates/activegate-info "Список всех ActiveGates, подключённых к окружению сейчас или недавно, через Dynatrace API.")

[Auto-update configuration](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Управление конфигурацией auto-update ваших Environment ActiveGates через Dynatrace API.")

[Auto-update jobs](/managed/dynatrace-api/environment-api/activegates/auto-update-jobs "Управление auto-update jobs ваших ActiveGates через Dynatrace API.")

### Anonymization

[Anonymization](/managed/dynatrace-api/environment-api/anonymization "Узнайте, как выполнить требования GDPR с помощью Dynatrace API для удаления данных пользователей.")

### Application Security

[Vulnerabilities](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей.")

[Davis Security Advisor](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")
[Attacks](/managed/dynatrace-api/environment-api/application-security/attacks "Узнайте, что предлагает Dynatrace Attacks API.")

### Audit logs

[Audit logs](/managed/dynatrace-api/environment-api/audit-logs "Чтение audit logs Dynatrace через Dynatrace API.")

### Cluster information

[Cluster information](/managed/dynatrace-api/environment-api/cluster-information "Узнайте, как проверить версию и время кластера через Dynatrace API.")

### Credential vault

[Credential vault](/managed/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для credentials.")

### Custom tags

[Custom tags of monitored entities](/managed/dynatrace-api/environment-api/custom-tags "Управление custom tags мониторящихся сущностей через Dynatrace API.")

### Deployment

[OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent "Скачивание установщиков OneAgent через Dynatrace API.")

[ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate "Скачивание установщиков ActiveGate через Dynatrace API.")

[BOSH tarballs](/managed/dynatrace-api/environment-api/deployment/bosh "Скачивание установщиков OneAgent как BOSH tarballs через Dynatrace API.")

[Orchestration tarballs](/managed/dynatrace-api/environment-api/deployment/orchestration "Скачивание установщиков OneAgent как orchestration tarballs через Dynatrace API.")

### Events

[List events](/managed/dynatrace-api/environment-api/events-v2/get-events "Список events окружения мониторинга через Dynatrace API.")

[List event types](/managed/dynatrace-api/environment-api/events-v2/get-event-types "Список типов events через Dynatrace API.")

[List event properties](/managed/dynatrace-api/environment-api/events-v2/get-event-properties "Список всех свойств events через Dynatrace API.")

[Ingest events](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingest event через Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями через Dynatrace Extensions 2.0 API.")

### Hub capabilities

[Hub capabilities](/managed/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через Hub items API.")

### Log Monitoring

[Log Monitoring](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно делать с Log Monitoring API v2.")

### Metrics

#### Version 1

[Basics](/managed/dynatrace-api/environment-api/metric-v1 "Получение информации о метриках через Timeseries v1 API.")

#### Version 2

[List metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "Список всех метрик, доступных в окружении мониторинга, через Metrics v2 API.")

[Get data points](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Чтение data points одной или нескольких метрик через Metrics v2 API.")

[Ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics в Dynatrace через Metrics v2 API.")

[Metric selector](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка metric selector для Metric v2 API.")

[Metric expressions](/managed/dynatrace-api/environment-api/metric-v2/metric-expressions "Используйте metric expressions для применения арифметических операций в запросе data points через Metrics API v2.")

### Metric units

[List units](/managed/dynatrace-api/environment-api/metrics-units/get-all-units "Список всех метрик, доступных для окружения мониторинга, через Dynatrace API.")

[View a unit](/managed/dynatrace-api/environment-api/metrics-units/get-unit "Просмотр метаданных metric unit через Dynatrace API.")

[Convert units](/managed/dynatrace-api/environment-api/metrics-units/get-unit-convert "Конвертация значения метрики из одной единицы в другую через Dynatrace API.")

### Monitored entities

[Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.")

### Network zones

[Network zones](/managed/dynatrace-api/environment-api/network-zones "Управление network zones через Dynatrace API.")

### OneAgent on a host

[OneAgent on a host](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации OneAgent-инстансов на хостах через Dynatrace API.")

### Problems

[Problems v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Problems v2 API.")

### Releases

[Releases](/managed/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Releases API.")

### Remote configuration

[OneAgent](/managed/dynatrace-api/environment-api/remote-configuration/oneagent "Удалённое управление конфигурацией OneAgents в масштабе через Dynatrace API.")

[ActiveGate](/managed/dynatrace-api/environment-api/remote-configuration/activegate "Удалённое управление конфигурацией ActiveGates в масштабе через Dynatrace API.")

### RUM

[Geographic regions](/managed/dynatrace-api/environment-api/rum/geographic-regions "Просмотр запросов, доступных через Dynatrace Geographic regions API.")

[User sessions](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает Dynatrace User Sessions Query language API.")

[Real User Monitoring JavaScript](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как использовать Dynatrace API для настройки и поддержки manually injected приложений через Real User Monitoring JavaScript API.")

### Settings

[Settings](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.")

### SLO

[Service-Level Objectives Classic](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Узнайте, что предлагает Dynatrace SLO API classic.")

### Synthetic

[Monitors](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управление synthetic monitors через Synthetic v1 API.")

[Monitor executions v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "Просмотр результатов выполнения Synthetic monitor через Synthetic v2 API.")

[Locations v1](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations "Управление synthetic locations через Synthetic v1 API.")

[Locations v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление synthetic locations через Synthetic v2 API.")

[Nodes v1](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes "Получение информации о synthetic nodes через Synthetic v1 API.")

[Nodes v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление synthetic nodes через Synthetic v2 API.")

[Third-party synthetic](/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic "Push third-party synthetic-данных в Dynatrace через API.")

### Tokens

[Tokens v2](/managed/dynatrace-api/environment-api/tokens-v2 "Управление access tokens Dynatrace через Dynatrace API.")

## API Explorer

Доступ ко всем endpoints Dynatrace API можно получить через API Explorer. Из [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по платформе Dynatrace Managed") прокрутите вниз до **Dynatrace API** и выберите интересующую секцию API.

Альтернативно можно получить доступ к API Explorer по прямой ссылке `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Authentication в API Explorer

Выберите иконку замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любым endpoint, чтобы увидеть информацию о токенах OAuth 2.0, защищающих этот endpoint. Каждому endpoint нужен конкретный тип токена.

Также можно разблокировать все endpoints, выбрав **Authorize**. В появившемся диалоге будет видно, какие разрешения токена нужны для каждого API-endpoint. Введя свой OAuth 2.0 токен в глобальный диалог **Available authorizations**, вы сможете разблокировать все связанные API-endpoints.

### Попробовать API-вызов

Введя свой OAuth 2.0 токен, можно напрямую выполнять API-вызовы в API explorer. Просто выберите **Try it out**, чтобы открыть секцию параметров выбранного API-endpoint, где можно ввести дополнительные параметры и изменить payload запроса перед выполнением через **Execute**.