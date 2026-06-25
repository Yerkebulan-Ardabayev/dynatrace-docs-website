---
title: Мониторинг Google Cloud Load Balancing
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring
scraped: 2026-05-12T11:50:34.931222
---

# Мониторинг Google Cloud Load Balancing

# Мониторинг Google Cloud Load Balancing

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Cloud Load Balancing доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| https\_lb\_rule/default\_metrics | Backend latency | Миллисекунда | loadbalancing.googleapis.com/https/backend\_latencies |
| https\_lb\_rule/default\_metrics | Backend Request Bytes | Байт | loadbalancing.googleapis.com/https/backend\_request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Backend Request Count | Количество | loadbalancing.googleapis.com/https/backend\_request\_count |
| https\_lb\_rule/default\_metrics | Backend Response Bytes | Байт | loadbalancing.googleapis.com/https/backend\_response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Frontend RTT | Миллисекунда | loadbalancing.googleapis.com/https/frontend\_tcp\_rtt |
| https\_lb\_rule/default\_metrics | Request bytes | Байт | loadbalancing.googleapis.com/https/request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Request count | Количество | loadbalancing.googleapis.com/https/request\_count |
| https\_lb\_rule/default\_metrics | Response bytes | Байт | loadbalancing.googleapis.com/https/response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Total latency | Миллисекунда | loadbalancing.googleapis.com/https/total\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Backend latencies | Миллисекунда | loadbalancing.googleapis.com/https/internal/backend\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Request bytes | Байт | loadbalancing.googleapis.com/https/internal/request\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Request count | Количество | loadbalancing.googleapis.com/https/internal/request\_count |
| internal\_http\_lb\_rule/default\_metrics | Response bytes | Байт | loadbalancing.googleapis.com/https/internal/response\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Total latencies | Миллисекунда | loadbalancing.googleapis.com/https/internal/total\_latencies |
| internal\_tcp\_lb\_rule/default\_metrics | Egress bytes | Байт | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Egress packets | Количество | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Ingress bytes | Байт | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Ingress packets | Количество | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | RTT latencies | Миллисекунда | loadbalancing.googleapis.com/l3/internal/rtt\_latencies |
| internal\_udp\_lb\_rule/default\_metrics | Egress bytes | Байт | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Egress packets | Количество | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_udp\_lb\_rule/default\_metrics | Ingress bytes | Байт | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Ingress packets | Количество | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Egress bytes | Байт | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Egress packets | Количество | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Ingress bytes | Байт | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Ingress packets | Количество | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | RTT latencies | Миллисекунда | loadbalancing.googleapis.com/l3/external/rtt\_latencies |
| udp\_lb\_rule/default\_metrics | Egress bytes | Байт | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Egress packets | Количество | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| udp\_lb\_rule/default\_metrics | Ingress bytes | Байт | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Ingress packets | Количество | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Closed connections | Количество | loadbalancing.googleapis.com/tcp\_ssl\_proxy/closed\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Egress bytes | Байт | loadbalancing.googleapis.com/tcp\_ssl\_proxy/egress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Frontend RTT | Миллисекунда | loadbalancing.googleapis.com/tcp\_ssl\_proxy/frontend\_tcp\_rtt |
| tcp\_ssl\_proxy\_rule/default\_metrics | Ingress bytes | Байт | loadbalancing.googleapis.com/tcp\_ssl\_proxy/ingress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | New connections opened | Количество | loadbalancing.googleapis.com/tcp\_ssl\_proxy/new\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Open Connections | Количество | loadbalancing.googleapis.com/tcp\_ssl\_proxy/open\_connections |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")