---
title: Azure Event Hubs (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hub-builtin
scraped: 2026-05-12T11:27:11.878032
---

# Azure Event Hubs (built-in)

# Azure Event Hubs (built-in)

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 26 июля 2022 г.

Dynatrace получает метрики из Azure Metrics API для **Azure Event Hubs**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

Этот сервис отслеживает и `Microsoft.EventHub/namespaces`, и `Microsoft.EventHub/namespaces/eventHubs`.

Непосредственно на странице обзора Azure, в разделе **Event hubs**, представлены только отслеживаемые Event Hubs (в отличие от Event Hub Namespaces). Чтобы просмотреть метрики для Event Hub Namespace, создайте пользовательский дашборд.

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
| builtin:cloud.azure.eventHub.capture.backlog | Capture backlog | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.capture.bytes | Captured bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.eventHub.capture.msg | Captured messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.errors.quotaExceeded | Quota exceeded errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.errors.server | Server errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.errors.user | User errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.requests.incoming | Incoming requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.requests.successful | Successful requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.requests.throttled | Throttled requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.bytesIn | Incoming bytes | Байт в минуту | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.bytesOut | Outgoing bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.msgIn | Incoming messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHub.traffic.msgOut | Outgoing messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.eventHubNamespace.connections.active | Active connections | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.eventHubNamespace.connections.closed | Closed connections | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.eventHubNamespace.connections.opened | Opened connections | Количество | autoavgmaxmin | DDUs |