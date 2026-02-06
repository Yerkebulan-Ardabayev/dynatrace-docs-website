---
title: Security integrations
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-02-06T16:21:04.179783
---

# Интеграция безопасности

# Интеграция безопасности

* Последняя версия Dynatrace
* Обзор
* Обновлено 7 января 2026 г.

Dynatrace предоставляет различные способы интеграции внешних данных безопасности из нескольких сторонних продуктов в [Грааль](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") и использования ваших данных на платформе Dynatrace.

## Прием данных

Для лучшего понимания типов интеграции см. [Типы интеграции OpenPipeline для событий безопасности](/docs/secure/threat-observability/concepts#security-ingest "Basic concepts related to Threat Observability").

Ниже приведены поддерживаемые интеграции (с инструкциями).

* [Прием пользовательских событий безопасности через API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Ingest security events from custom third-party products via API.")
* [Прием журналов безопасности и событий Akamai](/docs/secure/threat-observability/security-events-ingest/ingest-akamai "Ingest Akamai security logs and events into Dynatrace as security events.")
* [Получение данных об уязвимостях контейнера Amazon ECR и событий сканирования.](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.")
* [Получение результатов безопасности Amazon GuardDuty](/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.")
* [Получение результатов безопасности AWS Security Hub](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Ingest AWS Security Hub security findings and analyze them in Dynatrace.")
* [Прием событий безопасности и журналов аудита GitHub Advanced Security.](/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security "Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.")
* [Получение данных об уязвимостях, сканирований и журналов аудита Harbor](/docs/secure/threat-observability/security-events-ingest/ingest-harbor-data "Ingest Harbor vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Прием событий Microsoft Defender для облачной безопасности](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-defender "Ingest Microsoft Defender for Cloud security events and analyze them in Dynatrace.")
* [Прием журналов входа в систему с идентификатором Microsoft Entra ID](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-entra-id "Ingest Microsoft Entra ID sign-in logs and analyze them in Dynatrace.")
* [Прием событий безопасности Microsoft Sentinel](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-sentinel "Ingest Microsoft Sentinel security events and analyze them in Dynatrace.")
* [Получение результатов уязвимостей в формате OCSF](/docs/secure/threat-observability/security-events-ingest/ingest-ocsf-data "Ingest vulnerability findings in OCSF format from any provider and analyze them on the Dynatrace platform.")
* [Получение данных об уязвимостях Qualys, событий сканирования и журналов аудита.](/docs/secure/threat-observability/security-events-ingest/ingest-qualys "Ingest Qualys vulnerability findings, scan events, and audit logs into Dynatrace as security events.")
* [Результаты соответствия Ingest Runecast Analyser](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.")
* [Получение результатов поиска уязвимостей, сканирований и журналов аудита Snyk.](/docs/secure/threat-observability/security-events-ingest/ingest-snyk-data "Ingest Snyk vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Принимайте события безопасности и качества SonarQube, метрики и журналы аудита.](/docs/secure/threat-observability/security-events-ingest/ingest-sonarqube-data "Ingest SonarQube security and quality events, metrics, and audit logs into Dynatrace as security events.")
* [Прием событий безопасности жизненного цикла Sonatype и журналов аудита](/docs/secure/threat-observability/security-events-ingest/ingest-sonatype "Ingest Sonatype Lifecycle security events and audit logs into Dynatrace as security events.")
* [Получение результатов обнаружения уязвимостей Tenable, событий сканирования и журналов аудита.](/docs/secure/threat-observability/security-events-ingest/ingest-tenable-data "Ingest Tenable vulnerability findings, scan events, and audit logs into Dynatrace as security events.")

## Обогащение данных

Добавьте внешние данные о репутации в наблюдаемые, используя надежные источники информации об угрозах:

* [Обогатите наблюдаемые угрозы с помощью AbuseIPDB](/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.")
* [Обогатите наблюдаемые угрозы с помощью VirusTotal](/docs/secure/threat-observability/security-events-ingest/virustotal-enrich "Enrich threat observables with VirusTotal and analyze them in Dynatrace.")

После настройки источников обогащения вы можете применить их к:

* Проверка наблюдаемых данных в [![Расследования](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследования**](/docs/secure/investigations/enhance-results#enrich «Организация и интерпретация результатов запросов в ходе расследований — от анализа производительности до обнаружения угроз».)
* Улучшите результаты обнаружения в [![Угрозы и эксплойты](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Угрозы и эксплойты**](/docs/secure/threats-and-exploits/manage-results#enrich «Фильтрация, форматирование и сортировка результатов обнаружения».)