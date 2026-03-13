---
title: Google Cloud supported services
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new
scraped: 2026-03-06T21:18:05.172973
---

# Поддерживаемые сервисы Google Cloud

# Поддерживаемые сервисы Google Cloud

* Последняя версия Dynatrace
* Overview
* Чтение: 3 мин
* Обновлено 23 сентября 2024 г.

Dynatrace версии 1.230+

Данный раздел относится к метрикам сервисов Google Cloud, доступным при использовании интеграции Google Cloud версии 1.0.

* Метрики сервисов Google Cloud, доступные в более ранних версиях интеграции Google Cloud, см. в разделе [Метрики поддерживаемых сервисов Google Cloud (устаревшая версия)](/docs/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Supported GCP service metrics, metrics configuration, DDU consumption, and preset dashboard availability").

## Предварительные требования

[Развёртывание интеграции Dynatrace](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Поддерживаемые сервисы для метрик

После развёртывания интеграции Dynatrace вы можете получать сведения о метриках сервисов Google Cloud, собираемых из Google Operations API, для обеспечения работоспособности вашей облачной инфраструктуры.

Ниже приведён список поддерживаемых сервисов Google Cloud.

1

Сервисы могут иметь одну сущность, несколько сущностей или ни одной. Для каждой сущности вы можете просматривать метрики, свойства, журналы, ошибки и многое другое в Dynatrace [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once.").

## Проверка доступных метрик

Чтобы проверить доступные метрики для сервиса, необходимо:

1. Найти расширение в [Hub](https://www.dynatrace.com/hub/?query=google&filter=all) и выбрать его для открытия страницы обзора. Пример: [Google Cloud Functions](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).
2. Прокрутить страницу обзора расширения вниз, чтобы найти раздел **Feature sets**.
3. В таблице выбрать раскрывающийся список **default\_metrics**.
4. Теперь можно проверить все доступные метрики для выбранного сервиса.

## Потребление при мониторинге

### Приём метрик

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. в разделе [Расширение Dynatrace (единицы данных Davis)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Приём журналов

Потребление DDU распространяется на облачный Log Monitoring. Подробнее см. в разделе [DDU для Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
