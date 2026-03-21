---
title: Ввод журналов
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion
scraped: 2026-03-06T21:15:18.200005
---

# Приём логов


Приём логов — это процесс сбора данных логов из различных источников в инфраструктуре. Логи хранятся в хранилище данных Grail для анализа, автоматизации и мониторинга. Dynatrace упрощает этот процесс с помощью OneAgent, который автоматически обнаруживает логи и предлагает возможности централизованного управления. В бессерверных средах или там, где установка OneAgent невозможна, можно использовать API приёма логов (Logs Ingestion API).

Ниже представлен обзор стратегий приёма логов, которые можно использовать с Dynatrace.

[### OneAgent

Рекомендуется

Автоматический приём данных логов из различных источников.](lma-log-ingestion/lma-log-ingestion-via-oa.md "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")[### API приёма логов

Настройте интеграцию API приёма логов для ваших сценариев использования.](lma-log-ingestion/lma-log-ingestion-via-api.md "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")[![Syslog](https://dt-cdn.net/images/syslog-c85e9ae419.svg "Syslog")

### Приём syslog через ActiveGate

Приём логов syslog.](lma-log-ingestion/lma-log-ingestion-syslog.md "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.")

### Приём логов Kubernetes

Dynatrace Log Monitoring позволяет собирать логи из систем оркестрации контейнеров Kubernetes с помощью OneAgent. [Приём логов Kubernetes через OneAgent](../../ingest-from/setup-on-k8s/deployment/k8s-log-monitoring.md "Manage your Kubernetes logs with Dynatrace.") включает встроенное маскирование конфиденциальных данных, привязку к сущностям и сохранение метаданных Kubernetes.

Вы можете централизованно настраивать правила приёма OneAgent для всей среды Kubernetes. Применяя централизованные правила фильтрации, вы можете обеспечить приём только тех логов, которые релевантны для вашего сценария использования, сокращая затраты на обслуживание.

* [Потоковая передача логов Kubernetes с помощью OneAgent](../../ingest-from/setup-on-k8s/deployment/k8s-log-monitoring.md "Manage your Kubernetes logs with Dynatrace.")
* [Потоковая передача логов Kubernetes с помощью Fluent Bit](lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s.md "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.")
* [Потоковая передача логов Kubernetes с помощью Dynatrace OpenTelemetry Collector](../../ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich.md "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Потоковая передача логов Kubernetes с помощью Logstash](lma-log-ingestion/lma-stream-logs-with-logstash.md "Integrate Logstash to stream logs from nodes and pods to Dynatrace.")
* [Потоковая передача логов Kubernetes с помощью Fluentd](lma-log-ingestion/lma-stream-logs-fluentd-k8s.md "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")

### Экспорт телеметрических данных с помощью OpenTelemetry

OpenTelemetry Protocol (OTLP) — это основной сетевой протокол для обмена телеметрическими данными между сервисами и приложениями, поддерживающими OpenTelemetry.

Dynatrace предоставляет нативные OTLP-эндпоинты со следующими сервисами:

* Платформа SaaS
* Экземпляры ActiveGate
* Установки OneAgent

Кроме того, вы можете развернуть Collector в качестве промежуточного сервисного приложения для группировки запросов и повышения производительности сети или преобразования запросов перед их пересылкой в Dynatrace (например, для маскирования конфиденциальных данных).

* [Экспорт OpenTelemetry через OTLP](../../ingest-from/opentelemetry/otlp-api.md "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Пересылка данных логов из облачных платформ

[Пересылка облачных логов](lma-log-ingestion/lma-cloud-provider-log-forwarding.md "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.") позволяет осуществлять потоковую передачу данных логов из различных облачных платформ непосредственно в Dynatrace. Доступны следующие интеграции:

### AWS

Используйте интеграцию с Amazon Data Firehose, перенаправление из Amazon S3 и прямую интеграцию с AWS Lambda для оптимизации затрат при настройке потоковых логов с Dynatrace.

* [Потоковая передача логов через Amazon Data Firehose](../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [Потоковая передача логов из AWS S3](lma-log-ingestion/lma-cloud-provider-log-forwarding.md#s3-log-ingestion "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.")
* [Сбор логов из функций AWS Lambda](../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector.md "Collect logs from AWS Lambda functions")

### Azure

Потоковая передача логов из Azure Event Hubs в Dynatrace через экземпляр Azure Function App. Поддерживаются логи ресурсов и логи активности Azure. Dynatrace, приобретённый через Azure Marketplace, включает глубокую интеграцию с логами платформы Azure. Он предлагает упрощённую настройку через портал Azure и упрощает финансовые расчёты.

* [Потоковая передача логов Azure из Azure Event Hubs](../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md "Use Azure log forwarding to ingest Azure logs.")
* [Логи через Azure Native Dynatrace Service](../../ingest-from/microsoft-azure-services/azure-platform/azure-native-integration.md "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")

### GCP

Создайте подписку Pub/Sub для организации приёма метрик, логов, дашбордов и оповещений в Dynatrace. Это обеспечивает комплексное представление о состоянии вашей платформы Google Cloud, включая логи ресурсов и аудита.

* [Настройка интеграции Dynatrace с GCP для метрик и логов](../../ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

### Потоковая передача данных логов с помощью лог-шипперов

Лог-шиппер — это универсальный компонент, который можно легко интегрировать с API для сбора логов из различных источников и их пересылки в указанные пункты назначения. Ссылки ниже иллюстрируют поддерживаемые конфигурации, демонстрируя, как различные лог-шипперы могут быть адаптированы для различных потребностей развёртывания.

* [Потоковая передача логов с помощью Fluent Bit](lma-log-ingestion/lma-stream-logs-with-fluent-bit.md "Integrate Fluent Bit to stream logs to Dynatrace.")
* [Потоковая передача логов с помощью Fluentd в Kubernetes](lma-log-ingestion/lma-stream-logs-fluentd-k8s.md "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")
* [Потоковая передача логов с помощью Logstash](lma-log-ingestion/lma-stream-logs-with-logstash.md "Integrate Logstash to stream logs from nodes and pods to Dynatrace.")

### Потоковая передача логов с помощью Cribl

Вы можете отправлять логи, метрики и трассировки в Dynatrace с помощью Cribl Stream через OpenTelemetry Protocol (OTLP) или только логи через Cribl Stream с использованием HTTP-назначения Dynatrace, интегрированного с API приёма логов.

* [Потоковая передача логов с помощью Cribl](lma-log-ingestion/lma-stream-logs-with-cribl.md "How to send logs, metrics, and traces from Cribl Stream to Dynatrace using OTLP or HTTP integration.")

### Отправка логов с помощью Cloudflare

Используйте Cloudflare Logpush для отправки логов непосредственно в Dynatrace.
Настройте Logpush через панель управления Cloudflare или API.

* [Отправка логов с помощью Cloudflare](lma-log-ingestion/lma-push-logs-with-cloudflare.md "How to use Cloudflare Logpush to push logs directly to Dynatrace.")

### Интеграции через Dynatrace Hub

Dynatrace Hub — это маркетплейс расширений, интеграций и дополнений Dynatrace. Он предоставляет широкий спектр готовых решений для расширения возможностей Dynatrace. Вы можете найти различные интеграции для управления и аналитики логов в Dynatrace Hub.

* [Dynatrace Hub (Log Management and Analytics)](https://www.dynatrace.com/hub/?filter=log-management-and-analytics)

### Приём через расширения Dynatrace

Логи — это данные наблюдаемости, которые [расширения Dynatrace](../../ingest-from/extensions.md "Learn how to create and manage Dynatrace Extensions.") собирают и пересылают в Grail вместе с другими сигналами мониторинга для обеспечения целостного представления о вашей технологии. [Расширения](../../ingest-from/extend-dynatrace/extend-logs.md "Learn how to extend log observability in Dynatrace.") расширяют данные наблюдаемости и аналитические возможности, упрощая настройку данных и интеграцию со сторонними системами.

![log-extensions](https://dt-cdn.net/images/log-extensions-1980-76d7fc4317.png)

Вы можете использовать локальный API-эндпоинт `http://localhost:<port>/v2/logs/ingest` для отправки локально полученных логов в Dynatrace через защищённый и аутентифицированный канал. Узнайте больше на странице [Расширения](../../ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api.md "Use the Dynatrace API to push locally retrieved logs to Dynatrace.").

## Связанные темы

* [Приём логов через OneAgent](lma-log-ingestion/lma-log-ingestion-via-oa.md "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
* [API приёма логов](lma-log-ingestion/lma-log-ingestion-via-api.md "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [API приёма логов OneAgent](../../ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api.md "Use the Dynatrace API to push locally retrieved logs to Dynatrace.")
* [Обзор Log Management and Analytics в Dynatrace Hub](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)
* [Обработка логов с помощью OpenPipeline](lma-log-processing/lma-openpipeline.md "Process logs using Dynatrace OpenPipeline.")
