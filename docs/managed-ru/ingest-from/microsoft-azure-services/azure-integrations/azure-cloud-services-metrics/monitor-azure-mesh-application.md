---
title: Мониторинг Azure Mesh Application
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-mesh-application
scraped: 2026-05-12T11:27:15.401713
---

# Мониторинг Azure Mesh Application

# Мониторинг Azure Mesh Application

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 10 сентября 2020 г.

Этот сервис выведен Microsoft из эксплуатации. Дополнительную информацию см. в [объявлении Microsoft](https://azure.microsoft.com/en-us/updates/azure-service-fabric-mesh-preview-retirement/).

Dynatrace получает метрики из Azure Metrics API для Azure Mesh Application. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.201+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен предустановленный дашборд, он появится на вашей странице **Dashboards** с набором всех рекомендуемых метрик. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**…**) и выберите **Clone**.  
Чтобы убрать дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![Mesh](https://dt-cdn.net/images/dashboard-63-2674-12efdf4c98.png)

Mesh

## Доступные метрики

| Имя | Описание | Единица измерения | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| AllocatedCpu | ЦП, выделенный согласно шаблону Azure Resource Manager | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Количество | Применимо |
| AllocatedMemory | Память, выделенная согласно шаблону Azure Resource Manager | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Байт | Применимо |
| ActualCpu | Использование ЦП | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Количество | Применимо |
| ActualMemory | Использование памяти | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Байт | Применимо |
| CpuUtilization | Процент фактического/выделенного ЦП | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Процент | Применимо |
| MemoryUtilization | Процент фактической/выделенной памяти | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Процент | Применимо |