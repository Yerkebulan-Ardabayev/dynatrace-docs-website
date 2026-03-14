---
title: Мониторинг Google Cloud Composer
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring
scraped: 2026-03-04T21:37:01.937241
---

# Мониторинг Google Cloud Composer


* Последняя версия Dynatrace
* Практическое руководство
* 1 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud Composer доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_composer\_environment/default\_metrics | API-запросы | Count | composer.googleapis.com/environment/api/request\_count |
| cloud\_composer\_environment/default\_metrics | Задержка API | MilliSecond | composer.googleapis.com/environment/api/request\_latencies |
| cloud\_composer\_environment/default\_metrics | Количество ошибок разбора | Count | composer.googleapis.com/environment/dag\_processing/parse\_error\_count |
| cloud\_composer\_environment/default\_metrics | Процессы разбора DAG | Count | composer.googleapis.com/environment/dag\_processing/processes |
| cloud\_composer\_environment/default\_metrics | Количество таймаутов процессоров | Count | composer.googleapis.com/environment/dag\_processing/processor\_timeout\_count |
| cloud\_composer\_environment/default\_metrics | Суммарное время разбора | Second | composer.googleapis.com/environment/dag\_processing/total\_parse\_time |
| cloud\_composer\_environment/default\_metrics | Размер Dag Bag | Count | composer.googleapis.com/environment/dagbag\_size |
| cloud\_composer\_environment/default\_metrics | База данных работоспособна | Unspecified | composer.googleapis.com/environment/database\_health |
| cloud\_composer\_environment/default\_metrics | Свободные слоты исполнителя | Count | composer.googleapis.com/environment/executor/open\_slots |
| cloud\_composer\_environment/default\_metrics | Задачи исполнителя в работе | Count | composer.googleapis.com/environment/executor/running\_tasks |
| cloud\_composer\_environment/default\_metrics | Количество экземпляров задач | Count | composer.googleapis.com/environment/finished\_task\_instance\_count |
| cloud\_composer\_environment/default\_metrics | Работоспособен | Unspecified | composer.googleapis.com/environment/healthy |
| cloud\_composer\_environment/default\_metrics | Рабочие Celery | Count | composer.googleapis.com/environment/num\_celery\_workers |
| cloud\_composer\_environment/default\_metrics | Сигналы жизнеспособности планировщика | Count | composer.googleapis.com/environment/scheduler\_heartbeat\_count |
| cloud\_composer\_environment/default\_metrics | Длина очереди задач | Count | composer.googleapis.com/environment/task\_queue\_length |
| cloud\_composer\_environment/default\_metrics | Количество вытеснений подов воркеров | Count | composer.googleapis.com/environment/worker/pod\_eviction\_count |
| cloud\_composer\_environment/default\_metrics | Уничтоженных зомби-задач | Count | composer.googleapis.com/environment/zombie\_task\_killed\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
