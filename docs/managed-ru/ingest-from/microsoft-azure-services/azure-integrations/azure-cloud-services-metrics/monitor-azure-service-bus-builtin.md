---
title: Azure Service Bus (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-bus-builtin
scraped: 2026-05-12T11:26:52.157203
---

# Azure Service Bus (built-in)

# Azure Service Bus (built-in)

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 27 июля 2022 г.

Dynatrace получает метрики из Azure Metrics API для **Azure Service Bus**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Dynatrace версии 1.201+
* Environment ActiveGate версии 1.195+

* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

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
| builtin:cloud.azure.serviceBus.namespace.connections.active | Total active connections | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.errors.server | Server errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.errors.user | User errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.count | Count of messages | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.countActive | Count of active messages | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.countDeadLettered | Count of dead-lettered messages | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.countScheduled | Count of scheduled messages | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.incoming | Incoming messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.messages.outgoing | Outgoing messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.requests.incoming | Incoming requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.requests.successful | Total successful requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.requests.throttled | Throttled requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.namespace.cpu | Service bus premium namespace CPU usage metric | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.memory | Service bus premium namespace memory usage metric | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.namespace.size | Service bus size | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.errors.server | Server errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.errors.user | User errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.count | Count of messages in queue | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.countActive | Count of active messages in a queue | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.countDeadLettered | Count of dead-lettered messages in a queue | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.countScheduled | Count of scheduled messages in a queue | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.incoming | Incoming messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.messages.outgoing | Outgoing messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.requests.incoming | Incoming requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.requests.successful | Total successful requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.requests.throttled | Throttled requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.queue.size | Size of an queue | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.errors.server | Server errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.errors.user | User errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.count | Count of messages in topic | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.countActive | Count of active messages in a topic | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.countDeadLettered | Count of dead-lettered messages in a topic | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.countScheduled | Count of scheduled messages in a topic | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.incoming | Incoming messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.messages.outgoing | Outgoing messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.requests.incoming | Incoming requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.requests.successful | Total successful requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.requests.throttled | Throttled requests | Количество | autovalue | DDUs |
| builtin:cloud.azure.serviceBus.topic.size | Size of a topic | Байт | autoavgmaxmin | DDUs |