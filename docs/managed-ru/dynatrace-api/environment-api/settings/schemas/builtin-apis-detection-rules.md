---
title: Settings API - API detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-apis-detection-rules
scraped: 2026-05-12T11:42:15.224977
---

# Settings API - API detection rules schema table

# Settings API - API detection rules schema table

* Published Dec 05, 2023

### Правила обнаружения API (`builtin:apis.detection-rules)`

Современные приложения используют много разных фреймворков, поэтому stacktrace'ы в method hotspot'ах и исключениях становятся довольно длинными. API позволяют быстрее находить компонент и ответственную команду за hotspot или деградацию.

Правила обнаружения API анализируют фрейм stacktrace и классифицируют его по классам (Java, .NET и PHP) или файлам (Node.js, PHP и GO) в зависимости от технологии. Правила выполняются по порядку, и первое совпадение определяет API. Маркировка API как сторонних позволит сосредоточиться на не-сторонних API.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:apis.detection-rules` | * `group:service-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:apis.detection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:apis.detection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:apis.detection-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя API `apiName` | text | - | Required |
| Цвет `apiColor` | text | Этот цвет используется для выделения API при просмотре данных уровня кода, например distributed trace'ов или method hotspot'ов. | Required |
| Технология `technology` | enum | Ограничить это правило конкретной технологией. Возможные значения: * `Go` * `Nodejs` * `PHP` * `Java` * `dotNet` * `Python` | Optional |
| Этот API описывает стороннюю библиотеку `thirdPartyApi` | boolean | - | Required |
| Список условий `conditions` | Set<[apiRule](#apiRule)> | - | Required |

##### Объект `apiRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| База `base` | enum | Возможные значения: * `FQCN` * `FILE_NAME` * `PACKAGE` | Required |
| Сопоставитель `matcher` | enum | Возможные значения: * `BEGINS_WITH` * `CONTAINS` | Required |
| Шаблон `pattern` | text | - | Required |