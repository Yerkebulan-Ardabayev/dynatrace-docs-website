---
title: Пересылка логов облачных провайдеров (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding
scraped: 2026-05-12T11:13:10.794964
---

# Пересылка логов облачных провайдеров (Logs Classic)

# Пересылка логов облачных провайдеров (Logs Classic)

* Обзор
* Чтение: 3 мин
* Обновлено 18 января 2023 г.

Log Monitoring Classic

Dynatrace версии 1.230+

Потребление DDU для Log Monitoring

На облачный Log Monitoring распространяется тарификация DDU. Подробнее см. в разделе [DDU для Log Monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Amazon Web Services

Передавайте или пересылайте логи из Amazon CloudWatch, AWS S3 или других источников AWS.

### Потоковая передача логов через Amazon Data Firehose

Интеграция Dynatrace с Amazon Data Firehose обеспечивает простой и безопасный способ приёма логов AWS.

Чтобы включить пересылку логов AWS:

1. Создайте экземпляр Amazon Data Firehose.
2. Настройте его, указав вашу среду Dynatrace в качестве назначения.
3. Подключите группы логов CloudWatch, создав фильтр подписки, или отправляйте логи напрямую в Firehose из сервисов, поддерживающих это (например, VPC Flow Logs).
   За использование Firehose и других созданных облачных ресурсов взимается плата в соответствии со стандартной политикой тарификации AWS.

Подробнее см. в разделе [Потоковая передача логов через Amazon Data Firehose (Logs Classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция Amazon Data Firehose позволяет напрямую принимать облачные логи с высокой пропускной способностью.").

### Приём логов из Amazon S3

Вы можете передавать логи из AWS S3 в Dynatrace, используя бессерверную архитектуру.

Пересылчик логов предоставляет:

* Готовый разбор сервисов AWS — см. [Поддерживаемые сервисы AWS](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder#supported-aws-services)
* Механизм обработки для любых других сценариев, включая сторонние логи, записанные в S3 — см. [Обработка логов](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_processing.md#log-processing)
* Поддержку нескольких регионов — см. [Бакеты S3 в разных регионах AWS](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-regions)
* Поддержку нескольких аккаунтов AWS — см. [Бакеты S3 в разных аккаунтах AWS](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-accounts)

Подробные инструкции по настройке приёма логов из AWS S3 см. в [документации на GitHub](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder).

### Сбор логов AWS Lambda

Вы можете собирать логи непосредственно из функций AWS Lambda и отправлять их в Dynatrace для анализа. Это решение является альтернативой пересылчику логов CloudWatch с преимуществами в плане стоимости и задержки, а также проще настраивается, особенно если трассировка AWS Lambda уже включена. В рамках процесса установки OneAgent данная функция обеспечивает оптимизированный сбор логов из функций Lambda. Подробнее см. в разделе [Документация по AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Сбор логов из функций AWS Lambda").

### Мониторинг логов AWS с использованием пересылчика логов (устаревший способ)

Вы можете передавать логи из Amazon CloudWatch в Dynatrace через ActiveGate.

Для включения пересылки логов AWS необходимо развернуть специализированный стек CloudFormation в вашем аккаунте AWS. Стек состоит из экземпляра Kinesis Firehose и функции Lambda. За эти ресурсы взимается плата по стандартной политике тарификации AWS. То же самое относится к ресурсам самомониторинга (дашборды и метрики CloudWatch).

Подробные инструкции по настройке пересылки логов AWS см. в разделе [Мониторинг логов с пересылчиком логов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder#prereq "Используйте пересылку логов AWS для приёма логов AWS.").

## Microsoft Azure

Пересылка логов Azure позволяет передавать логи Azure из Azure Event Hubs в Dynatrace через экземпляр Azure Function App. Поддерживаются как журналы ресурсов Azure, так и журналы действий.

Пересылка логов Azure выполняется напрямую через Cluster API. Если вы не хотите использовать прямой приём через Cluster API, необходимо использовать существующий ActiveGate для приёма логов.

В результате развёртывания пересылчика логов Azure создаются следующие ресурсы:

* Учётная запись хранения (`Microsoft.Storage/storageAccounts`)
* Служба BLOB-хранилища (`Microsoft.Storage/storageAccounts/blobServices`)
* План обслуживания приложений Azure (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Пересылчик логов Azure использует функцию Azure на базе Linux по умолчанию. Функции на базе Windows не поддерживаются.

Подробности о создаваемых ресурсах см. в [файле Azure Resource Manager на GitHub](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json).

Подробные инструкции по настройке пересылки логов Azure см. в разделе [Логи Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure#prereq "Используйте пересылку логов Azure для приёма логов Azure.").

## Google Cloud

Для настройки мониторинга Google Cloud для метрик и логов необходимо запустить скрипт развёртывания в Google Cloud Shell. В процессе настройки будет создана новая подписка Pub/Sub. GKE запустит два контейнера: пересылчик метрик и пересылчик логов. После установки в Dynatrace появятся метрики, логи, дашборды и алерты для настроенных сервисов. Инструкции зависят от места запуска скрипта развёртывания:

* [На новом кластере GKE Autopilot, созданном автоматически](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.") — рекомендуется
* [На существующем кластере GKE standard или GKE Autopilot](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Развёртывание мониторинга логов и метрик для сервисов Google Cloud на существующем кластере GKE standard или GKE Autopilot")

В зависимости от места выполнения приёма логов могут потребоваться дополнительные ресурсы. Например, для развёртываний Managed существует возможность использовать ActiveGate для приёма логов. Однако это необходимо сделать вручную, поскольку скрипт установки не выполняет его развёртывание.

Все варианты приёма логов см. в разделе [Приём логов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#ingestion "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

## Связанные темы

* [DDU для Log Monitoring Classic](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.")