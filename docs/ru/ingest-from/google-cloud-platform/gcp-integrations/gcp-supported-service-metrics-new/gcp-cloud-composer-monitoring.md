---
title: Мониторинг Google Cloud Composer
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring
scraped: 2026-03-04T21:37:01.937241
---

# Мониторинг Google Cloud Composer

# Мониторинг Google Cloud Composer

* Последняя версия Dynatrace
* Практическое руководство
* 1 мин. чтения
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все важные данные на дашбордах, интеграция также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, можно добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов для получения необходимых данных.") и тайлах дашборда.

## Таблица метрик

Для Google Cloud Composer доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_composer\_environment/default\_metrics | API Requests | Count | composer.googleapis.com/environment/api/request\_count |
| cloud\_composer\_environment/default\_metrics | API Latency | MilliSecond | composer.googleapis.com/environment/api/request\_latencies |
| cloud\_composer\_environment/default\_metrics | Parse Error Count | Count | composer.googleapis.com/environment/dag\_processing/parse\_error\_count |
| cloud\_composer\_environment/default\_metrics | DAG parsing processes | Count | composer.googleapis.com/environment/dag\_processing/processes |
| cloud\_composer\_environment/default\_metrics | Processors Timeout Count | Count | composer.googleapis.com/environment/dag\_processing/processor\_timeout\_count |
| cloud\_composer\_environment/default\_metrics | Total Parse Time | Second | composer.googleapis.com/environment/dag\_processing/total\_parse\_time |
| cloud\_composer\_environment/default\_metrics | Dag Bag Size | Count | composer.googleapis.com/environment/dagbag\_size |
| cloud\_composer\_environment/default\_metrics | Database Healthy | Unspecified | composer.googleapis.com/environment/database\_health |
| cloud\_composer\_environment/default\_metrics | Executor Open Slots | Count | composer.googleapis.com/environment/executor/open\_slots |
| cloud\_composer\_environment/default\_metrics | Executor Running Tasks | Count | composer.googleapis.com/environment/executor/running\_tasks |
| cloud\_composer\_environment/default\_metrics | Task Instance Count | Count | composer.googleapis.com/environment/finished\_task\_instance\_count |
| cloud\_composer\_environment/default\_metrics | Healthy | Unspecified | composer.googleapis.com/environment/healthy |
| cloud\_composer\_environment/default\_metrics | Celery Workers | Count | composer.googleapis.com/environment/num\_celery\_workers |
| cloud\_composer\_environment/default\_metrics | Scheduler Heartbeats | Count | composer.googleapis.com/environment/scheduler\_heartbeat\_count |
| cloud\_composer\_environment/default\_metrics | Task Queue Length | Count | composer.googleapis.com/environment/task\_queue\_length |
| cloud\_composer\_environment/default\_metrics | Worker Pod Eviction Count | Count | composer.googleapis.com/environment/worker/pod\_eviction\_count |
| cloud\_composer\_environment/default\_metrics | Zombie Tasks Killed | Count | composer.googleapis.com/environment/zombie\_task\_killed\_count |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")
