---
title: Settings API - Log module feature flags schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-agent-feature-flags
scraped: 2026-05-12T11:42:55.616291
---

# Settings API - Log module feature flags schema table

# Settings API - Log module feature flags schema table

* Published Mar 17, 2025

### Feature flags модуля логов (`builtin:logmonitoring.log-agent-feature-flags)`

Откройте новые возможности модуля Log в Dynatrace.

Подробнее см. [documentation](https://dt-url.net/ib22wr3).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-agent-feature-flags` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-feature-flags` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-agent-feature-flags` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-feature-flags` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Собирать все логи контейнеров `NewContainerLogDetector` | boolean | Разрешить OneAgent собирать все логи контейнеров в Kubernetes-окружениях. Эта настройка включает:  * Обнаружение и сбор логов с короткоживущих контейнеров и процессов в Kubernetes. * Обнаружение и сбор логов с любых процессов в контейнерах в Kubernetes. До сих пор модулем Log покрывались только процессы, обнаруженные OneAgent. * Декорирование log events согласно semantic dictionary.   **Примечание:** сопоставитель "Deployment name" в конфигурации источников лога будет игнорироваться, его надо заменить на "Workload name". Требуется **Dynatrace Operator 1.4.2+**.  Подробнее см. [documentation](https://dt-url.net/jn02ey0). | Required |
| Собирать логи Journald `JournaldLogDetector` | boolean | Разрешить OneAgent собирать логи из Journald на Linux-системах. Эта настройка включает:  * Обнаружение; для приёма логов требуется совпавшее правило ingest. | Required |
| Поддержка структурированных данных в Windows Event Logs `UserAndEventData` | boolean | Разрешить OneAgent собирать данные из Event Logs в секциях User Data и Event Data. | Required |
| Добавлять контекст IIS Application Pool в логи `PlainIISConfigurationDetector` | boolean | Разрешить OneAgent привязывать логи к соответствующим IIS application pool при однозначно определённой IIS-конфигурации. | Required |