---
title: Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api
scraped: 2026-02-19T21:18:06.841732
---

# Dynatrace API

# Dynatrace API

* Ссылка
* Опубликовано 19 июля 2017 г.

Используйте Dynatrace API, чтобы автоматизировать задачи мониторинга и экспортировать различные типы данных в инструменты отчетности и анализа третьих сторон. API обеспечивает безопасность за счет использования защищенной связи через протокол HTTPS.

## Основы

[Аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как получить аутентификацию для использования Dynatrace API.")

[Коды ответов](/docs/dynatrace-api/basics/dynatrace-api-response-codes "Узнайте, какие коды ответов HTTP используются в Dynatrace API.")

[Ограничение доступа](/docs/dynatrace-api/basics/access-limit "Узнайте о ограничениях полезной нагрузки и ограничении запросов, которые могут повлиять на использование Dynatrace API.")

[Предварительные и ранние выпуски](/docs/dynatrace-api/basics/preview-early-access "Как работают предварительные и ранние выпуски конечных точек Dynatrace API")

[Руководства по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides "Перенесите свою автоматизацию на более новые конечные точки Dynatrace API.")

[Grail API](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Конечные точки

Environment

Конфигурация

Управление учетными записями

### ActiveGate

[Информация](/docs/dynatrace-api/environment-api/activegates/activegate-info "Список всех ActiveGate, в настоящее время или недавно подключенных к среде через Dynatrace API.")

[Конфигурация автоматического обновления](/docs/dynatrace-api/environment-api/activegates/auto-update-config "Управление конфигурацией автоматического обновления ваших Environment ActiveGate через Dynatrace API.")

[Задания автоматического обновления](/docs/dynatrace-api/environment-api/activegates/auto-update-jobs "Управление заданиями автоматического обновления ваших ActiveGate через Dynatrace API.")

### Анонимизация

[Анонимизация](/docs/dynatrace-api/environment-api/anonymization "Узнайте, как выполнить требования GDPR, используя Dynatrace API, чтобы удалить пользовательские данные.")

### Безопасность приложений

[Уязвимости](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей.")

[Советы по безопасности Davis](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации Совета по безопасности Davis через Dynatrace API.")
[Атаки](/docs/dynatrace-api/environment-api/application-security/attacks "Узнайте, что предлагает Dynatrace Атаки API.")

### Журналы аудита

[Журналы аудита](/docs/dynatrace-api/environment-api/audit-logs "Чтение журналов аудита Dynatrace через Dynatrace API.")

![Бизнес-наблюдаемость](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Бизнес-наблюдаемость")

### Бизнес-события

[Бизнес-события](/docs/dynatrace-api/environment-api/business-analytics-v2 "Узнайте, как можно включить бизнес-событие с помощью Dynatrace Бизнес-событий API v2.")

### Информация о кластере

[Информация о кластере](/docs/dynatrace-api/environment-api/cluster-information "Узнайте, как проверить версию кластера и время с помощью Dynatrace API.")

### Хранилище учетных данных

[Хранилище учетных данных](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для учетных данных.")

### Пользовательские теги

[Пользовательские теги контролируемых сущностей](/docs/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами контролируемых сущностей через Dynatrace API.")

### Развертывание

[OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent "Скачать установщики OneAgent через Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate "Скачать установщики ActiveGate через Dynatrace API.")

[Архивы BOSH](/docs/dynatrace-api/environment-api/deployment/bosh "Скачать установщики OneAgent в виде архивов BOSH через Dynatrace API.")

[Архивы оркестровки](/docs/dynatrace-api/environment-api/deployment/orchestration "Скачать установщики OneAgent в виде архивов оркестровки через Dynatrace API.")

### События

[Список событий](/docs/dynatrace-api/environment-api/events-v2/get-events "Список событий вашей среды мониторинга через Dynatrace API.")

[Список типов событий](/docs/dynatrace-api/environment-api/events-v2/get-event-types "Список типов событий через Dynatrace API.")

[Список свойств событий](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "Список всех свойств событий через Dynatrace API.")

[Включение событий](/docs/dynatrace-api/environment-api/events-v2/post-event "Включение события через Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API.")

### Возможности Hub

[Возможности Hub](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.")

### Мониторинг журналов

[Мониторинг журналов](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно сделать с помощью API Мониторинга журналов v2.")

### Метрики

#### Версия 1

[Основы](/docs/dynatrace-api/environment-api/metric-v1 "Получение информации о метриках через API Timeseries v1.")

#### Версия 2

[Список метрик](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "Список всех метрик, доступных в вашей среде мониторинга, через Метрики v2 API.")

[Получение данных](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Чтение данных одной или нескольких метрик через Метрики v2 API.")

[Включение данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Включение пользовательских метрик в Dynatrace через Метрики v2 API.")

[Выбор метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для API Метрик v2.")

[Выражения метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Использование выражений метрик для применения арифметических операций в запросе данных через API Метрик v2.")

### Единицы измерения метрик

[Список единиц](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "Список всех метрик, доступных для вашей среды мониторинга, через Dynatrace API.")

[Просмотр единицы](/docs/dynatrace-api/environment-api/metrics-units/get-unit "Просмотр метаданных единицы измерения метрики через Dynatrace API.")

[Преобразование единиц](/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert "Преобразование значения метрики из одной единицы в другую через Dynatrace API.")

### Контролируемые сущности

[Контролируемые сущности](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Контролируемых сущностях API.")

### Сети зон

[Сети зон](/docs/dynatrace-api/environment-api/network-zones "Управление сетями зон через Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на ваших хостах через Dynatrace API.")

### Проблемы

[Проблемы v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Проблемы v2 API.")

### Релизы

[Релизы](/docs/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает Dynatrace Релизы API.")

### Удаленная конфигурация

[OneAgent](/docs/dynatrace-api/environment-api/remote-configuration/oneagent "Управление конфигурацией OneAgent удаленно в крупном масштабе с помощью Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/remote-configuration/activegate "Управление конфигурацией ActiveGate удаленно в крупном масштабе с помощью Dynatrace API.")

### RUM

[Географические регионы](/docs/dynatrace-api/environment-api/rum/geographic-regions "Просмотр запросов, доступных через Dynatrace Географические регионы API.")

[Сессии пользователей](/docs/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает Dynatrace Язык запроса сессий пользователей API.")

[Real User Monitoring JavaScript](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как использовать Dynatrace API, чтобы настроить и поддерживать ваши вручную внедренные приложения с помощью Real User Monitoring JavaScript API.")

### Настройки

[Настройки](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.")

### SLO

[Цели обслуживания](/docs/dynatrace-api/environment-api/service-level-objectives "Откройте для себя функциональность API новых Целей обслуживания, работающих на Grail.")

### Синтетика

[Мониторы](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управление синтетическими мониторами через Синтетический API v1.")

[Выполнение мониторов v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "Просмотр результатов выполнения Синтетических мониторов через Синтетический API v2.")

[Местоположения v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations "Управление синтетическими местоположениями через Синтетический API v1.")

[Местоположения v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими местоположениями через Синтетический API v2.")

[Узлы v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-nodes "Получение информации о синтетических узлах через Синтетический API v1.")

[Узлы v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через Синтетический API v2.")

[Синтетический мониторинг третьих сторон](/docs/dynatrace-api/environment-api/synthetic/third-party-synthetic "Передача данных синтетического мониторинга третьих сторон в Dynatrace через API.")

### Токены

[Токены v2](/docs/dynatrace-api/environment-api/tokens-v2 "Управление токенами доступа Dynatrace через Dynatrace API.")

### Обнаружение аномалий

[Приложения](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Узнайте, что предлагает Dynatrace обнаружение аномалий API для приложений.")

[AWS](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Узнайте, что предлагает Dynatrace обнаружение аномалий API для AWS.")

[Службы баз данных](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Узнайте, что предлагает Dynatrace обнаружение аномалий API для служб баз данных.")

[События диска](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Узнайте, что предлагает Dynatrace обнаружение аномалий API для событий диска.")

[Хосты](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Узнайте, что предлагает Dynatrace обнаружение аномалий API для хостов.")

[Группы процессов](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups "Узнайте, что предлагает Dynatrace обнаружение аномалий API для групп процессов.")

[Службы](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Узнайте, что предлагает Dynatrace обнаружение аномалий API для служб.")

[VMware](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Узнайте, что предлагает Dynatrace обнаружение аномалий API для VMware.")

### AWS

[Учетные данные AWS](/docs/dynatrace-api/configuration-api/aws-credentials-api "Узнайте, что предлагает Dynatrace конфигурация учетных данных AWS API.")

[AWS PrivateLink](/docs/dynatrace-api/configuration-api/aws-privatelink "Узнайте, что предлагает Dynatrace конфигурация AWS PrivateLink API.")

[Поддерживаемые службы AWS](/docs/dynatrace-api/configuration-api/aws-supported-services "Получите список поддерживаемых служб AWS через Dynatrace API.")

### Azure

[Учетные данные Azure](/docs/dynatrace-api/configuration-api/azure-credentials-api "Узнайте, что предлагает Dynatrace конфигурация учетных данных Azure API.")

[Поддерживаемые службы Azure](/docs/dynatrace-api/configuration-api/azure-supported-services "Получите список поддерживаемых служб Azure через Dynatrace API.")

### Расчетные метрики

[Метрики мобильных приложений](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Управляйте расчетными метриками для мобильных и пользовательских приложений через Dynatrace конфигурацию API.")

[Метрики служб](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Управляйте расчетными метриками служб через Dynatrace конфигурацию API.")

[Синтетические метрики](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Управляйте расчетными синтетическими метриками через Dynatrace конфигурацию API.")

[Метрики веб-приложений](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Управляйте расчетными метриками веб-приложений через Dynatrace конфигурацию API.")

### Условное именование

[Условное именование](/docs/dynatrace-api/configuration-api/conditional-naming "Узнайте, что предлагает Dynatrace конфигурация API для условного именования.")

### Защита данных

[Защита данных](/docs/dynatrace-api/configuration-api/data-privacy-api "Узнайте, что предлагает Dynatrace конфигурация защиты данных API.")

### Панели управления

[Панели управления](/docs/dynatrace-api/configuration-api/dashboards-api "Узнайте, как управлять конфигурацией панели управления через Dynatrace классическую конфигурацию API.")

### Extensions

[Extensions](/docs/dynatrace-api/configuration-api/extensions-api "Узнайте, что предлагает Dynatrace расширение API.")

[Плагины](/docs/dynatrace-api/configuration-api/plugins-api "Узнайте, как управлять плагинами через Dynatrace конфигурацию API.")

### Мобильные устройства

[Конфигурация мобильных и пользовательских приложений](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace конфигурация мобильных и пользовательских приложений API.")

[Симболикация мобильных приложений](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Управляйте файлами символов мобильных приложений через Dynatrace API.")

### OneAgent

[OneAgent на хосте](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Управляйте конфигурацией экземпляров OneAgent на ваших хостах через Dynatrace API.")

[OneAgent в группе хостов](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Управляйте конфигурацией экземпляров OneAgent в ваших группах хостов через Dynatrace API.")

[Конфигурация Environment](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Управляйте конфигурацией OneAgent на уровне окружения через Dynatrace API.")

### Удаленные среды

[Удаленные среды](/docs/dynatrace-api/configuration-api/remote-environments "Управляйте конфигурациями удаленных сред Dynatrace через Dynatrace конфигурацию API.")

### Отчеты

[Отчеты](/docs/dynatrace-api/configuration-api/reports-api "Управляйте отчетами через Dynatrace конфигурацию API.")

### RUM

[Разрешенные источники сигналов для CORS](/docs/dynatrace-api/configuration-api/rum/allowed-beacon-cors "Узнайте, что предлагает Dynatrace конфигурация API для разрешенных источников сигналов для Cross Origin Resource Sharing.")

[Конфигурация обнаружения приложений](/docs/dynatrace-api/configuration-api/rum/application-detection-configuration "Узнайте, что предлагает Dynatrace конфигурация обнаружения приложений API.")

[Расчетные метрики веб-приложений](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Управляйте расчетными метриками веб-приложений через Dynatrace конфигурацию API.")

[Ресурсы контента](/docs/dynatrace-api/configuration-api/rum/content-resources "Узнайте, что предлагает Dynatrace конфигурация API для ресурсов контента.")

[Географические регионы - правила сопоставления IP-адресов](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнайте, что предлагает Dynatrace конфигурация API для правил сопоставления IP-адресов.")

[Географические регионы - заголовки сопоставления IP](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-header "Узнайте, что предлагает Dynatrace конфигурация API для заголовков сопоставления IP.")

[Конфигурация мобильных и пользовательских приложений](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace конфигурация мобильных и пользовательских приложений API.")

[Конфигурация веб-приложения](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Узнайте, что предлагает Dynatrace конфигурация веб-приложения API.")

### Службы

[Расчетные метрики служб](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Управляйте расчетными метриками служб через Dynatrace конфигурацию API.")

[Пользовательские службы](/docs/dynatrace-api/configuration-api/service-api/custom-services-api "Узнайте, что предлагает Dynatrace конфигурация пользовательских служб API.")

[Обнаружение сбоев](/docs/dynatrace-api/configuration-api/service-api/failure-detection "Узнайте, что предлагает Dynatrace конфигурация обнаружения сбоев API.")

[Атрибуты запросов](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Узнайте, что предлагает Dynatrace конфигурация атрибутов запросов API.")

[Именование запросов](/docs/dynatrace-api/configuration-api/service-api/request-naming-api "Узнайте, что предлагает Dynatrace конфигурация именования запросов API.")

[Правила обнаружения служб](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Узнайте, что предлагает Dynatrace конфигурация правил обнаружения служб API.")

### Управление пользователями

Просмотр и управление пользователями Dynatrace в вашем аккаунте. (/docs/dynatrace-api/account-management-api/user-management-api "Просмотр и управление пользователями в вашем аккаунте Dynatrace через API управления пользователями API.")

### Управление группами

Просмотр и управление группами пользователей в вашем аккаунте. (/docs/dynatrace-api/account-management-api/group-management-api "Создание и управление группами пользователей в вашем аккаунте Dynatrace через API управления группами API.")

### Управление разрешениями

Управление разрешениями пользователей в вашем аккаунте. (/docs/dynatrace-api/account-management-api/permission-management-api "Управление разрешениями групп пользователей в вашем аккаунте Dynatrace через API управления разрешениями API.")

### Управление политиками

Управление политиками доступа в вашем аккаунте. (/docs/dynatrace-api/account-management-api/policy-management-api/policies "Управление политиками доступа в вашем аккаунте Dynatrace через API управления политиками API.")

### Ограничения аккаунта

Просмотр ограничений аккаунта вашего аккаунта. (/docs/dynatrace-api/account-management-api/account-limits-api "Просмотр назначенных ограничений аккаунта в вашем аккаунте Dynatrace через Dynatrace API.")

### Управление сервисными пользователями

Управление сервисными пользователями в вашем аккаунте. (/docs/dynatrace-api/account-management-api/service-user-management-api "Создание и управление сервисными пользователями в вашем аккаунте Dynatrace через Dynatrace API.")

### Платформенные токены

Управление платформенными токенами вашего аккаунта. (/docs/dynatrace-api/account-management-api/platform-tokens-api "Создание и управление платформенными токенами в вашем аккаунте Dynatrace через Dynatrace API.")

### Управление Environment

Просмотр сред мониторинга вашего аккаунта Dynatrace. (/docs/dynatrace-api/account-management-api/environment-management-api/environment-management-api "Просмотр сред мониторинга вашего аккаунта Dynatrace через API управления Environment API.")

### Подписка на платформу Dynatrace

Просмотр вашей подписки на платформу Dynatrace и ее использования. (/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Запрос данных о вашей подписке на платформу Dynatrace через API управления аккаунтом API.")

### Справочные данные

Просмотр справочной информации о вашем аккаунте. (/docs/dynatrace-api/account-management-api/reference-data "Проверка справочной информации аккаунта через API справочных данных API.")

## Обозреватель API

Environment

Конфигурация

Управление учетными записями

Вы можете получить доступ ко всем конечным точкам Dynatrace API, используя API Explorer.

* Последняя Dynatrace Перейдите в **Токены доступа**, а затем выберите ссылку **Dynatrace API Explorer**.
* Предыдущая Dynatrace Из [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Перейти к последней Dynatrace"), прокрутите вниз до **Dynatrace API** и выберите раздел API, который вас интересует.

Альтернативно, вы можете получить доступ к API Explorer по прямой ссылке `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнить вызовы API внутри API Explorer. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить полезную нагрузку запроса перед выполнением его, выбрав **Выполнить**.

Вы можете получить доступ ко всем конечным точкам Dynatrace API, используя API Explorer.

* Последняя Dynatrace Перейдите в **Токены доступа**, а затем выберите ссылку **Dynatrace API Explorer**.
* Предыдущая Dynatrace Из [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Перейти к последней Dynatrace"), прокрутите вниз до **Dynatrace API** и выберите раздел API, который вас интересует.

Альтернативно, вы можете получить доступ к API Explorer по прямой ссылке `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнить вызовы API внутри API Explorer. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить полезную нагрузку запроса перед выполнением его, выбрав **Выполнить**.

Вы можете получить доступ ко всем конечным точкам Dynatrace API, используя API Explorer.

1. Перейдите в [**Управление учетными записями**](https://myaccount.dynatrace.com/). Если у вас есть несколько учетных записей, выберите учетную запись, которую вы хотите управлять.
2. В верхней навигационной панели перейдите в **Управление идентификаторами и доступом** > **Клиенты OAuth**.
3. В правом верхнем углу страницы выберите **Управление учетной записью API**.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнить вызовы API внутри API Explorer. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить полезную нагрузку запроса перед выполнением его, выбрав **Выполнить**.