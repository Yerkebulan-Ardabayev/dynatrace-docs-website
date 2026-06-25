---
title: Миграция на интеграцию Google Cloud версии 1.0
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function
scraped: 2026-05-12T11:51:47.072093
---

# Миграция на интеграцию Google Cloud версии 1.0

# Миграция на интеграцию Google Cloud версии 1.0

* Практическое руководство
* Чтение: 5 мин
* Опубликовано 17 января 2022 г.

Dynatrace версии 1.230+

Новая версия интеграции Google Cloud (v.1.0) использует [Extensions 2.0](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.") и вводит [пользовательскую топологию](/managed/ingest-from/extend-dynatrace/extend-topology/custom-topology "Узнайте, как создать модель пользовательской топологии, подходящую для ваших телеметрических данных.") для ряда сервисов Google Cloud.

Список сервисов с пользовательской топологией

* Google Compute Engine
* Google Cloud Storage
* Google Cloud Functions
* Google Cloud Run
* Google App Engine
* Google Cloud Tasks
* Google Cloud SQL
* Google Cloud Datastore
* Google Load Balancing
* Google Cloud NAT Gateway
* Google Filestore
* Google Kubernetes Engine
* Google Pub/Sub
* Google Pub/Sub Lite
* Google Memorystore
* Google Spanner

Обратите внимание, что имена существующих измерений метрик изменятся при переходе на интеграцию Google Cloud с использованием Dynatrace Extensions 2.0. Изменения имён измерений затрагивают все настроенные зоны управления, пользовательские оповещения и пользовательские дашборды в вашем окружении. Чтобы восстановить корректную работу этих сущностей, выполните приведённые ниже инструкции.

Обновление существующих установок `dynatrace-gcp-monitor` с более ранних версий не поддерживается. Сначала необходимо удалить существующее развёртывание, а затем установить интеграцию Google Cloud v.1.0. Инструкции приведены ниже.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Удалите существующее развёртывание**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#delete-deployment "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Удалите дашборды и/или оповещения**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#remove-dashboards "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Установите новое развёртывание Google Cloud**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#install-deployment "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Обновите измерения**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#update-dimensions "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.")

## Шаг 1 Удалите существующее развёртывание

Для развёртывания в контейнере Kubernetes

Для развёртывания в GC Function

1. Определите, какую версию релиза вы используете.

   ```
   helm ls -n dynatrace
   ```
2. Удалите релиз.

   Обязательно замените `<release-name>` на имя релиза из предыдущего вывода.

   ```
   helm uninstall <release-name> -n dynatrace
   ```

1. Удалите релиз.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/uninstall.sh -O uninstall.sh ; chmod a+x uninstall.sh ; ./uninstall.sh
```

2. Удалите файл конфигурации сервиса `activation-config.yaml`.

## Шаг 2 Удалите дашборды и/или оповещения

Необходимо вручную удалить все дашборды или оповещения, созданные вручную во время предыдущей установки.

## Шаг 3 Установите новое развёртывание Google Cloud

Чтобы установить новое развёртывание Google Cloud, см. [Настройка интеграции метрик и логов Dynatrace с Google Cloud (v.1.0) в новом кластере GKE Autopilot](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

## Шаг 4 Обновите измерения

Если вы создали собственные дашборды, оповещения или зоны управления на основе метрик Google Cloud, необходимо вручную обновить измерения согласно приведённому ниже списку, чтобы получить ссылки для сущностей.

### Список изменений измерений

| Старое имя измерения | Новое имя измерения |
| --- | --- |
| `project_id` | `gcp.project.id` |
| `region` | `gcp.region` |
| `zone` | `gcp.region` |
| `instance_id` | `gcp.instance.id` |
| `autoscaler_id` | `gcp.instance.id` |
| `model_id` | `gcp.instance.id` |
| `queue_id` | `gcp.instance.id` |
| `device_registry_id` | `gcp.instance.id` |
| `job_id` | `gcp.instance.id` |
| `version_id` | `gcp.instance.id` |
| `database_id` | `gcp.instance.id` |
| `volume_id` | `gcp.instance.id` |
| `router_id` | `gcp.instance.id` |
| `instance_group_id` | `gcp.instance.id` |
| `interconnect` | `gcp.instance.id` |
| `attachment` | `gcp.instance.id` |
| `volume_id` | `gcp.instance.id` |
| `snapshot_id` | `gcp.instance.id` |
| `subscription_id` | `gcp.instance.id` |
| `topic_id` | `gcp.instance.id` |
| `key_id` | `gcp.instance.id` |
| `worker_id` | `gcp.instance.id` |
| `agent_id` | `gcp.instance.id` |
| `gateway_id` | `gcp.instance.id` |
| `name` | `gcp.instance.name` |
| `autoscaler_name` | `gcp.instance.name` |
| `environment_name` | `gcp.instance.name` |
| `cluster_name gcp.instance.name` | `gcp.instance.name` |
| `function_name gcp.instance.name` | `gcp.instance.name` |
| `revision_name` | `gcp.instance.name` |
| `job_name` | `gcp.instance.name` |
| `instance_name` | `gcp.instance.name` |
| `domain_name` | `gcp.instance.name` |
| `table_name` | `gcp.instance.name` |
| `firewall_name` | `gcp.instance.name` |
| `bucket_name` | `gcp.instance.name` |
| `container_name` | `gcp.instance.name` |
| `url_map_name` | `gcp.instance.name` |
| `instance_group_name` | `gcp.instance.name` |
| `load_balancer_name` | `gcp.instance.name` |
| `canonical_service_name` | `gcp.instance.name` |
| `node_name` | `gcp.instance.name` |
| `pod_name` | `gcp.instance.name` |
| `broker_name` | `gcp.instance.name` |
| `revision_name` | `gcp.instance.name` |
| `trigger_name` | `gcp.instance.name` |
| `fqdn` | `gcp.instance.name` |
| `target_domain_name` | `gcp.instance.name` |
| `gateway_name` | `gcp.instance.name` |
| `policy_name` | `gcp.instance.name` |
| `proxy_name` | `gcp.instance.name` |
| `load_balancer_name` | `gcp.instance.name` |
| `backend_target_name` | `gcp.instance.name` |
| `connector_name` | `gcp.instance.name` |
| `gateway_name` | `gcp.instance.name` |

* Чтобы обновить измерения для дашбордов

  1. Перейдите в **Dashboards**.
  2. Выберите дашборд, для которого нужно обновить измерения, затем выберите **More** (**…**) > **Configure**.
  3. Выберите **Dashboard JSON**.
  4. В разделе `"splitBy"` замените старые измерения новыми значениями согласно [списку изменений измерений](#dimension).
  5. Выберите **Save changes**.

Кроме того, вы можете заменить измерения, настроив каждую плитку выбранного дашборда в Data Explorer.

* Чтобы обновить измерения для оповещений

  1. Перейдите в **Settings**.
  2. Выберите **Anomaly detection** > **Metric events**.
  3. Выберите событие, для которого нужно обновить измерения.
  4. В поле **Add dimension filter** выберите новые ключи измерений и введите соответствующие значения измерений согласно [списку изменений измерений](#dimension).
  5. Выберите **Save changes**.
* Чтобы обновить измерения для зон управления

  1. Перейдите в **Settings**.
  2. Выберите **Preferences** > **Management zones**.
  3. Выберите **Edit** для зоны управления, для которой нужно обновить измерения.
  4. Выберите **Edit**, чтобы изменить существующее правило.
  5. В разделе **Conditions** измените значение `DIMENSION` согласно [Списку изменений измерений](#dimension).
  6. Выберите **Save changes**.

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")