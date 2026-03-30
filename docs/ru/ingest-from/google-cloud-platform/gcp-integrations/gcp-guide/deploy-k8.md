---
title: Настройка интеграции метрик и логов Dynatrace GCP на новом кластере GKE Autopilot
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8
scraped: 2026-03-05T21:33:39.079131
---

Dynatrace версии 1.230+

Следуйте приведённым ниже инструкциям для настройки мониторинга Google Cloud для метрик и логов на новом кластере GKE Autopilot с использованием Google Cloud Shell. В процессе настройки будет создана новая подписка Pub/Sub. GKE запустит два контейнера: форвардер метрик и форвардер логов. После установки вы получите метрики, логи, дашборды и оповещения для настроенных сервисов в Dynatrace.

Если вы предпочитаете запускать скрипт развёртывания на существующем стандартном кластере GKE или GKE Autopilot, см. Настройка интеграции логов и метрик Dynatrace Google Cloud на существующем кластере GKE.

Другие варианты развёртывания см. в разделе Альтернативные сценарии развёртывания.

На этой странице описывается установка версии 1.0 интеграции GCP на кластере GKE.

* Если у вас уже установлена более ранняя версия, вам необходимо выполнить миграцию.

## Ограничения

Интеграция логов Dynatrace GCP поддерживает обработку до 8 ГБ данных в час (с базовыми ресурсами — без масштабирования). При больших нагрузках сообщения начнут накапливаться в подписке PubSub. Для измерения задержки отслеживайте следующие метрики: `Oldest unacked message age` и `Unacked messages`. Рекомендации по масштабированию см. в [руководстве по масштабированию](#scalingguide) ниже.

Интеграция метрик Dynatrace GCP поддерживает до 50 проектов GCP при стандартном развёртывании. Для мониторинга более крупных сред необходимо включить область метрик. См. Мониторинг нескольких проектов GCP — Крупные среды.

## Предварительные требования

Для развёртывания интеграции необходимо убедиться, что на машине, на которой вы выполняете установку, выполнены следующие требования.

* Только ОС Linux
* Доступ в интернет
* Доступ к кластеру GKE
* Доступ к среде Dynatrace

  Вам необходимо настроить конечную точку Dynatrace (URL среды, кластера или ActiveGate), на которую кластер GKE должен отправлять метрики и логи. Убедитесь, что у вас есть прямой сетевой доступ или, если между ними присутствует прокси-сервер или другой компонент, что связь не нарушена.

### Инструменты

Вы можете развернуть интеграцию Dynatrace GCP в Google Cloud Shell или в bash.

Если вы используете bash, вам необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* [helm](https://helm.sh/docs/intro/install/)
* [jq (версия 1.6)](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (версия 4.9.x+)](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Разрешения GCP

Для запуска скрипта развёртывания необходим набор разрешений. Вы можете создать пользовательскую роль (см. ниже) и использовать её для развёртывания `dynatrace-gcp-monitor`.

1. Создайте файл YAML с именем `dynatrace-gcp-monitor-helm-deployment-role.yaml` со следующим содержимым:

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

Каждая группа разрешений используется для управления различными ресурсами, включёнными в интеграцию. Создание и доступ — для новых ресурсов, обновление — для повторного использования существующих ресурсов, удаление — для деинсталляции.

* container.configMaps: для маппинга секретов и других переменных, используемых контейнерами.
* container.deployments: для развёртывания Kubernetes внутри кластера (включая поды, контейнеры и т.д.).
* container.namespaces: для пространства имён Kubernetes, в котором выполняется развёртывание ресурсов.
* container.pods: для подов Kubernetes.
* container.secrets: для секретов Kubernetes, в которых хранятся конфиденциальные переменные.
* container.serviceAccounts: для сервисного аккаунта в контексте Kubernetes.
* iam.roles: для необходимых разрешений для сбора данных.
* iam.serviceAccounts: для сервисного аккаунта общего контекста.
* resourcemanager.projects: для управления проектом, в котором выполняется развёртывание интеграции.
* serviceusage.services: для управления API сервисов.
* pubsub.subscriptions: для подписки PubSub, используемой для сбора и приёма логов.
* pubsub.topics: для темы PubSub, используемой для сбора и приёма логов.

2. Выполните команду ниже, заменив `<your_project_ID>` идентификатором проекта, в котором вы хотите развернуть интеграцию Dynatrace GCP.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно добавьте эту роль вашему пользователю GCP. Подробнее см. [Предоставление или отзыв отдельной роли](https://dt-url.net/vx03vid).

### Настройка экспорта логов

1. Выполните следующий shell-скрипт в проекте GCP, выбранном для развёртывания.

Обязательно замените `<your-subscription-name>` и `<your-topic-name>` вашими собственными значениями.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh


chmod +x deploy-pubsub.sh


./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Настройте [экспорт логов](https://dt-url.net/4743r02) для отправки нужных логов в тему GCP Pub/Sub, созданную выше.

### Разрешения Dynatrace

Вам необходимо создать токен с набором разрешений.

1. Перейдите в **Токены доступа**.
2. Выберите **Сгенерировать новый токен**.
3. Введите имя для вашего токена.
4. В разделе **Шаблон** выберите `GCP Services Monitoring`.
5. Нажмите **Сгенерировать**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Альтернативно вы можете создать токен и добавить разрешения вручную.

Добавить вручную

[Создайте API-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Learn the concept of an access token and its scopes.") и [включите следующие разрешения](../../../../dynatrace-api/basics/dynatrace-api-authentication.md#token-permissions "Find out how to get authenticated to use the Dynatrace API."):

* API v1:

  + **Чтение конфигурации**
  + **Запись конфигурации**
* API v2:

  + **Приём метрик**
  + **Чтение расширений**
  + **Запись расширений**
  + **Чтение конфигурации мониторинга расширений**
  + **Запись конфигурации мониторинга расширений**
  + **Чтение конфигурации среды расширений**
  + **Запись конфигурации среды расширений**
  + **Приём логов**
  + **Управление метаданными элементов Hub**
  + **Чтение данных, связанных с Hub**
  + **Установка и обновление элементов Hub**

Для мониторинга логов из нескольких проектов необходимо создать **Log Routing Sinks** в каждом исходном проекте, выбрав в качестве назначения ваш основной проект (в котором также развёрнуты интеграция, тема и подписка PubSub).
Дополнительную информацию см. в разделе [Маршрутизация логов к поддерживаемым назначениям](https://dt-url.net/cl038gj).

### Приём логов

* Определите, где будет выполняться приём логов, в соответствии с вашим развёртыванием. Это различие важно при настройке [параметров](#param) данной интеграции.

  + **Для развёртываний Dynatrace:** Приём лого, где приём логов выполняется непосредственно через Cluster API. Рекомендуется
  + **Для развёртываний Managed:** Вы можете использовать существующий ActiveGate для приёма логов. Информацию о его развёртывании см. в разделе Установка ActiveGate.

Из-за реализации GCP Cloud Function 2-го поколения логи от этих ресурсов будут связаны с базовыми экземплярами Cloud Run. Оба расширения должны быть включены.

Подробнее см. [Сравнение версий Google Cloud Functions](https://dt-url.net/b6038q5).

## Установка

Выполните приведённые ниже шаги для завершения настройки.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Загрузка пакета развёртывания Helm в Google Cloud Shell**](deploy-k8.md#dwld "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка значений параметров**](deploy-k8.md#param "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запуск скрипта развёртывания**](deploy-k8.md#script "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

### Шаг 1 Загрузка пакета развёртывания Helm в Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Настройка значений параметров

1. Пакет развёртывания Helm содержит файл `values.yaml` с необходимой конфигурацией для данного развёртывания. Перейдите в `helm-deployment-package/dynatrace-gcp-monitor` и отредактируйте файл `values.yaml`, задав обязательные и необязательные значения параметров следующим образом.

   Рекомендуется сохранить этот файл для будущих обновлений, так как он потребуется при повторных развёртываниях. Также учтите, что его схема может измениться. В таком случае следует использовать новый файл и только скопировать значения параметров.
2. Выберите, какие сервисы вы хотите мониторить с помощью Dynatrace.

   По умолчанию интеграция Dynatrace GCP начинает мониторинг выбранного набора сервисов. Список поддерживаемых сервисов см. в разделе Поддерживаемые сервисы Google Cloud.

Информацию о потреблении DDU см. в разделе [Потребление мониторинга](#ddu).

### Шаг 3 Запуск скрипта развёртывания

Скрипт развёртывания автоматически создаст новый кластер GKE Autopilot с именем `dynatrace-gcp-monitor` и развернёт на нём установку. Последние версии расширений GCP будут загружены.

```
cd helm-deployment-package


./deploy-helm.sh --create-autopilot-cluster
```

Чтобы задать другое имя для нового кластера, выполните приведённую ниже команду, заменив заполнитель (`<name-of-new-cluster>`) предпочитаемым именем.

```
cd helm-deployment-package


./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

Чтобы сохранить существующие версии установленных расширений и установить последние версии для остальных выбранных расширений, если они ещё не установлены, выполните приведённую ниже команду.

```
cd helm-deployment-package


./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Проверка установки

Для проверки успешности установки

1. Убедитесь, что контейнер запущен.

   После установки может потребоваться несколько минут, пока контейнер запустится и начнёт работать.

   ```
   kubectl -n dynatrace get pods
   ```
2. Проверьте логи контейнера на наличие ошибок или исключений. У вас есть два варианта:

   В Kubernetes CLI

   В консоли GCP

   Выполните следующие команды.

   ```
   kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics


   kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
   ```

   Для проверки логов контейнера на наличие ошибок в консоли GCP

   1. Перейдите в **Обозреватель логов**.
   2. Используйте фильтры ниже для получения логов приёма метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"` (для логов приёма метрик)
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"` (для логов приёма логов)
3. Проверьте, импортированы ли дашборды.

   Перейдите в ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Дашборды (Классические)** и отфильтруйте по **Тегу** `Google Cloud`. Должно быть доступно несколько дашбордов для сервисов Google Cloud.

## Выбор сервисов для мониторинга метрик

### Сервисы, включённые по умолчанию

Мониторинг следующих сервисов будет включён при развёртывании GCP Monitor:

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

Доступны дополнительные интеграции сервисов, но их необходимо включить. Список поддерживаемых сервисов см. в разделе Поддерживаемые сервисы Google Cloud. В следующем разделе описано, как ими управлять. В качестве альтернативного подхода рассмотрите использование автообнаружения для расширения охвата метрик.

### Управление включёнными сервисами

Вы можете управлять включёнными сервисами через Dynatrace Hub.

Отфильтруйте по "gcp" — в результатах вы увидите аннотации для элементов, которые уже доступны в вашей среде.

Для включения нового сервиса выберите его в Hub и установите.

Вы также можете отключить сервис через Dynatrace Hub.

Чтобы узнать, нужны ли обновления для сервисов, откройте их в Hub и проверьте примечания к выпуску. Обновления могут включать новые метрики, новые ресурсы, такие как дашборды, или другие изменения.

Все изменения включённых сервисов применяются к GCP Monitor в течение нескольких минут.

#### Наборы функций и доступные метрики

Чтобы узнать, какие метрики включены для конкретного сервиса, проверьте Поддерживаемые сервисы Google Cloud. По умолчанию включён только набор функций `defaultMetrics`. Чтобы включить дополнительные наборы функций, необходимо раскомментировать их в файле `values.yaml` и повторно развернуть весь GCP Monitor.

Текущую конфигурацию наборов функций можно найти в ConfigMap кластера с именем `dynatrace-gcp-function-config`.

#### Расширенное управление областью мониторинга

Для более точной настройки области мониторинга можно использовать поле `filter_conditions` в файле `values.yaml`. Для этого необходимо повторное развёртывание GCP Monitor. Синтаксис см. в разделе [Фильтры мониторинга GCP](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).

Пример:

```
filter_conditions:


resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Включение оповещений

Для активации оповещений необходимо включить события метрик для оповещений в Dynatrace.

Для включения событий метрик

1. Перейдите в **Настройки**.
2. В разделе **Обнаружение аномалий** выберите **События метрик**.
3. Отфильтруйте по оповещениям GCP и включите **Вкл./Выкл.** для оповещений, которые вы хотите активировать.

## Просмотр метрик и логов

После развёртывания интеграции вы можете:

* Просматривать метрики мониторируемых сервисов: перейдите в **Метрики** и отфильтруйте по `gcp`.
* Просматривать и анализировать логи GCP: перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Логи и события (Классические)** и для поиска логов GCP отфильтруйте по `cloud.provider: gcp`.

## Изменение настроек развёртывания

### Изменение параметров из `values.yaml`

Для загрузки нового файла `values.yaml` необходимо обновить ваш Helm-релиз.

Для обновления Helm-релиза

1. Узнайте, какую версию Helm-релиза вы используете.

   ```
   helm ls -n dynatrace
   ```
2. Выполните приведённую ниже команду, заменив `<your-helm-release>` значением из предыдущего шага.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

Подробнее см. [Helm upgrade](https://helm.sh/docs/helm/helm_upgrade/).

### Изменение типа развёртывания

Для изменения типа развёртывания (`all`, `metrics` или `logs`)

1. Узнайте, какую версию Helm-релиза вы используете.

   ```
   helm ls -n dynatrace
   ```
2. Удалите релиз.

   Обязательно замените `<your-helm-release>` именем релиза из предыдущего вывода.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Измените `deploymentType` в `values.yaml` на новое значение и сохраните файл.
4. Снова выполните команду развёртывания. Подробнее см. [Запуск скрипта развёртывания](#script).

## Проверка

Для исследования возможных проблем с развёртыванием и подключением

1. [Проверка установки](#verify)
2. Включение самомониторинга Необязательно
3. Проверьте файл логов `dynatrace_gcp_<date_time>.log`, созданный в процессе установки.

* Этот файл будет создаваться при каждом запуске скрипта установки.
* Отладочная информация не будет содержать конфиденциальных данных, таких как ключ доступа Dynatrace.
* Если вы обращаетесь к эксперту по продуктам Dynatrace через чат:

  + Обязательно предоставьте файл логов `dynatrace_gcp_<date_time>.log`, описанный в предыдущем шаге.
  + Предоставьте информацию о версии.

    - При проблемах во время установки проверьте файл `version.txt`.
    - При проблемах во время выполнения проверьте логи контейнера.

## Руководство по масштабированию для логов

Контейнер по умолчанию с 1.25vCPU и 1Gi (с конфигурацией по умолчанию) может обрабатывать 8 ГБ логов в час. Для достижения большей пропускной способности необходимо выделить больше ресурсов контейнеру (вертикальное масштабирование), увеличить количество реплик контейнера (горизонтальное масштабирование) и изменить конфигурационные параметры для эффективного использования выделенных ресурсов. Все конфигурационные переменные можно найти и изменить в `dynatrace-gcp-monitor-config`.

В следующей таблице представлены протестированные конфигурации и достигнутая пропускная способность с масштабированными контейнерами:

## Руководство по автомасштабированию для логов

Автомасштабирование работает только для типа развёртывания `logs`, но не `all`.

Рекомендуется сначала вручную масштабировать контейнер до машины 4vCPU 4Gi, а затем включить автомасштабирование.

GCP предоставляет автомасштабирование контейнеров в обоих направлениях: **горизонтальном** и **вертикальном**. Однако Dynatrace рекомендует только **горизонтальное** масштабирование.

Если у вас машина 4vCPU 4Gi, вы можете включить **горизонтальное** автомасштабирование. Однако мы **не** рекомендуем горизонтальное масштабирование с базовыми ресурсами контейнера (1.25vCPU, 1Gi). Во время тестирования это не показало эффективности. Одна машина 4vCPU работает лучше, чем четыре машины 1vCPU. Для включения горизонтального автомасштабирования используйте команду горизонтального автомасштабирования:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Автомасштабирование рекомендуется только при пропускной способности минимум 450 МБ/мин и возможности предоставить машину с 4vCPU 4Gi ОЗУ. Автомасштабирование выполняет только горизонтальное масштабирование, а не вертикальное.

Мы **не** рекомендуем **вертикальное** масштабирование, поскольку каждый раз при масштабировании машины необходимо изменять переменную окружения для создания большего количества процессов, соответствующих ядрам машины.

## Удаление

1. Узнайте, какую версию Helm-релиза вы используете.

```
helm ls -n dynatrace
```

2. Удалите релиз.

Обязательно замените `<your-helm-release>` именем релиза из предыдущего вывода.

```
helm uninstall <your-helm-release> -n dynatrace
```

Альтернативно вы можете удалить пространство имён.

```
kubectl delete namespace dynatrace
```

3. Для удаления всех ресурсов мониторинга (таких как дашборды и оповещения) из Dynatrace необходимо удалить все расширения GCP.

Вы можете найти и удалить соответствующие расширения через Dynatrace Hub.

Обязательно удалите следующие ресурсы вручную:

* Начальную роль, созданную и привязанную к сервисному аккаунту, который вы использовали для развёртывания интеграции.
* Тему PubSub.
* Подписку PubSub.
* LogRoute Sink.

## Потребление мониторинга

### Приём метрик

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества мониторируемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. Расширение Dynatrace (единицы данных Davis).").

### Приём логов

Потребление DDU применяется к облачному мониторингу логов. Подробнее см. DDU для мониторинга логов.

## Связанные темы

* Настройка Dynatrace в Google Cloud
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
