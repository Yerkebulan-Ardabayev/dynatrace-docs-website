---
title: Включение метрик Azure Monitor App Service Environment V2
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-environment
scraped: 2026-05-12T11:26:08.245710
---

# Включение метрик Azure Monitor App Service Environment V2

# Включение метрик Azure Monitor App Service Environment V2

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 29 июня 2022 г.

Dynatrace получает метрики из Azure Metrics API для Azure App Service Environment v2. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.201+
* Environment ActiveGate версии 1.195+

Dynatrace может отслеживать только App Service Environment v2.

Для мониторинга App Service Environment v1 обратитесь к эксперту по продуктам Dynatrace через live chat.

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в окружении Dynatrace на странице обзора пользовательского устройства (**custom device overview page**) или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы открыть страницу обзора пользовательского устройства

1. Откройте **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **custom device group overview page**.
4. На странице **custom device group overview page** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр, чтобы открыть **custom device overview page**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен преднастроенный дашборд, на странице **Dashboards** появится преднастроенный дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужный дашборд можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Напрямую вносить изменения в преднастроенный дашборд нельзя, но можно клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню (**…**) и выберите **Clone**.
Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![App Service Environment v2](https://dt-cdn.net/images/azure-metrics-3925-3bc9d7a9da.png)

App Service Environment v2

## Доступные метрики

| Имя | Описание | Измерения | Единица | Рекомендовано |
| --- | --- | --- | --- | --- |
| ActiveRequests | Активные запросы | **Instance** | Count | Применимо |
| CpuPercentage | Загрузка CPU | **Instance** | Percent | Применимо |
| BytesReceived | Входящие данные | **Instance** | Byte | Применимо |
| BytesSent | Исходящие данные | **Instance** | Byte | Применимо |
| DiskQueueLength | Длина очереди диска | **Instance** | Count | Применимо |
| Http101 | HTTP 101 | Instance | Count |  |
| Http2xx | HTTP 2xx | **Instance** | Count | Применимо |
| Http3xx | HTTP 3xx | **Instance** | Count | Применимо |
| Http401 | HTTP 401 | **Instance** | Count | Применимо |
| Http403 | HTTP 403 | **Instance** | Count | Применимо |
| Http404 | HTTP 404 | **Instance** | Count | Применимо |
| Http406 | HTTP 406 | **Instance** | Count | Применимо |
| Http4xx | HTTP 4xx | **Instance** | Count | Применимо |
| Http5xx | HTTP 5xx | **Instance** | Count | Применимо |
| HttpQueueLength | Длина очереди HTTP | **Instance** | Count |  |
| LargeAppServicePlanInstances | Рабочие процессы большого App Service Plan |  | Count |  |
| MediumAppServicePlanInstances | Рабочие процессы среднего App Service Plan |  | Count |  |
| MemoryPercentage | Использование памяти | **Instance** | Percent | Применимо |
| Requests | Запросы | **Instance** | Count | Применимо |
| SmallAppServicePlanInstances | Рабочие процессы малого App Service Plan |  | Count |  |
| TotalFrontEnds | Всего фронтендов |  | Count |  |