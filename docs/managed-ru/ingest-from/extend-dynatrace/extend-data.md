---
title: Обогащение данных мониторинга
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-data
scraped: 2026-05-12T11:37:59.140301
---

# Обогащение данных мониторинга

# Обогащение данных мониторинга

* 3-min read
* Updated on Mar 16, 2023

Dynatrace позволяет обогащать поступающие данные дополнительными полями, специфичными для Dynatrace. Это относится к логам, метрикам и трейсам.

## Справочник по атрибутам обогащения данных

Для обогащения данных используется директория обогащения. Файлы в этой директории содержат пары «ключ-значение», которые Dynatrace автоматически добавляет ко всем поступающим данным.

### Расположение директории обогащения

| ОС | Путь |
| --- | --- |
| Unix/Linux | `/var/lib/dynatrace/enrichment` |
| Windows | `%ProgramData%\dynatrace\enrichment` |

### Формат файла обогащения

Файлы обогащения должны быть в формате JSON. Каждый файл содержит JSON-объект с парами «ключ-значение»:

```json
{
  "key1": "value1",
  "key2": "value2"
}
```

### Пример загрузки файлов обогащения на Python

```python
import json
import os

enrichment_dir = "/var/lib/dynatrace/enrichment"
os.makedirs(enrichment_dir, exist_ok=True)

enrichment_data = {
    "environment": "production",
    "team": "platform"
}

with open(os.path.join(enrichment_dir, "custom.json"), "w") as f:
    json.dump(enrichment_data, f)
```

## Связанные темы

* [Обогащение метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширьте наблюдаемость метрик с помощью Dynatrace.")
* [Обогащение логов](/managed/ingest-from/extend-dynatrace/extend-logs "Расширьте аналитику логов с помощью Dynatrace.")