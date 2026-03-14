---
title: Интеграции безопасности
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-03-06T21:12:36.899894
---

# Интеграции безопасности


* Последняя версия Dynatrace
* Обзор
* Обновлено 07 января 2026 г.

Dynatrace предоставляет различные способы интеграции внешних данных безопасности из множества сторонних продуктов в [Grail](../../platform/grail.md "Информация о том, какие данные Dynatrace можно запрашивать и как это делать.") и операционализации ваших данных на платформе Dynatrace.

## Загрузка данных

Для лучшего понимания типов интеграции см. [Типы интеграции OpenPipeline для событий безопасности](concepts.md#security-ingest "Основные концепции, связанные с Threat Observability").

Ниже приведены поддерживаемые интеграции (с инструкциями).

* [Загрузка пользовательских событий безопасности через API](security-events-ingest/ingest-custom-data.md "Загрузка событий безопасности из пользовательских сторонних продуктов через API.")
* [Загрузка журналов и событий безопасности Akamai](security-events-ingest/ingest-akamai.md "Загрузка журналов и событий безопасности Akamai в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов сканирования и уязвимостей контейнеров Amazon ECR](security-events-ingest/ingest-aws-ecr-data.md "Загрузка результатов сканирования и уязвимостей образов контейнеров Amazon ECR и их анализ в Dynatrace.")
* [Загрузка результатов безопасности Amazon GuardDuty](security-events-ingest/ingest-amazon-guardduty.md "Загрузка результатов безопасности Amazon GuardDuty и их анализ в Dynatrace.")
* [Загрузка результатов безопасности AWS Security Hub](security-events-ingest/ingest-aws-security-hub.md "Загрузка результатов безопасности AWS Security Hub и их анализ в Dynatrace.")
* [Загрузка событий безопасности и журналов аудита GitHub Advanced Security](security-events-ingest/ingest-github-advanced-security.md "Загрузка журналов аудита и событий безопасности GitHub Advanced Security в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов уязвимостей, сканирований и журналов аудита Harbor](security-events-ingest/ingest-harbor-data.md "Загрузка результатов уязвимостей, сканирований и журналов аудита Harbor в Dynatrace в качестве событий безопасности.")
* [Загрузка событий безопасности Microsoft Defender for Cloud](security-events-ingest/ingest-microsoft-defender.md "Загрузка событий безопасности Microsoft Defender for Cloud и их анализ в Dynatrace.")
* [Загрузка журналов входа Microsoft Entra ID](security-events-ingest/ingest-microsoft-entra-id.md "Загрузка журналов входа Microsoft Entra ID и их анализ в Dynatrace.")
* [Загрузка событий безопасности Microsoft Sentinel](security-events-ingest/ingest-microsoft-sentinel.md "Загрузка событий безопасности Microsoft Sentinel и их анализ в Dynatrace.")
* [Загрузка результатов уязвимостей в формате OCSF](security-events-ingest/ingest-ocsf-data.md "Загрузка результатов уязвимостей в формате OCSF от любого поставщика и их анализ на платформе Dynatrace.")
* [Загрузка результатов уязвимостей, событий сканирования и журналов аудита Qualys](security-events-ingest/ingest-qualys.md "Загрузка результатов уязвимостей, событий сканирования и журналов аудита Qualys в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов соответствия Runecast Analyzer](security-events-ingest/ingest-runecast-analyzer.md "Загрузка результатов соответствия из Runecast Analyzer и их анализ на платформе Dynatrace.")
* [Загрузка результатов уязвимостей, сканирований и журналов аудита Snyk](security-events-ingest/ingest-snyk-data.md "Загрузка результатов уязвимостей, сканирований и журналов аудита Snyk в Dynatrace в качестве событий безопасности.")
* [Загрузка событий безопасности и качества, метрик и журналов аудита SonarQube](security-events-ingest/ingest-sonarqube-data.md "Загрузка событий безопасности и качества, метрик и журналов аудита SonarQube в Dynatrace в качестве событий безопасности.")
* [Загрузка событий безопасности и журналов аудита Sonatype Lifecycle](security-events-ingest/ingest-sonatype.md "Загрузка событий безопасности и журналов аудита Sonatype Lifecycle в Dynatrace в качестве событий безопасности.")
* [Загрузка результатов уязвимостей, событий сканирования и журналов аудита Tenable](security-events-ingest/ingest-tenable-data.md "Загрузка результатов уязвимостей, событий сканирования и журналов аудита Tenable в Dynatrace в качестве событий безопасности.")

## Обогащение данных

Добавляйте внешние репутационные данные к наблюдаемым объектам, используя надежные источники разведки угроз:

* [Обогащение наблюдаемых объектов угроз с помощью AbuseIPDB](security-events-ingest/abuseipdb-enrich.md "Обогащение наблюдаемых объектов угроз с помощью AbuseIPDB и их анализ в Dynatrace.")
* [Обогащение наблюдаемых объектов угроз с помощью VirusTotal](security-events-ingest/virustotal-enrich.md "Обогащение наблюдаемых объектов угроз с помощью VirusTotal и их анализ в Dynatrace.")

После настройки источников обогащения вы можете применить их к:

* Валидации наблюдаемых объектов в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations/enhance-results.md#enrich "Организация и интерпретация результатов запросов в рамках расследований --- от анализа производительности до обнаружения угроз.")
* Улучшению результатов обнаружения в [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../threats-and-exploits/manage-results.md#enrich "Фильтрация, форматирование и сортировка результатов обнаружения.")
