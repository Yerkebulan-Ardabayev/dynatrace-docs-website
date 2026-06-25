---
title: Мониторинг Azure App Service (встроенный)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-builtin
scraped: 2026-05-12T11:26:22.700373
---

# Мониторинг Azure App Service (встроенный)

# Мониторинг Azure App Service (встроенный)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 10 февраля 2025 г.

Dynatrace получает метрики из Azure Metrics API для **Azure Application Services (Web App, Function App)**. Можно просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

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
| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Количество | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Количество | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Количество | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | В секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | В секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | В секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Количество | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Количество | autovalue | DDUs |
| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Количество | autovalue | DDUs |
| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | В секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | В секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | В секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.other | IO other bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.read | IO read bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.io.write | IO write bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.response.avg | Response time avg | Секунда | autoavgmaxmin | DDUs |
| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Байт | autovalue | DDUs |
| builtin:cloud.azure.appService.traffic.requests | Requests count | Количество | autovalue | DDUs |

## Ограничения

Полная интеграция и связывание с сервисами OneAgent:

* Logs
* Problems
* Attributes
* Tags

с сущностями `Service` поддерживается только для [Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions "Мониторинг Azure Functions").