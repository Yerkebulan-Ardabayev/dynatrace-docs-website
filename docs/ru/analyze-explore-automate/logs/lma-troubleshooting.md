---
title: Устранение неполадок Log Management и Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-troubleshooting
scraped: 2026-03-05T21:36:06.993002
---

# Устранение неполадок в Log Management and Analytics


* Latest Dynatrace
* Troubleshooting
* 1-min read

На этой странице описаны действия в ситуациях, когда Log Management and Analytics не работает в вашей среде так, как ожидается.

## Общее устранение неполадок

Если вы столкнулись с проблемой, связанной с Log Management and Analytics, обратитесь к одной из следующих страниц в сообществе Dynatrace.

* [Почему мои логи не отображаются в Dynatrace?](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [Что может препятствовать появлению логов на сервере?](https://dt-url.net/lu23817)
* [Я получаю предупреждение о несоответствии регистра ключа атрибута](https://community.dynatrace.com/t5/Troubleshooting/I-get-an-ingest-warning-about-an-attribute-key-case-mismatch/ta-p/251188)
* [Я получаю предупреждение в Log Viewer о запросах с учётом регистра](https://community.dynatrace.com/t5/Troubleshooting/I-get-a-warning-in-the-Log-Viewer-about-case-sensitive-queries/ta-p/251189)
* [Руководство по устранению неполадок приёма Syslog через ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Устранение неполадок приёма Syslog](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)
* [Устранение неполадок приёма логов через API — POST ingest logs](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Устранение неполадок для конкретных технологий

* [Устранение неполадок логов, принятых через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)
* [Устранение неполадок Azure Log Forwarder](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
* [Приём логов в Kubernetes с Dynatrace](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)

## Конкретные проблемы

### Принятые логи выглядят не так, как ожидалось

Например, содержимое обрезано, временная метка скорректирована, или правило обработки, по всей видимости, не работает.

Конвейер приёма логов состоит из нескольких этапов, на которых логи обрабатываются и проверяются на соответствие характеристикам продукта и ограничениям. Отдельная запись лога содержит предупреждения о проблемах, возникших в конвейере приёма и обработки. Предупреждения сохраняются в атрибуте `dt.ingest.warnings` для каждой записи лога отдельно. Смотрите список и описание всех возможных предупреждений при приёме логов.

### OneAgent не принимает настроенные записи логов

Если OneAgent не принимает записи логов из файла лога, несмотря на то что файл лога настроен для приёма и был обнаружен автоматически или добавлен как пользовательский источник логов, могут быть нарушены правила безопасности Log Agent. Дополнительную информацию смотрите в разделе Правила безопасности.
