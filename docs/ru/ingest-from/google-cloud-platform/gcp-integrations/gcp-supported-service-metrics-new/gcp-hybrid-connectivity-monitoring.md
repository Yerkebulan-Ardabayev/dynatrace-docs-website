---
title: Мониторинг Google Cloud Hybrid Connectivity
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring
scraped: 2026-03-06T21:26:19.503219
---

* 2 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в браузере метрик, Data Explorer, а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud Hybrid Connectivity доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_router/default\_metrics | Количество полученных маршрутов | Count | router.googleapis.com/best\_received\_routes\_count |
| gce\_router/default\_metrics | Интервалы получения управляющих пакетов BFD | MilliSecond | router.googleapis.com/bfd/control/receive\_intervals |
| gce\_router/default\_metrics | Полученных управляющих пакетов | Count | router.googleapis.com/bfd/control/received\_packets\_count |
| gce\_router/default\_metrics | Отклонённых управляющих пакетов | Count | router.googleapis.com/bfd/control/rejected\_packets\_count |
| gce\_router/default\_metrics | Интервалы передачи управляющих пакетов BFD | MilliSecond | router.googleapis.com/bfd/control/transmit\_intervals |
| gce\_router/default\_metrics | Переданных управляющих пакетов | Count | router.googleapis.com/bfd/control/transmitted\_packets\_count |
| gce\_router/default\_metrics | Статус сессии BFD | Count | router.googleapis.com/bfd/session\_up |
| gce\_router/default\_metrics | Количество полученных маршрутов BGP | Count | router.googleapis.com/bgp/received\_routes\_count |
| gce\_router/default\_metrics | Количество отправленных маршрутов BGP | Count | router.googleapis.com/bgp/sent\_routes\_count |
| gce\_router/default\_metrics | Статус сессии BGP | Count | router.googleapis.com/bgp/session\_up |
| gce\_router/default\_metrics | Количество неактивных сессий BGP | Count | router.googleapis.com/bgp\_sessions\_down\_count |
| gce\_router/default\_metrics | Количество активных сессий BGP | Count | router.googleapis.com/bgp\_sessions\_up\_count |
| gce\_router/default\_metrics | Статус маршрутизатора | Count | router.googleapis.com/router\_up |
| gce\_router/default\_metrics | Количество отправленных маршрутов | Count | router.googleapis.com/sent\_routes\_count |
| interconnect/default\_metrics | Пропускная способность сети | BytePerSecond | interconnect.googleapis.com/network/interconnect/capacity |
| interconnect/default\_metrics | Потерянных пакетов | Unspecified | interconnect.googleapis.com/network/interconnect/dropped\_packets\_count |
| interconnect/default\_metrics | Рабочий статус канала | Unspecified | interconnect.googleapis.com/network/interconnect/link/operational |
| interconnect/default\_metrics | Мощность приёма канала | Unspecified | interconnect.googleapis.com/network/interconnect/link/rx\_power |
| interconnect/default\_metrics | Мощность передачи канала | Unspecified | interconnect.googleapis.com/network/interconnect/link/tx\_power |
| interconnect/default\_metrics | Рабочий статус | Unspecified | interconnect.googleapis.com/network/interconnect/operational |
| interconnect/default\_metrics | Ошибки входящего трафика | Unspecified | interconnect.googleapis.com/network/interconnect/receive\_errors\_count |
| interconnect/default\_metrics | Входящих байт | Byte | interconnect.googleapis.com/network/interconnect/received\_bytes\_count |
| interconnect/default\_metrics | Входящих юникаст-пакетов | Unspecified | interconnect.googleapis.com/network/interconnect/received\_unicast\_packets\_count |
| interconnect/default\_metrics | Ошибки исходящего трафика | Unspecified | interconnect.googleapis.com/network/interconnect/send\_errors\_count |
| interconnect/default\_metrics | Исходящих байт | Byte | interconnect.googleapis.com/network/interconnect/sent\_bytes\_count |
| interconnect/default\_metrics | Исходящих юникаст-пакетов | Unspecified | interconnect.googleapis.com/network/interconnect/sent\_unicast\_packets\_count |
| vpn\_gateway/default\_metrics | Количество подключений | Count | vpn.googleapis.com/gateway/connections |
| vpn\_gateway/default\_metrics | Потерянных входящих пакетов | Count | vpn.googleapis.com/network/dropped\_received\_packets\_count |
| vpn\_gateway/default\_metrics | Потерянных исходящих пакетов | Count | vpn.googleapis.com/network/dropped\_sent\_packets\_count |
| vpn\_gateway/default\_metrics | Полученных байт | Byte | vpn.googleapis.com/network/received\_bytes\_count |
| vpn\_gateway/default\_metrics | Полученных пакетов | Unspecified | vpn.googleapis.com/network/received\_packets\_count |
| vpn\_gateway/default\_metrics | Отправленных байт | Byte | vpn.googleapis.com/network/sent\_bytes\_count |
| vpn\_gateway/default\_metrics | Отправленных пакетов | Unspecified | vpn.googleapis.com/network/sent\_packets\_count |
| vpn\_gateway/default\_metrics | Туннель установлен | Count | vpn.googleapis.com/tunnel\_established |
| interconnect\_attachment/default\_metrics | Пропускная способность сети | BytePerSecond | interconnect.googleapis.com/network/attachment/capacity |
| interconnect\_attachment/default\_metrics | Входящих байт | Byte | interconnect.googleapis.com/network/attachment/received\_bytes\_count |
| interconnect\_attachment/default\_metrics | Входящих пакетов | Unspecified | interconnect.googleapis.com/network/attachment/received\_packets\_count |
| interconnect\_attachment/default\_metrics | Исходящих байт | Byte | interconnect.googleapis.com/network/attachment/sent\_bytes\_count |
| interconnect\_attachment/default\_metrics | Исходящих пакетов | Unspecified | interconnect.googleapis.com/network/attachment/sent\_packets\_count |

## Связанные темы

* Интеграции Google Cloud
