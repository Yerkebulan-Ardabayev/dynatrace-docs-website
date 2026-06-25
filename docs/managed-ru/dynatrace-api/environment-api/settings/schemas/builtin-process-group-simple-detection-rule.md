---
title: Settings API - Simple detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-simple-detection-rule
scraped: 2026-05-12T11:45:15.561974
---

# Settings API - Simple detection rules schema table

# Settings API - Simple detection rules schema table

* Published Dec 05, 2023

### Простые правила обнаружения (`builtin:process-group.simple-detection-rule)`

Простые правила обнаружения process group позволяют адаптировать логику обнаружения process group по умолчанию для глубокомониторимых процессов через **environment variables** или **Java system properties**. [More about custom process-group detection](https://dt-url.net/ty02won)

Примечание: правила обнаружения меняют состав, структуру и идентичность process group, а не только имя. Если нужно изменить только имя по умолчанию, используйте правила наименования (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`).

Правила обнаружения process group влияют только на процессы, которые глубокомониторятся Dynatrace OneAgent, и для применения изменений идентификации и группировки требуют перезапуска процессов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.simple-detection-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.simple-detection-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.simple-detection-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.simple-detection-rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Источник свойства `ruleType` | enum | Источник для разделения процессов на несколько process group. Возможные значения: * `prop` * `env` | Required |
| Идентификатор группы `groupIdentifier` | text | Если Dynatrace обнаружит это свойство при запуске процесса, он использует его значение для более детальной идентификации process group. | Required |
| Идентификатор инстанса `instanceIdentifier` | text | Используйте переменную для идентификации инстансов внутри process group.  Тип переменной такой же, как выбранный в 'Property source'. | Required |
| Ограничить это правило конкретными типами процессов `processType` | text | Примечание: не все типы могут быть обнаружены при запуске. | Optional |