---
title: Мониторинг Azure Standard Load Balancer
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer
scraped: 2026-05-12T11:26:39.050400
---

# Мониторинг Azure Standard Load Balancer

# Мониторинг Azure Standard Load Balancer

* Практическое руководство
* Чтение: 2 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими службами и другими службами см. в разделе [Миграция с классических служб Azure (ранее «встроенных») на облачные службы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Перенос классических служб Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure Standard Load Balancer. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.199+
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

## Доступные метрики

Этот сервис отслеживает часть Azure Load Balancer (Microsoft.Network/loadBalancers). Пока этот сервис настроен, вы не можете включить сервис Azure Load Balancers (built-in).

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Data path availability | Средняя доступность пути данных Load Balancer за период времени | Frontend IP address, Frontend port | Количество | Применимо |
| Health probe status | Средний статус пробы работоспособности Load Balancer за период времени | Protocol type, Backend port, Frontend IP address, Frontend port, Backend IP address | Количество | Применимо |
| Byte count | Общее количество байтов, переданных за период времени | Frontend IP address, Frontend port, Direction | Байт |  |
| Packet count | Общее количество пакетов, переданных за период времени | Frontend IP address, Frontend port, Direction | Количество |  |
| SYN count | Общее количество SYN-пакетов, переданных за период времени | Frontend IP address, Frontend port, Direction | Количество |  |
| SNAT connection count | Общее количество новых SNAT-подключений, созданных за период времени | Frontend IP address, Backend IP address, Connection state | Количество |  |
| Allocated SNAT ports | Общее количество SNAT-портов, выделенных за период времени | Frontend IP address, Backend IP address, Protocol type | Количество |  |
| Used SNAT ports | Общее количество SNAT-портов, использованных за период времени | Frontend IP address, Backend IP address, Protocol type | Количество |  |
| Health probe status | Работоспособность и статус бэкенда Azure Cross-region Load Balancer за период времени | Frontend IP address, Frontend port, Backend IP address, Protocol type, Frontend region, Backend region | Количество |  |