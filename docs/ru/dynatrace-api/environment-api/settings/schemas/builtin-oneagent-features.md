---
title: Settings API - таблица схем функций OneAgent
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-features
scraped: 2026-03-06T21:19:41.477715
---

# Settings API — таблица схемы функций OneAgent


* Опубликовано 05 декабря 2023 г.

### Функции OneAgent (`builtin:oneagent.features`)

Dynatrace OneAgent придерживается подхода нулевой конфигурации. Поэтому при первом развёртывании OneAgent применяется набор функций по умолчанию. Когда с новыми версиями OneAgent появляются дополнительные функции, их можно активировать здесь, чтобы сделать доступными во всей вашей среде.

| Идентификатор схемы | Группы схем | Область действия |
| --- | --- | --- |
| `builtin:oneagent.features` | * `group:preferences` | `PROCESS_GROUP_INSTANCE` — Процесс  `PROCESS_GROUP` — Группа процессов  `CLOUD_APPLICATION` — Рабочая нагрузка Kubernetes  `CLOUD_APPLICATION_NAMESPACE` — Пространство имён Kubernetes  `KUBERNETES_CLUSTER` — Кластер Kubernetes  `environment` |

Получить схему через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия **Чтение настроек** (`settings.read`). Чтобы узнать, как его получить и использовать, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Обязательный |
| Инструментирование включено (изменение требует перезапуска процесса) `instrumentation` | boolean | - | Необязательный |
| Активировать эту функцию также в OneAgent, удовлетворяющих только минимальной версии Opt-In `forcible` | boolean | - | Необязательный |
| Функция `key` | text | - | Обязательный |
