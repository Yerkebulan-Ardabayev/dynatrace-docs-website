---
title: Мониторинг Google Cloud Composer
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring
scraped: 2026-05-12T11:50:15.797372
---

# Мониторинг Google Cloud Composer

# Мониторинг Google Cloud Composer

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Cloud Composer доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_composer\_environment/default\_metrics | API Requests | Количество | composer.googleapis.com/environment/api/request\_count |
| cloud\_composer\_environment/default\_metrics | API Latency | Миллисекунда | composer.googleapis.com/environment/api/request\_latencies |
| cloud\_composer\_environment/default\_metrics | Parse Error Count | Количество | composer.googleapis.com/environment/dag\_processing/parse\_error\_count |
| cloud\_composer\_environment/default\_metrics | DAG parsing processes | Количество | composer.googleapis.com/environment/dag\_processing/processes |
| cloud\_composer\_environment/default\_metrics | Processors Timeout Count | Количество | composer.googleapis.com/environment/dag\_processing/processor\_timeout\_count |
| cloud\_composer\_environment/default\_metrics | Total Parse Time | Секунда | composer.googleapis.com/environment/dag\_processing/total\_parse\_time |
| cloud\_composer\_environment/default\_metrics | Dag Bag Size | Количество | composer.googleapis.com/environment/dagbag\_size |
| cloud\_composer\_environment/default\_metrics | Database Healthy | Не указано | composer.googleapis.com/environment/database\_health |
| cloud\_composer\_environment/default\_metrics | Executor Open Slots | Количество | composer.googleapis.com/environment/executor/open\_slots |
| cloud\_composer\_environment/default\_metrics | Executor Running Tasks | Количество | composer.googleapis.com/environment/executor/running\_tasks |
| cloud\_composer\_environment/default\_metrics | Task Instance Count | Количество | composer.googleapis.com/environment/finished\_task\_instance\_count |
| cloud\_composer\_environment/default\_metrics | Healthy | Не указано | composer.googleapis.com/environment/healthy |
| cloud\_composer\_environment/default\_metrics | Celery Workers | Количество | composer.googleapis.com/environment/num\_celery\_workers |
| cloud\_composer\_environment/default\_metrics | Scheduler Heartbeats | Количество | composer.googleapis.com/environment/scheduler\_heartbeat\_count |
| cloud\_composer\_environment/default\_metrics | Task Queue Length | Количество | composer.googleapis.com/environment/task\_queue\_length |
| cloud\_composer\_environment/default\_metrics | Worker Pod Eviction Count | Количество | composer.googleapis.com/environment/worker/pod\_eviction\_count |
| cloud\_composer\_environment/default\_metrics | Zombie Tasks Killed | Количество | composer.googleapis.com/environment/zombie\_task\_killed\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")