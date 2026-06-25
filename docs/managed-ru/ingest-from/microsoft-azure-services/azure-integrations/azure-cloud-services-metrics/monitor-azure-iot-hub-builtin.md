---
title: Azure IoT Hub (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin
scraped: 2026-05-12T11:25:22.462758
---

# Azure IoT Hub (built-in)

# Azure IoT Hub (built-in)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для **Azure IoT Hub**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Environment ActiveGate
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
| builtin:cloud.azure.iotHub.command.abandoned | Commands abandoned | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.command.completed | Commands completed | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.command.rejected | Commands rejected | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.device.connected | Connected devices | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.device.registered | Total devices | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Messages delivered to the built-in endpoint (messages/events) | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Message latency for the built-in endpoint (messages/events) | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.eventHub.messages.delivered | Messages delivered to Event Hub endpoints | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Message latency for event hub endpoints | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.messages.dropped | Dropped messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Invalid messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.orphaned | Orphaned messages | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.messages.sentToFallback | Messages matching fallback condition | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Message latency for service bus queue endpoints | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Messages delivered to service bus queue endpoints | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Message latency for service bus topic endpoints | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Messages delivered to service bus topic endpoints | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Message latency for storage endpoints | Миллисекунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Blobs written to storage | Количество | autovalue | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Data written to storage | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Messages delivered to storage endpoints | Количество | autovalue | DDUs |