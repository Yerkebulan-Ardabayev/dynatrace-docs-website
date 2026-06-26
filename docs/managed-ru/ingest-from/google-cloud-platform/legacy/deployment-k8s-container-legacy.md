---
title: Настройка интеграции GCP метрик и/или логов Dynatrace в контейнере Kubernetes (устаревшее)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy
scraped: 2026-05-12T12:08:47.584627
---

# Настройка интеграции GCP метрик и/или логов Dynatrace в контейнере Kubernetes (устаревшее)

# Настройка интеграции GCP метрик и/или логов Dynatrace в контейнере Kubernetes (устаревшее)

* Практическое руководство
* Чтение: 16 мин
* Опубликовано 12 марта 2021 г.
* Устарело

На этой странице описана установка версии 0.1 интеграции GCP в контейнере Kubernetes, которая готовится к выводу из эксплуатации.

* При новой установке используйте [развёртывание интеграции GCP метрик и/или логов (версия 1.0) в контейнере Kubernetes](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").
* Если версия 0.1 интеграции GCP уже установлена, выполните [миграцию на версию 1.0](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция с версии 0.1 на версию 1.0 интеграции Google Cloud в Kubernetes и в виде Google Cloud Function.").

Для приёма метрик и/или логов из Google Cloud необходимо развернуть контейнер в GKE (также работает в Google Autopilot). После развёртывания доступны метрики сервисов, определённых в configmap, преднастроенные дашборды и предопределённые оповещения.

## Настройка общего приёма логов (необязательно)

Для полной наблюдаемости рабочих нагрузок настройте общий приём логов до установки. Это требует дополнительной конфигурации и второго контейнера для пересылки логов. Инструкции см. ниже.

1. Создайте топик Pub/Sub и добавьте к нему подписку. Это можно сделать двумя способами:

   В консоли Google Cloud

   [Создайте топик Pub/Sub](https://dt-url.net/zp03r4n) и [добавьте к нему подписку](https://dt-url.net/5c23r4h).

   При редактировании подписки рекомендуются следующие значения:

   * **Acknowledgement deadline:** `120` секунд
   * **Message retention duration:** `1` день
   * **Retain acknowledged messages:** не выбрано

   В Google Cloud Shell

   Выполните следующий shell-скрипт в проекте GCP, выбранном для развёртывания.

   Обязательно замените `<your-subscription-name>` и `<your-topic-name>` своими значениями.

   ```
   wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



   chmod +x deploy-pubsub.sh



   ./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
   ```
2. Настройте [экспорт логов](https://dt-url.net/4743r02) для отправки нужных логов в топик GCP Pub/Sub, созданный на предыдущем шаге.
3. Если при развёртывании планируется использовать существующий ActiveGate, [настройте ActiveGate для общего приёма логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные логов и каковы возможные ограничения.").

## Предварительные требования

Для развёртывания Dynatrace GCP Monitor в контейнере Kubernetes убедитесь, что выполнены следующие требования GCP и Dynatrace.

### Требования GCP

#### Разрешения

Выполнение скрипта развёртывания требует ряда разрешений. Создайте пользовательскую роль (см. ниже) и используйте её для развёртывания `dynatrace-gcp-monitor`.

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



- container.replicaSets.create



- container.replicaSets.get



- container.replicaSets.getScale



- container.replicaSets.getStatus



- container.replicaSets.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- container.services.create



- container.services.delete



- container.services.get



- container.statefulSets.create



- container.statefulSets.delete



- container.statefulSets.get



- container.statefulSets.update



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- pubsub.subscriptions.create



- pubsub.subscriptions.get



- pubsub.subscriptions.list



- pubsub.topics.attachSubscription



- pubsub.topics.create



- pubsub.topics.getIamPolicy



- pubsub.topics.list



- pubsub.topics.setIamPolicy



- pubsub.topics.update



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get
```

2. Выполните команду ниже, заменив `<your_project_ID>` идентификатором проекта, в котором нужно развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно добавьте эту роль своему пользователю GCP.

#### Инструменты

При запуске развёртывания из GCP Cloud Shell дополнительные инструменты не требуются.

При запуске развёртывания с любого хоста с bash необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)
* [Kubernetes CLI](https://dt-url.net/ai03q1r)
* [Helm](https://dt-url.net/rh03rrz)

#### Настройки

При развёртывании на существующем стандартном кластере GKE необходимо:

* [Включить Workload Identity на кластере](https://dt-url.net/2j23qqv)
* [Включить `GKE_METADATA` на пулах узлов GKE](https://dt-url.net/an43q2s)

При развёртывании на существующем кластере GKE Autopilot или на новом кластере Autopilot, который будет автоматически создан скриптом развёртывания, дополнительные настройки не требуются.

### Требования Dynatrace

Ознакомьтесь с требованиями к ActiveGate и токенам, описанными ниже.

#### ActiveGate

Для ActiveGate доступны два варианта:

* Создание выделенного ActiveGate скриптом установки (вариант по умолчанию). Рекомендуется
* Использование существующего ActiveGate версии 1.213+. Обязательно

#### Токены

Требования к API и PaaS токенам:

* [Создайте API токен](https://dt-url.net/be03q3a)
* [Включите следующие разрешения для API токена](https://dt-url.net/c023q1m) по необходимости:

  + Для приёма метрик: **Ingest metrics** (API v2), **Read configuration** (API v1), **Write configuration** (API v1)
  + Для приёма логов: **Ingest logs** (API v2)
  + Для приёма логов и метрик: **Ingest logs** (API v2), **Ingest metrics** (API v2), **Read configuration** (API v1), **Write configuration** (API v1)
* [Создайте PaaS токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях.") (если планируется настройка нового ActiveGate при развёртывании)

## Установка

Для установки GCP Monitor в кластере Kubernetes следуйте приведённым ниже инструкциям.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Загрузка helm-пакета развёртывания в Google Cloud Shell**](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy#download-package "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Определение URL для вашей среды**](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy#url "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройка значений параметров**](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy#params "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Подключение кластера Kubernetes**](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy#connect-cluster "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Запуск скрипта**](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy#script "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes.")

### Шаг 1 Загрузка helm-пакета развёртывания в Google Cloud Shell

Загрузите и запустите скрипт установки ниже, заменив `<VERSION>` нужной версией релиза, например `0.1.19`.

Выбирайте версии до `release-1.0.0`, так как более новые версии требуют [других инструкций по установке](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Определение URL для вашей среды

* Для Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com`
* Для Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>`
* Для ActiveGate (при использовании существующего ActiveGate для приёма логов): `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>`

Для определения `<your-environment-id>` см. [идентификатор среды](https://dt-url.net/ej43qge).

### Шаг 3 Настройка значений параметров

Файл `values.yaml`, расположенный в `helm-deployment-package/dynatrace-gcp-monitor`, позволяет задать обязательные и необязательные значения параметров. Полный список доступных параметров интеграции см. ниже.

#### Параметры для приёма метрик и логов (тип развёртывания: all)

| Имя параметра | Описание | Значение по умолчанию |
| --- | --- | --- |
| `gcpProjectId` | Идентификатор проекта GCP, в котором будет развёрнут Dynatrace GCP Monitor. Используйте проект GCP с подпиской Pub/Sub для приёма логов. Подробнее см. [Настройка общего приёма логов](#logingest). | Идентификатор текущего проекта |
| `deploymentType` | Установите значение 'all'. | `all` |
| `dynatraceAccessKey` | Ваш API токен Dynatrace с необходимыми разрешениями в соответствии с выбранным типом развёртывания. Подробнее см. [Требования к токенам](#tokens). |  |
| `activeGate.dynatracePaasToken` | Ваш PaaS токен. Подробнее см. [Требования к токенам](#tokens). |  |
| `dynatraceUrl` | Эндпоинт вашей среды Dynatrace. Подробнее см. [Определение URL для вашей среды](#url). |  |
| `logsSubscriptionId` | Идентификатор подписки Pub/Sub для приёма логов. Подробнее см. [Настройка общего приёма логов](#logingest). |  |

#### Дополнительные необязательные параметры для приёма метрик и логов

Необязательно

| Имя параметра | Описание | Значение по умолчанию |
| --- | --- | --- |
| `activeGate.useExisting` | Установите true, если используется существующий ActiveGate для приёма логов. Подробнее см. [Требования к ActiveGate](#ag). | `false` |
| `dynatraceLogIngestUrl` | Эндпоинт ActiveGate для приёма логов в Dynatrace. Подробнее см. [Определение URL для вашей среды](#url). |  |
| `requireValidCertificate` | При значении `true` Dynatrace требует SSL-сертификат вашей среды Dynatrace. | `true` |
| `selfMonitoringEnabled` | Отправка пользовательских метрик в GCP для быстрой диагностики корректности обработки и отправки метрик/логов в Dynatrace службой `dynatrace-gcp-monitor`. | `false` |
| `dockerImage` | Docker-образ Dynatrace GCP Monitor. Рекомендуется использовать значение по умолчанию, однако при необходимости его можно изменить. | `dynatrace/dynatrace-gcp-monitor` |
| `logIngestContentMaxLength` | Максимальная длина содержимого события лога. Должна быть меньше или равна настройке вашей среды Dynatrace. | `8192` |
| `logIngestAttributeValueMaxLength` | Максимальная длина значения атрибута события лога. При превышении серверного лимита содержимое будет усечено. | `250` |
| `logIngestRequestMaxEvents` | Максимальное число событий лога в одном запросе к эндпоинту приёма логов. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `5000` |
| `logIngestRequestMaxSize` | Максимальный размер (в байтах) одного запроса к эндпоинту приёма логов. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `1048576` |
| `logIngestEventMaxAgeSeconds` | Определяет максимальный возраст пересылаемого события лога. Должно быть меньше или равно настройке вашей среды Dynatrace. | `86400` |
| `printMetricIngestInput` | При значении `true` GCP Monitor выводит строки метрик в stdout. | `false` |
| `serviceUsageBooking` | Учёт использования сервисов применяется для метрик и определяет проект, указанный вызывающей стороной, в целях квот и выставления счетов. При значении `source` вызовы monitoring API учитываются в проекте, где запущен контейнер Kubernetes. При значении `destination` - в отслеживаемом проекте. Подробнее см. [Мониторинг нескольких проектов GCP - Шаг 4](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик в Dynatrace из нескольких проектов Google Cloud."). | `source` |
| `useProxy` | В зависимости от значения этого флага GCP Monitor будет использовать следующие настройки прокси: Dynatrace (значение `DT_ONLY`), GCP API (значение `GCP_ONLY`) или оба варианта (значение `ALL`). | По умолчанию настройки прокси не используются. |
| `httpProxy` | HTTP-адрес прокси; используется совместно с `USE_PROXY`. |  |
| `httpsProxy` | HTTPS-адрес прокси; используется совместно с `USE_PROXY`. |  |
| `importDashboards` | Импорт предопределённых дашбордов для выбранных сервисов. | `true` |
| `importAlerts` | Импорт предопределённых правил оповещений для выбранных сервисов. | `true` |
| `gcpServicesYaml` | Файл конфигурации для сервисов GCP. |  |
| `queryInterval` | Интервал опроса метрик в минутах. Допустимые значения: `1` - `6` | `3` |

#### Параметры для приёма только метрик (тип развёртывания: metrics)

| Имя параметра | Описание | Значение по умолчанию |
| --- | --- | --- |
| `deploymentType` | Установите значение 'metrics'. | `all` |
| `dynatraceAccessKey` | Ваш API токен Dynatrace с необходимыми разрешениями в соответствии с выбранным типом развёртывания. Подробнее см. [Требования к токенам](#token). |  |
| `dynatraceUrl` | Эндпоинт вашей среды Dynatrace. Подробнее см. [Определение URL для вашей среды](#url). |  |

#### Дополнительные необязательные параметры для приёма только метрик

Необязательно

| Имя параметра | Описание | Значение по умолчанию |
| --- | --- | --- |
| `requireValidCertificate` | При значении `true` Dynatrace требует SSL-сертификат вашей среды Dynatrace. | `true` |
| `selfMonitoringEnabled` | Отправка пользовательских метрик в GCP для быстрой диагностики корректности обработки и отправки метрик/логов в Dynatrace службой `dynatrace-gcp-monitor`. | `false` |
| `dockerImage` | Docker-образ Dynatrace GCP Monitor. Рекомендуется использовать значение по умолчанию, однако при необходимости его можно изменить. | `dynatrace/dynatrace-gcp-monitor` |
| `printMetricIngestInput` | При значении `true` GCP Monitor выводит строки метрик в stdout. | `false` |
| `serviceUsageBooking` | Учёт использования сервисов применяется для метрик и определяет проект, указанный вызывающей стороной, в целях квот и выставления счетов. При значении `source` вызовы monitoring API учитываются в проекте, где запущен контейнер Kubernetes. При значении `destination` - в отслеживаемом проекте. Подробнее см. [Мониторинг нескольких проектов GCP - Шаг 4](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик в Dynatrace из нескольких проектов Google Cloud."). | `source` |
| `useProxy` | В зависимости от значения этого флага GCP Monitor будет использовать следующие настройки прокси: Dynatrace (значение `DT_ONLY`), GCP API (значение `GCP_ONLY`) или оба варианта (значение `ALL`). | По умолчанию настройки прокси не используются. |
| `httpProxy` | HTTP-адрес прокси; используется совместно с `USE_PROXY`. |  |
| `httpsProxy` | HTTPS-адрес прокси; используется совместно с `USE_PROXY`. |  |
| `importDashboards` | Импорт предопределённых дашбордов для выбранных сервисов. | `true` |
| `importAlerts` | Импорт предопределённых правил оповещений для выбранных сервисов. | `true` |
| `gcpServicesYaml` | Файл конфигурации для сервисов GCP. |  |
| `queryInterval` | Интервал опроса метрик в минутах. Допустимые значения: `1` - `6` | `3` |

#### Параметры для приёма только логов (тип развёртывания: logs)

| Имя параметра | Описание | Значение по умолчанию |
| --- | --- | --- |
| `gcpProjectId` | Идентификатор проекта GCP, в котором будет развёрнут Dynatrace GCP Monitor. Используйте проект GCP с подпиской Pub/Sub для приёма логов. Подробнее см. [Настройка общего приёма логов](#logingest). | Идентификатор текущего проекта |
| `deploymentType` | Установите значение 'logs'. | `all` |
| `dynatraceAccessKey` | Ваш API токен Dynatrace с необходимыми разрешениями в соответствии с выбранным типом развёртывания. Подробнее см. [Требования к токенам](#token). |  |
| `activeGate.dynatracePaasToken` | Ваш PaaS токен. Подробнее см. [Требования к токенам](#token). |  |
| `dynatraceUrl` | Эндпоинт вашей среды Dynatrace. Подробнее см. [Определение URL для вашей среды](#url). |  |
| `logsSubscriptionId` | Идентификатор подписки Pub/Sub для приёма логов. Подробнее см. [Настройка общего приёма логов](#logingest). |  |

#### Дополнительные необязательные параметры для приёма только логов

Необязательно

| Имя параметра | Описание | Значение по умолчанию |
| --- | --- | --- |
| `activeGate.useExisting` | Установите true, если используется существующий ActiveGate для приёма логов. Подробнее см. [Требования к ActiveGate](#ag). | `false` |
| `dynatraceLogIngestUrl` | Эндпоинт ActiveGate для приёма логов в Dynatrace. Подробнее см. [Определение URL для вашей среды](#url). |  |
| `requireValidCertificate` | При значении `true` Dynatrace требует SSL-сертификат вашей среды Dynatrace. | `true` |
| `selfMonitoringEnabled` | Отправка пользовательских метрик в GCP для быстрой диагностики корректности обработки и отправки метрик/логов в Dynatrace службой `dynatrace-gcp-monitor`. | `false` |
| `dockerImage` | Docker-образ Dynatrace GCP Monitor. Рекомендуется использовать значение по умолчанию, однако при необходимости его можно изменить. | `dynatrace/dynatrace-gcp-monitor` |
| `logIngestContentMaxLength` | Максимальная длина содержимого события лога. Должна быть меньше или равна настройке вашей среды Dynatrace. | `8192` |
| `logIngestAttributeValueMaxLength` | Максимальная длина значения атрибута события лога. При превышении серверного лимита содержимое будет усечено. | `250` |
| `logIngestRequestMaxEvents` | Максимальное число событий лога в одном запросе к эндпоинту приёма логов. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `5000` |
| `logIngestRequestMaxSize` | Максимальный размер (в байтах) одного запроса к эндпоинту приёма логов. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `1048576` |
| `logIngestEventMaxAgeSeconds` | Определяет максимальный возраст пересылаемого события лога. Должно быть меньше или равно настройке вашей среды Dynatrace. | `86400` |

### Шаг 4 Подключение кластера Kubernetes

* Чтобы создать новый кластер GKE Autopilot скриптом развёртывания, добавьте `--create-autopilot-cluster` к скрипту. В этом случае подключение не требуется, так как скрипт автоматически подключится к новому кластеру.
* При развёртывании на существующем стандартном кластере GKE или существующем кластере GKE Autopilot подключитесь к кластеру из консоли GCP или через терминал. Следуйте приведённым ниже инструкциям.

Из консоли GCP

Через терминал

1. В консоли GCP перейдите в Kubernetes Engine.
2. Выберите **Clusters** > **Connect**.
3. Выберите **Run in Cloud Shell**.

Выполните команду ниже, заменив

* `<cluster>` именем кластера
* `<region>` регионом, в котором работает кластер
* `<project>` идентификатором проекта, в котором работает кластер

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

Подробнее см. [Настройка доступа к кластеру для kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Шаг 5 Запуск скрипта

* При развёртывании на существующем стандартном кластере GKE или существующем кластере GKE Autopilot скрипт создаст IAM service account с необходимыми ролями и развернёт `dynatrace-gcp-monitor` в кластере Kubernetes.
* При запуске с параметром `--create-autopilot-cluster` скрипт автоматически создаст новый кластер GKE Autopilot и развернёт в нём `dynatrace-gcp-monitor`.

Для запуска скрипта следуйте приведённым ниже инструкциям.

Запуск на существующем кластере

Запуск на новом кластере

Доступны два варианта:

* Запустите скрипт без параметров для использования значений по умолчанию (`dynatrace-gcp-monitor-sa` для имени IAM service account и `dynatrace_monitor` для префикса имени IAM роли):

```
cd helm-deployment-package



./deploy-helm.sh
```

* Запустите скрипт с параметрами для задания собственных значений (замените плейсхолдеры нужными значениями):

```
cd helm-deployment-package



./deploy-helm.sh [--service-account <service-account-to-be-created/updated>] [--role-name <role-to-be-created/updated>]
```

Выполните команду ниже.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster [--autopilot-cluster-name <name-of-new-cluster>]
```

## Проверка установки

Чтобы проверить успешность установки:

1. Проверьте, запущен ли контейнер.

   После установки может потребоваться несколько минут, пока контейнер запустится.

   ```
   kubectl -n dynatrace get pods
   ```
2. Проверьте логи контейнера на наличие ошибок или исключений. Доступны два варианта:

В Kubernetes CLI

В консоли GCP

* Для развёртываний типа 'metrics' выполните:

  ```
  kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics
  ```
* Для развёртываний типа 'logs' выполните:

  ```
  kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
  ```
* Для развёртываний типа 'all' выполните:

  ```
  kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics



  kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
  ```

Проверка логов контейнера на наличие ошибок в консоли GCP

1. Перейдите в **Logs explorer**.
2. Используйте следующие фильтры для получения логов приёма метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"` (для логов приёма метрик)
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"` (для логов приёма логов)

3. Проверьте импорт дашбордов (для развёртываний типа 'metrics' или 'all').

   Перейдите в **Dashboards** и отфильтруйте по **Tag** со значением **Google Cloud**. Должен быть доступен ряд дашбордов для сервисов Google Cloud.

## Просмотр метрик и/или логов

После развёртывания интеграции, в зависимости от типа развёртывания, доступны следующие возможности:

* Просмотр метрик отслеживаемых сервисов: перейдите в **Metrics**.
* Просмотр и анализ логов GCP: в Dynatrace перейдите в **Logs** и для поиска логов GCP отфильтруйте по `cloud.provider: gcp`.

![Логи GCP](https://dt-cdn.net/images/2021-05-12-11-58-05-1506-4dddfe1936.png)

Логи GCP

## Устранение неполадок

Для диагностики возможных проблем с развёртыванием и подключением см. [Устранение неполадок настройки мониторинга Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")