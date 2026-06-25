---
title: Settings API - Performance thresholds schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-performance-thresholds
scraped: 2026-05-12T11:45:08.080013
---

# Settings API - Performance thresholds schema table

# Settings API - Performance thresholds schema table

* Published Jul 31, 2024

### Пороги производительности (`builtin:synthetic.multiprotocol.performance-thresholds)`

Dynatrace генерирует новую проблему, если этот синтетический монитор превышает любой из порогов производительности ниже в {violatingSamples} из {samples} последних прогонов запросов в данной локации, если нет открытого maintenance window для синтетического монитора. В одну проблему могут включаться несколько локаций с {violatingSamples} такими нарушениями. Проблема закрывается, если ни один порог производительности не нарушается в {dealertingSamples} последних прогонах запросов в каждой из ранее затронутых локаций.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.performance-thresholds` | * `group:web-and-mobile-monitoring` * `group:synthetic.multiprotocol` * `group:web-and-mobile-monitoring.multiprotocol-monitor-default-settings` | `MULTIPROTOCOL_MONITOR` - Network availability monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.performance-thresholds` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.performance-thresholds` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.performance-thresholds` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Генерировать проблему и отправлять оповещение при нарушении порогов производительности `enabled` | boolean | - | Required |
| Пороги производительности `thresholds` | Set<[ThresholdEntry](#ThresholdEntry)> | - | Required |

##### Объект `ThresholdEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог (в мс) `threshold` | integer | - | Required |
| Индекс шага `stepIndex` | integer | - | Required |
| Тип агрегации `aggregation` | enum | Возможные значения: * `AVG` * `MIN` * `MAX` | Required |
| Количество нарушающих прогонов запросов в анализируемом скользящем окне `violatingSamples` | integer | - | Required |
| Количество прогонов запросов в анализируемом скользящем окне (размер окна) `samples` | integer | - | Required |
| Количество последних ненарушающих прогонов запросов, закрывающих проблему `dealertingSamples` | integer | - | Required |