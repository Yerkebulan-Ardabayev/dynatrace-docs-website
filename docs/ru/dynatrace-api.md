---
title: Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api
scraped: 2026-03-06T21:16:34.990823
---

# Dynatrace API

* Ссылка
* Обновлено 26 февраля 2026 г.

Используйте Dynatrace API, чтобы автоматизировать задачи мониторинга и экспортировать различные типы данных в инструменты отчетности и анализа третьих лиц. Общение API обеспечивает безопасность с помощью защищенного общения через протокол HTTPS.

## Основы

[Аутентификация](dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как получить аутентификацию для использования Dynatrace API.")

[Коды ответов](dynatrace-api/basics/dynatrace-api-response-codes.md "Узнайте, какие коды ответов HTTP используются в Dynatrace API.")

[Ограничение доступа](dynatrace-api/basics/access-limit.md "Узнайте о пределах полезной нагрузки и ограничении запросов, которые могут повлиять на использование Dynatrace API.")

[Предварительные и ранние выпуски](dynatrace-api/basics/preview-early-access.md "Как работают предварительные и ранние выпуски конечных точек Dynatrace API")

[Руководства по миграции](dynatrace-api/basics/deprecation-migration-guides.md "Перенесите свою автоматизацию на более новые конечные точки Dynatrace API.")

[Grail APIs](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Конечные точки

Environment

Конфигурация

Управление учетными записями

### ActiveGate

[Информация](dynatrace-api/environment-api/activegates/activegate-info.md "Список всех ActiveGate, в настоящее время или недавно подключенных к среде через Dynatrace API.")

[Конфигурация автообновления](dynatrace-api/environment-api/activegates/auto-update-config.md "Управление конфигурацией автообновления ваших Environment ActiveGate через Dynatrace API.")

[Задания автообновления](dynatrace-api/environment-api/activegates/auto-update-jobs.md "Управление заданиями автообновления ваших ActiveGate через Dynatrace API.")

### Анонимизация

[Анонимизация](dynatrace-api/environment-api/anonymization.md "Узнайте, как выполнить требования GDPR, используя Dynatrace API, чтобы удалить пользовательские данные.")

### Безопасность приложений

[Уязвимости](dynatrace-api/environment-api/application-security/vulnerabilities.md "Узнайте, что предлагает API уязвимостей.")

[Советы по безопасности Davis](dynatrace-api/environment-api/application-security/davis-security-advice.md "Просмотрите рекомендации Совета по безопасности Davis через Dynatrace API.")
[Атаки](dynatrace-api/environment-api/application-security/attacks.md "Узнайте, что предлагает Dynatrace Атаки API.")

### Журналы аудита

[Журналы аудита](dynatrace-api/environment-api/audit-logs.md "Чтение журналов аудита Dynatrace через Dynatrace API.")

![Бизнес-наблюдаемость](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Бизнес-наблюдаемость")

### Бизнес-события

[Бизнес-события](dynatrace-api/environment-api/business-analytics-v2.md "Узнайте, как можно ингестировать бизнес-событие с помощью Dynatrace Бизнес-событий API v2.")

### Информация о кластере

[Информация о кластере](dynatrace-api/environment-api/cluster-information.md "Узнайте, как проверить версию кластера и время с помощью Dynatrace API.")

### Хранилище учетных данных

[Хранилище учетных данных](dynatrace-api/environment-api/credential-vault.md "Узнайте, что предлагает Dynatrace API для учетных данных.")

### Пользовательские теги

[Пользовательские теги контролируемых сущностей](dynatrace-api/environment-api/custom-tags.md "Управление пользовательскими тегами контролируемых сущностей через Dynatrace API.")

### Развертывание

[OneAgent](dynatrace-api/environment-api/deployment/oneagent.md "Скачайте установщики OneAgent через Dynatrace API.")

[ActiveGate](dynatrace-api/environment-api/deployment/activegate.md "Скачайте установщики ActiveGate через Dynatrace API.")

[Архивы BOSH](dynatrace-api/environment-api/deployment/bosh.md "Скачайте установщики OneAgent в виде архивов BOSH через Dynatrace API.")

[Архивы оркестровки](dynatrace-api/environment-api/deployment/orchestration.md "Скачайте установщики OneAgent в виде архивов оркестровки через Dynatrace API.")

### События

[Список событий](dynatrace-api/environment-api/events-v2/get-events.md "Список событий вашей среды мониторинга через Dynatrace API.")

[Список типов событий](dynatrace-api/environment-api/events-v2/get-event-types.md "Список типов событий через Dynatrace API.")

[Список свойств событий](dynatrace-api/environment-api/events-v2/get-event-properties.md "Список всех свойств событий через Dynatrace API.")

[Ингестирование событий](dynatrace-api/environment-api/events-v2/post-event.md "Ингестирование события через Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](dynatrace-api/environment-api/extensions-20.md "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API.")

### Возможности Hub

[Возможности Hub](dynatrace-api/environment-api/hub.md "Узнайте, как получить доступ к функциям Dynatrace Hub через элементы Hub API.")

### Мониторинг журналов

[Мониторинг журналов](dynatrace-api/environment-api/log-monitoring-v2.md "Узнайте, что можно сделать с помощью API Мониторинга журналов v2.")

### Метрики

#### Версия 1

[Основы](dynatrace-api/environment-api/metric-v1.md "Получение информации о метриках через API Timeseries v1.")

#### Версия 2

[Список метрик](dynatrace-api/environment-api/metric-v2/get-all-metrics.md "Список всех метрик, доступных в вашей среде мониторинга, через API Метрик v2.")

[Получение точек данных](dynatrace-api/environment-api/metric-v2/get-data-points.md "Чтение точек данных одной или нескольких метрик через API Метрик v2.")

[Ингестирование точек данных](dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Ингестирование пользовательских метрик в Dynatrace через API Метрик v2.")

[Выбор метрик](dynatrace-api/environment-api/metric-v2/metric-selector.md "Настройка селектора метрик для API Метрик v2.")

[Выражения метрик](dynatrace-api/environment-api/metric-v2/metric-expressions.md "Использование выражений метрик для применения арифметических операций в запросе точек данных через API Метрик.")

### Единицы измерения метрик

[Список единиц](dynatrace-api/environment-api/metrics-units/get-all-units.md "Список всех метрик, доступных для вашей среды мониторинга, через Dynatrace API.")

[Просмотр единицы](dynatrace-api/environment-api/metrics-units/get-unit.md "Просмотр метаданных единицы измерения через Dynatrace API.")

[Преобразование единиц](dynatrace-api/environment-api/metrics-units/get-unit-convert.md "Преобразование значения метрики из одной единицы в другую через Dynatrace API.")

### Контролируемые сущности

[Контролируемые сущности](dynatrace-api/environment-api/entity-v2.md "Узнайте о Dynatrace Контролируемых сущностях API.")

### Сети зон

[Сети зон](dynatrace-api/environment-api/network-zones.md "Управление сетями зон через Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md "Проверка конфигурации экземпляров OneAgent на ваших хостах через Dynatrace API.")

### Проблемы

[Проблемы v2](dynatrace-api/environment-api/problems-v2.md "Узнайте, что предлагает Dynatrace Проблемы v2 API.")

### Выпуски

[Выпуски](dynatrace-api/environment-api/releaseapi.md "Узнайте, что предлагает Dynatrace Выпуски API.")

### Удаленная конфигурация

[OneAgent](dynatrace-api/environment-api/remote-configuration/oneagent.md "Управление конфигурацией OneAgent удаленно в масштабе с помощью Dynatrace API.")

[ActiveGate](dynatrace-api/environment-api/remote-configuration/activegate.md "Управление конфигурацией ActiveGate удаленно в масштабе с помощью Dynatrace API.")

### RUM

[Географические регионы](dynatrace-api/environment-api/rum/geographic-regions.md "Просмотр запросов, доступных через Dynatrace Географические регионы API.")

[Сессии пользователей](dynatrace-api/environment-api/rum/user-sessions.md "Узнайте, что предлагает Dynatrace Сессии пользователей Query язык API.")

[Real User Monitoring JavaScript](dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code.md "Узнайте, как использовать Dynatrace API, чтобы настроить и поддерживать ваши вручную инъецированные приложения с помощью Real User Monitoring JavaScript API.")

### Настройки

[Настройки](dynatrace-api/environment-api/settings.md "Узнайте, что предлагает Dynatrace Настройки API.")

### SLO

[Цели обслуживания](dynatrace-api/environment-api/service-level-objectives.md "Откройте для себя функциональность API новых Целей обслуживания, работающих на Grail.")

### Синтетика

[Мониторы](dynatrace-api/environment-api/synthetic/synthetic-monitors.md "Управление синтетическими мониторами через Синтетический API v1.")

[Выполнение мониторов v2](dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution.md "Просмотр результатов выполнения Синтетических мониторов через Синтетический API v2.")

[Места v1](dynatrace-api/environment-api/synthetic/synthetic-locations.md "Управление синтетическими местами через Синтетический API v1.")

[Места v2](dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2.md "Управление синтетическими местами через Синтетический API v2.")

[Узлы v1](dynatrace-api/environment-api/synthetic/synthetic-nodes.md "Получение информации о синтетических узлах через Синтетический API v1.")

[Узлы v2](dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2.md "Управление синтетическими узлами через Синтетический API v2.")

[Синтетический третий](dynatrace-api/environment-api/synthetic/third-party-synthetic.md "Передача синтетических данных третьих лиц в Dynatrace через API.")

### Токены

[Токены v2](dynatrace-api/environment-api/tokens-v2.md "Управление токенами доступа Dynatrace через Dynatrace API.")

### Обнаружение аномалий

[Приложения](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для приложений.")

[AWS](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для AWS.")

[Сервисы баз данных](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для сервисов баз данных.")

[События диска](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для событий диска.")

[Хосты](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для хостов.")

[Группы процессов](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для групп процессов.")

[Сервисы](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для сервисов.")

[VMware](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware.md "Узнайте, что предлагает Dynatrace обнаружение аномалий API для VMware.")

### AWS

[Учетные данные AWS](dynatrace-api/configuration-api/aws-credentials-api.md "Узнайте, что предлагает Dynatrace конфигурация учетных данных AWS API.")

[AWS PrivateLink](dynatrace-api/configuration-api/aws-privatelink.md "Узнайте, что предлагает Dynatrace конфигурация AWS PrivateLink API.")

[Поддерживаемые сервисы AWS](dynatrace-api/configuration-api/aws-supported-services.md "Получите список поддерживаемых сервисов AWS через Dynatrace API.")

### Azure

[Учетные данные Azure](dynatrace-api/configuration-api/azure-credentials-api.md "Узнайте, что предлагает Dynatrace конфигурация учетных данных Azure API.")

[Поддерживаемые сервисы Azure](dynatrace-api/configuration-api/azure-supported-services.md "Получите список поддерживаемых сервисов Azure через Dynatrace API.")

### Расчетные метрики

[Метрики мобильных приложений](dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics.md "Управляйте расчетными метриками для мобильных и пользовательских приложений через Dynatrace конфигурацию API.")

[Метрики сервисов](dynatrace-api/configuration-api/calculated-metrics/service-metrics.md "Управляйте расчетными метриками сервисов через Dynatrace конфигурацию API.")

[Синтетические метрики](dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics.md "Управляйте расчетными синтетическими метриками через Dynatrace конфигурацию API.")

[Метрики веб-приложений](dynatrace-api/configuration-api/calculated-metrics/rum-metrics.md "Управляйте расчетными метриками веб-приложений через Dynatrace конфигурацию API.")

### Условное именование

[Условное именование](dynatrace-api/configuration-api/conditional-naming.md "Узнайте, что предлагает Dynatrace конфигурация API для условного именования.")

### Защита данных

[Защита данных](dynatrace-api/configuration-api/data-privacy-api.md "Узнайте, что предлагает Dynatrace конфигурация защиты данных API.")

### Панели управления

[Панели управления](dynatrace-api/configuration-api/dashboards-api.md "Узнайте, как управлять конфигурацией панели управления через Dynatrace классическую конфигурацию API.")

### Extensions

[Extensions](dynatrace-api/configuration-api/extensions-api.md "Узнайте, что предлагает Dynatrace расширение API.")

[Плагины](dynatrace-api/configuration-api/plugins-api.md "Узнайте, как управлять плагинами через Dynatrace конфигурацию API.")

### Мобильные устройства

[Конфигурация мобильных и пользовательских приложений](dynatrace-api/configuration-api/rum/mobile-custom-app-configuration.md "Узнайте, что предлагает Dynatrace конфигурация мобильных и пользовательских приложений API.")

[Символикация мобильных приложений](dynatrace-api/configuration-api/mobile-symbolication-api.md "Управляйте файлами символов мобильных приложений через Dynatrace API.")

### OneAgent

[OneAgent на хосте](dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host.md "Управляйте конфигурацией экземпляров OneAgent на ваших хостах через Dynatrace API.")

[OneAgent в группе хостов](dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group.md "Управляйте конфигурацией экземпляров OneAgent в ваших группах хостов через Dynatrace API.")

[Конфигурация Environment](dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide.md "Управляйте конфигурацией OneAgent на уровне среды через Dynatrace API.")

### Удаленные среды

[Удаленные среды](dynatrace-api/configuration-api/remote-environments.md "Управляйте конфигурациями удаленных сред Dynatrace через Dynatrace конфигурацию API.")

### Отчеты

[Отчеты](dynatrace-api/configuration-api/reports-api.md "Управляйте отчетами через Dynatrace конфигурацию API.")

### RUM

[Разрешенные источники маяков для CORS](dynatrace-api/configuration-api/rum/allowed-beacon-cors.md "Узнайте, что предлагает Dynatrace конфигурация API для разрешенных источников маяков для Cross Origin Resource Sharing.")

[Конфигурация обнаружения приложений](dynatrace-api/configuration-api/rum/application-detection-configuration.md "Узнайте, что предлагает Dynatrace конфигурация обнаружения приложений API.")

[Расчетные метрики веб-приложений](dynatrace-api/configuration-api/calculated-metrics/rum-metrics.md "Управляйте расчетными метриками веб-приложений через Dynatrace конфигурацию API.")

[Ресурсы контента](dynatrace-api/configuration-api/rum/content-resources.md "Узнайте, что предлагает Dynatrace конфигурация API для ресурсов контента.")

[Географические регионы - правила сопоставления IP-адресов](dynatrace-api/configuration-api/rum/geographic-regions-ip-address.md "Узнайте, что предлагает Dynatrace конфигурация API для правил сопоставления IP-адресов.")

[Географические регионы - заголовки сопоставления IP](dynatrace-api/configuration-api/rum/geographic-regions-ip-header.md "Узнайте, что предлагает Dynatrace конфигурация API для заголовков сопоставления IP.")

[Конфигурация мобильных и пользовательских приложений](dynatrace-api/configuration-api/rum/mobile-custom-app-configuration.md "Узнайте, что предлагает Dynatrace конфигурация мобильных и пользовательских приложений API.")

[Конфигурация веб-приложения](dynatrace-api/configuration-api/rum/web-application-configuration-api.md "Узнайте, что предлагает Dynatrace конфигурация веб-приложения API.")

### Сервисы

[Расчетные метрики сервисов](dynatrace-api/configuration-api/calculated-metrics/service-metrics.md "Управляйте расчетными метриками сервисов через Dynatrace конфигурацию API.")

[Пользовательские сервисы](dynatrace-api/configuration-api/service-api/custom-services-api.md "Узнайте, что предлагает Dynatrace конфигурация пользовательских сервисов API.")

[Обнаружение сбоев](dynatrace-api/configuration-api/service-api/failure-detection.md "Узнайте, что предлагает Dynatrace конфигурация обнаружения сбоев API.")

[Атрибуты запросов](dynatrace-api/configuration-api/service-api/request-attributes-api.md "Узнайте, что предлагает Dynatrace конфигурация атрибутов запросов API.")

[Именование запросов](dynatrace-api/configuration-api/service-api/request-naming-api.md "Узнайте, что предлагает Dynatrace конфигурация именования запросов API.")

[Правила обнаружения сервисов](dynatrace-api/configuration-api/service-api/detection-rules.md "Узнайте, что предлагает Dynatrace конфигурация правил обнаружения сервисов API.")

### Управление пользователями

[Просмотр и управление пользователями Dynatrace в вашем аккаунте.](dynatrace-api/account-management-api/user-management-api.md "Просмотр и управление пользователями в вашем аккаунте Dynatrace через API управления пользователями API.")

### Управление группами

[Просмотр и управление группами пользователей в вашем аккаунте.](dynatrace-api/account-management-api/group-management-api.md "Создание и управление группами пользователей в вашем аккаунте Dynatrace через API управления группами API.")

### Управление разрешениями

[Управление разрешениями пользователей в вашем аккаунте.](dynatrace-api/account-management-api/permission-management-api.md "Управление разрешениями групп пользователей в вашем аккаунте Dynatrace через API управления разрешениями API.")

### Управление политиками

[Управление политиками доступа в вашем аккаунте.](dynatrace-api/account-management-api/policy-management-api/policies.md "Управление политиками доступа в вашем аккаунте Dynatrace через API управления политиками API.")

### Ограничения аккаунта

[Просмотр ограничений аккаунта вашего аккаунта.](dynatrace-api/account-management-api/account-limits-api.md "Просмотр назначенных ограничений аккаунта в вашем аккаунте Dynatrace через Dynatrace API.")

### Управление сервисными пользователями

[Управление сервисными пользователями в вашем аккаунте.](dynatrace-api/account-management-api/service-user-management-api.md "Создание и управление сервисными пользователями в вашем аккаунте Dynatrace через Dynatrace API.")

### Токены платформы

[Управление токенами платформы вашего аккаунта.](dynatrace-api/account-management-api/platform-tokens-api.md "Создание и управление токенами платформы в вашем аккаунте Dynatrace через Dynatrace API.")

### Управление средами

[Просмотр сред мониторинга вашего аккаунта Dynatrace.](dynatrace-api/account-management-api/environment-management-api/environment-management-api.md "Просмотр сред мониторинга вашего аккаунта Dynatrace через управление средами API.")

### Подписка на платформу Dynatrace

[Просмотр вашей подписки на платформу Dynatrace и ее использования.](dynatrace-api/account-management-api/dynatrace-platform-subscription-api.md "Запрос данных о вашей подписке на платформу Dynatrace через API управления аккаунтом API.")

![Уведомления](https://dt-cdn.net/images/account-management-icon-notifications-8f074dc2ad.svg "Уведомления")

### Уведомления

[Список уведомлений для вашего аккаунта.](dynatrace-api/account-management-api/post-notifications.md "Список уведомлений для вашего аккаунта.")

### Справочные данные

[Просмотр справочной информации о вашем аккаунте.](dynatrace-api/account-management-api/reference-data.md "Проверка справочной информации вашего аккаунта через справочные данные API.")

## Исследователь API

Environment

Конфигурация

Управление учетными записями

Вы можете получить доступ ко всем конечным точкам Dynatrace API, используя API Explorer.

* Последняя Dynatrace Перейдите в **Access Tokens**, затем выберите ссылку **Dynatrace API Explorer**.
* Предыдущая Dynatrace Из [меню пользователя](discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Перейти к последней Dynatrace"), прокрутите вниз до **Dynatrace API** и выберите раздел API, который вас интересует.

Альтернативно, вы можете получить доступ к API Explorer через прямую ссылку `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Authorize**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода OAuth 2.0-токена вы можете непосредственно выполнять вызовы API внутри API Explorer. Просто выберите **Try it out**, чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить payload запроса перед выполнением его, выбрав **Execute**.

### Доступ к API Explorer

Вы можете получить доступ ко всем конечным точкам Dynatrace API, используя API Explorer.

**Через интерфейс Dynatrace:**

* **Последняя версия Dynatrace:** Перейдите в **Access Tokens**, затем выберите ссылку **Dynatrace API Explorer**.
* **Предыдущая версия Dynatrace:** Из [меню пользователя](discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Перейти к последней Dynatrace"), прокрутите вниз до **Dynatrace API** и выберите раздел API, который вас интересует.

**Через управление учетными записями:**

1. Перейдите в [**Управление учетными записями**](https://myaccount.dynatrace.com/). Если у вас несколько учетных записей, выберите учетную запись, которую вы хотите управлять.
2. В верхней навигационной панели перейдите в **Управление идентификаторами и доступом** > **Клиенты OAuth**.
3. В правом верхнем углу страницы выберите **Управление учетными записями API**.

Альтернативно, вы можете получить доступ к API Explorer через прямую ссылку `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Authorize**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Available authorizations**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода OAuth 2.0-токена вы можете непосредственно выполнять вызовы API внутри API Explorer. Просто выберите **Try it out**, чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить payload запроса перед выполнением его, выбрав **Execute**.