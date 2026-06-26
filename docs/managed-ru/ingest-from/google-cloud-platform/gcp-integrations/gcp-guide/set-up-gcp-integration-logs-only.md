---
title: Настройка интеграции логов Dynatrace с Google Cloud в контейнере Kubernetes (GKE)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only
scraped: 2026-05-12T11:51:39.690366
---

# Настройка интеграции логов Dynatrace с Google Cloud в контейнере Kubernetes (GKE)

# Настройка интеграции логов Dynatrace с Google Cloud в контейнере Kubernetes (GKE)

* Практическое руководство
* Чтение: 12 мин
* Обновлено 08 октября 2024 г.

Dynatrace версии 1.230+

В качестве альтернативы [основному развёртыванию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."), которое обеспечивает мониторинг Google Cloud и метрик, и логов, можно настроить мониторинг только логов. В этом сценарии скрипт развёртывания запускается в Google Cloud Shell. Инструкции зависят от того, где будет выполняться скрипт развёртывания:

* На новом кластере GKE Autopilot, созданном автоматически (рекомендуется)
* На существующем стандартном кластере GKE или кластере GKE Autopilot

В процессе настройки будет создана новая подписка Pub/Sub. GKE запустит контейнер для пересылки логов. После установки в Dynatrace станут доступны логи, дашборды и оповещения для настроенных сервисов.

Другие варианты развёртывания см. в разделе [Альтернативные сценарии развёртывания](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

На этой странице описана установка интеграции Google Cloud версии 1.0 на кластере GKE.

* Если установлена [более ранняя версия](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes."), необходимо выполнить [миграцию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция интеграции Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.").

## Ограничения

Интеграция логов Dynatrace с Google Cloud поддерживает обработку до 8 ГБ данных в час (при базовых ресурсах, без масштабирования). При больших нагрузках сообщения начнут накапливаться в подписке PubSub. Для измерения задержки используйте метрики: `Oldest unacked message age` и `Unacked messages`. Рекомендации по масштабированию см. в разделе [Руководство по масштабированию](#scalingguide) ниже.

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
* iam.roles: для необходимых разрешений сбора данных.
* iam.serviceAccounts: для service account в общем контексте.
* resourcemanager.projects: для управления проектом, в котором развёртывается интеграция.
* serviceusage.services: для управления API сервисов.
* pubsub.subscriptions: для подписки PubSub, используемой для сбора и приёма логов.
* pubsub.topics: для топика PubSub, используемого для сбора и приёма логов.

2. Выполните команду ниже, заменив `<your_project_ID>` на ID проекта, в котором нужно развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно добавьте эту роль своему пользователю Google Cloud. Подробнее см. [Предоставление или отзыв отдельной роли](https://dt-url.net/vx03vid).

### Настройка экспорта логов

1. Выполните следующий shell-скрипт в проекте Google Cloud, выбранном для развёртывания.

Обязательно замените `<your-subscription-name>` и `<your-topic-name>` на собственные значения.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Настройте [экспорт логов](https://dt-url.net/4743r02) для отправки нужных логов в созданный выше топик Google Cloud Pub/Sub.

Для мониторинга логов из нескольких проектов необходимо создать **Log Routing Sinks** в каждом исходном проекте, указав в качестве назначения основной проект (в котором развёрнута интеграция, а также топик и подписка PubSub).
Подробнее см. [Маршрутизация логов в поддерживаемые назначения](https://dt-url.net/cl038gj).

### Разрешения Dynatrace

* [Создайте API-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях видимости.") и [включите следующее разрешение](/managed/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Узнайте, как пройти аутентификацию для работы с API Dynatrace."): **Ingest logs** (API v2).

### Приём логов

* Определите, где будет выполняться приём логов в соответствии с вашим развёртыванием. Это важно при настройке [параметров](#param) интеграции.

  + **Для развёртываний SaaS:** приём логов SaaS, при котором логи принимаются напрямую через Cluster API (рекомендуется).
  + **Для развёртываний Managed:** можно использовать существующий ActiveGate для приёма логов. Информацию о развёртывании см. в разделе [Установка ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").

Из-за особенностей реализации Cloud Function 2nd gen в GCP логи этих ресурсов будут привязаны к базовым экземплярам Cloud Run. Необходимо включить оба расширения.

Подробнее см. [Сравнение версий Google Cloud Functions](https://dt-url.net/b6038q5).

## Установка

Выполните приведённые ниже шаги для завершения настройки.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Скачайте пакет развёртывания Helm в Google Cloud Shell**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#dwld "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте значения параметров**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#param "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Подключите кластер Kubernetes**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#connect "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Запустите скрипт развёртывания**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#script "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")

### Шаг 1 Скачайте пакет развёртывания Helm в Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Настройте значения параметров

Пакет развёртывания Helm содержит файл `values.yaml` с необходимой конфигурацией. Перейдите в `helm-deployment-package/dynatrace-gcp-monitor` и отредактируйте файл `values.yaml`, задав обязательные и необязательные параметры следующим образом.

Рекомендуется сохранить этот файл в надёжном месте для последующих обновлений: он потребуется при повторных развёртываниях. Учтите, что схема файла может измениться; в этом случае используйте новый файл и перенесите в него только значения параметров.

| **Имя параметра** | **Описание** | **Значение по умолчанию** |
| --- | --- | --- |
| `gcpProjectId` | Обязательный. ID проекта Google Cloud, выбранного для развёртывания. | Текущий ID проекта |
| `deploymentType` | Обязательный. Установите значение `logs`. | `all` |
| `dynatraceAccessKey` | Обязательный. Ваш [API-токен Dynatrace](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях видимости.") с [необходимыми разрешениями](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."). |  |
| `dynatraceAccessKeySecretName` | Необязательный. Можно указать ключ для получения эндпоинта из Google Cloud Secret Manager вместо `dynatraceAccessKey`. |  |
| `dynatraceUrlSecretName` | Необязательный. Можно указать ключ для получения эндпоинта из Google Cloud Secret Manager вместо `dynatraceUrl`. |  |
|  |  |  |
| `dynatraceUrl` | Обязательный. Для приёма логов Managed используется URL кластера (`https:/<your_cluster_IP_or_hostname>/e/<your_environment_ID>`). Для приёма логов Managed с существующим ActiveGate используется URL ActiveGate (`https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`). **Примечание:** для определения `<your-environment-id>` см. [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как работать с окружениями мониторинга."). |  |
| `logsSubscriptionId` | Обязательный. ID подписки Pub/Sub для приёма логов. Подробнее см. [Настройка экспорта логов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#pubsub "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."). |  |
| `requireValidCertificate` | Необязательный. Если установлено значение `true`, Dynatrace требует SSL-сертификат окружения. Для приёма логов Managed с новым ActiveGate рекомендуется установить значение `false`. | `true` |
| `selfMonitoringEnabled` | Необязательный. Отправляет пользовательские метрики в Google Cloud для быстрой диагностики корректности обработки и отправки логов в Dynatrace. Подробнее см. [Метрики самомониторинга для интеграции Dynatrace с Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Проверьте, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace."). | `false` |
| `serviceAccount` | Необязательный. Имя создаваемого service account. |  |
| `dockerImage` | Необязательный. Docker-образ Dynatrace Google Cloud Monitor. Рекомендуется использовать значение по умолчанию, но при необходимости его можно изменить. | `dynatrace/dynatrace-gcp-monitor:v1-latest` |
| `logIngestContentMaxLength` | Необязательный. Максимальная длина содержимого события лога. Должна быть не больше соответствующего параметра окружения Dynatrace. | `8192` |
| `logIngestAttributeValueMaxLength` | Необязательный. Максимальная длина значения атрибута события лога. При превышении серверного лимита содержимое будет усечено. | `250` |
| `logIngestRequestMaxEvents` | Необязательный. Максимальное количество событий лога в одном запросе к эндпоинту приёма. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `5000` |
| `logIngestRequestMaxSize` | Необязательный. Максимальный размер (в байтах) одного запроса к эндпоинту приёма. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `1048576` |
| `logIngestEventMaxAgeSeconds` | Необязательный. Определяет максимальный возраст пересылаемого события лога. Должен быть не больше соответствующего параметра окружения Dynatrace. | `86400` |
| `clusterIpv4Cidr` | Необязательный. Задайте диапазон IP-адресов для подов кластера в нотации CIDR, если требуется пользовательский диапазон. |  |
| `servicesIpv4Cidr` | Необязательный. Задайте диапазон IP-адресов для сервисов. Можно указать в виде размера маски сети или в нотации CIDR. |  |
| `useCustomMasterCidr` | Необязательный. Если установлено значение `true`, можно задать диапазон IPv4 CIDR для сети master. | `false` |
| `masterIpv4Cidr` | Необязательный. Диапазон IPv4 CIDR для сети master. Требует, чтобы `useCustomMasterCidr` было установлено в `true`. |  |

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
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
```

Для проверки логов контейнера в консоли Google Cloud

1. Перейдите в **Logs explorer**.
2. Используйте фильтры ниже для получения логов приёма метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"`

3. Проверьте, импортированы ли дашборды.

   В Dynatrace перейдите в **Dashboards** и отфильтруйте по тегу `Google Cloud`. Должен быть доступен набор дашбордов для сервисов Google Cloud.

## Включение оповещений

Для активации оповещений необходимо включить метрические события в Dynatrace.

Чтобы включить метрические события

1. Перейдите в **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте оповещения Google Cloud и включите нужные с помощью переключателя **On/Off**.

## Просмотр логов

После развёртывания интеграции логи Google Cloud можно просматривать и анализировать в Dynatrace: перейдите в **Logs** и отфильтруйте по `cloud.provider: gcp`.

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

## Руководство по масштабированию для логов

Контейнер по умолчанию с 1,25 vCPU и 1 ГиБ (при стандартной конфигурации) может обрабатывать до 8 ГБ логов в час. Для большей пропускной способности необходимо выделить контейнеру больше ресурсов (вертикальное масштабирование), увеличить количество реплик (горизонтальное масштабирование) и скорректировать конфигурационные параметры для эффективного использования выделенных ресурсов. Все конфигурационные переменные находятся в `dynatrace-gcp-monitor-config`.

В таблице ниже приведены проверенные конфигурации и достигнутая пропускная способность при вертикальном и горизонтальном масштабировании контейнеров:

| Достигнутая пропускная способность | Ресурсы машины | Наборы реплик | Значения конфигурационных переменных |
| --- | --- | --- | --- |
| ~8 МБ/с => ~480 МБ/мин | 4 vCPU 4 ГиБ RAM | 1 | `PARALLEL_PROCESSES=4`,  `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20` |
| ~25 МБ/с => ~1,5 ГБ/мин => ~2 ТБ/сут | 4 vCPU 4 ГиБ RAM | 4 | `PARALLEL_PROCESSES=4`,  `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20` |
| ~46 МБ/с => ~2,7 ГБ/мин => ~4 ТБ/сут | 4 vCPU 4 ГиБ RAM | 6 | `PARALLEL_PROCESSES=4`,  `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20` |

## Руководство по автоматическому масштабированию для логов

Автоматическое масштабирование работает только для типа развёртывания `logs`, но не `all`.

Рекомендуется сначала вручную масштабировать контейнер до конфигурации 4 vCPU / 4 ГиБ, а затем включить автоматическое масштабирование.

GCP поддерживает автоматическое масштабирование контейнеров в обоих направлениях: **горизонтальное** и **вертикальное**. Тем не менее Dynatrace рекомендует только **горизонтальное** масштабирование.

При наличии машины 4 vCPU / 4 ГиБ можно включить **горизонтальное** автоматическое масштабирование. Однако горизонтальное масштабирование с базовыми ресурсами контейнера (1,25 vCPU, 1 ГиБ) **не рекомендуется**: тестирование не подтвердило его эффективности. Одна машина на 4 vCPU работает лучше, чем четыре машины на 1 vCPU. Для включения горизонтального автоматического масштабирования выполните команду:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Автоматическое масштабирование рекомендуется только при минимальной пропускной способности 450 МБ/мин и наличии машины 4 vCPU / 4 ГиБ RAM. Автоматическое масштабирование выполняется только горизонтально, без вертикального увеличения ресурсов машины.

**Вертикальное** масштабирование **не рекомендуется**: при каждом увеличении ресурсов машины необходимо изменять переменную окружения для создания большего числа процессов, соответствующего ядрам машины.

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

Обязательно удалите вручную следующие ресурсы:

* Исходную роль, созданную и привязанную к service account, использованному для развёртывания интеграции.
* Топик PubSub.
* Подписку PubSub.
* Маршрутизатор LogRoute Sink.

## Потребление при мониторинге

Потребление DDU применяется к облачному мониторингу логов. Подробнее см. [DDU для мониторинга логов](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)