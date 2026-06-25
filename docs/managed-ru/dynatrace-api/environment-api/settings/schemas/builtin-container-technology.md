---
title: Settings API - Container monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-container-technology
scraped: 2026-05-12T11:47:42.869431
---

# Settings API - Container monitoring schema table

# Settings API - Container monitoring schema table

* Published Dec 05, 2023

### Мониторинг контейнеров (`builtin:container.technology)`

Включайте и отключайте автоматическую инъекцию модулей кода в конкретные контейнеры.

Dynatrace OneAgent автоматически мониторит все процессы, запущенные на мониторимых хостах. В контейнерных окружениях (например, Kubernetes, OpenShift, Cloud Foundry или Docker) OneAgent автоматически инъецирует модули кода в контейнеризованные процессы, чтобы обеспечить full-stack-наблюдаемость «из коробки» для приложений, работающих внутри контейнеров. Включение auto-injection даёт deep monitoring для всех процессов в контейнерах на уровнях request и PurePath. При отключении OneAgent не будет инъецировать в контейнеры конкретного типа вообще. Dynatrace даёт полный контроль над автоматической инъекцией модулей кода в перечисленные ниже контейнерные технологии. Подробности см. [Supported container versions](https://dt-url.net/lmy0p0j "Visit Dynatrace support center").

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:container.technology` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.technology` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:container.technology` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.technology` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Контейнеры BOSH Process Manager (BPM) `boshProcessManager` | boolean | Платформа: Cloud Foundry  Статус: Released  ОС: Linux  Мин. версия агента: 1.159 | Required |
| Контейнеры Containerd `containerd` | boolean | Платформа: Kubernetes  Статус: Released  ОС: Linux  Мин. версия агента: 1.169 | Required |
| Контейнеры CRI-O `crio` | boolean | Платформа: Kubernetes  Статус: Released  ОС: Linux  Мин. версия агента: 1.163 | Required |
| Контейнеры Docker `docker` | boolean | Платформа: Docker и Kubernetes  Статус: Released  ОС: Linux | Required |
| Контейнеры Docker для Windows Server `dockerWindows` | boolean | Платформа: Docker  Статус: Early adopter  ОС: Windows  Мин. версия агента: 1.149 | Required |
| Контейнеры Garden `garden` | boolean | Платформа: Cloud Foundry  Статус: Released  ОС: Linux  Мин. версия агента: 1.133 | Required |
| Контейнеры Winc для Windows Server `winc` | boolean | Платформа: Cloud Foundry  Статус: Early adopter  ОС: Windows  Мин. версия агента: 1.175 | Required |
| Контейнеры Podman `podman` | boolean | Платформа: Podman  Статус: Released  ОС: Linux  Мин. версия агента: 1.267 | Required |