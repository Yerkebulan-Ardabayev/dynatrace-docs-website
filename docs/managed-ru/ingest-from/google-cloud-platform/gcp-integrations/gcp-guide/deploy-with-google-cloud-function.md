---
title: Развёртывание интеграции метрик Dynatrace Google Cloud в Google Cloud Functions
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function
scraped: 2026-05-12T11:51:49.839631
---

# Развёртывание интеграции метрик Dynatrace Google Cloud в Google Cloud Functions

# Развёртывание интеграции метрик Dynatrace Google Cloud в Google Cloud Functions

* Практическое руководство
* Чтение: 7 мин
* Обновлено 6 сентября 2022 г.
* Устарело

Dynatrace версии 1.230+

Интеграция метрик Dynatrace Google Cloud в Google Cloud Functions **больше не** поддерживается.

Если используется такой тип развёртывания, необходимо как можно скорее перейти на интеграцию Google Cloud на основе k8s.
См. раздел [Миграция с Google Cloud Functions 1.0 на Google Cloud k8s 1.0](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function-1-to-k8s-1 "Миграция с Google Cloud Functions v1.0 на Google Cloud k8s v1.0.").

В качестве альтернативы [основному развёртыванию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."), которое обеспечивает мониторинг Google Cloud как для метрик, так и для логов в кластере GKE, можно настроить мониторинг только метрик в Google Cloud Cloud Function. Развёртывание через Google Cloud Cloud Function не рекомендуется для крупных сред и не поддерживает пересылку логов.
В этом сценарии скрипт развёртывания запускается в Google Cloud Shell или bash. После установки в Dynatrace появятся метрики, дашборды и оповещения для настроенных сервисов.

Другие варианты развёртывания описаны в разделе [Альтернативные сценарии развёртывания](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

На этой странице описывается развёртывание версии 1.0 интеграции Dynatrace Google Cloud в Google Cloud Cloud Function.

* Если установлена [более ранняя версия](/managed/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy "Настройка мониторинга для сервисов Google Cloud с использованием Google Cloud Function.") Google Cloud Monitor, необходимо выполнить [миграцию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция с Google Cloud integration версии 0.1 на версию 1.0 в Kubernetes и как Google Cloud Function.").

## Предварительные требования

### Инструменты

Интеграцию Dynatrace Google Cloud можно развернуть в Google Cloud Shell или bash.

При использовании bash необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)

### Разрешения Google Cloud

Для запуска скрипта развёртывания требуется набор разрешений. Необходимо создать пользовательскую роль и использовать её для развёртывания `dynatrace-gcp-monitor`.

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
2. Выполните команду ниже, заменив `<your_project_ID>` на идентификатор проекта, в котором требуется развернуть интеграцию Dynatrace.

   ```
   gcloud iam roles create dynatrace_monitor.cloud_function_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-cloud-function-deployment-role.yaml
   ```

Обязательно добавьте эту роль своему пользователю Google Cloud. Подробности см. в разделе [Предоставление или отзыв одной роли](https://dt-url.net/vx03vid).

### Разрешения Dynatrace

[Создайте API-токен](https://dt-url.net/be03q3a) и [включите следующие разрешения](https://dt-url.net/c023q1m):

* API v1:

  + **Чтение конфигурации**
  + **Запись конфигурации**
* API v2:

  + **Приём метрик**
  + **Чтение расширений**
  + **Запись расширений**
  + **Чтение конфигураций мониторинга расширений**
  + **Запись конфигураций мониторинга расширений**
  + **Чтение конфигураций среды расширений**
  + **Запись конфигураций среды расширений**

### URL Dynatrace

Определите URL своей среды.

* Для Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/`
* Для Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/`

Чтобы узнать `<your-environment-id>`, см. раздел [Идентификатор среды](https://dt-url.net/ej43qge).

## Установка

Интеграцию Dynatrace Google Cloud можно развернуть в Google Cloud Shell или bash. Для настройки интеграции следуйте инструкциям ниже.

При развёртывании в bash перед установкой необходимо перезапустить консоль и [инициализировать Cloud SDK](https://dt-url.net/ac43q0f).

Чтобы инициализировать Cloud SDK, выполните

```
gcloud init
```

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Загрузить пакет развёртывания**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#dwld "Настройка мониторинга сервисов Google Cloud в Google Cloud Functions.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настроить развёртывание**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#configure-deployment "Настройка мониторинга сервисов Google Cloud в Google Cloud Functions.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запустить скрипт развёртывания**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#script "Настройка мониторинга сервисов Google Cloud в Google Cloud Functions.")

### Шаг 1 Загрузка пакета развёртывания

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/tag/release-1.1.8/download/function-deployment-package.zip" -O function-deployment-package.zip; unzip function-deployment-package.zip; chmod a+x *.sh
```

### Шаг 2 Настройка развёртывания

1. Настройте параметры в файле `activation-config.yaml` из пакета развёртывания.

   Рекомендуется сохранить этот файл для будущих обновлений, так как он потребуется при повторных развёртываниях. Учтите, что его схема может меняться: в таком случае следует использовать новый файл и переносить только значения параметров.
2. Выберите сервисы для мониторинга в Dynatrace.

По умолчанию интеграция Google Cloud начинает мониторинг набора выбранных сервисов. Раскомментируйте в файле `activation-config.yaml` дополнительные сервисы для мониторинга в Dynatrace.

Информацию о потреблении DDU см. в разделе [Потребление при мониторинге](#ddu).

### Шаг 3 Запуск скрипта развёртывания

Обновление версий расширений выполняется по умолчанию. Чтобы сохранить текущие версии существующих расширений, запустите скрипт с параметром `--without-extensions-upgrade`.

```
./setup.sh
```

Во время развёртывания скрипт может запрашивать подтверждения. Для целей CI/CD добавьте параметр `-d`, чтобы скрипт работал в неинтерактивном режиме.

После развёртывания интеграции в Dynatrace появятся метрики отслеживаемых сервисов. Чтобы изменить область мониторинга (сервисы и featureSets) или обновить интеграцию Google Cloud, см. раздел [Изменение параметров развёртывания](#manage) ниже.

## Проверка установки

Чтобы проверить успешность установки

1. В консоли Google Cloud перейдите в раздел Cloud Functions и убедитесь, что `dynatrace-gcp-monitor` присутствует.
2. Выберите только что развёрнутую функцию Google Cloud Monitor и перейдите в раздел **Logs**, чтобы убедиться в отсутствии сообщений об ошибках.

## Включение оповещений

Для активации оповещений необходимо включить метрические события для оповещений в Dynatrace.

Чтобы включить пользовательские события

1. Перейдите в раздел **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте оповещения GCP и включите **On/Off** для нужных оповещений.

## Просмотр включённых сервисов

Чтобы найти список включённых сервисов, перейдите в Cloud Function в консоли Google Cloud и проверьте переменную среды `ACTIVATION_CONFIG`.

## Обновление сервисов

Добавление, удаление и обновление версий существующих сервисов выполняется путём изменения соответствующего списка сервисов и повторного развёртывания.

1. Внесите изменения в `activation-config.yaml`, закомментировав или раскомментировав блоки конфигурации для конкретных сервисов.
   Терминология файла включает:

   * `service`: название сервиса Google Cloud для мониторинга. Сервисы сгруппированы по расширениям, но можно указать, что отслеживать на более детальном уровне (`featureSets`).
   * `featureSet`: набор метрик для конкретного сервиса. `default_metrics` является набором `featureSet` по умолчанию с рекомендуемыми метриками. В отдельных случаях можно рассмотреть мониторинг таких наборов, как `istio featureSet` для `gae_instance service`.
   * `filter_conditions`: фильтр уровня сервиса для сужения области мониторинга на основе [фильтров GCP Monitoring](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).
     Пример:

     ```
     filter_conditions:



     resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
     ```
2. Обновите отслеживаемые сервисы, запустив скрипт ниже.

   Обновление версий расширений выполняется по умолчанию. Чтобы сохранить текущие версии существующих расширений, запустите скрипт с параметром `--without-extensions-upgrade`.

   ```
   ./setup.sh
   ```
3. Если сервисы были исключены из мониторинга, найдите соответствующие расширения в Dynatrace Hub и удалите их, чтобы убрать специфические ресурсы (дашборды и оповещения).

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

Полный список поддерживаемых сервисов Google Cloud см. в разделе [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new#services "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик.").

## Изменение параметров развёртывания

Для добавления или удаления сервисов либо обновления параметров необходимо повторно развернуть интеграцию.

1. Внесите изменения в `activation-config.yaml`.

   Обязательно используйте то же значение параметра `FUNCTION_NAME`, что и раньше.
2. [Повторно запустите скрипт развёртывания](#script).

## Верификация

Для диагностики возможных проблем с развёртыванием и подключением

1. [Проверьте установку](#verify)
2. [Включите самомониторинг](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.") Опционально
3. Проверьте лог-файл `dynatrace_gcp_<date_time>.log`, созданный в процессе установки.

* Этот файл создаётся при каждом запуске скрипта установки.
* Отладочная информация не содержит конфиденциальных данных, таких как ключ доступа Dynatrace.
* При обращении к эксперту Dynatrace через чат:

  + Предоставьте лог-файл `dynatrace_gcp_<date_time>.log`, описанный на предыдущем шаге.
  + Укажите информацию о версии.

    - Для проблем при установке проверьте файл `version.txt`.
    - Для проблем во время работы [проверьте логи функции](#verify).

## Удаление

1. Перейдите в каталог установки и выполните команду ниже.

```
./uninstall.sh
```

2. Чтобы удалить все ресурсы мониторинга (дашборды и оповещения) из Dynatrace, необходимо удалить все расширения Google Cloud.

Найти и удалить соответствующие расширения можно через Dynatrace Hub.

## Потребление при мониторинге

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от числа отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробности см. в разделе [Расширение Dynatrace (единицы данных Davis)](/managed/license/monitoring-consumption-classic/davis-data-units "Понимание расчёта потребления мониторинга Dynatrace на основе единиц данных Davis (DDU).").

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")