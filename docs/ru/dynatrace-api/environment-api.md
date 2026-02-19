---
title: Environment API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api
scraped: 2026-02-19T21:16:10.845306
---

# Environment API

# Environment API

* Справка
* Опубликовано 01 апр. 2019 г.

## Основы

[Аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как аутентифицироваться для использования Dynatrace API.")

[Коды ответов](/docs/dynatrace-api/basics/dynatrace-api-response-codes "Узнайте, какие коды ответов HTTP используются в Dynatrace API.")

[Ограничение доступа](/docs/dynatrace-api/basics/access-limit "Узнайте о ограничениях полезной нагрузки и ограничении запросов, которые могут повлиять на ваше использование Dynatrace API.")

[Предварительные и ранние выпуски](/docs/dynatrace-api/basics/preview-early-access "Как работают предварительные и ранние выпуски конечных точек Dynatrace API")

[Руководства по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides "Перенесите свою автоматизацию на более новые конечные точки Dynatrace API.")

[Grail APIs](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Конечные точки

### ActiveGate

[Информация](/docs/dynatrace-api/environment-api/activegates/activegate-info "Список всех ActiveGate, в настоящее время или недавно подключенных к среде через Dynatrace API.")

[Конфигурация автоматического обновления](/docs/dynatrace-api/environment-api/activegates/auto-update-config "Управление конфигурацией автоматического обновления ваших Environment ActiveGate через Dynatrace API.")

[Задания автоматического обновления](/docs/dynatrace-api/environment-api/activegates/auto-update-jobs "Управление заданиями автоматического обновления ваших ActiveGate через Dynatrace API.")

### Анонимизация

[Анонимизация](/docs/dynatrace-api/environment-api/anonymization "Узнайте, как выполнить требования GDPR, используя Dynatrace API для удаления данных пользователей.")

### Безопасность приложений

[Уязвимости](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей.")

[Советник по безопасности Davis](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Совета по безопасности Davis через Dynatrace API.")
[Атаки](/docs/dynatrace-api/environment-api/application-security/attacks "Узнайте, что предлагает Dynatrace Атаки API.")

### Журналы аудита

[Журналы аудита](/docs/dynatrace-api/environment-api/audit-logs "Чтение журналов аудита Dynatrace через Dynatrace API.")

![Бизнес-наблюдаемость](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Бизнес-наблюдаемость")

### Бизнес-события

[Бизнес-события](/docs/dynatrace-api/environment-api/business-analytics-v2 "Узнайте, как можно ингестировать бизнес-событие с помощью Dynatrace Бизнес-событий API v2.")

### Информация о кластере

[Информация о кластере](/docs/dynatrace-api/environment-api/cluster-information "Узнайте, как проверить версию кластера и время с помощью Dynatrace API.")

### Хранилище учетных данных

[Хранилище учетных данных](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для учетных данных.")

### Пользовательские теги

[Пользовательские теги контролируемых сущностей](/docs/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами контролируемых сущностей через Dynatrace API.")

### Развертывание

[OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent "Скачайте установщики OneAgent через Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate "Скачайте установщики ActiveGate через Dynatrace API.")

[Архивы BOSH](/docs/dynatrace-api/environment-api/deployment/bosh "Скачайте установщики OneAgent в виде архивов BOSH через Dynatrace API.")

[Архивы оркестровки](/docs/dynatrace-api/environment-api/deployment/orchestration "Скачайте установщики OneAgent в виде архивов оркестровки через Dynatrace API.")

### События

[Список событий](/docs/dynatrace-api/environment-api/events-v2/get-events "Список событий вашей среды мониторинга через Dynatrace API.")

[Список типов событий](/docs/dynatrace-api/environment-api/events-v2/get-event-types "Список типов событий через Dynatrace API.")

[Список свойств событий](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "Список всех свойств событий через Dynatrace API.")

[Ингестирование событий](/docs/dynatrace-api/environment-api/events-v2/post-event "Ингестирование события через Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API.")

### Возможности Hub

[Возможности Hub](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.")

### Мониторинг журналов

[Мониторинг журналов](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно сделать с помощью конечной точки Мониторинга журналов API v2.")

### Метрики

#### Версия 1

[Основы](/docs/dynatrace-api/environment-api/metric-v1 "Получение информации о метриках через конечную точку Timeseries v1 API.")

#### Версия 2

[Список метрик](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "Список всех метрик, доступных в вашей среде мониторинга, через Метрики v2 API.")

[Получение точек данных](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Чтение точек данных одной или нескольких метрик через Метрики v2 API.")

[Ингестирование точек данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ингестирование пользовательских метрик в Dynatrace через Метрики v2 API.")

[Селектор метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для конечной точки Метрик v2 API.")

[Выражения метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Использование выражений метрик для применения арифметических операций в запросе точек данных через конечную точку Метрик API v2.")

### Единицы измерения метрик

[Список единиц](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "Список всех метрик, доступных для вашей среды мониторинга, через Dynatrace API.")

[Просмотр единицы](/docs/dynatrace-api/environment-api/metrics-units/get-unit "Просмотр метаданных единицы измерения через Dynatrace API.")

[Преобразование единиц](/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert "Преобразование значения метрики из одной единицы в другую через Dynatrace API.")

### Контролируемые сущности

[Контролируемые сущности](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о конечной точке Контролируемых сущностей Dynatrace API.")

### Сети зон

[Сети зон](/docs/dynatrace-api/environment-api/network-zones "Управление сетями зон через Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на ваших хостах через Dynatrace API.")

### Проблемы

[Проблемы v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает конечная точка Проблем Dynatrace v2 API.")

### Релизы

[Релизы](/docs/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает конечная точка Релизов Dynatrace API.")

### Удаленная конфигурация

[OneAgent](/docs/dynatrace-api/environment-api/remote-configuration/oneagent "Управление конфигурацией OneAgent удаленно в масштабе с помощью Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/remote-configuration/activegate "Управление конфигурацией ActiveGate удаленно в масштабе с помощью Dynatrace API.")

### RUM

[Географические регионы](/docs/dynatrace-api/environment-api/rum/geographic-regions "Просмотр запросов, доступных через конечную точку Географических регионов Dynatrace API.")

[Сессии пользователей](/docs/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает язык запросов Сессий пользователей Dynatrace API.")

[Real User Monitoring JavaScript](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как можно использовать Dynatrace API, чтобы настроить и поддерживать ваши вручную инъектированные приложения с помощью Real User Monitoring JavaScript API.")

### Настройки

[Настройки](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает конечная точка Настроек Dynatrace API.")

### SLO

[Цели обслуживания](/docs/dynatrace-api/environment-api/service-level-objectives "Откройте для себя функциональность конечной точки Целей обслуживания, основанную на Grail.")

### Синтетический

[Мониторы](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управление синтетическими мониторами через конечную точку Синтетического v1 API.")

[Выполнение мониторов v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "Просмотр результатов выполнения Синтетических мониторов через конечную точку Синтетического v2 API.")

[Местоположения v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations "Управление синтетическими местоположениями через конечную точку Синтетического v1 API.")

[Местоположения v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими местоположениями через конечную точку Синтетического v2 API.")

[Узлы v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-nodes "Получение информации о синтетических узлах через конечную точку Синтетического v1 API.")

[Узлы v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через конечную точку Синтетического v2 API.")

[Синтетический третьих сторон](/docs/dynatrace-api/environment-api/synthetic/third-party-synthetic "Передача синтетических данных третьих сторон в Dynatrace через API.")

### Токены

[Токены v2](/docs/dynatrace-api/environment-api/tokens-v2 "Управление токенами доступа Dynatrace через Dynatrace API.")

## Исследователь API

Вы можете получить доступ ко всем конечным точкам Dynatrace API, используя Исследователь API.

* Последний Dynatrace. Перейдите в **Токены доступа**, затем выберите ссылку **Исследователь Dynatrace API**.
* Предыдущий Dynatrace. Из [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Перейдите в последний Dynatrace"), прокрутите вниз до **Dynatrace API** и выберите раздел Исследователя API, который вас интересует.

Альтернативно, вы можете получить доступ к Исследователю API через прямую ссылку `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в Исследователе API

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой API конечной точки. Вводя ваш OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные API конечные точки.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнять API-вызовы внутри API-обозревателя. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной API-конечной точки, где вы можете ввести дополнительные параметры и изменить полезную нагрузку запроса перед выполнением его, выбрав **Выполнить**.