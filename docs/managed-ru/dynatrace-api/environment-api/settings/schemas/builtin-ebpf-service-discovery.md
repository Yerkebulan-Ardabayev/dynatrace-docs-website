---
title: Settings API - eBPF Service Discovery schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ebpf-service-discovery
scraped: 2026-05-12T11:43:11.470017
---

# Settings API - eBPF Service Discovery schema table

# Settings API - eBPF Service Discovery schema table

* Published Feb 26, 2024

### eBPF Service Discovery (`builtin:ebpf.service.discovery)`

Этот модуль OneAgent позволяет обнаруживать активные сервисы в сети. Это безопасный способ идентификации сервисов, требующих мониторинга, с минимальной нагрузкой.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ebpf.service.discovery` | * `group:network-and-discovery` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ebpf.service.discovery` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ebpf.service.discovery` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ebpf.service.discovery` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить обнаружение сервисов `ebpf` | boolean | Если отключено, Dynatrace может обнаруживать сервисы только в режиме Full Stack. | Required |