---
title: Google Cloud Virtual Private Cloud (VPC) monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-virtual-private-cloud-monitoring
scraped: 2026-03-06T21:33:45.103383
---

# Мониторинг Google Cloud Virtual Private Cloud (VPC)

# Мониторинг Google Cloud Virtual Private Cloud (VPC)

* Последняя версия Dynatrace
* Практическое руководство
* 1 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в [Таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [Браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Выполняйте запросы к метрикам и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud VPC.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| vpc\_access\_connector/default\_metrics | Загрузка ЦПУ | Процент | vpcaccess.googleapis.com/connector/cpu/utilizations |
| vpc\_access\_connector/default\_metrics | Активные экземпляры | Количество | vpcaccess.googleapis.com/connector/instances |
| vpc\_access\_connector/default\_metrics | Дельта полученных байтов | Байт | vpcaccess.googleapis.com/connector/received\_bytes\_count |
| vpc\_access\_connector/default\_metrics | Дельта полученных пакетов | Не указано | vpcaccess.googleapis.com/connector/received\_packets\_count |
| vpc\_access\_connector/default\_metrics | Дельта отправленных байтов | Байт | vpcaccess.googleapis.com/connector/sent\_bytes\_count |
| vpc\_access\_connector/default\_metrics | Дельта отправленных пакетов | Не указано | vpcaccess.googleapis.com/connector/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройте и сконфигурируйте Dynatrace в Google Cloud.")
