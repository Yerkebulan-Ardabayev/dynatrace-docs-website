---
title: Приём и обработка логов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data
scraped: 2026-05-12T11:13:35.756005
---

# Приём и обработка логов (Logs Classic)

# Приём и обработка логов (Logs Classic)

* Обзор
* Чтение: 2 мин
* Обновлено 4 мая 2026 г.

Log Monitoring Classic

Dynatrace автоматически собирает данные логов и событий из широкого спектра технологий. С помощью API приёма логов можно передавать записи логов в систему, и Dynatrace преобразует поток в понятные сообщения.

Dynatrace поддерживает все основные сторонние платформы и архитектуры.

## Автоматическое обнаружение и пользовательские источники логов

Вы можете использовать автоматически обнаруженные или добавленные вручную источники логов для OneAgent. См. [матрицу поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживает OneAgent на различных операционных системах и платформах.").

* [Автоматическое обнаружение данных логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Узнайте об автоматическом обнаружении содержимого логов и требованиях для его работы.")
* [Добавление файлов логов вручную](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Узнайте, как вручную добавлять файлы логов для анализа.")

![LMC — конфигурации приёма и обработки логов OneAgent при захвате](https://dt-cdn.net/images/lmc-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-c4876fc96b.png)

LMC — конфигурации приёма и обработки логов OneAgent при захвате

## Облачные провайдеры

Log Monitoring включает встроенную поддержку [Red Hat OpenShift](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes "Расширьте видимость событий Kubernetes/OpenShift.") и [логов и событий Kubernetes](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Узнайте, как осуществлять мониторинг логов в Kubernetes.") для платформ, рабочих нагрузок и приложений Kubernetes.

Log Monitoring поддерживает [мультиоблачные среды](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding "Узнайте, как настроить пересылку логов из AWS, Azure и Google Cloud."), включая:

* [AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция Amazon Data Firehose позволяет напрямую принимать облачные логи с высокой пропускной способностью.")
* [Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.")
* [Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку логов Azure для приёма логов.")

## Syslog

Syslog — стандартный протокол для ведения журналов сообщений и управления системными логами. Маршрутизаторы, принтеры, хосты, коммутаторы и другие устройства используют syslog для ведения журналов активности пользователей, событий жизненного цикла систем и программного обеспечения, состояния и диагностики.

Логи syslog принимаются через получатель syslog, доступный на Environment ActiveGate.

Подробности см. в разделе [Приём syslog с помощью ActiveGate (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/syslog "Принимайте данные syslog в Dynatrace с помощью ActiveGate.").

## Открытое программное обеспечение

Dynatrace Log Monitoring поддерживает фреймворки логов с открытым исходным кодом, включая Fluentd и Logstash.

## API приёма логов

С помощью API приёма логов можно передавать записи логов в Dynatrace и преобразовывать поток в понятные сообщения.

* [API приёма логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные логов и каковы возможные ограничения.")
* [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте о возможностях Log Monitoring API v2.")

![API приёма логов](https://cdn.bfldr.com/B686QPH3/as/tn5965tpbsb8pxnbnnxttncz/Generic_log_ingestion_API_-_Light_Mode?auto=webp&format=png&position=1)

API приёма логов

## Обработка логов

Dynatrace Log Monitoring включает преобразование входящих данных логов в форму, необходимую для лучшего понимания, анализа или дальнейшей обработки. С помощью Dynatrace Pattern Language (DPL) можно определять шаблоны с использованием сопоставителей и создавать набор правил, которые Log Monitoring применяет к принятым данным логов.

* [Обработка логов](/managed/analyze-explore-automate/log-monitoring/log-processing "Создавайте правила обработки логов, преобразующие входящие данные для лучшего анализа или дальнейшей обработки.")
* [Dynatrace Pattern Language](https://docs.dynatrace.com/docs/shortlink/dpl-dynatrace-pattern-language-hub)

![LMC — конвейер обработки логов](https://dt-cdn.net/images/lmc-log-processing-pipeline-2500-60d2c2d7b6.png)

LMC — конвейер обработки логов