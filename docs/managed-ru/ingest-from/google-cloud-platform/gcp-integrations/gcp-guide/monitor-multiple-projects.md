---
title: Мониторинг нескольких проектов Google Cloud
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects
scraped: 2026-05-12T11:51:51.977809
---

# Мониторинг нескольких проектов Google Cloud

# Мониторинг нескольких проектов Google Cloud

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 12 марта 2021 г.

Вы можете отправлять метрики в Dynatrace из нескольких проектов Google Cloud. Например, вы можете запустить `dynatrace-gcp-monitor` в проекте, выделенном для мониторинга, и получать метрики из проектов production, stage или development.

Существует два метода мониторинга нескольких проектов Google Cloud в зависимости от размера окружения, которое вы хотите отслеживать:

* Большие окружения: рекомендуемый метод мультипроектного мониторинга
* Стандартные окружения: альтернативный метод

## Большие окружения

Для мониторинга больших окружений можно воспользоваться функцией областей метрик (metrics scope) от Google. Необходимо выбрать основной проект области метрик (scoping project), в котором будет развёрнута интеграция Google Cloud, и настроить остальные проекты как отслеживаемые. Инструкции приведены ниже.

Для изменения области метрик необходимы разрешения роли Monitoring Admin (roles/monitoring.admin) для всех задействованных проектов.

1. В консоли Google Cloud выберите основной проект области метрик и перейдите к сервису Monitoring.
2. Выберите настройки **Metrics Scope** в левом меню.
3. Выберите **Add Cloud projects to metrics scope**.
4. Выберите все нужные проекты, которые будут отслеживаться основным проектом области метрик, и добавьте их.

По сути, вы расширяете видимость метрик от основного проекта области метрик на все отслеживаемые проекты из консоли Google Cloud. Подробнее см. [Просмотр метрик для нескольких проектов](https://cloud.google.com/monitoring/settings).

На следующем шаге разверните интеграцию Google Cloud Monitor, указав в конфигурационном файле параметр `scopingProjectSupportEnabled` со значением `true`. См. [Основное развёртывание](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") или [Альтернативные сценарии развёртывания](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

Такой подход работает примерно до 375 проектов среднего размера. Если вы хотите отслеживать больше проектов, потребуется настроить несколько интеграций Google Cloud Monitor в разных основных проектах области метрик, назначив каждый отслеживаемый проект одному из них.

## Стандартные окружения

Настроить стандартный мониторинг можно двумя способами: с помощью gcloud CLI или в консоли Google Cloud. Инструкции приведены ниже.

Предварительные требования

Разверните интеграцию Dynatrace в [контейнере Kubernetes](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

### Настройка мониторинга с помощью gcloud CLI

Чтобы добавить проекты в мониторинг с помощью gcloud CLI

1. Создайте роли IAM.

Обязательно замените `<your-desired-project-ID>` на ID нужного вам проекта.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/gcp_iam_roles/dynatrace-gcp-monitor-metrics-role.yaml



gcloud iam roles create dynatrace_monitor.metrics --project=<your-desired-project-ID> --file=dynatrace-gcp-monitor-metrics-role.yaml
```

2. Предоставьте необходимые IAM-политики сервисному аккаунту IAM для нужных проектов.

Обязательно замените `<your-desired-project-ID>` на ID нужного проекта, а `<your-GCP-project-ID>` на ID проекта, в котором был создан сервисный аккаунт IAM.

Развёртывание в контейнере Kubernetes

Развёртывание в Google Cloud Function

```
gcloud projects add-iam-policy-binding <your-desired-project-ID> --member="serviceAccount:dynatrace-gcp-monitor-sa@<your-GCP-project-ID>.iam.gserviceaccount.com" --role=projects/<your-desired-project-ID>/roles/dynatrace_monitor.metrics
```

```
gcloud projects add-iam-policy-binding <your-desired-project-ID> --member="serviceAccount:dynatrace-gcp-service-custom@<your-GCP-project-ID>.iam.gserviceaccount.com" --role=projects/<your-desired-project-ID>/roles/dynatrace_monitor.metrics
```

3. Повторите шаги 1 и 2 для всех остальных проектов, которые вы хотите отслеживать.
4. Включите разрешение для учёта использования сервисов (service usage booking). Необязательно

Если вы хотите настроить учёт использования сервисов, необходимо включить [разрешение **serviceusage.services.use** для вашего сервисного аккаунта IAM](https://cloud.google.com/service-usage/docs/access-control#permissions).
Подробнее о настройке `serviceUsageBooking` см. [Параметры](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#param "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Метрики из вновь настроенных проектов появляются в Dynatrace примерно через минуту.

При развёртывании GKE после добавления проектов в мониторинг необходимо перезапустить контейнер Kubernetes.

### Настройка мониторинга в консоли Google Cloud

Кроме того, вы можете предоставить доступ для всех нужных проектов в консоли Google Cloud.

Чтобы добавить проекты в мониторинг в консоли Google Cloud

1. В консоли Google Cloud перейдите в **IAM & Admin**.
2. Выберите проект, который вы хотите отслеживать, и добавьте разрешения для сервисного аккаунта IAM, привязанного к функции.
3. Повторите шаг 2 для всех остальных проектов, которые вы хотите отслеживать.

При развёртывании GKE после добавления проектов в мониторинг необходимо перезапустить контейнер Kubernetes.

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")