---
title: Мониторинг Google Cloud Router
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring
scraped: 2026-05-12T11:50:49.248304
---

# Мониторинг Google Cloud Router

# Мониторинг Google Cloud Router

* Практическое руководство
* Чтение: 1 мин
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

Для Google Cloud Router доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| nat\_gateway/default\_metrics | Allocated ports | Не указано | router.googleapis.com/nat/allocated\_ports |
| nat\_gateway/default\_metrics | Closed connections count | Не указано | router.googleapis.com/nat/closed\_connections\_count |
| nat\_gateway/default\_metrics | Received packets dropped count | Не указано | router.googleapis.com/nat/dropped\_received\_packets\_count |
| nat\_gateway/default\_metrics | Sent packets dropped count | Не указано | router.googleapis.com/nat/dropped\_sent\_packets\_count |
| nat\_gateway/default\_metrics | NAT allocation failed | Не указано | router.googleapis.com/nat/nat\_allocation\_failed |
| nat\_gateway/default\_metrics | New connections count | Не указано | router.googleapis.com/nat/new\_connections\_count |
| nat\_gateway/default\_metrics | Open connections | Не указано | router.googleapis.com/nat/open\_connections |
| nat\_gateway/default\_metrics | Port usage | Не указано | router.googleapis.com/nat/port\_usage |
| nat\_gateway/default\_metrics | Received bytes count | Байт | router.googleapis.com/nat/received\_bytes\_count |
| nat\_gateway/default\_metrics | Received packets count | Не указано | router.googleapis.com/nat/received\_packets\_count |
| nat\_gateway/default\_metrics | Sent bytes count | Байт | router.googleapis.com/nat/sent\_bytes\_count |
| nat\_gateway/default\_metrics | Sent packets count | Не указано | router.googleapis.com/nat/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")