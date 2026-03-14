---
title: Мониторинг Google Cloud Router
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring
scraped: 2026-03-06T21:29:27.949865
---

# Мониторинг Google Cloud Router


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

Для Google Cloud Router доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| nat\_gateway/default\_metrics | Выделенные порты | Unspecified | router.googleapis.com/nat/allocated\_ports |
| nat\_gateway/default\_metrics | Количество закрытых соединений | Unspecified | router.googleapis.com/nat/closed\_connections\_count |
| nat\_gateway/default\_metrics | Количество отброшенных входящих пакетов | Unspecified | router.googleapis.com/nat/dropped\_received\_packets\_count |
| nat\_gateway/default\_metrics | Количество отброшенных исходящих пакетов | Unspecified | router.googleapis.com/nat/dropped\_sent\_packets\_count |
| nat\_gateway/default\_metrics | Сбой выделения NAT | Unspecified | router.googleapis.com/nat/nat\_allocation\_failed |
| nat\_gateway/default\_metrics | Количество новых соединений | Unspecified | router.googleapis.com/nat/new\_connections\_count |
| nat\_gateway/default\_metrics | Открытые соединения | Unspecified | router.googleapis.com/nat/open\_connections |
| nat\_gateway/default\_metrics | Использование портов | Unspecified | router.googleapis.com/nat/port\_usage |
| nat\_gateway/default\_metrics | Количество полученных байт | Byte | router.googleapis.com/nat/received\_bytes\_count |
| nat\_gateway/default\_metrics | Количество полученных пакетов | Unspecified | router.googleapis.com/nat/received\_packets\_count |
| nat\_gateway/default\_metrics | Количество отправленных байт | Byte | router.googleapis.com/nat/sent\_bytes\_count |
| nat\_gateway/default\_metrics | Количество отправленных пакетов | Unspecified | router.googleapis.com/nat/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
