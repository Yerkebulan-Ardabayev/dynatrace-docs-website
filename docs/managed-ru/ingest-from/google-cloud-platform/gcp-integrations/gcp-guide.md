---
title: Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide
scraped: 2026-05-12T11:10:39.052799
---

# Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite

# Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite

* Обзор
* Чтение: 2 мин
* Опубликовано 17 января 2022 г.

Dynatrace идеально интегрируется с Google Cloud, обеспечивая глубокую видимость рабочих нагрузок, выполняющихся на этой платформе.

## Поддерживаемые сервисы Google Cloud

Dynatrace может анализировать метрики всех сервисов, доступных в Google Operations API. Сведения о мониторинге поддерживаемых сервисов Google Cloud, возможностях и параметрах конфигурации см. в разделе [Метрики поддерживаемых сервисов Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик.").

## Обзорная страница Google Cloud

Dynatrace предоставляет обзорную страницу Google Cloud. Она включает представления по каждому проекту Google Cloud и списки инстансов для виртуальных машин, SQL, Cloud Functions и Kubernetes.

Если вы уже отслеживаете Google Cloud, а обзорная страница недоступна, необходимо обновить имеющуюся у вас интеграцию с Google Cloud.

## Настройка приёма метрик и логов

Чтобы начать анализировать метрики и логи всех сервисов, доступных в Google Operations API, см. [Настройка интеграции метрик и логов Dynatrace с Google Cloud в новом кластере GKE Autopilot](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") Рекомендуется.

Другие варианты развёртывания см. в разделах

* [Настройка интеграции логов и метрик Dynatrace с Google Cloud в существующем кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Разверните мониторинг логов и метрик для сервисов Google Cloud в существующем стандартном кластере GKE или кластере GKE Autopilot")
* [Настройка интеграции метрик Dynatrace с Google Cloud в кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only "Настройте мониторинг метрик для сервисов Google Cloud в кластере GKE.")
* [Настройка интеграции логов Dynatrace с Google Cloud в кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only "Настройте мониторинг логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")
* [Развёртывание интеграции метрик Dynatrace с Google Cloud в Google Cloud Function](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Настройте мониторинг сервисов Google Cloud в Google Cloud Functions.")

[Основное развёртывание](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") описывает, как установить версию 1.0 интеграции с Google Cloud в кластере GKE. Если у вас уже установлены более ранние версии, необходимо выполнить [миграцию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.").

После развёртывания интеграции [метрики в Dynatrace можно отправлять из нескольких проектов Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправляйте метрики в Dynatrace из нескольких проектов Google Cloud.").

Чтобы проверить, правильно ли ваша функция мониторинга обрабатывает и отправляет логи в Dynatrace, см. [Самомониторинг интеграции Dynatrace с Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли ваша функция самомониторинга обрабатывает и отправляет логи в Dynatrace.").

## Потребление мониторинга

### Приём метрик

Все облачные сервисы потребляют DDU. Объём потребления DDU на один экземпляр сервиса зависит от числа отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. [Расширение Dynatrace (единицы Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление при мониторинге Dynatrace на основе единиц Davis data units (DDU).").

### Приём логов

Потребление DDU применяется к облачному Log Monitoring. Подробнее см. [DDU для Log Monitoring Classic](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")