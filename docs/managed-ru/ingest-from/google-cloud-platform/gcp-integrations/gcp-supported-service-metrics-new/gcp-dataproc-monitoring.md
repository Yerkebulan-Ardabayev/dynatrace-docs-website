---
title: Мониторинг Google Cloud Dataproc
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring
scraped: 2026-05-12T11:50:17.698245
---

# Мониторинг Google Cloud Dataproc

# Мониторинг Google Cloud Dataproc

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

Для Google Cloud Dataproc доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_dataproc\_cluster/default\_metrics | HDFS DataNodes | Количество | dataproc.googleapis.com/cluster/hdfs/datanodes |
| cloud\_dataproc\_cluster/default\_metrics | HDFS capacity | Гибибайт | dataproc.googleapis.com/cluster/hdfs/storage\_capacity |
| cloud\_dataproc\_cluster/default\_metrics | HDFS storage utilization | Количество | dataproc.googleapis.com/cluster/hdfs/storage\_utilization |
| cloud\_dataproc\_cluster/default\_metrics | Unhealthy HDFS blocks by status | Количество | dataproc.googleapis.com/cluster/hdfs/unhealthy\_blocks |
| cloud\_dataproc\_cluster/default\_metrics | Job duration | Секунда | dataproc.googleapis.com/cluster/job/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Job state duration | Секунда | dataproc.googleapis.com/cluster/job/duration |
| cloud\_dataproc\_cluster/default\_metrics | Failed jobs | Количество | dataproc.googleapis.com/cluster/job/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Running jobs | Количество | dataproc.googleapis.com/cluster/job/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Submitted jobs | Количество | dataproc.googleapis.com/cluster/job/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Operation duration | Секунда | dataproc.googleapis.com/cluster/operation/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Operation state duration | Секунда | dataproc.googleapis.com/cluster/operation/duration |
| cloud\_dataproc\_cluster/default\_metrics | Failed operations | Количество | dataproc.googleapis.com/cluster/operation/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Running operations | Количество | dataproc.googleapis.com/cluster/operation/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Submitted operations | Количество | dataproc.googleapis.com/cluster/operation/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | YARN allocated memory percentage | Количество | dataproc.googleapis.com/cluster/yarn/allocated\_memory\_percentage |
| cloud\_dataproc\_cluster/default\_metrics | YARN active applications | Количество | dataproc.googleapis.com/cluster/yarn/apps |
| cloud\_dataproc\_cluster/default\_metrics | YARN containers | Количество | dataproc.googleapis.com/cluster/yarn/containers |
| cloud\_dataproc\_cluster/default\_metrics | YARN memory size | Гибибайт | dataproc.googleapis.com/cluster/yarn/memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | YARN NodeManagers | Количество | dataproc.googleapis.com/cluster/yarn/nodemanagers |
| cloud\_dataproc\_cluster/default\_metrics | YARN pending memory size | Гибибайт | dataproc.googleapis.com/cluster/yarn/pending\_memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | YARN virtual cores | Количество | dataproc.googleapis.com/cluster/yarn/virtual\_cores |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")