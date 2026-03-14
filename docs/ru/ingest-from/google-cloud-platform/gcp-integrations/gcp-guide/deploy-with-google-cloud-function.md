---
title: Развертывание интеграции метрик Dynatrace Google Cloud в Google Cloud Functions
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function
scraped: 2026-03-05T21:32:17.758122
---

# Развёртывание интеграции метрик Dynatrace Google Cloud в Google Cloud Functions


* Latest Dynatrace
* Руководство
* Чтение: 7 мин
* Обновлено 6 сентября 2022
* Устарело

Dynatrace версии 1.230+

Интеграция метрик Dynatrace Google Cloud в Google Cloud Functions **больше не** поддерживается.

Если вы используете этот тип развёртывания, вам следует как можно скорее перейти на интеграцию Google Cloud на базе Kubernetes.
См. [Миграция с Google Cloud Functions 1.0 на Google Cloud k8s 1.0](migrate-gcp-function-1-to-k8s-1.md "Миграция с Google Cloud Functions v1.0 на Google Cloud k8s v1.0.").

В качестве альтернативы [основному развёртыванию](deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot."), которое обеспечивает мониторинг Google Cloud как для метрик, так и для логов, и где развёртывание выполняется в кластере GKE, вы можете настроить мониторинг только метрик в Google Cloud Cloud Function. Обратите внимание, что развёртывание в Google Cloud Cloud Function не рекомендуется для крупных сред и не поддерживает пересылку логов.
В этом сценарии вы сможете запустить скрипт развёртывания либо в Google Cloud Shell, либо в bash. После установки вы получите метрики, дашборды и оповещения для настроенных сервисов в Dynatrace.

Другие варианты развёртывания см. в разделе [Альтернативные сценарии развёртывания](../gcp-guide.md "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

На этой странице описывается развёртывание версии 1.0 интеграции Dynatrace Google Cloud в Google Cloud Cloud Function.

* Если у вас уже установлена [предыдущая версия](../../legacy/deploy-with-google-cloud-function-legacy.md "Настройте мониторинг для сервисов Google Cloud с помощью Google Cloud Function.") Google Cloud Monitor, вам необходимо выполнить [миграцию](migrate-gcp-function.md "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 в Kubernetes и Google Cloud Function.").

## Предварительные требования

### Инструменты

Вы можете развернуть интеграцию Dynatrace Google Cloud в Google Cloud Shell или в bash.

Если вы используете bash, вам необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)

### Разрешения Google Cloud

Для запуска скрипта развёртывания требуется список разрешений. Вам необходимо создать пользовательскую роль и использовать её для развёртывания `dynatrace-gcp-monitor`.

Чтобы создать пользовательскую роль

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
2. Выполните команду ниже, заменив `<your_project_ID>` на идентификатор проекта, в котором вы хотите развернуть интеграцию Dynatrace.

   ```
   gcloud iam roles create dynatrace_monitor.cloud_function_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-cloud-function-deployment-role.yaml
   ```

Обязательно добавьте эту роль вашему пользователю Google Cloud. Подробности см. в [Предоставление или отзыв отдельной роли](https://dt-url.net/vx03vid).

### Разрешения Dynatrace

[Создайте API-токен](https://dt-url.net/be03q3a) и [включите следующие разрешения](https://dt-url.net/c023q1m):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extension monitoring configurations**
  + **Write extension monitoring configurations**
  + **Read extension environment configurations**
  + **Write extension environment configurations**

### URL Dynatrace

Определите URL для вашей среды.

* Для Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/`
* Для Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/`

Чтобы определить `<your-environment-id>`, см. [идентификатор среды](https://dt-url.net/ej43qge).

## Установка

Вы можете развернуть интеграцию Dynatrace Google Cloud в Google Cloud Shell или в bash. Для настройки интеграции следуйте инструкциям ниже.

Для развёртывания в bash обязательно перезапустите консоль и [инициализируйте Cloud SDK](https://dt-url.net/ac43q0f) перед началом установки.

Для инициализации Cloud SDK выполните

```
gcloud init
```

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Скачайте пакет развёртывания**](deploy-with-google-cloud-function.md#dwld "Настройте мониторинг сервисов Google Cloud в Google Cloud Functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройте развёртывание**](deploy-with-google-cloud-function.md#configure-deployment "Настройте мониторинг сервисов Google Cloud в Google Cloud Functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Запустите скрипт развёртывания**](deploy-with-google-cloud-function.md#script "Настройте мониторинг сервисов Google Cloud в Google Cloud Functions.")

### Шаг 1 Скачивание пакета развёртывания

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/tag/release-1.1.8/download/function-deployment-package.zip" -O function-deployment-package.zip; unzip function-deployment-package.zip; chmod a+x *.sh
```

### Шаг 2 Настройка развёртывания

1. Настройте параметры в файле `activation-config.yaml` из пакета развёртывания.

   Рекомендуется сохранить этот файл для будущих обновлений, так как он понадобится при повторных развёртываниях. Также учтите, что его схема может измениться. В таком случае следует использовать новый файл и скопировать только значения параметров.
2. Выберите, какие сервисы вы хотите, чтобы Dynatrace мониторил.

По умолчанию интеграция Google Cloud начинает мониторинг серии выбранных сервисов. Раскомментируйте любые дополнительные сервисы, которые вы хотите, чтобы Dynatrace мониторил, в файле `activation-config.yaml`.

Информацию о потреблении DDU см. в разделе [Потребление мониторинга](#ddu).

### Шаг 3 Запуск скрипта развёртывания

Обновление версий расширений выполняется по умолчанию. Чтобы сохранить версии существующих расширений, запустите скрипт с параметром `--without-extensions-upgrade`.

```
./setup.sh
```

Скрипт может запросить подтверждение во время развёртывания. Для целей CI/CD вы можете добавить опцию `-d`, чтобы сделать скрипт неинтерактивным.

После развёртывания интеграции вы сможете видеть метрики от отслеживаемых сервисов. Если вы хотите изменить область мониторинга (сервисы и наборы функций) или обновить интеграцию Google Cloud, см. [Изменение настроек развёртывания](#manage) ниже.

## Проверка установки

Чтобы проверить, была ли установка успешной

1. В консоли Google Cloud перейдите в Cloud Functions и убедитесь, что `dynatrace-gcp-monitor` присутствует.
2. Выберите недавно развёрнутую функцию Google Cloud Monitor и перейдите в **Logs**, чтобы убедиться в отсутствии сообщений об ошибках.

## Включение оповещений

Для активации оповещений необходимо включить события метрик для оповещений в Dynatrace.

Чтобы включить пользовательские события

1. Перейдите в **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте по оповещениям GCP и включите **On/Off** для тех оповещений, которые хотите активировать.

## Просмотр включённых сервисов

Чтобы найти список текущих включённых сервисов, перейдите в Cloud Function в консоли Google Cloud и проверьте переменную окружения `ACTIVATION_CONFIG`.

## Обновление сервисов

Добавление, удаление и обновление версий существующих сервисов выполняется путём изменения соответствующего списка сервисов и повторного развёртывания.

1. Примените изменения к `activation-config.yaml`, комментируя или раскомментируя блоки конфигурации, соответствующие конкретным сервисам.
   Терминология в файле включает:

   * `service`: представляет имя сервиса Google Cloud, который вы хотите мониторить. Сервисы сгруппированы по расширениям, но вы можете определить, что нужно мониторить, на более низком уровне (`featureSets`)
   * `featureSet`: набор метрик для данного сервиса. `default_metrics` — это набор функций по умолчанию с рекомендуемым набором метрик для мониторинга. Для более специфичных сценариев вы можете рассмотреть мониторинг таких наборов, как `istio featureSet` для `gae_instance service`
   * `filter_conditions`: фильтр на уровне сервиса, который позволяет сузить область мониторинга. Он основан на [фильтрах Google Cloud Monitoring](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).
     Пример:

     ```
     filter_conditions:


     resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
     ```
2. Обновите мониторируемые сервисы, запустив скрипт ниже.

   Обновление версий расширений выполняется по умолчанию. Чтобы сохранить версии существующих расширений, запустите скрипт с параметром `--without-extensions-upgrade`.

   ```
   ./setup.sh
   ```
3. Если вы удалили сервисы из мониторинга, найдите соответствующие расширения в Dynatrace Hub и удалите их, чтобы удалить специфичные для сервиса ресурсы (такие как дашборды и оповещения).

### Пример

В следующем примере

* Сервис `gae_instance` отключён.
* Для сервиса `gce_instance` включены только два набора функций: `default_metrics` и `istio`.

```
# Google App Engine Instance


#- service: gae_instance


#  featureSets:


#    - default_metrics


#  vars:


#    filter_conditions: ""


# Google VM Instance


- service: gce_instance


featureSets:


- default_metrics


#    - agent


#    - firewallinsights


- istio


#    - uptime_check


vars:


filter_conditions: ""
```

Полный список поддерживаемых сервисов Google Cloud см. в [Поддерживаемые сервисы Google Cloud](../gcp-supported-service-metrics-new.md#services "Мониторьте сервисы Google Cloud с помощью Dynatrace и просматривайте доступные метрики.").

## Изменение настроек развёртывания

Чтобы добавить или удалить сервисы или обновить параметры, необходимо повторно развернуть интеграцию.

1. Примените изменения к `activation-config.yaml`.

   Обязательно используйте то же значение параметра `FUNCTION_NAME`, что и раньше.
2. [Перезапустите скрипт развёртывания](#script).

## Верификация

Для расследования потенциальных проблем с развёртыванием и подключением

1. [Проверьте установку](#verify)
2. [Включите самомониторинг](deploy-k8/self-monitoring-gcp.md "Определите, правильно ли ваша функция самомониторинга обрабатывает и отправляет логи в Dynatrace.") (необязательно)
3. Проверьте файл логов `dynatrace_gcp_<date_time>.log`, созданный во время процесса установки.

* Этот файл создаётся каждый раз при запуске скрипта установки.
* Отладочная информация не будет содержать конфиденциальных данных, таких как ключ доступа Dynatrace.
* Если вы обращаетесь к эксперту Dynatrace через живой чат:

  + Обязательно предоставьте файл логов `dynatrace_gcp_<date_time>.log`, описанный в предыдущем шаге.
  + Предоставьте информацию о версии.

    - Для проблем во время установки проверьте файл `version.txt`.
    - Для проблем во время выполнения [проверьте логи функции](#verify).

## Удаление

1. Перейдите в каталог установки и выполните команду ниже.

```
./uninstall.sh
```

2. Чтобы удалить все ресурсы мониторинга (такие как дашборды и оповещения) из Dynatrace, необходимо удалить все расширения Google Cloud.

Вы можете найти и удалить соответствующие расширения через Dynatrace Hub.

## Потребление мониторинга

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества мониторируемых метрик и их измерений (каждое измерение метрики приводит к загрузке 1 точки данных; 1 точка данных потребляет 0.001 DDU). Подробности см. в [Расширение Dynatrace (единицы данных Davis)](../../../../license/monitoring-consumption-classic/davis-data-units.md "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).").

## Связанные темы

* [Настройка Dynatrace в Google Cloud](../../../google-cloud-platform.md "Мониторинг Google Cloud с помощью Dynatrace.")