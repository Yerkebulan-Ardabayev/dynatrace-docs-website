---
title: Google Cloud Data Loss Prevention monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring
scraped: 2026-03-03T21:28:51.746646
---

# Google Cloud Data Loss Prevention monitoring

# Google Cloud Data Loss Prevention monitoring

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собираемые из Google Operation API, для постоянного мониторинга состояния и производительности сервисов Google Cloud. Объединяя все релевантные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройте мониторинг журналов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройте мониторинг журналов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете видеть метрики отслеживаемых сервисов в [обозревателе метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просматривайте метрики с помощью обозревателя метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных.") и плитках дашборда.

## Таблица метрик

Для Google Cloud Data Loss Prevention доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_dlp\_project/default\_metrics | Content bytes inspected | Байт | dlp.googleapis.com/content\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Content bytes transformed | Байт | dlp.googleapis.com/content\_bytes\_transformed\_count |
| cloud\_dlp\_project/default\_metrics | Findings | Количество | dlp.googleapis.com/finding\_count |
| cloud\_dlp\_project/default\_metrics | Job results | Количество | dlp.googleapis.com/job\_result\_count |
| cloud\_dlp\_project/default\_metrics | Job trigger runs | Количество | dlp.googleapis.com/job\_trigger\_run\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes inspected | Байт | dlp.googleapis.com/storage\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes transformed | Байт | dlp.googleapis.com/storage\_bytes\_transformed\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройте и сконфигурируйте Dynatrace в Google Cloud.")
