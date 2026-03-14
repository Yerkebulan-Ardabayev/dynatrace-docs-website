---
title: Комплексное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide
scraped: 2026-03-03T21:24:19.522416
---

# Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite

# Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite

* Latest Dynatrace
* Обзор
* Чтение: 2 мин
* Опубликовано 17 января 2022 г.

Dynatrace превосходно интегрируется с Google Cloud, обеспечивая глубокую видимость рабочих нагрузок, выполняющихся на этой платформе.

## Поддерживаемые сервисы Google Cloud

Dynatrace может анализировать метрики всех сервисов, доступных в Google Operations API. Чтобы узнать о мониторинге поддерживаемых сервисов Google Cloud, возможностях и параметрах конфигурации, см. [Метрики поддерживаемых сервисов Google Cloud](gcp-supported-service-metrics-new.md "Мониторинг сервисов Google Cloud с Dynatrace и просмотр доступных метрик.").

## Обзор Google Cloud

Dynatrace предоставляет страницу обзора Google Cloud. Она включает представления по проектам Google Cloud и списки экземпляров для виртуальных машин, SQL, Cloud Functions и Kubernetes.

Если вы уже ведёте мониторинг Google Cloud, а обзор недоступен, вам необходимо обновить имеющуюся интеграцию Google Cloud.

## Настройка приёма метрик и логов

Чтобы начать анализ метрик и логов всех сервисов, доступных в Google Operations API, см. [Настройка интеграции метрик и логов Dynatrace для Google Cloud на новом кластере GKE Autopilot](gcp-guide/deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.") (Рекомендуется).

Другие варианты развёртывания:

* [Настройка интеграции логов и метрик Dynatrace для Google Cloud на существующем кластере GKE](gcp-guide/set-up-gcp-integration-on-existing-cluster.md "Развёртывание мониторинга логов и метрик для сервисов Google Cloud на существующем стандартном кластере GKE или GKE Autopilot")
* [Настройка интеграции метрик Dynatrace для Google Cloud на кластере GKE](gcp-guide/set-up-gcp-integration-metrics-only.md "Настройка мониторинга метрик для сервисов Google Cloud на кластере GKE.")
* [Настройка интеграции логов Dynatrace для Google Cloud на кластере GKE](gcp-guide/set-up-gcp-integration-logs-only.md "Настройка мониторинга логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")
* [Развёртывание интеграции метрик Dynatrace для Google Cloud в Google Cloud Function](gcp-guide/deploy-with-google-cloud-function.md "Настройка мониторинга сервисов Google Cloud в Google Cloud Functions.")

В [основном руководстве по развёртыванию](gcp-guide/deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.") описано, как установить версию 1.0 интеграции Google Cloud на кластере GKE. Если у вас уже установлены более ранние версии, вам необходимо выполнить [миграцию](gcp-guide/migrate-gcp-function.md "Миграция с версии 0.1 интеграции Google Cloud на версию 1.0 в Kubernetes и в виде Google Cloud Function.").

После развёртывания интеграции [вы можете передавать метрики в Dynatrace из нескольких проектов Google Cloud](gcp-guide/monitor-multiple-projects.md "Передавайте метрики в Dynatrace из нескольких проектов Google Cloud.").

Чтобы проверить, правильно ли ваша функция мониторинга обрабатывает и отправляет логи в Dynatrace, см. [Самомониторинг для интеграции Dynatrace с Google Cloud](gcp-guide/deploy-k8/self-monitoring-gcp.md "Определите, правильно ли ваша функция самомониторинга обрабатывает и отправляет логи в Dynatrace.").

## Мониторинг потребления

### Приём метрик

Все облачные сервисы потребляют DDU (единицы данных Davis). Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. [Расширение Dynatrace (единицы данных Davis)](../../../license/monitoring-consumption-classic/davis-data-units.md "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).").

### Приём логов

Потребление DDU применяется к облачному Log Monitoring. Подробнее см. [DDU для Log Monitoring](../../../license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption.md "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Настройка Dynatrace в Google Cloud](../../google-cloud-platform.md "Мониторинг Google Cloud с Dynatrace.")
