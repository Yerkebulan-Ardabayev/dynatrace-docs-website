---
title: Settings API - URL path pattern matching schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-url-path-pattern-matching-rules
scraped: 2026-05-12T11:48:20.698933
---

# Settings API - URL path pattern matching schema table

# Settings API - URL path pattern matching schema table

* Published Sep 25, 2025

### Сопоставление шаблонов URL-путей (`builtin:url-path-pattern-matching-rules)`

Задайте правила для извлечения URL-шаблонов из URL-путей. См. [Service Detection v2 documentation](https://dt-url.net/sy035si)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:url-path-pattern-matching-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-path-pattern-matching-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:url-path-pattern-matching-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-path-pattern-matching-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если включено, правило будет вычисляться. | Required |
| Правило `rule` | [Rule](#Rule) | - | Required |

##### Объект `Rule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя правила `ruleName` | text | - | Required |
| Описание `description` | text | - | Optional |
| Условие сопоставления `condition` | text | Ограничивает scope правила service splitting [DQL matcher](https://dt-url.net/l603wby)-условиями по resource attributes.  Правило применяется только если условие совпало, иначе вычисление ruleset продолжается.  Если поле пустое, условие всегда совпадает. | Optional |
| Шаблоны URL-путей `urlPathPatterns` | list | Первый совпавший шаблон определяет результирующее значение атрибута url.path.pattern.  Шаблон URL-пути описывает, как сырой URL-путь (например, `/path/123`) обобщается в стабильный template (например, `/path/{id}`). Работает с сегментами пути (частями между `/`) и используется для получения low-volatility-значений атрибута `url.path.pattern`.  Шаблоны сопоставляются с нормализованным путём, который всегда начинается с одного ведущего `/`. Сопоставление чувствительно к регистру.  Синтаксис. Шаблоны записываются как последовательность сегментов, разделённых `/`:  * Литеральные сегменты + Совпадают с точным сегментом пути и копируются как есть.   + Пример: `/api/items` совпадает только с путями, у которых первые два сегмента: `api` и `items`. * `{placeholder}` + Совпадает ровно с одним сегментом пути и выводит имя placeholder в фигурных скобках.   + Используется, чтобы скрыть переменные части вроде ID или других динамических идентификаторов.   + Пример: `/api/items/{id}` совпадает с `/api/items/123` или `/api/items/abc` и даёт `/api/items/{id}`. * `_` + Переменный сегмент, совпадающий ровно с одним сегментом пути и сохраняющий исходное значение в результате.   + Типичное применение, версионируемые API, где версия должна оставаться видимой.   + Пример: `/api/_/getAll` совпадает с `/api/v1/getAll` или `/api/v2/getAll` и даёт соответственно `/api/v1/getAll` или `/api/v2/getAll`. * `*` + Catch-all, совпадающий с нулём или более trailing-сегментов.   + Должен быть последним токеном шаблона.   + Пример: `/internal/*` совпадает с `/internal`, `/internal/service`, `/internal/service/operation/extra` и даёт `/internal/*`.  Примеры  * `/api/items/{id}` + Совпадения: `/api/items/1`, `/api/items/xyz`   + Не совпадения: `/api/items`, `/api/items/1/details` * `/api/_/getAll` + Совпадения: `/api/v1/getAll`, `/api/v2/getAll` * `/internal/*` + Совпадения с любым путём, начинающимся на `/internal`, на любой глубине.  Используйте эти шаблоны, чтобы заменить high-cardinality-части URL (ID, номера версий, глубокие внутренние пути) на placeholder'ы или catch-all-конструкции, сохраняя общую структуру эндпоинта узнаваемой. | Required |