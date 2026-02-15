---
title: Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api
scraped: 2026-02-15T08:57:43.539821
---

# Dynatrace API

# Dynatrace API

* Справка
* Опубликовано 19 июля 2017 г.

Используйте Dynatrace API, чтобы автоматизировать задачи мониторинга и экспортировать различные типы данных в инструменты отчетности и анализа третьих лиц. Общение через API обеспечивает безопасность с помощью защищенного соединения по протоколу HTTPS.

## Основы

[Аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как получить аутентификацию для использования Dynatrace API.")

[Коды ответов](/docs/dynatrace-api/basics/dynatrace-api-response-codes "Узнайте, какие коды ответов HTTP используются в Dynatrace API.")

[Ограничение доступа](/docs/dynatrace-api/basics/access-limit "Узнайте о ограничениях полезной нагрузки и ограничении запросов, которые могут повлиять на использование Dynatrace API.")

[Предварительные и ранние версии](/docs/dynatrace-api/basics/preview-early-access "Как работают предварительные и ранние версии конечных точек Dynatrace API")

[Руководства по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides "Перенесите свою автоматизацию на более новые конечные точки Dynatrace API.")

[Grail API](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Конечные точки

Окружение

Конфигурация

Управление учетными записями

### ActiveGate

[Информация](/docs/dynatrace-api/environment-api/activegates/activegate-info "Список всех ActiveGate, в настоящее время или недавно подключенных к окружению через Dynatrace API.")

[Конфигурация автоматического обновления](/docs/dynatrace-api/environment-api/activegates/auto-update-config "Управление конфигурацией автоматического обновления ActiveGate окружения через Dynatrace API.")

[Задания автоматического обновления](/docs/dynatrace-api/environment-api/activegates/auto-update-jobs "Управление заданиями автоматического обновления ActiveGate через Dynatrace API.")

### Анонимизация

[Анонимизация](/docs/dynatrace-api/environment-api/anonymization "Узнайте, как выполнить требования GDPR, используя Dynatrace API для удаления данных пользователей.")

### Безопасность приложений

[Уязвимости](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей.")

[Советы по безопасности Davis](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотрите рекомендации по безопасности Davis через Dynatrace API.")
[Атаки](/docs/dynatrace-api/environment-api/application-security/attacks "Узнайте, что предлагает API атак Dynatrace.")

### Журналы аудита

[Журналы аудита](/docs/dynatrace-api/environment-api/audit-logs "Чтение журналов аудита Dynatrace через Dynatrace API.")

![Бизнес-наблюдаемость](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Бизнес-наблюдаемость")

### Бизнес-события

[Бизнес-события](/docs/dynatrace-api/environment-api/business-analytics-v2 "Узнайте, как можно принять бизнес-событие с помощью API бизнес-событий Dynatrace v2.")

### Информация о кластере

[Информация о кластере](/docs/dynatrace-api/environment-api/cluster-information "Узнайте, как проверить версию кластера и время с помощью Dynatrace API.")

### Хранилище учетных данных

[Хранилище учетных данных](/docs/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает API учетных данных Dynatrace.")

### Пользовательские теги

[Пользовательские теги контролируемых сущностей](/docs/dynatrace-api/environment-api/custom-tags "Управление пользовательскими тегами контролируемых сущностей через Dynatrace API.")

### Развертывание

[OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent "Загрузка установщиков OneAgent через Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate "Загрузка установщиков ActiveGate через Dynatrace API.")

[BOSH-тарболы](/docs/dynatrace-api/environment-api/deployment/bosh "Загрузка установщиков OneAgent в виде BOSH-тарболов через Dynatrace API.")

[Тарболы оркестровки](/docs/dynatrace-api/environment-api/deployment/orchestration "Загрузка установщиков OneAgent в виде тарболов оркестровки через Dynatrace API.")

### События

[Список событий](/docs/dynatrace-api/environment-api/events-v2/get-events "Список событий окружения мониторинга через Dynatrace API.")

[Список типов событий](/docs/dynatrace-api/environment-api/events-v2/get-event-types "Список типов событий через Dynatrace API.")

[Список свойств событий](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "Список всех свойств событий через Dynatrace API.")

[Принятие событий](/docs/dynatrace-api/environment-api/events-v2/post-event "Принятие события через Dynatrace API.")

### Расширения 2.0

[Расширения 2.0](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью API расширений Dynatrace 2.0.")

### Возможности Hub

[Возможности Hub](/docs/dynatrace-api/environment-api/hub "Узнайте, как получить доступ к функциям Dynatrace Hub через API элементов Hub.")

### Мониторинг журналов

[Мониторинг журналов](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно сделать с помощью API мониторинга журналов v2.")

### Метрики

#### Версия 1

[Основы](/docs/dynatrace-api/environment-api/metric-v1 "Получение информации о метриках через API Timeseries v1.")

#### Версия 2

[Список метрик](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "Список всех метрик, доступных в окружении мониторинга, через API метрик v2.")

[Получение точек данных](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Чтение точек данных одной или нескольких метрик через API метрик v2.")

[Принятие точек данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Принятие пользовательских метрик в Dynatrace через API метрик v2.")

[Селектор метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для API метрик v2.")

[Выражения метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Использование выражений метрик для применения арифметических операций в запросе точек данных через API метрик v2.")

### Единицы измерения метрик

[Список единиц](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "Список всех метрик, доступных для окружения мониторинга, через Dynatrace API.")

[Просмотр единицы](/docs/dynatrace-api/environment-api/metrics-units/get-unit "Просмотр метаданных единицы измерения через Dynatrace API.")

[Преобразование единиц](/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert "Преобразование значения метрики из одной единицы в другую через Dynatrace API.")

### Контролируемые сущности

[Контролируемые сущности](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о API контролируемых сущностей Dynatrace.")

### Сети зон

[Сети зон](/docs/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API.")

### OneAgent на хосте

[OneAgent на хосте](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на хостах через Dynatrace API.")

### Проблемы

[Проблемы v2](/docs/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает API проблем Dynatrace v2.")

### Релизы

[Релизы](/docs/dynatrace-api/environment-api/releaseapi "Узнайте, что предлагает API релизов Dynatrace.")

### Удаленная конфигурация

[OneAgent](/docs/dynatrace-api/environment-api/remote-configuration/oneagent "Управление конфигурацией OneAgent удаленно в масштабе с помощью Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/remote-configuration/activegate "Управление конфигурацией ActiveGate удаленно в масштабе с помощью Dynatrace API.")

### RUM

[Географические регионы](/docs/dynatrace-api/environment-api/rum/geographic-regions "Просмотр запросов, доступных через API географических регионов Dynatrace.")

[Сессии пользователей](/docs/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает API языка запроса сессий пользователей Dynatrace.")

[JavaScript Real User Monitoring](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как можно использовать Dynatrace API для настройки и поддержки вручную инъектируемых приложений с помощью API JavaScript Real User Monitoring.")

### Настройки

[Настройки](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает API настроек Dynatrace.")

### SLO

[Цели обслуживания](/docs/dynatrace-api/environment-api/service-level-objectives "Откройте для себя возможности API новых целей обслуживания, работающих на Grail.")

### Синтетический

[Мониторы](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управление синтетическими мониторами через API синтетики v1.")

[Выполнение мониторов v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "Просмотр результатов выполнения синтетических мониторов через API синтетики v2.")

[Местоположения v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations "Управление синтетическими местоположениями через API синтетики v1.")

[Местоположения v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление синтетическими местоположениями через API синтетики v2.")

[Узлы v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-nodes "Получение информации о синтетических узлах через API синтетики v1.")

[Узлы v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Управление синтетическими узлами через API синтетики v2.")

[Синтетика третьих лиц](/docs/dynatrace-api/environment-api/synthetic/third-party-synthetic "Передача синтетических данных третьих лиц в Dynatrace через API.")

### Токены

[Токены v2](/docs/dynatrace-api/environment-api/tokens-v2 "Управление токенами доступа Dynatrace через Dynatrace API.")

### Обнаружение аномалий

[Приложения](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Узнайте, что предлагает API обнаружения аномалий Dynatrace для приложений.")

[АWS](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Узнайте, что предлагает API обнаружения аномалий Dynatrace для AWS.")

[Службы баз данных](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Узнайте, что предлагает API обнаружения аномалий Dynatrace для служб баз данных.")

[События диска](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Узнайте, что предлагает API обнаружения аномалий Dynatrace для событий диска.")

[Хосты](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Узнайте, что предлагает API обнаружения аномалий Dynatrace для хостов.")

[Группы процессов](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups "Узнайте, что предлагает API обнаружения аномалий Dynatrace для групп процессов.")

[Службы](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Узнайте, что предлагает API обнаружения аномалий Dynatrace для служб.")

[VMware](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Узнайте, что предлагает API обнаружения аномалий Dynatrace для VMware.")

### АWS

[Учетные данные АWS](/docs/dynatrace-api/configuration-api/aws-credentials-api "Узнайте, что предлагает API конфигурации учетных данных Dynatrace для AWS.")

[АWS PrivateLink](/docs/dynatrace-api/configuration-api/aws-privatelink "Узнайте, что предлагает API конфигурации Dynatrace для AWS PrivateLink.")

[Поддерживаемые службы АWS](/docs/dynatrace-api/configuration-api/aws-supported-services "Получите список поддерживаемых служб AWS через API Dynatrace.")

### Azure

[Учетные данные Azure](/docs/dynatrace-api/configuration-api/azure-credentials-api "Узнайте, что предлагает API конфигурации учетных данных Dynatrace для Azure.")

[Поддерживаемые службы Azure](/docs/dynatrace-api/configuration-api/azure-supported-services "Получите список поддерживаемых служб Azure через API Dynatrace.")

### Расчетные метрики

[Метрики мобильных приложений](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Управляйте расчетными метриками для мобильных и пользовательских приложений через API конфигурации Dynatrace.")

[Метрики служб](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Управляйте расчетными метриками служб через API конфигурации Dynatrace.")

[Синтетические метрики](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Управляйте расчетными синтетическими метриками через API конфигурации Dynatrace.")

[Метрики веб-приложений](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Управляйте расчетными метриками веб-приложений через API конфигурации Dynatrace.")

### Условное именование

[Условное именование](/docs/dynatrace-api/configuration-api/conditional-naming "Узнайте, что предлагает API конфигурации Dynatrace для условного именования.")

### Защита данных

[Защита данных](/docs/dynatrace-api/configuration-api/data-privacy-api "Узнайте, что предлагает API конфигурации защиты данных Dynatrace.")

### Панели мониторинга

[Панели мониторинга](/docs/dynatrace-api/configuration-api/dashboards-api "Узнайте, как управлять конфигурацией панелей мониторинга через классический API конфигурации Dynatrace.")

### Расширения

[Расширения](/docs/dynatrace-api/configuration-api/extensions-api "Узнайте, что предлагает API расширений Dynatrace.")

[Плагины](/docs/dynatrace-api/configuration-api/plugins-api "Узнайте, как управлять плагинами через API конфигурации Dynatrace.")

### Мобильные устройства

[Конфигурация мобильных и пользовательских приложений](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает API конфигурации мобильных и пользовательских приложений Dynatrace.")

[Симболикация мобильных приложений](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Управляйте файлами символов мобильных приложений через API Dynatrace.")

### OneAgent

[OneAgent на хосте](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Управляйте конфигурацией экземпляров OneAgent на ваших хостах через API Dynatrace.")

[OneAgent в группе хостов](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Управляйте конфигурацией экземпляров OneAgent в ваших группах хостов через API Dynatrace.")

[Конфигурация среды](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Управляйте конфигурацией OneAgent на уровне среды через API Dynatrace.")

### Удаленные среды

[Удаленные среды](/docs/dynatrace-api/configuration-api/remote-environments "Управляйте конфигурациями удаленных сред Dynatrace через API конфигурации Dynatrace.")

### Отчеты

[Отчеты](/docs/dynatrace-api/configuration-api/reports-api "Управляйте отчетами через API конфигурации Dynatrace.")

### RUM

[Разрешенные источники сигналов для CORS](/docs/dynatrace-api/configuration-api/rum/allowed-beacon-cors "Узнайте, что предлагает API конфигурации Dynatrace для разрешенных источников сигналов для Cross Origin Resource Sharing.")

[Конфигурация обнаружения приложений](/docs/dynatrace-api/configuration-api/rum/application-detection-configuration "Узнайте, что предлагает API обнаружения приложений Dynatrace.")

[Расчетные метрики веб-приложений](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Управляйте расчетными метриками веб-приложений через API конфигурации Dynatrace.")

[Ресурсы контента](/docs/dynatrace-api/configuration-api/rum/content-resources "Узнайте, что предлагает API конфигурации Dynatrace для ресурсов контента.")

[Географические регионы - правила сопоставления IP-адресов](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнайте, что предлагает API конфигурации Dynatrace для правил сопоставления IP-адресов.")

[Географические регионы - заголовки сопоставления IP](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-header "Узнайте, что предлагает API конфигурации Dynatrace для заголовков сопоставления IP.")

[Конфигурация мобильных и пользовательских приложений](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает API конфигурации мобильных и пользовательских приложений Dynatrace.")

[Конфигурация веб-приложения](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Узнайте, что предлагает API конфигурации веб-приложения Dynatrace.")

### Службы

[Расчетные метрики служб](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Управляйте расчетными метриками служб через API конфигурации Dynatrace.")

[Пользовательские службы](/docs/dynatrace-api/configuration-api/service-api/custom-services-api "Узнайте, что предлагает API конфигурации пользовательских служб Dynatrace.")

[Обнаружение сбоев](/docs/dynatrace-api/configuration-api/service-api/failure-detection "Узнайте, что предлагает API конфигурации обнаружения сбоев Dynatrace.")

[Атрибуты запросов](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Узнайте, что предлагает API конфигурации атрибутов запросов Dynatrace.")

[Именование запросов](/docs/dynatrace-api/configuration-api/service-api/request-naming-api "Узнайте, что предлагает API конфигурации именования запросов Dynatrace.")

[Правила обнаружения служб](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Узнайте, что предлагает API конфигурации правил обнаружения служб Dynatrace.")

### Управление пользователями

Просмотр и управление пользователями Dynatrace в вашем аккаунте. [/docs/dynatrace-api/account-management-api/user-management-api "Просмотр и управление пользователями в вашем аккаунте Dynatrace через API управления пользователями."]

### Управление группами

Просмотр и управление группами пользователей в вашем аккаунте. [/docs/dynatrace-api/account-management-api/group-management-api "Создание и управление группами пользователей в вашем аккаунте Dynatrace через API управления группами."]

### Управление разрешениями

Управление разрешениями пользователей в вашем аккаунте. [/docs/dynatrace-api/account-management-api/permission-management-api "Управление разрешениями групп пользователей в вашем аккаунте Dynatrace через API управления разрешениями."]

### Управление политиками

Управление политиками доступа в вашем аккаунте. [/docs/dynatrace-api/account-management-api/policy-management-api/policies "Управление политиками доступа в вашем аккаунте Dynatrace через API управления политиками."]

### Ограничения аккаунта

Просмотр ограничений аккаунта вашего аккаунта. [/docs/dynatrace-api/account-management-api/account-limits-api "Просмотр назначенных ограничений аккаунта в вашем аккаунте Dynatrace через API Dynatrace."]

### Управление служебными пользователями

Управление служебными пользователями в вашем аккаунте. [/docs/dynatrace-api/account-management-api/service-user-management-api "Создание и управление служебными пользователями в вашем аккаунте Dynatrace через API Dynatrace."]

### Платформенные токены

Управление платформенными токенами вашего аккаунта. [/docs/dynatrace-api/account-management-api/platform-tokens-api "Создание и управление платформенными токенами в вашем аккаунте Dynatrace через API Dynatrace."]

### Управление средой

Просмотр сред мониторинга вашего аккаунта Dynatrace. [/docs/dynatrace-api/account-management-api/environment-management-api/environment-management-api "Просмотр сред мониторинга вашего аккаунта Dynatrace через API управления средой."]

### Подписка на платформу Dynatrace

Просмотр вашей подписки на платформу Dynatrace и ее использования. [/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Запрос данных о вашей подписке на платформу Dynatrace через API управления аккаунтом."]

### Справочные данные

Просмотр справочной информации о вашем аккаунте. [/docs/dynatrace-api/account-management-api/reference-data "Просмотр справочной информации о вашем аккаунте через API справочных данных."]

## Обозреватель API

Среда

Конфигурация

Управление учетными записями

Вы можете получить доступ ко всем конечным точкам API Dynatrace с помощью API Explorer.

* Последняя версия Dynatrace Перейдите в раздел **Токены доступа** и выберите ссылку **API Explorer Dynatrace**.
* Предыдущая версия Dynatrace Из [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по последней версии Dynatrace"), прокрутите вниз до **API Dynatrace** и выберите раздел API, который вас интересует.

Альтернативно, вы можете получить доступ к API Explorer через прямую ссылку `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнить вызовы API в API Explorer. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить payload запроса перед выполнением его, выбрав **Выполнить**.

Вы можете получить доступ ко всем конечным точкам API Dynatrace с помощью API Explorer.

* Последняя версия Dynatrace Перейдите в раздел **Токены доступа** и выберите ссылку **API Explorer Dynatrace**.
* Предыдущая версия Dynatrace Из [меню пользователя](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Навигация по последней версии Dynatrace"), прокрутите вниз до **API Dynatrace** и выберите раздел API, который вас интересует.

Альтернативно, вы можете получить доступ к API Explorer через прямую ссылку `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнить вызовы API в API Explorer. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить payload запроса перед выполнением его, выбрав **Выполнить**.

Вы можете получить доступ ко всем конечным точкам API Dynatrace с помощью API Explorer.

1. Перейдите в [**Управление учетными записями**](https://myaccount.dynatrace.com/). Если у вас есть несколько учетных записей, выберите учетную запись, которую вы хотите управлять.
2. В верхней навигационной панели перейдите в **Управление идентификаторами и доступом** > **Клиенты OAuth**.
3. В правом верхнем углу страницы выберите **API управления учетными записями**.

### Аутентификация в API Explorer

Выберите значок замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любой конечной точкой, чтобы отобразить информацию об OAuth 2.0-токенах, которые защищают эту конечную точку. Каждая конечная точка требует определенного типа токена.

Вы также можете разблокировать все конечные точки, выбрав **Авторизовать**. В отображаемом диалоговом окне вы можете увидеть, какие разрешения токена необходимы для каждой конечной точки API. Вводя свой OAuth 2.0-токен в глобальный диалог **Доступные авторизации**, вы можете разблокировать все связанные конечные точки API.

### Попробуйте вызов API

После ввода вашего OAuth 2.0-токена вы можете直接 выполнить вызовы API в API Explorer. Просто выберите **Попробовать** , чтобы открыть раздел параметров выбранной конечной точки API, где вы можете ввести дополнительные параметры и изменить payload запроса перед выполнением его, выбрав **Выполнить**.