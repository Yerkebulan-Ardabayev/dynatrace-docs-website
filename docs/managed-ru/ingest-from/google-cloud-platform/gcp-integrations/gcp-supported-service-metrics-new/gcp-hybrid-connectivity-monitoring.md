---
title: Мониторинг Google Cloud Hybrid Connectivity
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring
scraped: 2026-05-12T11:51:02.936578
---

# Мониторинг Google Cloud Hybrid Connectivity

# Мониторинг Google Cloud Hybrid Connectivity

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

Для Google Cloud Hybrid Connectivity доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_router/default\_metrics | Received routes count | Количество | router.googleapis.com/best\_received\_routes\_count |
| gce\_router/default\_metrics | BFD control packets receive intervals | Миллисекунда | router.googleapis.com/bfd/control/receive\_intervals |
| gce\_router/default\_metrics | Control packets received | Количество | router.googleapis.com/bfd/control/received\_packets\_count |
| gce\_router/default\_metrics | Control packets rejected | Количество | router.googleapis.com/bfd/control/rejected\_packets\_count |
| gce\_router/default\_metrics | BFD control packets transmit intervals | Миллисекунда | router.googleapis.com/bfd/control/transmit\_intervals |
| gce\_router/default\_metrics | Control packets transmitted | Количество | router.googleapis.com/bfd/control/transmitted\_packets\_count |
| gce\_router/default\_metrics | BFD session status | Количество | router.googleapis.com/bfd/session\_up |
| gce\_router/default\_metrics | BGP received routes count | Количество | router.googleapis.com/bgp/received\_routes\_count |
| gce\_router/default\_metrics | BGP sent routes count | Количество | router.googleapis.com/bgp/sent\_routes\_count |
| gce\_router/default\_metrics | BGP session status | Количество | router.googleapis.com/bgp/session\_up |
| gce\_router/default\_metrics | BGP sessions down count | Количество | router.googleapis.com/bgp\_sessions\_down\_count |
| gce\_router/default\_metrics | BGP sessions up count | Количество | router.googleapis.com/bgp\_sessions\_up\_count |
| gce\_router/default\_metrics | Router status | Количество | router.googleapis.com/router\_up |
| gce\_router/default\_metrics | Sent routes count | Количество | router.googleapis.com/sent\_routes\_count |
| interconnect/default\_metrics | Network Capacity | Байт/с | interconnect.googleapis.com/network/interconnect/capacity |
| interconnect/default\_metrics | Dropped Packets | Не указано | interconnect.googleapis.com/network/interconnect/dropped\_packets\_count |
| interconnect/default\_metrics | Circuit Operational Status | Не указано | interconnect.googleapis.com/network/interconnect/link/operational |
| interconnect/default\_metrics | Circuit Receive Power | Не указано | interconnect.googleapis.com/network/interconnect/link/rx\_power |
| interconnect/default\_metrics | Circuit Transmit Power | Не указано | interconnect.googleapis.com/network/interconnect/link/tx\_power |
| interconnect/default\_metrics | Operational Status | Не указано | interconnect.googleapis.com/network/interconnect/operational |
| interconnect/default\_metrics | Ingress Errors | Не указано | interconnect.googleapis.com/network/interconnect/receive\_errors\_count |
| interconnect/default\_metrics | Ingress Bytes | Байт | interconnect.googleapis.com/network/interconnect/received\_bytes\_count |
| interconnect/default\_metrics | Ingress Unicast Packets | Не указано | interconnect.googleapis.com/network/interconnect/received\_unicast\_packets\_count |
| interconnect/default\_metrics | Egress Errors | Не указано | interconnect.googleapis.com/network/interconnect/send\_errors\_count |
| interconnect/default\_metrics | Egress Bytes | Байт | interconnect.googleapis.com/network/interconnect/sent\_bytes\_count |
| interconnect/default\_metrics | Egress Unicast Packets | Не указано | interconnect.googleapis.com/network/interconnect/sent\_unicast\_packets\_count |
| vpn\_gateway/default\_metrics | Number of connections | Количество | vpn.googleapis.com/gateway/connections |
| vpn\_gateway/default\_metrics | Incoming packets dropped | Количество | vpn.googleapis.com/network/dropped\_received\_packets\_count |
| vpn\_gateway/default\_metrics | Outgoing packets dropped | Количество | vpn.googleapis.com/network/dropped\_sent\_packets\_count |
| vpn\_gateway/default\_metrics | Received bytes | Байт | vpn.googleapis.com/network/received\_bytes\_count |
| vpn\_gateway/default\_metrics | Received packets | Не указано | vpn.googleapis.com/network/received\_packets\_count |
| vpn\_gateway/default\_metrics | Sent bytes | Байт | vpn.googleapis.com/network/sent\_bytes\_count |
| vpn\_gateway/default\_metrics | Sent packets | Не указано | vpn.googleapis.com/network/sent\_packets\_count |
| vpn\_gateway/default\_metrics | Tunnel established | Количество | vpn.googleapis.com/tunnel\_established |
| interconnect\_attachment/default\_metrics | Network Capacity | Байт/с | interconnect.googleapis.com/network/attachment/capacity |
| interconnect\_attachment/default\_metrics | Ingress Bytes | Байт | interconnect.googleapis.com/network/attachment/received\_bytes\_count |
| interconnect\_attachment/default\_metrics | Ingress Packets | Не указано | interconnect.googleapis.com/network/attachment/received\_packets\_count |
| interconnect\_attachment/default\_metrics | Egress Bytes | Байт | interconnect.googleapis.com/network/attachment/sent\_bytes\_count |
| interconnect\_attachment/default\_metrics | Egress Packets | Не указано | interconnect.googleapis.com/network/attachment/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")