---
title: Settings API - Anomaly detectors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-davis-anomaly-detectors
scraped: 2026-05-12T11:47:29.201959
---

# Settings API - Anomaly detectors schema table

# Settings API - Anomaly detectors schema table

* Published May 20, 2024

### Детекторы аномалий (`builtin:davis.anomaly-detectors)`

Детекторы аномалий используются для автоматического обнаружения аномалий во временных рядах через пороги или baseline.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:davis.anomaly-detectors` | * `group:anomaly-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:davis.anomaly-detectors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:davis.anomaly-detectors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:davis.anomaly-detectors` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если включено, детектор аномалий будет активен и работать. | Required |
| Заголовок `title` | text | Заголовок детектора аномалий | Required |
| Описание `description` | text | Описание детектора аномалий | Required |
| Источник `source` | text | Источник, создавший детектор аномалий | Required |
| Параметры выполнения `executionSettings` | [ExecutionSettings](#ExecutionSettings) | Задаёт параметры конфигурации, влияющие на то, как и в каком контексте выполняется запрос или вычисление. | Required |
| Вход анализатора `analyzer` | [AnalyzerInput](#AnalyzerInput) | Вход анализатора для его инициализации | Required |
| Шаблон события `eventTemplate` | [DavisEventTemplate](#DavisEventTemplate) | Задаёт дополнительные поля для davis-событий, запускаемых детектором аномалий | Required |

##### Объект `ExecutionSettings`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Актор `actor` | text | UUID сервисного пользователя. Запросы выполняются от имени сервисного пользователя. | Required |
| Сдвиг запроса `queryOffset` | integer | Сдвиг скользящего окна вычисления (в минутах) для метрик с задержкой | Optional |
| Задержка выполнения `delay` | integer | Фиксированная задержка между выполнениями (в секундах) | Optional |

##### Объект `AnalyzerInput`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Полное квалифицированное имя анализатора | Required |
| Входные поля `input` | Set<[AnalyzerInputField](#AnalyzerInputField)> | Входные поля для указанного анализатора | Required |

##### Объект `DavisEventTemplate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свойства события `properties` | [EventProperty](#EventProperty)[] | Набор дополнительных key-value-свойств, прикрепляемых к запущенному событию. | Required |

##### Объект `AnalyzerInputField`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `key` | text | Ключ поля входа анализатора | Required |
| Значение `value` | text | Значение поля входа анализатора | Required |

##### Объект `EventProperty`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `key` | text | Ключ свойства | Required |
| Значение `value` | text | Значение свойства. Поддерживает подстановку placeholder'ов в фигурных скобках {}. | Required |