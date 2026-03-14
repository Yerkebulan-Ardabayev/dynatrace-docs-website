---
title: Мониторинг Google Cloud Firebase
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring
scraped: 2026-03-04T21:37:39.481282
---

# Мониторинг Google Cloud Firebase


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

Для Google Cloud Firebase доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| firebase\_domain/default\_metrics | Лимит хранимых байтов | Byte | firebasehosting.googleapis.com/storage/limit |
| firebase\_domain/default\_metrics | Хранимые байты | Byte | firebasehosting.googleapis.com/storage/total\_bytes |
| firebase\_namespace/default\_metrics | Загрузка базы данных | Count | firebasedatabase.googleapis.com/io/database\_load |
| firebase\_namespace/default\_metrics | Сохранённых байт | Byte | firebasedatabase.googleapis.com/io/persisted\_bytes\_count |
| firebase\_namespace/default\_metrics | Отправлено ответов | Count | firebasedatabase.googleapis.com/io/sent\_responses\_count |
| firebase\_namespace/default\_metrics | Утилизация ввода-вывода | Count | firebasedatabase.googleapis.com/io/utilization |
| firebase\_namespace/default\_metrics | Подключения | Count | firebasedatabase.googleapis.com/network/active\_connections |
| firebase\_namespace/default\_metrics | Обращений к API | Count | firebasedatabase.googleapis.com/network/api\_hits\_count |
| firebase\_namespace/default\_metrics | Загрузка широковещательных рассылок | Count | firebasedatabase.googleapis.com/network/broadcast\_load |
| firebase\_namespace/default\_metrics | Отключено из-за превышения лимита | Unspecified | firebasedatabase.googleapis.com/network/disabled\_for\_overages |
| firebase\_namespace/default\_metrics | Получено HTTPS-запросов | Count | firebasedatabase.googleapis.com/network/https\_requests\_count |
| firebase\_namespace/default\_metrics | Отправлено байт за месяц | Byte | firebasedatabase.googleapis.com/network/monthly\_sent |
| firebase\_namespace/default\_metrics | Лимит отправленных байтов | Byte | firebasedatabase.googleapis.com/network/monthly\_sent\_limit |
| firebase\_namespace/default\_metrics | Всего тарифицируемых байтов | Byte | firebasedatabase.googleapis.com/network/sent\_bytes\_count |
| firebase\_namespace/default\_metrics | Отправлено байтов полезной нагрузки и протокола | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_and\_protocol\_bytes\_count |
| firebase\_namespace/default\_metrics | Отправлено байтов полезной нагрузки | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_bytes\_count |
| firebase\_namespace/default\_metrics | Вычисления правил | Count | firebasedatabase.googleapis.com/rules/evaluation\_count |
| firebase\_namespace/default\_metrics | Лимит хранимых байтов | Byte | firebasedatabase.googleapis.com/storage/limit |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
