---
title: Интеграции безопасности
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-03-06T21:12:36.899894
---

Интеграция внешних данных безопасности из сторонних продуктов в Grail через платформу Dynatrace.

## Загрузка данных

Типы интеграции: см. [Типы интеграции OpenPipeline для событий безопасности](concepts.md#security-ingest).

Поддерживаемые интеграции:

- Пользовательские события безопасности через API
- Akamai — журналы и события безопасности
- Amazon ECR — результаты сканирования и уязвимости контейнеров
- Amazon GuardDuty — результаты безопасности
- AWS Security Hub — результаты безопасности
- GitHub Advanced Security — события безопасности и журналы аудита
- Harbor — уязвимости, сканирования и журналы аудита
- Microsoft Defender for Cloud — события безопасности
- Microsoft Entra ID — журналы входа
- Microsoft Sentinel — события безопасности
- OCSF — результаты уязвимостей
- Qualys — уязвимости, сканирования и журналы аудита
- Runecast Analyzer — результаты соответствия
- Snyk — уязвимости, сканирования и журналы аудита
- SonarQube — события безопасности и качества, метрики и журналы аудита
- Sonatype Lifecycle — события безопасности и журналы аудита
- Tenable — уязвимости, сканирования и журналы аудита

## Обогащение данных

Добавление репутационных данных к наблюдаемым объектам:

- Обогащение с помощью AbuseIPDB
- Обогащение с помощью VirusTotal

Применение источников обогащения:

- Валидация в [**Investigations**](../investigations/enhance-results.md#enrich)
- Улучшение результатов в [**Threats & Exploits**](../threats-and-exploits/manage-results.md#enrich)
