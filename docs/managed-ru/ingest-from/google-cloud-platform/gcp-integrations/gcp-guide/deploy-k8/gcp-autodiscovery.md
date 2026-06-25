---
title: Мониторинг проектов Google Cloud с помощью автообнаружения
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery
scraped: 2026-05-12T12:08:45.262975
---

# Мониторинг проектов Google Cloud с помощью автообнаружения

# Мониторинг проектов Google Cloud с помощью автообнаружения

* Практическое руководство
* Чтение: 6 мин
* Опубликовано 25 сентября 2023 г.
* Early Access

Начиная с версии 1.3.0+ интеграции Google Cloud Monitor, вы можете расширить охват метрик за пределы предопределённого набора сервисов, поддерживаемых расширениями.

* Полный список поддерживаемых сервисов см. в разделе [Метрики поддерживаемых сервисов Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик.").
* Чтобы отслеживать любую метрику любого ресурса Google, не охваченного этими сервисами, следуйте инструкциям на этой странице для активации автообнаружения.

Возможные сценарии автообнаружения зависят от сервисов, метрики которых вы хотите отслеживать:

* Расширение метрик для уже поддерживаемых сервисов
* Интеграция любого сервиса на основе имени ресурса

## Перед началом

Это руководство является частью основной [настройки интеграции метрик и логов Dynatrace с Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") и посвящено исключительно конфигурации автообнаружения.

### Минимальная версия

Если интеграция Google Cloud ранее была настроена с использованием версии ниже 1.3.0, необходимо выполнить новое развёртывание всего решения с использованием версии 1.3.0+.

### Настройка мониторинга с автообнаружением

#### Проверьте разрешения

Если вы управляете разрешениями вручную, убедитесь, что следующие разрешения добавлены к роли Dynatrace Google Cloud Metrics Monitor.

* `monitoring.metricDescriptors.list`
* `monitoring.monitoredResourceDescriptors.get`
* `monitoring.monitoredResourceDescriptors.list`

#### Включите обогащение метрик автообнаружением

Чтобы включить обогащение метрик автообнаружением, отредактируйте следующий параметр в `values.yaml`:

```
metricAutodiscovery: "true"
```

## Расширение метрик для уже поддерживаемых сервисов

В рамках стандартных поддерживаемых сервисов в Dynatrace регулярно отправляется заранее определённый набор метрик. Подробнее о включении этих сервисов см. [Выбор сервисов для мониторинга метрик](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#services-metrics "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Однако режим автообнаружения обеспечивает большую гибкость, позволяя собирать все доступные метрики для конкретного сервиса.

### Включение автообнаружения

Чтобы включить его, необходимо изменить файл `values.yaml`, найдя нужный сервис следующим образом:

```
- service: cloud_service_name



allowAutodiscovery: True
```

### Поддерживаемые сервисы

Разверните приведённую ниже таблицу со списком ресурсов, которые в настоящее время отслеживаются поддерживаемыми сервисами и могут быть расширены с помощью автообнаружения.

### Поддерживаемые сервисы Dynatrace Google Cloud

| Отслеживаемый ресурс | Имя сервиса |
| --- | --- |
| alloydb.googleapis.com/Database | Google AlloyDB |
| alloydb.googleapis.com/Instance | Google AlloyDB |
| api | Google Cloud APIs |
| apigee.googleapis.com/Environment | Google Apigee |
| apigee.googleapis.com/Proxy | Google Apigee |
| apigee.googleapis.com/ProxyV2 | Google Apigee |
| apigee.googleapis.com/TargetV2 | Google Apigee |
| assistant\_action\_project | Google Assistant Smart Home |
| autoscaler | Google Compute Engine |
| aws\_ec2\_instance | Google Compute Engine |
| baremetalsolution.googleapis.com/Instance | Google Compute Engine |
| bigquery\_biengine\_model | Google BigQuery |
| bigquery\_project | Google BigQuery |
| bigtable\_cluster | Google Cloud Bigtable |
| bigtable\_table | Google Cloud Bigtable |
| cloud\_composer\_environment | Google Cloud Composer |
| cloud\_dataproc\_cluster | Google Dataproc |
| cloud\_dlp\_project | Google Cloud Data Loss Prevention |
| cloud\_function | Google Cloud Functions |
| cloud\_run\_job | Google Cloud Run |
| cloud\_run\_revision | Google Cloud Run |
| cloud\_tasks\_queue | Google Cloud Tasks |
| cloudiot\_device\_registry | Google Cloud IoT Core |
| cloudml\_job | Google AI Platform |
| cloudml\_model\_version | Google AI Platform |
| cloudsql\_database | Google Cloud SQL |
| cloudsql\_instance\_database | Google Cloud SQL |
| cloudvolumesgcp-api.netapp.com/CloudVolume | NetApp on Google Cloud |
| consumed\_api | Google Cloud APIs |
| consumer\_quota | Google Cloud APIs |
| dataflow\_job | Google Dataflow |
| datastore\_request | Google Firestore in Datastore mode |
| dns\_query | Google Cloud DNS |
| filestore\_instance | Google Cloud Filestore |
| firebase\_domain | Google Firebase |
| firebase\_namespace | Google Firebase |
| firestore.googleapis.com/Database | Google Cloud Filestore |
| firestore\_instance | Google Cloud Filestore |
| gae\_app | Google App Engine |
| gae\_instance | Google App Engine |
| gce\_router | Google Hybrid Connectivity |
| gce\_zone\_network\_health | Google Network Topology |
| gcs\_bucket | Google Cloud Storage |
| https\_lb\_rule | Google Cloud Load Balancing |
| instance\_group | Google Compute Engine |
| interconnect | Google Hybrid Connectivity |
| interconnect\_attachment | Google Hybrid Connectivity |
| internal\_http\_lb\_rule | Google Cloud Load Balancing |
| internal\_tcp\_lb\_rule | Google Cloud Load Balancing |
| internal\_udp\_lb\_rule | Google Cloud Load Balancing |
| istio\_control\_plane | Google Kubernetes Engine |
| k8s\_container | Google Kubernetes Engine |
| k8s\_node | Google Kubernetes Engine |
| k8s\_pod | Google Kubernetes Engine |
| loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule | Google Cloud Load Balancing |
| microsoft\_ad\_domain | Google Managed Microsoft AD |
| nat\_gateway | Google Cloud Router |
| netapp\_cloud\_volume | NetApp on Google Cloud |
| network\_security\_policy | Google Network Security |
| produced\_api | Google Cloud APIs |
| producer\_quota | Google Cloud APIs |
| pubsub\_snapshot | Google Pub/Sub |
| pubsub\_subscription | Google Pub/Sub |
| pubsub\_topic | Google Pub/Sub |
| pubsublite\_subscription\_partition | Google Pub/Sub Lite |
| pubsublite\_topic\_partition | Google Pub/Sub Lite |
| recaptchaenterprise.googleapis.com/Key | Google reCAPTCHA Enterprise |
| redis\_instance | Google Memorystore |
| spanner\_instance | Google Cloud Spanner |
| tcp\_lb\_rule | Google Cloud Load Balancing |
| tcp\_ssl\_proxy\_rule | Google Cloud Load Balancing |
| tpu\_worker | Google Compute Engine |
| transfer\_service\_agent | Google Cloud Storage Transfer Service |
| udp\_lb\_rule | Google Cloud Load Balancing |
| vpc\_access\_connector | Google Virtual Private Cloud |
| vpn\_gateway | Google Hybrid Connectivity |

## Интеграция любого сервиса на основе имени ресурса

В ситуациях, когда расширенных возможностей мониторинга поддерживаемых сервисов недостаточно, автообнаружение Google Cloud предоставляет решение для мониторинга любого сервиса, предлагаемого Google.

### Ограничения

* Режим автообнаружения предназначен для обнаружения только тех метрик, которые связаны с одним ресурсом.
* Эти метрики не привязаны ни к какому поддерживаемому сервису, поэтому из них не будет извлечена сущность или какое-либо обогащение.

### Настройка значений параметров

Пакет развёртывания helm содержит файл `autodiscovery-values.yaml` с необходимой конфигурацией для этого сценария. Отредактируйте этот файл, чтобы задать обязательные и необязательные значения параметров следующим образом.

| **Имя параметра** | **Описание** | **Значение по умолчанию** |
| --- | --- | --- |
| `autodiscoveryQueryInterval` | Обязательный. Интервал опроса автообнаружения в минутах. Минимальное значение: `60`. | `60` |
| `autodiscoveryIncludeAlphaMetrics` | Необязательный. При установке в `true` включает автоматическое обнаружение экспериментальных метрик Google Cloud с меткой 'Alpha'. | `true` |
| `autodiscoveryAddLabels` | Необязательный. При установке в `true` добавляет метку `[Autodiscovered]` к именам метрик во время автоматического обнаружения. | `true` |
| `autodiscoveryResourcesYaml` | Необязательный. Конфигурационный файл для ресурсов автообнаружения. |  |
| `autodiscoveryBlockListYaml` | Необязательный. Конфигурационный файл для префиксов имён метрик автообнаружения, которые не должны включаться. |  |

### Выбор ресурсов

Укажите метрики для отправки в Dynatrace, перечислив типы ресурсов отслеживаемых ресурсов в разделе `autodiscoveryResourcesYaml`. Чтобы определить ресурсы для мониторинга в вашем проекте, см. [Метрики Google Cloud](https://dt-url.net/th03qct).

Пример:

```
autodiscoveryResourcesYaml: |



autodicovery_config:



searched_resources:



- memcache_node
```

### Отключение выбранных метрик

Чтобы исключить определённые метрики, перечислите их префиксы в разделе `autodiscoveryBlockListYaml`. Любая подходящая метрика будет исключена.

Пример:

```
autodiscoveryBlockListYaml: |



block_list:



- memcache.googleapis.com/node/
```

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")
* [Мониторинг нескольких проектов Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправляйте метрики в Dynatrace из нескольких проектов Google Cloud.")