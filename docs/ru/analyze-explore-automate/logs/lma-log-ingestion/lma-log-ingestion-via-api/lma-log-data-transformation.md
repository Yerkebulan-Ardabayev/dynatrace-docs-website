---
title: Автоматическое обогащение логов
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation
scraped: 2026-03-06T21:29:26.252310
---

# Автоматическое обогащение логов

# Автоматическое обогащение логов

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Apr 07, 2025

Dynatrace автоматически обогащает логи, принятые через API.

## Преобразование логов, принятых через API

API приёма логов автоматически преобразует ключи серьёзности `status`, `severity`, `level` и `syslog.severity` в атрибут `loglevel`.

Входные значения ключей серьёзности `status`, `severity`, `level` и `syslog.severity` преобразуются (без учёта регистра) в выходные значения атрибута `loglevel` в соответствии со следующей таблицей сопоставления:

## Преобразование всех типов логов

Кроме того, для каждого события лога создаётся атрибут `status` со значением, представляющим сумму значений `loglevel` на основе следующей группировки:

Например:
Ключ серьёзности `level` в параметре запроса API приёма логов содержит значение `serious`.

1. Ключ серьёзности `level` преобразуется в атрибут `loglevel`, при этом значение `serious` сопоставляется с `SEVERE` согласно приведённой выше таблице.
2. Атрибут `loglevel` со значением `SEVERE` группируется в атрибут `status`. Согласно таблице группировки выше, атрибут `status` будет содержать значение `ERROR`.
3. В деталях события лога программа просмотра логов отобразит следующее:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Связанные темы

* [API приёма логов](../lma-log-ingestion-via-api.md "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Приём логов через OneAgent](../lma-log-ingestion-via-oa.md "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
