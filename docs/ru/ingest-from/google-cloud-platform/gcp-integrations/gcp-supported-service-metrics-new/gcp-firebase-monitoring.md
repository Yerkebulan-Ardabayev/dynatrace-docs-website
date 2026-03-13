---
title: Google Cloud Firebase monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring
scraped: 2026-03-04T21:37:39.481282
---

# Мониторинг Google Cloud Firebase

# Мониторинг Google Cloud Firebase

* Последняя версия Dynatrace
* Практическое руководство
* Чтение займёт 1 минуту
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные на панелях мониторинга, интеграция также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление и удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и на плитках панелей мониторинга.

## Таблица метрик

Для Google Cloud Firebase доступны следующие наборы функций.

| Набор функций | Имя | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| firebase\_domain/default\_metrics | Лимит хранимых байтов | Byte | firebasehosting.googleapis.com/storage/limit |
| firebase\_domain/default\_metrics | Хранимые байты | Byte | firebasehosting.googleapis.com/storage/total\_bytes |
| firebase\_namespace/default\_metrics | Загрузка базы данных | Count | firebasedatabase.googleapis.com/io/database\_load |
| firebase\_namespace/default\_metrics | Сохранённые байты | Byte | firebasedatabase.googleapis.com/io/persisted\_bytes\_count |
| firebase\_namespace/default\_metrics | Отправлено ответов | Count | firebasedatabase.googleapis.com/io/sent\_responses\_count |
| firebase\_namespace/default\_metrics | Использование I/O | Count | firebasedatabase.googleapis.com/io/utilization |
| firebase\_namespace/default\_metrics | Подключения | Count | firebasedatabase.googleapis.com/network/active\_connections |
| firebase\_namespace/default\_metrics | Обращений к API | Count | firebasedatabase.googleapis.com/network/api\_hits\_count |
| firebase\_namespace/default\_metrics | Загрузка широковещательных рассылок | Count | firebasedatabase.googleapis.com/network/broadcast\_load |
| firebase\_namespace/default\_metrics | Отключено по сети | Unspecified | firebasedatabase.googleapis.com/network/disabled\_for\_overages |
| firebase\_namespace/default\_metrics | Получено HTTPS-запросов | Count | firebasedatabase.googleapis.com/network/https\_requests\_count |
| firebase\_namespace/default\_metrics | Отправлено байт за месяц | Byte | firebasedatabase.googleapis.com/network/monthly\_sent |
| firebase\_namespace/default\_metrics | Лимит отправленных байтов | Byte | firebasedatabase.googleapis.com/network/monthly\_sent\_limit |
| firebase\_namespace/default\_metrics | Всего тарифицируемых байтов | Byte | firebasedatabase.googleapis.com/network/sent\_bytes\_count |
| firebase\_namespace/default\_metrics | Отправлено байтов полезной нагрузки и протокола | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_and\_protocol\_bytes\_count |
| firebase\_namespace/default\_metrics | Отправлено байтов полезной нагрузки | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_bytes\_count |
| firebase\_namespace/default\_metrics | Оценок правил | Count | firebasedatabase.googleapis.com/rules/evaluation\_count |
| firebase\_namespace/default\_metrics | Лимит хранимых байтов | Byte | firebasedatabase.googleapis.com/storage/limit |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
