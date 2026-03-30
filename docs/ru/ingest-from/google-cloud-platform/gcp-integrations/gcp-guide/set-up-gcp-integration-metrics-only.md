---
title: Настройка интеграции Dynatrace с Google Cloud для сбора метрик на кластере GKE
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only
scraped: 2026-03-05T21:40:45.625171
---

Dynatrace версии 1.230+

В качестве альтернативы основному развёртыванию, которое обеспечивает мониторинг Google Cloud как для метрик, так и для логов, вы можете настроить мониторинг только метрик. В этом сценарии вы запустите скрипт развёртывания в Google Cloud Shell. Инструкции зависят от того, где вы хотите запустить скрипт развёртывания:

* На новом кластере GKE Autopilot, создаваемом автоматически Рекомендуется
* На существующем стандартном кластере GKE или кластере GKE Autopilot

Во время настройки GKE запустит контейнер для пересылки метрик. После установки вы получите метрики, дашборды и оповещения для настроенных сервисов в Dynatrace.

Другие варианты развёртывания описаны в разделе Альтернативные сценарии развёртывания.

На этой странице описана установка версии 1.0 интеграции с Google Cloud на кластере GKE.

* Если у вас уже установлена более ранняя версия, необходимо выполнить миграцию.

## Ограничения

Интеграция Dynatrace с Google Cloud для сбора метрик поддерживает до 50 проектов Google Cloud при стандартном развёртывании. Для мониторинга более крупных сред необходимо включить область метрик. См. Мониторинг нескольких проектов Google Cloud — крупные среды.

## Предварительные требования

Для развёртывания интеграции необходимо убедиться, что на машине, на которой выполняется установка, выполнены следующие требования.

* Только ОС Linux
* Доступ в интернет
* Доступ к кластеру GKE
* Доступ к среде Dynatrace

  Необходимо настроить конечную точку Dynatrace (URL среды, кластера или ActiveGate), на которую кластер GKE будет отправлять метрики и логи. Убедитесь, что у вас есть прямой сетевой доступ или, если между компонентами находится прокси-сервер или другой промежуточный компонент, что связь не нарушена.

### Инструменты

Вы можете развернуть интеграцию Dynatrace с GCP в Google Cloud Shell или в bash.

