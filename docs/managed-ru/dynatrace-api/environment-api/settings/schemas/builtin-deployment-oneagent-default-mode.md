---
title: Settings API - OneAgent default mode schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-oneagent-default-mode
scraped: 2026-05-12T11:47:04.655943
---

# Settings API - OneAgent default mode schema table

# Settings API - OneAgent default mode schema table

* Published Aug 05, 2024

### Режим OneAgent по умолчанию (`builtin:deployment.oneagent.default-mode)`

Вы можете настроить, какой [режим мониторинга](https://dt-url.net/8703q1z) OneAgent будет использоваться по умолчанию для команд установки OneAgent, предоставляемых в веб-интерфейсе Dynatrace. Это не влияет на поведение инсталлятора OneAgent. OneAgent, установленный без параметра режима мониторинга, будет работать в режиме Full-Stack Monitoring.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.oneagent.default-mode` | * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.default-mode` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.oneagent.default-mode` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.oneagent.default-mode` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Режим мониторинга OneAgent по умолчанию `defaultMode` | enum | Возможные значения: * `FULL_STACK` * `INFRASTRUCTURE` * `DISCOVERY` | Required |