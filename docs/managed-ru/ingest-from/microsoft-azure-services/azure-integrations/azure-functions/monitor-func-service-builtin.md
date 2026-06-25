---
title: Мониторинг Function Service (встроенный)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin
scraped: 2026-05-12T11:38:19.445764
---

# Мониторинг Function Service (встроенный)

# Мониторинг Function Service (встроенный)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 10 февраля 2025 г.

Dynatrace получает метрики из Azure Metrics API для **Azure Function App**. Для каждого экземпляра сервиса можно просматривать метрики, разбивать их по различным измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервисов Azure можно просматривать в окружении Dynatrace на странице подписки Azure или на собственном дашборде.

Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).

### Просмотр метрик на странице учётной записи Azure

Чтобы получить доступ к метрикам на странице учётной записи Azure

1. Перейдите в **Azure**.
2. Выберите подписку Azure.
3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.

   ![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)

   Azure service metrics

### Просмотр метрик на дашборде

Для просмотра метрик сервисов Azure можно создать собственный дашборд. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").

## Доступные метрики

Видимость метрик зависит от типа приложения.

* builtin:cloud.azure.appService

  + для WebApps (`Microsoft.Web/sites, kind = app`)
* builtin:cloud.azure.appService.functions

  + для FunctionApps (`Microsoft.Web/sites, kind = functionapp`)
  + для Logic Apps, созданных на Standard Plan (`"type": "Microsoft.Web/sites", "kind": "functionapp,workflowapp"`)

| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |
| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.response.avg | Response time avg | Second | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |
| builtin:cloud.azure.appService.traffic.requests | Requests count | Count | autovalue | DDUs |