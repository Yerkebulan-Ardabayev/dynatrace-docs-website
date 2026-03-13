---
title: Мониторинг Google Cloud Hybrid Connectivity
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring
scraped: 2026-03-06T21:26:19.503219
---

# Мониторинг Google Cloud Hybrid Connectivity

# Мониторинг Google Cloud Hybrid Connectivity

* Последняя версия Dynatrace
* Практическое руководство
* 2 мин. чтения
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все важные данные на дашбордах, интеграция также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, можно добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов для получения необходимых данных.") и тайлах дашборда.

## Таблица метрик

Для Google Cloud Hybrid Connectivity доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_router/default\_metrics | Received routes count | Count | router.googleapis.com/best\_received\_routes\_count |
| gce\_router/default\_metrics | BFD control packets receive intervals | MilliSecond | router.googleapis.com/bfd/control/receive\_intervals |
| gce\_router/default\_metrics | Control packets received | Count | router.googleapis.com/bfd/control/received\_packets\_count |
| gce\_router/default\_metrics | Control packets rejected | Count | router.googleapis.com/bfd/control/rejected\_packets\_count |
| gce\_router/default\_metrics | BFD control packets transmit intervals | MilliSecond | router.googleapis.com/bfd/control/transmit\_intervals |
| gce\_router/default\_metrics | Control packets transmitted | Count | router.googleapis.com/bfd/control/transmitted\_packets\_count |
| gce\_router/default\_metrics | BFD session status | Count | router.googleapis.com/bfd/session\_up |
| gce\_router/default\_metrics | BGP received routes count | Count | router.googleapis.com/bgp/received\_routes\_count |
| gce\_router/default\_metrics | BGP sent routes count | Count | router.googleapis.com/bgp/sent\_routes\_count |
| gce\_router/default\_metrics | BGP session status | Count | router.googleapis.com/bgp/session\_up |
| gce\_router/default\_metrics | BGP sessions down count | Count | router.googleapis.com/bgp\_sessions\_down\_count |
| gce\_router/default\_metrics | BGP sessions up count | Count | router.googleapis.com/bgp\_sessions\_up\_count |
| gce\_router/default\_metrics | Router status | Count | router.googleapis.com/router\_up |
| gce\_router/default\_metrics | Sent routes count | Count | router.googleapis.com/sent\_routes\_count |
| interconnect/default\_metrics | Network Capacity | BytePerSecond | interconnect.googleapis.com/network/interconnect/capacity |
| interconnect/default\_metrics | Dropped Packets | Unspecified | interconnect.googleapis.com/network/interconnect/dropped\_packets\_count |
| interconnect/default\_metrics | Circuit Operational Status | Unspecified | interconnect.googleapis.com/network/interconnect/link/operational |
| interconnect/default\_metrics | Circuit Receive Power | Unspecified | interconnect.googleapis.com/network/interconnect/link/rx\_power |
| interconnect/default\_metrics | Circuit Transmit Power | Unspecified | interconnect.googleapis.com/network/interconnect/link/tx\_power |
| interconnect/default\_metrics | Operational Status | Unspecified | interconnect.googleapis.com/network/interconnect/operational |
| interconnect/default\_metrics | Ingress Errors | Unspecified | interconnect.googleapis.com/network/interconnect/receive\_errors\_count |
| interconnect/default\_metrics | Ingress Bytes | Byte | interconnect.googleapis.com/network/interconnect/received\_bytes\_count |
| interconnect/default\_metrics | Ingress Unicast Packets | Unspecified | interconnect.googleapis.com/network/interconnect/received\_unicast\_packets\_count |
| interconnect/default\_metrics | Egress Errors | Unspecified | interconnect.googleapis.com/network/interconnect/send\_errors\_count |
| interconnect/default\_metrics | Egress Bytes | Byte | interconnect.googleapis.com/network/interconnect/sent\_bytes\_count |
| interconnect/default\_metrics | Egress Unicast Packets | Unspecified | interconnect.googleapis.com/network/interconnect/sent\_unicast\_packets\_count |
| vpn\_gateway/default\_metrics | Number of connections | Count | vpn.googleapis.com/gateway/connections |
| vpn\_gateway/default\_metrics | Incoming packets dropped | Count | vpn.googleapis.com/network/dropped\_received\_packets\_count |
| vpn\_gateway/default\_metrics | Outgoing packets dropped | Count | vpn.googleapis.com/network/dropped\_sent\_packets\_count |
| vpn\_gateway/default\_metrics | Received bytes | Byte | vpn.googleapis.com/network/received\_bytes\_count |
| vpn\_gateway/default\_metrics | Received packets | Unspecified | vpn.googleapis.com/network/received\_packets\_count |
| vpn\_gateway/default\_metrics | Sent bytes | Byte | vpn.googleapis.com/network/sent\_bytes\_count |
| vpn\_gateway/default\_metrics | Sent packets | Unspecified | vpn.googleapis.com/network/sent\_packets\_count |
| vpn\_gateway/default\_metrics | Tunnel established | Count | vpn.googleapis.com/tunnel\_established |
| interconnect\_attachment/default\_metrics | Network Capacity | BytePerSecond | interconnect.googleapis.com/network/attachment/capacity |
| interconnect\_attachment/default\_metrics | Ingress Bytes | Byte | interconnect.googleapis.com/network/attachment/received\_bytes\_count |
| interconnect\_attachment/default\_metrics | Ingress Packets | Unspecified | interconnect.googleapis.com/network/attachment/received\_packets\_count |
| interconnect\_attachment/default\_metrics | Egress Bytes | Byte | interconnect.googleapis.com/network/attachment/sent\_bytes\_count |
| interconnect\_attachment/default\_metrics | Egress Packets | Unspecified | interconnect.googleapis.com/network/attachment/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")
