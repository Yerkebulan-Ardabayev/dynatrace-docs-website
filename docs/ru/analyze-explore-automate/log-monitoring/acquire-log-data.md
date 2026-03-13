---
title: Log ingest & process (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data
scraped: 2026-03-06T21:37:45.649064
---

# Приём и обработка журналов (Logs Classic)

# Приём и обработка журналов (Logs Classic)

* Classic
* Overview
* 2-min read
* Updated on Aug 11, 2023

Log Monitoring Classic

Dynatrace автоматически собирает данные журналов и событий из широкого спектра технологий. С помощью Log ingestion API вы можете передавать записи журналов в систему и Dynatrace преобразует поток в понятные сообщения журналов.

Dynatrace поддерживает все основные сторонние платформы и архитектуры.

## Автообнаружение журналов и пользовательские источники журналов

Вы можете полагаться на автоматически обнаруженные или добавленные вручную источники журналов для OneAgent. См. [Матрицу поддержки платформ и возможностей OneAgent](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.").

* [Автоматическое обнаружение данных журналов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Узнайте об автообнаружении содержимого журналов и требованиях к автообнаружению.")
* [Добавление файлов журналов вручную](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Узнайте, как вручную добавлять файлы журналов для анализа.")

![LMC - OneAgent log ingestion and processing configurations at capture](https://dt-cdn.net/images/lmc-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-c4876fc96b.png)

## Облачные провайдеры

Log Monitoring включает встроенную поддержку журналов и событий [Red Hat OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes "Расширьте видимость событий Kubernetes/OpenShift.") и [Kubernetes](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Узнайте, как отслеживать журналы в Kubernetes.") для платформ Kubernetes, рабочих нагрузок и приложений, работающих внутри Kubernetes.

Log Monitoring имеет встроенную поддержку [мультиоблачных сред](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding "Узнайте, как настроить пересылку журналов AWS, Azure и Google Cloud для приёма журналов."), включая:

* [AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция Amazon Data Firehose позволяет напрямую принимать облачные журналы без дополнительной инфраструктуры и с более высокой пропускной способностью.")
* [Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройте мониторинг журналов и метрик для сервисов GCP в новом кластере GKE Autopilot.")
* [Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку журналов Azure для приёма журналов Azure.")

## Syslog

Syslog — стандартный протокол для ведения журналов сообщений и управления системными журналами. Маршрутизаторы, принтеры, хосты, коммутаторы и другие устройства на различных платформах используют syslog для записи активности пользователей, событий жизненного цикла системы и программного обеспечения, статуса или диагностических данных.

Журналы Syslog принимаются через syslog-приёмник, доступный на Environment ActiveGate.

Для получения дополнительной информации см. [Приём Syslog с ActiveGate (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog "Принимайте данные журналов syslog в Dynatrace с помощью ActiveGate и преобразуйте их в понятные сообщения журналов.").

## Открытый исходный код

Dynatrace Log Monitoring поддерживает фреймворки для работы с журналами с открытым исходным кодом, включая Fluentd и Logstash.

## Log ingestion API

С помощью Log ingestion API вы можете передавать записи журналов в Dynatrace и Dynatrace преобразует поток в понятные сообщения журналов. Вы также можете использовать Log ingestion API для потоковой передачи записей журналов в Dynatrace через API.

* [Log ingestion API](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов и каковы возможные ограничения такого приёма.")
* [Log Monitoring API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно сделать с помощью Log Monitoring API v2.")

![LMC - Generic log ingestion API](https://dt-cdn.net/images/lmc-generic-log-ingestion-api-2500-e9c0d3ff5f.png)

## Обработка журналов

Dynatrace Log Monitoring включает преобразование входящих данных журналов в форму, которая может потребоваться для лучшего понимания, анализа или дальнейшей обработки данных журналов в Dynatrace. Используя Dynatrace Pattern Language (DPL), вы можете определять паттерны с помощью матчеров и создавать набор правил, которые Log Monitoring применяет к принятым данным журналов.

* [Обработка журналов](/docs/analyze-explore-automate/log-monitoring/log-processing "Создавайте правила обработки журналов, преобразующие входящие данные журналов для лучшего анализа или дальнейшей обработки.")
* [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Используйте Dynatrace Pattern Language для описания паттернов с помощью матчеров.")

![LMC - Log processing pipeline](https://dt-cdn.net/images/lmc-log-processing-pipeline-2500-60d2c2d7b6.png)
