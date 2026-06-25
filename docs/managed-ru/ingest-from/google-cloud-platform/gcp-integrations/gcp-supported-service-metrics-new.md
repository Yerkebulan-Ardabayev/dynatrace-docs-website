---
title: Поддерживаемые сервисы Google Cloud
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new
scraped: 2026-05-12T11:10:35.442784
---

# Поддерживаемые сервисы Google Cloud

# Поддерживаемые сервисы Google Cloud

* Обзор
* Чтение: 3 мин
* Обновлено 23 сентября 2024 г.

Dynatrace версии 1.230+

Этот раздел относится к метрикам сервисов Google Cloud, доступным с интеграцией Google Cloud версии 1.0.

* Метрики сервисов Google Cloud, доступные с более ранними версиями интеграции с Google Cloud, см. в разделе [Метрики поддерживаемых сервисов Google Cloud (устаревшее)](/managed/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Поддерживаемые метрики сервисов GCP, конфигурация метрик, потребление DDU и доступность готовых дашбордов").

## Предварительные условия

[Развёртывание интеграции Dynatrace](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Поддерживаемые сервисы для метрик

После развёртывания интеграции Dynatrace можно получать аналитику по метрикам сервисов Google Cloud, собранным через Google Operations API, чтобы обеспечивать работоспособность вашей облачной инфраструктуры.

Ниже приведён список поддерживаемых сервисов Google Cloud.

| Сервисы | Поддерживаемые сущности[1](#fn-1-1-def) | Поддерживаемые логи | Сущности логов |
| --- | --- | --- | --- |
| [Мониторинг Google Cloud AI Platform (устарело)](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring "Мониторинг Google Cloud AI Platform и просмотр доступных метрик.") | cloudml\_job, cloudml\_model\_version | да | cloudml\_job, cloudml\_model\_version |
| [Мониторинг Google Cloud AlloyDB](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-alloydb-monitoring "Мониторинг Google Cloud AlloyDB и просмотр доступных метрик.") | alloydb\_database, alloydb\_instance | да | alloydb\_database, alloydb\_instance |
| [Мониторинг Google Cloud APIs](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Мониторинг Google Cloud APIs и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Apigee](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring "Мониторинг Google Cloud Apigee и просмотр доступных метрик.") | apigee\_environment, apigee\_proxy, apigee\_target | нет |  |
| [Мониторинг Google App Engine с метриками Operations suite](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Мониторинг Google App Engine и просмотр доступных метрик.") | gae\_app | да | gae\_app |
| [Мониторинг Google Cloud Assistant Smart Home](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-assistant-smart-home-monitoring "Мониторинг Google Cloud Assistant Smart Home и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google BigQuery](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Мониторинг Google BigQuery и просмотр доступных метрик.") | bigquery\_bigengine\_model | нет |  |
| [Мониторинг Google Cloud Bigtable](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring "Мониторинг Google Cloud Bigtable и просмотр доступных метрик.") | bigtable\_cluster, bigtable\_table | нет |  |
| [Мониторинг Google Cloud DNS](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-dns-monitoring "Мониторинг Google Cloud DNS и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Мониторинг Google Cloud Functions и просмотр доступных метрик.") | cloud\_function | да | cloud\_function |
| [Мониторинг Google Cloud IoT Core (устарело)](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-iot-core-monitoring "Мониторинг Google Cloud IoT Core и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Router](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring "Мониторинг Google Cloud Router и просмотр доступных метрик.") | nat\_gateway | да | nat\_gateway |
| [Мониторинг Google Cloud Run](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Мониторинг Google Cloud Run и просмотр доступных метрик.") | cloud\_function, cloud\_run\_revision | да | cloud\_run\_revision |
| [Мониторинг Google Cloud Storage](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Мониторинг Google Cloud Storage и просмотр доступных метрик.") | gcs\_bucket | да | gcs\_bucket |
| [Мониторинг Google Cloud Tasks](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-tasks-monitoring "Мониторинг Google Cloud Tasks и просмотр доступных метрик.") | cloud\_tasks\_queue | да | cloud\_tasks\_queue |
| [Мониторинг Google Cloud Composer](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring "Мониторинг Google Cloud Composer и просмотр доступных метрик.") | cloud\_composer\_environment | да | cloud\_composer\_environment |
| [Мониторинг Google Compute Engine с метриками Operations suite](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Мониторинг Google Compute Engine и просмотр доступных метрик.") | autoscaler, gce\_instance, instance\_group, tpu\_worker | да | autoscaler, gce\_autoscaler, gce\_instance\_group, gce\_instance, tpu\_worker |
| [Мониторинг Google Cloud Data Loss Prevention](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring "Мониторинг Google Cloud Data Loss Prevention (теперь часть Sensitive Data Protection) и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Storage Transfer Service](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-storage-transfer-service-monitoring "Мониторинг Google Cloud Storage Transfer Service и просмотр доступных метрик.") | storage\_transfer\_job, transfer\_service\_agent | да | storage\_transfer\_job |
| [Мониторинг Google Cloud Dataflow](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring "Мониторинг Google Cloud Dataflow и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Dataproc](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring "Мониторинг Google Cloud Dataproc и просмотр доступных метрик.") | cloud\_dataproc\_cluster | да | cloud\_dataproc\_cluster |
| [Мониторинг Google Cloud Firestore in Datastore mode](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Мониторинг Google Cloud Firestore in Datastore mode и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Filestore](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Мониторинг Google Filestore и просмотр доступных метрик.") | filestore\_instance | нет |  |
| [Мониторинг Google Cloud Firebase](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring "Мониторинг Google Cloud Firebase и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Cloud Firestore](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring "Мониторинг Google Cloud Firestore и просмотр доступных метрик.") | firestore\_database | нет |  |
| [Мониторинг Google Cloud Hybrid Connectivity](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring "Мониторинг Google Cloud Hybrid Connectivity и просмотр доступных метрик.") | interconnect, interconnect\_attachment, gce\_router, vpn\_gateway | да | gce\_router, vpn\_gateway |
| [Мониторинг Google Kubernetes Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Мониторинг Google Kubernetes Engine и просмотр доступных метрик.") | k8s\_cluster, k8s\_container, k8s\_node, k8s\_pod | да | k8s\_cluster, k8s\_container, k8s\_node, k8s\_pod |
| [Мониторинг Google Cloud Load Balancing](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Мониторинг Google Cloud Load Balancing и просмотр доступных метрик.") | https\_lb, internal\_http\_lb\_rule, internal\_network\_lb\_rule, network\_lb\_rule, tcp\_ssl\_proxy\_rule | да | http\_load\_balancer, internal\_http\_lb\_rule, internal\_network\_lb\_rule, network\_lb\_rule, tcp\_ssl\_proxy\_rule |
| [Мониторинг Google Managed Microsoft AD](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-managed-microsoft-ad-monitoring "Мониторинг Google Managed Microsoft AD и просмотр доступных метрик.") | microsoft\_ad\_domain | нет |  |
| [Мониторинг Google Cloud Memorystore](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring "Мониторинг Google Cloud Memorystore и просмотр доступных метрик.") | redis\_instance | да | redis\_instance |
| [Мониторинг NetApp on Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring "Мониторинг NetApp on Google Cloud и просмотр доступных метрик.") | netapp\_volumes\_replication, netapp\_volumes\_storage\_pool, netapp\_volumes\_volume | нет |  |
| [Мониторинг Google Cloud Network Security](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-security-monitoring "Мониторинг Google Cloud Network Security и просмотр доступных метрик.") | network\_security\_policy | да | network\_security\_policy |
| [Operations: Cloud Monitoring & Logging](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging "Мониторинг пакета Operations suite Google Cloud и просмотр доступных метрик.") | uptime\_url | да | uptime\_url |
| [Мониторинг Google Cloud Pub/Sub](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Мониторинг Google Cloud Pub/Sub и просмотр доступных метрик.") | pubsub\_snapshot, pubsub\_subscription, pubsub\_topic | да | pubsub\_snapshot, pubsub\_subscription, pubsub\_topic |
| [Мониторинг Google Cloud Pub/Sub Lite](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Мониторинг Google Cloud Pub/Sub Lite и просмотр доступных метрик.") | subscription\_partition, topic\_partition | нет |  |
| [Мониторинг Google Cloud Spanner](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring "Мониторинг Google Cloud Spanner и просмотр доступных метрик.") | spanner\_instance | да | spanner\_instance |
| [Мониторинг Google Cloud SQL](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Мониторинг Google Cloud SQL и просмотр доступных метрик.") | cloudsql\_database | да | cloudsql\_database |
| [Мониторинг Google Cloud Virtual Private Cloud (VPC)](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-virtual-private-cloud-monitoring "Мониторинг Google Cloud Virtual Private Cloud (VPC) и просмотр доступных метрик.") | vpc\_access\_connector | да | vpc\_access\_connector |
| [Мониторинг Google Cloud Network Topology](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-topology-monitoring "Мониторинг Google Cloud Network Topology и просмотр доступных метрик.") |  | нет |  |
| [Мониторинг Google Vertex AI](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-vertex-ai "Мониторинг Google Cloud Vertex AI и просмотр доступных метрик.") | vertex\_ai\_deployment\_resource\_pool, vertex\_ai\_endpoint, vertex\_ai\_feature\_online\_store, vertex\_ai\_feature\_store, vertex\_ai\_pipeline\_job, vertex\_ai\_index, vertex\_ai\_index\_endpoint, vertex\_ai\_publisher\_model, vision\_ai\_instance, vision\_ai\_stream | да | vertex\_ai\_deployment\_resource\_pool, vertex\_ai\_endpoint, vertex\_ai\_feature\_store, vertex\_ai\_pipeline\_job, vertex\_ai\_index\_endpoint |

1

У сервисов может быть одна сущность, несколько сущностей или ни одной.

## Проверка доступных метрик

Чтобы проверить доступные метрики для сервиса, выполните следующие действия:

1. Найдите расширение в [Hub](https://www.dynatrace.com/hub/?query=google&filter=all) и выберите его, чтобы открыть обзорную страницу. См. пример: [Google Cloud Functions](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).
2. Прокрутите обзорную страницу расширения до конца, чтобы найти раздел **Feature sets**.
3. В таблице выберите раскрывающийся список **default\_metrics**.
4. Теперь можно проверить все доступные метрики для выбранного сервиса.

## Потребление мониторинга

### Приём метрик

Все облачные сервисы потребляют DDU. Объём потребления DDU на один экземпляр сервиса зависит от числа отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. [Расширение Dynatrace (единицы Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление при мониторинге Dynatrace на основе единиц Davis data units (DDU).").

### Приём логов

Потребление DDU применяется к облачному Log Monitoring. Подробнее см. [DDU для Log Monitoring Classic](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")