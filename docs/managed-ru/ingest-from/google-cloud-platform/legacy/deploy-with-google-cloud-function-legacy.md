---
title: Развёртывание интеграции метрик Dynatrace Google Cloud с использованием Google Cloud Function (устаревшее)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy
scraped: 2026-05-12T12:08:49.693134
---

# Развёртывание интеграции метрик Dynatrace Google Cloud с использованием Google Cloud Function (устаревшее)

# Развёртывание интеграции метрик Dynatrace Google Cloud с использованием Google Cloud Function (устаревшее)

* Практическое руководство
* Чтение: 5 мин
* Опубликовано 12 марта 2021 г.
* Устаревшее

На этой странице описывается установка Google Cloud Function версии 0.1, которая запланирована к устареванию.

* Для новой установки следует [развернуть Google Cloud Function версии 1.0](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Настройка мониторинга сервисов Google Cloud с помощью Google Cloud Functions.").
* Если Google Cloud Function версии 0.1 уже установлена, следует [выполнить миграцию на Google Cloud Function версии 1.0](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.").

## Установка

Для настройки интеграции Dynatrace в виде Google Cloud Function следуйте инструкциям ниже.

Развёртывание в Google Cloud Shell

Развёртывание в bash

### Предварительные условия

* [Установите yq версии 4.9.8](https://dt-url.net/411p0nlq)
  **Пример команды для установки yq:**

  ```
  sudo wget https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64 -O /usr/bin/yq && sudo chmod +x /usr/bin/yq
  ```
* [Установите jq](https://dt-url.net/cl1203zc)
* [Создайте API-токен](https://dt-url.net/be03q3a)
* [Включите следующие разрешения для API-токена](https://dt-url.net/c023q1m): `Ingest metrics` (API v2), `Read configuration` (API v1) и `Write configuration` (API v1)
* Определите URL вашей среды.

  + Для Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/`
  + Для Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/`

  Чтобы определить `<your-environment-id>`, см. [идентификатор среды](https://dt-url.net/ej43qge).
* Для запуска скрипта развёртывания требуется набор разрешений. Можно создать пользовательскую роль (инструкция ниже) и использовать её для развёртывания `dynatrace-gcp-monitor`.

1. Создайте YAML-файл с именем `dynatrace-gcp-monitor-cloud-function-deployment-role.yaml` со следующим содержимым:

dynatrace-gcp-monitor-cloud-function-deployment-role.yaml

```
title: Dynatrace GCP Monitor cloud function deployment role



description: Role for Dynatrace GCP Monitor cloud function deployment



stage: GA



includedPermissions:



- appengine.applications.get



- appengine.applications.create



- cloudfunctions.functions.create



- cloudfunctions.functions.get



- cloudfunctions.functions.list



- cloudfunctions.functions.sourceCodeSet



- cloudfunctions.functions.update



- cloudfunctions.functions.getIamPolicy



- cloudfunctions.operations.get



- cloudfunctions.operations.list



- cloudscheduler.locations.list



- cloudscheduler.jobs.list



- cloudscheduler.jobs.create



- cloudscheduler.jobs.get



- cloudscheduler.jobs.delete



- pubsub.topics.list



- pubsub.topics.create



- pubsub.topics.update



- secretmanager.secrets.list



- secretmanager.versions.add



- secretmanager.secrets.create



- secretmanager.versions.list



- secretmanager.secrets.getIamPolicy



- secretmanager.secrets.setIamPolicy



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- iam.serviceAccounts.actAs



- iam.serviceAccounts.list



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.setIamPolicy



- iam.roles.list



- iam.roles.create



- iam.roles.update



- monitoring.dashboards.list



- monitoring.dashboards.create
```

2. Выполните приведённую ниже команду, заменив `<your_project_ID>` на идентификатор проекта, в котором нужно развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.cloud_function_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-cloud-function-deployment-role.yaml
```

Обязательно добавьте эту роль своему пользователю GCP.

Для развёртывания функции Dynatrace GCP в Google Cloud Shell загрузите и запустите скрипт установки ниже, заменив `<VERSION>` на нужную версию релиза, например `0.1.19`.

Обязательно выбирайте версию, выпущенную до `release-1.0.0`, так как более новые версии требуют [других инструкций по установке](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/setup.sh" -O setup.sh; chmod a+x *.sh; ./setup.sh
```

Dynatrace GCP Monitor использует [Cloud Scheduler](https://dt-url.net/n483qgj), которому требуется приложение App Engine. Если App Engine не установлен, скрипт установки предложит создать его и выбрать регион, в котором будет выполняться скрипт.

Скрипт установки запросит следующие параметры:

* **GCP project ID**: идентификатор проекта Google Cloud, в котором нужно развернуть Dynatrace GCP Monitor. По умолчанию используется текущий идентификатор проекта из gcloud CLI.
* **Function size**: объём памяти для выделения функции. Доступные варианты:

  + `[s]`: Small (выделяет 256 МБ памяти функции). Выберите этот вариант, если у вас до 500 экземпляров сервисов GCP.
  + `[m]`: Medium (выделяет 512 МБ памяти функции). Выберите этот вариант, если у вас до 1000 экземпляров сервисов GCP.
  + `[l]`: Large (выделяет 2048 МБ памяти функции). Выберите этот вариант, если у вас до 5000 экземпляров сервисов GCP.

    Объём памяти можно изменить после установки.
* **Dynatrace tenant URI**: URL вашей среды Dynatrace. Подробнее см. в разделе **Предварительные условия**.
* **Dynatrace API token**: ваш API-токен Dynatrace. Подробнее см. в разделе **Предварительные условия**.

### Предварительные условия

* [Установите jq](https://dt-url.net/cl1203zc)
* [Установите yq 4.9.x](https://dt-url.net/411p0nlq)
  **Пример команды для установки yq:**

  ```
  sudo wget https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64 -O /usr/bin/yq && sudo chmod +x /usr/bin/yq
  ```
* [Установите Google Cloud SDK](https://dt-url.net/e8110336)
* [Создайте API-токен](https://dt-url.net/be03q3a)
* [Включите разрешения `Ingest metrics`, `Read configuration` и `Write configuration` для API-токена](https://dt-url.net/c023q1m)
* Определите URL вашей среды.

**Для SaaS:**
`https://<your-environment-id>.live.dynatrace.com/`

**Для Managed:**
`https://<your-domain>/e/<your-environment-id>/`

Чтобы определить `<your-environment-id>`, см. [идентификатор среды](https://dt-url.net/ej43qge).

* Для запуска скрипта развёртывания требуется набор разрешений. Можно создать пользовательскую роль (инструкция ниже) и использовать её для развёртывания `dynatrace-gcp-monitor`.

1. Создайте YAML-файл с именем `dynatrace-gcp-monitor-cloud-function-deployment-role.yaml` со следующим содержимым:

dynatrace-gcp-monitor-cloud-function-deployment-role.yaml

```
title: Dynatrace GCP Monitor cloud function deployment role



description: Role for Dynatrace GCP Monitor cloud function deployment



stage: GA



includedPermissions:



- appengine.applications.get



- appengine.applications.create



- cloudfunctions.functions.create



- cloudfunctions.functions.get



- cloudfunctions.functions.list



- cloudfunctions.functions.sourceCodeSet



- cloudfunctions.functions.update



- cloudfunctions.functions.getIamPolicy



- cloudfunctions.operations.get



- cloudfunctions.operations.list



- cloudscheduler.locations.list



- cloudscheduler.jobs.list



- cloudscheduler.jobs.create



- cloudscheduler.jobs.get



- cloudscheduler.jobs.delete



- pubsub.topics.list



- pubsub.topics.create



- pubsub.topics.update



- secretmanager.secrets.list



- secretmanager.versions.add



- secretmanager.secrets.create



- secretmanager.versions.list



- secretmanager.secrets.getIamPolicy



- secretmanager.secrets.setIamPolicy



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- iam.serviceAccounts.actAs



- iam.serviceAccounts.list



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.setIamPolicy



- iam.roles.list



- iam.roles.create



- iam.roles.update



- monitoring.dashboards.list



- monitoring.dashboards.create
```

2. Выполните приведённую ниже команду, заменив `<your_project_ID>` на идентификатор проекта, в котором нужно развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.cloud_function_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-cloud-function-deployment-role.yaml
```

Обязательно добавьте эту роль своему пользователю GCP.

Для развёртывания функции Dynatrace GCP в bash

1. Перезапустите консоль и [инициализируйте Cloud SDK](https://dt-url.net/ac43q0f).

```
gcloud init
```

2. Загрузите и запустите скрипт установки ниже.

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/setup.sh" -O setup.sh; chmod a+x *.sh; ./setup.sh
```

Dynatrace GCP Monitor использует [Cloud Scheduler](https://dt-url.net/n483qgj), которому требуется приложение App Engine. Если App Engine не установлен, скрипт установки предложит создать его и выбрать регион, в котором будет выполняться скрипт.

Скрипт установки запросит следующие параметры:

* **GCP project ID**: идентификатор проекта Google Cloud, в котором нужно развернуть Dynatrace GCP Monitor. По умолчанию используется текущий идентификатор проекта из gcloud CLI.
* **Function size**: объём памяти для выделения функции. Доступные варианты:

  + `[s]`: Small (выделяет 256 МБ памяти функции). Выберите этот вариант, если у вас до 500 экземпляров сервисов GCP.
  + `[m]`: Medium (выделяет 512 МБ памяти функции). Выберите этот вариант, если у вас до 1000 экземпляров сервисов GCP.
  + `[l]`: Large (выделяет 2048 МБ памяти функции). Выберите этот вариант, если у вас до 5000 экземпляров сервисов GCP.

    Объём памяти можно изменить после установки.
* **Dynatrace tenant URI**: URL вашей среды Dynatrace. Подробнее см. в разделе **Предварительные условия**.
* **Dynatrace API token**: ваш API-токен Dynatrace. Подробнее см. в разделе **Предварительные условия**.

После развёртывания интеграции доступны метрики отслеживаемых сервисов. Чтобы добавить сервисы в мониторинг, см. раздел [Расширение мониторинга](#expand) ниже.

## Проверка установки

Чтобы проверить успешность установки

1. В консоли Google Cloud перейдите в Cloud Functions и убедитесь, что `dynatrace-gcp-monitor` присутствует.
2. Выберите только что развёрнутую функцию и перейдите в раздел **Logs**, чтобы убедиться в отсутствии сообщений об ошибках.

## Расширение мониторинга

Добавить сервисы в мониторинг Dynatrace при использовании Google Cloud Function можно двумя способами: через файл конфигурации сервиса или через консоль GCP. Инструкции приведены ниже.

В файле конфигурации сервиса

В консоли Google Cloud

Чтобы добавить сервисы через файл конфигурации сервиса

1. Загрузите файл конфигурации сервиса `activation-config.yaml`, заменив `<VERSION>` на версию релиза вашей функции.

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/dynatrace-gcp-monitor.zip" -O dynatrace-gcp-monitor.zip; unzip -p dynatrace-gcp-monitor.zip activation-config.yaml >activation-config.yaml
```

2. Отредактируйте раздел `activation.metrics.services` в файле `activation-config.yaml`, раскомментировав сервисы, которые нужно отслеживать.
3. Загрузите и запустите скрипт установки `dynatrace-gcp-monitor` в той же папке, куда был загружен файл `activation-config.yaml`.

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/setup.sh" -O setup.sh; chmod a+x *.sh; ./setup.sh
```

Чтобы добавить сервисы через консоль Google Cloud

1. Перейдите в **Cloud Functions**
2. Выберите **dynatrace-gcp-monitor**
3. Выберите **Edit**
4. В разделе **Variables, networking and advanced settings** выберите **Environment variables**
5. Выберите **Runtime environment variables**
6. Измените значение параметра **GCP services**, добавив нужные сервисы или конфигурации (например, `cloud_function`, `gce_instance/agent`).
7. Выберите **Next**, затем **Deploy**

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")