---
title: Настройка интеграции Dynatrace с Google Cloud для сбора логов в контейнере Kubernetes (GKE)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only
scraped: 2026-03-05T21:37:05.026071
---

# Настройка интеграции Dynatrace с Google Cloud для сбора логов в контейнере Kubernetes (GKE)

# Настройка интеграции Dynatrace с Google Cloud для сбора логов в контейнере Kubernetes (GKE)

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 12 мин
* Обновлено 8 октября 2024 г.

Dynatrace версии 1.230+

В качестве альтернативы [основному развёртыванию](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP на новом кластере GKE Autopilot."), которое обеспечивает мониторинг Google Cloud как для метрик, так и для логов, вы можете настроить мониторинг только логов. В этом сценарии вы запустите скрипт развёртывания в Google Cloud Shell. Инструкции зависят от того, где вы хотите запустить скрипт развёртывания:

* На новом кластере GKE Autopilot, создаваемом автоматически Рекомендуется
* На существующем стандартном кластере GKE или кластере GKE Autopilot

Во время настройки будет создана новая подписка Pub/Sub. GKE запустит контейнер для пересылки логов. После установки вы получите логи, дашборды и оповещения для настроенных сервисов в Dynatrace.

Другие варианты развёртывания описаны в разделе [Альтернативные сценарии развёртывания](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

На этой странице описана установка версии 1.0 интеграции с Google Cloud на кластере GKE.

* Если у вас уже установлена [более ранняя версия](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes."), необходимо выполнить [миграцию](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 для Kubernetes и Google Cloud Function.").

## Ограничения

Интеграция Dynatrace с Google Cloud для сбора логов поддерживает обработку до 8 ГБ данных в час (с базовыми ресурсами — без масштабирования). При больших нагрузках сообщения начнут накапливаться в подписке PubSub. Для измерения задержки используйте метрики: `Oldest unacked message age` и `Unacked messages`. Рекомендации по масштабированию приведены в [руководстве по масштабированию](#scalingguide) ниже.

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

Каждая группа разрешений используется для управления различными ресурсами, входящими в интеграцию. Создание и доступ предназначены для новых ресурсов, обновление — для повторного использования существующих, а удаление — для деинсталляции.

* container.configMaps: для сопоставления секретов и других переменных, используемых контейнерами.
* container.deployments: для развёртывания K8s в кластере (включая поды, контейнеры и т. д.).
* container.namespaces: для пространства имён K8s, в которое выполняется развёртывание ресурсов.
* container.pods: для подов K8s.
* container.secrets: для секретов K8s, в которых хранятся конфиденциальные переменные.
* container.serviceAccounts: для сервисных аккаунтов в контексте K8s.
* iam.roles: для необходимых разрешений на сбор данных.
* iam.serviceAccounts: для общего контекстного сервисного аккаунта.
* resourcemanager.projects: для управления проектом, в котором выполняется развёртывание интеграции.
* serviceusage.services: для управления API сервисов.
* pubsub.subscriptions: для подписки PubSub, используемой для сбора и загрузки логов.
* pubsub.topics: для темы PubSub, используемой для сбора и загрузки логов.

2. Выполните приведённую ниже команду, заменив `<your_project_ID>` на идентификатор проекта, в котором вы хотите развернуть интеграцию Dynatrace.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно назначьте эту роль вашему пользователю Google Cloud. Подробности см. в разделе [Назначение или отзыв отдельной роли](https://dt-url.net/vx03vid).

### Настройка экспорта логов

1. Запустите следующий shell-скрипт в проекте Google Cloud, выбранном для развёртывания.

Обязательно замените `<your-subscription-name>` и `<your-topic-name>` на ваши значения.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Настройте [экспорт логов](https://dt-url.net/4743r02) для отправки нужных логов в тему Google Cloud Pub/Sub, созданную выше.

Для мониторинга логов из нескольких проектов необходимо создать **приёмники маршрутизации логов (Log Routing Sinks)** в каждом исходном проекте, выбирая в качестве назначения ваш основной проект (в котором также развёрнута интеграция, тема и подписка PubSub).
Дополнительную информацию см. в разделе [Маршрутизация логов в поддерживаемые назначения](https://dt-url.net/cl038gj).

### Разрешения Dynatrace

* [Создайте API-токен](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях действия.") и [включите следующее разрешение](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Узнайте, как пройти аутентификацию для использования Dynatrace API."): **Ingest logs** (API v2).

### Загрузка логов

* Определите, где будет выполняться загрузка логов, в зависимости от вашего развёртывания. Это различие важно при настройке [параметров](#param) для данной интеграции.

  + **Для SaaS-развёртываний:** загрузка логов SaaS, при которой загрузка логов выполняется напрямую через Cluster API. Рекомендуется
  + **Для Managed-развёртываний:** вы можете использовать существующий ActiveGate для загрузки логов. Информацию о развёртывании см. в разделе [Установка ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").

Из-за реализации GCP Cloud Function 2-го поколения, логи этих ресурсов будут связаны с базовыми экземплярами Cloud Run. Оба расширения должны быть включены.

Подробнее см. в разделе [Сравнение версий Google Cloud Functions](https://dt-url.net/b6038q5).

## Установка

Выполните приведённые ниже шаги для завершения настройки.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Скачайте пакет развёртывания Helm в Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#dwld "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте значения параметров**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#param "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Подключите ваш кластер Kubernetes**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#connect "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Запустите скрипт развёртывания**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#script "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")

### Шаг 1 Скачайте пакет развёртывания Helm в Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Настройте значения параметров

Пакет развёртывания Helm содержит файл `values.yaml` с необходимой конфигурацией для данного развёртывания. Перейдите в `helm-deployment-package/dynatrace-gcp-monitor` и отредактируйте файл `values.yaml`, установив обязательные и необязательные значения параметров следующим образом.

Рекомендуется сохранить этот файл для будущих обновлений, так как он понадобится при повторном развёртывании. Также учитывайте, что его схема может измениться. В этом случае следует использовать новый файл и скопировать в него только значения параметров.

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
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
```

Для проверки логов контейнера на наличие ошибок в консоли Google Cloud

1. Перейдите в **Logs explorer**.
2. Используйте следующие фильтры для получения логов загрузки метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"`

3. Проверьте, импортированы ли дашборды.

   В Dynatrace перейдите в ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** и отфильтруйте по **Tag** для `Google Cloud`. Должны быть доступны дашборды для сервисов Google Cloud.

## Включение оповещений

Для активации оповещений необходимо включить события метрик для оповещений в Dynatrace.

Для включения событий метрик

1. Перейдите в **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте оповещения Google Cloud и включите **On/Off** для оповещений, которые хотите активировать.

## Просмотр логов

После развёртывания интеграции вы можете просматривать и анализировать логи Google Cloud в Dynatrace, перейдя в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** и отфильтровав по `cloud.provider: gcp`.

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
2. [Включите самомониторинг](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.") Необязательно
3. Проверьте лог-файл `dynatrace_gcp_<date_time>.log`, созданный в процессе установки.

* Этот файл создаётся при каждом запуске скрипта установки.
* Отладочная информация не будет содержать конфиденциальных данных, таких как ключ доступа Dynatrace.
* Если вы обращаетесь к эксперту Dynatrace через чат:

  + Обязательно предоставьте лог-файл `dynatrace_gcp_<date_time>.log`, описанный на предыдущем шаге.
  + Предоставьте информацию о версии.

    - При проблемах во время установки проверьте файл `version.txt`.
    - При проблемах во время выполнения [проверьте логи контейнера](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.").

## Руководство по масштабированию для логов

Контейнер по умолчанию с 1,25 vCPU и 1 Gi (с конфигурацией по умолчанию) способен обрабатывать 8 ГБ логов в час. Для достижения большей пропускной способности необходимо выделить контейнеру больше ресурсов (вертикальное масштабирование), увеличить количество реплик контейнера (горизонтальное масштабирование) и изменить конфигурационные параметры для эффективного использования выделенных ресурсов. Все конфигурационные переменные можно найти и изменить в `dynatrace-gcp-monitor-config`.

В следующей таблице представлена протестированная конфигурация и достигнутая пропускная способность при масштабированных контейнерах:

## Руководство по автомасштабированию для логов

Автомасштабирование работает только для типа развёртывания `logs`, но не `all`.

Рекомендуется сначала вручную масштабировать контейнер до 4 vCPU и 4 Gi, а затем включить автомасштабирование.

GCP предоставляет автомасштабирование контейнеров в обоих направлениях: **горизонтальном** и **вертикальном**. Однако Dynatrace рекомендует только **горизонтальное** масштабирование.

Если у вас есть машина 4 vCPU 4 Gi, вы можете включить **горизонтальное** автомасштабирование. Однако мы **не** рекомендуем горизонтальное масштабирование с базовыми ресурсами контейнера (1,25 vCPU, 1 Gi). Эффективность этого подхода не была подтверждена при тестировании. Одна машина 4 vCPU работает лучше, чем четыре машины 1 vCPU. Для включения горизонтального автомасштабирования используйте команду:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Автомасштабирование рекомендуется только при минимальной пропускной способности 450 МБ/мин и наличии машины 4 vCPU 4 Gi RAM. Автомасштабирование выполняет только горизонтальное масштабирование, но не вертикальное.

Мы **не** рекомендуем **вертикальное** масштабирование, поскольку при каждом увеличении мощности машины необходимо изменять переменную окружения для создания дополнительных процессов, соответствующих ядрам машины.

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

Убедитесь, что вы вручную удалили следующие ресурсы:

* Первоначальную роль, созданную и привязанную к сервисному аккаунту, который вы использовали для развёртывания интеграции.
* Тему PubSub.
* Подписку PubSub.
* Приёмник маршрутизации логов (LogRoute Sink).

## Потребление мониторинга

Потребление DDU применяется к облачному мониторингу логов. Подробности см. в разделе [DDU для мониторинга логов](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/docs/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
