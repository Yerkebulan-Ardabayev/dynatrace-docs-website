---
title: Мониторинг Azure API Management (built-in) (устарело)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-services-builtin
scraped: 2026-05-12T11:25:38.487519
---

# Мониторинг Azure API Management (built-in) (устарело)

# Мониторинг Azure API Management (built-in) (устарело)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure API Management Services. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать их по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на дашбордах.

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
| builtin:cloud.azure.apiMgmt.requests.failed | Failed requests | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.apiMgmt.requests.other | Other requests | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.apiMgmt.requests.successful | Successful requests | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.apiMgmt.requests.total | Total requests | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.apiMgmt.requests.unauth | Unauthorized requests | Количество | autoavgcountmaxminsum | DDUs |
| builtin:cloud.azure.apiMgmt.capacity | Capacity | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.apiMgmt.duration | Duration | Миллисекунда | autoavgmaxmin | DDUs |