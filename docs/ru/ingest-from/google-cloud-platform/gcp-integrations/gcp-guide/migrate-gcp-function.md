---
title: Migrate to Google Cloud integration version 1.0
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function
scraped: 2026-03-06T21:35:30.359364
---

# Миграция на версию 1.0 интеграции с Google Cloud

# Миграция на версию 1.0 интеграции с Google Cloud

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 5 мин
* Опубликовано 17 января 2022 г.

Dynatrace версии 1.230+

Новая версия интеграции с Google Cloud (v.1.0) использует [Extensions 2.0](/docs/ingest-from/extensions "Узнайте, как создавать и управлять расширениями Dynatrace.") и вводит [пользовательскую топологию](/docs/ingest-from/extend-dynatrace/extend-topology/custom-topology "Узнайте, как создать пользовательскую модель топологии, подходящую для ваших телеметрических данных.") для ряда сервисов Google Cloud.

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

Обратите внимание, что названия измерений метрик изменятся при переходе на интеграцию Google Cloud с использованием Dynatrace Extensions 2.0. Изменения названий измерений затрагивают все настроенные зоны управления, пользовательские оповещения и пользовательские дашборды в вашей среде. Чтобы восстановить правильную работу этих сущностей, следуйте приведённым ниже инструкциям.

Обновление существующих установок `dynatrace-gcp-monitor` с более ранних версий не поддерживается. Необходимо сначала удалить существующее развёртывание, а затем установить интеграцию Google Cloud v.1.0. Инструкции приведены ниже.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Удаление существующего развёртывания**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#delete-deployment "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 на Kubernetes и в виде Google Cloud Function.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Удаление дашбордов и/или оповещений**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#remove-dashboards "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 на Kubernetes и в виде Google Cloud Function.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Установка нового развёртывания Google Cloud**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#install-deployment "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 на Kubernetes и в виде Google Cloud Function.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Обновление измерений**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#update-dimensions "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 на Kubernetes и в виде Google Cloud Function.")

## Шаг 1 Удаление существующего развёртывания

Для контейнерного развёртывания на Kubernetes

Для развёртывания GC Function

1. Узнайте, какую версию релиза вы используете.

   ```
   helm ls -n dynatrace
   ```
2. Удалите релиз.

   Обязательно замените `<release-name>` на название релиза из предыдущего вывода.

   ```
   helm uninstall <release-name> -n dynatrace
   ```

1. Удалите релиз.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/uninstall.sh -O uninstall.sh ; chmod a+x uninstall.sh ; ./uninstall.sh
```

2. Удалите файл конфигурации сервиса `activation-config.yaml`.

## Шаг 2 Удаление дашбордов и/или оповещений

Необходимо вручную удалить все дашборды или оповещения, созданные вручную во время предыдущей установки.

## Шаг 3 Установка нового развёртывания Google Cloud

Для установки нового развёртывания Google Cloud см. [Настройка интеграции метрик и логов Dynatrace Google Cloud (v.1.0) на новом кластере GKE Autopilot](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

## Шаг 4 Обновление измерений

Если вы создали собственные дашборды, оповещения или зоны управления на основе метрик Google Cloud, вам необходимо вручную обновить измерения в соответствии с приведённым ниже списком, чтобы получить ссылки на сущности.

### Список изменений измерений

| Старое название измерения | Новое название измерения |
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

* Для обновления измерений в дашбордах

  1. Перейдите в ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
  2. Выберите дашборд, для которого хотите обновить измерения, а затем выберите **More** (**...**) > **Configure**.
  3. Выберите **Dashboard JSON**.
  4. В разделе `"splitBy"` замените старые измерения на новые значения в соответствии со [списком изменений измерений](#dimension).
  5. Выберите **Save changes**.

Также можно заменить измерения, настроив каждую плитку дашборда выбранного дашборда в Data Explorer.

* Для обновления измерений в оповещениях

  1. Перейдите в **Settings**.
  2. Выберите **Anomaly detection** > **Metric events**.
  3. Выберите событие, для которого хотите обновить измерения.
  4. В поле **Add dimension filter** выберите новые ключи измерений и введите соответствующие значения измерений в соответствии со [списком изменений измерений](#dimension).
  5. Выберите **Save changes**.
* Для обновления измерений в зонах управления

  1. Перейдите в **Settings**.
  2. Выберите **Preferences** > **Management zones**.
  3. Выберите **Edit** для зоны управления, для которой хотите обновить измерения.
  4. Выберите **Edit** для редактирования существующего правила.
  5. В **Conditions** отредактируйте значение `DIMENSION` в соответствии со [списком изменений измерений](#dimension).
  6. Выберите **Save changes**.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/docs/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
