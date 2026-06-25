---
title: Azure Redis Cache (built-in)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin
scraped: 2026-05-12T11:27:29.739751
---

# Azure Redis Cache (built-in)

# Azure Redis Cache (built-in)

* Практическое руководство
* Чтение: 1 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических (ранее «built-in») сервисов Azure на облачные сервисы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Миграция классических сервисов Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для **Azure Redis Cache**. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Environment ActiveGate
* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

Этот сервис отслеживает Azure Cache for Redis (`Microsoft.Cache/redis`).

Сервис Enterprise Azure Cache for Redis (`Microsoft.Cache/redisEnterprise`) в настоящее время не может отслеживаться; чтобы запросить этот тип мониторинга, создайте RFE (Request for Enhancement).

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
| builtin:cloud.azure.redis.cache.hits | Cache hits | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.cache.misses | Cache misses | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.cache.read | Read bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.cache.write | Write bytes/s | Байт в секунду | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.commands.get | Get commands | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.commands.set | Set commands | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.commands.total | Total no. of processed commands | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.keys.evicted | No. of evicted keys | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.keys.expired | No. of expired keys | Количество | autovalue | DDUs |
| builtin:cloud.azure.redis.keys.total | Total no. of keys | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.memory.used | Used memory | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | Байт | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.connected | Connected clients | Количество | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.load | Server load | Процент (%) | autoavgmaxmin | DDUs |
| builtin:cloud.azure.redis.processorTime | Processor time | Процент (%) | autoavgmaxmin | DDUs |