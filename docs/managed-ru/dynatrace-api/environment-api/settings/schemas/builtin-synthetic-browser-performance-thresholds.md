---
title: Settings API - Performance thresholds schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-performance-thresholds
scraped: 2026-05-12T11:41:13.729706
---

# Settings API - Performance thresholds schema table

# Settings API - Performance thresholds schema table

* Published Dec 05, 2023

### Пороги производительности (`builtin:synthetic.browser.performance-thresholds)`

Dynatrace создаёт новую проблему, если этот synthetic-монитор превышает любой из порогов производительности 'Total duration' ниже в 3 из 5 последних прогонов в данном расположении, при условии что для synthetic-монитора нет открытого maintenance window. В одну проблему могут входить несколько расположений с 3 такими нарушениями. Проблема закрывается, если в 5 последних прогонах в каждом из ранее затронутых расположений ни один порог не нарушен.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.performance-thresholds` | - | `SYNTHETIC_TEST` - Synthetic monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.performance-thresholds` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.performance-thresholds` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.performance-thresholds` |

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
| Synthetic-событие `event` | text | - | Required |
| Порог (в секундах) `threshold` | float | - | Required |
| Количество нарушающих прогонов в анализируемом скользящем окне `violatingSamples` | integer | - | Required |
| Количество прогонов в анализируемом скользящем окне (размер окна) `samples` | integer | - | Required |
| Количество последних ненарушающих прогонов, закрывающих проблему `dealertingSamples` | integer | - | Required |