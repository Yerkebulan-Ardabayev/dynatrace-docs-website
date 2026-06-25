---
title: Azure Load Balancers (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin
scraped: 2026-05-12T11:25:50.753874
---

# Azure Load Balancers (built-in)

# Azure Load Balancers (built-in)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для **Azure Load Balancers**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

Для Load Balancers уровня Basic SKU метрики недоступны.

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервисов Azure можно просматривать в вашем окружении Dynatrace на странице подписки Azure или на собственном дашборде.

Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).

### Просмотр метрик на странице учётной записи Azure

Чтобы получить доступ к метрикам на странице учётной записи Azure

1. Перейдите в **Azure**.
2. Выберите подписку Azure.
3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### Просмотр метрик на дашборде

Вы можете создать собственный дашборд для просмотра метрик сервисов Azure. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").

## Доступные метрики

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.loadbalancer.availability.dipTcp | Load balancer DIP TCP availability | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.loadbalancer.availability.dipUdp | Load balancer DIP UDP availability | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.loadbalancer.availability.vip | Load Balancer VIP availability | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.loadbalancer.snatConnection.est | SNAT connections successful | Количество | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.snatConnection.pending | SNAT connections pending | Количество | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.snatConnection.rej | SNAT connections failed | Количество | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.traffic.byteIn | Bytes received | Байт | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.traffic.byteOut | Bytes sent | Байт | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.traffic.packetIn | Packets received | Количество | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.traffic.packetOut | Packets sent | Количество | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.traffic.packetSynIn | SYN packets received | Количество | autovalue | DDUs |
| builtin:cloud.azure.loadbalancer.traffic.packetSynOut | SYN packets sent | Количество | autovalue | DDUs |