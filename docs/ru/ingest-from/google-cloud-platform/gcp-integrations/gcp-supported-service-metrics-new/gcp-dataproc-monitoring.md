---
title: Google Cloud Dataproc monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring
scraped: 2026-03-06T21:37:51.032158
---

# Мониторинг Google Cloud Dataproc

# Мониторинг Google Cloud Dataproc

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собираемые из Google Operation API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в панелях мониторинга, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройте интеграцию](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций Google Cloud (метрик). Помимо этого, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Add or remove services](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Metrics browser](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и плитках панели мониторинга.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud Dataproc.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_dataproc\_cluster/default\_metrics | HDFS DataNodes | Count | dataproc.googleapis.com/cluster/hdfs/datanodes |
| cloud\_dataproc\_cluster/default\_metrics | Ёмкость HDFS | GibiByte | dataproc.googleapis.com/cluster/hdfs/storage\_capacity |
| cloud\_dataproc\_cluster/default\_metrics | Использование хранилища HDFS | Count | dataproc.googleapis.com/cluster/hdfs/storage\_utilization |
| cloud\_dataproc\_cluster/default\_metrics | Неработоспособные блоки HDFS по статусу | Count | dataproc.googleapis.com/cluster/hdfs/unhealthy\_blocks |
| cloud\_dataproc\_cluster/default\_metrics | Длительность задания | Second | dataproc.googleapis.com/cluster/job/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Длительность состояния задания | Second | dataproc.googleapis.com/cluster/job/duration |
| cloud\_dataproc\_cluster/default\_metrics | Неудачные задания | Count | dataproc.googleapis.com/cluster/job/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Выполняемые задания | Count | dataproc.googleapis.com/cluster/job/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Отправленные задания | Count | dataproc.googleapis.com/cluster/job/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Длительность операции | Second | dataproc.googleapis.com/cluster/operation/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Длительность состояния операции | Second | dataproc.googleapis.com/cluster/operation/duration |
| cloud\_dataproc\_cluster/default\_metrics | Неудачные операции | Count | dataproc.googleapis.com/cluster/operation/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Выполняемые операции | Count | dataproc.googleapis.com/cluster/operation/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Отправленные операции | Count | dataproc.googleapis.com/cluster/operation/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Процент выделенной памяти YARN | Count | dataproc.googleapis.com/cluster/yarn/allocated\_memory\_percentage |
| cloud\_dataproc\_cluster/default\_metrics | Активные приложения YARN | Count | dataproc.googleapis.com/cluster/yarn/apps |
| cloud\_dataproc\_cluster/default\_metrics | Контейнеры YARN | Count | dataproc.googleapis.com/cluster/yarn/containers |
| cloud\_dataproc\_cluster/default\_metrics | Размер памяти YARN | GibiByte | dataproc.googleapis.com/cluster/yarn/memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | NodeManagers YARN | Count | dataproc.googleapis.com/cluster/yarn/nodemanagers |
| cloud\_dataproc\_cluster/default\_metrics | Размер ожидающей памяти YARN | GibiByte | dataproc.googleapis.com/cluster/yarn/pending\_memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | Виртуальные ядра YARN | Count | dataproc.googleapis.com/cluster/yarn/virtual\_cores |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
