---
title: Пересылка журналов провайдера облака (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding
scraped: 2026-03-06T21:30:55.800554
---

# Пересылка логов от облачных провайдеров (Logs Classic)

# Пересылка логов от облачных провайдеров (Logs Classic)

* Classic
* Обзор
* Чтение: 3 мин
* Обновлено 18 января 2023 г.

Log Monitoring Classic

Dynatrace версии 1.230+

Для новейшей версии Dynatrace см. [Пересылка логов от облачных провайдеров](../../logs/lma-log-ingestion/lma-cloud-provider-log-forwarding.md "Настройте пересылку логов AWS, Azure и Google Cloud для потоковой передачи данных логов в Dynatrace с помощью API.").

Потребление DDU для Log Monitoring

Для облачного Log Monitoring применяется ценообразование на основе DDU. Подробности см. в разделе [DDU для Log Monitoring](../../../license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption.md "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

## Amazon Web Services

Потоковая передача или пересылка логов из Amazon CloudWatch, AWS S3 или других источников AWS.

### Потоковая передача логов через Amazon Data Firehose

Интеграция Dynatrace с Amazon Data Firehose обеспечивает простой и безопасный способ приёма логов AWS.

Чтобы включить пересылку логов AWS,

1. Создайте экземпляр Amazon Data Firehose.
2. Настройте его, указав среду Dynatrace в качестве назначения.
3. Подключите группы логов CloudWatch, создав фильтр подписки, или отправляйте логи напрямую в Firehose из сервисов, которые это поддерживают (например, VPC Flow Logs).
   Firehose и другие созданные облачные ресурсы влекут за собой расходы AWS в соответствии со стандартной политикой тарификации AWS.

Подробнее см. [Потоковая передача логов через Amazon Data Firehose (Logs Classic)](../../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.").

### Приём логов из Amazon S3

Вы можете осуществлять потоковую передачу логов из AWS S3 в Dynatrace с использованием бессерверной архитектуры.

Компонент пересылки логов предлагает:

* Готовый парсинг сервисов AWS, см. [Supported AWS Services](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder#supported-aws-services)
* Механизм обработки для любых других сценариев, включая логи сторонних сервисов, записываемые в S3, см. [Log Processing](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_processing.md#log-processing)
* Поддержка нескольких регионов, см. [S3 buckets on different AWS Regions](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-regions)
* Поддержка нескольких аккаунтов AWS, см. [S3 buckets on different AWS accounts](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-accounts)

Подробные инструкции по настройке приёма логов из AWS S3 см. в [документации на GitHub](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder).

### Сбор логов AWS Lambda

Вы можете собирать логи непосредственно из функций AWS Lambda и отправлять их в Dynatrace для анализа. Это решение является альтернативой компоненту пересылки логов CloudWatch с преимуществами в плане стоимости и задержки, а также более простой настройкой, особенно если трассировка AWS Lambda уже настроена. В рамках процесса установки OneAgent эта функция предоставляет оптимизированное решение для сбора логов из ваших функций Lambda. Подробнее см. [страницу документации AWS Lambda](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector.md "Сбор логов из функций AWS Lambda").

### Мониторинг логов AWS с помощью компонента пересылки Deprecated

Вы можете осуществлять потоковую передачу логов из Amazon CloudWatch в логи Dynatrace через ActiveGate.

Чтобы включить пересылку логов AWS, необходимо развернуть специальный стек CloudFormation в вашем аккаунте AWS. Стек состоит из экземпляра Kinesis Firehose и функции Lambda. Эти ресурсы влекут за собой расходы AWS в соответствии со стандартной политикой тарификации AWS. Это же относится к включённым ресурсам самомониторинга (дашборды и метрики CloudWatch).

Подробные инструкции по настройке пересылки логов AWS см. в разделе [Мониторинг логов с помощью компонента пересылки AWS](../../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder.md#prereq "Используйте пересылку логов AWS для приёма логов AWS.").

### Потоковая передача логов через Amazon Data Firehose

Интеграция Dynatrace с Amazon Data Firehose обеспечивает простой и безопасный способ приёма логов AWS.

Чтобы включить пересылку логов AWS, необходимо создать экземпляр Amazon Data Firehose и настроить его, указав среду Dynatrace в качестве назначения. Затем вы можете подключить группы логов CloudWatch, создав фильтр подписки, или отправлять логи напрямую в Firehose из сервисов, которые это поддерживают (например, VPC Flow Logs). Firehose и другие созданные облачные ресурсы влекут за собой расходы AWS в соответствии со стандартной политикой тарификации AWS.

## Microsoft Azure

Пересылка логов Azure позволяет осуществлять потоковую передачу логов Azure из Azure Event Hubs в логи Dynatrace через экземпляр Azure Function App. Поддерживаются как логи ресурсов Azure, так и логи активности.

Пересылка логов Azure выполняется напрямую через Cluster API. Если вы не хотите использовать прямой приём через Cluster API, необходимо использовать существующий ActiveGate для приёма логов.

Развёртывание компонента пересылки логов Azure приводит к созданию следующих ресурсов:

* Учётная запись хранения (`Microsoft.Storage/storageAccounts`)
* Служба BLOB-объектов учётной записи хранения (`Microsoft.Storage/storageAccounts/blobServices`)
* План службы приложений Azure (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Компонент пересылки логов Azure по умолчанию использует функцию Azure на базе Linux. Функция на базе Windows не поддерживается.

Подробности о создаваемых ресурсах см. в [файле Azure Resource Manager на GitHub](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json)

Подробные инструкции по настройке пересылки логов Azure см. в разделе [Логи Azure](../../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md#prereq "Используйте пересылку логов Azure для приёма логов Azure.").

## Google Cloud

Для настройки мониторинга Google Cloud для метрик и логов вам необходимо запустить скрипт развёртывания в Google Cloud Shell. В процессе настройки будет создана новая подписка Pub/Sub. GKE будет запускать два контейнера: компонент пересылки метрик и компонент пересылки логов. После установки вы получите метрики, логи, дашборды и оповещения для настроенных сервисов в Dynatrace. Инструкции зависят от места, где вы хотите запустить скрипт развёртывания:

* [На новом кластере GKE Autopilot, создаваемом автоматически](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot."). Рекомендуется
* [На существующем стандартном кластере GKE или кластере GKE Autopilot](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster.md "Разверните мониторинг логов и метрик для сервисов Google Cloud на существующем стандартном кластере GKE или кластере GKE Autopilot").

В зависимости от того, где вы хотите выполнять приём логов, могут потребоваться дополнительные ресурсы. Например, для управляемых развёртываний существует возможность использования ActiveGate для приёма логов. Однако это необходимо сделать вручную, так как скрипт установки его не развёртывает.

Все варианты приёма логов см. в разделе [Приём логов](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8.md#ingestion "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

## Связанные темы

* [DDU для Log Monitoring Classic](../../../license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption.md "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.")
