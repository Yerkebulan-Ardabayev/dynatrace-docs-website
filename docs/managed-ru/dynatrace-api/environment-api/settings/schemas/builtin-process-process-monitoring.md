---
title: Settings API - Process group monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-process-monitoring
scraped: 2026-05-12T11:48:02.047094
---

# Settings API - Process group monitoring schema table

# Settings API - Process group monitoring schema table

* Published Dec 05, 2023

### Мониторинг process group (`builtin:process.process-monitoring)`

Dynatrace OneAgent автоматически мониторит все process group, обнаруженные в окружении (процессы, работающие во время установки OneAgent, должны быть перезапущены для запуска мониторинга).

OneAgent дополнительно предоставляет deep monitoring для всех процессов, которые он может мониторить на уровне request и PurePath.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process.process-monitoring` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.process-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process.process-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.process-monitoring` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить автоматический deep monitoring `autoMonitoring` | boolean | Отключив автоматический deep monitoring, Dynatrace OneAgent будет deep-мониторить только те процессы, которые покрыты соответствующим правилом deep monitoring или для которых мониторинг включён явно. Отключение работает, только если все установленные агенты имеют версию 1.123 или выше.  При включённом автоматическом мониторинге можно создавать правила, описывающие исключения из автоматического обнаружения и мониторинга процессов. При отключённом автоматическом мониторинге можно задавать правила, идентифицирующие конкретные процессы, которые надо мониторить. Правила применяются в том порядке, в котором они перечислены в настройках пользовательских и встроенных правил мониторинга процессов. Это позволяет конструировать сложные операции для тонкого контроля над процессами, мониторимыми в окружении. Например, можно задать правило включения, за которым следует правило исключения, покрывающее тот же процесс. После создания правила мониторинга можно включать и выключать в любой момент. Правила вступают в силу только после перезапуска соответствующих процессов. Альтернативно можно полностью отключить автоматический мониторинг и вместо этого задать правила "Include" для тех процессов, которые надо мониторить. | Required |