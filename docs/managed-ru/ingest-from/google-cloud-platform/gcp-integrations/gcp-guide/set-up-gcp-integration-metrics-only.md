---
title: Настройка интеграции метрик Dynatrace с Google Cloud на кластере GKE
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only
scraped: 2026-05-12T11:51:42.751874
---

# Настройка интеграции метрик Dynatrace с Google Cloud на кластере GKE

# Настройка интеграции метрик Dynatrace с Google Cloud на кластере GKE

* Практическое руководство
* Чтение: 15 мин
* Обновлено 08 октября 2024 г.

Dynatrace версии 1.230+

В качестве альтернативы [основному развёртыванию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."), которое обеспечивает мониторинг Google Cloud и метрик, и логов, можно настроить мониторинг только метрик. В этом сценарии скрипт развёртывания запускается в Google Cloud Shell. Инструкции зависят от того, где будет выполняться скрипт развёртывания:

* На новом кластере GKE Autopilot, созданном автоматически (рекомендуется)
* На существующем стандартном кластере GKE или кластере GKE Autopilot

В процессе настройки GKE запустит контейнер для пересылки метрик. После установки в Dynatrace станут доступны метрики, дашборды и оповещения для настроенных сервисов.

Другие варианты развёртывания см. в разделе [Альтернативные сценарии развёртывания](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

На этой странице описана установка интеграции Google Cloud версии 1.0 на кластере GKE.

* Если установлена [более ранняя версия](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes."), необходимо выполнить [миграцию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция интеграции Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.").

## Ограничения

Интеграция метрик Dynatrace с Google Cloud поддерживает до 50 проектов Google Cloud при стандартном развёртывании. Для мониторинга более крупных окружений необходимо включить область видимости метрик. См. [Мониторинг нескольких проектов Google Cloud: крупные окружения](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик из нескольких проектов Google Cloud в Dynatrace.").

## Предварительные требования

Для развёртывания интеграции необходимо убедиться, что на машине, с которой выполняется установка, выполнены следующие требования.

* Только Linux
* Доступ к интернету
* Доступ к кластеру GKE
* Доступ к окружению Dynatrace

  Необходимо настроить эндпоинт Dynatrace (URL окружения, кластера или ActiveGate), на который кластер GKE будет отправлять метрики и логи. Убедитесь в наличии прямого сетевого доступа или в том, что промежуточные компоненты (прокси и другие) не влияют на соединение.

### Инструменты

Интеграцию Dynatrace GCP можно развернуть в Google Cloud Shell или в bash.

При использовании bash необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* [helm](https://helm.sh/docs/intro/install/)
* [jq (версия 1.6)](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (версия 4.9.x+)](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Разрешения Google Cloud

Для запуска скрипта развёртывания требуется набор разрешений. Необходимо создать пользовательскую роль (см. ниже) и использовать её для развёртывания `dynatrace-gcp-monitor`.

1. Создайте YAML-файл с именем `dynatrace-gcp-monitor-helm-deployment-role.yaml` со следующим содержимым:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Каждая группа разрешений предназначена для управления различными ресурсами интеграции: создание и доступ для новых ресурсов, обновление для повторного использования существующих, удаление для деинсталляции.

* container.configMaps: для сопоставления секретов и других переменных, используемых контейнерами.
* container.deployments: для развёртывания K8s в кластере (включая поды, контейнеры и т.д.).
* container.namespaces: для пространства имён K8s, в котором развёртываются ресурсы.
* container.pods: для подов K8s.
* container.secrets: для секретов K8s, в которых хранятся конфиденциальные данные.
* container.serviceAccounts: для service account в контексте K8s.
* iam.roles: для необходимых разрешений сбора метрик.
* iam.serviceAccounts: для service account в общем контексте.
* resourcemanager.projects: для управления проектом, в котором развёртывается интеграция.
* serviceusage.services: для управления API сервисов.

2. Выполните команду ниже, заменив `<your_project_ID>` на ID проекта, в котором нужно развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно добавьте эту роль своему пользователю Google Cloud. Подробнее см. [Предоставление или отзыв отдельной роли](https://dt-url.net/vx03vid).

### Настройки Google Cloud

Место развёртывания интеграции определяет, нужно ли изменять дополнительные настройки.

#### Развёртывание на кластере GKE Autopilot

При развёртывании интеграции на существующем кластере GKE Autopilot или на новом кластере Autopilot, который будет создан автоматически скриптом развёртывания, никаких дополнительных настроек не требуется.

#### Развёртывание на стандартном кластере GKE

При развёртывании интеграции на существующем стандартном кластере GKE необходимо:

* [Включить Workload Identity на кластере.](https://dt-url.net/2j23qqv)
* [Включить `GKE_METADATA` на пулах узлов GKE.](https://dt-url.net/an43q2s)

### Разрешения Dynatrace

Необходимо создать токен с набором разрешений.

1. Перейдите в **Access tokens**.
2. Выберите **Generate new token**.
3. Введите имя токена.
4. В разделе **Template** выберите `GCP Services Monitoring`.
5. Выберите **Generate**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Также можно создать токен и добавить разрешения вручную.

Добавить вручную

[Создайте API-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях видимости.") и [включите следующие разрешения](/managed/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Узнайте, как пройти аутентификацию для работы с API Dynatrace."):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extensions monitoring configuration**
  + **Write extensions monitoring configuration**
  + **Read extensions environment configuration**
  + **Write extensions environment configuration**
  + **Manage metadata of Hub items**
  + **Read Hub related data**
  + **Install and update Hub items**

## Установка

Выполните приведённые ниже шаги для завершения настройки.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Скачайте пакет развёртывания Helm в Google Cloud Shell**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#dwld "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте значения параметров**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#params "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Подключите кластер Kubernetes**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#connect "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Запустите скрипт развёртывания**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#script "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")

### Шаг 1 Скачайте пакет развёртывания Helm в Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Настройте значения параметров

1. Пакет развёртывания Helm содержит файл `values.yaml` с необходимой конфигурацией. Перейдите в `helm-deployment-package/dynatrace-gcp-monitor` и отредактируйте файл `values.yaml`, задав обязательные и необязательные параметры следующим образом.

   Рекомендуется сохранить этот файл в надёжном месте для последующих обновлений: он потребуется при повторных развёртываниях. Учтите, что схема файла может измениться; в этом случае используйте новый файл и перенесите в него только значения параметров.

   | **Имя параметра** | **Описание** | **Значение по умолчанию** |
   | --- | --- | --- |
   | `gcpProjectId` | Обязательный. ID проекта Google Cloud, выбранного для развёртывания. | Текущий ID проекта |
   | `deploymentType` | Обязательный. Установите значение `metrics`. | `all` |
   | `dynatraceAccessKey` | Обязательный. Ваш [API-токен Dynatrace](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях видимости.") с [необходимыми разрешениями](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."). |  |
   | `dynatraceAccessKeySecretName` | Необязательный. Можно указать ключ для получения эндпоинта из Google Cloud Secret Manager вместо `dynatraceAccessKey`. |  |
   | `dynatraceUrlSecretName` | Необязательный. Можно указать ключ для получения эндпоинта из Google Cloud Secret Manager вместо `dynatraceUrl`. |  |
   |  |  |  |
   | `dynatraceUrl` | Обязательный. Для приёма логов Managed используется URL кластера (`https:/<your_cluster_IP_or_hostname>/e/<your_environment_ID>`). Для приёма логов Managed с существующим ActiveGate используется URL ActiveGate (`https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`). **Примечание:** для определения `<your-environment-id>` см. [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как работать с окружениями мониторинга."). |  |
   | `requireValidCertificate` | Необязательный. Если установлено значение `true`, Dynatrace требует SSL-сертификат окружения. Для приёма логов Managed с новым ActiveGate рекомендуется установить значение `false`. | `true` |
   | `selfMonitoringEnabled` | Необязательный. Отправляет пользовательские метрики в Google Cloud для быстрой диагностики корректности обработки и отправки логов в Dynatrace. Подробнее см. [Метрики самомониторинга для интеграции Dynatrace с Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Проверьте, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace."). | `false` |
   | `serviceAccount` | Необязательный. Имя создаваемого service account. |  |
   | `dockerImage` | Необязательный. Docker-образ Dynatrace Google Cloud Monitor. Рекомендуется использовать значение по умолчанию, но при необходимости его можно изменить. | `dynatrace/dynatrace-gcp-monitor:v1-latest` |
   | `printMetricIngestInput` | Необязательный. Если установлено значение `true`, Google Cloud Monitor выводит строки метрик в stdout. | `false` |
   | `serviceUsageBooking` | Необязательный. Используется для метрик и определяет проект для квоты и биллинга. При значении `source` вызовы API мониторинга тарифицируются в проекте, где работает контейнер Kubernetes. При значении `destination` вызовы тарифицируются в отслеживаемом проекте. Подробнее см. [Мониторинг нескольких проектов Google Cloud: стандартные окружения, шаг 4](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик из нескольких проектов Google Cloud в Dynatrace."). | `source` |
   | `useProxy` | Необязательный. В зависимости от значения флага Google Cloud Monitor использует следующие настройки прокси: Dynatrace (значение `DT_ONLY`), Google Cloud API (значение `GCP_ONLY`) или оба (значение `ALL`). | По умолчанию настройки прокси не используются. |
   | `httpProxy` | Необязательный. HTTP-адрес прокси; используйте совместно с `USE_PROXY`. |  |
   | `httpsProxy` | Необязательный. HTTPS-адрес прокси; используйте совместно с `USE_PROXY`. |  |
   | `gcpServicesYaml` | Необязательный. Конфигурационный файл для сервисов Google Cloud. |  |
   | `queryInterval` | Необязательный. Интервал опроса метрик в минутах. Допустимые значения: от `1` до `6`. | `3` |
   | `scopingProjectSupportEnabled` | Необязательный. Установите `true`, если настроена область видимости метрик: в этом случае метрики будут собираться со всех проектов, добавленных в область видимости. Подробнее см. [Мониторинг нескольких проектов Google Cloud: крупные окружения](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик из нескольких проектов Google Cloud в Dynatrace."). | `false` |
   | `excludedProjects` | Необязательный. Список проектов, исключённых из мониторинга, через запятую (например, `<project_A>,<project_B>`). |  |
   | `excludedMetricsAndDimensions` | Необязательный. Список метрик и их измерений для исключения из мониторинга в формате YAML. |  |
   | `metricAutodiscovery` | Необязательный. Если установлено значение `true`, Google Cloud Monitor запускается в режиме автоматического обнаружения метрик, расширяя возможности выбора отслеживаемых метрик. Подробнее см. [Мониторинг проектов Google Cloud с автообнаружением](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Отправка любых метрик Google Cloud в Dynatrace."). |  |
   | `clusterIpv4Cidr` | Необязательный. Задайте диапазон IP-адресов для подов кластера в нотации CIDR, если требуется пользовательский диапазон. |  |
   | `servicesIpv4Cidr` | Необязательный. Задайте диапазон IP-адресов для сервисов. Можно указать в виде размера маски сети или в нотации CIDR. |  |
   | `useCustomMasterCidr` | Необязательный. Если установлено значение `true`, можно задать диапазон IPv4 CIDR для сети master. | `false` |
   | `masterIpv4Cidr` | Необязательный. Диапазон IPv4 CIDR для сети master; требует, чтобы `useCustomMasterCidr` было установлено в `true`. |  |
2. Выберите сервисы, которые Dynatrace будет отслеживать.

   По умолчанию интеграция Dynatrace с Google Cloud начинает мониторинг набора выбранных сервисов. Список поддерживаемых сервисов см. в разделе [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик.").

Информацию о потреблении DDU см. в разделе [Потребление при мониторинге](#ddu).

### Шаг 3 Подключите кластер Kubernetes

* Чтобы скрипт развёртывания создал новый кластер GKE Autopilot, добавьте в скрипт `--create-autopilot-cluster`. Подключение к кластеру будет настроено автоматически; можно сразу перейти к [шагу 4](#script).
* При запуске скрипта развёртывания на существующем стандартном кластере GKE или кластере GKE Autopilot подключиться к нему можно через консоль Google Cloud или через терминал. Следуйте инструкциям ниже.

Из консоли Google Cloud

Через терминал

1. В консоли Google Cloud перейдите в Kubernetes Engine.
2. Выберите **Clusters**, затем выберите **Connect**.
3. Выберите **Run in Cloud Shell**.

Выполните команду ниже, обязательно заменив

* `<cluster>` на имя кластера
* `<region>` на регион, в котором работает кластер
* `<project>` на ID проекта, в котором работает кластер

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

Подробнее см. [Настройка доступа к кластеру для kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Шаг 4 Запустите скрипт развёртывания

* При запуске скрипта развёртывания на существующем стандартном кластере GKE или кластере GKE Autopilot скрипт создаст IAM service account с необходимыми ролями и развернёт `dynatrace-gcp-monitor` в кластере Kubernetes.
* При запуске скрипта с параметром `--create-autopilot-cluster` будет автоматически создан новый кластер GKE Autopilot и в нём развёрнут `dynatrace-gcp-monitor`.

Для запуска скрипта развёртывания следуйте инструкциям ниже.

Запуск на существующем кластере

Запуск на новом кластере

Будут загружены последние версии расширений Google Cloud. Доступны два варианта:

* Запустите скрипт без параметров, чтобы использовать значения по умолчанию (`dynatrace-gcp-monitor-sa` в качестве имени IAM service account и `dynatrace_monitor` в качестве префикса имени IAM-роли):

```
cd helm-deployment-package



./deploy-helm.sh
```

* Запустите скрипт с параметрами, чтобы задать собственные значения (обязательно замените плейсхолдеры на нужные значения):

```
cd helm-deployment-package



./deploy-helm.sh [--role-name <role-to-be-created/updated>]
```

Чтобы сохранить существующие версии установленных расширений и установить последние версии остальных выбранных расширений (если они не установлены), выполните вместо этого следующую команду.

```
cd helm-deployment-package



./deploy-helm.sh --without-extensions-upgrade
```

Выполните команду ниже. Будут загружены последние версии расширений.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster
```

Чтобы задать другое имя нового кластера, выполните вместо этого следующую команду, заменив плейсхолдер (`<name-of-new-cluster>`) на нужное имя.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

Чтобы сохранить существующие версии установленных расширений и установить последние версии остальных выбранных расширений (если они не установлены), выполните вместо этого следующую команду.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Проверка установки

Для проверки успешности установки

1. Проверьте, работает ли контейнер.

   После установки может пройти несколько минут, прежде чем контейнер запустится.

   ```
   kubectl -n dynatrace get pods
   ```
2. Проверьте логи контейнера на наличие ошибок или исключений. Доступны два варианта:

В Kubernetes CLI

В консоли Google Cloud

Выполните следующую команду.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics
```

Для проверки логов контейнера в консоли Google Cloud

1. Перейдите в **Logs explorer**.
2. Используйте фильтры ниже для получения логов приёма метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"`

3. Проверьте, импортированы ли дашборды.

   Перейдите в **Dashboards** и отфильтруйте по тегу `Google Cloud`. Должен быть доступен набор дашбордов для сервисов Google Cloud.

## Выбор сервисов для мониторинга метрик

### Сервисы, включённые по умолчанию

В процессе развёртывания Google Cloud Monitor будет включён мониторинг следующих сервисов:

* [Google APIs](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Мониторинг Google Cloud APIs и просмотр доступных метрик.")
* [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Мониторинг Google App Engine и просмотр доступных метрик.")
* [Google BigQuery](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Мониторинг Google BigQuery и просмотр доступных метрик.")
* [Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Мониторинг Google Cloud Functions и просмотр доступных метрик.")
* [Google Cloud Run](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Мониторинг Google Cloud Run и просмотр доступных метрик.")
* [Google Cloud Storage](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Мониторинг Google Cloud Storage и просмотр доступных метрик.")
* [Google Compute Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Мониторинг Google Compute Engine и просмотр доступных метрик.")
* [Google Firestore in Datastore mode](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Мониторинг Google Cloud Firestore в режиме Datastore и просмотр доступных метрик.")
* [Google Filestore](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Мониторинг Google Filestore и просмотр доступных метрик.")
* [Google Kubernetes Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Мониторинг Google Kubernetes Engine и просмотр доступных метрик.")
* [Google Cloud Load Balancing](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Мониторинг Google Cloud Load Balancing и просмотр доступных метрик.")
* [Google Cloud Pub/Sub](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Мониторинг Google Cloud Pub/Sub и просмотр доступных метрик.")
* [Google Cloud Pub/Sub Lite](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Мониторинг Google Cloud Pub/Sub Lite и просмотр доступных метрик.")
* [Google Cloud SQL](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Мониторинг Google Cloud SQL и просмотр доступных метрик.")

Доступны и другие интеграции с сервисами, которые нужно включить отдельно. Список поддерживаемых сервисов см. в разделе [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик."). В следующем разделе описывается управление сервисами. Для расширения охвата метрик рассмотрите также [автообнаружение](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Отправка любых метрик Google Cloud в Dynatrace.").

### Управление включёнными сервисами

Управление включёнными сервисами выполняется через Dynatrace Hub.

Отфильтруйте по «gcp»: в результатах будут аннотации для элементов, уже доступных в вашем окружении.

Чтобы включить новый сервис, выберите его в Hub и установите.

Сервис также можно отключить через Dynatrace Hub.

Чтобы проверить наличие обновлений для сервисов, откройте их в Hub и просмотрите примечания к выпуску. Обновления могут включать новые метрики, новые ресурсы (дашборды) и другие изменения.

Все изменения включённых сервисов применяются в Google Cloud Monitor в течение нескольких минут.

#### Наборы функций и доступные метрики

Чтобы узнать, какие метрики доступны для конкретного сервиса, см. раздел [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик."). По умолчанию включён только набор функций `defaultMetrics`. Для включения дополнительных наборов раскомментируйте их в файле `values.yaml` и повторно разверните Google Cloud Monitor.

Текущая конфигурация наборов функций содержится в ConfigMap кластера с именем `dynatrace-gcp-function-config`.

#### Расширенное управление областью мониторинга

Для дополнительной настройки области мониторинга используйте поле `filter_conditions` в файле `values.yaml`. Для этого потребуется повторное развёртывание Google Cloud Monitor. Синтаксис фильтров см. в разделе [Фильтры Google Cloud Monitoring](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).

Пример:

```
filter_conditions:



resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Включение оповещений

Для активации оповещений необходимо включить метрические события в Dynatrace.

Чтобы включить метрические события

1. Перейдите в **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте оповещения Google Cloud и включите нужные с помощью переключателя **On/Off**.

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов доступны в разделе **Metrics** (отфильтруйте по `gcp`).

## Изменение параметров развёртывания

### Изменение параметров из `values.yaml`

Для загрузки нового файла `values.yaml` необходимо обновить Helm-релиз.

Чтобы обновить Helm-релиз

1. Определите текущую версию Helm-релиза.

   ```
   helm ls -n dynatrace
   ```
2. Выполните команду ниже, заменив `<your-helm-release>` на значение из предыдущего шага.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

Подробнее см. [Helm upgrade](https://helm.sh/docs/helm/helm_upgrade/).

### Изменение типа развёртывания

Чтобы изменить тип развёртывания (`all`, `metrics` или `logs`)

1. Определите текущую версию Helm-релиза.

   ```
   helm ls -n dynatrace
   ```
2. Удалите релиз.

   Обязательно замените `<your-helm-release>` на имя релиза из предыдущего вывода.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Измените значение `deploymentType` в `values.yaml` на новое и сохраните файл.
4. Запустите команду развёртывания повторно. Подробнее см. [Запустите скрипт развёртывания](#script).

## Диагностика

Для диагностики возможных проблем с развёртыванием и подключением

1. [Проверьте установку](#verify)
2. [Включите самомониторинг](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Проверьте, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.") (необязательно)
3. Проверьте лог-файл `dynatrace_gcp_<date_time>.log`, созданный в процессе установки.

* Этот файл создаётся при каждом запуске скрипта установки.
* Отладочная информация не содержит конфиденциальных данных, таких как токен доступа Dynatrace.
* При обращении к специалисту Dynatrace через чат:

  + Предоставьте лог-файл `dynatrace_gcp_<date_time>.log`, описанный в предыдущем пункте.
  + Предоставьте информацию о версии.

    - При проблемах во время установки проверьте файл `version.txt`.
    - При проблемах во время работы [проверьте логи контейнера](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Проверьте, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.").

## Удаление

1. Определите текущую версию Helm-релиза.

```
helm ls -n dynatrace
```

2. Удалите релиз.

Обязательно замените `<your-helm-release>` на имя релиза из предыдущего вывода.

```
helm uninstall <your-helm-release> -n dynatrace
```

Также можно удалить пространство имён.

```
kubectl delete namespace dynatrace
```

3. Для удаления всех ресурсов мониторинга (дашбордов, оповещений) из Dynatrace необходимо удалить все расширения Google Cloud.

Нужные расширения можно найти и удалить через Dynatrace Hub.

Обязательно удалите исходную роль, созданную и привязанную к service account, использованному для развёртывания интеграции.

## Потребление при мониторинге

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики соответствует приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. [Расширение Dynatrace (единицы данных Davis)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).").

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)