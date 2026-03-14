---
title: Мониторинг Google Cloud Load Balancing
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring
scraped: 2026-03-06T21:33:09.848966
---

# Мониторинг Google Cloud Load Balancing


* Последняя версия Dynatrace
* Практическое руководство
* 2 мин. чтения
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

Для Google Cloud Load Balancing доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| https\_lb\_rule/default\_metrics | Задержка бэкенда | MilliSecond | loadbalancing.googleapis.com/https/backend\_latencies |
| https\_lb\_rule/default\_metrics | Байт запросов бэкенда | Byte | loadbalancing.googleapis.com/https/backend\_request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Количество запросов к бэкенду | Count | loadbalancing.googleapis.com/https/backend\_request\_count |
| https\_lb\_rule/default\_metrics | Байт ответов бэкенда | Byte | loadbalancing.googleapis.com/https/backend\_response\_bytes\_count |
| https\_lb\_rule/default\_metrics | RTT фронтенда | MilliSecond | loadbalancing.googleapis.com/https/frontend\_tcp\_rtt |
| https\_lb\_rule/default\_metrics | Байт запросов | Byte | loadbalancing.googleapis.com/https/request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Количество запросов | Count | loadbalancing.googleapis.com/https/request\_count |
| https\_lb\_rule/default\_metrics | Байт ответов | Byte | loadbalancing.googleapis.com/https/response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Суммарная задержка | MilliSecond | loadbalancing.googleapis.com/https/total\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Задержки бэкенда | MilliSecond | loadbalancing.googleapis.com/https/internal/backend\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Байт запросов | Byte | loadbalancing.googleapis.com/https/internal/request\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Количество запросов | Count | loadbalancing.googleapis.com/https/internal/request\_count |
| internal\_http\_lb\_rule/default\_metrics | Байт ответов | Byte | loadbalancing.googleapis.com/https/internal/response\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Суммарные задержки | MilliSecond | loadbalancing.googleapis.com/https/internal/total\_latencies |
| internal\_tcp\_lb\_rule/default\_metrics | Исходящих байт | Byte | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Исходящих пакетов | Count | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Входящих байт | Byte | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Входящих пакетов | Count | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | RTT-задержки | MilliSecond | loadbalancing.googleapis.com/l3/internal/rtt\_latencies |
| internal\_udp\_lb\_rule/default\_metrics | Исходящих байт | Byte | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Исходящих пакетов | Count | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_udp\_lb\_rule/default\_metrics | Входящих байт | Byte | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Входящих пакетов | Count | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Исходящих байт | Byte | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Исходящих пакетов | Count | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Входящих байт | Byte | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Входящих пакетов | Count | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | RTT-задержки | MilliSecond | loadbalancing.googleapis.com/l3/external/rtt\_latencies |
| udp\_lb\_rule/default\_metrics | Исходящих байт | Byte | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Исходящих пакетов | Count | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| udp\_lb\_rule/default\_metrics | Входящих байт | Byte | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Входящих пакетов | Count | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Закрытых соединений | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/closed\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Исходящих байт | Byte | loadbalancing.googleapis.com/tcp\_ssl\_proxy/egress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | RTT фронтенда | MilliSecond | loadbalancing.googleapis.com/tcp\_ssl\_proxy/frontend\_tcp\_rtt |
| tcp\_ssl\_proxy\_rule/default\_metrics | Входящих байт | Byte | loadbalancing.googleapis.com/tcp\_ssl\_proxy/ingress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Открытых новых соединений | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/new\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Открытых соединений | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/open\_connections |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
