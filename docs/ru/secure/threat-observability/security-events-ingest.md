---
title: Security integrations
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-03-06T21:12:36.899894
---

# Интеграции безопасности

# Интеграции безопасности

* Последняя версия Dynatrace
* Обзор
* Обновлено 07 января 2026 г.

Dynatrace предоставляет различные способы интеграции внешних данных безопасности из множества сторонних продуктов в [Grail](/docs/platform/grail "Информация о том, какие данные Dynatrace можно запрашивать и как это делать.") и операционализации ваших данных на платформе Dynatrace.

## Загрузка данных

Для лучшего понимания типов интеграции см. [Типы интеграции OpenPipeline для событий безопасности](/docs/secure/threat-observability/concepts#security-ingest "Основные концепции, связанные с Threat Observability").

Ниже приведены поддерживаемые интеграции (с инструкциями).

* [Загрузка пользовательских событий безопасности через API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Загрузка событий безопасности из пользовательских сторонних продуктов через API.")
* [Загрузка журналов и событий безопасности Akamai](/docs/secure/threat-observability/security-events-ingest/ingest-akamai "Загрузка журналов и событий безопасности Akamai в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов сканирования и уязвимостей контейнеров Amazon ECR](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Загрузка результатов сканирования и уязвимостей образов контейнеров Amazon ECR и их анализ в Dynatrace.")
* [Загрузка результатов безопасности Amazon GuardDuty](/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty "Загрузка результатов безопасности Amazon GuardDuty и их анализ в Dynatrace.")
* [Загрузка результатов безопасности AWS Security Hub](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Загрузка результатов безопасности AWS Security Hub и их анализ в Dynatrace.")
* [Загрузка событий безопасности и журналов аудита GitHub Advanced Security](/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security "Загрузка журналов аудита и событий безопасности GitHub Advanced Security в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов уязвимостей, сканирований и журналов аудита Harbor](/docs/secure/threat-observability/security-events-ingest/ingest-harbor-data "Загрузка результатов уязвимостей, сканирований и журналов аудита Harbor в Dynatrace в качестве событий безопасности.")
* [Загрузка событий безопасности Microsoft Defender for Cloud](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-defender "Загрузка событий безопасности Microsoft Defender for Cloud и их анализ в Dynatrace.")
* [Загрузка журналов входа Microsoft Entra ID](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-entra-id "Загрузка журналов входа Microsoft Entra ID и их анализ в Dynatrace.")
* [Загрузка событий безопасности Microsoft Sentinel](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-sentinel "Загрузка событий безопасности Microsoft Sentinel и их анализ в Dynatrace.")
* [Загрузка результатов уязвимостей в формате OCSF](/docs/secure/threat-observability/security-events-ingest/ingest-ocsf-data "Загрузка результатов уязвимостей в формате OCSF от любого поставщика и их анализ на платформе Dynatrace.")
* [Загрузка результатов уязвимостей, событий сканирования и журналов аудита Qualys](/docs/secure/threat-observability/security-events-ingest/ingest-qualys "Загрузка результатов уязвимостей, событий сканирования и журналов аудита Qualys в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов соответствия Runecast Analyzer](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Загрузка результатов соответствия из Runecast Analyzer и их анализ на платформе Dynatrace.")
* [Загрузка результатов уязвимостей, сканирований и журналов аудита Snyk](/docs/secure/threat-observability/security-events-ingest/ingest-snyk-data "Загрузка результатов уязвимостей, сканирований и журналов аудита Snyk в Dynatrace в качестве событий безопасности.")
* [Загрузка событий безопасности и качества, метрик и журналов аудита SonarQube](/docs/secure/threat-observability/security-events-ingest/ingest-sonarqube-data "Загрузка событий безопасности и качества, метрик и журналов аудита SonarQube в Dynatrace в качестве событий безопасности.")
* [Загрузка событий безопасности и журналов аудита Sonatype Lifecycle](/docs/secure/threat-observability/security-events-ingest/ingest-sonatype "Загрузка событий безопасности и журналов аудита Sonatype Lifecycle в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов уязвимостей, событий сканирования и журналов аудита Tenable](/docs/secure/threat-observability/security-events-ingest/ingest-tenable-data "Загрузка результатов уязвимостей, событий сканирования и журналов аудита Tenable в Dynatrace в качестве событий безопасности.")

## Обогащение данных

Добавляйте внешние репутационные данные к наблюдаемым объектам, используя надежные источники разведки угроз:

* [Обогащение наблюдаемых объектов угроз с помощью AbuseIPDB](/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich "Обогащение наблюдаемых объектов угроз с помощью AbuseIPDB и их анализ в Dynatrace.")
* [Обогащение наблюдаемых объектов угроз с помощью VirusTotal](/docs/secure/threat-observability/security-events-ingest/virustotal-enrich "Обогащение наблюдаемых объектов угроз с помощью VirusTotal и их анализ в Dynatrace.")

После настройки источников обогащения вы можете применить их к:

* Валидации наблюдаемых объектов в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations/enhance-results#enrich "Организация и интерпретация результатов запросов в рамках расследований --- от анализа производительности до обнаружения угроз.")
* Улучшению результатов обнаружения в [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits/manage-results#enrich "Фильтрация, форматирование и сортировка результатов обнаружения.")