Если вы используете bash, необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* [helm](https://helm.sh/docs/intro/install/)
* [jq (версия 1.6)](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (версия 4.9.x+)](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Разрешения Google Cloud

Для запуска скрипта развёртывания требуется список разрешений. Необходимо создать пользовательскую роль (см. ниже) и использовать её для развёртывания `dynatrace-gcp-monitor`.

1. Создайте YAML файл с именем `dynatrace-gcp-monitor-helm-deployment-role.yaml` со следующим содержимым:

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

Каждая группа разрешений используется для управления различными ресурсами, входящими в интеграцию. Создание и доступ предназначены для новых ресурсов, обновление — для повторного использования существующих, а удаление — для деинсталляции.

* container.configMaps: для сопоставления секретов и других переменных, используемых контейнерами.
* container.deployments: для развёртывания K8s в кластере (включая поды, контейнеры и т. д.).
* container.namespaces: для пространства имён K8s, в которое выполняется развёртывание ресурсов.
* container.pods: для подов K8s.
* container.secrets: для секретов K8s, в которых хранятся конфиденциальные переменные.
* container.serviceAccounts: для сервисных аккаунтов в контексте K8s.
* iam.roles: для необходимых разрешений на сбор метрик.
* iam.serviceAccounts: для общего контекстного сервисного аккаунта.
* resourcemanager.projects: для управления проектом, в котором выполняется развёртывание интеграции.
* serviceusage.services: для управления API сервисов.

2. Выполните приведённую ниже команду, заменив `<your_project_ID>` на идентификатор проекта, в котором вы хотите развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно назначьте эту роль вашему пользователю Google Cloud. Подробности см. в разделе [Назначение или отзыв отдельной роли](https://dt-url.net/vx03vid).

### Настройки Google Cloud

Место развёртывания интеграции определяет, нужно ли изменять дополнительные настройки.

#### Развёртывание на кластере GKE Autopilot

Если вы развёртываете интеграцию на существующем кластере GKE Autopilot или на новом кластере Autopilot, который будет автоматически создан скриптом развёртывания, дополнительные настройки не требуются.

#### Развёртывание на стандартном кластере GKE

Если вы развёртываете интеграцию на существующем стандартном кластере GKE, необходимо:

* [Включить Workload Identity на кластере.](https://dt-url.net/2j23qqv)
* [Включить `GKE_METADATA` на пулах узлов GKE.](https://dt-url.net/an43q2s)

### Разрешения Dynatrace

Необходимо создать токен с набором разрешений.

1. Перейдите в **Access tokens**.
2. Выберите **Generate new token**.
3. Введите имя для вашего токена.
4. В разделе **Template** выберите `GCP Services Monitoring`.
5. Выберите **Generate**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Альтернативно вы можете создать токен и добавить разрешения вручную.

Добавить вручную

[Создайте API-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") и [включите следующие разрешения](../../../../dynatrace-api/basics/dynatrace-api-authentication.md#token-permissions "Узнайте, как пройти аутентификацию для использования Dynatrace API."):

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

**Скачайте пакет развёртывания Helm в Google Cloud Shell**](set-up-gcp-integration-metrics-only.md#dwld "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте значения параметров**](set-up-gcp-integration-metrics-only.md#params "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Подключите ваш кластер Kubernetes**](set-up-gcp-integration-metrics-only.md#connect "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Запустите скрипт развёртывания**](set-up-gcp-integration-metrics-only.md#script "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")

### Шаг 1 Скачайте пакет развёртывания Helm в Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Настройте значения параметров

1. Пакет развёртывания Helm содержит файл `values.yaml` с необходимой конфигурацией для данного развёртывания. Перейдите в `helm-deployment-package/dynatrace-gcp-monitor` и отредактируйте файл `values.yaml`, установив обязательные и необязательные значения параметров следующим образом.

   Рекомендуется сохранить этот файл для будущих обновлений, так как он понадобится при повторном развёртывании. Также учитывайте, что его схема может измениться. В этом случае следует использовать новый файл и скопировать в него только значения параметров.
2. Выберите, какие сервисы вы хотите мониторить с помощью Dynatrace.

   По умолчанию интеграция Dynatrace с Google Cloud начинает мониторинг набора выбранных сервисов. Список поддерживаемых сервисов см. в разделе Поддерживаемые сервисы Google Cloud.

Информацию о потреблении DDU см. в разделе [Потребление мониторинга](#ddu).

### Шаг 3 Подключите ваш кластер Kubernetes

* Если вы хотите, чтобы новый кластер GKE Autopilot был создан скриптом развёртывания, добавьте `--create-autopilot-cluster` к скрипту. В этом случае подключение к кластеру произойдёт автоматически, и вы можете перейти к [шагу 4](#script).
* Если вы запускаете скрипт развёртывания на существующем стандартном кластере GKE или кластере GKE Autopilot, вы можете подключиться к кластеру из консоли Google Cloud или через терминал. Следуйте инструкциям ниже.

Из консоли Google Cloud

Через терминал

1. В консоли Google Cloud перейдите в Kubernetes Engine.
2. Выберите **Clusters**, затем выберите **Connect**.
3. Выберите **Run in Cloud Shell**.

Выполните приведённую ниже команду, заменив

* `<cluster>` на имя вашего кластера
* `<region>` на регион, в котором работает ваш кластер
* `<project>` на идентификатор проекта, в котором работает ваш кластер

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

Подробности см. в разделе [Настройка доступа к кластеру для kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Шаг 4 Запустите скрипт развёртывания

* Если вы запускаете скрипт развёртывания на существующем стандартном кластере GKE или кластере GKE Autopilot, скрипт создаст IAM-сервисный аккаунт с необходимыми ролями и развернёт `dynatrace-gcp-monitor` на вашем кластере Kubernetes.
* Если вы запускаете скрипт развёртывания с параметром `--create-autopilot-cluster`, скрипт автоматически создаст новый кластер GKE Autopilot и развернёт на нём `dynatrace-gcp-monitor`.

Для запуска скрипта развёртывания следуйте инструкциям ниже.

Запуск на существующем кластере

Запуск на новом кластере

Будут загружены последние версии расширений Google Cloud. У вас есть два варианта:

* Запустите скрипт развёртывания без параметров, если хотите использовать значения по умолчанию (`dynatrace-gcp-monitor-sa` для имени IAM-сервисного аккаунта и `dynatrace_monitor` для префикса имени IAM-роли):

```
cd helm-deployment-package


./deploy-helm.sh
```

* Запустите скрипт развёртывания с параметрами, если хотите задать собственные значения (обязательно замените заполнители на нужные значения):

```
cd helm-deployment-package


./deploy-helm.sh [--role-name <role-to-be-created/updated>]
```

Чтобы сохранить существующие версии установленных расширений и установить последние версии только для остальных выбранных расширений (если они отсутствуют), выполните следующую команду.

```
cd helm-deployment-package


./deploy-helm.sh --without-extensions-upgrade
```

Выполните приведённую ниже команду. Будут загружены последние версии расширений.

```
cd helm-deployment-package


./deploy-helm.sh --create-autopilot-cluster
```

Чтобы задать другое имя для нового кластера, выполните следующую команду, заменив заполнитель (`<name-of-new-cluster>`) на предпочитаемое имя.

```
cd helm-deployment-package


./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

Чтобы сохранить существующие версии установленных расширений и установить последние версии только для остальных выбранных расширений (если они отсутствуют), выполните следующую команду.

```
cd helm-deployment-package


./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Проверка установки

Для проверки успешности установки

1. Проверьте, работает ли контейнер.

   После установки может потребоваться несколько минут, прежде чем контейнер запустится.

   ```
   kubectl -n dynatrace get pods
   ```
2. Проверьте логи контейнера на наличие ошибок или исключений. У вас есть два варианта:

В Kubernetes CLI

В консоли Google Cloud

Выполните следующую команду.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics
```

Для проверки логов контейнера на наличие ошибок в консоли Google Cloud

1. Перейдите в **Logs explorer**.
2. Используйте следующие фильтры для получения логов загрузки метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"`

3. Проверьте, импортированы ли дашборды.

   Перейдите в ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** и отфильтруйте по **Tag** для `Google Cloud`. Должны быть доступны дашборды для сервисов Google Cloud.

## Выбор сервисов для мониторинга метрик

### Сервисы, включённые по умолчанию

При развёртывании Google Cloud Monitor будет включён мониторинг следующих сервисов:

* Google APIs
* Google App Engine
* Google BigQuery
* Google Cloud Functions
* Google Cloud Run
* Google Cloud Storage
* Google Compute Engine
* Google Firestore в режиме Datastore
* Google Filestore
* Google Kubernetes Engine
* Google Cloud Load Balancing
* Google Cloud Pub/Sub
* Google Cloud Pub/Sub Lite
* Google Cloud SQL

Доступны дополнительные интеграции сервисов, но их необходимо включить. Список поддерживаемых сервисов см. в разделе Поддерживаемые сервисы Google Cloud. В следующем разделе описано управление ими. Для альтернативного подхода рассмотрите использование автообнаружения для расширения охвата метрик.

### Управление включёнными сервисами

Управлять включёнными сервисами можно через Dynatrace Hub.

Отфильтруйте по "gcp" — вы увидите аннотации в результатах для элементов, которые уже доступны в вашей среде.

Чтобы включить новый сервис, выберите его в Hub и установите.

Вы также можете отключить сервис через Dynatrace Hub.

Чтобы проверить, нуждаются ли сервисы в обновлении, откройте их в Hub и проверьте примечания к выпуску. Обновления могут включать новые метрики, новые ресурсы, такие как дашборды, или другие изменения.

Все изменения включённых сервисов применяются к Google Cloud Monitor в течение нескольких минут.

#### Наборы функций и доступные метрики

Чтобы узнать, какие метрики включены для конкретного сервиса, см. Поддерживаемые сервисы Google Cloud. По умолчанию включён только набор функций `defaultMetrics`. Для включения дополнительных наборов функций необходимо раскомментировать их в файле `values.yaml` и повторно развернуть Google Cloud Monitor.

Текущую конфигурацию наборов функций можно найти в ConfigMap кластера с именем `dynatrace-gcp-function-config`.

#### Расширенное управление областью мониторинга

Для более точной настройки области мониторинга можно использовать поле `filter_conditions` в файле `values.yaml`. Для этого требуется повторное развёртывание Google Cloud Monitor. Синтаксис см. в разделе [Фильтры Google Cloud Monitoring](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).

Пример:

```
filter_conditions:


resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Включение оповещений

Для активации оповещений необходимо включить события метрик для оповещений в Dynatrace.

Для включения событий метрик

1. Перейдите в **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте оповещения Google Cloud и включите **On/Off** для оповещений, которые хотите активировать.

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики от отслеживаемых сервисов (перейдите в **Metrics** и отфильтруйте по `gcp`).

## Изменение настроек развёртывания

### Изменение параметров из `values.yaml`

Для загрузки нового файла `values.yaml` необходимо обновить ваш Helm-релиз.

Для обновления Helm-релиза

1. Узнайте, какую версию Helm-релиза вы используете.

   ```
   helm ls -n dynatrace
   ```
2. Выполните приведённую ниже команду, заменив `<your-helm-release>` на значение из предыдущего шага.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

Подробности см. в документации [Helm upgrade](https://helm.sh/docs/helm/helm_upgrade/).

### Изменение типа развёртывания

Для изменения типа развёртывания (`all`, `metrics` или `logs`)

1. Узнайте, какую версию Helm-релиза вы используете.

   ```
   helm ls -n dynatrace
   ```
2. Удалите релиз.

   Обязательно замените `<your-helm-release>` на имя релиза из предыдущего вывода.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Измените значение `deploymentType` в `values.yaml` на новое и сохраните файл.
4. Повторно запустите команду развёртывания. Подробности см. в разделе [Запуск скрипта развёртывания](#script).

## Верификация

Для исследования потенциальных проблем развёртывания и подключения

1. [Проверьте установку](#verify)
2. Включите самомониторинг Необязательно
3. Проверьте лог-файл `dynatrace_gcp_<date_time>.log`, созданный в процессе установки.

* Этот файл создаётся при каждом запуске скрипта установки.
* Отладочная информация не будет содержать конфиденциальных данных, таких как ключ доступа Dynatrace.
* Если вы обращаетесь к эксперту Dynatrace через чат:

  + Обязательно предоставьте лог-файл `dynatrace_gcp_<date_time>.log`, описанный на предыдущем шаге.
  + Предоставьте информацию о версии.

    - При проблемах во время установки проверьте файл `version.txt`.
    - При проблемах во время выполнения проверьте логи контейнера.

## Удаление

1. Узнайте, какую версию Helm-релиза вы используете.

```
helm ls -n dynatrace
```

2. Удалите релиз.

Обязательно замените `<your-helm-release>` на имя релиза из предыдущего вывода.

```
helm uninstall <your-helm-release> -n dynatrace
```

Альтернативно можно удалить пространство имён.

```
kubectl delete namespace dynatrace
```

3. Для удаления всех ресурсов мониторинга (таких как дашборды и оповещения) из Dynatrace необходимо удалить все расширения Google Cloud.

Вы можете найти и удалить соответствующие расширения через Dynatrace Hub.

Убедитесь, что вы вручную удалили первоначальную роль, созданную и привязанную к сервисному аккаунту, который использовался для развёртывания интеграции.

## Потребление мониторинга

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к загрузке 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробности см. в разделе Расширение Dynatrace (единицы данных Davis).").

## Связанные темы

* Настройка Dynatrace в Google Cloud
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
