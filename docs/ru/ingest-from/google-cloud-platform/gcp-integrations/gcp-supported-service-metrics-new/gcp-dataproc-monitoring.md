---
title: Мониторинг Google Cloud Dataproc
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring
scraped: 2026-03-06T21:37:51.032158
---

# Мониторинг Google Cloud Dataproc


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

Для Google Cloud Dataproc доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_dataproc\_cluster/default\_metrics | HDFS DataNodes | Count | dataproc.googleapis.com/cluster/hdfs/datanodes |
| cloud\_dataproc\_cluster/default\_metrics | Ёмкость HDFS | GibiByte | dataproc.googleapis.com/cluster/hdfs/storage\_capacity |
| cloud\_dataproc\_cluster/default\_metrics | Утилизация хранилища HDFS | Count | dataproc.googleapis.com/cluster/hdfs/storage\_utilization |
| cloud\_dataproc\_cluster/default\_metrics | Неработоспособных блоков HDFS по статусу | Count | dataproc.googleapis.com/cluster/hdfs/unhealthy\_blocks |
| cloud\_dataproc\_cluster/default\_metrics | Длительность задания | Second | dataproc.googleapis.com/cluster/job/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Длительность состояния задания | Second | dataproc.googleapis.com/cluster/job/duration |
| cloud\_dataproc\_cluster/default\_metrics | Неудачных заданий | Count | dataproc.googleapis.com/cluster/job/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Выполняемых заданий | Count | dataproc.googleapis.com/cluster/job/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Отправленных заданий | Count | dataproc.googleapis.com/cluster/job/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Длительность операции | Second | dataproc.googleapis.com/cluster/operation/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Длительность состояния операции | Second | dataproc.googleapis.com/cluster/operation/duration |
| cloud\_dataproc\_cluster/default\_metrics | Неудачных операций | Count | dataproc.googleapis.com/cluster/operation/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Выполняемых операций | Count | dataproc.googleapis.com/cluster/operation/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Отправленных операций | Count | dataproc.googleapis.com/cluster/operation/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Процент выделенной памяти YARN | Count | dataproc.googleapis.com/cluster/yarn/allocated\_memory\_percentage |
| cloud\_dataproc\_cluster/default\_metrics | Активных приложений YARN | Count | dataproc.googleapis.com/cluster/yarn/apps |
| cloud\_dataproc\_cluster/default\_metrics | Контейнеры YARN | Count | dataproc.googleapis.com/cluster/yarn/containers |
| cloud\_dataproc\_cluster/default\_metrics | Размер памяти YARN | GibiByte | dataproc.googleapis.com/cluster/yarn/memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | NodeManagers YARN | Count | dataproc.googleapis.com/cluster/yarn/nodemanagers |
| cloud\_dataproc\_cluster/default\_metrics | Ожидающий объём памяти YARN | GibiByte | dataproc.googleapis.com/cluster/yarn/pending\_memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | Виртуальные ядра YARN | Count | dataproc.googleapis.com/cluster/yarn/virtual\_cores |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
